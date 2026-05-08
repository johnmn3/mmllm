# milkmaid curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

### G1-01: Eval as substitution

- examples: 4
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 5, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'LOW_GROUNDING': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`0` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`"hello"` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`nil` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`nil` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`nil` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`nil` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-02: Integer numbers

- examples: 6
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 9, 'FORM_DISPLAY_AND_FORM_NOUN': 3, 'LOW_GROUNDING': 1, 'AS_ONE_WHO_CADENCE': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`7` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`-3` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`-3` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FOREIGN_FABLE_IMAGERY] form=`-3` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`-3` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FOREIGN_FABLE_IMAGERY] form=`0` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose

### G1-03: Ratios

- examples: 5
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 7, 'LOW_GROUNDING': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`1/2` — tortoise-hare-specific imagery 'leather notebook' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`1/2` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`3/4` — tortoise-hare-specific imagery 'leather notebook' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`(+ 1/2 1/4)` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(+ 1/2 1/4)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FOREIGN_FABLE_IMAGERY] form=`(+ 1/2 1/4)` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose

### G1-04: Strings

- examples: 5
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 6}
    - [FOREIGN_FABLE_IMAGERY] form=`"hello"` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`"hello"` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`"race"` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`"race"` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`"slow and steady"` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`""` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into milkmaid prose

### G1-05: Booleans

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'AS_ONE_WHO_CADENCE': 2, 'FOREIGN_FABLE_IMAGERY': 8, 'FORM_DISPLAY_AND_FORM_NOUN': 3}
    - [LOW_GROUNDING] form=`true` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [AS_ONE_WHO_CADENCE] form=`false` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [FOREIGN_FABLE_IMAGERY] form=`false` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`false` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`false` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`false` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-06: nil

- examples: 5
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 9, 'FORM_DISPLAY_AND_FORM_NOUN': 4, 'LOW_GROUNDING': 4}
    - [FOREIGN_FABLE_IMAGERY] form=`nil` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into milkmaid prose
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`nil` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FOREIGN_FABLE_IMAGERY] form=`(nil? nil)` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(nil? nil)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(nil? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(nil? nil)` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose

### G1-07: Keywords

- examples: 5
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 6, 'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`:hare` — tortoise-hare-specific imagery 'leather notebook' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`:hare` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`:hare` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FOREIGN_FABLE_IMAGERY] form=`:winner` — tortoise-hare-specific imagery 'leather notebook' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`(keyword? :hare)` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`(= :hare :hare)` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into milkmaid prose

### G1-08: Characters

- examples: 4
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 7, 'FORM_DISPLAY_AND_FORM_NOUN': 3, 'STRING_AS_CHAR_MISCLAIM': 6}
    - [FOREIGN_FABLE_IMAGERY] form=`\h` — tortoise-hare-specific imagery 'leather notebook' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`\h` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`\h` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FOREIGN_FABLE_IMAGERY] form=`\space` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`\space` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [STRING_AS_CHAR_MISCLAIM] form=`\space` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)

### G1-09: Symbols vs values

- examples: 4
- variety @ n=50: 0.99
- issues: {'PRONOUN_BEFORE_NAME': 4, 'LOW_GROUNDING': 8, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [PRONOUN_BEFORE_NAME] form=`(symbol? 'hare)` — sentence-initial 'She' appears before any named character is introduced
    - [LOW_GROUNDING] form=`(symbol? 'hare)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(symbol? 'hare)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(symbol? 42)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('48',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(symbol? 42)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('85',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(symbol? 42)` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G1-10: Comments

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'THE_FORM_OVERUSE': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'STORY_RESOLUTION_NO_DRAWN': 4}
    - [LOW_GROUNDING] form=`(+ 1 2) ; sum of one and two` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [THE_FORM_OVERUSE] form=`(+ 1 2) ; sum of one and two` — `the form` appears 6 times in user_msg (template tic — vary references)
    - [LOW_GROUNDING] form=`(+ 1 2) ; sum of one and two` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(+ 1 2) ; sum of one and two` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(+ 1 2) ; sum of one and two` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2) ; sum of one and two` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '8'), resolution doesn't close the loop)

### G1-11: Whitespace doesn't matter

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5, 'LOW_GROUNDING': 1, 'THE_FORM_OVERUSE': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+    1    2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(+    1    2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [THE_FORM_OVERUSE] form=`(+    1    2)` — `the form` appears 6 times in user_msg (template tic — vary references)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+    1    2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+
  1
  2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+
  1
  2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G1-12: Parens group; they don't multiply

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'PRONOUN_BEFORE_NAME': 1, 'THE_FORM_OVERUSE': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '3'), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(+ 2 3)` — sentence-initial 'She' appears before any named character is introduced
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '5'), resolution doesn't close the loop)
    - [THE_FORM_OVERUSE] form=`(+ 2 3)` — `the form` appears 6 times in user_msg (template tic — vary references)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* (+ 1 2) 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)

### G1-13: First arithmetic call

- examples: 6
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 18, 'AS_ONE_WHO_CADENCE': 2, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'ANSWER_LEAK': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '6'), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(+ 1 2)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(- 5 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(- 5 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '4'), resolution doesn't close the loop)

### G1-14: Nested call evaluation

- examples: 4
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1, 'STORY_RESOLUTION_NO_DRAWN': 12, 'PRONOUN_BEFORE_NAME': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [ANSWER_LEAK] form=`(+ 1 (* 2 3))` — answer 7 in narrative
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (* 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '4', '8'), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(+ 1 (* 2 3))` — sentence-initial 'She' appears before any named character is introduced
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (* 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (* 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '3', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* (+ 1 2) (+ 3 4))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '6'), resolution doesn't close the loop)

### G1-15: Equality

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 11, 'STORY_RESOLUTION_NO_DRAWN': 18, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 5, 'FORM_DISPLAY_AND_FORM_NOUN': 2, 'PRONOUN_BEFORE_NAME': 1}
    - [LOW_GROUNDING] form=`(= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= 1 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '9'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= 1 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '5'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(= 1 1)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(= 1 1)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G1-16: Numeric predicates

- examples: 6
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 14, 'PRONOUN_BEFORE_NAME': 2, 'CLAUSE_STACK_OVERFLOW': 1, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 1, 'AS_ONE_WHO_CADENCE': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(zero? 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(zero? 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(zero? 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(zero? 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(zero? 5)` — sentence-initial 'She' appears before any named character is introduced
    - [STORY_RESOLUTION_NO_DRAWN] form=`(pos? 7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)

### G1-17: Printing vs returning

- examples: 2
- variety @ n=50: 1.00
- issues: {'PRONOUN_BEFORE_NAME': 1, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'PROCEDURAL_OPENER': 2}
    - [PRONOUN_BEFORE_NAME] form=`42` — sentence-initial 'She' appears before any named character is introduced
    - [CAP_PRONOUN_MID_SENTENCE] form=`(+ 1 2)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(+ 1 2)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [PROCEDURAL_OPENER] form=`(+ 1 2)` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    - [CAP_PRONOUN_MID_SENTENCE] form=`(+ 1 2)` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(+ 1 2)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G1-18: Errors are safe in the REPL

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOWERCASE_CONCEPT_AFTER_PERIOD': 2, 'STORY_RESOLUTION_NO_DRAWN': 6, 'PRONOUN_BEFORE_NAME': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(+ 1 2)` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '5'), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(+ 1 2)` — sentence-initial 'She' appears before any named character is introduced
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(* 7 6)` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)

## Grade 2

### G2-01: Multi-arg arithmetic

- examples: 6
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 12, 'STORY_RESOLUTION_NO_DRAWN': 15, 'CLAUSE_STACK_OVERFLOW': 2, 'AS_ONE_WHO_CADENCE': 3, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(* 2 3 4)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 2 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '7', '9'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(* 2 3 4)` — sentence with 5 commas reads as AI-output cadence: 'Vespasia only shook her\nhead, stepping deliberately, one foot before the next, a'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(* 2 3 4)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 2 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '3'), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(* 2 3 4)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G2-02: Comparison chains

- examples: 5
- variety @ n=50: 1.00
- issues: {'AS_ONE_WHO_CADENCE': 2, 'NARRATIVE_NUMERAL_HARDCODE': 9, 'STORY_RESOLUTION_NO_DRAWN': 9, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'PRONOUN_BEFORE_NAME': 2}
    - [AS_ONE_WHO_CADENCE] form=`(< 1 2 3)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [AS_ONE_WHO_CADENCE] form=`(< 1 2 3)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(< 3 2 1)` — parametric example has hard-coded English numeral 'three piles' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(< 3 2 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '9', '7'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(< 3 2 1)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(< 3 2 1)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G2-03: not= and = with multiple args

- examples: 5
- variety @ n=50: 1.00
- issues: {'AS_ONE_WHO_CADENCE': 3, 'CLAUSE_STACK_OVERFLOW': 3, 'STORY_RESOLUTION_NO_DRAWN': 10, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [AS_ONE_WHO_CADENCE] form=`(not= 1 2)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [CLAUSE_STACK_OVERFLOW] form=`(not= 1 2)` — sentence with 6 commas reads as AI-output cadence: 'Theophilus only shook his\nhead, her breath even, her step even, her thought even'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not= 1 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not= 1 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not= 1 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= 1 1 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '5', '5'), resolution doesn't close the loop)

### G2-04: min and max

- examples: 5
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'AS_ONE_WHO_CADENCE': 2, 'NARRATIVE_NUMERAL_HARDCODE': 12, 'STORY_RESOLUTION_NO_DRAWN': 12, 'CLAUSE_STACK_OVERFLOW': 5}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(min 1 2 3)` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(min 1 2 3)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [AS_ONE_WHO_CADENCE] form=`(min 1 2 3)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(max 1 2 3)` — parametric example has hard-coded English numeral 'three piles' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(max 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '3'), resolution doesn't close the loop)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(max 1 2 3)` — parametric example has hard-coded English numeral 'three piles' in a story slot — the actual draws may differ from this fixed count

### G2-05: quot, rem, mod

- examples: 6
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 4, 'POST_COMMA_CAPITAL_PRONOUN': 4, 'PROCEDURAL_OPENER': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'STORY_RESOLUTION_NO_DRAWN': 15, 'AS_ONE_WHO_CADENCE': 2, 'PRONOUN_BEFORE_NAME': 4, 'ANSWER_LEAK': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(quot 17 5)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(quot 17 5)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [PROCEDURAL_OPENER] form=`(quot 17 5)` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    - [CLAUSE_STACK_OVERFLOW] form=`(quot 17 5)` — sentence with 6 commas reads as AI-output cadence: 'Theodoric only shook his\nhead, her breath even, her step even, her thought even,'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(rem 17 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '20'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(rem 17 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '19'), resolution doesn't close the loop)

### G2-06: inc and dec

- examples: 5
- variety @ n=50: 1.00
- issues: {'AS_ONE_WHO_CADENCE': 3, 'PRONOUN_BEFORE_NAME': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'STORY_RESOLUTION_NO_DRAWN': 7, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'LOW_GROUNDING': 1}
    - [AS_ONE_WHO_CADENCE] form=`(inc 5)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [PRONOUN_BEFORE_NAME] form=`(inc 5)` — sentence-initial 'She' appears before any named character is introduced
    - [AS_ONE_WHO_CADENCE] form=`(inc 5)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [CLAUSE_STACK_OVERFLOW] form=`(inc 5)` — sentence with 5 commas reads as AI-output cadence: 'Zerlina only shook her\nhead, stepping deliberately, one foot before the next, an'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(dec 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(dec 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)

### G2-07: Absolute value

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 11, 'CLAUSE_STACK_OVERFLOW': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(abs 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(abs 5)` — sentence with 5 commas reads as AI-output cadence: 'Euclid only shook his\nhead, her steps unhurried, her mind clear, and began sorti'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(abs 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(abs -5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-86',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(abs -5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-53',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(abs -5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-95',), resolution doesn't close the loop)

### G2-08: Arithmetic on ratios

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'AS_ONE_WHO_CADENCE': 3, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1/2 1/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(+ 1/2 1/4)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1/2 1/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1/2 1/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 2/3 3/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3', '4'), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(* 2/3 3/4)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G2-09: Floats vs ints (the / operator)

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'PRONOUN_BEFORE_NAME': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(/ 10 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '-15'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(/ 10 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '12'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(/ 10 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '17'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(/ 10 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(/ 10 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(/ 10 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)

### G2-10: Powers via repeated multiplication

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'ANSWER_LEAK': 2, 'CAP_PRONOUN_MID_SENTENCE': 4, 'POST_COMMA_CAPITAL_PRONOUN': 4, 'PARAGRAPH_FRAGMENTATION': 4, 'AS_ONE_WHO_CADENCE': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 2 2 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '7', '7'), resolution doesn't close the loop)
    - [ANSWER_LEAK] form=`(* 5 5)` — answer 25 in narrative
    - [CAP_PRONOUN_MID_SENTENCE] form=`(* 5 5)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(* 5 5)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 5 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '6'), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(* 5 5)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G2-11: String concatenation with str

- examples: 4
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 5, 'POST_COMMA_CAPITAL_PRONOUN': 5, 'STORY_RESOLUTION_NO_DRAWN': 12, 'PRONOUN_BEFORE_NAME': 2, 'PARAGRAPH_FRAGMENTATION': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'LOW_GROUNDING': 3}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(str "ab" "cd")` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(str "ab" "cd")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(str "ab" "cd")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('candle', 'bridge'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(str "ab" "cd")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('stone', 'stone'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(str "ab" "cd")` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(str "ab" "cd")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G2-12: print and println — return values

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'PRONOUN_BEFORE_NAME': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(println "hello")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('thistle',), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(println "hello")` — sentence-initial 'She' appears before any named character is introduced
    - [STORY_RESOLUTION_NO_DRAWN] form=`(println "hello")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('harbor',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(println "hello")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('thread',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(print "x")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('indigo',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(print "x")` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G2-13: and / or — short circuit, return values

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 12, 'POST_COMMA_CAPITAL_PRONOUN': 6, 'PRONOUN_BEFORE_NAME': 2, 'CAP_PRONOUN_MID_SENTENCE': 3, 'BOOL_LEAK_RESOLUTION': 1, 'PARAGRAPH_FRAGMENTATION': 2, 'NARRATIVE_NUMERAL_HARDCODE': 6, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(and true true)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(and true false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(and true false)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G2-14: not — turning truthy to false

- examples: 5
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 13, 'PRONOUN_BEFORE_NAME': 3, 'POST_COMMA_CAPITAL_PRONOUN': 4, 'CAP_PRONOUN_MID_SENTENCE': 2, 'BOOL_LEAK_RESOLUTION': 2, 'PARAGRAPH_FRAGMENTATION': 1, 'STORY_RESOLUTION_NO_DRAWN': 5}
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PRONOUN_BEFORE_NAME] form=`(not true)` — sentence-initial 'She' appears before any named character is introduced
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(not true)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-15: Falsey values: only false and nil

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 10, 'CAP_PRONOUN_MID_SENTENCE': 4, 'POST_COMMA_CAPITAL_PRONOUN': 6, 'LOW_GROUNDING': 3, 'PRONOUN_BEFORE_NAME': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if 0 1 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '5', '9'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(if 0 1 0)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(if 0 1 0)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if 0 1 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '4', '8'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(if 0 1 0)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(if 0 1 0)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G2-16: Truthy 0 and empty string

- examples: 4
- variety @ n=50: 1.00
- issues: {'POST_COMMA_CAPITAL_PRONOUN': 2, 'STORY_RESOLUTION_NO_DRAWN': 6, 'PRONOUN_BEFORE_NAME': 4, 'LOW_GROUNDING': 9}
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(boolean 0)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(boolean 0)` — sentence-initial 'She' appears before any named character is introduced
    - [LOW_GROUNDING] form=`(boolean "")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-17: Keyword as function for map lookup

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 9, 'STORY_RESOLUTION_NO_DRAWN': 9, 'PRONOUN_BEFORE_NAME': 2, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(:hare {:hare 1 :tortoise 2})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:hare {:hare 1 :tortoise 2})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '9', '7'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(:hare {:hare 1 :tortoise 2})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:hare {:hare 1 :tortoise 2})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '4', '6'), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(:hare {:hare 1 :tortoise 2})` — sentence-initial 'She' appears before any named character is introduced
    - [LOW_GROUNDING] form=`(:hare {:hare 1 :tortoise 2})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-18: Quoting symbols

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'PRONOUN_BEFORE_NAME': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'BOOL_LEAK_RESOLUTION': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'STORY_RESOLUTION_NO_DRAWN': 2}
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PRONOUN_BEFORE_NAME] form=`(symbol? (quote hare))` — sentence-initial 'She' appears before any named character is introduced
    - [LOW_GROUNDING] form=`(= (quote tortoise) 'tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(= (quote tortoise) 'tortoise)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(= (quote tortoise) 'tortoise)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G2-19: Auto-promotion to bigint

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 6, 'AS_ONE_WHO_CADENCE': 1, 'PRONOUN_BEFORE_NAME': 1, 'ANSWER_LEAK': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(* 1000000 1000000)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(* 1000000 1000000)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(* 1000000 1000000)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 1000000 1000000)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('1048576', '1048576'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 1000000 1000000)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10000000', '10000000'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(* 1000000 1000000)` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G2-20: Counting

- examples: 3
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 9, 'CLAUSE_STACK_OVERFLOW': 1, 'LOWERCASE_CONCEPT_AFTER_PERIOD': 3, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'PRONOUN_BEFORE_NAME': 3, 'DOUBLED_PLACE': 1}
    - [LOW_GROUNDING] form=`(count [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '17'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'That is how to\ncount the elements in the vector containing 1, 2, and 3 — walk th'
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(count [1 2 3])` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    - [LOW_GROUNDING] form=`(count [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '6', '13'), resolution doesn't close the loop)

### G2-21: String length and substring

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'SMALL_INT_LEAK': 1, 'PARAGRAPH_FRAGMENTATION': 1, 'PRONOUN_BEFORE_NAME': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('thread',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(count "tortoise")` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(count "tortoise")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('pewter',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('bridge',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('river',), resolution doesn't close the loop)

### G2-22: Compose pure arithmetic (multi-step calculation)

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 7, 'CLAUSE_STACK_OVERFLOW': 1, 'ANSWER_LEAK': 2, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(- (* 5 4) 7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '8'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(- (* 5 4) 7)` — sentence with 5 commas reads as AI-output cadence: '"To compute 7 times 8, then subtract 0, we must count — truly count, and the nes'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(- (* 5 4) 7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '7'), resolution doesn't close the loop)
    - [ANSWER_LEAK] form=`(+ (* 3 8) (* 2 4))` — answer 32 in narrative
    - [CAP_PRONOUN_MID_SENTENCE] form=`(+ (* 3 8) (* 2 4))` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(+ (* 3 8) (* 2 4))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

## Grade 3

### G3-01: def — top-level binding

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 42) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('89',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 42) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('49',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 42) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('61',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def y 7) y)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def y 7) y)` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (def y 7) y)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G3-02: def — redefinition

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'PRONOUN_BEFORE_NAME': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 1) (def x 99) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '58'), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(do (def x 1) (def x 99) x)` — sentence-initial 'She' appears before any named character is introduced
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 1) (def x 99) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('36',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 1) (def x 99) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '57'), resolution doesn't close the loop)

### G3-03: let — local binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 8, 'CLAUSE_STACK_OVERFLOW': 3, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 3] (+ x 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 3] (+ x 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '8'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(let [x 3] (+ x 1))` — sentence with 6 commas reads as AI-output cadence: 'She arrived with\na form, saying, "To bind a value of 5 to a local name x for one'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 3] (+ x 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [n 10] (* n n))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [n 10] (* n n))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17',), resolution doesn't close the loop)

### G3-04: let — multi-binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'CAP_PRONOUN_MID_SENTENCE': 4, 'POST_COMMA_CAPITAL_PRONOUN': 4, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'ANSWER_LEAK': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 1 b 2] (+ a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 1 b 2] (+ a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(let [a 1 b 2] (+ a b))` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(let [a 1 b 2] (+ a b))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 1 b 2] (+ a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 5 y 3] (- x y))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)

### G3-05: let — shadowing outer def

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 6, 'PARAGRAPH_FRAGMENTATION': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'AS_ONE_WHO_CADENCE': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def x 10) (let [x 99] x))` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (def x 10) (let [x 99] x))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (def x 10) (let [x 99] x))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 10) (let [x 99] x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '76'), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(do (def x 10) (let [x 99] x))` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 10) (let [x 99] x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('19', '30'), resolution doesn't close the loop)

### G3-06: let — binding can reference prior

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 1, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'ANSWER_LEAK': 2, 'PARAGRAPH_FRAGMENTATION': 1}
    - [LOW_GROUNDING] form=`(let [a 5 b (* a 2)] b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 5 b (* a 2)] b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(let [a 5 b (* a 2)] b)` — user_msg 213 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(let [a 5 b (* a 2)] b)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(let [a 5 b (* a 2)] b)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 5 b (* a 2)] b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)

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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [a b c] (+ a b c)) 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [a b c] (+ a b c)) 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [a b c] (+ a b c)) 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G3-09: defn — shorthand

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'ANSWER_LEAK': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'HIGH_LENGTH': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(do (defn dbl [x] (* x 2)) (dbl 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn dbl [x] (* x 2)) (dbl 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn dbl [x] (* x 2)) (dbl 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn dbl [x] (* x 2)) (dbl 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '9'), resolution doesn't close the loop)
    - [ANSWER_LEAK] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — answer 6 in narrative
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'PRONOUN_BEFORE_NAME': 1, 'HIGH_LENGTH': 2, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(+ % 1) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(#(+ % 1) 5)` — sentence-initial 'She' appears before any named character is introduced
    - [HIGH_LENGTH] form=`(#(+ % 1) 5)` — user_msg 221 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(#(+ % 1) 5)` — ', He wrote…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(#(+ % 1) 5)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(+ % 1) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)

### G3-11: Substitution rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 4, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(let [a 7] (+ a a))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [a 7] (+ a a))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 7] (+ a a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (* x x)) 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (* x x)) 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`((fn [x] (* x x)) 6)` — sentence with 5 commas reads as AI-output cadence: 'He arrived with\na form, saying, "To apply a function that squares its argument t'

### G3-12: Scope vs namespace

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'PRONOUN_BEFORE_NAME': 2, 'HIGH_LENGTH': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def g 5) (let [g 99] (+ g 1)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '46', '7'), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(do (def g 5) (let [g 99] (+ g 1)))` — sentence-initial 'She' appears before any named character is introduced
    - [HIGH_LENGTH] form=`(do (def g 5) (let [g 99] (+ g 1)))` — user_msg 213 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def g 5) (let [g 99] (+ g 1)))` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (def g 5) (let [g 99] (+ g 1)))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def g 5) (let [g 99] (+ g 1)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('58',), resolution doesn't close the loop)

### G3-13: fn body returns last form

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`((fn [x] x x x 99) 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] x x x 99) 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`((fn [x] x x x 99) 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] x x x 99) 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`((fn [x] x x x 99) 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] x x x 99) 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99',), resolution doesn't close the loop)

### G3-14: do form

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'PRONOUN_BEFORE_NAME': 2, 'THE_FORM_OVERUSE': 3}
    - [LOW_GROUNDING] form=`(do 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '4', '8'), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(do 1 2 3)` — sentence-initial 'She' appears before any named character is introduced
    - [LOW_GROUNDING] form=`(do 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '3'), resolution doesn't close the loop)
    - [THE_FORM_OVERUSE] form=`(do 1 2 3)` — `the form` appears 6 times in user_msg (template tic — vary references)

