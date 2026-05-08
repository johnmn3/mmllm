# dog-shadow curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

### G1-01: Eval as substitution

- examples: 4
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 5, 'AS_ONE_WHO_CADENCE': 2, 'LOW_GROUNDING': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`42` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose
    - [AS_ONE_WHO_CADENCE] form=`42` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [FOREIGN_FABLE_IMAGERY] form=`0` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`"hello"` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose
    - [AS_ONE_WHO_CADENCE] form=`"hello"` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [FOREIGN_FABLE_IMAGERY] form=`"hello"` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose

### G1-02: Integer numbers

- examples: 6
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 10, 'LOW_GROUNDING': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`7` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`7` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`7` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`0` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`0` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`0` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into dog-shadow prose

### G1-03: Ratios

- examples: 5
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 5, 'LOW_GROUNDING': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`1/2` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`1/2` — tortoise-hare-specific imagery 'leather notebook' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`1/2` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`3/4` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`(+ 1/2 1/4)` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`(- 1 1/3)` — tortoise-hare-specific imagery 'leather notebook' leaks into dog-shadow prose

### G1-04: Strings

- examples: 5
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 6, 'AS_ONE_WHO_CADENCE': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`"hello"` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`"hello"` — tortoise-hare-specific imagery 'leather notebook' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`"race"` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    - [AS_ONE_WHO_CADENCE] form=`"slow and steady"` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [FOREIGN_FABLE_IMAGERY] form=`"slow and steady"` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`""` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose

### G1-05: Booleans

- examples: 6
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 5, 'LOW_GROUNDING': 2, 'AS_ONE_WHO_CADENCE': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`true` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`true` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [AS_ONE_WHO_CADENCE] form=`false` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [FOREIGN_FABLE_IMAGERY] form=`false` — tortoise-hare-specific imagery 'leather notebook' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`false` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [AS_ONE_WHO_CADENCE] form=`false` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G1-06: nil

- examples: 5
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 8, 'LOW_GROUNDING': 3, 'AS_ONE_WHO_CADENCE': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`nil` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`nil` — tortoise-hare-specific imagery 'leather notebook' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`nil` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(nil? nil)` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose
    - [AS_ONE_WHO_CADENCE] form=`(nil? nil)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [FOREIGN_FABLE_IMAGERY] form=`(nil? nil)` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose

### G1-07: Keywords

- examples: 5
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 6, 'AS_ONE_WHO_CADENCE': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`:hare` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`:hare` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`:tortoise` — tortoise-hare-specific imagery 'leather notebook' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`:winner` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into dog-shadow prose
    - [AS_ONE_WHO_CADENCE] form=`:winner` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [FOREIGN_FABLE_IMAGERY] form=`(keyword? :hare)` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose

### G1-08: Characters

- examples: 4
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 5}
    - [FOREIGN_FABLE_IMAGERY] form=`\h` — tortoise-hare-specific imagery 'leather notebook' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`\h` — tortoise-hare-specific imagery 'leather notebook' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`\T` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`\T` — tortoise-hare-specific imagery 'leather notebook' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`(char? \h)` — tortoise-hare-specific imagery 'leather notebook' leaks into dog-shadow prose

### G1-09: Symbols vs values

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'CAP_PRONOUN_MID_SENTENCE': 7, 'POST_COMMA_CAPITAL_PRONOUN': 7, 'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 3, 'BOOL_LEAK_RESOLUTION': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(symbol? 'hare)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(symbol? 'hare)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(symbol? 'hare)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(symbol? 'hare)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(symbol? 42)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(symbol? 42)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G1-10: Comments

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 5, 'CLAUSE_STACK_OVERFLOW': 2, 'CAP_PRONOUN_MID_SENTENCE': 4, 'POST_COMMA_CAPITAL_PRONOUN': 4, 'LOW_GROUNDING': 1}
    - [HIGH_LENGTH] form=`(+ 1 2) ;; sum of one and two` — user_msg 218 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2) ;; sum of one and two` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(+ 1 2) ;; sum of one and two` — sentence with 5 commas reads as AI-output cadence: 'To add 2 and 9, with a double-semicolon trailing comment, she, her promise small'
    - [CAP_PRONOUN_MID_SENTENCE] form=`(+ 1 2) ;; sum of one and two` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(+ 1 2) ;; sum of one and two` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(+ 1 2) ;; sum of one and two` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-11: Whitespace doesn't matter

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'HIGH_LENGTH': 1, 'THE_FORM_OVERUSE': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+    1    2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '9'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(+    1    2)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(+    1    2)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+    1    2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '8'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(+    1    2)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(+    1    2)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G1-12: Parens group; they don't multiply

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'STORY_RESOLUTION_NO_DRAWN': 5, 'CLAUSE_STACK_OVERFLOW': 1, 'AS_ONE_WHO_CADENCE': 1, 'HIGH_LENGTH': 1, 'ANSWER_LEAK': 2}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(+ 2 3)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(+ 2 3)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '7'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(+ 2 3)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(+ 2 3)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G1-13: First arithmetic call

- examples: 6
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 18, 'CAP_PRONOUN_MID_SENTENCE': 4, 'POST_COMMA_CAPITAL_PRONOUN': 4, 'REPL_AS_TIME_TRAVELLER': 3, 'AS_ONE_WHO_CADENCE': 2, 'SENTENCE_START_LOWER_PRONOUN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '7'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(+ 1 2)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(+ 1 2)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '8'), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(+ 1 2)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '5'), resolution doesn't close the loop)

### G1-14: Nested call evaluation

