# dog-shadow curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

### G1-01: Eval as substitution

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'FOREIGN_FABLE_IMAGERY': 2}
    - [LOW_GROUNDING] form=`0` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`0` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`nil` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`nil` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`nil` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-02: Integer numbers

- examples: 6
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 6, 'LOW_GROUNDING': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`7` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`7` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`7` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`-3` — tortoise-hare-specific imagery 'leather notebook' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`0` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`100` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose

### G1-03: Ratios

- examples: 5
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 6, 'LOW_GROUNDING': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`1/2` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`1/2` — tortoise-hare-specific imagery 'leather notebook' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`1/2` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`3/4` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`(+ 1/2 1/4)` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`(* 2 1/2)` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose

### G1-05: Booleans

- examples: 6
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 5, 'LOW_GROUNDING': 6}
    - [FOREIGN_FABLE_IMAGERY] form=`true` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`true` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`false` — tortoise-hare-specific imagery 'leather notebook' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`false` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(= 1 1)` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`(= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-06: nil

- examples: 5
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 6, 'LOW_GROUNDING': 4}
    - [FOREIGN_FABLE_IMAGERY] form=`nil` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`nil` — tortoise-hare-specific imagery 'leather notebook' leaks into dog-shadow prose
    - [LOW_GROUNDING] form=`nil` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(nil? nil)` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`(nil? nil)` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`(nil? 0)` — tortoise-hare-specific imagery 'leather notebook' leaks into dog-shadow prose

### G1-07: Keywords

- examples: 5
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 7}
    - [FOREIGN_FABLE_IMAGERY] form=`:hare` — tortoise-hare-specific imagery 'leather notebook' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`:hare` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`:hare` — tortoise-hare-specific imagery 'leather notebook' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`:tortoise` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`:tortoise` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`(keyword? :hare)` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose

### G1-09: Symbols vs values

- examples: 4
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 5, 'CAP_PRONOUN_MID_SENTENCE': 5, 'POST_COMMA_CAPITAL_PRONOUN': 5, 'STORY_RESOLUTION_NO_DRAWN': 2, 'HIGH_LENGTH': 1, 'BOOL_LEAK_RESOLUTION': 1}
    - [LOW_GROUNDING] form=`(symbol? 'hare)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(symbol? 'hare)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(symbol? 'hare)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(symbol? 'hare)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(symbol? 42)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(symbol? 42)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G1-12: Parens group; they don't multiply

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G1-13: First arithmetic call

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'STORY_RESOLUTION_NO_DRAWN': 7}
    - [LOW_GROUNDING] form=`(+ 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(+ 1 2)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(+ 1 2)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(+ 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(+ 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(- 5 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '3'), resolution doesn't close the loop)

### G1-15: Equality

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 5, 'SENTENCE_START_LOWER_PRONOUN': 1, 'BOOL_LEAK_RESOLUTION': 1}
    - [LOW_GROUNDING] form=`(= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= :hare :hare)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':hare'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= :hare :hare)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':hare'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= :hare :hare)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':hare'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= :hare :tortoise)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':tortoise'), resolution doesn't close the loop)

### G1-16: Numeric predicates

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 12, 'BOOL_LEAK_RESOLUTION': 4}
    - [LOW_GROUNDING] form=`(zero? 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(zero? 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(zero? 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(zero? 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(zero? 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(pos? 7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)

### G1-17: Printing vs returning

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'STORY_RESOLUTION_NO_DRAWN': 2, 'LOW_GROUNDING': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`42` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`42` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`42` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`42` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(+ 1 2)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(+ 1 2)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G1-18: Errors are safe in the REPL

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'LOW_GROUNDING': 2}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(+ 1 2)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(+ 1 2)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(+ 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(+ 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 2

### G2-02: Comparison chains

- examples: 5
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(< 3 2 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G2-03: not= and = with multiple args

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'BOOL_LEAK_RESOLUTION': 1}
    - [LOW_GROUNDING] form=`(not= 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(not= 1 1)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(not= 1 1)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(not= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [BOOL_LEAK_RESOLUTION] form=`(= 1 1 1)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead

### G2-06: inc and dec

- examples: 5
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 7, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'LOW_GROUNDING': 5}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inc 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inc 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inc 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(dec 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(dec 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(dec 5)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G2-07: Absolute value

- examples: 4
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 5}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(abs 5)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(abs 5)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(abs -5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(abs -5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-5',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(abs -5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(abs -5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-5',), resolution doesn't close the loop)

### G2-08: Arithmetic on ratios

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 9, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [LOW_GROUNDING] form=`(+ 1/2 1/4)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1/2 1/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1/2 1/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(+ 1/2 1/4)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(+ 1/2 1/4)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(+ 1/2 1/4)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-09: Floats vs ints (the / operator)

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(/ 10 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(/ 10 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10',), resolution doesn't close the loop)

### G2-10: Powers via repeated multiplication

- examples: 4
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 3, 'WRONG_FABLE_LITERAL': 1, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'LOW_GROUNDING': 1, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(* 2 2 2)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [WRONG_FABLE_LITERAL] form=`(* 2 2 2)` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(* 2 2 2)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(* 2 2 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(* 5 5)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(* 5 5)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G2-13: and / or — short circuit, return values

- examples: 6
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 3, 'LOW_GROUNDING': 8}
    - [BOOL_LEAK_RESOLUTION] form=`(and true true)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(and true false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [BOOL_LEAK_RESOLUTION] form=`(and true false)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(and true false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-14: not — turning truthy to false

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 8}
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-15: Falsey values: only false and nil

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(if 0 1 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-16: Truthy 0 and empty string

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(boolean 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(boolean 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(boolean nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(boolean nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(boolean false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-18: Quoting symbols

- examples: 3
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 6, 'BOOL_LEAK_RESOLUTION': 2, 'HIGH_LENGTH': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(symbol? (quote hare))` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(symbol? (quote hare))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [BOOL_LEAK_RESOLUTION] form=`(symbol? (quote hare))` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(symbol? (quote hare))` — user_msg 201 words

### G2-19: Auto-promotion to bigint

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(* 1000000 1000000)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(* 1000000 1000000)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(* 1000000 1000000)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 1000000 1000000)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('1000000', '1000000'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 1000000 1000000)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('1000000', '1000000'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(* 1000000 1000000)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-22: Compose pure arithmetic (multi-step calculation)

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(- (* 5 4) 7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '4', '7'), resolution doesn't close the loop)

## Grade 3

### G3-01: def — top-level binding

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 4}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 42) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def y 7) y)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def y 7) y)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def y 7) y)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)