### G3-15: Side-effects in body

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(do (println "hi") 42)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (println "hi") 42)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('94', 'ochre'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (println "hi") 42)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (println "hi") 42)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('35', 'cobalt'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(do (println "hi") 42)` — user_msg 201 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (println "hi") 42)` — ', He wrote…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G3-16: Name collision: namespace vs let

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(let [+ 99] +)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [+ 99] +)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('74',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(let [+ 99] +)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [+ 99] +)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('73',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(let [+ 99] +)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [+ 99] +)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('76',), resolution doesn't close the loop)

### G3-17: Naming conventions (kebab-case)

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [hare-speed 4 tortoise-speed 1] (- hare-speed` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [hare-speed 4 tortoise-speed 1] (- hare-speed` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [hare-speed 4 tortoise-speed 1] (- hare-speed` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)

### G3-18: When to name vs inline

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 4, 'LOW_GROUNDING': 1, 'AS_ONE_WHO_CADENCE': 1, 'PRONOUN_BEFORE_NAME': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [n 5] (* n n n))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(let [n 5] (* n n n))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [n 5] (* n n n))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(* 5 5 5)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 5 5 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '8', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 5 5 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '6', '6'), resolution doesn't close the loop)

## Grade 4

### G4-01: Vector literal

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 9, 'STORY_RESOLUTION_NO_DRAWN': 6, 'PRONOUN_BEFORE_NAME': 1, 'FORM_LEAK': 2, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [LOW_GROUNDING] form=`[1 2 3]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`[1 2 3]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '12', '19'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`[1 2 3]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`[1 2 3]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '14', '5'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`[1 2 3]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`[1 2 3]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '16', '11'), resolution doesn't close the loop)

### G4-02: nth — vector access

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 4}
    - [CLAUSE_STACK_OVERFLOW] form=`(nth [10 20 30] 0)` — sentence with 6 commas reads as AI-output cadence: 'To get the element at index 0 of a vector containing 10, 20, and 30, produce a f'
    - [LOW_GROUNDING] form=`(nth [10 20 30] 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(nth [10 20 30] 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '4', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(nth [10 20 30] 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '19', '3'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(nth [10 20 30] 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(nth [10 20 30] 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '14'), resolution doesn't close the loop)

### G4-03: conj — append to vector

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 5, 'FORM_LEAK': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(conj [1 2] 3)` — parametric example has hard-coded English numeral 'three items' in a story slot — the actual draws may differ from this fixed count
    - [LOW_GROUNDING] form=`(conj [1 2] 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(conj [1 2] 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '17', '6'), resolution doesn't close the loop)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(conj [1 2] 3)` — parametric example has hard-coded English numeral 'three items' in a story slot — the actual draws may differ from this fixed count
    - [LOW_GROUNDING] form=`(conj [1 2] 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(conj [1 2] 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '15'), resolution doesn't close the loop)

### G4-04: List literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 2, 'AS_ONE_WHO_CADENCE': 1, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 3, 'PARAGRAPH_FRAGMENTATION': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three items' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '14', '7'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`'(1 2 3)` — sentence with 6 commas reads as AI-output cadence: 'To create a list containing 1, 2, and 3, produce a form that builds a new basket'
    - [AS_ONE_WHO_CADENCE] form=`'(1 2 3)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [CAP_PRONOUN_MID_SENTENCE] form=`'(1 2 3)` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`'(1 2 3)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G4-05: cons — prepend to seq

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'PARAMETRIC_LITERAL_NUMERALS': 3, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 1}
    - [HIGH_LENGTH] form=`(cons 0 '(1 2 3))` — user_msg 203 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(cons 0 '(1 2 3))` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(cons 0 '(1 2 3))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(cons 0 '(1 2 3))` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(cons 0 '(1 2 3))` — parametric example has hard-coded English numeral 'four items' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cons 0 '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '9', '19'), resolution doesn't close the loop)

### G4-06: Map literal

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`{:hare 1 :tortoise 2}` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '3', '19'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`{:hare 1 :tortoise 2}` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '12', '12'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`{:hare 1 :tortoise 2}` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`{:hare 1 :tortoise 2}` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '3', '20'), resolution doesn't close the loop)

### G4-07: get — map lookup

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [LOW_GROUNDING] form=`(get {:a 1 :b 2} :a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(get {:a 1 :b 2} :a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '5', '15'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(get {:a 1 :b 2} :a)` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(get {:a 1 :b 2} :a)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(get {:a 1 :b 2} :a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(get {:a 1 :b 2} :a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '19', ':elderberry'), resolution doesn't close the loop)

### G4-08: assoc — map update

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 2, 'HIGH_LENGTH': 1, 'FORM_LEAK': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(assoc {:a 1} :b 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '20', '3'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(assoc {:a 1} :b 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(assoc {:a 1} :b 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '16', '12'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(assoc {:a 1} :b 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(assoc {:a 1} :b 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('19', '9', ':quince'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(assoc {:a 1} :a 99)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '19', '87'), resolution doesn't close the loop)

### G4-09: dissoc — map remove key

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 2, 'PRONOUN_BEFORE_NAME': 1, 'FORM_LEAK': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(dissoc {:a 1 :b 2} :a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(dissoc {:a 1 :b 2} :a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '10', '3'), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(dissoc {:a 1 :b 2} :a)` — sentence-initial 'She' appears before any named character is introduced
    - [FORM_LEAK] form=`(dissoc {:a 1 :b 2} :a)` — form '(dissoc {:a 1 :b 2} :a)' appears in user_msg of a goal-style subject
    - [CAP_PRONOUN_MID_SENTENCE] form=`(dissoc {:a 1 :b 2} :a)` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(dissoc {:a 1 :b 2} :a)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G4-10: keys and vals

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'LOW_GROUNDING': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (keys {:a 1 :b 2 :c 3}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '7', ':grape'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(count (keys {:a 1 :b 2 :c 3}))` — sentence with 6 commas reads as AI-output cadence: 'To count how many keys are in a map binding :a, :b, and :c, produce a form that '
    - [LOW_GROUNDING] form=`(count (keys {:a 1 :b 2 :c 3}))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count (keys {:a 1 :b 2 :c 3}))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-11: Set literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'HIGH_LENGTH': 1}
    - [LOW_GROUNDING] form=`(count #{1 2 3})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count #{1 2 3})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '16', '18'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count #{1 2 3})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '18', '15'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(count #{1 2 3})` — sentence with 6 commas reads as AI-output cadence: 'To count the elements in a set containing 1, 2, and 3, produce a form that build'
    - [CAP_PRONOUN_MID_SENTENCE] form=`(count #{1 2 3})` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(count #{1 2 3})` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G4-12: Set membership

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 6, 'PRONOUN_BEFORE_NAME': 2, 'CLAUSE_STACK_OVERFLOW': 2, 'FORM_LEAK': 2, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [LOW_GROUNDING] form=`(contains? #{1 2 3} 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(contains? #{1 2 3} 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('11', '7', '15'), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(contains? #{1 2 3} 2)` — sentence-initial 'She' appears before any named character is introduced
    - [STORY_RESOLUTION_NO_DRAWN] form=`(contains? #{1 2 3} 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '4', '4'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(contains? #{1 2 3} 2)` — sentence with 6 commas reads as AI-output cadence: 'To check whether 2 is a member of a set containing 1, 2, and 3, produce a form t'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(contains? #{1 2 3} 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '16', '8'), resolution doesn't close the loop)

### G4-13: count — universal

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 9, 'STORY_RESOLUTION_NO_DRAWN': 12, 'CLAUSE_STACK_OVERFLOW': 3, 'AS_ONE_WHO_CADENCE': 1}
    - [LOW_GROUNDING] form=`(count [1 2 3 4 5])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3 4 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '15', '15'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3 4 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '12', '18'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3 4 5])` — sentence with 8 commas reads as AI-output cadence: 'To count the elements in a vector containing 1, 2, 3, 4, and 5, produce a form t'
    - [LOW_GROUNDING] form=`(count [1 2 3 4 5])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3 4 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '19', '7'), resolution doesn't close the loop)

### G4-14: empty?

- examples: 3
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 7, 'STORY_RESOLUTION_NO_DRAWN': 9, 'PRONOUN_BEFORE_NAME': 1, 'FORM_LEAK': 2, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [LOW_GROUNDING] form=`(empty? [])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(empty? [])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '18', '3'), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(empty? [])` — sentence-initial 'She' appears before any named character is introduced
    - [STORY_RESOLUTION_NO_DRAWN] form=`(empty? [])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '18', '4'), resolution doesn't close the loop)
    - [FORM_LEAK] form=`(empty? [])` — form '(empty? [])' appears in user_msg of a goal-style subject
    - [CAP_PRONOUN_MID_SENTENCE] form=`(empty? [])` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G4-15: first, rest, last

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 8, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(first [10 20 30])` — sentence with 6 commas reads as AI-output cadence: 'To get the first element of a vector containing 10, 20, and 30, produce a form t'
    - [LOW_GROUNDING] form=`(first [10 20 30])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first [10 20 30])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '13', '18'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(first [10 20 30])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first [10 20 30])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('11', '14', '15'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(last [10 20 30])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '7', '8'), resolution doesn't close the loop)

### G4-16: into and conj on collections

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'AS_ONE_WHO_CADENCE': 1, 'LOW_GROUNDING': 4, 'PRONOUN_BEFORE_NAME': 1, 'FORM_LEAK': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(into [] '(1 2 3))` — parametric example has hard-coded English numeral 'three elements' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '12', '8'), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(into [] '(1 2 3))` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(into [] '(1 2 3))` — parametric example has hard-coded English numeral 'three elements' in a story slot — the actual draws may differ from this fixed count
    - [LOW_GROUNDING] form=`(into [] '(1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '18', '16'), resolution doesn't close the loop)

### G4-17: Immutability — assoc returns new

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(let [m {:a 1}] (assoc m :a 99) m)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :a 99) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '9', '7'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(let [m {:a 1}] (assoc m :a 99) m)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :a 99) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '6', '41'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(let [m {:a 1}] (assoc m :a 99) m)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :a 99) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('19', '4', '9'), resolution doesn't close the loop)

### G4-18: Equality of vectors and lists

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(= [1 2 3] '(1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= [1 2 3] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '8', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= [1 2 3] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '13', '8'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(= [1 2 3] '(1 2 3))` — sentence with 6 commas reads as AI-output cadence: 'To test whether a vector with elements 1, 2, 3 equals a list with the same eleme'
    - [LOW_GROUNDING] form=`(= [1 2 3] '(1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= [1 2 3] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '16', '5'), resolution doesn't close the loop)

### G4-19: range and seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'STORY_RESOLUTION_NO_DRAWN': 5, 'CLAUSE_STACK_OVERFLOW': 2, 'LOW_GROUNDING': 1, 'PRONOUN_BEFORE_NAME': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(count (range 5))` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(count (range 5))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (range 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(count (range 5))` — sentence with 5 commas reads as AI-output cadence: 'The milkmaid walked the market road, counting off each milestone: 0, 1, 2, 3, 4'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (range 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(count (range 5))` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G4-20: Collection vs sequence

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [LOW_GROUNDING] form=`(count (seq [1 2 3]))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (seq [1 2 3]))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '17'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count (seq [1 2 3]))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (seq [1 2 3]))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '6', '13'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(count (seq [1 2 3]))` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(count (seq [1 2 3]))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

## Grade 5

### G5-01: if

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOWERCASE_CONCEPT_AFTER_PERIOD': 2, 'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 9, 'CAP_PRONOUN_MID_SENTENCE': 4, 'POST_COMMA_CAPITAL_PRONOUN': 4, 'PRONOUN_BEFORE_NAME': 1}
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(if true :a :b)` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    - [LOW_GROUNDING] form=`(if true :a :b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if true :a :b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':east', ':x'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if true :a :b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':third', ':b'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(if true :a :b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if true :a :b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':left', ':slow'), resolution doesn't close the loop)

### G5-02: if as expression

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOWERCASE_CONCEPT_AFTER_PERIOD': 3, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(+ 1 (if true 10 20))` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (if true 10 20))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '10', '3'), resolution doesn't close the loop)
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(+ 1 (if true 10 20))` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (if true 10 20))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '7', '13'), resolution doesn't close the loop)
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(+ 1 (if true 10 20))` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (if true 10 20))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '14'), resolution doesn't close the loop)

### G5-03: when

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'LOWERCASE_CONCEPT_AFTER_PERIOD': 1}
    - [LOW_GROUNDING] form=`(when true :yes)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true :yes)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':alpha',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(when true :yes)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true :yes)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':b',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(when true :yes)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true :yes)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':alpha',), resolution doesn't close the loop)

### G5-04: cond

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '6', '7'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '7', '7'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G5-05: cond — :else

- examples: 1
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(cond false :a false :b :else :c)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(cond false :a false :b :else :c)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(cond false :a false :b :else :c)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(cond false :a false :b :else :c)` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(cond false :a false :b :else :c)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G5-06: case

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOWERCASE_CONCEPT_AFTER_PERIOD': 3, 'LOW_GROUNDING': 1, 'STORY_RESOLUTION_NO_DRAWN': 6, 'PRONOUN_BEFORE_NAME': 1}
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(case 2 1 :one 2 :two 3 :three :default)` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    - [LOW_GROUNDING] form=`(case 2 1 :one 2 :two 3 :three :default)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(case 2 1 :one 2 :two 3 :three :default)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '6', ':c'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(case 2 1 :one 2 :two 3 :three :default)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '9', '5'), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(case 2 1 :one 2 :two 3 :three :default)` — sentence-initial 'She' appears before any named character is introduced
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(case 2 1 :one 2 :two 3 :three :default)` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)