- examples: 4
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'STORY_RESOLUTION_NO_DRAWN': 12, 'ANSWER_LEAK': 1, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'REPL_AS_TIME_TRAVELLER': 2, 'AS_ONE_WHO_CADENCE': 1}
    - [HIGH_LENGTH] form=`(+ 1 (* 2 3))` — user_msg 217 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (* 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (* 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '8'), resolution doesn't close the loop)
    - [ANSWER_LEAK] form=`(+ 1 (* 2 3))` — answer 7 in narrative
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (* 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '7'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(* (+ 1 2) (+ 3 4))` — user_msg 209 words

### G1-15: Equality

- examples: 6
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'LOW_GROUNDING': 7, 'STORY_RESOLUTION_NO_DRAWN': 13}
    - [WRONG_FABLE_LITERAL] form=`(= 1 1)` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [LOW_GROUNDING] form=`(= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '7'), resolution doesn't close the loop)

### G1-16: Numeric predicates

- examples: 6
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 16, 'REPL_AS_TIME_TRAVELLER': 2, 'CAP_PRONOUN_MID_SENTENCE': 7, 'POST_COMMA_CAPITAL_PRONOUN': 7, 'LOW_GROUNDING': 1, 'BOOL_LEAK_RESOLUTION': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(zero? 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(zero? 0)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [CAP_PRONOUN_MID_SENTENCE] form=`(zero? 0)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(zero? 0)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(zero? 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(zero? 5)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G1-17: Printing vs returning

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`42` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('52',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`42` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('82',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`42` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`42` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`42` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('78',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '3'), resolution doesn't close the loop)

### G1-18: Errors are safe in the REPL

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'STORY_RESOLUTION_NO_DRAWN': 4, 'HIGH_LENGTH': 1, 'AS_ONE_WHO_CADENCE': 1, 'LOW_GROUNDING': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(+ 1 2)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(+ 1 2)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '6'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(+ 1 2)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(+ 1 2)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

## Grade 2

### G2-01: Multi-arg arithmetic

- examples: 6
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'STORY_RESOLUTION_NO_DRAWN': 17, 'CLAUSE_STACK_OVERFLOW': 5, 'REPL_AS_TIME_TRAVELLER': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(+ 1 2 3 4)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(+ 1 2 3 4)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '3', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 2 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '5'), resolution doesn't close the loop)

### G2-02: Comparison chains

- examples: 5
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'HIGH_LENGTH': 4, 'BOOL_LEAK_RESOLUTION': 1, 'REPL_AS_TIME_TRAVELLER': 1, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'LOW_GROUNDING': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(< 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '4'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(< 1 2 3)` — user_msg 203 words
    - [BOOL_LEAK_RESOLUTION] form=`(< 1 2 3)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [STORY_RESOLUTION_NO_DRAWN] form=`(< 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '6', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(< 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '8'), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(< 3 2 1)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

### G2-03: not= and = with multiple args

- examples: 5
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 13, 'LOW_GROUNDING': 4, 'REPL_AS_TIME_TRAVELLER': 4, 'BOOL_LEAK_RESOLUTION': 2, 'CLAUSE_STACK_OVERFLOW': 2, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not= 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '8'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(not= 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [REPL_AS_TIME_TRAVELLER] form=`(not= 1 2)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not= 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '3'), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(not= 1 1)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not= 1 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '9'), resolution doesn't close the loop)

### G2-04: min and max

- examples: 5
- variety @ n=50: 1.00
- issues: {'REPL_AS_TIME_TRAVELLER': 1, 'STORY_RESOLUTION_NO_DRAWN': 14, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'CLAUSE_STACK_OVERFLOW': 2}
    - [REPL_AS_TIME_TRAVELLER] form=`(min 1 2 3)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(min 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '3', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(min 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(min 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '8', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(max 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '8', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(max 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '7'), resolution doesn't close the loop)

### G2-05: quot, rem, mod

- examples: 6
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 18, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'REPL_AS_TIME_TRAVELLER': 3, 'SMALL_INT_LEAK': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(quot 17 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '17'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(quot 17 5)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(quot 17 5)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(quot 17 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '-15'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(quot 17 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '5'), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(rem 17 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

### G2-06: inc and dec

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 11, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'REPL_AS_TIME_TRAVELLER': 2}
    - [LOW_GROUNDING] form=`(inc 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inc 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inc 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(dec 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(dec 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inc 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)

### G2-07: Absolute value

- examples: 4
- variety @ n=50: 1.00
- issues: {'REPL_AS_TIME_TRAVELLER': 3, 'AS_ONE_WHO_CADENCE': 2, 'STORY_RESOLUTION_NO_DRAWN': 8, 'LOW_GROUNDING': 4}
    - [REPL_AS_TIME_TRAVELLER] form=`(abs 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [AS_ONE_WHO_CADENCE] form=`(abs 5)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [REPL_AS_TIME_TRAVELLER] form=`(abs 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(abs 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(abs 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(abs 5)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G2-08: Arithmetic on ratios

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 9, 'CLAUSE_STACK_OVERFLOW': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'REPL_AS_TIME_TRAVELLER': 1}
    - [LOW_GROUNDING] form=`(+ 1/2 1/4)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1/2 1/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1/2 1/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(+ 1/2 1/4)` — sentence with 5 commas reads as AI-output cadence: 'To add one-half and one-quarter, he, her breath even, her step even, her thought'
    - [CAP_PRONOUN_MID_SENTENCE] form=`(+ 1/2 1/4)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(+ 1/2 1/4)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G2-09: Floats vs ints (the / operator)

- examples: 3
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'STORY_RESOLUTION_NO_DRAWN': 9, 'REPL_AS_TIME_TRAVELLER': 2}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(/ 10 2)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(/ 10 2)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(/ 10 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '-16'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(/ 10 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-18',), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(/ 10 2)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(/ 10 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '10'), resolution doesn't close the loop)

### G2-10: Powers via repeated multiplication

- examples: 4
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'CAP_PRONOUN_MID_SENTENCE': 4, 'POST_COMMA_CAPITAL_PRONOUN': 4, 'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [CLAUSE_STACK_OVERFLOW] form=`(* 2 2 2)` — sentence with 5 commas reads as AI-output cadence: 'To multiply 2 by itself three times, she, her breath even, her step even, her th'
    - [CAP_PRONOUN_MID_SENTENCE] form=`(* 2 2 2)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(* 2 2 2)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(* 2 2 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 2 2 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '4', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 5 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3'), resolution doesn't close the loop)

### G2-11: String concatenation with str

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 5, 'AS_ONE_WHO_CADENCE': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(str "ab" "cd")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('saffron', 'indigo'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(str "ab" "cd")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('harbor', 'myrrh'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(str "ab" "cd")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('feather', 'ochre'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(str 42)` — sentence with 5 commas reads as AI-output cadence: 'Concat two strips\ntogether, and the marks are spliced; cut a substring out, and\n'
    - [CLAUSE_STACK_OVERFLOW] form=`(str 42)` — sentence with 5 commas reads as AI-output cadence: 'Concat two strips\ntogether, and the marks are spliced; cut a substring out, and\n'
    - [AS_ONE_WHO_CADENCE] form=`(str "p" "q" "r")` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G2-12: print and println — return values

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 1, 'AS_ONE_WHO_CADENCE': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(println "hello")` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(println "hello")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(println "hello")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('amber',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(println "hello")` — user_msg 202 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(println "hello")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('feather',), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(println "hello")` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G2-13: and / or — short circuit, return values

- examples: 6
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 3, 'LOW_GROUNDING': 8, 'STORY_RESOLUTION_NO_DRAWN': 5, 'CLAUSE_STACK_OVERFLOW': 3}
    - [BOOL_LEAK_RESOLUTION] form=`(and true true)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(and true false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [BOOL_LEAK_RESOLUTION] form=`(and true false)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(and true false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-14: not — turning truthy to false

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 8, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)

### G2-15: Falsey values: only false and nil

- examples: 4
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'STORY_RESOLUTION_NO_DRAWN': 12, 'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [WRONG_FABLE_LITERAL] form=`(if 0 1 0)` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if 0 1 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(if 0 1 0)` — user_msg 211 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if 0 1 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '8', '6'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(if 0 1 0)` — sentence with 5 commas reads as AI-output cadence: 'To use if to return 8 when the condition is 0 (then-branch) and 0 otherwise (els'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if 0 1 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)

### G2-16: Truthy 0 and empty string

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5, 'LOW_GROUNDING': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(boolean "")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean "")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('coral',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(boolean "")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean "")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('coral',), resolution doesn't close the loop)

### G2-17: Keyword as function for map lookup

- examples: 3
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 6, 'AS_ONE_WHO_CADENCE': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(:hare {:hare 1 :tortoise 2})` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(:hare {:hare 1 :tortoise 2})` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:hare {:hare 1 :tortoise 2})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '7', ':doe'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(:hare {:hare 1 :tortoise 2})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:hare {:hare 1 :tortoise 2})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '11', ':wren'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(:hare {:hare 1 :tortoise 2})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-18: Quoting symbols

- examples: 3
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'LOW_GROUNDING': 6, 'HIGH_LENGTH': 2, 'BOOL_LEAK_RESOLUTION': 2, 'CLAUSE_STACK_OVERFLOW': 7, 'STORY_RESOLUTION_NO_DRAWN': 3, 'AS_ONE_WHO_CADENCE': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(symbol? (quote hare))` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(symbol? (quote hare))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(symbol? (quote hare))` — user_msg 229 words
    - [BOOL_LEAK_RESOLUTION] form=`(symbol? (quote hare))` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [CLAUSE_STACK_OVERFLOW] form=`(symbol? (quote hare))` — sentence with 5 commas reads as AI-output cadence: 'To ask whether long-form quoting of the name hare produces a symbol, using symbo'

### G2-19: Auto-promotion to bigint

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'REPL_AS_TIME_TRAVELLER': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 1000000 1000000)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('1048576', '1048576'), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(* 1000000 1000000)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 1000000 1000000)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('100000000000', '100000000000'), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(* 1000000 1000000)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 1000000 1000000)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9007199254740992', '9007199254740992'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 99999999999 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16777216', '4'), resolution doesn't close the loop)

### G2-20: Counting

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 6, 'HIGH_LENGTH': 1, 'AS_ONE_WHO_CADENCE': 2}
    - [LOW_GROUNDING] form=`(count [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '7'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3])` — sentence with 9 commas reads as AI-output cadence: 'The runtime does this for any collection — vector, list, map,\nstring." To count '
    - [LOW_GROUNDING] form=`(count [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '7', '11'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3])` — sentence with 9 commas reads as AI-output cadence: 'The runtime does this for any collection — vector, list, map,\nstring." To count '

### G2-21: String length and substring

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'CLAUSE_STACK_OVERFLOW': 2, 'AS_ONE_WHO_CADENCE': 1, 'HIGH_LENGTH': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('alder',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(count "tortoise")` — sentence with 5 commas reads as AI-output cadence: 'Concat two strips\ntogether, and the marks are spliced; cut a substring out, and\n'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('river',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(count "tortoise")` — sentence with 5 commas reads as AI-output cadence: 'Concat two strips\ntogether, and the marks are spliced; cut a substring out, and\n'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('willow',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('pebble',), resolution doesn't close the loop)

### G2-22: Compose pure arithmetic (multi-step calculation)

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 2, 'ANSWER_LEAK': 2, 'REPL_AS_TIME_TRAVELLER': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(- (* 5 4) 7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '6', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(- (* 5 4) 7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(- (* 5 4) 7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '9', '6'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(+ (* 3 8) (* 2 4))` — user_msg 211 words
    - [ANSWER_LEAK] form=`(+ (* 3 8) (* 2 4))` — answer 32 in narrative
    - [HIGH_LENGTH] form=`(+ (* 3 8) (* 2 4))` — user_msg 210 words

## Grade 3

### G3-01: def — top-level binding

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def x 42) x)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (def x 42) x)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 42) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('28',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 42) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('36',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 42) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('52',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def y 7) y)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)

### G3-02: def — redefinition

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 1) (def x 99) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('78',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 1) (def x 99) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '47'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 1) (def x 99) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('73',), resolution doesn't close the loop)

### G3-03: let — local binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 3, 'STORY_RESOLUTION_NO_DRAWN': 8, 'THE_FORM_OVERUSE': 2}
    - [HIGH_LENGTH] form=`(let [x 3] (+ x 1))` — user_msg 263 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 3] (+ x 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '8'), resolution doesn't close the loop)
    - [THE_FORM_OVERUSE] form=`(let [x 3] (+ x 1))` — `the form` appears 6 times in user_msg (template tic — vary references)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 3] (+ x 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [n 10] (* n n))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(let [n 10] (* n n))` — user_msg 249 words

### G3-04: let — multi-binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'HIGH_LENGTH': 3, 'CLAUSE_STACK_OVERFLOW': 3, 'ANSWER_LEAK': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 1 b 2] (+ a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 1 b 2] (+ a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 1 b 2] (+ a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '8'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(let [x 5 y 3] (- x y))` — user_msg 223 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 5 y 3] (- x y))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '7'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(let [x 5 y 3] (- x y))` — sentence with 5 commas reads as AI-output cadence: 'To bind x to 4 and y to 7, then subtract y from x, he, with steady, careful step'

### G3-05: let — shadowing outer def

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 1, 'THE_FORM_OVERUSE': 1, 'CLAUSE_STACK_OVERFLOW': 2}
    - [LOW_GROUNDING] form=`(do (def x 10) (let [x 99] x))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 10) (let [x 99] x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '93'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 10) (let [x 99] x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '31'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(do (def x 10) (let [x 99] x))` — user_msg 221 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 10) (let [x 99] x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '70'), resolution doesn't close the loop)
    - [THE_FORM_OVERUSE] form=`(do (def x 10) (let [x 99] x))` — `the form` appears 5 times in user_msg (template tic — vary references)

### G3-06: let — binding can reference prior

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'AS_ONE_WHO_CADENCE': 2, 'HIGH_LENGTH': 4, 'THE_FORM_OVERUSE': 4, 'CLAUSE_STACK_OVERFLOW': 5, 'ANSWER_LEAK': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 5 b (* a 2)] b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(let [a 5 b (* a 2)] b)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [HIGH_LENGTH] form=`(let [a 5 b (* a 2)] b)` — user_msg 267 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 5 b (* a 2)] b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [THE_FORM_OVERUSE] form=`(let [a 5 b (* a 2)] b)` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a 5 b (* a 2)] b)` — sentence with 5 commas reads as AI-output cadence: 'To bind a to 5, then bind b to twice a, and return b, she, in the slow rhythm of'

### G3-07: fn — anonymous function

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'AS_ONE_WHO_CADENCE': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'CONCEPT_AS_VERB': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (+ x 1)) 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (+ x 1)) 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`((fn [x] (+ x 1)) 4)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (+ x 1)) 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`((fn [a b] (* a b)) 3 4)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`((fn [a b] (* a b)) 3 4)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G3-08: fn — multi-arg

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'HIGH_LENGTH': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`((fn [a b c] (+ a b c)) 1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'To create an anonymous function with three parameters that adds them and apply i'
    - [HIGH_LENGTH] form=`((fn [a b c] (+ a b c)) 1 2 3)` — user_msg 208 words
    - [CLAUSE_STACK_OVERFLOW] form=`((fn [a b c] (+ a b c)) 1 2 3)` — sentence with 7 commas reads as AI-output cadence: 'To create an anonymous function with three parameters that adds them and apply i'

### G3-09: defn — shorthand

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'HIGH_LENGTH': 1, 'AS_ONE_WHO_CADENCE': 1}
    - [LOW_GROUNDING] form=`(do (defn dbl [x] (* x 2)) (dbl 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defn dbl [x] (* x 2)) (dbl 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn dbl [x] (* x 2)) (dbl 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '7'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — sentence with 6 commas reads as AI-output cadence: 'To define a function add3 that adds three arguments, then call it with 4, 8, and'
    - [HIGH_LENGTH] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — user_msg 257 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — sentence with 6 commas reads as AI-output cadence: 'To define a function add3 that adds three arguments, then call it with 9, 8, and'

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'CONCEPT_AS_VERB': 3}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(#(+ % 1) 5)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(#(+ % 1) 5)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CONCEPT_AS_VERB] form=`(#(+ % 1) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CAP_PRONOUN_MID_SENTENCE] form=`(#(+ % 1) 5)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(#(+ % 1) 5)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CONCEPT_AS_VERB] form=`(#(+ % 1) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G3-11: Substitution rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 2, 'HIGH_LENGTH': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 7] (+ a a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 7] (+ a a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`((fn [x] (* x x)) 6)` — user_msg 229 words

### G3-12: Scope vs namespace

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def g 5) (let [g 99] (+ g 1)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '84', '8'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def g 5) (let [g 99] (+ g 1)))` — sentence with 6 commas reads as AI-output cadence: 'To define g at the top level, shadow it in a let with a different value, and com'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def g 5) (let [g 99] (+ g 1)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('55',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def g 5) (let [g 99] (+ g 1)))` — sentence with 5 commas reads as AI-output cadence: 'The next dog along the bank\nreads the freshest scratch — whatever the latest mar'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def g 5) (let [g 99] (+ g 1)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('30',), resolution doesn't close the loop)

### G3-13: fn body returns last form

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 2}
    - [HIGH_LENGTH] form=`((fn [x] x x x 99) 1)` — user_msg 252 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] x x x 99) 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`((fn [x] x x x 99) 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] x x x 99) 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`((fn [x] x x x 99) 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] x x x 99) 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99',), resolution doesn't close the loop)

### G3-14: do form

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'LOW_GROUNDING': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(do 1 2 3)` — user_msg 226 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '8'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do 1 2 3)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do 1 2 3)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '8'), resolution doesn't close the loop)

### G3-15: Side-effects in body

- examples: 1
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1, 'SENTENCE_START_LOWER_PRONOUN': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [WRONG_FABLE_LITERAL] form=`(do (println "hi") 42)` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [LOW_GROUNDING] form=`(do (println "hi") 42)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (println "hi") 42)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('65', 'thread'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(do (println "hi") 42)` — user_msg 230 words
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do (println "hi") 42)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (println "hi") 42)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('71', 'coral'), resolution doesn't close the loop)

### G3-16: Name collision: namespace vs let

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [+ 99] +)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('49',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(let [+ 99] +)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [+ 99] +)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('32',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [+ 99] +)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('50',), resolution doesn't close the loop)

### G3-17: Naming conventions (kebab-case)

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [hare-speed 4 tortoise-speed 1] (- hare-speed` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [hare-speed 4 tortoise-speed 1] (- hare-speed` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '6'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(let [hare-speed 4 tortoise-speed 1] (- hare-speed` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(let [hare-speed 4 tortoise-speed 1] (- hare-speed` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [hare-speed 4 tortoise-speed 1] (- hare-speed` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)

### G3-18: When to name vs inline

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5, 'AS_ONE_WHO_CADENCE': 1, 'HIGH_LENGTH': 2, 'THE_FORM_OVERUSE': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [n 5] (* n n n))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(let [n 5] (* n n n))` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [n 5] (* n n n))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(let [n 5] (* n n n))` — user_msg 243 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [n 5] (* n n n))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [THE_FORM_OVERUSE] form=`(let [n 5] (* n n n))` — `the form` appears 5 times in user_msg (template tic — vary references)

## Grade 4

### G4-01: Vector literal

- examples: 3
- variety @ n=50: 1.00
- issues: {'PARAMETRIC_LITERAL_NUMERALS': 3, 'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [PARAMETRIC_LITERAL_NUMERALS] form=`[1 2 3]` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [LOW_GROUNDING] form=`[1 2 3]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`[1 2 3]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '7'), resolution doesn't close the loop)
    - [PARAMETRIC_LITERAL_NUMERALS] form=`[1 2 3]` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [STORY_RESOLUTION_NO_DRAWN] form=`[1 2 3]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '12', '4'), resolution doesn't close the loop)
    - [PARAMETRIC_LITERAL_NUMERALS] form=`[1 2 3]` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces

### G4-02: nth — vector access

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 4, 'CLAUSE_STACK_OVERFLOW': 2, 'LOW_GROUNDING': 2, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(nth [10 20 30] 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '19', '19'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(nth [10 20 30] 0)` — sentence with 5 commas reads as AI-output cadence: 'To get the element at index 0 of a vector containing 10, 20, and 30, she, with t'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(nth [10 20 30] 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '13', '15'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(nth [10 20 30] 0)` — sentence with 5 commas reads as AI-output cadence: 'To get the element at index 0 of a vector containing 10, 20, and 30, he, as a fi'
    - [LOW_GROUNDING] form=`(nth [10 20 30] 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(nth [10 20 30] 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '9', '4'), resolution doesn't close the loop)

### G4-03: conj — append to vector

- examples: 2
- variety @ n=50: 1.00
- issues: {'PARAMETRIC_LITERAL_NUMERALS': 3, 'STORY_RESOLUTION_NO_DRAWN': 6, 'AS_ONE_WHO_CADENCE': 2, 'LOW_GROUNDING': 2}
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(conj [1 2] 3)` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [STORY_RESOLUTION_NO_DRAWN] form=`(conj [1 2] 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '6', '17'), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(conj [1 2] 3)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(conj [1 2] 3)` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [STORY_RESOLUTION_NO_DRAWN] form=`(conj [1 2] 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '6', '18'), resolution doesn't close the loop)
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(conj [1 2] 3)` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces

### G4-04: List literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 1, 'HANGING_FORM_THAT': 1, 'LOW_GROUNDING': 2}
    - [CAP_PRONOUN_MID_SENTENCE] form=`'(1 2 3)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`'(1 2 3)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '7', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '9', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '14'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`'(1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'To create a list containing 1, 2, and 3\nproperly, he wrote a list literal carefu'

### G4-05: cons — prepend to seq

- examples: 1
- variety @ n=50: 1.00
- issues: {'PARAMETRIC_LITERAL_NUMERALS': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 1}
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(cons 0 '(1 2 3))` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cons 0 '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '17', '9'), resolution doesn't close the loop)
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(cons 0 '(1 2 3))` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cons 0 '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '10', '6'), resolution doesn't close the loop)
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(cons 0 '(1 2 3))` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [LOW_GROUNDING] form=`(cons 0 '(1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-06: Map literal

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`{:hare 1 :tortoise 2}` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`{:hare 1 :tortoise 2}` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '3', ':raspberry'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`{:hare 1 :tortoise 2}` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`{:hare 1 :tortoise 2}` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '12', '12'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`{:hare 1 :tortoise 2}` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`{:hare 1 :tortoise 2}` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '20', '6'), resolution doesn't close the loop)

### G4-07: get — map lookup

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 3}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(get {:a 1 :b 2} :a)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(get {:a 1 :b 2} :a)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(get {:a 1 :b 2} :a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '5', ':raspberry'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(get {:a 1 :b 2} :a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '19', '9'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(get {:a 1 :b 2} :a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(get {:a 1 :b 2} :a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '14', '10'), resolution doesn't close the loop)

### G4-08: assoc — map update

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5, 'LOW_GROUNDING': 2, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(assoc {:a 1} :b 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '11', '4'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(assoc {:a 1} :b 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(assoc {:a 1} :b 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', ':persimmon', ':guava'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(assoc {:a 1} :b 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(assoc {:a 1} :b 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', ':kiwi', ':apricot'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(assoc {:a 1} :a 99)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G4-09: dissoc — map remove key

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 2}
    - [LOW_GROUNDING] form=`(dissoc {:a 1 :b 2} :a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(dissoc {:a 1 :b 2} :a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '10', ':plum'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(dissoc {:a 1 :b 2} :a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(dissoc {:a 1 :b 2} :a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '5', ':kumquat'), resolution doesn't close the loop)

### G4-10: keys and vals

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 2, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (keys {:a 1 :b 2 :c 3}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '7', ':tangerine'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(count (keys {:a 1 :b 2 :c 3}))` — sentence with 5 commas reads as AI-output cadence: 'To count how many keys are in a map binding :a, :b, and :c, she, with the soft p'
    - [LOW_GROUNDING] form=`(count (keys {:a 1 :b 2 :c 3}))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (keys {:a 1 :b 2 :c 3}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '13', ':peach'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (keys {:a 1 :b 2 :c 3}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '7', ':berry'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(count (keys {:a 1 :b 2 :c 3}))` — sentence with 5 commas reads as AI-output cadence: 'To count how many keys are in a map binding :a, :b, and :c\nproperly, he wrote co'

### G4-11: Set literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(count #{1 2 3})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count #{1 2 3})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '8', '5'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count #{1 2 3})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count #{1 2 3})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '15', '20'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count #{1 2 3})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count #{1 2 3})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13',), resolution doesn't close the loop)

### G4-12: Set membership

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 1, 'LOW_GROUNDING': 1, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(contains? #{1 2 3} 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '18', '12'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(contains? #{1 2 3} 2)` — sentence with 5 commas reads as AI-output cadence: 'To check whether 2 is a member of a set containing 1, 2, and 3\nproperly, he wrot'
    - [LOW_GROUNDING] form=`(contains? #{1 2 3} 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(contains? #{1 2 3} 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '9', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(contains? #{1 2 3} 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '9', '3'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(contains? #{1 2 3} 4)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G4-13: count — universal

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 11, 'CLAUSE_STACK_OVERFLOW': 3, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3 4 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '15', '15'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3 4 5])` — sentence with 7 commas reads as AI-output cadence: 'To count the elements in a vector containing 1, 2, 3, 4, and 5, he, as a hen sit'
    - [CAP_PRONOUN_MID_SENTENCE] form=`(count [1 2 3 4 5])` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(count [1 2 3 4 5])` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3 4 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '14', '6'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(count {:a 1 :b 2})` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G4-14: empty?

- examples: 3
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 3, 'STORY_RESOLUTION_NO_DRAWN': 9, 'AS_ONE_WHO_CADENCE': 2, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'LOW_GROUNDING': 2}
    - [BOOL_LEAK_RESOLUTION] form=`(empty? [])` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [STORY_RESOLUTION_NO_DRAWN] form=`(empty? [])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '3', '16'), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(empty? [])` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [STORY_RESOLUTION_NO_DRAWN] form=`(empty? [])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '4', '17'), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(empty? [])` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [CAP_PRONOUN_MID_SENTENCE] form=`(empty? [])` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G4-15: first, rest, last

- examples: 3
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 8, 'CLAUSE_STACK_OVERFLOW': 4, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [WRONG_FABLE_LITERAL] form=`(first [10 20 30])` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [LOW_GROUNDING] form=`(first [10 20 30])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first [10 20 30])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '6', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first [10 20 30])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('19', '16', '20'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(first [10 20 30])` — sentence with 6 commas reads as AI-output cadence: 'To get the first element of a vector containing 10, 20, and 30, she, neither res'
    - [CAP_PRONOUN_MID_SENTENCE] form=`(first [10 20 30])` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G4-16: into and conj on collections

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 4, 'POST_COMMA_CAPITAL_PRONOUN': 4, 'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(into [] '(1 2 3))` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(into [] '(1 2 3))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(into [] '(1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '15', '20'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(into [] '(1 2 3))` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(into [] '(1 2 3))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G4-17: Immutability — assoc returns new

- examples: 1
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(let [m {:a 1}] (assoc m :a 99) m)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(let [m {:a 1}] (assoc m :a 99) m)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :a 99) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '7', '95'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :a 99) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('11', '16', '69'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(let [m {:a 1}] (assoc m :a 99) m)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :a 99) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '5', '76'), resolution doesn't close the loop)

### G4-18: Equality of vectors and lists

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(= [1 2 3] '(1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= [1 2 3] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '6', '5'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(= [1 2 3] '(1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= [1 2 3] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '8', '14'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(= [1 2 3] '(1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= [1 2 3] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '6', '18'), resolution doesn't close the loop)

### G4-19: range and seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5, 'CLAUSE_STACK_OVERFLOW': 2, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (range 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(count (range 5))` — sentence with 6 commas reads as AI-output cadence: 'The range is a promise of five bones (0, 1, 2, 3, 4), and count consumes that pr'
    - [CAP_PRONOUN_MID_SENTENCE] form=`(count (range 5))` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(count (range 5))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (range 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(count (range 5))` — sentence with 6 commas reads as AI-output cadence: 'The range is a promise of five bones (0, 1, 2, 3, 4), and count consumes that pr'

### G4-20: Collection vs sequence

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 2, 'AS_ONE_WHO_CADENCE': 1, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (seq [1 2 3]))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '7'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(count (seq [1 2 3]))` — sentence with 5 commas reads as AI-output cadence: 'To convert a vector containing 1, 2, and 3 to a sequence and count its elements\n'
    - [AS_ONE_WHO_CADENCE] form=`(count (seq [1 2 3]))` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [CAP_PRONOUN_MID_SENTENCE] form=`(count (seq [1 2 3]))` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(count (seq [1 2 3]))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (seq [1 2 3]))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '7', '11'), resolution doesn't close the loop)

## Grade 5

### G5-01: if

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'CLAUSE_STACK_OVERFLOW': 2, 'LOW_GROUNDING': 3, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'HIGH_LENGTH': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if true :a :b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':b', ':open'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(if true :a :b)` — sentence with 5 commas reads as AI-output cadence: 'The runtime checks the\ncondition, walks the right arm, and the unrun arm is just'
    - [LOW_GROUNDING] form=`(if true :a :b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if true :a :b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':x', ':west'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(if true :a :b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if true :a :b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':delta', ':south'), resolution doesn't close the loop)

### G5-02: if as expression

- examples: 1
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(+ 1 (if true 10 20))` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(+ 1 (if true 10 20))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (if true 10 20))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '10'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(+ 1 (if true 10 20))` — user_msg 253 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (if true 10 20))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '13', '19'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (if true 10 20))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '4', '17'), resolution doesn't close the loop)

### G5-03: when

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'STORY_RESOLUTION_NO_DRAWN': 6, 'AS_ONE_WHO_CADENCE': 1, 'LOW_GROUNDING': 2}
    - [HIGH_LENGTH] form=`(when true :yes)` — user_msg 218 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true :yes)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':north',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true :yes)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':low',), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(when true :yes)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [LOW_GROUNDING] form=`(when true :yes)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true :yes)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':north',), resolution doesn't close the loop)

### G5-04: cond

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '3', '6'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', ':far', ':high'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '8', '3'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — sentence with 5 commas reads as AI-output cadence: 'Whatever the condition evaluates to, that\ndecides." To walk three condition-ston'

### G5-05: cond — :else

- examples: 1
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'LOW_GROUNDING': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(cond false :a false :b :else :c)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(cond false :a false :b :else :c)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(cond false :a false :b :else :c)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(cond false :a false :b :else :c)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(cond false :a false :b :else :c)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(cond false :a false :b :else :c)` — sentence with 5 commas reads as AI-output cadence: 'The runtime checks the\ncondition, walks the right arm, and the unrun arm is just'

### G5-06: case

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 3}
    - [LOW_GROUNDING] form=`(case 2 1 :one 2 :two 3 :three :default)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(case 2 1 :one 2 :two 3 :three :default)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '6', ':c'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(case 2 1 :one 2 :two 3 :three :default)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '9', '5'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(case 2 1 :one 2 :two 3 :three :default)` — sentence with 5 commas reads as AI-output cadence: 'The runtime checks the\ncondition, walks the right arm, and the unrun arm is just'
    - [LOW_GROUNDING] form=`(case 2 1 :one 2 :two 3 :three :default)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(case 2 1 :one 2 :two 3 :three :default)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '8', ':far'), resolution doesn't close the loop)

### G5-07: and / or as control flow

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 1, 'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(and 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(and 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '4'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(and 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(and 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(or nil false :found)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':soft',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(or nil false :found)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':gamma',), resolution doesn't close the loop)

### G5-08: not

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not (> 1 2))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not (> 1 2))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not (> 1 2))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)

### G5-10: map

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'COLLECTION_LEAK': 1, 'STORY_RESOLUTION_NO_DRAWN': 1, 'CLAUSE_STACK_OVERFLOW': 3, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'AS_ONE_WHO_CADENCE': 1}
    - [HIGH_LENGTH] form=`(map inc [1 2 3])` — user_msg 218 words
    - [COLLECTION_LEAK] form=`(map inc [1 2 3])` — elements of expected [2, 3, 4] appear comma-separated in user_msg (collection answer leak)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map inc [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '7', '14'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(map inc [1 2 3])` — sentence with 8 commas reads as AI-output cadence: 'To pour the vector containing 1, 2, 3 through a sieve whose rule is inc, collect'
    - [CAP_PRONOUN_MID_SENTENCE] form=`(map inc [1 2 3])` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(map inc [1 2 3])` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G5-11: filter

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3}
    - [LOW_GROUNDING] form=`(filter even? [1 2 3 4])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(filter even? [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '8', '5'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(filter even? [1 2 3 4])` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(filter even? [1 2 3 4])` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(filter even? [1 2 3 4])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(filter even? [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '15', '20'), resolution doesn't close the loop)

### G5-12: reduce

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 6, 'ANSWER_LEAK': 2, 'STORY_RESOLUTION_NO_DRAWN': 5, 'CLAUSE_STACK_OVERFLOW': 9, 'LOW_GROUNDING': 1, 'AS_ONE_WHO_CADENCE': 1}
    - [HIGH_LENGTH] form=`(reduce + [1 2 3 4])` — user_msg 255 words
    - [ANSWER_LEAK] form=`(reduce + [1 2 3 4])` — answer 10 in narrative
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce + [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '18', '12'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + [1 2 3 4])` — sentence with 6 commas reads as AI-output cadence: 'To walk the row of pebbles 1, 2, 3, 4 carrying a tally that combines each with +'
    - [HIGH_LENGTH] form=`(reduce + [1 2 3 4])` — user_msg 248 words
    - [ANSWER_LEAK] form=`(reduce + [1 2 3 4])` — answer 10 in narrative

### G5-13: reduce with init

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'ANSWER_LEAK': 1, 'STORY_RESOLUTION_NO_DRAWN': 5, 'CLAUSE_STACK_OVERFLOW': 3, 'LOW_GROUNDING': 1}
    - [HIGH_LENGTH] form=`(reduce + 100 [1 2 3])` — user_msg 231 words
    - [ANSWER_LEAK] form=`(reduce + 100 [1 2 3])` — answer 106 in narrative
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce + 100 [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('492', '15', '9'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + 100 [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To fold + over the vector containing 1, 2, 3 starting from an initial accumulato'
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + 100 [1 2 3])` — sentence with 9 commas reads as AI-output cadence: 'The runtime does this for any collection — vector, list, map,\nstring." To fold +'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce + 100 [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('464', '11', '18'), resolution doesn't close the loop)

### G5-14: apply

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 3, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 4, 'AS_ONE_WHO_CADENCE': 2, 'LOW_GROUNDING': 1}
    - [HIGH_LENGTH] form=`(apply + [1 2 3 4])` — user_msg 234 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(apply + [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '3', '16'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(apply + [1 2 3 4])` — sentence with 6 commas reads as AI-output cadence: 'To apply + to the elements of the vector containing 1, 2, 3, and 4, he, in the p'
    - [AS_ONE_WHO_CADENCE] form=`(apply + [1 2 3 4])` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [STORY_RESOLUTION_NO_DRAWN] form=`(apply + [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '4', '17'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(apply + [1 2 3 4])` — sentence with 6 commas reads as AI-output cadence: 'To apply + to the elements of the vector containing 1, 2, 3, and 4, he composed\n'

### G5-15: comp

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'HIGH_LENGTH': 1, 'ANSWER_LEAK': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'CONCEPT_AS_VERB': 1}
    - [WRONG_FABLE_LITERAL] form=`((comp inc inc) 5)` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [HIGH_LENGTH] form=`((comp inc inc) 5)` — user_msg 228 words
    - [ANSWER_LEAK] form=`((comp inc inc) 5)` — answer 7 in narrative
    - [CAP_PRONOUN_MID_SENTENCE] form=`((comp str inc) 9)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`((comp str inc) 9)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CONCEPT_AS_VERB] form=`((comp str inc) 9)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G5-16: partial

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'CONCEPT_AS_VERB': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`((partial + 10) 5)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`((partial + 10) 5)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CONCEPT_AS_VERB] form=`((partial + 10) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G5-17: juxt

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`((juxt inc dec) 5)` — user_msg 212 words

### G5-18: some

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 4, 'POST_COMMA_CAPITAL_PRONOUN': 4, 'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 4, 'HIGH_LENGTH': 2, 'PREDICATE_QUESTION_COLLISION': 2, 'CLAUSE_STACK_OVERFLOW': 2}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(some even? [1 3 5 8 7])` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(some even? [1 3 5 8 7])` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(some even? [1 3 5 8 7])` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(some even? [1 3 5 8 7])` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(some even? [1 3 5 8 7])` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(some even? [1 3 5 8 7])` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G5-19: every?

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'PREDICATE_QUESTION_COLLISION': 1, 'BOOL_LEAK_RESOLUTION': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'CAP_PRONOUN_MID_SENTENCE': 4, 'POST_COMMA_CAPITAL_PRONOUN': 4, 'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 4}
    - [HIGH_LENGTH] form=`(every? pos? [1 2 3])` — user_msg 221 words
    - [PREDICATE_QUESTION_COLLISION] form=`(every? pos? [1 2 3])` — predicate-suffix ``?`` collides with the question framing's trailing ``?`` or ``.``
    - [BOOL_LEAK_RESOLUTION] form=`(every? pos? [1 2 3])` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [CLAUSE_STACK_OVERFLOW] form=`(every? pos? [1 2 3])` — sentence with 7 commas reads as AI-output cadence: 'To check if all elements in the vector containing 1, 2, and 3 are positive, she,'
    - [CAP_PRONOUN_MID_SENTENCE] form=`(every? pos? [1 2 3])` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(every? pos? [1 2 3])` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G5-20: take and drop

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(take 3 [10 20 30 40 50])` — sentence with 8 commas reads as AI-output cadence: 'Zoomer the dog shook\nhis head and went on with the work: to take the first 3 ele'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(take 3 [10 20 30 40 50])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '18', '16'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(take 3 [10 20 30 40 50])` — sentence with 8 commas reads as AI-output cadence: 'Slate the dog shook\nhis head and went on with the work: to take the first 3 elem'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(take 3 [10 20 30 40 50])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '12', '12'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(drop 2 [10 20 30 40 50])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '7', '12'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(drop 2 [10 20 30 40 50])` — sentence with 8 commas reads as AI-output cadence: 'Boomer the dog shook\nhis head and went on with the work: to drop the first 2 ele'

### G5-21: distinct and sort

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(distinct [1 1 2 3 3 4])` — sentence with 5 commas reads as AI-output cadence: 'Write a Clojure expression that computes the sequence produced by passing 1, 1, '
    - [CLAUSE_STACK_OVERFLOW] form=`(distinct [1 1 2 3 3 4])` — sentence with 9 commas reads as AI-output cadence: 'Marley the dog shook\nhis head and went on with the work: to remove duplicate ele'
    - [CAP_PRONOUN_MID_SENTENCE] form=`(distinct [1 1 2 3 3 4])` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(distinct [1 1 2 3 3 4])` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(distinct [1 1 2 3 3 4])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(distinct [1 1 2 3 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '17', '13'), resolution doesn't close the loop)

### G5-22: recur — first taste

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 3}
    - [HIGH_LENGTH] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — user_msg 255 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — sentence with 5 commas reads as AI-output cadence: 'To walk a small circuit five times, multiplying a running tally by the current s'
    - [HIGH_LENGTH] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — user_msg 252 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — sentence with 5 commas reads as AI-output cadence: 'To walk a small circuit five times, multiplying a running tally by the current s'

## Grade 6

### G6-01: Namespace as file

- examples: 3
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'LOW_GROUNDING': 5, 'HIGH_LENGTH': 2, 'ANSWER_LEAK_STRING': 1, 'WRONG_FABLE_LITERAL': 1, 'BOOL_LEAK_RESOLUTION': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(name 'foo.bar)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(name 'foo.bar)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(name 'foo.bar)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name 'foo.bar)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(name 'foo.bar)` — user_msg 201 words
    - [ANSWER_LEAK_STRING] form=`(name 'foo.bar)` — answer string 'foo.bar' appears in user_msg

### G6-02: ns form

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'BOOL_LEAK_RESOLUTION': 1}
    - [LOW_GROUNDING] form=`(name 'race.tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name 'race.tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(name 'race.tortoise)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(name 'race.tortoise)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(name 'race.tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 'race.tortoise 'race.tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-03: require

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [HIGH_LENGTH] form=`(clojure.string/upper-case "hare")` — user_msg 202 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('cedar',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('myrrh',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('cedar',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/lower-case "ZEBRA")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('cobalt',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/lower-case "ZEBRA")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('cedar',), resolution doesn't close the loop)

### G6-04: refer and use

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(= (clojure.string/upper-case "x") (clojure.string` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= (clojure.string/upper-case "x") (clojure.string` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('ochre', 'ochre'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(= (clojure.string/upper-case "x") (clojure.string` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= (clojure.string/upper-case "x") (clojure.string` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('apple', 'apple'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= (clojure.string/upper-case "x") (clojure.string` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('harbor', 'harbor'), resolution doesn't close the loop)

### G6-05: Fully qualified names

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 12, 'CAP_PRONOUN_MID_SENTENCE': 4, 'POST_COMMA_CAPITAL_PRONOUN': 4, 'LOW_GROUNDING': 3, 'ANSWER_LEAK_STRING': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "hello")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('ember',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(clojure.string/upper-case "hello")` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(clojure.string/upper-case "hello")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "hello")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('linen',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(clojure.string/upper-case "hello")` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(clojure.string/upper-case "hello")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G6-06: Private defs

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(:private (meta 'x))` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(:private (meta 'x))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G6-07: Public vs private API

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'AS_ONE_WHO_CADENCE': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta '^:private hidden)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private', ':private'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta '^:private hidden)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private', ':private'), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(boolean (:private (meta '^:private hidden)))` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta '^:private hidden)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private', ':private'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta 'public)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta 'public)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private',), resolution doesn't close the loop)

### G6-08: Circular dependencies

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'LOW_GROUNDING': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "a")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('candle',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "a")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('pewter',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "a")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('thistle',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(= 'a.b 'a.b)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(= 'a.b 'a.b)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(= 'a.b 'a.b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-09: Loading order

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 5, 'CLAUSE_STACK_OVERFLOW': 2}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-10: Leiningen and deps.edn

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 1, 'FOREIGN_FABLE_IMAGERY': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:deps {:deps {:a 1 :b 2}})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '13', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:deps {:deps {:a 1 :b 2}})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '13', ':warm'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(:deps {:deps {:a 1 :b 2}})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:deps {:deps {:a 1 :b 2}})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '19', '4'), resolution doesn't close the loop)
    - [FOREIGN_FABLE_IMAGERY] form=`(get-in {:paths ["src"]} [:paths 0])` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose

### G6-11: Classpath

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1, 'LOW_GROUNDING': 1, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [FOREIGN_FABLE_IMAGERY] form=`(clojure.string/split "src:test" #":")` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`(clojure.string/split "src:test" #":")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "src:test" #":")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':test', 'src:test'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "src:test" #":")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':test', 'src:test'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "src:test" #":")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':test', 'src:test'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count ["src" "test" "resources"])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('src', 'test', 'resources'), resolution doesn't close the loop)

### G6-12: Multiple files in one project

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 3}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(count ['race.tortoise 'race.hare 'race.shared])` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(count ['race.tortoise 'race.hare 'race.shared])` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(count ['race.tortoise 'race.hare 'race.shared])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(map name ['race.tortoise 'race.hare])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(map name ['race.tortoise 'race.hare])` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(map name ['race.tortoise 'race.hare])` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G6-13: Aliasing conventions

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'STORY_RESOLUTION_NO_DRAWN': 3, 'AS_ONE_WHO_CADENCE': 1}
    - [HIGH_LENGTH] form=`(let [s clojure.string/upper-case] (s "hare"))` — user_msg 219 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [s clojure.string/upper-case] (s "hare"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('auburn',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(let [s clojure.string/upper-case] (s "hare"))` — user_msg 225 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [s clojure.string/upper-case] (s "hare"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('myrrh',), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(let [s clojure.string/upper-case] (s "hare"))` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [s clojure.string/upper-case] (s "hare"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('coral',), resolution doesn't close the loop)

### G6-14: Import for host classes

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'LOW_GROUNDING': 3, 'AS_ONE_WHO_CADENCE': 2}
    - [HIGH_LENGTH] form=`(symbol? 'java.util.List)` — user_msg 223 words
    - [CLAUSE_STACK_OVERFLOW] form=`(symbol? 'java.util.List)` — sentence with 5 commas reads as AI-output cadence: 'To test whether a Java class name written as a quoted symbol is a symbol, he, go'
    - [CAP_PRONOUN_MID_SENTENCE] form=`(symbol? 'java.util.List)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(symbol? 'java.util.List)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(symbol? 'java.util.List)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [AS_ONE_WHO_CADENCE] form=`(symbol? 'java.util.List)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G6-15: Namespace meta

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'HIGH_LENGTH': 1}
    - [WRONG_FABLE_LITERAL] form=`(:doc (meta '\{:doc "steady wins"\} race))` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:doc (meta '\{:doc "steady wins"\} race))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':doc', ':doc', 'steady wins'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(:doc (meta '\{:doc "steady wins"\} race))` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(:doc (meta '\{:doc "steady wins"\} race))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:doc (meta '\{:doc "steady wins"\} race))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':doc', ':doc', 'steady wins'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(:doc (meta '\{:doc "steady wins"\} race))` — user_msg 229 words

### G6-16: Cleaning up requires

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'BOOL_LEAK_RESOLUTION': 1}
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.string)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.string)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.string)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.set)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.set)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [BOOL_LEAK_RESOLUTION] form=`(contains? #{'clojure.string} 'clojure.set)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead

## Grade 7

### G7-01: throw

- examples: 1
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(try (throw (Exception. "bad")) (catch Exception e` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(try (throw (Exception. "bad")) (catch Exception e` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(try (throw (Exception. "bad")) (catch Exception e` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "bad")) (catch Exception e` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1', 'bad'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(try (throw (Exception. "bad")) (catch Exception e` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "bad")) (catch Exception e` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1', 'bad'), resolution doesn't close the loop)

### G7-02: try / catch

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 1, 'AS_ONE_WHO_CADENCE': 1, 'LOW_GROUNDING': 3}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(try (/ 1 0) (catch Exception e -1))` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(try (/ 1 0) (catch Exception e -1))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (/ 1 0) (catch Exception e -1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '-61'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(try (/ 1 0) (catch Exception e -1))` — user_msg 205 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (/ 1 0) (catch Exception e -1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '6', '-25'), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(try (/ 1 0) (catch Exception e -1))` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G7-03: try / finally

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'AS_ONE_WHO_CADENCE': 1, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 3}
    - [HIGH_LENGTH] form=`(try 7 (finally (prn :cleanup)))` — user_msg 221 words
    - [AS_ONE_WHO_CADENCE] form=`(try 7 (finally (prn :cleanup)))` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [CAP_PRONOUN_MID_SENTENCE] form=`(try 7 (finally (prn :cleanup)))` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(try 7 (finally (prn :cleanup)))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(try 7 (finally (prn :cleanup)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(try (try (/ 1 0) (finally (prn :ran))) (catch Exc` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G7-04: ex-info

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [LOW_GROUNDING] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', 'bad'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', 'bad'), resolution doesn't close the loop)

### G7-05: nil punning

- examples: 4
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'LOW_GROUNDING': 9, 'STORY_RESOLUTION_NO_DRAWN': 2, 'AS_ONE_WHO_CADENCE': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(some? nil)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(some? nil)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(some? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(some? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(some? nil)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(some? nil)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G7-06: pre and post conditions

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [LOW_GROUNDING] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exce` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exce` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G7-07: assert

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'AS_ONE_WHO_CADENCE': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 2, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(do (assert (= 1 1)) 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [AS_ONE_WHO_CADENCE] form=`(do (assert (= 1 1)) 1)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '9'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — sentence with 5 commas reads as AI-output cadence: 'To\nassert that 7 equals 9, catch the failure, and return a numeric code required'
    - [CAP_PRONOUN_MID_SENTENCE] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G7-08: prn and pprint

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(with-out-str (prn 42))` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(with-out-str (prn 42))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [HIGH_LENGTH] form=`(with-out-str (prn 42))` — user_msg 206 words
    - [CLAUSE_STACK_OVERFLOW] form=`(with-out-str (prn 42))` — sentence with 5 commas reads as AI-output cadence: 'To print the number 42 and capture the output string, he, her breath even, her s'
    - [CAP_PRONOUN_MID_SENTENCE] form=`(with-out-str (prn :hare))` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(with-out-str (prn :hare))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G7-09: tap>

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(tap> :hello)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(tap> :hello)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(tap> :hello)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(tap> :hello)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(tap> 42)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(tap> 42)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-10: doc and source

- examples: 1
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(:doc (meta '^{:doc "adds two"} plus))` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(:doc (meta '^{:doc "adds two"} plus))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(:doc (meta '^{:doc "adds two"} plus))` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(:doc (meta '^{:doc "adds two"} plus))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G7-11: Reading stack traces

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3, 'AS_ONE_WHO_CADENCE': 1, 'ANSWER_LEAK_STRING': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(try (throw (Exception. "oops")) (catch Exception ` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(try (throw (Exception. "oops")) (catch Exception ` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(try (throw (Exception. "oops")) (catch Exception ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(try (throw (Exception. "oops")) (catch Exception ` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G7-12: slurp and spit

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 2, 'ANSWER_LEAK': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(count "hare
tortoise
")` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(count "hare
tortoise
")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(count "hare
tortoise
")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "hare
tortoise
")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('amber',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(count "hare
tortoise
")` — sentence with 5 commas reads as AI-output cadence: 'Message-bones are how the two meet — a\nvalue crosses out and becomes scratches o'
    - [ANSWER_LEAK] form=`(count "hare
tortoise
")` — answer 14 in narrative

### G7-13: line-seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 4, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(first (clojure.string/split-lines "first\nsecond"` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-14: with-open

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'LOW_GROUNDING': 2, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [HIGH_LENGTH] form=`(with-out-str (println "hare"))` — user_msg 211 words
    - [LOW_GROUNDING] form=`(with-out-str (println "hare"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(with-out-str (println "hare"))` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(with-out-str (println "hare"))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(with-out-str (println "hare"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-15: *in* and *out*

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'LOW_GROUNDING': 5, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [WRONG_FABLE_LITERAL] form=`(with-out-str (print "x"))` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [LOW_GROUNDING] form=`(with-out-str (print "x"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(with-out-str (print "x"))` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(with-out-str (print "x"))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(with-out-str (print "x"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (println))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-16: edn read

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(clojure.edn/read-string "42")` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(clojure.edn/read-string "42")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "{:a 1}")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', '{:a 1}'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "{:a 1}")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', '{:a 1}'), resolution doesn't close the loop)

### G7-17: JSON roundtrip

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'LOW_GROUNDING': 4, 'HIGH_LENGTH': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — user_msg 213 words

### G7-18: Shell command

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 5, 'POST_COMMA_CAPITAL_PRONOUN': 5, 'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(:cmd {:cmd "ls" :args ["-l"]})` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(:cmd {:cmd "ls" :args ["-l"]})` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(:cmd {:cmd "ls" :args ["-l"]})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:cmd {:cmd "ls" :args ["-l"]})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '16', ':north'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(:cmd {:cmd "ls" :args ["-l"]})` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(:cmd {:cmd "ls" :args ["-l"]})` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

## Grade 8

### G8-01: Why polymorphism

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'HIGH_LENGTH': 1, 'LOW_GROUNDING': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':tortoise', ':else'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':tortoise', ':else'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — user_msg 227 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':tortoise', ':else'), resolution doesn't close the loop)

### G8-02: deftype introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 2, 'HIGH_LENGTH': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — sentence with 5 commas reads as AI-output cadence: 'Faster,\nmore focused, less convenient." To define a type Pebble with a color fie'
    - [LOW_GROUNDING] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-03: defrecord introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'ANSWER_LEAK_STRING': 1, 'STORY_RESOLUTION_NO_DRAWN': 6, 'AS_ONE_WHO_CADENCE': 1, 'CAP_PRONOUN_MID_SENTENCE': 5, 'POST_COMMA_CAPITAL_PRONOUN': 5, 'CLAUSE_STACK_OVERFLOW': 2, 'LOW_GROUNDING': 3}
    - [HIGH_LENGTH] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — user_msg 229 words
    - [ANSWER_LEAK_STRING] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — answer string ':slow' appears in user_msg
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':pace', ':slow', 'Alice'), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G8-04: Protocol definition

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 4, 'POST_COMMA_CAPITAL_PRONOUN': 4, 'LOW_GROUNDING': 6}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol Greet (hail [this])) (some? Greet` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G8-05: Protocol extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 5}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('swift', 'hare'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 6 commas reads as AI-output cadence: 'The runtime looks up which breed the\ndog is, then runs that breed\'s answer." To '
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G8-06: Protocol method dispatch

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 4, 'POST_COMMA_CAPITAL_PRONOUN': 4, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 6, 'LOW_GROUNDING': 3}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'Any dog\nthat learns the signals may join the pack." To define a protocol Pace wi'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, extend it to both String and Long t'

### G8-07: Record implementing protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 4, 'AS_ONE_WHO_CADENCE': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':swift', 'Pip'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':swift', 'Pip'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, define a record Hare that implement'

### G8-08: Multimethod defmulti

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 4, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmulti pace :species) (defmethod pace :hare` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':species', ':hare', ':swift'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(do (defmulti pace :species) (defmethod pace :hare` — user_msg 225 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmulti pace :species) (defmethod pace :hare` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':species', ':hare', ':swift'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 5 commas reads as AI-output cadence: "To declare a sorting-table named pace that reads each runner's :species stamp; a"
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmulti pace :species) (defmethod pace :hare` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':species', ':hare', ':swift'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 5 commas reads as AI-output cadence: 'The runtime reads it, finds the matching pile,\nand runs that one." To declare a '

### G8-09: Multimethod defmethod

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 5, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 6 commas reads as AI-output cadence: 'The runtime reads it, finds the matching pile,\nand runs that one." To define a m'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 5 commas reads as AI-output cadence: 'To define a multimethod pace that dispatches on :species with methods for both :'
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defmulti pace :species) (defmethod pace :hare` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defmulti pace :species) (defmethod pace :hare` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 6 commas reads as AI-output cadence: 'The runtime reads it, finds the matching pile,\nand runs that one." To define a m'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 6 commas reads as AI-output cadence: 'The runtime reads it, finds the matching pile,\nand runs that one." To define a m'

### G8-10: Multimethod vs protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 3, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'LOW_GROUNDING': 3}
    - [HIGH_LENGTH] form=`(do (defmulti show identity) (defmethod show :rabb` — user_msg 212 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti show identity) (defmethod show :rabb` — sentence with 5 commas reads as AI-output cadence: 'To define a multimethod show that dispatches on identity with a method for one s'
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defmulti show identity) (defmethod show :rabb` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defmulti show identity) (defmethod show :rabb` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defmulti show identity) (defmethod show :rabb` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defmulti show identity) (defmethod show :rabb` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G8-11: Protocol vs Java interface

- examples: 1
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'LOW_GROUNDING': 1, 'CLAUSE_STACK_OVERFLOW': 3, 'HIGH_LENGTH': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol IPace (run [this])) (extend-proto` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defprotocol IPace (run [this])) (extend-proto` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (defprotocol IPace (run [this])) (extend-proto` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol IPace (run [this])) (extend-proto` — sentence with 6 commas reads as AI-output cadence: 'The runtime looks up which breed the\ndog is, then runs that breed\'s answer." To '
    - [HIGH_LENGTH] form=`(do (defprotocol IPace (run [this])) (extend-proto` — user_msg 220 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol IPace (run [this])) (extend-proto` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol IPace with method run, extend it to String type, then call '

### G8-12: extend-type on built-in types

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 5, 'LOW_GROUNDING': 3, 'HIGH_LENGTH': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-type` — sentence with 6 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, use extend-type to attach it to Lon'
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-type` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-type` — sentence with 7 commas reads as AI-output cadence: 'The runtime reads it, finds the matching pile,\nand runs that one." To define a p'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-type` — sentence with 6 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, use extend-type to attach it to Lon'
    - [HIGH_LENGTH] form=`(do (defprotocol Pace (speed [this])) (extend-type` — user_msg 211 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-type` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, use extend-type to attach it to Str'

### G8-13: this-style vs fn-style

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 6, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'LOW_GROUNDING': 4}
    - [HIGH_LENGTH] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg 216 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Named (name-of [this])) (defrecor` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':n', 'Zephyr'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Named (name-of [this])) (defrecor` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Named with method name-of, define a record that uses this t'
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol Named (name-of [this])) (defrecor` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defprotocol Named (name-of [this])) (defrecor` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-14: Protocols don't inherit

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 3, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'LOW_GROUNDING': 1, 'AS_ONE_WHO_CADENCE': 1}
    - [HIGH_LENGTH] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg 246 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — sentence with 6 commas reads as AI-output cadence: 'To define two protocols A and B, each with a method, extend both to String type '
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-15: derive and isa? — multimethod hierarchy

- examples: 3
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'CLAUSE_STACK_OVERFLOW': 3, 'HIGH_LENGTH': 1, 'BOOL_LEAK_RESOLUTION': 2, 'LOW_GROUNDING': 4, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [WRONG_FABLE_LITERAL] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [CLAUSE_STACK_OVERFLOW] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — sentence with 6 commas reads as AI-output cadence: 'The runtime reads it, finds the matching pile,\nand runs that one." To establish '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — sentence with 5 commas reads as AI-output cadence: 'To establish a type relationship where ::hare is a type of ::runner, then check '
    - [HIGH_LENGTH] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — user_msg 212 words
    - [BOOL_LEAK_RESOLUTION] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(isa? java.lang.Long java.lang.Number)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-16: Abstract design with protocols

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 5, 'POST_COMMA_CAPITAL_PRONOUN': 5, 'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 3}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':leap', ':plod'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — sentence with 5 commas reads as AI-output cadence: 'Any dog\nthat learns the signals may join the pack." To define a protocol Move wi'
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

## Grade 9

### G9-01: Immutability as default — review

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :b 2) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '6', ':kumquat'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(let [m {:a 1}] (assoc m :b 2) m)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(let [m {:a 1}] (assoc m :b 2) m)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :b 2) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '12', '4'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(let [v [1 2 3]] (conj v 4) v)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(let [v [1 2 3]] (conj v 4) v)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G9-02: Why state at all

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'CLAUSE_STACK_OVERFLOW': 6, 'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1}
    - [LOW_GROUNDING] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — sentence with 8 commas reads as AI-output cadence: 'If two dogs arrive at once, the runtime makes sure only one of us\ngoes through a'
    - [LOW_GROUNDING] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — sentence with 8 commas reads as AI-output cadence: 'to\nwrite atomically, no matter who else is sniffing." To\nconstruct an atom holdi'
    - [LOW_GROUNDING] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — sentence with 7 commas reads as AI-output cadence: 'The\ncount changes only when one of us scratches a new one — and only\nas the runt'

### G9-03: Atom introduction

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 9, 'AS_ONE_WHO_CADENCE': 1, 'LOW_GROUNDING': 4}
    - [HIGH_LENGTH] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg 240 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 7 commas reads as AI-output cadence: 'To set up a shared notebook starting at 0, atomically add one to its page, then '
    - [AS_ONE_WHO_CADENCE] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 7 commas reads as AI-output cadence: 'To set up a shared notebook starting at 0, atomically add one to its page, then '
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 7 commas reads as AI-output cadence: 'The\ncount changes only when one of us scratches a new one — and only\nas the runt'

### G9-04: Atom CAS semantics

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CLAUSE_STACK_OVERFLOW': 6}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — sentence with 7 commas reads as AI-output cadence: 'The\nruntime sees to that — no two writers stomp on each other\'s\nwork." To constr'
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — sentence with 7 commas reads as AI-output cadence: 'The\ncount changes only when one of us scratches a new one — and only\nas the runt'
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — sentence with 7 commas reads as AI-output cadence: 'The\ncount changes only when one of us scratches a new one — and only\nas the runt'

### G9-05: Watch on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 3}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':w',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — sentence with 8 commas reads as AI-output cadence: 'If two dogs arrive at once, the runtime makes sure only one of us\ngoes through a'
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':w',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — sentence with 7 commas reads as AI-output cadence: 'The\nruntime sees to that — no two writers stomp on each other\'s\nwork." To constr'

### G9-06: Validator on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'CLAUSE_STACK_OVERFLOW': 3}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — sentence with 5 commas reads as AI-output cadence: 'validator on it, atomically swap by applying inc, and dereference, he composed a'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — sentence with 5 commas reads as AI-output cadence: 'validator on it, atomically swap by applying inc, and dereference, he composed\na'
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — sentence with 5 commas reads as AI-output cadence: 'validator on it, atomically swap by applying inc, and dereference, he\ncomposed a'

### G9-07: Ref introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'CLAUSE_STACK_OVERFLOW': 6, 'AS_ONE_WHO_CADENCE': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 8 commas reads as AI-output cadence: 'The\nruntime sees to that — no two writers stomp on each other\'s\nwork." To constr'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 8 commas reads as AI-output cadence: 'To construct a ref holding 0, perform a transactional alter by applying inc insi'
    - [AS_ONE_WHO_CADENCE] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 8 commas reads as AI-output cadence: 'To construct a ref holding 0, perform a transactional alter by applying inc insi'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('100', '7'), resolution doesn't close the loop)

### G9-08: dosync and alter

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 6, 'LOW_GROUNDING': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — sentence with 6 commas reads as AI-output cadence: 'To construct refs a and b, perform a coordinated transaction that alters both by'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — sentence with 8 commas reads as AI-output cadence: 'To construct refs a and b, perform a coordinated transaction that alters both by'
    - [LOW_GROUNDING] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — sentence with 6 commas reads as AI-output cadence: 'The\ncount changes only when one of us scratches a new one — and only\nas the runt'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '5'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — sentence with 8 commas reads as AI-output cadence: 'To construct a ref holding 10, perform a transactional alter by applying + with '

### G9-09: Ref vs atom

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'CLAUSE_STACK_OVERFLOW': 6}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 7 commas reads as AI-output cadence: 'The\ncount changes only when one of us scratches a new one — and only\nas the runt'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 7 commas reads as AI-output cadence: 'To construct an atom holding 0, atomically swap it by applying inc, and derefere'
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 7 commas reads as AI-output cadence: 'The\nruntime sees to that — no two writers stomp on each other\'s\nwork." To constr'
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-10: Agent introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 6, 'LOW_GROUNDING': 2, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [HIGH_LENGTH] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg 216 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 10 commas reads as AI-output cadence: 'To construct an agent holding 0, asynchronously send inc to it, await its comple'
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 10 commas reads as AI-output cadence: 'The result will be there when you\nask for it — sometimes you have to wait for th'
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 10 commas reads as AI-output cadence: 'The result will be there when you\nask for it — sometimes you have to wait for th'

### G9-11: send and send-off

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CLAUSE_STACK_OVERFLOW': 5, 'HIGH_LENGTH': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 10 commas reads as AI-output cadence: 'The result will be there when you\nask for it — sometimes you have to wait for th'
    - [HIGH_LENGTH] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg 222 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 9 commas reads as AI-output cadence: 'To construct an agent holding 0, use send to asynchronously apply inc, await its'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 9 commas reads as AI-output cadence: 'To construct an agent holding 0, use send to asynchronously apply inc, await its'
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def ag (agent 0)) (send-off ag inc) (await ag` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G9-12: await — synchronizing on agents

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'LOW_GROUNDING': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 9 commas reads as AI-output cadence: 'To construct an agent holding 0, asynchronously send inc twice, synchronize with'
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 9 commas reads as AI-output cadence: 'The runtime makes that easier than it sounds." To construct an agent holding 0, '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 9 commas reads as AI-output cadence: 'To construct an agent holding 0, asynchronously send inc twice, synchronize with'

### G9-13: future introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 4, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [HIGH_LENGTH] form=`@(future (+ 1 2))` — user_msg 238 words
    - [CLAUSE_STACK_OVERFLOW] form=`@(future (+ 1 2))` — sentence with 6 commas reads as AI-output cadence: 'To dispatch a runner to compute the sum of 1 and 2; later, ask the runner for th'
    - [CAP_PRONOUN_MID_SENTENCE] form=`@(future (+ 1 2))` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`@(future (+ 1 2))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`@(future (+ 1 2))` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G9-14: deref @ shorthand

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'AS_ONE_WHO_CADENCE': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(do (def a (atom 7)) @a)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) (deref a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) (deref a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)

### G9-15: promise — deliver and deref

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 3, 'WRONG_FABLE_LITERAL': 1, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'LOW_GROUNDING': 1, 'CLAUSE_STACK_OVERFLOW': 5, 'ANSWER_LEAK_STRING': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def p (promise)) (deliver p :done) @p)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [WRONG_FABLE_LITERAL] form=`(do (def p (promise)) (deliver p :done) @p)` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (def p (promise)) (deliver p :done) @p)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (def p (promise)) (deliver p :done) @p)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def p (promise)) (deliver p :done) @p)` — sentence with 7 commas reads as AI-output cadence: 'The runtime makes that easier than it sounds." To construct a promise, deliver a'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def p (promise)) (deliver p :done) @p)` — sentence with 7 commas reads as AI-output cadence: 'To construct a promise, deliver a completion keyword to it, and dereference to g'

### G9-16: volatile — when STM is too heavy

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CLAUSE_STACK_OVERFLOW': 6, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — sentence with 8 commas reads as AI-output cadence: 'to\nwrite atomically, no matter who else is sniffing." To\nconstruct a volatile ho'
    - [LOW_GROUNDING] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — sentence with 8 commas reads as AI-output cadence: 'If two dogs arrive at once, the runtime makes sure only one of us\ngoes through a'
    - [LOW_GROUNDING] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — sentence with 7 commas reads as AI-output cadence: 'The\nruntime sees to that — no two writers stomp on each other\'s\nwork." To constr'

### G9-17: binding — thread-local

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — sentence with 7 commas reads as AI-output cadence: 'The\nruntime sees to that — no two writers stomp on each other\'s\nwork." To define'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — sentence with 7 commas reads as AI-output cadence: 'To define a dynamic var *p* as 1, use binding to rebind it to 99, and read its v'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — sentence with 7 commas reads as AI-output cadence: 'To define a dynamic var *p* as 1, use binding to rebind it to 99, and read its v'

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'CLAUSE_STACK_OVERFLOW': 6, 'HIGH_LENGTH': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — sentence with 7 commas reads as AI-output cadence: 'The\ncount changes only when one of us scratches a new one — and only\nas the runt'
    - [HIGH_LENGTH] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg 257 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — sentence with 8 commas reads as AI-output cadence: 'To create an object to use as a monitor, acquire the lock, and evaluate an addit'
    - [HIGH_LENGTH] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg 259 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — sentence with 8 commas reads as AI-output cadence: 'To create an object to use as a monitor, acquire the lock, and evaluate an addit'

## Grade 10

### G10-01: quote, unquote, unquote-splice

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'CAP_PRONOUN_MID_SENTENCE': 4, 'POST_COMMA_CAPITAL_PRONOUN': 4, 'HIGH_LENGTH': 3, 'THE_FORM_OVERUSE': 3, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(quote (+ 1 2))` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(quote (+ 1 2))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(quote (+ 1 2))` — user_msg 227 words
    - [THE_FORM_OVERUSE] form=`(quote (+ 1 2))` — `the form` appears 5 times in user_msg (template tic — vary references)

### G10-02: syntax-quote

- examples: 2
- variety @ n=50: 1.00
- issues: {'THE_FORM_OVERUSE': 3, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'LOW_GROUNDING': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1}
    - [THE_FORM_OVERUSE] form=`(let [x 10] `(+ ~x ~x))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(let [x 10] `(+ ~x ~x))` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(let [x 10] `(+ ~x ~x))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(let [x 10] `(+ ~x ~x))` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(let [x 10] `(+ ~x ~x))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [THE_FORM_OVERUSE] form=`(let [x 10] `(+ ~x ~x))` — `the form` appears 5 times in user_msg (template tic — vary references)

### G10-03: defmacro introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'AS_ONE_WHO_CADENCE': 1, 'LOW_GROUNDING': 2, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg 266 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G10-04: Macro expansion rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(when true 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(macroexpand-1 '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(when true 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(macroexpand-1 '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(when true 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(macroexpand-1 '(or a b))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-05: macroexpand

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'LOW_GROUNDING': 4, 'CLAUSE_STACK_OVERFLOW': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(macroexpand '(when true 1))` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(macroexpand '(when true 1))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(macroexpand '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(macroexpand '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(macroexpand '(-> 1 inc inc))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(macroexpand '(-> 1 inc inc))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-06: when and when-not as macros

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 7, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 1, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'WRONG_FABLE_LITERAL': 1}
    - [LOW_GROUNDING] form=`(when true 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(when true 1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'You set the rule\nonce, and any mark that uses it gets rewritten on the way to th'
    - [CAP_PRONOUN_MID_SENTENCE] form=`(when true 1 2 3)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(when true 1 2 3)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(when true 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'ANSWER_LEAK': 2, 'HIGH_LENGTH': 3, 'STORY_RESOLUTION_NO_DRAWN': 4, 'AS_ONE_WHO_CADENCE': 2, 'CLAUSE_STACK_OVERFLOW': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'CONCEPT_AS_VERB': 1}
    - [LOW_GROUNDING] form=`(-> 5 inc inc inc)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [ANSWER_LEAK] form=`(-> 5 inc inc inc)` — answer 8 in narrative
    - [HIGH_LENGTH] form=`(-> 5 inc inc inc)` — user_msg 240 words
    - [ANSWER_LEAK] form=`(-> 5 inc inc inc)` — answer 8 in narrative
    - [STORY_RESOLUTION_NO_DRAWN] form=`(-> 5 inc inc inc)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(-> 5 inc inc inc)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G10-08: Macro vs fn

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'ANSWER_LEAK': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [ANSWER_LEAK] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — answer 7 in narrative
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)

### G10-09: Hygiene and gensym

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(symbol? (gensym))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('x_', 'x_'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('x_', 'x_'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-10: Anaphoric macros are confusing

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3}
    - [HIGH_LENGTH] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — user_msg 235 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G10-11: Reader macros overview

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 7, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CAP_PRONOUN_MID_SENTENCE': 5, 'POST_COMMA_CAPITAL_PRONOUN': 5, 'HIGH_LENGTH': 2, 'ANSWER_LEAK': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'AS_ONE_WHO_CADENCE': 1}
    - [LOW_GROUNDING] form=`'(1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '8', '5'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`'(1 2 3)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`'(1 2 3)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`'(1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '15', '20'), resolution doesn't close the loop)

### G10-12: Tagged literals

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 5, 'POST_COMMA_CAPITAL_PRONOUN': 5, 'LOW_GROUNDING': 5, 'CLAUSE_STACK_OVERFLOW': 2, 'HIGH_LENGTH': 1, 'BOOL_LEAK_RESOLUTION': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'AS_ONE_WHO_CADENCE': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(inst? #inst "2024-01-01")` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(inst? #inst "2024-01-01")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(inst? #inst "2024-01-01")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(inst? #inst "2024-01-01")` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'
    - [CAP_PRONOUN_MID_SENTENCE] form=`(inst? #inst "2024-01-01")` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(inst? #inst "2024-01-01")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G10-13: Data readers and EDN extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 3, 'AS_ONE_WHO_CADENCE': 1}
    - [HIGH_LENGTH] form=`(clojure.edn/read-string "42")` — user_msg 207 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(clojure.edn/read-string "42")` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(clojure.edn/read-string "42")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(clojure.edn/read-string "42")` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(clojure.edn/read-string "42")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G10-14: eval (the function)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'ANSWER_LEAK': 1, 'LOW_GROUNDING': 3, 'CLAUSE_STACK_OVERFLOW': 2, 'AS_ONE_WHO_CADENCE': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [HIGH_LENGTH] form=`(eval '(+ 1 2 3))` — user_msg 233 words
    - [ANSWER_LEAK] form=`(eval '(+ 1 2 3))` — answer 6 in narrative
    - [LOW_GROUNDING] form=`(eval '(+ 1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(eval '(+ 1 2 3))` — sentence with 5 commas reads as AI-output cadence: 'You set the rule\nonce, and any mark that uses it gets rewritten on the way to th'
    - [AS_ONE_WHO_CADENCE] form=`(eval '(+ 1 2 3))` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [CAP_PRONOUN_MID_SENTENCE] form=`(eval (list '+ 4 5))` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G10-15: When not to write a macro

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'AS_ONE_WHO_CADENCE': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'LOW_GROUNDING': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [WRONG_FABLE_LITERAL] form=`(do "a function suffices when no syntax shaping is` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [AS_ONE_WHO_CADENCE] form=`(do "a function suffices when no syntax shaping is` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do "a function suffices when no syntax shaping is` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do "a function suffices when no syntax shaping is` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do "prefer fn unless you must shape syntax" (map ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "prefer fn unless you must shape syntax" (map ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '7', '8'), resolution doesn't close the loop)

### G10-16: Macro pattern library

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'CLAUSE_STACK_OVERFLOW': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1}
    - [LOW_GROUNDING] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — sentence with 5 commas reads as AI-output cadence: 'You set the rule\nonce, and any mark that uses it gets rewritten on the way to th'
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':slow',), resolution doesn't close the loop)

## Grade 11

### G11-01: JVM vs CLR vs JS vs Python (host overview)

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'FOREIGN_FABLE_IMAGERY': 3, 'AS_ONE_WHO_CADENCE': 1}
    - [LOW_GROUNDING] form=`(do "Clojure runs on multiple hosts: JVM, CLR, JS,` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(do "Clojure runs on multiple hosts: JVM, CLR, JS,` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose
    - [AS_ONE_WHO_CADENCE] form=`(do "Clojure runs on multiple hosts: JVM, CLR, JS,` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [FOREIGN_FABLE_IMAGERY] form=`(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScr` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScr` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScr` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose

### G11-02: Method call syntax

- examples: 3
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 6, 'POST_COMMA_CAPITAL_PRONOUN': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 1, 'BOOL_LEAK_RESOLUTION': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(.toUpperCase "abc")` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(.toUpperCase "abc")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(.toUpperCase "abc")` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(.toUpperCase "abc")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(.toUpperCase "abc")` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(.toUpperCase "abc")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G11-03: Static method call

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'AS_ONE_WHO_CADENCE': 1, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(Math/abs -7)` — user_msg 249 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(Math/abs -7)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(Math/abs -7)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(Math/abs -7)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G11-04: Field access

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 3, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'HIGH_LENGTH': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('ochre',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(count "tortoise")` — sentence with 5 commas reads as AI-output cadence: 'The runtime moves a value across the\nboundary, calls the human-side tool, and br'
    - [CAP_PRONOUN_MID_SENTENCE] form=`(count "tortoise")` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(count "tortoise")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('apple',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('harbor',), resolution doesn't close the loop)

### G11-05: Import form

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 3, 'LOW_GROUNDING': 2, 'AS_ONE_WHO_CADENCE': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "(:import (java.util Date)) imports a host cla` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`(do "(:import (java.util Date)) imports a host cla` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(do "(:import (java.util Date)) imports a host cla` — tortoise-hare-specific imagery 'leather notebook' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`(do "(:import (java.util Date)) imports a host cla` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [AS_ONE_WHO_CADENCE] form=`(do "import is a top-of-file ns clause" :studied)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [FOREIGN_FABLE_IMAGERY] form=`(do "import is a top-of-file ns clause" :studied)` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose

### G11-06: new and dot-construct

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 5, 'POST_COMMA_CAPITAL_PRONOUN': 5, 'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(String. "go")` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(String. "go")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(String. "go")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(String. "go")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('go',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(String. "go")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('go',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(String. "go")` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G11-07: Arrays

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'AS_ONE_WHO_CADENCE': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a (int-array [10 20 30])] (aget a 1))` — sentence with 5 commas reads as AI-output cadence: 'The runtime moves a value across the\nboundary, calls the human-side tool, and br'
    - [AS_ONE_WHO_CADENCE] form=`(let [a (int-array [10 20 30])] (aget a 1))` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a (int-array [1 2 3])] (alength a))` — sentence with 5 commas reads as AI-output cadence: 'The runtime moves a value across the\nboundary, calls the human-side tool, and br'
    - [CAP_PRONOUN_MID_SENTENCE] form=`(let [a (int-array [1 2 3])] (alength a))` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(let [a (int-array [1 2 3])] (alength a))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G11-08: Type hints

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1, 'AS_ONE_WHO_CADENCE': 2, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [^String s "abc"] (.toUpperCase s))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(let [^String s "abc"] (.toUpperCase s))` — user_msg 202 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [^String s "abc"] (.toUpperCase s))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(let [^String s "abc"] (.toUpperCase s))` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [CAP_PRONOUN_MID_SENTENCE] form=`(let [^String s "abc"] (.toUpperCase s))` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(let [^String s "abc"] (.toUpperCase s))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G11-09: Checked vs unchecked math

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'LOW_GROUNDING': 3, 'REPL_AS_TIME_TRAVELLER': 2, 'STORY_RESOLUTION_NO_DRAWN': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(+ 1 2)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(+ 1 2)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(+ 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(+ 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [REPL_AS_TIME_TRAVELLER] form=`(+ 1 2)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '7'), resolution doesn't close the loop)

### G11-10: ClojureScript overview

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 3, 'LOW_GROUNDING': 3}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "ClojureScript compiles to JavaScript via the ` — tortoise-hare-specific imagery 'leather notebook' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`(do "ClojureScript compiles to JavaScript via the ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(do "ClojureScript compiles to JavaScript via the ` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`(do "cljs runs in browsers and Node, with JS inter` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(do "cljs runs in browsers and Node, with JS inter` — tortoise-hare-specific imagery 'leather notebook' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`(do "cljs runs in browsers and Node, with JS inter` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-11: cljs / JavaScript interop

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2, 'LOW_GROUNDING': 2, 'AS_ONE_WHO_CADENCE': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "(js/console.log x) calls a JS global; (.-foo ` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`(do "(js/console.log x) calls a JS global; (.-foo ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [AS_ONE_WHO_CADENCE] form=`(do "(js/console.log x) calls a JS global; (.-foo ` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [LOW_GROUNDING] form=`(do "(js/console.log x) calls a JS global; (.-foo ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(do "js/<name> namespaces JS globals; .- prefix ma` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into dog-shadow prose

### G11-12: Basilisp overview (Python host)

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'FOREIGN_FABLE_IMAGERY': 2}
    - [LOW_GROUNDING] form=`(do "basilisp is a Clojure-like Lisp implemented o` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(do "basilisp is a Clojure-like Lisp implemented o` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`(do "basilisp is a Clojure-like Lisp implemented o` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(do "basilisp interops with Python via the same do` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`(do "basilisp interops with Python via the same do` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-13: Cross-platform .cljc and reader-conditionals

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'FOREIGN_FABLE_IMAGERY': 2, 'LOW_GROUNDING': 2, 'AS_ONE_WHO_CADENCE': 1}
    - [WRONG_FABLE_LITERAL] form=`(do "#?(:clj … :cljs …) selects a form per host at` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [FOREIGN_FABLE_IMAGERY] form=`(do "#?(:clj … :cljs …) selects a form per host at` — tortoise-hare-specific imagery 'leather notebook' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`(do "#?(:clj … :cljs …) selects a form per host at` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [AS_ONE_WHO_CADENCE] form=`(do ".cljc files share code across multiple hosts"` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [FOREIGN_FABLE_IMAGERY] form=`(do ".cljc files share code across multiple hosts"` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`(do ".cljc files share code across multiple hosts"` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-14: Debugging host leaks

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'CAP_PRONOUN_MID_SENTENCE': 4, 'POST_COMMA_CAPITAL_PRONOUN': 4, 'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "host stack traces leak through interop; learn` — sentence with 5 commas reads as AI-output cadence: 'To learn to read and debug host runtime errors, he, going slowly, looking twice '
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do "host stack traces leak through interop; learn` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do "host stack traces leak through interop; learn` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do "host stack traces leak through interop; learn` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do "host stack traces leak through interop; learn` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do "host stack traces leak through interop; learn` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

## Grade 12

### G12-01: Transducers introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'HIGH_LENGTH': 1, 'COLLECTION_LEAK': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'WRONG_FABLE_LITERAL': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(into [] (map inc) [1 2 3])` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(into [] (map inc) [1 2 3])` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(into [] (map inc) [1 2 3])` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(into [] (map inc) [1 2 3])` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [HIGH_LENGTH] form=`(into [] (map inc) [1 2 3])` — user_msg 257 words
    - [COLLECTION_LEAK] form=`(into [] (map inc) [1 2 3])` — elements of expected [2, 3, 4] appear comma-separated in user_msg (collection answer leak)

### G12-02: Transducer composition

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 3, 'HIGH_LENGTH': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G12-03: into with a transducer (xform)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'COLLECTION_LEAK': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'AS_ONE_WHO_CADENCE': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [HIGH_LENGTH] form=`(into #{} (map inc) [1 2 3])` — user_msg 265 words
    - [COLLECTION_LEAK] form=`(into #{} (map inc) [1 2 3])` — elements of expected {2, 3, 4} appear comma-separated in user_msg (collection answer leak)
    - [CLAUSE_STACK_OVERFLOW] form=`(into #{} (map inc) [1 2 3])` — sentence with 7 commas reads as AI-output cadence: 'To use the map-inc transducer with into to create a set from the incremented ele'
    - [AS_ONE_WHO_CADENCE] form=`(into #{} (map inc) [1 2 3])` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [CLAUSE_STACK_OVERFLOW] form=`(into #{} (map inc) [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'Leo the dog shook\nhis head and went on with the work: to use the map-inc transdu'
    - [CAP_PRONOUN_MID_SENTENCE] form=`(into #{} (map inc) [1 2 3])` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G12-04: core.async introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 3}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "(chan), (go ...), (<! ...), (>! ...) form the` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do "(chan), (go ...), (<! ...), (>! ...) form the` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do "go-blocks let you write async code as if it w` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose

### G12-05: Channels and pipelines

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 3, 'LOW_GROUNDING': 2, 'CLAUSE_STACK_OVERFLOW': 1, 'AS_ONE_WHO_CADENCE': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "pipe, mult, mix, pipeline-async route values ` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`(do "pipe, mult, mix, pipeline-async route values ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(do "pipe, mult, mix, pipeline-async route values ` — tortoise-hare-specific imagery 'leather notebook' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`(do "pipe, mult, mix, pipeline-async route values ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do "pipe, mult, mix, pipeline-async route values ` — sentence with 5 commas reads as AI-output cadence: 'Marigold the dog squinted at the goal — to study how pipe, mult, mix, and pipeli'
    - [AS_ONE_WHO_CADENCE] form=`(do "pipelines transform streams of values channel` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G12-06: clojure.spec

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 4}
    - [FOREIGN_FABLE_IMAGERY] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose

### G12-07: Spec generators

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "s/exercise produces sample inputs for a spec"` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do "spec generators turn specs into property-base` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into dog-shadow prose

### G12-08: clojure.test

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "(deftest …), (is …), (testing …) are the core` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into dog-shadow prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do "(deftest …), (is …), (testing …) are the core` — sentence with 6 commas reads as AI-output cadence: 'Marble the dog, her breath even, her step even, her thought even, had already wr'

### G12-09: Test fixtures

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'FOREIGN_FABLE_IMAGERY': 2, 'AS_ONE_WHO_CADENCE': 1}
    - [LOW_GROUNDING] form=`(do "(use-fixtures :each f) wraps every deftest in` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(do "(use-fixtures :each f) wraps every deftest in` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose
    - [AS_ONE_WHO_CADENCE] form=`(do "(use-fixtures :each f) wraps every deftest in` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [LOW_GROUNDING] form=`(do "fixtures provide setup/teardown around deftes` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(do "fixtures provide setup/teardown around deftes` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`(do "fixtures provide setup/teardown around deftes` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-10: Property-based testing

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2, 'LOW_GROUNDING': 3, 'AS_ONE_WHO_CADENCE': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(= (reverse (reverse [1 2 3])) [1 2 3])` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`(= (reverse (reverse [1 2 3])) [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [AS_ONE_WHO_CADENCE] form=`(do "test.check generates inputs and checks proper` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [LOW_GROUNDING] form=`(do "test.check generates inputs and checks proper` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(do "test.check generates inputs and checks proper` — tortoise-hare-specific imagery 'leather notebook' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`(do "test.check generates inputs and checks proper` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-11: Leiningen project.clj

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2, 'LOW_GROUNDING': 2, 'AS_ONE_WHO_CADENCE': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "project.clj declares :dependencies, :main, :p` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`(do "project.clj declares :dependencies, :main, :p` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [AS_ONE_WHO_CADENCE] form=`(do "project.clj declares :dependencies, :main, :p` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [LOW_GROUNDING] form=`(do "project.clj declares :dependencies, :main, :p` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(do "Leiningen reads project.clj at the project ro` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into dog-shadow prose

### G12-12: deps.edn projects

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'FOREIGN_FABLE_IMAGERY': 2}
    - [LOW_GROUNDING] form=`(do "deps.edn declares :deps and :aliases for the ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(do "deps.edn declares :deps and :aliases for the ` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`(do "deps.edn declares :deps and :aliases for the ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(do "deps.edn is read by the official `clj`/`cloju` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`(do "deps.edn is read by the official `clj`/`cloju` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-13: Aliases and tools

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'FOREIGN_FABLE_IMAGERY': 2, 'LOW_GROUNDING': 2, 'AS_ONE_WHO_CADENCE': 1}
    - [WRONG_FABLE_LITERAL] form=`(do "`clj -M:test` runs the :test alias from deps.` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [FOREIGN_FABLE_IMAGERY] form=`(do "`clj -M:test` runs the :test alias from deps.` — tortoise-hare-specific imagery 'leather notebook' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`(do "`clj -M:test` runs the :test alias from deps.` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [AS_ONE_WHO_CADENCE] form=`(do "aliases compose extra paths, deps, and main o` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [FOREIGN_FABLE_IMAGERY] form=`(do "aliases compose extra paths, deps, and main o` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`(do "aliases compose extra paths, deps, and main o` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-14: Pedestal / Ring (web stack brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2, 'LOW_GROUNDING': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "Ring models HTTP as request-map -> response-m` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`(do "Ring models HTTP as request-map -> response-m` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do "Pedestal layers interceptors over Ring for ri` — sentence with 5 commas reads as AI-output cadence: 'Berry the dog, her face quiet, her hands quieter still, had already written\nthe '
    - [FOREIGN_FABLE_IMAGERY] form=`(do "Pedestal layers interceptors over Ring for ri` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`(do "Pedestal layers interceptors over Ring for ri` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-15: Datomic / XTDB (datalog db brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'LOW_GROUNDING': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [WRONG_FABLE_LITERAL] form=`(do "Datomic and XTDB are immutable, time-aware da` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [LOW_GROUNDING] form=`(do "Datomic and XTDB are immutable, time-aware da` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "Datomic and XTDB are immutable, time-aware da` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do "Datomic and XTDB are immutable, time-aware da` — sentence with 5 commas reads as AI-output cadence: 'Setter the dog, who had simply walked to the slate and begun to\nwrite the family'
    - [LOW_GROUNDING] form=`(do "queries are written in datalog over EDN-shape` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-16: Reagent (cljs UI brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 6, 'LOW_GROUNDING': 3}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "Reagent wraps React with Hiccup-shaped Clojur` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do "Reagent wraps React with Hiccup-shaped Clojur` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do "Reagent wraps React with Hiccup-shaped Clojur` — tortoise-hare-specific imagery 'leather notebook' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do "components are functions returning Hiccup vec` — tortoise-hare-specific imagery 'leather notebook' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`(do "components are functions returning Hiccup vec` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(do "components are functions returning Hiccup vec` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose

### G12-17: Library design patterns

- examples: 3
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1, 'LOW_GROUNDING': 2, 'AS_ONE_WHO_CADENCE': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "good libraries expose data, then functions, t` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`(do "good libraries expose data, then functions, t` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= [1 2 3] (vec '(1 2 3)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [AS_ONE_WHO_CADENCE] form=`(= [1 2 3] (vec '(1 2 3)))` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G12-18: Clojure style guide

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2, 'LOW_GROUNDING': 4, 'AS_ONE_WHO_CADENCE': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "kebab-case names, two-space indent, threading` — tortoise-hare-specific imagery 'leather notebook' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`(do "kebab-case names, two-space indent, threading` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(do "kebab-case names, two-space indent, threading` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`(do "kebab-case names, two-space indent, threading` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "prefer pure functions, name predicates with ?` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [AS_ONE_WHO_CADENCE] form=`(do "prefer pure functions, name predicates with ?` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

---

## Summary

### Issue counts (across all examples × 3 records)

- **STORY_RESOLUTION_NO_DRAWN**: 812
- **LOW_GROUNDING**: 465
- **CLAUSE_STACK_OVERFLOW**: 294
- **CAP_PRONOUN_MID_SENTENCE**: 290
- **POST_COMMA_CAPITAL_PRONOUN**: 290
- **HIGH_LENGTH**: 121
- **FOREIGN_FABLE_IMAGERY**: 101
- **AS_ONE_WHO_CADENCE**: 75
- **REPL_AS_TIME_TRAVELLER**: 31
- **BOOL_LEAK_RESOLUTION**: 24
- **ANSWER_LEAK**: 17
- **THE_FORM_OVERUSE**: 16
- **WRONG_FABLE_LITERAL**: 16
- **PARAMETRIC_LITERAL_NUMERALS**: 9
- **CONCEPT_AS_VERB**: 7
- **ANSWER_LEAK_STRING**: 6
- **COLLECTION_LEAK**: 3
- **PREDICATE_QUESTION_COLLISION**: 3
- **SENTENCE_START_LOWER_PRONOUN**: 2
- **SMALL_INT_LEAK**: 1
- **HANGING_FORM_THAT**: 1

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 278 | — |
| 2 | 22 | 88 | 389 | — |
| 3 | 18 | 31 | 163 | — |
| 4 | 20 | 39 | 236 | — |
| 5 | 22 | 39 | 233 | — |
| 6 | 16 | 33 | 145 | — |
| 7 | 18 | 36 | 203 | — |
| 8 | 16 | 31 | 261 | — |
| 9 | 18 | 34 | 204 | — |
| 10 | 16 | 36 | 227 | — |
| 11 | 14 | 29 | 137 | — |
| 12 | 18 | 37 | 108 | — |

### Sample issues by severity

#### FOREIGN_FABLE_IMAGERY

- `G1-01` (form `42`): tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose
    ```
    Some greedy creatures lose what they have to a thief; others lose it to themselves, by way of a careless glance.

At a moss-covered milestone near the road, Guardian the dog sketched a small
wager into the path: whoever guessed the result of `36`
first would win the right to set the next race. Baile...
    ```
- `G1-01` (form `0`): tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    ```
    A reflection is a strange kind of promise: present and unreachable, and very hard to argue with.

A small audience of forest creatures had gathered by the pond to watch
Steel the dog attempt to outwit Yappy the dog at reading the REPL.
Yappy pointed to the value 9 and read out the form aloud:
`9`. T...
    ```
- `G1-01` (form `"hello"`): tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose
    ```
    Ranger the dog was crossing the stream on the road when he caught a glimpse of his own reflection.

At a moss-covered milestone on the road, Caramel the dog sketched a small
wager into the path: whoever guessed the result of `"garnet"`
first would win the right to set the next race. Ranger the dog,
...
    ```
- `G1-01` (form `"hello"`): tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose
    ```
    The path home wound past a slow brook, and on bright days the brook was full of borrowed shapes.

At a moss-covered milestone at the edge of the meadow, Marmalade the dog sketched a small
wager into the path: whoever guessed the result of `"cobalt"`
first would win the right to set the next race. Gi...
    ```
- `G1-01` (form `nil`): tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    ```
    A reflection is a strange kind of promise: present and unreachable, and very hard to argue with.

A small audience of forest creatures had gathered by the pond to watch
Steel the dog attempt to outwit Yappy the dog at reading the REPL.
Yappy pointed to the literal nil and read out the form aloud:
`n...
    ```

#### AS_ONE_WHO_CADENCE

- `G1-01` (form `42`): user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    ```
    Some greedy creatures lose what they have to a thief; others lose it to themselves, by way of a careless glance.

At a moss-covered milestone near the road, Guardian the dog sketched a small
wager into the path: whoever guessed the result of `36`
first would win the right to set the next race. Baile...
    ```
- `G1-01` (form `"hello"`): user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    ```
    Ranger the dog was crossing the stream on the road when he caught a glimpse of his own reflection.

At a moss-covered milestone on the road, Caramel the dog sketched a small
wager into the path: whoever guessed the result of `"garnet"`
first would win the right to set the next race. Ranger the dog,
...
    ```
- `G1-04` (form `"slow and steady"`): user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    ```
    A reflection is a strange kind of promise: present and unreachable, and very hard to argue with.

Buddy the dog and Milo the dog stopped near the meadow where someone had
written the string "indigo" on a flat stone. Buddy, as one who has counted his victory before the running, declared
that he could...
    ```
- `G1-05` (form `false`): user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    ```
    There is a kind of greed that does not see what it already has, and another kind that mistakes a reflection for a meal.

With a twig, Spot the dog marked out a wager in the meadow: whoever
guessed the result of `false` first would win the right to
choose the next contest. Murphy the dog, in the pati...
    ```
- `G1-05` (form `false`): user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    ```
    Some greedy creatures lose what they have to a thief; others lose it to themselves, by way of a careless glance.

Galloper the dog and Charcoal the dog stopped on the river bank where someone had
written the literal false on a flat stone. Galloper, with a pride that filled him from ear-tip to heel, ...
    ```

#### LOW_GROUNDING

- `G1-01` (form `nil`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    A reflection is a strange kind of promise: present and unreachable, and very hard to argue with.

A small audience of forest creatures had gathered by the pond to watch
Steel the dog attempt to outwit Yappy the dog at reading the REPL.
Yappy pointed to the literal nil and read out the form aloud:
`n...
    ```
- `G1-01` (form `nil`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    Ace had found the bone near the road and was carrying it home with no small amount of pride.

Halfway through the race, Hugo the dog stopped on the road and refused to
continue until someone could prove what the form `nil`
evaluated to. Hugo called it impossible.
Ace the dog, walking up at her usual...
    ```
- `G1-02` (form `7`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    It was an afternoon of quiet sky and steady current, and the world below the surface seemed almost solid.

A small audience of forest creatures had gathered at the village to watch
Honey the dog attempt to outwit Hound the dog at reading the REPL.
Hound pointed to the integer 1 and read out the form...
    ```
- `G1-03` (form `1/2`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    in the forest, the stream ran clear enough to mirror anything that passed above it, and Leo passed above it.

Leo the dog had been keeping a small leather notebook of every
form he had successfully evaluated. Today at the edge of the forest, the
next entry was the ratio 1/2. Shepherd the dog peered ...
    ```
- `G1-05` (form `true`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    There was once a dog who carried a fine bone home along a path that crossed a stream by an old wooden bridge.

A small audience of forest creatures had gathered near the meadow to watch
Riley the dog attempt to outwit Yipper the dog at reading the REPL.
Yipper pointed to the literal true and read ou...
    ```

#### CAP_PRONOUN_MID_SENTENCE

- `G1-09` (form `(symbol? 'hare)`): ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    ```
    It happened on a day so ordinary that it seemed impossible anything could have been lost.

"There's a difference between *labeling* the form and
*evaluating* it," Ashy the dog said. "Quote in any of its
shapes is the labeling — the runtime hands you back the form,
not its value, unless you say other...
    ```
- `G1-09` (form `(symbol? 42)`): ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    ```
    It was an afternoon of quiet sky and steady current, and the world below the surface seemed almost solid.

Coal the dog pointed at a name scratched into the bark in the forest,
then at an actual bone lying on the path. "The mark on the bark
is the *name*; the bone is the *value*. They are not the sa...
    ```
- `G1-09` (form `(symbol? 42)`): ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    ```
    It is one of the oldest tricks of light to make one bone seem like two and to make a fool of the unwary.

Russet the dog pointed at a name scratched into the bark near the beach,
then at an actual bone lying on the path. "The mark on the bark
is the *name*; the bone is the *value*. They are not the ...
    ```
- `G1-09` (form `(symbol? "tortoise")`): ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    ```
    Some greedy creatures lose what they have to a thief; others lose it to themselves, by way of a careless glance.

Polly the dog pointed at a name scratched into the bark by the village,
then at an actual bone lying on the path. "The mark on the bark
is the *name*; the bone is the *value*. They are n...
    ```
- `G1-09` (form `(symbol? "tortoise")`): ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    ```
    It was an afternoon of quiet sky and steady current, and the world below the surface seemed almost solid.

Bear the dog pointed at a name scratched into the bark near the meadow,
then at an actual bone lying on the path. "The mark on the bark
is the *name*; the bone is the *value*. They are not the ...
    ```

#### POST_COMMA_CAPITAL_PRONOUN

- `G1-09` (form `(symbol? 'hare)`): capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    ```
    It happened on a day so ordinary that it seemed impossible anything could have been lost.

"There's a difference between *labeling* the form and
*evaluating* it," Ashy the dog said. "Quote in any of its
shapes is the labeling — the runtime hands you back the form,
not its value, unless you say other...
    ```
- `G1-09` (form `(symbol? 42)`): capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    ```
    It was an afternoon of quiet sky and steady current, and the world below the surface seemed almost solid.

Coal the dog pointed at a name scratched into the bark in the forest,
then at an actual bone lying on the path. "The mark on the bark
is the *name*; the bone is the *value*. They are not the sa...
    ```
- `G1-09` (form `(symbol? 42)`): capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    ```
    It is one of the oldest tricks of light to make one bone seem like two and to make a fool of the unwary.

Russet the dog pointed at a name scratched into the bark near the beach,
then at an actual bone lying on the path. "The mark on the bark
is the *name*; the bone is the *value*. They are not the ...
    ```
- `G1-09` (form `(symbol? "tortoise")`): capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    ```
    Some greedy creatures lose what they have to a thief; others lose it to themselves, by way of a careless glance.

Polly the dog pointed at a name scratched into the bark by the village,
then at an actual bone lying on the path. "The mark on the bark
is the *name*; the bone is the *value*. They are n...
    ```
- `G1-09` (form `(symbol? "tortoise")`): capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    ```
    It was an afternoon of quiet sky and steady current, and the world below the surface seemed almost solid.

Bear the dog pointed at a name scratched into the bark near the meadow,
then at an actual bone lying on the path. "The mark on the bark
is the *name*; the bone is the *value*. They are not the ...
    ```

#### STORY_RESOLUTION_NO_DRAWN

- `G1-09` (form `(symbol? 42)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('51',), resolution doesn't close the loop)
    ```
    It was an afternoon of quiet sky and steady current, and the world below the surface seemed almost solid.

Coal the dog pointed at a name scratched into the bark in the forest,
then at an actual bone lying on the path. "The mark on the bark
is the *name*; the bone is the *value*. They are not the sa...
    ```
- `G1-09` (form `(symbol? 42)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('99',), resolution doesn't close the loop)
    ```
    It is one of the oldest tricks of light to make one bone seem like two and to make a fool of the unwary.

Russet the dog pointed at a name scratched into the bark near the beach,
then at an actual bone lying on the path. "The mark on the bark
is the *name*; the bone is the *value*. They are not the ...
    ```
- `G1-09` (form `(symbol? 42)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('68',), resolution doesn't close the loop)
    ```
    Silver had crossed this bridge a hundred times by the village, but never with so fine a bone clamped in his jaws.

Patch the hound stood at the stream's edge, holding two objects side by side: a scratch-mark on bark and a smooth stone bearing the number 68. "This one is the symbol," Patch said, tapp...
    ```
- `G1-09` (form `(symbol? "tortoise")`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('linen',), resolution doesn't close the loop)
    ```
    Some greedy creatures lose what they have to a thief; others lose it to themselves, by way of a careless glance.

Polly the dog pointed at a name scratched into the bark by the village,
then at an actual bone lying on the path. "The mark on the bark
is the *name*; the bone is the *value*. They are n...
    ```
- `G1-09` (form `(symbol? "tortoise")`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('thistle',), resolution doesn't close the loop)
    ```
    The bone was good, the day was warm, and the path was clear, and yet the trouble was already shaped in the water.

Patch the hound held a message scratched on bark — not a name to pass around, but a strand of letters. "The reader will treat this as text, not as a symbol the dogs can quote," Patch sa...
    ```

#### HIGH_LENGTH

- `G1-09` (form `(symbol? 42)`): user_msg 239 words
    ```
    Silver had crossed this bridge a hundred times by the village, but never with so fine a bone clamped in his jaws.

Patch the hound stood at the stream's edge, holding two objects side by side: a scratch-mark on bark and a smooth stone bearing the number 68. "This one is the symbol," Patch said, tapp...
    ```
- `G1-09` (form `(symbol? "tortoise")`): user_msg 218 words
    ```
    The bone was good, the day was warm, and the path was clear, and yet the trouble was already shaped in the water.

Patch the hound held a message scratched on bark — not a name to pass around, but a strand of letters. "The reader will treat this as text, not as a symbol the dogs can quote," Patch sa...
    ```
- `G1-09` (form `(= 'hare 'hare)`): user_msg 236 words
    ```
    in the meadow, where the boards of the bridge meet the stones of the path, Jack the dog caught sight of himself in the stream.

Rex the hound laid two scratch-marks side by side on bark near the forest. Both marks said the same thing: hare, hare. "Are these two scratches the same name?" Rex asked. "...
    ```
- `G1-10` (form `(+ 1 2) ;; sum of one and two`): user_msg 218 words
    ```
    The bone was good, the day was warm, and the path was clear, and yet the trouble was already shaped in the water.

Bell the hound wrote a form on a clean strip of bark near the pond, then added a double-semicolon mark followed by a note in plain words. "The note is only for other dogs to read," she ...
    ```
- `G1-11` (form `(+
  1
  2)`): user_msg 231 words
    ```
    A dog with a bone in his jaws is a happy creature; a dog who looks too hard at the water may not be.

Patch the hound marked a form on a long bark-strip at the stream's edge but spread the tokens across many lines, each indented neatly. "Does the layout change what the form says?" his packmate asked...
    ```

#### BOOL_LEAK_RESOLUTION

- `G1-09` (form `(symbol? 42)`): resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    ```
    Silver had crossed this bridge a hundred times by the village, but never with so fine a bone clamped in his jaws.

Patch the hound stood at the stream's edge, holding two objects side by side: a scratch-mark on bark and a smooth stone bearing the number 68. "This one is the symbol," Patch said, tapp...
    ```
- `G1-09` (form `(symbol? "tortoise")`): resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    ```
    The bone was good, the day was warm, and the path was clear, and yet the trouble was already shaped in the water.

Patch the hound held a message scratched on bark — not a name to pass around, but a strand of letters. "The reader will treat this as text, not as a symbol the dogs can quote," Patch sa...
    ```
- `G1-09` (form `(= 'hare 'hare)`): resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    ```
    in the meadow, where the boards of the bridge meet the stones of the path, Jack the dog caught sight of himself in the stream.

Rex the hound laid two scratch-marks side by side on bark near the forest. Both marks said the same thing: hare, hare. "Are these two scratches the same name?" Rex asked. "...
    ```
- `G1-16` (form `(pos? -2)`): resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    ```
    The bone was good, the day was warm, and the path was clear, and yet the trouble was already shaped in the water.

Patch the hound held a negative number on bark near the forest and asked: "Is this count moving forward from the marker stone?" "Let the runtime check," someone said.

Patch wanted the ...
    ```
- `G1-16` (form `(neg? -3)`): resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    ```
    On a path that ran beside the stream, a dog was carrying his supper home and looking pleased with himself.

Bell the hound marked a negative number on flat bark at the pond and asked: "Is this count moving backward from the starting point?" "The runtime can check," her packmate said.

She wanted the...
    ```

#### CLAUSE_STACK_OVERFLOW

- `G1-09` (form `(= 'hare 'hare)`): sentence with 5 commas reads as AI-output cadence: "The\nreflection in the stream looks like a bone, but the scratch that\nsays 'bone'"
    ```
    On a path that ran beside the stream, a dog was carrying his supper home and looking pleased with himself.

Oscar the dog pointed at a name scratched into the bark near the beach,
then at an actual bone lying on the path. "The mark on the bark
is the *name*; the bone is the *value*. They are not the...
    ```
- `G1-10` (form `(+ 1 2) ;; sum of one and two`): sentence with 5 commas reads as AI-output cadence: 'To add 2 and 9, with a double-semicolon trailing comment, she, her promise small'
    ```
    The bone was good, the day was warm, and the path was clear, and yet the trouble was already shaped in the water.

Bell the hound wrote a form on a clean strip of bark near the pond, then added a double-semicolon mark followed by a note in plain words. "The note is only for other dogs to read," she ...
    ```
- `G1-10` (form `(+ 1 2) ;; sum of one and two`): sentence with 6 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'
    ```
    A dog with a bone in his jaws is a happy creature; a dog who looks too hard at the water may not be.

"A form is what's actually there on the bark," Cocoa the dog
said, "after the conventions of writing and reading have done
their work. The runtime sees the cleaned-up form, evaluates it,
and gives b...
    ```
- `G1-12` (form `(+ 2 3)`): sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'
    ```
    at the edge of the meadow, where the path crosses the stream, Topsy the dog trotted home with a fine bone in his teeth.

"A form is what's actually there on the bark," Topsy the dog
said, "after the conventions of writing and reading have done
their work. The runtime sees the cleaned-up form, evalua...
    ```
- `G1-17` (form `(+ 1 2)`): sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'
    ```
    It was near the pond, on the wooden bridge above the slow brook, that Mocha the dog looked down at the water.

"A form is what's actually there on the bark," Mocha the dog
said, "after the conventions of writing and reading have done
their work. The runtime sees the cleaned-up form, evaluates it,
an...
    ```

#### THE_FORM_OVERUSE

- `G1-11` (form `(+
  1
  2)`): `the form` appears 6 times in user_msg (template tic — vary references)
    ```
    A dog with a bone in his jaws is a happy creature; a dog who looks too hard at the water may not be.

Patch the hound marked a form on a long bark-strip at the stream's edge but spread the tokens across many lines, each indented neatly. "Does the layout change what the form says?" his packmate asked...
    ```
- `G3-03` (form `(let [x 3] (+ x 1))`): `the form` appears 6 times in user_msg (template tic — vary references)
    ```
    Diesel had crossed this bridge a hundred times on the beach, but never with so fine a bone clamped in his jaws.

Bell the hound had picked up a small bone near the pond and held it firmly between her jaws. Just for the next stretch of crossing she would need to know the bone's tally — 7 — by a short...
    ```
- `G3-03` (form `(let [a 5] a)`): `the form` appears 6 times in user_msg (template tic — vary references)
    ```
    On a path that ran beside the stream, a dog was carrying his supper home and looking pleased with himself.

Bell the hound found a bone near the meadow, five joints long, and cradled it between her teeth. "For this one stretch of the path, I will know this bone by the name a," she said through the g...
    ```
- `G3-05` (form `(do (def x 10) (let [x 99] x))`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    Down by the stream where the bank dipped low, the world above was answered politely by the world below.

Bell the hound marked a stone with the name x and value 15. One day, she picked up a larger bone and held it in her jaws. "For this form, x means what I hold — not what's on the stone."

The form...
    ```
- `G3-06` (form `(let [a 5 b (* a 2)] b)`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    Some lessons are taught by mirrors, and some are taught by rivers; this one was taught by both at once.

Rex the hound gathered five bones and clamped them in his jaws as the name a. Before stepping forward, he computed in his mind what twice that grip would weigh — and held both the first grip and ...
    ```

#### ANSWER_LEAK

- `G1-12` (form `(* (+ 1 2) 3)`): answer 9 in narrative
    ```
    On a path that ran beside the stream, a dog was carrying his supper home and looking pleased with himself.

Patch the hound marked a nested form on a flat stone near the bank, with one grouped form tucked inside another. "The inner group runs first," Patch said. "Its value becomes the input to the o...
    ```
- `G1-12` (form `(* (+ 1 2) 3)`): answer 9 in narrative
    ```
    Cinnamon the dog was halfway home in the pond when the water played its old trick on a young dog.

Cinnamon the dog smoothed a fresh strip of bark at the edge of the pond and
scratched slowly, paying attention to every mark. "The form has
to be written so the reader can read it cleanly,"
he said. "I...
    ```
- `G1-14` (form `(+ 1 (* 2 3))`): answer 7 in narrative
    ```
    at the edge of the forest, the stream ran clear enough to mirror anything that passed above it, and Alabaster passed above it.

Alabaster the dog laid bones out on a flat stone by the forest, sorting
them into small piles. "Numbers in Clojure are just like bones
in piles," she said: "you can count t...
    ```
- `G2-22` (form `(+ (* 3 8) (* 2 4))`): answer 32 in narrative
    ```
    There was once a dog who carried a fine bone home along a path that crossed a stream by an old wooden bridge.

Bell the hound had two tasks near the pond. First, she needed to multiply 4 and 5 to get one pile. Then, she would multiply 8 and 6 to get another pile. Finally, she would add them together...
    ```
- `G2-22` (form `(+ (* 3 8) (* 2 4))`): answer 32 in narrative
    ```
    by the beach, on a still afternoon by the brook, Scoutmaster learned what a reflection costs the careless.

Bell the hound had two tasks near the pond. First, she needed to multiply 9 and 4 to get one pile. Then, she would multiply 1 and 1 to get another pile. Finally, she would add them together.

...
    ```

#### REPL_AS_TIME_TRAVELLER

- `G1-13` (form `(+ 1 2)`): user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    ```
    Charcoal had crossed this bridge a hundred times near the river bank, but never with so fine a bone clamped in his jaws.

Fudge the dog eyed the pile, with the cold appetite of unceasing want, and called out a guess
about how many bones were there without bothering to count.
Charcoal the dog simply ...
    ```
- `G1-13` (form `(/ 10 2)`): user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    ```
    Auburn had found the bone near the river bank and was carrying it home with no small amount of pride.

Tucker the dog eyed the pile, with the hard glitter of one who must have more, and called out a guess
about how many bones were there without bothering to count.
Auburn the dog simply began countin...
    ```
- `G1-13` (form `(- 20 7)`): user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    ```
    Tawny the dog was halfway home by the pond when the water played its old trick on a young dog.

Polly the dog eyed the pile, with the hard glitter of one who must have more, and called out a guess
about how many bones were there without bothering to count.
Tawny the dog simply began counting — to su...
    ```
- `G1-14` (form `(- 100 (* 5 5))`): user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    ```
    Some greedy creatures lose what they have to a thief; others lose it to themselves, by way of a careless glance.

Henry the dog eyed the pile, his thoughts already on more, and called out a guess
about how many bones were there without bothering to count.
Wallace the dog simply began counting — to s...
    ```
- `G1-14` (form `(+ (* 2 3) (* 4 5))`): user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    ```
    It happened along the road, on the very bridge Inky the dog crossed every day, that he stopped longer than he should have.

Charcoal the dog eyed the pile, with the hard glitter of one who must have more, and called out a guess
about how many bones were there without bothering to count.
Inky the dog...
    ```

#### SENTENCE_START_LOWER_PRONOUN

- `G1-13` (form `(+ 7 8)`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    Honey had crossed this bridge a hundred times along the river bank, but never with so fine a bone clamped in his jaws.

Rex the hound gathered seven bones from one bank and eight from another. "Should I count them all?" he asked. "Let the runtime add them together. It will give the exact total."

He...
    ```
- `G3-15` (form `(do (println "hi") 42)`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    When Bruno reached the bridge in the village, he paused to admire the bone he had been so lucky to find.

Bell the hound barked a signal across the bank near the forest — "Hi!" she called out, watching it echo into the canyon. "That bark had its moment," she said. "But what I carry back is not the s...
    ```

#### WRONG_FABLE_LITERAL

- `G1-15` (form `(= 1 1)`): tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    ```
    near the road, where the path crosses the stream, Pip the dog trotted home with a fine bone in his teeth.

"You can't tell whether the crossing will be open by guessing,"
Pip the dog said. "You bring the value to the bank, the
runtime checks it, and the conditions give the only answer that
matters."...
    ```
- `G2-15` (form `(if 0 1 0)`): tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    ```
    near the road, where the path crosses the stream, Pip the dog trotted home with a fine bone in his teeth.

"You can't tell whether the crossing will be open by guessing,"
Pip the dog said. "You bring the value to the bank, the
runtime checks it, and the conditions give the only answer that
matters."...
    ```
- `G3-15` (form `(do (println "hi") 42)`): tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    ```
    near the road, where the path crosses the stream, Pip the dog trotted home with a fine bone in his teeth.

"On any nose-trail," Pip the dog explained, "the last sniff
is what you carry home." He took the goal — to
execute a print statement for side-effects, then return a different value — and laid o...
    ```
- `G4-15` (form `(first [10 20 30])`): tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    ```
    near the road, where the path crosses the stream, Pip the dog trotted home with a fine bone in his teeth.

A row of bones lay tucked end-to-end inside the log on the road, head
at the front, the rest trailing behind. "Many of our caches are
like this row," Pip the dog said. "You can grab the first b...
    ```
- `G5-15` (form `((comp inc inc) 5)`): tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    ```
    near the road, where the path crosses the stream, Pip the dog trotted home with a fine bone in his teeth.

"On any nose-trail," Pip the dog explained, "the last sniff
is what you carry home." He took the goal — to
compose two inc functions and apply them to 5 — and laid out the routine's paw-steps i...
    ```

#### SMALL_INT_LEAK

- `G2-05` (form `(mod -7 3)`): small-int answer 2 leaks via resolution-slot phrasing
    ```
    It is one of the oldest tricks of light to make one bone seem like two and to make a fool of the unwary.

Bell the hound stood by the river bank holding a negative value — negative seven — and wanted to find its modulo against three. Negative numbers in modulo work in their own way.

She needed to k...
    ```

#### CONCEPT_AS_VERB

- `G3-07` (form `((fn [a b] (* a b)) 3 4)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    by the beach, on a still afternoon by the brook, Jasper learned what a reflection costs the careless.

"A nose-trail is only useful when it gets walked," Jasper the dog
said, head low. "You set out the sniffs, you bring the
ingredients, the runtime does the rest." To create an anonymous function tha...
    ```
- `G3-10` (form `(#(+ % 1) 5)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    Bayer had crossed this bridge a hundred times near the forest, but never with so fine a bone clamped in his jaws.

"A nose-trail is only useful when it gets walked," Bayer the dog
said, head low. "You set out the sniffs, you bring the
ingredients, the runtime does the rest." To use the shorthand syn...
    ```
- `G3-10` (form `(#(+ % 1) 5)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    Beau had found the bone at the edge of the pond and was carrying it home with no small amount of pride.

"A nose-trail is only useful when it gets walked," Beau the dog
said, head low. "You set out the sniffs, you bring the
ingredients, the runtime does the rest." To use the shorthand syntax to crea...
    ```
- `G3-10` (form `(#(* %1 %2) 3 4)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    in the meadow, where the boards of the bridge meet the stones of the path, Bingo the dog caught sight of himself in the stream.

"A nose-trail is only useful when it gets walked," Bingo the dog
said, head low. "You set out the sniffs, you bring the
ingredients, the runtime does the rest." To use the...
    ```
- `G5-15` (form `((comp str inc) 9)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    It is one of the oldest tricks of light to make one bone seem like two and to make a fool of the unwary.

"A nose-trail is only useful when it gets walked," Peach the dog
said, head low. "You set out the sniffs, you bring the
ingredients, the runtime does the rest." To compose str and inc functions ...
    ```

#### PARAMETRIC_LITERAL_NUMERALS

- `G4-01` (form `[1 2 3]`): parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    ```
    Bayer had crossed this bridge a hundred times in the meadow, but never with so fine a bone clamped in his jaws.

A row of bones lay tucked end-to-end inside the log in the meadow, head
at the front, the rest trailing behind. "Many of our caches are
like this row," Bayer the dog said. "You can grab t...
    ```
- `G4-01` (form `[1 2 3]`): parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    ```
    Sooty had crossed this bridge a hundred times near the river bank, but never with so fine a bone clamped in his jaws.

Sooty the dog pointed to a hollow log on the river bank, its inside lined
with bones tucked into named slots. "Whatever I want to do with
what's cached," he said, "I read from the l...
    ```
- `G4-01` (form `[1 2 3]`): parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    ```
    It is one of the oldest tricks of light to make one bone seem like two and to make a fool of the unwary.

Woofer the dog pointed to a hollow log along the river bank, its inside lined
with bones tucked into named slots. "Whatever I want to do with
what's cached," she said, "I read from the log, work...
    ```
- `G4-03` (form `(conj [1 2] 3)`): parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    ```
    Diesel had crossed this bridge a hundred times on the beach, but never with so fine a bone clamped in his jaws.

Patch the hound tended a hollow log cache holding two bones already: one and two. A third bone lay nearby, ready to be added to the end of the row.

Patch wanted the third bone packed int...
    ```
- `G4-03` (form `(conj [1 2] 3)`): parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    ```
    When Sprocket reached the bridge in the forest, she paused to admire the bone he had been so lucky to find.

Sprocket the dog pointed to a hollow log by the forest, its inside lined
with bones tucked into named slots. "Whatever I want to do with
what's cached," she said, "I read from the log, work
t...
    ```

#### HANGING_FORM_THAT

- `G4-04` (form `'()`): 'form that <noun>' rendered without a verb — template should be 'form for {concept_phrase}'
    ```
    On a path that ran beside the stream, a dog was carrying his supper home and looking pleased with himself.

Patch the hound picked up an empty chain by the bank, a mere collar with no bones attached, and held it up.

Patch wanted the empty chain itself to be a recognizable form that the REPL would h...
    ```

#### COLLECTION_LEAK

- `G5-10` (form `(map inc [1 2 3])`): elements of expected [2, 3, 4] appear comma-separated in user_msg (collection answer leak)
    ```
    The bone was good, the day was warm, and the path was clear, and yet the trouble was already shaped in the water.

Rex held bones marked 1, 2, 3 at the stream. A log above held a gap shaped like inc: take a bone, add 1, drop the result on the far bank. Map would pour all three through, one at a time...
    ```
- `G12-01` (form `(into [] (map inc) [1 2 3])`): elements of expected [2, 3, 4] appear comma-separated in user_msg (collection answer leak)
    ```
    There is a kind of greed that does not see what it already has, and another kind that mistakes a reflection for a meal.

Bell the hound found a log with a gap at the stream's edge, the opening shaped to add one bone's weight to any bone that passed through. Laid before it lay a row of light bones — ...
    ```
- `G12-03` (form `(into #{} (map inc) [1 2 3])`): elements of expected {2, 3, 4} appear comma-separated in user_msg (collection answer leak)
    ```
    Diesel had crossed this bridge a hundred times on the beach, but never with so fine a bone clamped in his jaws.

Rex the hound stood at the stream's edge with two kinds of receivers: an empty row and an empty pile. He had a gap that added weight, and bones 1, 2, 3 lay ready. "The gap is the same rul...
    ```

#### PREDICATE_QUESTION_COLLISION

- `G5-18` (form `(some neg? [1 2 3])`): predicate-suffix ``?`` collides with the question framing's trailing ``?`` or ``.``
    ```
    Down by the stream where the bank dipped low, the world above was answered politely by the world below.

Bell the hound held a pile of bones marked 1, 2, 3 by the river bank. A gap-sieve before her had a different rule: only negative-marked bones can pass. She wanted to know: does any bone fit throu...
    ```
- `G5-18` (form `(some neg? [1 2 3])`): predicate-suffix ``?`` collides with the question framing's trailing ``?`` or ``.``
    ```
    It was on the river bank, on the wooden bridge above the slow brook, that Gizmo the dog looked down at the water.

Bell the hound held a pile of bones marked 1, 2, 3 by the river bank. A gap-sieve before her had a different rule: only negative-marked bones can pass. She wanted to know: does any bone...
    ```
- `G5-19` (form `(every? pos? [1 2 3])`): predicate-suffix ``?`` collides with the question framing's trailing ``?`` or ``.``
    ```
    Peach the dog was crossing the stream near the village when she caught a glimpse of his own reflection.

Patch the hound held a pile of bones marked 1, 2, 3 at the stream near the forest. A gap-sieve had a rule: only positive-marked bones can pass. She wanted to know: will every bone in this pile fi...
    ```

#### ANSWER_LEAK_STRING

- `G6-01` (form `(name 'foo.bar)`): answer string 'foo.bar' appears in user_msg
    ```
    There is a kind of greed that does not see what it already has, and another kind that mistakes a reflection for a meal.

Patch the hound examined a marker stone at the stream's edge with a strange dotted path scratched into it — foo.bar. {hound_he_she} wanted to read what the scratch said without us...
    ```
- `G6-05` (form `(namespace :owner/item)`): answer string 'owner' appears in user_msg
    ```
    It happened at the edge of the forest, on the very bridge Bingo the dog crossed every day, that he stopped longer than he should have.

At the forest edge, Bell found a marker with a qualified keyword written there — low. The mark had two parts separated by a slash, and she wondered what lay before ...
    ```
- `G6-05` (form `(name :owner/item)`): answer string 'item' appears in user_msg
    ```
    The path home wound past a slow brook, and on bright days the brook was full of borrowed shapes.

Looking at the same marker :owner/item, Bell now wanted the other half — the local name after the slash, to see what kind of thing the owner had stored.

She wanted to pull the name portion from the qua...
    ```
- `G7-11` (form `(try (throw (ex-info "trouble" {})) (catch Exception e (.get`): answer string 'trouble' appears in user_msg
    ```
    It is one of the oldest tricks of light to make one bone seem like two and to make a fool of the unwary.

Alabaster the dog stepped onto a fallen log spanning the stream
near the forest, testing its hold paw by paw before trusting full weight.
"If the log gives, I retreat to the bank; the run doesn'...
    ```
- `G8-03` (form `(do (defrecord Runner [name pace]) (:pace (->Runner "Alice" `): answer string ':slow' appears in user_msg
    ```
    Diesel had crossed this bridge a hundred times on the beach, but never with so fine a bone clamped in his jaws.

Bell the hound crafted a labeled kennel-bag for tracking runners. The bag had two named compartments — one for a runner's name, one for the runner's pace-style. She slipped "Alice" and :s...
    ```