### G3-03: let — local binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 7, 'HIGH_LENGTH': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 3] (+ x 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [n 10] (* n n))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(let [n 10] (* n n))` — user_msg 246 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [n 10] (* n n))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(let [n 10] (* n n))` — user_msg 251 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [n 10] (* n n))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10',), resolution doesn't close the loop)

### G3-04: let — multi-binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 4}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 5 y 3] (- x y))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 5 y 3] (- x y))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 5 y 3] (- x y))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 2 b 3 c 4] (+ a b c))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)

### G3-06: let — binding can reference prior

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 2}
    - [HIGH_LENGTH] form=`(let [a 5 b (* a 2)] b)` — user_msg 262 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 5 b (* a 2)] b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G3-07: fn — anonymous function

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'CONCEPT_AS_VERB': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (+ x 1)) 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (+ x 1)) 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (+ x 1)) 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`((fn [a b] (* a b)) 3 4)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`((fn [a b] (* a b)) 3 4)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CONCEPT_AS_VERB] form=`((fn [a b] (* a b)) 3 4)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G3-08: fn — multi-arg

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`((fn [a b c] (+ a b c)) 1 2 3)` — user_msg 208 words

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
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`((fn [x] (* x x)) 6)` — user_msg 229 words

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

### G3-16: Name collision: namespace vs let

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'STORY_RESOLUTION_NO_DRAWN': 1}
    - [LOW_GROUNDING] form=`(let [+ 99] +)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [+ 99] +)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99',), resolution doesn't close the loop)

### G3-18: When to name vs inline

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [HIGH_LENGTH] form=`(let [n 5] (* n n n))` — user_msg 252 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [n 5] (* n n n))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [n 5] (* n n n))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [n 5] (* n n n))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 5 5 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '5', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 5 5 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '5', '5'), resolution doesn't close the loop)

## Grade 4

### G4-01: Vector literal

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`["a" "b"]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`["a" "b"]` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`["a" "b"]` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G4-11: Set literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(count #{1 1 1})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count #{1 1 1})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-16: into and conj on collections

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(into #{} [1 2 2 3])` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(into #{} [1 2 2 3])` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(into #{} [1 2 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into #{} [1 2 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(into #{} [1 2 2 3])` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(into #{} [1 2 2 3])` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G4-19: range and seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (range 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (range 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(count (range 5))` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(count (range 5))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (range 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)

## Grade 5

### G5-01: if

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if true :a :b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b'), resolution doesn't close the loop)