### G5-07: and / or as control flow

- examples: 2
- variety @ n=50: 1.00
- issues: {'POST_COMMA_CAPITAL_PRONOUN': 4, 'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CAP_PRONOUN_MID_SENTENCE': 3, 'DOUBLED_PLACE': 1}
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(and 1 2 3)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(and 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(and 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(and 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(and 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '8', '9'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(and 1 2 3)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G5-08: not

- examples: 1
- variety @ n=50: 1.00
- issues: {'POST_COMMA_CAPITAL_PRONOUN': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(not (> 1 2))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not (> 1 2))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not (> 1 2))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(not (> 1 2))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not (> 1 2))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '5'), resolution doesn't close the loop)

### G5-09: fn as value

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [f x] (f (f x))) inc 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [f x] (f (f x))) inc 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`((fn [f x] (f (f x))) inc 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [f x] (f (f x))) inc 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)

### G5-10: map

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'STORY_RESOLUTION_NO_DRAWN': 6, 'PRONOUN_BEFORE_NAME': 2, 'HIGH_LENGTH': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(map inc [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map inc [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '20', '7'), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(map inc [1 2 3])` — sentence-initial 'She' appears before any named character is introduced
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map inc [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '5', '12'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map inc [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '3', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map #(* % %) [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)

### G5-11: filter

- examples: 2
- variety @ n=50: 1.00
- issues: {'PARAMETRIC_LITERAL_NUMERALS': 3, 'NARRATIVE_NUMERAL_HARDCODE': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 5, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'CLAUSE_STACK_OVERFLOW': 3}
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(filter even? [1 2 3 4])` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(filter even? [1 2 3 4])` — parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(filter even? [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '16', '18'), resolution doesn't close the loop)
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(filter even? [1 2 3 4])` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(filter even? [1 2 3 4])` — parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    - [LOW_GROUNDING] form=`(filter even? [1 2 3 4])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G5-12: reduce

- examples: 3
- variety @ n=50: 0.97
- issues: {'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 9, 'PRONOUN_BEFORE_NAME': 2, 'CLAUSE_STACK_OVERFLOW': 8, 'HIGH_LENGTH': 3, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'PARAMETRIC_LITERAL_NUMERALS': 3, 'LOWERCASE_CONCEPT_AFTER_PERIOD': 2}
    - [LOW_GROUNDING] form=`(reduce + [1 2 3 4])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce + [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('11', '7', '15'), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(reduce + [1 2 3 4])` — sentence-initial 'She' appears before any named character is introduced
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + [1 2 3 4])` — sentence with 8 commas reads as AI-output cadence: 'To walk the row of pebbles 1, 2, 3, 4 carrying a tally that combines each with +'
    - [HIGH_LENGTH] form=`(reduce + [1 2 3 4])` — user_msg 203 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(reduce + [1 2 3 4])` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G5-13: reduce with init

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 2, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce + 100 [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('506', '15', '15'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + 100 [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'That is how to\nfold + over the vector containing 1, 2, 3 starting from an initia'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce + 100 [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('254', '12', '18'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + 100 [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'To fold + over the vector containing 1, 2, 3 starting from an initial accumulato'
    - [CAP_PRONOUN_MID_SENTENCE] form=`(reduce + 100 [1 2 3])` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(reduce + 100 [1 2 3])` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G5-14: apply

- examples: 2
- variety @ n=50: 1.00
- issues: {'PARAMETRIC_LITERAL_NUMERALS': 3, 'NARRATIVE_NUMERAL_HARDCODE': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'PRONOUN_BEFORE_NAME': 1, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(apply + [1 2 3 4])` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply + [1 2 3 4])` — parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(apply + [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '18', '3'), resolution doesn't close the loop)
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(apply + [1 2 3 4])` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply + [1 2 3 4])` — parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(apply + [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '18', '4'), resolution doesn't close the loop)

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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'LOW_GROUNDING': 2, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`((partial + 10) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((partial + 10) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((partial + 10) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '5'), resolution doesn't close the loop)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(map (partial * 3) [1 2 3])` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map (partial * 3) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '6', '9'), resolution doesn't close the loop)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(map (partial * 3) [1 2 3])` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count

### G5-17: juxt

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`((juxt inc dec) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((juxt inc dec) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((juxt inc dec) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)

### G5-18: some

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 2, 'AS_ONE_WHO_CADENCE': 1, 'PARAMETRIC_LITERAL_NUMERALS': 3, 'LOW_GROUNDING': 2}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(some even? [1 3 5 8 7])` — parametric example has hard-coded English numeral 'five counts' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(some even? [1 3 5 8 7])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '8', '6'), resolution doesn't close the loop)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(some even? [1 3 5 8 7])` — parametric example has hard-coded English numeral 'five counts' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(some even? [1 3 5 8 7])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '13', '8'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(some even? [1 3 5 8 7])` — sentence with 5 commas reads as AI-output cadence: '"To\ncheck if any element in the vector containing 1, 3, 5, 8, and 7 is even, sub'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(some even? [1 3 5 8 7])` — parametric example has hard-coded English numeral 'five counts' in a story slot — the actual draws may differ from this fixed count

### G5-19: every?

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'BOOL_LEAK_RESOLUTION': 2, 'PARAMETRIC_LITERAL_NUMERALS': 6, 'NARRATIVE_NUMERAL_HARDCODE': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 2, 'LOW_GROUNDING': 3, 'AS_ONE_WHO_CADENCE': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(every? pos? [1 2 3])` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(every? pos? [1 2 3])` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [BOOL_LEAK_RESOLUTION] form=`(every? pos? [1 2 3])` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(every? pos? [1 2 3])` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(every? pos? [1 2 3])` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(every? pos? [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '3', '10'), resolution doesn't close the loop)

### G5-20: take and drop

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 5, 'AS_ONE_WHO_CADENCE': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'PRONOUN_BEFORE_NAME': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(take 3 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'five counts' in a story slot — the actual draws may differ from this fixed count
    - [LOW_GROUNDING] form=`(take 3 [10 20 30 40 50])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(take 3 [10 20 30 40 50])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '17', '7'), resolution doesn't close the loop)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(take 3 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'five counts' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(take 3 [10 20 30 40 50])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '18', '16'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(take 3 [10 20 30 40 50])` — sentence with 5 commas reads as AI-output cadence: 'But she must write it —\nthe farmer\'s form, not the milkmaid\'s guess."\n\nQuestion:'

### G5-21: distinct and sort

- examples: 2
- variety @ n=50: 1.00
- issues: {'PARAMETRIC_LITERAL_NUMERALS': 3, 'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 6, 'PRONOUN_BEFORE_NAME': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'AS_ONE_WHO_CADENCE': 1}
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(distinct [1 1 2 3 3 4])` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [LOW_GROUNDING] form=`(distinct [1 1 2 3 3 4])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(distinct [1 1 2 3 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '14', '15'), resolution doesn't close the loop)
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(distinct [1 1 2 3 3 4])` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [LOW_GROUNDING] form=`(distinct [1 1 2 3 3 4])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(distinct [1 1 2 3 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '6'), resolution doesn't close the loop)

### G5-22: recur — first taste

- examples: 1
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [HIGH_LENGTH] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — user_msg 205 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)

## Grade 6

### G6-01: Namespace as file

- examples: 3
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 9, 'CAP_PRONOUN_MID_SENTENCE': 4, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'CONCEPT_AS_VERB': 1, 'PRONOUN_BEFORE_NAME': 1}
    - [LOW_GROUNDING] form=`(name 'foo.bar)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(name 'foo.bar)` — ', He brought…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [LOW_GROUNDING] form=`(name 'foo.bar)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(name 'foo.bar)` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(name 'foo.bar)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(name 'foo.bar)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-02: ns form

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'PRONOUN_BEFORE_NAME': 2, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(name 'race.tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PRONOUN_BEFORE_NAME] form=`(name 'race.tortoise)` — sentence-initial 'She' appears before any named character is introduced
    - [CAP_PRONOUN_MID_SENTENCE] form=`(name 'race.tortoise)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(name 'race.tortoise)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(name 'race.tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name 'race.tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-03: require

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CONCEPT_AS_VERB': 1, 'CAP_PRONOUN_MID_SENTENCE': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('harbor',), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`(clojure.string/upper-case "hare")` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('river',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(clojure.string/upper-case "hare")` — ', He brought…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('harbor',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(clojure.string/lower-case "ZEBRA")` — ', He brought…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G6-04: refer and use

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(= (clojure.string/upper-case "x") (clojure.string` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= (clojure.string/upper-case "x") (clojure.string` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('lichen', 'lichen'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(= (clojure.string/upper-case "x") (clojure.string` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(= (clojure.string/upper-case "x") (clojure.string` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(= (clojure.string/upper-case "x") (clojure.string` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= (clojure.string/upper-case "x") (clojure.string` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('pewter', 'pewter'), resolution doesn't close the loop)

### G6-05: Fully qualified names

- examples: 4
- variety @ n=50: 0.99
- issues: {'CAP_PRONOUN_MID_SENTENCE': 6, 'POST_COMMA_CAPITAL_PRONOUN': 5, 'STORY_RESOLUTION_NO_DRAWN': 12, 'CONCEPT_AS_VERB': 2, 'LOW_GROUNDING': 6}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(clojure.string/upper-case "hello")` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(clojure.string/upper-case "hello")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "hello")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('bridge',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(clojure.string/upper-case "hello")` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(clojure.string/upper-case "hello")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "hello")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('stone',), resolution doesn't close the loop)

### G6-06: Private defs

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'PRONOUN_BEFORE_NAME': 2, 'CONCEPT_AS_VERB': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:private (meta '^:private x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private', ':private'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:private (meta '^:private x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private', ':private'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:private (meta '^:private x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private', ':private'), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(:private (meta '^:private x))` — sentence-initial 'She' appears before any named character is introduced
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:private (meta 'x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private',), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`(:private (meta 'x))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G6-07: Public vs private API

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 3, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CONCEPT_AS_VERB': 1, 'PRONOUN_BEFORE_NAME': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(boolean (:private (meta '^:private hidden)))` — ', He brought…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta '^:private hidden)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private', ':private'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(boolean (:private (meta '^:private hidden)))` — ', She brought…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta '^:private hidden)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private', ':private'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(boolean (:private (meta '^:private hidden)))` — ', She brought…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta '^:private hidden)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private', ':private'), resolution doesn't close the loop)

### G6-08: Circular dependencies

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CONCEPT_AS_VERB': 2, 'PRONOUN_BEFORE_NAME': 4}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(clojure.string/upper-case "a")` — ', He brought…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [LOW_GROUNDING] form=`(clojure.string/upper-case "a")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "a")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('myrtle',), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`(clojure.string/upper-case "a")` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(clojure.string/upper-case "a")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "a")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('saffron',), resolution doesn't close the loop)

### G6-09: Loading order

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 5, 'PRONOUN_BEFORE_NAME': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'HIGH_LENGTH': 1, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '6'), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — sentence-initial 'She' appears before any named character is introduced
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '9'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — sentence with 5 commas reads as AI-output cadence: 'To define step1 as 1, then define step2 as step1 plus 1, then return step2, writ'

### G6-10: Leiningen and deps.edn

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 4, 'LOW_GROUNDING': 3, 'HEDGING_NEAR_FORM': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(:deps {:deps {:a 1 :b 2}})` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`(:deps {:deps {:a 1 :b 2}})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(:deps {:deps {:a 1 :b 2}})` — tortoise-hare-specific imagery 'leather notebook' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`(:deps {:deps {:a 1 :b 2}})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(:deps {:deps {:a 1 :b 2}})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(:deps {:deps {:a 1 :b 2}})` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value

### G6-11: Classpath

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'HEDGING_NEAR_FORM': 1}
    - [LOW_GROUNDING] form=`(clojure.string/split "src:test" #":")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(clojure.string/split "src:test" #":")` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [LOW_GROUNDING] form=`(count ["src" "test" "resources"])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-12: Multiple files in one project

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'PRONOUN_BEFORE_NAME': 1, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(count ['race.tortoise 'race.hare 'race.shared])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PRONOUN_BEFORE_NAME] form=`(count ['race.tortoise 'race.hare 'race.shared])` — sentence-initial 'She' appears before any named character is introduced
    - [CAP_PRONOUN_MID_SENTENCE] form=`(count ['race.tortoise 'race.hare 'race.shared])` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(count ['race.tortoise 'race.hare 'race.shared])` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(count ['race.tortoise 'race.hare 'race.shared])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(count ['race.tortoise 'race.hare 'race.shared])` — ', She brought…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G6-13: Aliasing conventions

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CAP_PRONOUN_MID_SENTENCE': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [s clojure.string/upper-case] (s "hare"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('amber',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [s clojure.string/upper-case] (s "hare"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('topaz',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(let [s clojure.string/upper-case] (s "hare"))` — ', She brought…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [s clojure.string/upper-case] (s "hare"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('pewter',), resolution doesn't close the loop)

### G6-14: Import for host classes

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'PRONOUN_BEFORE_NAME': 1, 'CONCEPT_AS_VERB': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(symbol? 'java.util.List)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PRONOUN_BEFORE_NAME] form=`(symbol? 'java.util.List)` — sentence-initial 'She' appears before any named character is introduced
    - [LOW_GROUNDING] form=`(symbol? 'java.util.List)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(symbol? 'java.util.List)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name 'java.util.Map)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(name 'java.util.Map)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G6-15: Namespace meta

- examples: 2
- variety @ n=50: 0.99
- issues: {'CONCEPT_AS_VERB': 2, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [CONCEPT_AS_VERB] form=`(:doc (meta '\{:doc "steady wins"\} race))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:doc (meta '\{:doc "steady wins"\} race))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':doc', ':doc', 'steady wins'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:doc (meta '\{:doc "steady wins"\} race))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':doc', ':doc', 'steady wins'), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`(:doc (meta '\{:doc "steady wins"\} race))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:doc (meta '\{:doc "steady wins"\} race))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':doc', ':doc', 'steady wins'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:author (meta '\{:author "Aesop"\} race))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':author', ':author', 'Aesop'), resolution doesn't close the loop)

### G6-16: Cleaning up requires

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'LOW_GROUNDING': 6, 'PRONOUN_BEFORE_NAME': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(contains? #{'clojure.string} 'clojure.string)` — ', She brought…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.string)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.string)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PRONOUN_BEFORE_NAME] form=`(contains? #{'clojure.string} 'clojure.string)` — sentence-initial 'She' appears before any named character is introduced
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.string)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.set)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 7

### G7-01: throw

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(try (throw (Exception. "bad")) (catch Exception e` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "bad")) (catch Exception e` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1', 'bad'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(try (throw (Exception. "bad")) (catch Exception e` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "bad")) (catch Exception e` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1', 'bad'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(try (throw (Exception. "bad")) (catch Exception e` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(try (throw (Exception. "bad")) (catch Exception e` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G7-02: try / catch

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'PRONOUN_BEFORE_NAME': 3, 'LOW_GROUNDING': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (/ 1 0) (catch Exception e -1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '4', '-6'), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(try (/ 1 0) (catch Exception e -1))` — sentence-initial 'She' appears before any named character is introduced
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (/ 1 0) (catch Exception e -1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-23',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (/ 1 0) (catch Exception e -1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '4', '-35'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(try 42 (catch Exception e :caught))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try 42 (catch Exception e :caught))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('33', ':gamma'), resolution doesn't close the loop)

### G7-03: try / finally

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'PRONOUN_BEFORE_NAME': 1}
    - [LOW_GROUNDING] form=`(try 7 (finally (prn :cleanup)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try 7 (finally (prn :cleanup)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try 7 (finally (prn :cleanup)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PRONOUN_BEFORE_NAME] form=`(try 7 (finally (prn :cleanup)))` — sentence-initial 'She' appears before any named character is introduced
    - [LOW_GROUNDING] form=`(try (try (/ 1 0) (finally (prn :ran))) (catch Exc` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try (try (/ 1 0) (finally (prn :ran))) (catch Exc` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-04: ex-info

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [LOW_GROUNDING] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', 'bad'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', 'bad'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G7-05: nil punning

- examples: 4
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'BOOL_LEAK_RESOLUTION': 3, 'LOW_GROUNDING': 11, 'STORY_RESOLUTION_NO_DRAWN': 1, 'LOWERCASE_CONCEPT_AFTER_PERIOD': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(some? nil)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(some? nil)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [BOOL_LEAK_RESOLUTION] form=`(some? nil)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(some? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(some? nil)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(some? nil)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G7-06: pre and post conditions

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'PRONOUN_BEFORE_NAME': 3, 'LOWERCASE_CONCEPT_AFTER_PERIOD': 2}
    - [LOW_GROUNDING] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', ':pre'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', ':pre'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', ':pre'), resolution doesn't close the loop)

### G7-07: assert

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLED_PLACE': 1}
    - [LOW_GROUNDING] form=`(do (assert (= 1 1)) 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (assert (= 1 1)) 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (assert (= 1 1)) 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '7'), resolution doesn't close the loop)

### G7-08: prn and pprint

- examples: 2
- variety @ n=50: 1.00
- issues: {'AS_ONE_WHO_CADENCE': 2}
    - [AS_ONE_WHO_CADENCE] form=`(with-out-str (prn :hare))` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [AS_ONE_WHO_CADENCE] form=`(with-out-str (prn :hare))` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G7-09: tap>

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 5, 'PRONOUN_BEFORE_NAME': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(tap> :hello)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hello',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(tap> :hello)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(tap> :hello)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hello',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(tap> :hello)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(tap> :hello)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hello',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(tap> 42)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-10: doc and source

- examples: 1
- variety @ n=50: 1.00
- issues: {'PRONOUN_BEFORE_NAME': 1, 'ANSWER_LEAK_STRING': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [PRONOUN_BEFORE_NAME] form=`(:doc (meta '^{:doc "adds two"} plus))` — sentence-initial 'She' appears before any named character is introduced
    - [ANSWER_LEAK_STRING] form=`(:doc (meta '^{:doc "adds two"} plus))` — answer string 'adds two' appears in user_msg
    - [CAP_PRONOUN_MID_SENTENCE] form=`(:doc (meta '^{:doc "adds two"} plus))` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(:doc (meta '^{:doc "adds two"} plus))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G7-11: Reading stack traces

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'PRONOUN_BEFORE_NAME': 1}
    - [LOW_GROUNDING] form=`(try (throw (Exception. "oops")) (catch Exception ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(try (throw (Exception. "oops")) (catch Exception ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(try (throw (Exception. "oops")) (catch Exception ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)

### G7-12: slurp and spit

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [LOW_GROUNDING] form=`(count "hare
tortoise
")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "hare
tortoise
")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('thistle',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count "hare
tortoise
")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "hare
tortoise
")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('harbor',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count "hare
tortoise
")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "hare
tortoise
")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('thread',), resolution doesn't close the loop)

### G7-13: line-seq

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)

### G7-14: with-open

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(with-out-str (println "hare"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (println "hare"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (println "hare"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-15: *in* and *out*

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 6}
    - [LOW_GROUNDING] form=`(with-out-str (print "x"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (print "x"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (print "x"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (println))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (println))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (println))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-16: edn read

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 7}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "{:a 1}")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "{:a 1}")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "{:a 1}")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "[:hare :tortoise]")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-17: JSON roundtrip

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G7-18: Shell command

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(:cmd {:cmd "ls" :args ["-l"]})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:cmd {:cmd "ls" :args ["-l"]})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '16', '3'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(:cmd {:cmd "ls" :args ["-l"]})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:cmd {:cmd "ls" :args ["-l"]})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '8', ':alpha'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(:cmd {:cmd "ls" :args ["-l"]})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:cmd {:cmd "ls" :args ["-l"]})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', ':low', ':lime'), resolution doesn't close the loop)

## Grade 8

### G8-01: Why polymorphism

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 3, 'PRONOUN_BEFORE_NAME': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':tortoise', ':else'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':tortoise', ':else'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':tortoise', ':else'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(let [speak (fn [k] (cond (= k :hare) "swift" (= k` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-02: deftype introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'PRONOUN_BEFORE_NAME': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — user_msg 204 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-03: defrecord introduction

- examples: 2
- variety @ n=50: 0.99
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'PRONOUN_BEFORE_NAME': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'LOW_GROUNDING': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':pace', ':slow', 'Alice'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':pace', ':slow', 'Alice'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':pace', ':slow', 'Alice'), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — sentence-initial 'She' appears before any named character is introduced
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — sentence with 5 commas reads as AI-output cadence: "reading the pace compartment of a Runner case is the form that says: 'A pail of "
    - [LOW_GROUNDING] form=`(do (defrecord Runner [name pace]) (:name (->Runne` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-04: Protocol definition

- examples: 2
- variety @ n=50: 0.98
- issues: {'LOW_GROUNDING': 6, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'PRONOUN_BEFORE_NAME': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol Greet (hail [this])) (some? Greet` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G8-05: Protocol extension

- examples: 2
- variety @ n=50: 0.98
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CONCEPT_AS_VERB': 3}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('swift', 'hare'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G8-06: Protocol method dispatch

- examples: 2
- variety @ n=50: 0.98
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 2, 'PRONOUN_BEFORE_NAME': 1, 'LOW_GROUNDING': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, extend it to both String and Long t'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence-initial 'She' appears before any named character is introduced
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, extend it to both String and Long t'

### G8-07: Record implementing protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CONCEPT_AS_VERB': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (defrecord M` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord M` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':swift', 'Pip'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (defrecord M` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord M` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':swift', 'Pip'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (defrecord M` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord M` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':swift', 'Pip'), resolution doesn't close the loop)

### G8-08: Multimethod defmulti

- examples: 2
- variety @ n=50: 0.99
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 5 commas reads as AI-output cadence: 'To build a sorting-table named pace that reads the :species stamp, add a :hare a'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti tag :kind) (defmethod tag :stone [_]` — sentence with 5 commas reads as AI-output cadence: 'To define multimethod tag dispatching on :kind, add a :stone arm, then call tag '

### G8-09: Multimethod defmethod

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 5 commas reads as AI-output cadence: 'Without a stamp, the table cannot route, and the milk cannot flow."\n\nWrite a Clo'

### G8-10: Multimethod vs protocol

- examples: 2
- variety @ n=50: 0.99
- issues: {'PRONOUN_BEFORE_NAME': 1, 'HIGH_LENGTH': 2, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [PRONOUN_BEFORE_NAME] form=`(do (defmulti show identity) (defmethod show :rabb` — sentence-initial 'She' appears before any named character is introduced
    - [HIGH_LENGTH] form=`(do (defmulti show identity) (defmethod show :rabb` — user_msg 216 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defmulti show identity) (defmethod show :rabb` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defmulti show identity) (defmethod show :rabb` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (defprotocol Show (show [this])) (extend-proto` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Show (show [this])) (extend-proto` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('str-', 'hare'), resolution doesn't close the loop)

### G8-11: Protocol vs Java interface

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CONCEPT_AS_VERB': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol IPace (run [this])) (extend-proto` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol IPace (run [this])) (extend-proto` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':ran', 'hare'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defprotocol IPace (run [this])) (extend-proto` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol IPace (run [this])) (extend-proto` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':ran', 'hare'), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`(do (defprotocol IPace (run [this])) (extend-proto` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(do (defprotocol IPace (run [this])) (extend-proto` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-12: extend-type on built-in types

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'PRONOUN_BEFORE_NAME': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-type` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-type` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', ':number-pace'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(do (defprotocol Pace (speed [this])) (extend-type` — user_msg 217 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol Pace (speed [this])) (extend-type` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defprotocol Pace (speed [this])) (extend-type` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-type` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-13: this-style vs fn-style

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [LOW_GROUNDING] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Named (name-of [this])) (defrecor` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':n', 'Zephyr'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Named (name-of [this])) (defrecor` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':n', 'Zephyr'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Named (name-of [this])) (defrecor` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':n', 'Zephyr'), resolution doesn't close the loop)

### G8-14: Protocols don't inherit

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 2}
    - [LOW_GROUNDING] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — sentence with 5 commas reads as AI-output cadence: 'He\nexplained to Pernille, "To define two protocols A and B, each with a method, '
    - [LOW_GROUNDING] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — sentence with 6 commas reads as AI-output cadence: 'To define two protocols A and B, each with a method, extend both to String type '

### G8-15: derive and isa? — multimethod hierarchy

- examples: 3
- variety @ n=50: 0.99
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 6, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':runner', ':hare'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':runner', ':hare'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':runner', ':hare'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(isa? java.lang.Long java.lang.Number)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(isa? java.lang.Long java.lang.Number)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(isa? java.lang.Long java.lang.Number)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-16: Abstract design with protocols

- examples: 2
- variety @ n=50: 0.98
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CONCEPT_AS_VERB': 4, 'CLAUSE_STACK_OVERFLOW': 3}
    - [LOW_GROUNDING] form=`(do (defprotocol Move (step [this])) (defrecord Mi` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Move (step [this])) (defrecord Mi` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':leap', ':plod'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defprotocol Move (step [this])) (defrecord Mi` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Move (step [this])) (defrecord Mi` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':leap', ':plod'), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`(do (defprotocol Move (step [this])) (defrecord Mi` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(do (defprotocol Move (step [this])) (defrecord Mi` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 9

### G9-01: Immutability as default — review

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 4, 'LOW_GROUNDING': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :b 2) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '7', '3'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(let [m {:a 1}] (assoc m :b 2) m)` — sentence with 5 commas reads as AI-output cadence: 'To bind a map m, call assoc to add :b 6 to a new map, then return the unchanged '
    - [LOW_GROUNDING] form=`(let [m {:a 1}] (assoc m :b 2) m)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :b 2) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '12', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :b 2) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '6', '5'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(let [m {:a 1}] (assoc m :b 2) m)` — sentence with 8 commas reads as AI-output cadence: 'To bind a map m, call assoc to add :b 5 to a new map, then return the unchanged '

### G9-02: Why state at all

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 5, 'HIGH_LENGTH': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'SMALL_INT_LEAK': 1, 'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — sentence with 6 commas reads as AI-output cadence: "She said untroubled by what others thought, the chalk's edge cool against her\nfi"
    - [HIGH_LENGTH] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — user_msg 206 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [SMALL_INT_LEAK] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — small-int answer 1 leaks via resolution-slot phrasing
    - [LOW_GROUNDING] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-03: Atom introduction

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'CONCEPT_PHRASE_COMMA_LIST': 9, 'CLAUSE_STACK_OVERFLOW': 4, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 5 commas reads as AI-output cadence: '"Each farmer submits a form for atom, swap, and deref — a form\nthat reads the cu'
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-04: Atom CAS semantics

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 6, 'LOW_GROUNDING': 2, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — concept_phrase 'atom, CAS, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — sentence with 7 commas reads as AI-output cadence: "She said as a millwheel turns, slow and sure, the chalk's edge cool against her\n"
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — concept_phrase 'atom, CAS, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — sentence with 5 commas reads as AI-output cadence: 'But to change it, atom, CAS, deref happens in one\nbreath: read the old number, a'
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G9-05: Watch on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 3}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':w',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — sentence with 5 commas reads as AI-output cadence: 'To construct an atom a, construct a log atom, add a watch to a that conjoins new'
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G9-06: Validator on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-07: Ref introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 5, 'STORY_RESOLUTION_NO_DRAWN': 3, 'PRONOUN_BEFORE_NAME': 1}
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — concept_phrase 'ref, dosync, alter, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 6 commas reads as AI-output cadence: '"Each farmer submits a form for ref, dosync, alter, deref — a form\nthat reads th'
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — concept_phrase 'ref, dosync, alter, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 6 commas reads as AI-output cadence: '"Each farmer submits a form for ref, dosync, alter, deref — a form\nthat reads th'

### G9-08: dosync and alter

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 3, 'CLAUSE_STACK_OVERFLOW': 5, 'STORY_RESOLUTION_NO_DRAWN': 3, 'PRONOUN_BEFORE_NAME': 1, 'CONCEPT_PHRASE_COMMA_LIST': 3}
    - [LOW_GROUNDING] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — sentence with 5 commas reads as AI-output cadence: "That is\nthe slate's promise: construct refs a and b, perform a coordinated trans"
    - [LOW_GROUNDING] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — sentence with 5 commas reads as AI-output cadence: 'The count will construct refs a and b, perform a coordinated transaction that al'
    - [LOW_GROUNDING] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '5'), resolution doesn't close the loop)

### G9-09: Ref vs atom

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'PRONOUN_BEFORE_NAME': 1, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 5, 'AS_ONE_WHO_CADENCE': 1}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PRONOUN_BEFORE_NAME] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence-initial 'She' appears before any named character is introduced
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 5 commas reads as AI-output cadence: 'The count will construct an atom holding 0, atomically swap it by applying inc, '
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose

### G9-10: Agent introduction

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 3, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'HIGH_LENGTH': 2, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'CLAUSE_STACK_OVERFLOW': 4, 'STORY_RESOLUTION_NO_DRAWN': 3, 'PRONOUN_BEFORE_NAME': 1}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [HIGH_LENGTH] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg 213 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-11: send and send-off

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 3, 'PRONOUN_BEFORE_NAME': 1}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 5 commas reads as AI-output cadence: '"To construct an agent holding 0, use send to asynchronously apply inc, await it'
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 5 commas reads as AI-output cadence: '"To construct an agent holding 0, use send to asynchronously apply inc, await it'

### G9-12: await — synchronizing on agents

- examples: 1
- variety @ n=50: 0.96
- issues: {'LOW_GROUNDING': 3, 'PRONOUN_BEFORE_NAME': 1, 'CONCEPT_PHRASE_COMMA_LIST': 3, 'CLAUSE_STACK_OVERFLOW': 3, 'HIGH_LENGTH': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PRONOUN_BEFORE_NAME] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence-initial 'He' appears before any named character is introduced
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — concept_phrase 'agent, double send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 7 commas reads as AI-output cadence: 'To construct an agent holding 0, asynchronously send inc twice, synchronize with'
    - [HIGH_LENGTH] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — user_msg 201 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G9-13: future introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`@(future (+ 1 2))` — concept_phrase 'future, add, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`@(future (+ 1 2))` — concept_phrase 'future, add, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`@(future (+ 1 2))` — concept_phrase 'future, add, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose

### G9-14: deref @ shorthand

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 7)) @a)` — sentence with 6 commas reads as AI-output cadence: "He said her breath even, her step even, her thought even, the chalk's edge cool "
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) (deref a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) (deref a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)

### G9-15: promise — deliver and deref

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 4}
    - [LOW_GROUNDING] form=`(do (def p (promise)) (deliver p :done) @p)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def p (promise)) (deliver p :done) @p)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':done',), resolution doesn't close the loop)
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def p (promise)) (deliver p :done) @p)` — concept_phrase 'promise, deliver, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [LOW_GROUNDING] form=`(do (def p (promise)) (deliver p :done) @p)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def p (promise)) (deliver p :done) @p)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':done',), resolution doesn't close the loop)
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def p (promise)) (deliver p :done) @p)` — concept_phrase 'promise, deliver, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose

### G9-16: volatile — when STM is too heavy

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 6, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — concept_phrase 'volatile, vswap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — sentence with 5 commas reads as AI-output cadence: '"Each farmer submits a form for volatile, vswap, deref — a form\nthat reads the c'
    - [LOW_GROUNDING] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — concept_phrase 'volatile, vswap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — sentence with 5 commas reads as AI-output cadence: 'But to change it, volatile, vswap, deref happens in one\nbreath: read the old num'

### G9-17: binding — thread-local

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 5, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — concept_phrase 'dynamic var, binding, read' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — sentence with 5 commas reads as AI-output cadence: 'But to change it, dynamic var, binding, read happens in one\nbreath: read the old'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — concept_phrase 'dynamic var, binding, read' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — sentence with 5 commas reads as AI-output cadence: 'But to change it, dynamic var, binding, read happens in one\nbreath: read the old'

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 0.98
- issues: {'LOW_GROUNDING': 5, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 4, 'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1, 'DOUBLE_PREP': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — concept_phrase 'lock, locking, arithmetic' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — concept_phrase 'lock, locking, arithmetic' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — sentence with 5 commas reads as AI-output cadence: 'But to change it, lock, locking, arithmetic happens in one\nbreath: read the old '
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 10

### G10-01: quote, unquote, unquote-splice

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'STORY_RESOLUTION_NO_DRAWN': 6, 'PRONOUN_BEFORE_NAME': 1, 'HIGH_LENGTH': 1}
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(quote (+ 1 2))` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(quote (+ 1 2))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`'(1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-02: syntax-quote

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'LOW_GROUNDING': 3, 'PRONOUN_BEFORE_NAME': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 10] `(+ ~x ~x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(let [x 10] `(+ ~x ~x))` — user_msg 205 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(let [x 10] `(+ ~x ~x))` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(let [x 10] `(+ ~x ~x))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 10] `(+ ~x ~x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 10] `(+ ~x ~x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10',), resolution doesn't close the loop)

### G10-03: defmacro introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'PRONOUN_BEFORE_NAME': 1}
    - [LOW_GROUNDING] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G10-04: Macro expansion rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 3, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'PARAGRAPH_FRAGMENTATION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(when true 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(macroexpand-1 '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(when true 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(macroexpand-1 '(when true 1))` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(macroexpand-1 '(when true 1))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(when true 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)

### G10-05: macroexpand

- examples: 2
- variety @ n=50: 0.99
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 6, 'PRONOUN_BEFORE_NAME': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(macroexpand '(when true 1))` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(macroexpand '(when true 1))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(macroexpand '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(macroexpand '(when true 1))` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(macroexpand '(when true 1))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(macroexpand '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-06: when and when-not as macros

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'HIGH_LENGTH': 2, 'CAP_PRONOUN_MID_SENTENCE': 4, 'POST_COMMA_CAPITAL_PRONOUN': 4, 'LOW_GROUNDING': 8, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(when true 1 2 3)` — user_msg 209 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(when true 1 2 3)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(when true 1 2 3)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(when true 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1, 'STORY_RESOLUTION_NO_DRAWN': 5, 'LOW_GROUNDING': 7, 'HIGH_LENGTH': 1, 'DOUBLED_PLACE': 1, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [ANSWER_LEAK] form=`(-> 5 inc inc inc)` — answer 8 in narrative
    - [STORY_RESOLUTION_NO_DRAWN] form=`(-> 5 inc inc inc)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(-> 5 inc inc inc)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(-> 5 inc inc inc)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '14', '16'), resolution doesn't close the loop)

### G10-08: Macro vs fn

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CONCEPT_AS_VERB': 3, 'AS_ONE_WHO_CADENCE': 1, 'ANSWER_LEAK': 1, 'PRONOUN_BEFORE_NAME': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '3'), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [ANSWER_LEAK] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — answer 7 in narrative
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '5'), resolution doesn't close the loop)

### G10-09: Hygiene and gensym

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'PRONOUN_BEFORE_NAME': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'AS_ONE_WHO_CADENCE': 1}
    - [LOW_GROUNDING] form=`(symbol? (gensym))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PRONOUN_BEFORE_NAME] form=`(symbol? (gensym))` — sentence-initial 'She' appears before any named character is introduced
    - [LOW_GROUNDING] form=`(symbol? (gensym))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(symbol? (gensym))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('x_', 'x_'), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G10-10: Anaphoric macros are confusing

- examples: 2
- variety @ n=50: 0.99
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 1, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'PRONOUN_BEFORE_NAME': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — user_msg 209 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)

### G10-11: Reader macros overview

- examples: 3
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'LOW_GROUNDING': 9, 'STORY_RESOLUTION_NO_DRAWN': 9, 'THE_FORM_OVERUSE': 2, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [LOW_GROUNDING] form=`'(1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '16', '18'), resolution doesn't close the loop)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [LOW_GROUNDING] form=`'(1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '18', '15'), resolution doesn't close the loop)

### G10-12: Tagged literals

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'PRONOUN_BEFORE_NAME': 2, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(inst? #inst "2024-01-01")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inst? #inst "2024-01-01")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('2024', '-01', '-01'), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(inst? #inst "2024-01-01")` — sentence-initial 'She' appears before any named character is introduced
    - [CAP_PRONOUN_MID_SENTENCE] form=`(inst? #inst "2024-01-01")` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(inst? #inst "2024-01-01")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(inst? #inst "2024-01-01")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-13: Data readers and EDN extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "42")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', '42'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "42")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', '42'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "42")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', '42'), resolution doesn't close the loop)

### G10-14: eval (the function)

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 6, 'PRONOUN_BEFORE_NAME': 1, 'CONCEPT_AS_VERB': 2, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(eval '(+ 1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval '(+ 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(eval '(+ 1 2 3))` — sentence-initial 'She' appears before any named character is introduced
    - [CONCEPT_AS_VERB] form=`(eval '(+ 1 2 3))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval '(+ 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(eval '(+ 1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-15: When not to write a macro

- examples: 2
- variety @ n=50: 0.99
- issues: {'CONCEPT_AS_VERB': 3, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'LOW_GROUNDING': 1}
    - [CONCEPT_AS_VERB] form=`(do "a function suffices when no syntax shaping is` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "a function suffices when no syntax shaping is` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', 'ochre'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "a function suffices when no syntax shaping is` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', 'cobalt'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do "a function suffices when no syntax shaping is` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do "a function suffices when no syntax shaping is` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "a function suffices when no syntax shaping is` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', 'marble'), resolution doesn't close the loop)

### G10-16: Macro pattern library

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 6, 'PRONOUN_BEFORE_NAME': 1, 'HIGH_LENGTH': 2}
    - [LOW_GROUNDING] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':slow-and-steady'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':slow-and-steady'), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — sentence-initial 'She' appears before any named character is introduced
    - [LOW_GROUNDING] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 11

### G11-02: Method call syntax

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'HIGH_LENGTH': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'PRONOUN_BEFORE_NAME': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(.toUpperCase "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(.toUpperCase "abc")` — user_msg 208 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(.toUpperCase "abc")` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(.toUpperCase "abc")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(.toUpperCase "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(.toUpperCase "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)

### G11-03: Static method call

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'PRONOUN_BEFORE_NAME': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(Math/abs -7)` — sentence-initial 'She' appears before any named character is introduced
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/max 3 9)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/max 3 9)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '9'), resolution doesn't close the loop)

### G11-04: Field access

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'PRONOUN_BEFORE_NAME': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('lichen',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(count "tortoise")` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(count "tortoise")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('pewter',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('topaz',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('coral',), resolution doesn't close the loop)

### G11-05: Import form

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'FOREIGN_FABLE_IMAGERY': 1, 'HEDGING_NEAR_FORM': 1}
    - [LOW_GROUNDING] form=`(do "(:import (java.util Date)) imports a host cla` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do "(:import (java.util Date)) imports a host cla` — sentence with 6 commas reads as AI-output cadence: 'Theodoric, her breath even, her step even, her thought even, had already written'
    - [FOREIGN_FABLE_IMAGERY] form=`(do "import is a top-of-file ns clause" :studied)` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`(do "import is a top-of-file ns clause" :studied)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "import is a top-of-file ns clause" :studied)` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [LOW_GROUNDING] form=`(do "import is a top-of-file ns clause" :studied)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-06: new and dot-construct

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CONCEPT_AS_VERB': 4, 'PRONOUN_BEFORE_NAME': 2}
    - [LOW_GROUNDING] form=`(String. "go")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(String. "go")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('go',), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`(String. "go")` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(String. "go")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(String. "go")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('go',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(String. "go")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-07: Arrays

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CONCEPT_AS_VERB': 2, 'PRONOUN_BEFORE_NAME': 1}
    - [LOW_GROUNDING] form=`(let [a (int-array [10 20 30])] (aget a 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (int-array [10 20 30])] (aget a 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '20', '30'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(let [a (int-array [10 20 30])] (aget a 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (int-array [10 20 30])] (aget a 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '20', '30'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(let [a (int-array [10 20 30])] (aget a 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (int-array [10 20 30])] (aget a 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '20', '30'), resolution doesn't close the loop)

### G11-08: Type hints

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 3, 'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'PRONOUN_BEFORE_NAME': 1}
    - [CONCEPT_AS_VERB] form=`(let [^String s "abc"] (.toUpperCase s))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(let [^String s "abc"] (.toUpperCase s))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [^String s "abc"] (.toUpperCase s))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`(let [^String s "abc"] (.toUpperCase s))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(let [^String s "abc"] (.toUpperCase s))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [^String s "abc"] (.toUpperCase s))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)

### G11-09: Checked vs unchecked math

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "*unchecked-math* turns off overflow checking ` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':z', 'lichen'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do "*unchecked-math* turns off overflow checking ` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do "*unchecked-math* turns off overflow checking ` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G11-10: ClojureScript overview

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 4, 'LOW_GROUNDING': 4}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "ClojureScript compiles to JavaScript via the ` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`(do "ClojureScript compiles to JavaScript via the ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(do "ClojureScript compiles to JavaScript via the ` — tortoise-hare-specific imagery 'leather notebook' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`(do "ClojureScript compiles to JavaScript via the ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "ClojureScript compiles to JavaScript via the ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(do "cljs runs in browsers and Node, with JS inter` — tortoise-hare-specific imagery 'leather notebook' leaks into milkmaid prose

### G11-11: cljs / JavaScript interop

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'HEDGING_NEAR_FORM': 2, 'FOREIGN_FABLE_IMAGERY': 2}
    - [LOW_GROUNDING] form=`(do "(js/console.log x) calls a JS global; (.-foo ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "(js/console.log x) calls a JS global; (.-foo ` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [LOW_GROUNDING] form=`(do "(js/console.log x) calls a JS global; (.-foo ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "(js/console.log x) calls a JS global; (.-foo ` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [FOREIGN_FABLE_IMAGERY] form=`(do "js/<name> namespaces JS globals; .- prefix ma` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do "js/<name> namespaces JS globals; .- prefix ma` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose

### G11-12: Basilisp overview (Python host)

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 3, 'LOW_GROUNDING': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "basilisp is a Clojure-like Lisp implemented o` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`(do "basilisp is a Clojure-like Lisp implemented o` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(do "basilisp interops with Python via the same do` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do "basilisp interops with Python via the same do` — tortoise-hare-specific imagery 'leather notebook' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`(do "basilisp interops with Python via the same do` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-13: Cross-platform .cljc and reader-conditionals

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'HEDGING_NEAR_FORM': 1, 'FOREIGN_FABLE_IMAGERY': 1}
    - [LOW_GROUNDING] form=`(do "#?(:clj … :cljs …) selects a form per host at` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "#?(:clj … :cljs …) selects a form per host at` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "#?(:clj … :cljs …) selects a form per host at` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "#?(:clj … :cljs …) selects a form per host at` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [FOREIGN_FABLE_IMAGERY] form=`(do ".cljc files share code across multiple hosts"` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into milkmaid prose

### G11-14: Debugging host leaks

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 6, 'PRONOUN_BEFORE_NAME': 1, 'HIGH_LENGTH': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(do "host stack traces leak through interop; learn` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "host stack traces leak through interop; learn` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':delta', 'cedar'), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(do "host stack traces leak through interop; learn` — sentence-initial 'She' appears before any named character is introduced
    - [LOW_GROUNDING] form=`(do "host stack traces leak through interop; learn` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "host stack traces leak through interop; learn` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':y', 'pewter'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do "host stack traces leak through interop; learn` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 12

### G12-01: Transducers introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'AS_ONE_WHO_CADENCE': 2, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'CLAUSE_STACK_OVERFLOW': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(into [] (map inc) [1 2 3])` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [CAP_PRONOUN_MID_SENTENCE] form=`(into [] (map inc) [1 2 3])` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(into [] (map inc) [1 2 3])` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G12-02: Transducer composition

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'PRONOUN_BEFORE_NAME': 1, 'CLAUSE_STACK_OVERFLOW': 6, 'HIGH_LENGTH': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'AS_ONE_WHO_CADENCE': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — sentence-initial 'She' appears before any named character is introduced
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — sentence with 5 commas reads as AI-output cadence: '"To\ncompose map-inc and filter-even into a transducer pipeline, then apply it wi'
    - [HIGH_LENGTH] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — user_msg 207 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G12-03: into with a transducer (xform)

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'AS_ONE_WHO_CADENCE': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into #{} (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into #{} (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into #{} (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (take 3) (range 100))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '100'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (take 3) (range 100))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '100'), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(into [] (take 3) (range 100))` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G12-04: core.async introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "(chan), (go ...), (<! ...), (>! ...) form the` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do "go-blocks let you write async code as if it w` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into milkmaid prose

### G12-05: Channels and pipelines

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'LOW_GROUNDING': 3, 'FOREIGN_FABLE_IMAGERY': 1, 'HEDGING_NEAR_FORM': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "pipe, mult, mix, pipeline-async route values ` — sentence with 5 commas reads as AI-output cadence: 'Maeve squinted at the goal — to study how pipe, mult, mix, and pipeline-async ro'
    - [LOW_GROUNDING] form=`(do "pipe, mult, mix, pipeline-async route values ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do "pipe, mult, mix, pipeline-async route values ` — sentence with 6 commas reads as AI-output cadence: 'Theodoric, her breath even, her step even, her thought even, had already written'
    - [FOREIGN_FABLE_IMAGERY] form=`(do "pipelines transform streams of values channel` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`(do "pipelines transform streams of values channel` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "pipelines transform streams of values channel` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value

### G12-06: clojure.spec

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into milkmaid prose

### G12-07: Spec generators

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'HEDGING_NEAR_FORM': 2, 'FOREIGN_FABLE_IMAGERY': 2}
    - [LOW_GROUNDING] form=`(do "s/exercise produces sample inputs for a spec"` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "s/exercise produces sample inputs for a spec"` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [FOREIGN_FABLE_IMAGERY] form=`(do "s/exercise produces sample inputs for a spec"` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`(do "s/exercise produces sample inputs for a spec"` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(do "spec generators turn specs into property-base` — tortoise-hare-specific imagery 'leather notebook' leaks into milkmaid prose
    - [HEDGING_NEAR_FORM] form=`(do "spec generators turn specs into property-base` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value

### G12-08: clojure.test

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 3, 'FOREIGN_FABLE_IMAGERY': 1, 'LOW_GROUNDING': 1, 'AS_ONE_WHO_CADENCE': 1}
    - [HEDGING_NEAR_FORM] form=`(= (+ 1 2) 3)` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [FOREIGN_FABLE_IMAGERY] form=`(= (+ 1 2) 3)` — tortoise-hare-specific imagery 'leather notebook' leaks into milkmaid prose
    - [HEDGING_NEAR_FORM] form=`(= (+ 1 2) 3)` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [LOW_GROUNDING] form=`(do "(deftest …), (is …), (testing …) are the core` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "(deftest …), (is …), (testing …) are the core` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [AS_ONE_WHO_CADENCE] form=`(do "(deftest …), (is …), (testing …) are the core` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G12-09: Test fixtures

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 3}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "(use-fixtures :each f) wraps every deftest in` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do "fixtures provide setup/teardown around deftes` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do "fixtures provide setup/teardown around deftes` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into milkmaid prose

### G12-10: Property-based testing

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 4, 'LOW_GROUNDING': 5, 'HEDGING_NEAR_FORM': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(= (reverse (reverse [1 2 3])) [1 2 3])` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`(= (reverse (reverse [1 2 3])) [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(= (reverse (reverse [1 2 3])) [1 2 3])` — tortoise-hare-specific imagery 'leather notebook' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`(= (reverse (reverse [1 2 3])) [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(do "test.check generates inputs and checks proper` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`(do "test.check generates inputs and checks proper` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-11: Leiningen project.clj

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'HEDGING_NEAR_FORM': 2, 'FOREIGN_FABLE_IMAGERY': 2}
    - [LOW_GROUNDING] form=`(do "project.clj declares :dependencies, :main, :p` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "project.clj declares :dependencies, :main, :p` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [LOW_GROUNDING] form=`(do "project.clj declares :dependencies, :main, :p` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "project.clj declares :dependencies, :main, :p` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [FOREIGN_FABLE_IMAGERY] form=`(do "Leiningen reads project.clj at the project ro` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do "Leiningen reads project.clj at the project ro` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose

### G12-12: deps.edn projects

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 3, 'LOW_GROUNDING': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "deps.edn declares :deps and :aliases for the ` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`(do "deps.edn declares :deps and :aliases for the ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(do "deps.edn is read by the official `clj`/`cloju` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do "deps.edn is read by the official `clj`/`cloju` — tortoise-hare-specific imagery 'leather notebook' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`(do "deps.edn is read by the official `clj`/`cloju` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-13: Aliases and tools

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'HEDGING_NEAR_FORM': 1, 'FOREIGN_FABLE_IMAGERY': 1}
    - [LOW_GROUNDING] form=`(do "`clj -M:test` runs the :test alias from deps.` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "`clj -M:test` runs the :test alias from deps.` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "`clj -M:test` runs the :test alias from deps.` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "`clj -M:test` runs the :test alias from deps.` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [FOREIGN_FABLE_IMAGERY] form=`(do "aliases compose extra paths, deps, and main o` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into milkmaid prose

### G12-14: Pedestal / Ring (web stack brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 5, 'LOW_GROUNDING': 3}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "Ring models HTTP as request-map -> response-m` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`(do "Ring models HTTP as request-map -> response-m` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(do "Ring models HTTP as request-map -> response-m` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do "Pedestal layers interceptors over Ring for ri` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do "Pedestal layers interceptors over Ring for ri` — tortoise-hare-specific imagery 'leather notebook' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`(do "Pedestal layers interceptors over Ring for ri` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-15: Datomic / XTDB (datalog db brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 3, 'LOW_GROUNDING': 2, 'AS_ONE_WHO_CADENCE': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "Datomic and XTDB are immutable, time-aware da` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`(do "Datomic and XTDB are immutable, time-aware da` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [AS_ONE_WHO_CADENCE] form=`(do "Datomic and XTDB are immutable, time-aware da` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [FOREIGN_FABLE_IMAGERY] form=`(do "queries are written in datalog over EDN-shape` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do "queries are written in datalog over EDN-shape` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`(do "queries are written in datalog over EDN-shape` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-16: Reagent (cljs UI brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 3, 'LOW_GROUNDING': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "Reagent wraps React with Hiccup-shaped Clojur` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do "components are functions returning Hiccup vec` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do "components are functions returning Hiccup vec` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`(do "components are functions returning Hiccup vec` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-17: Library design patterns

- examples: 3
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 5, 'AS_ONE_WHO_CADENCE': 1, 'LOW_GROUNDING': 3}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "good libraries expose data, then functions, t` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into milkmaid prose
    - [AS_ONE_WHO_CADENCE] form=`(do "good libraries expose data, then functions, t` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [FOREIGN_FABLE_IMAGERY] form=`(do "good libraries expose data, then functions, t` — tortoise-hare-specific imagery 'leather notebook' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`(do "good libraries expose data, then functions, t` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(do "small public API surface, plain data inputs, ` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`(= [1 2 3] (vec '(1 2 3)))` — tortoise-hare-specific imagery 'leather notebook' leaks into milkmaid prose

### G12-18: Clojure style guide

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 3, 'LOW_GROUNDING': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "kebab-case names, two-space indent, threading` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do "kebab-case names, two-space indent, threading` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`(do "prefer pure functions, name predicates with ?` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(do "prefer pure functions, name predicates with ?` — tortoise-hare-specific imagery 'leather notebook' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`(do "prefer pure functions, name predicates with ?` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

---

## Summary

### Issue counts (across all examples × 3 records)

- **STORY_RESOLUTION_NO_DRAWN**: 967
- **LOW_GROUNDING**: 643
- **CAP_PRONOUN_MID_SENTENCE**: 209
- **POST_COMMA_CAPITAL_PRONOUN**: 206
- **CLAUSE_STACK_OVERFLOW**: 166
- **PRONOUN_BEFORE_NAME**: 124
- **FOREIGN_FABLE_IMAGERY**: 112
- **NARRATIVE_NUMERAL_HARDCODE**: 108
- **CONCEPT_PHRASE_COMMA_LIST**: 75
- **AS_ONE_WHO_CADENCE**: 48
- **CONCEPT_AS_VERB**: 39
- **HIGH_LENGTH**: 36
- **PARAMETRIC_LITERAL_NUMERALS**: 24
- **FORM_DISPLAY_AND_FORM_NOUN**: 21
- **LOWERCASE_CONCEPT_AFTER_PERIOD**: 19
- **HEDGING_NEAR_FORM**: 16
- **ANSWER_LEAK**: 15
- **PARAGRAPH_FRAGMENTATION**: 13
- **THE_FORM_OVERUSE**: 11
- **FORM_LEAK**: 10
- **BOOL_LEAK_RESOLUTION**: 9
- **STRING_AS_CHAR_MISCLAIM**: 6
- **DOUBLED_PLACE**: 4
- **PROCEDURAL_OPENER**: 3
- **SMALL_INT_LEAK**: 2
- **ANSWER_LEAK_STRING**: 1
- **DOUBLE_PREP**: 1

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 270 | — |
| 2 | 22 | 88 | 496 | — |
| 3 | 18 | 31 | 176 | — |
| 4 | 20 | 39 | 276 | — |
| 5 | 22 | 39 | 322 | — |
| 6 | 16 | 33 | 183 | — |
| 7 | 18 | 36 | 180 | — |
| 8 | 16 | 31 | 192 | — |
| 9 | 18 | 34 | 293 | — |
| 10 | 16 | 36 | 249 | — |
| 11 | 14 | 29 | 128 | — |
| 12 | 18 | 37 | 123 | — |

### Sample issues by severity

#### FOREIGN_FABLE_IMAGERY

- `G1-01` (form `0`): tortoise-hare-specific imagery 'moss-covered milestone' leaks into milkmaid prose
    ```
    Helga carried more than milk that morning at the edge of the orchard; she carried a whole imagined fortune.

At a moss-covered milestone by the orchard, Helga sketched a small
wager into the path: whoever guessed the result of `7`
first would win the right to set the next race. Ulysses,
untroubled b...
    ```
- `G1-01` (form `"hello"`): tortoise-hare-specific imagery 'moss-covered milestone' leaks into milkmaid prose
    ```
    A pail of milk is a small fortune to a careful walker and a lost fortune to a careless one.

At a moss-covered milestone at the edge of the meadow, Evgenia sketched a small
wager into the path: whoever guessed the result of `"cobalt"`
first would win the right to set the next race. Nathaniel,
with a...
    ```
- `G1-01` (form `nil`): tortoise-hare-specific imagery 'moss-covered milestone' leaks into milkmaid prose
    ```
    Helga carried more than milk that morning at the edge of the orchard; she carried a whole imagined fortune.

At a moss-covered milestone by the orchard, Helga sketched a small
wager into the path: whoever guessed the result of `nil`
first would win the right to set the next race. Ulysses,
with stead...
    ```
- `G1-01` (form `nil`): tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

A small audience of forest creatures had gathered at the farm to watch
Marzena attempt to outwit Konstantin at reading the REPL.
Konstantin pointed to the literal nil and read out the form aloud:
`...
    ```
- `G1-01` (form `nil`): tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into milkmaid prose
    ```
    Long before the market opened its stalls, a young woman had already spent her milk three times in her head.

A wooden sign nailed to a tree in the orchard carried a puzzle. The riddle
was simple: it asked the reader to evaluate `nil`. Sanda
laughed, with great whoops of laughter, and declared it too...
    ```

#### FORM_DISPLAY_AND_FORM_NOUN

- `G1-01` (form `nil`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

A small audience of forest creatures had gathered at the farm to watch
Marzena attempt to outwit Konstantin at reading the REPL.
Konstantin pointed to the literal nil and read out the form aloud:
`...
    ```
- `G1-02` (form `-3`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    It was the season of new chicks and first cheeses, and every small profit felt like the start of a larger one.

A small audience of forest creatures had gathered by the village to watch
Greta attempt to outwit Anselmo at reading the REPL.
Anselmo pointed to the integer -97 and read out the form alou...
    ```
- `G1-02` (form `-3`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    near the market, the dairy stood between the lane and the meadow, and the day's milk waited to be carried to town.

A small audience of forest creatures had gathered near the market to watch
Paola attempt to outwit Bartholomew at reading the REPL.
Bartholomew pointed to the integer -54 and read out ...
    ```
- `G1-02` (form `-25`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    Ingrid hummed quietly near the road as she walked, the pail steady and the future already half-spent.

A small audience of forest creatures had gathered on the road to watch
Ingrid attempt to outwit Alaric at reading the REPL.
Alaric pointed to the integer -96 and read out the form aloud:
`-96`. The...
    ```
- `G1-03` (form `(+ 1/2 1/4)`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    Between the dairy and the marketplace stretched a road, a hill, and an entire life imagined into being.

A small audience of forest creatures had gathered by the market to watch
Klara attempt to outwit Kasimir at reading the REPL.
Kasimir pointed to the form (+ 1/2 1/4) and read out the form aloud:
...
    ```

#### LOW_GROUNDING

- `G1-01` (form `nil`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

A small audience of forest creatures had gathered at the farm to watch
Marzena attempt to outwit Konstantin at reading the REPL.
Konstantin pointed to the literal nil and read out the form aloud:
`...
    ```
- `G1-02` (form `0`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    The road from the farm to the town was long, and a daydream could fit comfortably along its length.

Halfway through the race, Octavia stopped near the orchard and refused to
continue until someone could prove what the form `2`
evaluated to. Octavia called it impossible.
Clementine, walking up at he...
    ```
- `G1-03` (form `1/2`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    Long before the market opened its stalls, a young woman had already spent her milk three times in her head.

Iustinian had been keeping a small leather notebook of every
form he had successfully evaluated. Today near the road, the
next entry was the ratio 1/2. Zara peered over
his shoulder at the fo...
    ```
- `G1-05` (form `true`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    at the market, where the lane bends past the old hedge, Edyta began to add up coins she had not yet earned.

Halfway through the race, Edyta stopped near the market and refused to
continue until someone could prove what the form `true`
evaluated to. Edyta called it impossible.
Drusilla, walking up a...
    ```
- `G1-05` (form `false`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    It is an old habit to count the worth of a thing before the thing has reached the buyer.

A small audience of forest creatures had gathered near the orchard to watch
Friederike attempt to outwit Theodelinda at reading the REPL.
Theodelinda pointed to the literal false and read out the form aloud:
`f...
    ```

#### AS_ONE_WHO_CADENCE

- `G1-02` (form `12345`): user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    ```
    It is an old habit to count the worth of a thing before the thing has reached the buyer.

"There is no need to evaluate that," Agata said, as one who has counted his victory before the running.
"Anyone can see what the integer 100000000000 comes to." Apollonia, who
near the hilltop had grown used to...
    ```
- `G1-05` (form `false`): user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    ```
    She had not yet sold the milk and yet had already chosen the ribbons she would wear at the dance.

Czeslawa and Cassius stopped at the edge of the orchard where someone had
written the literal false on a flat stone. Czeslawa, as one who has counted his victory before the running, declared
that she c...
    ```
- `G1-05` (form `(= 1 2)`): user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    ```
    By the time Oksana had reached the second milestone in the orchard, the milk had become eggs, and the eggs a flock.

Oksana chalked a wager on a flat stone near the orchard: whoever
predicted the result of `(= 4 8)` would set the next race's
distance. Valerian, as one who has all the day before her,...
    ```
- `G1-13` (form `(+ 1 2)`): user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    ```
    It happened near the farm, on the morning Tove took the milk to market and her thoughts ran ahead of her feet.

She watched Ezekiel sort coins at the dairy table: copper in one pile, silver
in another, gold in a third — three small heaps growing patient and even under his
hands. "Ezekiel, how do you...
    ```
- `G1-13` (form `(* 4 5)`): user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    ```
    The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

Every morning, Estrid carried a pail of milk to the dairy, imagining what the coins would
total. She only smiled and said, "Come. Let us count the coins from yesterday's
sales." Together they counted: on...
    ```

#### STRING_AS_CHAR_MISCLAIM

- `G1-08` (form `\space`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    A pail of milk is a small fortune to a careful walker and a lost fortune to a careless one.

A small audience of forest creatures had gathered on the hilltop to watch
Evgenia attempt to outwit Gerhardt at reading the REPL.
Gerhardt pointed to the character \space and read out the form aloud:
`"amber...
    ```
- `G1-08` (form `\space`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

Solveig and Nicoletta stopped by the market where someone had
written the character \space on a flat stone. Solveig, tossing his head as a proud horse tosses its mane, declared
that she could see the ans...
    ```
- `G1-08` (form `\space`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    at the market, the road from the farmstead curved gently downhill, and Tudora walked it with her head held high.

A wooden sign nailed to a tree in the market carried a puzzle. The riddle
was simple: it asked the reader to evaluate `"marble"`. Tudora
laughed, as a victor walks before a victory is na...
    ```
- `G1-08` (form `\T`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    On market mornings, the dairy yard smelled of damp grass and warm tin, and the future seemed safely arrangeable.

A wooden sign nailed to a tree at the village carried a puzzle. The riddle
was simple: it asked the reader to evaluate `"harbor"`. Vivien
laughed, as if the race were already won, and de...
    ```
- `G1-08` (form `\T`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    It is an old habit to count the worth of a thing before the thing has reached the buyer.

A wooden sign nailed to a tree at the edge of the hilltop carried a puzzle. The riddle
was simple: it asked the reader to evaluate `"feather"`. Ninon
laughed, as a young rooster crows above the yard, and declar...
    ```

#### PRONOUN_BEFORE_NAME

- `G1-09` (form `(symbol? 'hare)`): sentence-initial 'She' appears before any named character is introduced
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

She claimed, swaggering through the underbrush, "I can ask whether a quoted name is a symbol, using the symbol? predicate without opening the pail — I'll
just read the label!" He tapped the pail, t...
    ```
- `G1-09` (form `(symbol? "tortoise")`): sentence-initial 'She' appears before any named character is introduced
    ```
    On market mornings, the dairy yard smelled of damp grass and warm tin, and the future seemed safely arrangeable.

She held up a pail with a chalk mark on its side — the word "cream" written in white.
"Is this cream?" She asked, pointing at the chalk mark. She laughed gently. "No.
The chalk mark is t...
    ```
- `G1-09` (form `(symbol? "tortoise")`): sentence-initial 'She' appears before any named character is introduced
    ```
    It is an old habit to count the worth of a thing before the thing has reached the buyer.

She held two pails side by side. One had "butter" chalked on it; the other held actual butter.
She touched the chalk mark and asked, "Is this butter?" She said, "That is the
chalk mark — the word. This is the b...
    ```
- `G1-09` (form `(= 'hare 'hare)`): sentence-initial 'She' appears before any named character is introduced
    ```
    It is an old habit to count the worth of a thing before the thing has reached the buyer.

She held up a pail with a chalk mark on its side — the word "cream" written in white.
"Is this cream?" She asked, pointing at the chalk mark. He laughed gently. "No.
The chalk mark is the name — the label on th...
    ```
- `G1-12` (form `(+ 2 3)`): sentence-initial 'She' appears before any named character is introduced
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

She arrived at the dairy to find the wall covered in chalk marks above the milk churns.
"What are all these notes?" She asked. Theophilus pointed and said, "The chalk marks
explain the steps below ...
    ```

#### STORY_RESOLUTION_NO_DRAWN

- `G1-09` (form `(symbol? 42)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('48',), resolution doesn't close the loop)
    ```
    Solvi hummed quietly on the farm as she walked, the pail steady and the future already half-spent.

One day, Solvi arrived with a stack of pails, each chalked with a different name: "cream," "skim," "butter,"
"curds." She pointed at one and guessed, "This pail contains butter." He asked,
"Did you op...
    ```
- `G1-09` (form `(symbol? 42)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('85',), resolution doesn't close the loop)
    ```
    along the road, before the cocks had finished crowing, Liesel had set out with the milk and a head full of plans.

One day, Liesel arrived with a stack of pails, each chalked with a different name: "cream," "skim," "butter,"
"curds." She pointed at one and guessed, "This pail contains butter." She a...
    ```
- `G1-09` (form `(symbol? 42)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('96',), resolution doesn't close the loop)
    ```
    Every step of the road carried the soft sound of liquid against tin and the louder sound of a daydream gathering speed.

The farmer held up a pail with a chalk mark written on its side. Below the mark sat actual coins — the real milk money. She asked the milkmaid: is that mark itself a symbol, a nam...
    ```
- `G1-09` (form `(symbol? "tortoise")`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('apple',), resolution doesn't close the loop)
    ```
    On market mornings, the dairy yard smelled of damp grass and warm tin, and the future seemed safely arrangeable.

She held up a pail with a chalk mark on its side — the word "cream" written in white.
"Is this cream?" She asked, pointing at the chalk mark. She laughed gently. "No.
The chalk mark is t...
    ```
- `G1-09` (form `(symbol? "tortoise")`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('indigo',), resolution doesn't close the loop)
    ```
    It is an old habit to count the worth of a thing before the thing has reached the buyer.

She held two pails side by side. One had "butter" chalked on it; the other held actual butter.
She touched the chalk mark and asked, "Is this butter?" She said, "That is the
chalk mark — the word. This is the b...
    ```

#### CAP_PRONOUN_MID_SENTENCE

- `G1-09` (form `(symbol? 42)`): ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    ```
    Every step of the road carried the soft sound of liquid against tin and the louder sound of a daydream gathering speed.

The farmer held up a pail with a chalk mark written on its side. Below the mark sat actual coins — the real milk money. She asked the milkmaid: is that mark itself a symbol, a nam...
    ```
- `G1-09` (form `(= 'hare 'hare)`): ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    ```
    Long before the market opened its stalls, a young woman had already spent her milk three times in her head.

Two chalk marks were written on the dairy wall: 'hare' and 'hare'. The milkmaid nodded, guessing they were the same. The farmer asked: but are those symbols truly equal? Let us read them thro...
    ```
- `G1-10` (form `(+ 1 2) ; sum of one and two`): ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

Beside the dairy tally, the milkmaid had chalked a note: '; sum of one and two.' The note was for her own reference — the dairy buyer at market would never see the chalk wall.

She needed a way to ...
    ```
- `G1-13` (form `(/ 10 2)`): ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    ```
    The pail sat steady on Fleur's head as she started down the lane in the market.

Ten coins sat on the tally table. The farmer needed to split them evenly into two equal piles. She chalked a form to divide them. The milkmaid guessed aloud, but the farmer asked: let us ask the REPL, and see what each ...
    ```
- `G1-14` (form `(- 100 (* 5 5))`): ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    ```
    On market mornings, the dairy yard smelled of damp grass and warm tin, and the future seemed safely arrangeable.

The farmer had one hundred coins on the tally table. Five coins sat in one pile, another five sat beside it. She chalked a form to find what remained when those two groups were multiplie...
    ```

#### POST_COMMA_CAPITAL_PRONOUN

- `G1-09` (form `(symbol? 42)`): capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    ```
    Every step of the road carried the soft sound of liquid against tin and the louder sound of a daydream gathering speed.

The farmer held up a pail with a chalk mark written on its side. Below the mark sat actual coins — the real milk money. She asked the milkmaid: is that mark itself a symbol, a nam...
    ```
- `G1-09` (form `(= 'hare 'hare)`): capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    ```
    Long before the market opened its stalls, a young woman had already spent her milk three times in her head.

Two chalk marks were written on the dairy wall: 'hare' and 'hare'. The milkmaid nodded, guessing they were the same. The farmer asked: but are those symbols truly equal? Let us read them thro...
    ```
- `G1-10` (form `(+ 1 2) ; sum of one and two`): capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

Beside the dairy tally, the milkmaid had chalked a note: '; sum of one and two.' The note was for her own reference — the dairy buyer at market would never see the chalk wall.

She needed a way to ...
    ```
- `G1-13` (form `(/ 10 2)`): capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    ```
    The pail sat steady on Fleur's head as she started down the lane in the market.

Ten coins sat on the tally table. The farmer needed to split them evenly into two equal piles. She chalked a form to divide them. The milkmaid guessed aloud, but the farmer asked: let us ask the REPL, and see what each ...
    ```
- `G1-14` (form `(- 100 (* 5 5))`): capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    ```
    On market mornings, the dairy yard smelled of damp grass and warm tin, and the future seemed safely arrangeable.

The farmer had one hundred coins on the tally table. Five coins sat in one pile, another five sat beside it. She chalked a form to find what remained when those two groups were multiplie...
    ```

#### THE_FORM_OVERUSE

- `G1-10` (form `(+ 1 2) ; sum of one and two`): `the form` appears 6 times in user_msg (template tic — vary references)
    ```
    A pail of milk is a small fortune to a careful walker and a lost fortune to a careless one.

Ula peered at Xaverius's dairy wall and saw lines of chalk marks above the form. Some marks were
crossed out, some added. "The form looks like a mess!" She cried. Xaverius smiled.
"No — the chalk marks are n...
    ```
- `G1-11` (form `(+    1    2)`): `the form` appears 6 times in user_msg (template tic — vary references)
    ```
    The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

Niamh peered at Cassandra's dairy wall and saw lines of chalk marks above the form. Some marks were
crossed out, some added. "The form looks like a mess!" She cried. Cassandra smiled.
"No — the chalk mar...
    ```
- `G1-11` (form `(+
  1
  2)`): `the form` appears 6 times in user_msg (template tic — vary references)
    ```
    A pail of milk is a small fortune to a careful walker and a lost fortune to a careless one.

Dorothea peered at Augusta's dairy wall and saw lines of chalk marks above the form. Some marks were
crossed out, some added. "The form looks like a mess!" She cried. Augusta smiled.
"No — the chalk marks ar...
    ```
- `G1-12` (form `(+ 2 3)`): `the form` appears 6 times in user_msg (template tic — vary references)
    ```
    Long before the market opened its stalls, a young woman had already spent her milk three times in her head.

Maeve peered at Euclid's dairy wall and saw lines of chalk marks above the form. Some marks were
crossed out, some added. "The form looks like a mess!" She cried. Euclid smiled.
"No — the cha...
    ```
- `G1-12` (form `(* (+ 1 2) 3)`): `the form` appears 6 times in user_msg (template tic — vary references)
    ```
    The cows had given generously that dawn, and the pail was heavier than usual, and the imagination was heavier still.

Rosa peered at Mortimer's dairy wall and saw lines of chalk marks above the form. Some marks were
crossed out, some added. "The form looks like a mess!" She cried. Mortimer smiled.
"...
    ```

#### NARRATIVE_NUMERAL_HARDCODE

- `G1-13` (form `(* 4 5)`): parametric example has hard-coded English numeral 'four piles' in a story slot — the actual draws may differ from this fixed count
    ```
    Roisin was not a careless girl by nature, but at the edge of the orchard the morning was bright and the daydreams were brighter.

She arrived at the market with a handful of copper coins, jingling in
her pocket — the pail was heavy on her arm and the road had been
long. "I know how much I have witho...
    ```
- `G1-13` (form `(* 4 5)`): parametric example has hard-coded English numeral 'four piles' in a story slot — the actual draws may differ from this fixed count
    ```
    It happened in the market, on the morning Paola took the milk to market and her thoughts ran ahead of her feet.

One afternoon, She found a cache of coins hidden in the dairy and tried to guess
the fortune, stepping high, as proud creatures step, the dairy cool and the imagined market still far away...
    ```
- `G1-13` (form `(* 4 5)`): parametric example has hard-coded English numeral 'four piles' in a story slot — the actual draws may differ from this fixed count
    ```
    The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

Every morning, Estrid carried a pail of milk to the dairy, imagining what the coins would
total. She only smiled and said, "Come. Let us count the coins from yesterday's
sales." Together they counted: on...
    ```
- `G1-18` (form `(* 7 6)`): parametric example has hard-coded English numeral 'seven piles' in a story slot — the actual draws may differ from this fixed count
    ```
    on the hilltop, the road from the farmstead curved gently downhill, and Ingrid walked it with her head held high.

She claimed, "I can multiply 7 by 2 while running and juggling!" But she
knew better. "In the real meadow, a stumble spills the pail. But in the practice meadow — the REPL — the
safety ...
    ```
- `G1-18` (form `(* 7 6)`): parametric example has hard-coded English numeral 'seven piles' in a story slot — the actual draws may differ from this fixed count
    ```
    By the time Danuta had reached the second milestone near the market, the milk had become eggs, and the eggs a flock.

She arrived at the dairy after a long walk, pail intact and milk brimming. He
smiled and asked, "How did you keep the pail so steady?" She replied, "I walked carefully,
one step at a...
    ```

#### ANSWER_LEAK

- `G1-13` (form `(- 20 7)`): answer 13 in narrative
    ```
    Seren was not a careless girl by nature, but in the orchard the morning was bright and the daydreams were brighter.

She arrived at the market with a handful of copper coins, jingling in
her pocket — the pail was heavy on her arm and the road had been
long. "I know how much I have without counting,"...
    ```
- `G1-14` (form `(+ 1 (* 2 3))`): answer 7 in narrative
    ```
    It was the kind of morning that tempts a careful person into carelessness through the back door of a happy thought.

She arrived at the market with a handful of copper coins, jingling in
her pocket — the pail was heavy on her arm and the road had been
long. "I know how much I have without counting,"...
    ```
- `G2-05` (form `(quot 100 7)`): answer 14 in narrative
    ```
    Between the dairy and the marketplace stretched a road, a hill, and an entire life imagined into being.

The farmer had 163 coins to divide equally among 3 merchants at the market. She gave each merchant the same whole number of coins without any coins left over. She needed to know how many whole co...
    ```
- `G2-10` (form `(* 5 5)`): answer 25 in narrative
    ```
    The road from the farm to the town was long, and a daydream could fit comfortably along its length.

The farmer had a square garden plot: 5 paces wide and 5 paces long. She needed the total area in square paces to know how much seed to sow.

She needed to multiply 6 by itself to find the area of the...
    ```
- `G2-10` (form `(* 3 3 3 3)`): answer 81 in narrative
    ```
    A pail of milk is a small fortune to a careful walker and a lost fortune to a careless one.

The farmer had a four-dimensional arrangement of coins (a thought experiment): 5 coins in each dimension. She wondered what the total count would be if she could stack all dimensions at once.

She needed to ...
    ```

#### CLAUSE_STACK_OVERFLOW

- `G1-14` (form `(- 100 (* 5 5))`): sentence with 5 commas reads as AI-output cadence: 'Philomena only shook her\nhead, as a tortoise walks, neither hurrying nor stoppin'
    ```
    on the road, where the lane bends past the old hedge, Sanda began to add up coins she had not yet earned.

One afternoon, She found a cache of coins hidden in the dairy and tried to guess
the fortune, with quiet steps, taking the long way, the dairy cool and the imagined market still far away. "Sure...
    ```
- `G1-16` (form `(pos? 7)`): sentence with 5 commas reads as AI-output cadence: 'Septimus only shook his\nhead, as a millwheel turns, slow and sure, and began sor'
    ```
    The road from the farm to the town was long, and a daydream could fit comfortably along its length.

One afternoon, She found a cache of coins hidden in the dairy and tried to guess
the fortune, with a laugh that carried over the field, the dairy cool and the imagined market still far away. "Surely ...
    ```
- `G2-01` (form `(* 2 3 4)`): sentence with 5 commas reads as AI-output cadence: 'Vespasia only shook her\nhead, stepping deliberately, one foot before the next, a'
    ```
    She had not yet sold the milk and yet had already chosen the ribbons she would wear at the dance.

One afternoon, She found a cache of coins hidden in the dairy and tried to guess
the fortune, boasting at every turn, the dairy cool and the imagined market still far away. "Surely I can
see the total ...
    ```
- `G2-01` (form `(+ 1 2 3 4 5 6 7 8 9 10)`): sentence with 5 commas reads as AI-output cadence: 'Adelaide only shook her\nhead, as a tortoise walks, neither hurrying nor stopping'
    ```
    It was by the orchard, on a fair-weather morning, that Helena began the long walk to market.

One afternoon, She found a cache of coins hidden in the dairy and tried to guess
the fortune, his chest thrown out before him, the dairy cool and the imagined market still far away. "Surely I can
see the to...
    ```
- `G2-03` (form `(not= 1 2)`): sentence with 6 commas reads as AI-output cadence: 'Theophilus only shook his\nhead, her breath even, her step even, her thought even'
    ```
    The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

One afternoon, She found a cache of coins hidden in the dairy and tried to guess
the fortune, his step bouncing with self-regard, the dairy cool and the imagined market still far away. "Surely I can
see ...
    ```

#### PROCEDURAL_OPENER

- `G1-17` (form `(+ 1 2)`): user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    ```
    The pail sat steady on Niamh's head as she started down the lane on the road.

To add 9 and 5 so the REPL returns the result, He composed the addition and submitted the form. The REPL read past the chalk marks and returned:

Write a form whose evaluation gives the value returned by adding 9 and 5....
    ```
- `G1-17` (form `(+ 1 2)`): user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    ```
    It is an old habit to count the worth of a thing before the thing has reached the buyer.

To add 5 and 0 so the REPL returns the result, She composed the addition and submitted the form. The REPL read past the chalk marks and returned:

Write a form whose evaluation gives the value returned by addin...
    ```
- `G2-05` (form `(quot 17 5)`): user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    ```
    She had not yet sold the milk and yet had already chosen the ribbons she would wear at the dance.

To find the integer quotient of 10 divided by 8, He composed the integer quotient and submitted the form. The REPL counted out the coins:

Write a Clojure expression that computes 10 divided by 8, with...
    ```

#### LOWERCASE_CONCEPT_AFTER_PERIOD

- `G1-18` (form `(+ 1 2)`): sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    ```
    Milk does not forgive a tilted head, but a dreaming mind seldom remembers as much.

She claimed, "I can add 7 and 7 while running and juggling!" But he
knew better. "In the real meadow, a stumble spills the pail. But in the practice meadow — the REPL — the
safety net catches every stumble. the addit...
    ```
- `G1-18` (form `(* 7 6)`): sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    ```
    on the hilltop, the road from the farmstead curved gently downhill, and Ingrid walked it with her head held high.

She claimed, "I can multiply 7 by 2 while running and juggling!" But she
knew better. "In the real meadow, a stumble spills the pail. But in the practice meadow — the REPL — the
safety ...
    ```
- `G2-20` (form `(count [1 2 3])`): sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    ```
    The cows had given generously that dawn, and the pail was heavier than usual, and the imagination was heavier still.

She arrived at the market breathless. "How many coins do I have?" He asked.
She counted on her fingers, looking back at each milestone. "I picked up bags at
five milestones. I counte...
    ```
- `G2-20` (form `(count "hello")`): sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    ```
    It was the kind of morning that tempts a careful person into carelessness through the back door of a happy thought.

She arrived at the market breathless. "How many coins do I have?" He asked.
She counted on her fingers, looking back at each milestone. "I picked up bags at
five milestones. I counted...
    ```
- `G2-20` (form `(count [])`): sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    ```
    A pail of milk is a small fortune to a careful walker and a lost fortune to a careless one.

She arrived at the market breathless. "How many coins do I have?" She asked.
She counted on her fingers, looking back at each milestone. "I picked up bags at
five milestones. I counted them all together..." ...
    ```

#### PARAGRAPH_FRAGMENTATION

- `G2-10` (form `(* 5 5)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    The road from the farm to the town was long, and a daydream could fit comfortably along its length.

The farmer had a square garden plot: 5 paces wide and 5 paces long. She needed the total area in square paces to know how much seed to sow.

She needed to multiply 6 by itself to find the area of the...
    ```
- `G2-10` (form `(* 3 3 3 3)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    A pail of milk is a small fortune to a careful walker and a lost fortune to a careless one.

The farmer had a four-dimensional arrangement of coins (a thought experiment): 5 coins in each dimension. She wondered what the total count would be if she could stack all dimensions at once.

She needed to ...
    ```
- `G2-10` (form `(* 10 10)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    Some plans grow gently from the ground up; others are built from the rooftop down, and topple just as fast.

The farmer had a large square market space with stalls arranged in a grid. She needed the total number of stalls to allocate fairly among traders.

She needed to multiply the width by the len...
    ```
- `G2-10` (form `(* 10 10)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    The pail sat steady on Hanna's head as she started down the lane in the orchard.

The farmer had a large square market space with stalls arranged in a grid. She needed the total number of stalls to allocate fairly among traders.

She needed to multiply the width by the length to find the total stall...
    ```
- `G2-11` (form `(str "p" "q" "r")`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    by the orchard, before the cocks had finished crowing, Jadwiga had set out with the milk and a head full of plans.

The milkmaid had three single-character cloth-marks on her shelf. She needed to braid all three together into one continuous strand.

She needed to join three cloth-strands end-to-end ...
    ```

#### BOOL_LEAK_RESOLUTION

- `G2-13` (form `(or false false)`): resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    ```
    by the meadow, the dairy stood between the lane and the meadow, and the day's milk waited to be carried to town.

The farmer had two gates: both were blocked (both false). She wondered if the or-chain would have any way through.

She needed to test if at least one gate opened using the or operator.
...
    ```
- `G2-14` (form `(not false)`): resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    ```
    The pail sat steady on Adela's head as she started down the lane at the edge of the hilltop.

The farmer stood at the gate with the condition false (the gate was blocked). She wondered what would happen if she inverted the condition to the opposite.

She needed to negate the value false, flipping it...
    ```
- `G2-14` (form `(not nil)`): resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    ```
    Long before the market opened its stalls, a young woman had already spent her milk three times in her head.

The farmer held nil (nothing, a falsey value) in her hand. She wondered what the not operator would return if she inverted it.

She needed to negate nil, flipping the falsey value to its trut...
    ```
- `G2-18` (form `(= (quote tortoise) 'tortoise)`): resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

The scribe had two chalk marks: one was written as (quote tortoise), the other as 'tortoise (using the short-hand apostrophe). She wondered if the two chalk marks were equal.

She needed to check i...
    ```
- `G5-19` (form `(every? pos? [1 2 3])`): resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    ```
    Marina had walked this road near the farm a hundred times before, but never quite so dreamily.

The milkmaid held the `pos?` strainer over the pail and let three counts pass through: one, two, three. She watched each piece hit the mesh — all of them were above zero.

She needed to know whether every...
    ```

#### DOUBLED_PLACE

- `G2-20` (form `(count [])`): location stutter: 'farm by the farm...'
    ```
    Tove set out from the farm by the farm with the pail balanced carefully on her head.

The farmer held an empty basket (an empty vector). She walked the rope road from start to finish but found no pails inside. She wondered what the count would be.

She needed to count the elements in an empty collec...
    ```
- `G5-07` (form `(or nil false :found)`): location stutter: 'farm on the farm...'
    ```
    Zenta set out from the farm on the farm with the pail balanced carefully on her head.

The milkmaid stood at a farmyard gate with three latch-checks in sequence. The first latch returned nothing; the second returned false. The third bore a keyword mark.

She needed the gate to stop at the first latc...
    ```
- `G7-07` (form `(try (assert (= 1 2)) (catch Throwable e 0))`): location stutter: 'farm on the farm...'
    ```
    Katarzyna set out from the farm on the farm with the pail balanced carefully on her head.

Bess stopped and checked: 'Do I have one coin on my left and two coins on my right, and they are equal?' No—they were clearly different.

The assertion was false. Would the error be caught, or would the walk f...
    ```
- `G10-07` (form `(->> [1 2 3 4] (filter even?) (map inc) (reduce +))`): location stutter: 'farm on the farm...'
    ```
    Zenta set out from the farm on the farm with the pail balanced carefully on her head.

The farmer had written a longer pail-steps card: strain the pail through a sieve, ladle the results through a tally, and reduce the tallied pours to a single measure. The milkmaid threaded the vector through all t...
    ```

#### SMALL_INT_LEAK

- `G2-21` (form `(count "hare")`): small-int answer 4 leaks via resolution-slot phrasing
    ```
    Runa balanced the pail with the ease of long practice, and at the edge of the hilltop the road stretched out invitingly.

The milkmaid had woven another cloth-label with the name 'lichen' braided end-to-end. She walked this shorter strand from first character to last, counting each knot.

She needed...
    ```
- `G9-02` (form `(do (def counter (atom 0)) (swap! counter inc) @counter)`): small-int answer 1 leaks via resolution-slot phrasing
    ```
    Long before the market opened its stalls, a young woman had already spent her milk three times in her head.

The milkmaid hung a fresh tally-slate by the dairy door with the number 0 chalked at the top — the starting count for the day's deliveries. The first pail went out; the slate needed updating....
    ```

#### HIGH_LENGTH

- `G3-06` (form `(let [a 5 b (* a 2)] b)`): user_msg 213 words
    ```
    The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

The milkmaid had sewn two compartments into her apron-pocket at the start of the morning round: she tucked a count into the first compartment, then reached in to read it while sewing the second compartme...
    ```
- `G3-09` (form `(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))`): user_msg 218 words
    ```
    Every step of the road carried the soft sound of liquid against tin and the louder sound of a daydream gathering speed.

The milkmaid had nailed a three-slot pail-steps card to the market-board under the name add3: three input slots for the morning, midday, and afternoon counts, and a step that summ...
    ```
- `G3-10` (form `(#(+ % 1) 5)`): user_msg 221 words
    ```
    It was the season of new chicks and first cheeses, and every small profit felt like the start of a larger one.

The milkmaid needed a nameless pail-steps card in a hurry and scrawled it in shorthand on a scrap of cheesecloth: a percent mark for whatever count came in, plus one. She passed the scrap ...
    ```
- `G3-10` (form `(#(* %1 %2) 3 4)`): user_msg 201 words
    ```
    Maja hummed quietly by the meadow as she walked, the pail steady and the future already half-spent.

The milkmaid had scrawled a two-slot nameless card in shorthand on a scrap of cheesecloth: first-count mark, second-count mark, and a step that multiplied them. She passed the scrap to the buyer at t...
    ```
- `G3-12` (form `(do (def g 5) (let [g 99] (+ g 1)))`): user_msg 213 words
    ```
    The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

The milkmaid had posted g on the market-board at the village square with a small posting. Later, on a new stretch of road, she tucked a much larger value for g into her apron-pocket and computed g plus o...
    ```

#### FORM_LEAK

- `G4-01` (form `["a" "b"]`): form '["a" "b"]' appears in user_msg of a goal-style subject
    ```
    Ilona set out from the farm near the hilltop with the pail balanced carefully on her head.

The milkmaid reached for the market-basket and placed two labeled jars inside: one compartment held a string marked 'a', another held a string marked 'b'.

She needed a literal sequence of two strings — order...
    ```
- `G4-01` (form `["a" "b"]`): form '["a" "b"]' appears in user_msg of a goal-style subject
    ```
    Sigrid carried more than milk that morning near the meadow; she carried a whole imagined fortune.

The milkmaid reached for the market-basket and placed two labeled jars inside: one compartment held a string marked 'a', another held a string marked 'b'.

She needed a literal sequence of two strings ...
    ```
- `G4-03` (form `(conj [1 2] 3)`): form '(conj [1 2] 3)' appears in user_msg of a goal-style subject
    ```
    Roisin balanced the pail with the ease of long practice, and atop the hilltop the road stretched out invitingly.

The milkmaid carried a market-basket holding two items: the number 1 in the first compartment, the number 2 in the second. She paused at the roadside, thinking to add one more item.

She...
    ```
- `G4-08` (form `(assoc {:a 1} :a 99)`): form '(assoc {:a 1} :a 99)' appears in user_msg of a goal-style subject
    ```
    It was by the village, on a fair-weather morning, that Tegan began the long walk to market.

The milkmaid's first basket had been marked :a and held the value 1. But after the day's business, she needed the :a compartment to hold a new value instead — 69, a much larger prize.

She needed to change t...
    ```
- `G4-09` (form `(dissoc {:a 1 :b 2} :a)`): form '(dissoc {:a 1 :b 2} :a)' appears in user_msg of a goal-style subject
    ```
    The road from the farm to the town was long, and a daydream could fit comfortably along its length.

The milkmaid's market-basket held two labeled compartments: one marked :a held 1, another marked :b held 2. But the buyer no longer needed the :a label — the milkmaid decided to leave that compartmen...
    ```

#### PARAMETRIC_LITERAL_NUMERALS

- `G4-05` (form `(cons 0 '(1 2 3))`): parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    ```
    She had not yet sold the milk and yet had already chosen the ribbons she would wear at the dance.

The milkmaid had spoken a list aloud: one, two, three. But then she realized she had forgotten the starting point — the zero from which the count should begin. She needed to add it to the front.

She n...
    ```
- `G4-05` (form `(cons 0 '(1 2 3))`): parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    ```
    It was in the orchard, on a fair-weather morning, that Gisele began the long walk to market.

The market-basket held cream in the first slot, skim in the second, curds in the third. Gisele
peered in and guessed, "I know what's here." But he asked, "How do you know? Look at
the form for the cons oper...
    ```
- `G4-05` (form `(cons 0 '(1 2 3))`): parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    ```
    Some plans grow gently from the ground up; others are built from the rooftop down, and topple just as fast.

The milkmaid had spoken a list aloud: one, two, three. But then she realized she had forgotten the starting point — the zero from which the count should begin. She needed to add it to the fro...
    ```
- `G5-11` (form `(filter even? [1 2 3 4])`): parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    ```
    The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

One morning, She poured milk through a strainer with no rule written. The strainer
did nothing — every drop fell away, the fresh pail was empty, and the milk pooled cold and useless
on the dairy floor. "...
    ```
- `G5-11` (form `(filter even? [1 2 3 4])`): parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    ```
    Milk does not forgive a tilted head, but a dreaming mind seldom remembers as much.

She stood with a pail of milk and cried, "I can guess which cream belongs in the market
basket!" But he set a milk-strainer between them. "No guessing," he said. "To
keep the even elements from the vector containing ...
    ```

#### CONCEPT_AS_VERB

- `G6-01` (form `(name 'clojure.string)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    It was the season of new chicks and first cheeses, and every small profit felt like the start of a larger one.

She declared, "I will invent new names for the prices each time I visit the market!"
But he only shook his head. "No, Katarzyna. To extract the string form of a quoted namespace symbol, yo...
    ```
- `G6-03` (form `(clojure.string/upper-case "hare")`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    by the farm, before the cocks had finished crowing, Trudi had set out with the milk and a head full of plans.

She declared, "I will invent new names for the prices each time I visit the market!"
But she only shook her head. "No, Trudi. To call the upper-case routine on the clojure.string scroll, ap...
    ```
- `G6-05` (form `(clojure.string/reverse "abc")`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    Every step of the road carried the soft sound of liquid against tin and the louder sound of a daydream gathering speed.

She declared, "I will invent new names for the prices each time I visit the market!"
But he only shook his head. "No, Wanda. To call the reversing function from clojure.string on ...
    ```
- `G6-05` (form `(name :owner/item)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    The cows had given generously that dawn, and the pail was heavier than usual, and the imagination was heavier still.

She declared, "I will invent new names for the prices each time I visit the market!"
But he only shook his head. "No, Mira. To extract the name local portion of a qualified keyword, ...
    ```
- `G6-06` (form `(:private (meta 'x))`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    Some plans grow gently from the ground up; others are built from the rooftop down, and topple just as fast.

She declared, "I will invent new names for the prices each time I visit the market!"
But she only shook her head. "No, Slavena. To check whether the :private flag is present in the metadata o...
    ```

#### HEDGING_NEAR_FORM

- `G6-10` (form `(:deps {:deps {:a 1 :b 2}})`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    By the time Grainne had reached the second milestone in the orchard, the milk had become eggs, and the eggs a flock.

The wager was set by the orchard: produce the value before the breeze had
turned the next leaf. Grainne bolted into a flurry of
guesses, calling out numbers and second-guessing herse...
    ```
- `G6-11` (form `(clojure.string/split "src:test" #":")`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

The wager was set in the orchard: produce the value before the breeze had
turned the next leaf. Lydia bolted into a flurry of
guesses, calling out numbers and second-guessing herself
about whether the go...
    ```
- `G11-05` (form `(do "import is a top-of-file ns clause" :studied)`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    Every step of the road carried the soft sound of liquid against tin and the louder sound of a daydream gathering speed.

The wager was set at the edge of the meadow: produce the value before the breeze had
turned the next leaf. Winifred bolted into a flurry of
guesses, calling out numbers and second...
    ```
- `G11-11` (form `(do "(js/console.log x) calls a JS global; (.-foo o) reads a`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

The wager was set by the orchard: produce the value before the breeze had
turned the next leaf. Lydia bolted into a flurry of
guesses, calling out numbers and second-guessing herself
about whether the go...
    ```
- `G11-11` (form `(do "(js/console.log x) calls a JS global; (.-foo o) reads a`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    The road from the farm to the town was long, and a daydream could fit comfortably along its length.

The wager was set in the market: produce the value before the breeze had
turned the next leaf. Niamh bolted into a flurry of
guesses, calling out numbers and second-guessing herself
about whether the...
    ```

#### ANSWER_LEAK_STRING

- `G7-10` (form `(:doc (meta '^{:doc "adds two"} plus))`): answer string 'adds two' appears in user_msg
    ```
    It was the season of new chicks and first cheeses, and every small profit felt like the start of a larger one.

Clara found an old scroll marking the symbol 'plus' with notes written in the margins: 'adds two'.

She wanted to read the attached documentation note. What words were written in those mar...
    ```

#### CONCEPT_PHRASE_COMMA_LIST

- `G9-03` (form `(do (def a (atom 0)) (swap! a inc) @a)`): concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    Between the dairy and the marketplace stretched a road, a hill, and an entire life imagined into being.

He approached the tally-slate and muttered a form: "The old count is 47. Add 3. The new
count is 50. Write it." In one motion, he read, computed, and wrote. She
watched and asked, "How did you ke...
    ```
- `G9-03` (form `(do (def a (atom 0)) (swap! a inc) @a)`): concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    Long before the market opened its stalls, a young woman had already spent her milk three times in her head.

One morning, three farmers arrived at the slate to update the count. Zara panicked — "Will the count
become a mess?" But he said no. "Each farmer submits a form for atom, swap, and deref — a ...
    ```
- `G9-03` (form `(do (def a (atom 0)) (swap! a inc) @a)`): concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    On market mornings, the dairy yard smelled of damp grass and warm tin, and the future seemed safely arrangeable.

The tally-slate hung by the dairy door, chalked with the day's count: 47 pails. Every farmer who passed
could read it. But when She tried to erase and rewrite it while another farmer was...
    ```
- `G9-03` (form `(do (def a (atom 10)) (swap! a + 5) @a)`): concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    by the farm, before the cocks had finished crowing, Jadwiga had set out with the milk and a head full of plans.

She stood at the dairy door, staring at the tally-slate. "I want to change the count,
but I do not know how," she admitted. Remigius smiled and placed a form in
her hand. "Here. This form...
    ```
- `G9-03` (form `(do (def a (atom 10)) (swap! a + 5) @a)`): concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    It was on the farm, on a fair-weather morning, that Sigrid began the long walk to market.

One morning, three farmers arrived at the slate to update the count. Sigrid panicked — "Will the count
become a mess?" But he said no. "Each farmer submits a form for atom, swap, deref — a form
that reads the ...
    ```

#### DOUBLE_PREP

- `G9-18` (form `(do (def lock (Object.)) (locking lock 42))`): verb+preposition followed by {place} which already carries its own preposition
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

The farmer showed the milkmaid the simplest possible padlocked section: just a plain value inside the lock. The padlock was real — it acquired the monitor — but the body needed no computation.

She...
    ```