### G5-08: not

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(not (> 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G5-10: map

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(map #(* % %) [1 2 3 4])` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(map #(* % %) [1 2 3 4])` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(map #(* % %) [1 2 3 4])` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(map #(* % %) [1 2 3 4])` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

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

### G5-22: recur — first taste

- examples: 1
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 3, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [HIGH_LENGTH] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — user_msg 229 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — user_msg 228 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — user_msg 226 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)

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

### G6-05: Fully qualified names

- examples: 4
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 2, 'ANSWER_LEAK_STRING': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(clojure.string/reverse "abc")` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(clojure.string/reverse "abc")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/reverse "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/reverse "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/reverse "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(name :owner/item)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta '^:private hidden)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private', ':private'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta '^:private hidden)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private', ':private'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta '^:private hidden)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private', ':private'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta 'public)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta 'public)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta 'public)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private',), resolution doesn't close the loop)

### G6-08: Circular dependencies

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'LOW_GROUNDING': 2}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(= 'a.b 'a.b)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(= 'a.b 'a.b)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(= 'a.b 'a.b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 'a.b 'a.b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-09: Loading order

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 5, 'HIGH_LENGTH': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(let [a 1 b (+ a 1)] (+ a b))` — user_msg 224 words

### G6-10: Leiningen and deps.edn

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
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

### G6-14: Import for host classes

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3}
    - [LOW_GROUNDING] form=`(symbol? 'java.util.List)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(symbol? 'java.util.List)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(symbol? 'java.util.List)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(symbol? 'java.util.List)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(name 'java.util.Map)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(name 'java.util.Map)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

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
    - [HIGH_LENGTH] form=`(:doc (meta '\{:doc "steady wins"\} race))` — user_msg 205 words

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
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(try (throw (Exception. "bad")) (catch Exception e` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(try (throw (Exception. "bad")) (catch Exception e` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(try (throw (Exception. "bad")) (catch Exception e` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "bad")) (catch Exception e` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1', 'bad'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(try (throw (Exception. "bad")) (catch Exception e` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "bad")) (catch Exception e` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1', 'bad'), resolution doesn't close the loop)

### G7-03: try / finally

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 3}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(try 7 (finally (prn :cleanup)))` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(try 7 (finally (prn :cleanup)))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(try 7 (finally (prn :cleanup)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(try (try (/ 1 0) (finally (prn :ran))) (catch Exc` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(try (try (/ 1 0) (finally (prn :ran))) (catch Exc` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(try (try (/ 1 0) (finally (prn :ran))) (catch Exc` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

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
- issues: {'CAP_PRONOUN_MID_SENTENCE': 5, 'POST_COMMA_CAPITAL_PRONOUN': 5, 'LOW_GROUNDING': 12}
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
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (assert (= 1 1)) 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-08: prn and pprint

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(with-out-str (prn 42))` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(with-out-str (prn 42))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(with-out-str (prn :hare))` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(with-out-str (prn :hare))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
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
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'ANSWER_LEAK_STRING': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(try (throw (Exception. "oops")) (catch Exception ` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(try (throw (Exception. "oops")) (catch Exception ` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(try (throw (Exception. "oops")) (catch Exception ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(try (throw (Exception. "oops")) (catch Exception ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)

### G7-12: slurp and spit

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "a\nb\nc" #"\n")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc', '\\n'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(clojure.string/split "a\nb\nc" #"\n")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "a\nb\nc" #"\n")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc', '\\n'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(clojure.string/split "a\nb\nc" #"\n")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "a\nb\nc" #"\n")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc', '\\n'), resolution doesn't close the loop)

### G7-13: line-seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)

### G7-14: with-open

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(with-out-str (println "hare"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(with-out-str (println "hare"))` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(with-out-str (println "hare"))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(with-out-str (println "hare"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-15: *in* and *out*

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'LOW_GROUNDING': 6, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [WRONG_FABLE_LITERAL] form=`(with-out-str (print "x"))` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [LOW_GROUNDING] form=`(with-out-str (print "x"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(with-out-str (print "x"))` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(with-out-str (print "x"))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(with-out-str (print "x"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (print "x"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-16: edn read

- examples: 3
- variety @ n=50: 0.99
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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'LOW_GROUNDING': 5}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 8

### G8-01: Why polymorphism

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':tortoise', ':else'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':tortoise', ':else'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':tortoise', ':else'), resolution doesn't close the loop)

### G8-02: deftype introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)

### G8-03: defrecord introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'ANSWER_LEAK_STRING': 1, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CAP_PRONOUN_MID_SENTENCE': 5, 'POST_COMMA_CAPITAL_PRONOUN': 5, 'LOW_GROUNDING': 3}
    - [HIGH_LENGTH] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — user_msg 206 words
    - [ANSWER_LEAK_STRING] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — answer string ':slow' appears in user_msg
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':pace', ':slow', 'Alice'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':pace', ':slow', 'Alice'), resolution doesn't close the loop)

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
- issues: {'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('swift', 'hare'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G8-06: Protocol method dispatch

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 4, 'POST_COMMA_CAPITAL_PRONOUN': 4, 'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 3}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G8-07: Record implementing protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':swift', 'Pip'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':swift', 'Pip'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':swift', 'Pip'), resolution doesn't close the loop)

### G8-08: Multimethod defmulti

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmulti pace :species) (defmethod pace :hare` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':species', ':hare', ':swift'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmulti pace :species) (defmethod pace :hare` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':species', ':hare', ':swift'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmulti pace :species) (defmethod pace :hare` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':species', ':hare', ':swift'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defmulti tag :kind) (defmethod tag :stone [_]` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defmulti tag :kind) (defmethod tag :stone [_]` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defmulti tag :kind) (defmethod tag :stone [_]` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G8-09: Multimethod defmethod

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defmulti pace :species) (defmethod pace :hare` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defmulti pace :species) (defmethod pace :hare` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G8-10: Multimethod vs protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'LOW_GROUNDING': 3}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defmulti show identity) (defmethod show :rabb` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defmulti show identity) (defmethod show :rabb` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defmulti show identity) (defmethod show :rabb` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defmulti show identity) (defmethod show :rabb` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (defprotocol Show (show [this])) (extend-proto` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol Show (show [this])) (extend-proto` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G8-11: Protocol vs Java interface

- examples: 1
- variety @ n=50: 0.98
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'LOW_GROUNDING': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol IPace (run [this])) (extend-proto` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defprotocol IPace (run [this])) (extend-proto` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (defprotocol IPace (run [this])) (extend-proto` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-12: extend-type on built-in types

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-type` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-type` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-type` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-13: this-style vs fn-style

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3}
    - [LOW_GROUNDING] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Named (name-of [this])) (defrecor` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':n', 'Zephyr'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol Named (name-of [this])) (defrecor` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defprotocol Named (name-of [this])) (defrecor` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Named (name-of [this])) (defrecor` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':n', 'Zephyr'), resolution doesn't close the loop)

### G8-14: Protocols don't inherit

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [HIGH_LENGTH] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg 216 words
    - [LOW_GROUNDING] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-15: derive and isa? — multimethod hierarchy

- examples: 3
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'BOOL_LEAK_RESOLUTION': 2, 'LOW_GROUNDING': 5, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [WRONG_FABLE_LITERAL] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [BOOL_LEAK_RESOLUTION] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(isa? java.lang.Long java.lang.Number)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(isa? java.lang.Long java.lang.Number)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(isa? java.lang.Long java.lang.Number)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(isa? java.lang.Long java.lang.Number)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G8-16: Abstract design with protocols

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 5, 'POST_COMMA_CAPITAL_PRONOUN': 5, 'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':leap', ':plod'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

## Grade 9

### G9-02: Why state at all

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1}
    - [LOW_GROUNDING] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def progress (atom :idle)) (reset! progress :` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def progress (atom :idle)) (reset! progress :` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':idle', ':running'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(do (def progress (atom :idle)) (reset! progress :` — user_msg 243 words

### G9-03: Atom introduction

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'LOW_GROUNDING': 4}
    - [HIGH_LENGTH] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg 240 words
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom :start)) (reset! a :done) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom :start)) (reset! a :done) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom :start)) (reset! a :done) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-04: Atom CAS semantics

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-05: Watch on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':w',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':w',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':w',), resolution doesn't close the loop)

### G9-06: Validator on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-07: Ref introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('100', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('100', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('100', '7'), resolution doesn't close the loop)

### G9-08: dosync and alter

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '5'), resolution doesn't close the loop)

### G9-09: Ref vs atom

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-10: Agent introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def ag (agent 5)) (send ag + 10) (await ag) @` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (def ag (agent 5)) (send ag + 10) (await ag) @` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def ag (agent 5)) (send ag + 10) (await ag) @` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G9-11: send and send-off

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 4, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def ag (agent 0)) (send-off ag inc) (await ag` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (def ag (agent 0)) (send-off ag inc) (await ag` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send-off ag inc) (await ag` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send-off ag inc) (await ag` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-12: await — synchronizing on agents

- examples: 1
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'LOW_GROUNDING': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-13: future introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'LOW_GROUNDING': 3, 'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [HIGH_LENGTH] form=`@(future (+ 1 2))` — user_msg 210 words
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`@(future (+ 1 2))` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`@(future (+ 1 2))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`@(future (+ 1 2))` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G9-14: deref @ shorthand

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) (deref a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) (deref a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) (deref a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)

### G9-15: promise — deliver and deref

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 3, 'WRONG_FABLE_LITERAL': 1, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'LOW_GROUNDING': 1, 'ANSWER_LEAK_STRING': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def p (promise)) (deliver p :done) @p)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [WRONG_FABLE_LITERAL] form=`(do (def p (promise)) (deliver p :done) @p)` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (def p (promise)) (deliver p :done) @p)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (def p (promise)) (deliver p :done) @p)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [ANSWER_LEAK_STRING] form=`(do (def p (promise)) (deliver p :done) @p)` — answer string ':done' appears in user_msg
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def p (promise)) (deliver p 42) @p)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G9-16: volatile — when STM is too heavy

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def v (volatile! 5)) (vreset! v 99) @v)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '99'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def v (volatile! 5)) (vreset! v 99) @v)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '99'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def v (volatile! 5)) (vreset! v 99) @v)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '99'), resolution doesn't close the loop)

### G9-17: binding — thread-local

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'HIGH_LENGTH': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg 257 words
    - [HIGH_LENGTH] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg 259 words
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock 42))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def lock (Object.)) (locking lock 42))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock 42))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 10

### G10-01: quote, unquote, unquote-splice

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(quote (+ 1 2))` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(quote (+ 1 2))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 5] `(a ~x b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)

### G10-02: syntax-quote

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'LOW_GROUNDING': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(let [x 10] `(+ ~x ~x))` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(let [x 10] `(+ ~x ~x))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(let [x 10] `(+ ~x ~x))` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(let [x 10] `(+ ~x ~x))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(let [xs [1 2 3]] `(list ~@xs))` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(let [xs [1 2 3]] `(list ~@xs))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G10-03: defmacro introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [HIGH_LENGTH] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg 234 words
    - [LOW_GROUNDING] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G10-04: Macro expansion rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(when true 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(macroexpand-1 '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(when true 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(macroexpand-1 '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(when true 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(macroexpand-1 '(or a b))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-05: macroexpand

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'LOW_GROUNDING': 4}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(macroexpand '(when true 1))` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(macroexpand '(when true 1))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(macroexpand '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(macroexpand '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(macroexpand '(-> 1 inc inc))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(macroexpand '(-> 1 inc inc))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-06: when and when-not as macros

- examples: 3
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 2, 'WRONG_FABLE_LITERAL': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(when-not false :ok)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [WRONG_FABLE_LITERAL] form=`(when-not false :ok)` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [CAP_PRONOUN_MID_SENTENCE] form=`(when-not false :ok)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(when-not false :ok)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(when-not false :ok)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'HIGH_LENGTH': 1}
    - [LOW_GROUNDING] form=`(macroexpand '(-> x f g))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(macroexpand '(-> x f g))` — user_msg 215 words

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
    - [HIGH_LENGTH] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — user_msg 206 words
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
- issues: {'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'LOW_GROUNDING': 5, 'HIGH_LENGTH': 1, 'ANSWER_LEAK': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(#(* % %) 6)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(#(* % %) 6)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(#(* % %) 6)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(#(* % %) 6)` — user_msg 212 words
    - [ANSWER_LEAK] form=`(#(* % %) 6)` — answer 36 in narrative
    - [CAP_PRONOUN_MID_SENTENCE] form=`(#(* % %) 6)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G10-12: Tagged literals

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 5, 'POST_COMMA_CAPITAL_PRONOUN': 5, 'LOW_GROUNDING': 6, 'BOOL_LEAK_RESOLUTION': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(inst? #inst "2024-01-01")` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(inst? #inst "2024-01-01")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(inst? #inst "2024-01-01")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(inst? #inst "2024-01-01")` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(inst? #inst "2024-01-01")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(inst? #inst "2024-01-01")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-13: Data readers and EDN extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(clojure.edn/read-string "42")` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(clojure.edn/read-string "42")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(clojure.edn/read-string "42")` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(clojure.edn/read-string "42")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-14: eval (the function)

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1, 'LOW_GROUNDING': 4, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [ANSWER_LEAK] form=`(eval '(+ 1 2 3))` — answer 6 in narrative
    - [LOW_GROUNDING] form=`(eval '(+ 1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(eval (list '+ 4 5))` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(eval (list '+ 4 5))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(eval (list '+ 4 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval (list '+ 4 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '5'), resolution doesn't close the loop)

### G10-16: Macro pattern library

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':slow',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':slow',), resolution doesn't close the loop)

## Grade 11

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
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [HIGH_LENGTH] form=`(Math/abs -7)` — user_msg 221 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(Math/abs -7)` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(Math/abs -7)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)

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
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(let [a (int-array [1 2 3])] (alength a))` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(let [a (int-array [1 2 3])] (alength a))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G11-08: Type hints

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [^String s "abc"] (.toUpperCase s))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [^String s "abc"] (.toUpperCase s))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(let [^String s "abc"] (.toUpperCase s))` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(let [^String s "abc"] (.toUpperCase s))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [^String s "abc"] (.toUpperCase s))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)

### G11-09: Checked vs unchecked math

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'LOW_GROUNDING': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(+ 1 2)` — ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(+ 1 2)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(+ 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-14: Debugging host leaks

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(try (Math/sqrt 4) (catch Exception _ :err))` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(try (Math/sqrt 4) (catch Exception _ :err))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (Math/sqrt 4) (catch Exception _ :err))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', ':err'), resolution doesn't close the loop)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(try (Math/sqrt 4) (catch Exception _ :err))` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(try (Math/sqrt 4) (catch Exception _ :err))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (Math/sqrt 4) (catch Exception _ :err))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', ':err'), resolution doesn't close the loop)

## Grade 12

### G12-01: Transducers introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'HIGH_LENGTH': 1, 'COLLECTION_LEAK': 1, 'WRONG_FABLE_LITERAL': 1}
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
- issues: {'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1}
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
- issues: {'HIGH_LENGTH': 1, 'COLLECTION_LEAK': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [HIGH_LENGTH] form=`(into #{} (map inc) [1 2 3])` — user_msg 265 words
    - [COLLECTION_LEAK] form=`(into #{} (map inc) [1 2 3])` — elements of expected {2, 3, 4} appear comma-separated in user_msg (collection answer leak)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(into #{} (map inc) [1 2 3])` — ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(into #{} (map inc) [1 2 3])` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (take 3) (range 100))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '100'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (take 3) (range 100))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '100'), resolution doesn't close the loop)

### G12-06: clojure.spec

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 4}
    - [FOREIGN_FABLE_IMAGERY] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose

### G12-17: Library design patterns

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(= [1 2 3] (vec '(1 2 3)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

---

## Summary

### Issue counts (across all examples × 3 records)

- **LOW_GROUNDING**: 330
- **STORY_RESOLUTION_NO_DRAWN**: 307
- **CAP_PRONOUN_MID_SENTENCE**: 177
- **POST_COMMA_CAPITAL_PRONOUN**: 177
- **FOREIGN_FABLE_IMAGERY**: 38
- **HIGH_LENGTH**: 36
- **BOOL_LEAK_RESOLUTION**: 19
- **WRONG_FABLE_LITERAL**: 9
- **CONCEPT_AS_VERB**: 6
- **ANSWER_LEAK_STRING**: 5
- **ANSWER_LEAK**: 3
- **COLLECTION_LEAK**: 2
- **SENTENCE_START_LOWER_PRONOUN**: 1

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 120 | — |
| 2 | 22 | 88 | 124 | — |
| 3 | 18 | 31 | 52 | — |
| 4 | 20 | 39 | 20 | — |
| 5 | 22 | 39 | 22 | — |
| 6 | 16 | 33 | 97 | — |
| 7 | 18 | 36 | 150 | — |
| 8 | 16 | 31 | 191 | — |
| 9 | 18 | 34 | 105 | — |
| 10 | 16 | 36 | 134 | — |
| 11 | 14 | 29 | 66 | — |
| 12 | 18 | 37 | 29 | — |

### Sample issues by severity

#### LOW_GROUNDING

- `G1-01` (form `0`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    Champ had found the bone at the edge of the meadow and was carrying it home with no small amount of pride.

Halfway through the race, Crumpet the dog stopped near the meadow and refused to
continue until someone could prove what the form `0`
evaluated to. Crumpet called it impossible.
Champ the dog,...
    ```
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
- `G1-02` (form `0`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    It was an afternoon of quiet sky and steady current, and the world below the surface seemed almost solid.

Halfway through the race, Zippy the dog stopped near the village and refused to
continue until someone could prove what the form `0`
evaluated to. Zippy called it impossible.
Springer the dog, ...
    ```
- `G1-03` (form `1/2`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    in the forest, the stream ran clear enough to mirror anything that passed above it, and Leo passed above it.

Leo the dog had been keeping a small leather notebook of every
form he had successfully evaluated. Today at the edge of the forest, the
next entry was the ratio 1/2. Shepherd the dog peered ...
    ```

#### FOREIGN_FABLE_IMAGERY

- `G1-01` (form `0`): tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose
    ```
    The bridge had stood there as long as anyone remembered, and so had the temptation it offered to anyone crossing with full jaws.

At a moss-covered milestone in the pond, Watchdog the dog sketched a small
wager into the path: whoever guessed the result of `0`
first would win the right to set the nex...
    ```
- `G1-01` (form `nil`): tortoise-hare-specific imagery 'small audience of forest creatures' leaks into dog-shadow prose
    ```
    A reflection is a strange kind of promise: present and unreachable, and very hard to argue with.

A small audience of forest creatures had gathered by the pond to watch
Steel the dog attempt to outwit Yappy the dog at reading the REPL.
Yappy pointed to the literal nil and read out the form aloud:
`n...
    ```
- `G1-02` (form `7`): tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into dog-shadow prose
    ```
    Some lessons are taught by mirrors, and some are taught by rivers; this one was taught by both at once.

A wooden sign nailed to a tree near the forest carried a puzzle. The riddle
was simple: it asked the reader to evaluate `7`. Henry
laughed, his step bouncing with self-regard, and declared it too...
    ```
- `G1-02` (form `7`): tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into dog-shadow prose
    ```
    Diesel had crossed this bridge a hundred times on the beach, but never with so fine a bone clamped in his jaws.

A wooden sign nailed to a tree by the beach carried a puzzle. The riddle
was simple: it asked the reader to evaluate `7`. Sooty
laughed, stepping high, as proud creatures step, and declar...
    ```
- `G1-02` (form `7`): tortoise-hare-specific imagery 'moss-covered milestone' leaks into dog-shadow prose
    ```
    Saffron had carried his prize all the way from the village, and in the forest the bridge offered him an unwelcome second look.

At a moss-covered milestone by the forest, Herder the dog sketched a small
wager into the path: whoever guessed the result of `7`
first would win the right to set the next ...
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
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    ```
    Tracker had found the bone near the pond and was carrying it home with no small amount of pride.

Tracker the dog pointed at a name scratched into the bark by the pond,
then at an actual bone lying on the path. "The mark on the bark
is the *name*; the bone is the *value*. They are not the same
thing...
    ```
- `G1-09` (form `(symbol? 42)`): ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    ```
    It was on the beach, on the wooden bridge above the slow brook, that Whiff the dog looked down at the water.

"There's a difference between *labeling* the form and
*evaluating* it," Whiff the dog said. "Quote in any of its
shapes is the labeling — the runtime hands you back the form,
not its value, ...
    ```
- `G1-09` (form `(= 'hare 'hare)`): ',
She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    ```
    On a path that ran beside the stream, a dog was carrying his supper home and looking pleased with himself.

Oscar the dog pointed at a name scratched into the bark near the beach,
then at an actual bone lying on the path. "The mark on the bark
is the *name*; the bone is the *value*. They are not the...
    ```
- `G1-09` (form `(= 'hare 'hare)`): ',
He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    ```
    Chester the dog was nearly home near the road when the water below showed him a second bone that did not exist.

"There's a difference between *labeling* the form and
*evaluating* it," Chester the dog said. "Quote in any of its
shapes is the labeling — the runtime hands you back the form,
not its va...
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
    Tracker had found the bone near the pond and was carrying it home with no small amount of pride.

Tracker the dog pointed at a name scratched into the bark by the pond,
then at an actual bone lying on the path. "The mark on the bark
is the *name*; the bone is the *value*. They are not the same
thing...
    ```
- `G1-09` (form `(symbol? 42)`): capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    ```
    It was on the beach, on the wooden bridge above the slow brook, that Whiff the dog looked down at the water.

"There's a difference between *labeling* the form and
*evaluating* it," Whiff the dog said. "Quote in any of its
shapes is the labeling — the runtime hands you back the form,
not its value, ...
    ```
- `G1-09` (form `(= 'hare 'hare)`): capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    ```
    On a path that ran beside the stream, a dog was carrying his supper home and looking pleased with himself.

Oscar the dog pointed at a name scratched into the bark near the beach,
then at an actual bone lying on the path. "The mark on the bark
is the *name*; the bone is the *value*. They are not the...
    ```
- `G1-09` (form `(= 'hare 'hare)`): capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    ```
    Chester the dog was nearly home near the road when the water below showed him a second bone that did not exist.

"There's a difference between *labeling* the form and
*evaluating* it," Chester the dog said. "Quote in any of its
shapes is the labeling — the runtime hands you back the form,
not its va...
    ```

#### STORY_RESOLUTION_NO_DRAWN

- `G1-09` (form `(symbol? 42)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)
    ```
    Tracker had found the bone near the pond and was carrying it home with no small amount of pride.

Tracker the dog pointed at a name scratched into the bark by the pond,
then at an actual bone lying on the path. "The mark on the bark
is the *name*; the bone is the *value*. They are not the same
thing...
    ```
- `G1-09` (form `(symbol? 42)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)
    ```
    It was on the beach, on the wooden bridge above the slow brook, that Whiff the dog looked down at the water.

"There's a difference between *labeling* the form and
*evaluating* it," Whiff the dog said. "Quote in any of its
shapes is the labeling — the runtime hands you back the form,
not its value, ...
    ```
- `G1-12` (form `(+ 2 3)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    ```
    Some greedy creatures lose what they have to a thief; others lose it to themselves, by way of a careless glance.

Snort the dog, as one who would weigh his neighbour's loaf, glanced at the form and called out
what he thought it would do without paying attention
to the conventions of how it was scrat...
    ```
- `G1-13` (form `(- 5 3)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '3'), resolution doesn't close the loop)
    ```
    Some lessons are taught by mirrors, and some are taught by rivers; this one was taught by both at once.

"Whatever the pile looks like after the operation,"
Saffron the dog said, "the runtime gives the exact count — small
or large, fraction or whole, the answer is precise." To
subtract 3 from 5, he ...
    ```
- `G1-13` (form `(- 5 3)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '3'), resolution doesn't close the loop)
    ```
    in the pond, where the path crosses the stream, Sterling the dog trotted home with a fine bone in his teeth.

Sterling the dog laid bones out on a flat stone near the pond, sorting
them into small piles. "Numbers in Clojure are just like bones
in piles," he said: "you can count them, you can
add two...
    ```

#### HIGH_LENGTH

- `G1-09` (form `(= 'hare 'hare)`): user_msg 208 words
    ```
    in the meadow, where the boards of the bridge meet the stones of the path, Jack the dog caught sight of himself in the stream.

Rex the hound laid two scratch-marks side by side on bark near the forest. Both marks said the same thing: hare, hare. "Are these two scratches the same name?" Rex asked. "...
    ```
- `G2-18` (form `(symbol? (quote hare))`): user_msg 201 words
    ```
    There was once a dog who carried a fine bone home along a path that crossed a stream by an old wooden bridge.

Patch the hound found a bone scratch on bark at the stream's edge that read hare. They wondered — was this mark the same as the animal, or just a name-mark that stood for it?

They needed t...
    ```
- `G3-03` (form `(let [n 10] (* n n))`): user_msg 246 words
    ```
    Down by the stream where the bank dipped low, the world above was answered politely by the world below.

Rex the hound found ten smooth stones near the forest and gathered them into a tight mouthful. "I hold this count only for one stretch — while I carry these stones from bank to bank," he said, hi...
    ```
- `G3-03` (form `(let [n 10] (* n n))`): user_msg 251 words
    ```
    It is one of the oldest tricks of light to make one bone seem like two and to make a fool of the unwary.

Rex the hound found ten smooth stones near the forest and gathered them into a tight mouthful. "I hold this count only for one stretch — while I carry these stones from bank to bank," he said, h...
    ```
- `G3-06` (form `(let [a 5 b (* a 2)] b)`): user_msg 262 words
    ```
    It was an afternoon of quiet sky and steady current, and the world below the surface seemed almost solid.

Rex the hound gathered five bones and clamped them in his jaws as the name a. Before stepping forward, he computed in his mind what twice that grip would weigh — and held both the first grip an...
    ```

#### BOOL_LEAK_RESOLUTION

- `G1-09` (form `(= 'hare 'hare)`): resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    ```
    in the meadow, where the boards of the bridge meet the stones of the path, Jack the dog caught sight of himself in the stream.

Rex the hound laid two scratch-marks side by side on bark near the forest. Both marks said the same thing: hare, hare. "Are these two scratches the same name?" Rex asked. "...
    ```
- `G1-15` (form `(= 1 1 1 1)`): resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    ```
    It happened on a day so ordinary that it seemed impossible anything could have been lost.

Bell the hound laid four pebbles in a row at the stream's edge, each marked with the number one. "Are all four of these pebbles the same?" she asked. "The runtime can check them all at once."

She wanted the R...
    ```
- `G1-16` (form `(pos? -2)`): resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    ```
    Hunter the dog was nearly home near the forest when the water below showed him a second bone that did not exist.

Patch the hound held a negative number on bark near the forest and asked: "Is this count moving forward from the marker stone?" "Let the runtime check," someone said.

Patch wanted the R...
    ```
- `G1-16` (form `(neg? -3)`): resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    ```
    Herder had found the bone on the road and was carrying it home with no small amount of pride.

Bell the hound marked a negative number on flat bark at the pond and asked: "Is this count moving backward from the starting point?" "The runtime can check," her packmate said.

She wanted the REPL to test...
    ```
- `G1-16` (form `(neg? 4)`): resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    ```
    There is a kind of greed that does not see what it already has, and another kind that mistakes a reflection for a meal.

Rex the hound scratched the number four on bark near the river and asked: "Is this count moving backward?" "Let the runtime tell," said Patch.

He wanted the REPL to test the numb...
    ```

#### SENTENCE_START_LOWER_PRONOUN

- `G1-15` (form `(= 1 1 1 1)`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    It happened on a day so ordinary that it seemed impossible anything could have been lost.

Bell the hound laid four pebbles in a row at the stream's edge, each marked with the number one. "Are all four of these pebbles the same?" she asked. "The runtime can check them all at once."

She wanted the R...
    ```

#### WRONG_FABLE_LITERAL

- `G2-10` (form `(* 2 2 2)`): tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    ```
    near the road, where the path crosses the stream, Pip the dog trotted home with a fine bone in his teeth.

Pip the dog arranged a small heap of bones along the road, careful
with the count. "Numbers in Clojure don't fudge,"
he said. "Whatever you do — adding, subtracting,
dividing into piles with le...
    ```
- `G5-15` (form `((comp inc inc) 5)`): tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    ```
    near the road, where the path crosses the stream, Pip the dog trotted home with a fine bone in his teeth.

"On any nose-trail," Pip the dog explained, "the last sniff
is what you carry home." He took the goal — to
compose two inc functions and apply them to 5 — and laid out the routine's paw-steps i...
    ```
- `G6-01` (form `(name 'clojure.string)`): tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    ```
    Some lessons are taught by mirrors, and some are taught by rivers; this one was taught by both at once.

Bear the dog, his thoughts running on doubling and tripling, glanced at the marker stone near the road
and called out what he thought it said without slowing.
Pip the dog stopped and read careful...
    ```
- `G6-15` (form `(:doc (meta '\{:doc "steady wins"\} race))`): tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    ```
    near the road, where the path crosses the stream, Pip the dog trotted home with a fine bone in his teeth.

"The world outside the REPL is bigger than the REPL,"
Pip the dog said, "and a message-bone out there has its own
discipline — pick it up carefully, handle it with care, set it
back when you're...
    ```
- `G7-15` (form `(with-out-str (print "x"))`): tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    ```
    near the road, where the path crosses the stream, Pip the dog trotted home with a fine bone in his teeth.

"The world outside the REPL is bigger than the REPL,"
Pip the dog said, "and a message-bone out there has its own
discipline — pick it up carefully, handle it with care, set it
back when you're...
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

#### ANSWER_LEAK

- `G5-15` (form `((comp inc inc) 5)`): answer 7 in narrative
    ```
    It was an afternoon of quiet sky and steady current, and the world below the surface seemed almost solid.

Patch the hound laid down two nose-trails end to end by the river bank. The first trail was inc, the second trail was inc again. She would chain them together, so what the first trail turned up...
    ```
- `G10-11` (form `(#(* % %) 6)`): answer 36 in narrative
    ```
    by the pond, where the path crosses the stream, Ace the dog trotted home with a fine bone in his teeth.

Bell the hound found a shorthand reading-mark on bark: #(* % %). This was the scribe's way of saying "make a quick function where %  is the argument." The function would take 6 and square it. No ...
    ```
- `G10-14` (form `(eval '(+ 1 2 3))`): answer 6 in narrative
    ```
    The stream ran clear that afternoon, and the bridge cast a long trembling shadow across the water.

Bell the hound had a quoted form scratched on bark: (+ 1 2 3). The quote kept it as a form, not evaluated. But she wanted to ask the runtime to evaluate it later — not at read-time, but when she calle...
    ```

#### ANSWER_LEAK_STRING

- `G6-01` (form `(name 'foo.bar)`): answer string 'foo.bar' appears in user_msg
    ```
    There is a kind of greed that does not see what it already has, and another kind that mistakes a reflection for a meal.

Patch the hound examined a marker stone at the stream's edge with a strange dotted path scratched into it — foo.bar. {hound_he_she} wanted to read what the scratch said without us...
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
- `G9-15` (form `(do (def p (promise)) (deliver p :done) @p)`): answer string ':done' appears in user_msg
    ```
    It was an afternoon of quiet sky and steady current, and the world below the surface seemed almost solid.

Bell sent a scout-dog with a task. She created a promise — an empty satchel for the scout's answer.

The scout would race ahead, do the work, then deliver the answer to the promise. Bell would ...
    ```

#### COLLECTION_LEAK

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

