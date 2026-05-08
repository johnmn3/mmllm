# milkmaid curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

### G1-01: Eval as substitution

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'FOREIGN_FABLE_IMAGERY': 4}
    - [LOW_GROUNDING] form=`0` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`0` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`0` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`0` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`nil` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`nil` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose

### G1-02: Integer numbers

- examples: 6
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 5, 'LOW_GROUNDING': 3}
    - [FOREIGN_FABLE_IMAGERY] form=`7` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`-3` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`0` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`0` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`0` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`0` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into milkmaid prose

### G1-03: Ratios

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'FOREIGN_FABLE_IMAGERY': 6}
    - [LOW_GROUNDING] form=`1/2` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`1/2` — tortoise-hare-specific imagery 'leather notebook' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`1/2` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`1/2` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`3/4` — tortoise-hare-specific imagery 'leather notebook' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`(+ 1/2 1/4)` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose

### G1-05: Booleans

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 10, 'FOREIGN_FABLE_IMAGERY': 5}
    - [LOW_GROUNDING] form=`true` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`true` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`true` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`false` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`false` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`false` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-06: nil

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 12, 'FOREIGN_FABLE_IMAGERY': 8}
    - [LOW_GROUNDING] form=`nil` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`nil` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`nil` — tortoise-hare-specific imagery 'moss-covered milestone' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`(nil? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(nil? nil)` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`(nil? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-07: Keywords

- examples: 5
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(keyword? :hare)` — tortoise-hare-specific imagery 'leather notebook' leaks into milkmaid prose

### G1-09: Symbols vs values

- examples: 4
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 5, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(symbol? 'hare)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(symbol? 'hare)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 'hare 'hare)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 'hare 'hare)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(= 'hare 'hare)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(= 'hare 'hare)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G1-13: First arithmetic call

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(+ 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-15: Equality

- examples: 6
- variety @ n=50: 1.00
- issues: {'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 8}
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(= 1 1)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-16: Numeric predicates

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'CAP_PRONOUN_MID_SENTENCE': 5, 'POST_COMMA_CAPITAL_PRONOUN': 5}
    - [LOW_GROUNDING] form=`(zero? 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(zero? 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(zero? 5)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(zero? 5)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(pos? 7)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(pos? 7)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G1-17: Printing vs returning

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(+ 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(+ 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-18: Errors are safe in the REPL

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(+ 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 2

### G2-02: Comparison chains

- examples: 5
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 2}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(< 3 2 1)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(< 3 2 1)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(<= 1 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(<= 1 1 2)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(<= 1 1 2)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(<= 1 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-03: not= and = with multiple args

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 7}
    - [LOW_GROUNDING] form=`(not= 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not= 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not= 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 1 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-06: inc and dec

- examples: 5
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 3, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'LOW_GROUNDING': 3}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(inc 5)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(inc 5)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(dec 5)` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(dec 5)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(inc 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(inc 0)` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G2-07: Absolute value

- examples: 4
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 4}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(abs 5)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(abs 5)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(abs -5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(abs 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(abs 0)` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(abs 0)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G2-08: Arithmetic on ratios

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 8}
    - [LOW_GROUNDING] form=`(+ 1/2 1/4)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(+ 1/2 1/4)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(+ 1/2 1/4)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(* 2/3 3/4)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(* 2/3 3/4)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(- 1 1/3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-09: Floats vs ints (the / operator)

- examples: 3
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 2}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(/ 10 2)` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(/ 10 2)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(/ 1.0 2)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(/ 1.0 2)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(/ 1.0 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(/ 1.0 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-10: Powers via repeated multiplication

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'ANSWER_LEAK': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(* 2 2 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(* 2 2 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(* 2 2 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [ANSWER_LEAK] form=`(* 3 3 3 3)` — answer 81 in narrative
    - [CAP_PRONOUN_MID_SENTENCE] form=`(* 3 3 3 3)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(* 3 3 3 3)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G2-11: String concatenation with str

- examples: 4
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(str 42)` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(str 42)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(str 42)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(str 42)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G2-13: and / or — short circuit, return values

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 12, 'POST_COMMA_CAPITAL_PRONOUN': 5, 'CAP_PRONOUN_MID_SENTENCE': 1, 'BOOL_LEAK_RESOLUTION': 1}
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(and true true)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(and true false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(and true false)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G2-14: not — turning truthy to false

- examples: 5
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 12, 'POST_COMMA_CAPITAL_PRONOUN': 3, 'CAP_PRONOUN_MID_SENTENCE': 2, 'BOOL_LEAK_RESOLUTION': 2}
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(not true)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-15: Falsey values: only false and nil

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(if nil 1 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(if nil 1 0)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(if nil 1 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(if false 1 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-16: Truthy 0 and empty string

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 9, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(boolean 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(boolean 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(boolean 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(boolean nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(boolean nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(boolean nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-18: Quoting symbols

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'BOOL_LEAK_RESOLUTION': 1}
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= (quote tortoise) 'tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(= (quote tortoise) 'tortoise)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(= (quote tortoise) 'tortoise)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G2-19: Auto-promotion to bigint

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(* 1000000 1000000)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(* 1000000 1000000)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 3

### G3-03: let — local binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(let [n 10] (* n n))` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(let [n 10] (* n n))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(let [a 5] a)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(let [a 5] a)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G3-04: let — multi-binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(let [a 1 b 2] (+ a b))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [a 1 b 2] (+ a b))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [a 1 b 2] (+ a b))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [HIGH_LENGTH] form=`(#(+ % 1) 5)` — user_msg 221 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(#(+ % 1) 5)` — ', He wrote…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(#(+ % 1) 5)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [HIGH_LENGTH] form=`(#(* %1 %2) 3 4)` — user_msg 201 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(#(* %1 %2) 3 4)` — ', He wrote…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(#(* %1 %2) 3 4)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G3-13: fn body returns last form

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`((fn [x] x x x 99) 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`((fn [x] x x x 99) 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`((fn [x] x x x 99) 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G3-16: Name collision: namespace vs let

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(let [+ 99] +)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 4

### G4-01: Vector literal

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'FORM_LEAK': 2, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [LOW_GROUNDING] form=`["a" "b"]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_LEAK] form=`["a" "b"]` — form '["a" "b"]' appears in user_msg of a goal-style subject
    - [CAP_PRONOUN_MID_SENTENCE] form=`["a" "b"]` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`["a" "b"]` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`["a" "b"]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_LEAK] form=`["a" "b"]` — form '["a" "b"]' appears in user_msg of a goal-style subject

### G4-11: Set literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'HIGH_LENGTH': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(count #{1 1 1})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count #{1 1 1})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(count #{1 1 1})` — user_msg 204 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(count #{1 1 1})` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(count #{1 1 1})` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(count #{1 1 1})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-16: into and conj on collections

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'FORM_LEAK': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(into #{} [1 2 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(into #{} [1 2 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_LEAK] form=`(into #{} [1 2 2 3])` — form '(into #{} [1 2 2 3])' appears in user_msg of a goal-style subject
    - [CAP_PRONOUN_MID_SENTENCE] form=`(into #{} [1 2 2 3])` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(into #{} [1 2 2 3])` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G4-19: range and seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(count (range 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count (range 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count (range 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 5

### G5-08: not

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(not (> 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not (> 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(not (> 1 2))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(not (> 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G5-09: fn as value

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`((fn [f x] (f (f x))) inc 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G5-10: map

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [HIGH_LENGTH] form=`(map #(* % %) [1 2 3 4])` — user_msg 201 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(map #(* % %) [1 2 3 4])` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(map #(* % %) [1 2 3 4])` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G5-22: recur — first taste

- examples: 1
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [HIGH_LENGTH] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — user_msg 205 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

## Grade 6

### G6-01: Namespace as file

- examples: 3
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 9, 'CAP_PRONOUN_MID_SENTENCE': 4, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'CONCEPT_AS_VERB': 1}
    - [LOW_GROUNDING] form=`(name 'foo.bar)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(name 'foo.bar)` — ', He brought…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [LOW_GROUNDING] form=`(name 'foo.bar)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(name 'foo.bar)` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(name 'foo.bar)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(name 'foo.bar)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-02: ns form

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(name 'race.tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(name 'race.tortoise)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(name 'race.tortoise)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(name 'race.tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name 'race.tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 'race.tortoise 'race.tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-05: Fully qualified names

- examples: 4
- variety @ n=50: 0.99
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'CONCEPT_AS_VERB': 2, 'LOW_GROUNDING': 3}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(clojure.string/reverse "abc")` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(clojure.string/reverse "abc")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CONCEPT_AS_VERB] form=`(clojure.string/reverse "abc")` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(name :owner/item)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name :owner/item)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(name :owner/item)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G6-06: Private defs

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 2}
    - [CONCEPT_AS_VERB] form=`(:private (meta 'x))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(:private (meta 'x))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G6-07: Public vs private API

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 3, 'CONCEPT_AS_VERB': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(boolean (:private (meta '^:private hidden)))` — ', He brought…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(boolean (:private (meta '^:private hidden)))` — ', She brought…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [CAP_PRONOUN_MID_SENTENCE] form=`(boolean (:private (meta '^:private hidden)))` — ', She brought…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [CONCEPT_AS_VERB] form=`(boolean (:private (meta 'public)))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G6-08: Circular dependencies

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(= 'a.b 'a.b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 'a.b 'a.b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 'a.b 'a.b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-09: Loading order

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'CAP_PRONOUN_MID_SENTENCE': 2}
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — ', He brought…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — ', She brought…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [a 1 b (+ a 1)] (+ a b))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-10: Leiningen and deps.edn

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`(get-in {:paths ["src"]} [:paths 0])` — tortoise-hare-specific imagery 'leather notebook' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`(get-in {:paths ["src"]} [:paths 0])` — tortoise-hare-specific imagery 'leather notebook' leaks into milkmaid prose

### G6-11: Classpath

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(clojure.string/split "src:test" #":")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.string/split "src:test" #":")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.string/split "src:test" #":")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count ["src" "test" "resources"])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count ["src" "test" "resources"])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-12: Multiple files in one project

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(count ['race.tortoise 'race.hare 'race.shared])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(count ['race.tortoise 'race.hare 'race.shared])` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(count ['race.tortoise 'race.hare 'race.shared])` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(count ['race.tortoise 'race.hare 'race.shared])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(count ['race.tortoise 'race.hare 'race.shared])` — ', She brought…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [LOW_GROUNDING] form=`(count ['race.tortoise 'race.hare 'race.shared])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-14: Import for host classes

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'CONCEPT_AS_VERB': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(symbol? 'java.util.List)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(symbol? 'java.util.List)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(symbol? 'java.util.List)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name 'java.util.Map)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(name 'java.util.Map)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(name 'java.util.Map)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-15: Namespace meta

- examples: 2
- variety @ n=50: 0.99
- issues: {'CONCEPT_AS_VERB': 2}
    - [CONCEPT_AS_VERB] form=`(:doc (meta '\{:doc "steady wins"\} race))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(:doc (meta '\{:doc "steady wins"\} race))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G6-16: Cleaning up requires

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'LOW_GROUNDING': 6}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(contains? #{'clojure.string} 'clojure.string)` — ', She brought…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.string)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.string)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.string)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.set)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.set)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 7

### G7-01: throw

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(try (throw (Exception. "bad")) (catch Exception e` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try (throw (Exception. "bad")) (catch Exception e` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(try (throw (Exception. "bad")) (catch Exception e` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(try (throw (Exception. "bad")) (catch Exception e` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(try (throw (Exception. "bad")) (catch Exception e` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-03: try / finally

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6}
    - [LOW_GROUNDING] form=`(try 7 (finally (prn :cleanup)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try 7 (finally (prn :cleanup)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try 7 (finally (prn :cleanup)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try (try (/ 1 0) (finally (prn :ran))) (catch Exc` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try (try (/ 1 0) (finally (prn :ran))) (catch Exc` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try (try (/ 1 0) (finally (prn :ran))) (catch Exc` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-04: ex-info

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 5, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [LOW_GROUNDING] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(try (throw (ex-info "x" {:k :v})) (catch Exceptio` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G7-05: nil punning

- examples: 4
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'BOOL_LEAK_RESOLUTION': 2, 'LOW_GROUNDING': 12, 'LOWERCASE_CONCEPT_AFTER_PERIOD': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(some? nil)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(some? nil)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [BOOL_LEAK_RESOLUTION] form=`(some? nil)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(some? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(some? nil)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(some? nil)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G7-06: pre and post conditions

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 6, 'LOWERCASE_CONCEPT_AFTER_PERIOD': 2}
    - [LOW_GROUNDING] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exce` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exce` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    - [LOW_GROUNDING] form=`(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exce` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-07: assert

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(do (assert (= 1 1)) 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (assert (= 1 1)) 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (assert (= 1 1)) 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-09: tap>

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(tap> :hello)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(tap> :hello)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(tap> 42)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(tap> 42)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(tap> 42)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-10: doc and source

- examples: 1
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [ANSWER_LEAK_STRING] form=`(:doc (meta '^{:doc "adds two"} plus))` — answer string 'adds two' appears in user_msg
    - [CAP_PRONOUN_MID_SENTENCE] form=`(:doc (meta '^{:doc "adds two"} plus))` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(:doc (meta '^{:doc "adds two"} plus))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G7-11: Reading stack traces

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6}
    - [LOW_GROUNDING] form=`(try (throw (Exception. "oops")) (catch Exception ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try (throw (Exception. "oops")) (catch Exception ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try (throw (Exception. "oops")) (catch Exception ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try (throw (ex-info "trouble" {})) (catch Excepti` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try (throw (ex-info "trouble" {})) (catch Excepti` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try (throw (ex-info "trouble" {})) (catch Excepti` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-12: slurp and spit

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(clojure.string/split "a\nb\nc" #"\n")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.string/split "a\nb\nc" #"\n")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.string/split "a\nb\nc" #"\n")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-13: line-seq

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 6}
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(first (clojure.string/split-lines "morning-delive` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(first (clojure.string/split-lines "morning-delive` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(first (clojure.string/split-lines "morning-delive` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

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
- issues: {'LOW_GROUNDING': 9}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "{:a 1}")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "{:a 1}")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "{:a 1}")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-17: JSON roundtrip

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 8

### G8-01: Why polymorphism

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G8-02: deftype introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'HIGH_LENGTH': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — user_msg 204 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-03: defrecord introduction

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(do (defrecord Runner [name pace]) (:name (->Runne` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defrecord Runner [name pace]) (:name (->Runne` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defrecord Runner [name pace]) (:name (->Runne` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-04: Protocol definition

- examples: 2
- variety @ n=50: 0.98
- issues: {'LOW_GROUNDING': 6, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol Greet (hail [this])) (some? Greet` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G8-05: Protocol extension

- examples: 2
- variety @ n=50: 0.98
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 6, 'CONCEPT_AS_VERB': 3}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-06: Protocol method dispatch

- examples: 2
- variety @ n=50: 0.98
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-07: Record implementing protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'CONCEPT_AS_VERB': 2}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (defrecord M` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (defrecord M` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (defrecord M` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(do (defprotocol Pace (speed [this])) (defrecord F` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (defrecord F` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(do (defprotocol Pace (speed [this])) (defrecord F` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G8-10: Multimethod vs protocol

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 2, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 3}
    - [HIGH_LENGTH] form=`(do (defmulti show identity) (defmethod show :rabb` — user_msg 216 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defmulti show identity) (defmethod show :rabb` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defmulti show identity) (defmethod show :rabb` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (defprotocol Show (show [this])) (extend-proto` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Show (show [this])) (extend-proto` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(do (defprotocol Show (show [this])) (extend-proto` — user_msg 223 words

### G8-11: Protocol vs Java interface

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CONCEPT_AS_VERB': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol IPace (run [this])) (extend-proto` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol IPace (run [this])) (extend-proto` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(do (defprotocol IPace (run [this])) (extend-proto` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(do (defprotocol IPace (run [this])) (extend-proto` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-12: extend-type on built-in types

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 6, 'HIGH_LENGTH': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-type` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(do (defprotocol Pace (speed [this])) (extend-type` — user_msg 217 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defprotocol Pace (speed [this])) (extend-type` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defprotocol Pace (speed [this])) (extend-type` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-type` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-type` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-13: this-style vs fn-style

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 6}
    - [LOW_GROUNDING] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Tagged (tag-of [this])) (defrecor` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Tagged (tag-of [this])) (defrecor` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Tagged (tag-of [this])) (defrecor` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-14: Protocols don't inherit

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-15: derive and isa? — multimethod hierarchy

- examples: 3
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 6, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [LOW_GROUNDING] form=`(isa? java.lang.Long java.lang.Number)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(isa? java.lang.Long java.lang.Number)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(isa? java.lang.Long java.lang.Number)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(isa? java.lang.String java.lang.Number)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(isa? java.lang.String java.lang.Number)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(isa? java.lang.String java.lang.Number)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-16: Abstract design with protocols

- examples: 2
- variety @ n=50: 0.98
- issues: {'LOW_GROUNDING': 6, 'CONCEPT_AS_VERB': 4}
    - [LOW_GROUNDING] form=`(do (defprotocol Move (step [this])) (defrecord Mi` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Move (step [this])) (defrecord Mi` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(do (defprotocol Move (step [this])) (defrecord Mi` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(do (defprotocol Move (step [this])) (defrecord Mi` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(do (defprotocol Sound (cry [this])) (defrecord Mi` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(do (defprotocol Sound (cry [this])) (defrecord Mi` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 9

### G9-02: Why state at all

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'SMALL_INT_LEAK': 1, 'LOW_GROUNDING': 5}
    - [HIGH_LENGTH] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — user_msg 206 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [SMALL_INT_LEAK] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — small-int answer 1 leaks via resolution-slot phrasing
    - [LOW_GROUNDING] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-03: Atom introduction

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom :start)) (reset! a :done) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom :start)) (reset! a :done) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom :start)) (reset! a :done) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-04: Atom CAS semantics

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def a (atom 5)) (compare-and-set! a 0 99) @a)` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)

### G9-05: Watch on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 3}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-06: Validator on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-07: Ref introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-08: dosync and alter

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-09: Ref vs atom

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-10: Agent introduction

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 3, 'HIGH_LENGTH': 2, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg 213 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-11: send and send-off

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send-off ag inc) (await ag` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send-off ag inc) (await ag` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send-off ag inc) (await ag` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-12: await — synchronizing on agents

- examples: 1
- variety @ n=50: 0.96
- issues: {'LOW_GROUNDING': 3, 'HIGH_LENGTH': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — user_msg 201 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-13: future introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-14: deref @ shorthand

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def a (atom 7)) (deref a))` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (def a (atom 7)) (deref a))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G9-15: promise — deliver and deref

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(do (def p (promise)) (deliver p :done) @p)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def p (promise)) (deliver p :done) @p)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def p (promise)) (deliver p :done) @p)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-16: volatile — when STM is too heavy

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-17: binding — thread-local

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 0.98
- issues: {'LOW_GROUNDING': 6, 'HIGH_LENGTH': 1, 'DOUBLE_PREP': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock 42))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(do (def lock (Object.)) (locking lock 42))` — user_msg 203 words
    - [DOUBLE_PREP] form=`(do (def lock (Object.)) (locking lock 42))` — verb+preposition followed by {place} which already carries its own preposition

## Grade 10

### G10-01: quote, unquote, unquote-splice

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'HIGH_LENGTH': 1}
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(quote (+ 1 2))` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(quote (+ 1 2))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(let [x 5] `(a ~x b))` — user_msg 207 words

### G10-02: syntax-quote

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'LOW_GROUNDING': 3}
    - [HIGH_LENGTH] form=`(let [x 10] `(+ ~x ~x))` — user_msg 205 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(let [x 10] `(+ ~x ~x))` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(let [x 10] `(+ ~x ~x))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(let [xs [1 2 3]] `(list ~@xs))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [xs [1 2 3]] `(list ~@xs))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [xs [1 2 3]] `(list ~@xs))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-03: defmacro introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6}
    - [LOW_GROUNDING] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-04: Macro expansion rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [LOW_GROUNDING] form=`(macroexpand-1 '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(macroexpand-1 '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(macroexpand-1 '(when true 1))` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(macroexpand-1 '(when true 1))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(macroexpand-1 '(or a b))` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(macroexpand-1 '(or a b))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G10-05: macroexpand

- examples: 2
- variety @ n=50: 0.99
- issues: {'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2, 'LOW_GROUNDING': 6}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(macroexpand '(when true 1))` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(macroexpand '(when true 1))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(macroexpand '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(macroexpand '(when true 1))` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(macroexpand '(when true 1))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(macroexpand '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-06: when and when-not as macros

- examples: 3
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'LOW_GROUNDING': 3}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(when-not false :ok)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(when-not false :ok)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(when-not false :ok)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(when-not false :ok)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(when-not false :ok)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1, 'LOW_GROUNDING': 3}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(macroexpand '(-> x f g))` — ', He wrote…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(macroexpand '(-> x f g))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(macroexpand '(-> x f g))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(macroexpand '(-> x f g))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(macroexpand '(-> x f g))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-08: Macro vs fn

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 2}
    - [CONCEPT_AS_VERB] form=`(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G10-09: Hygiene and gensym

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6}
    - [LOW_GROUNDING] form=`(symbol? (gensym))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(symbol? (gensym))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(symbol? (gensym))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-10: Anaphoric macros are confusing

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 1, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [HIGH_LENGTH] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — user_msg 209 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(if-let [x 7] (* x x) 0)` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(if-let [x 7] (* x x) 0)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G10-11: Reader macros overview

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'CAP_PRONOUN_MID_SENTENCE': 2, 'POST_COMMA_CAPITAL_PRONOUN': 2}
    - [LOW_GROUNDING] form=`(#(* % %) 6)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(#(* % %) 6)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(#(* % %) 6)` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(#(* % %) 6)` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(#(* % %) 6)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`[1 #_ 2 3]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-12: Tagged literals

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(inst? #inst "2024-01-01")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CAP_PRONOUN_MID_SENTENCE] form=`(inst? #inst "2024-01-01")` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(inst? #inst "2024-01-01")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    - [LOW_GROUNDING] form=`(inst? #inst "2024-01-01")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(inst? #inst "2024-01-01")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(uuid? #uuid "00000000-0000-0000-0000-000000000000` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-13: Data readers and EDN extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "[:a :b :c]")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "[:a :b :c]")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "[:a :b :c]")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-14: eval (the function)

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'CONCEPT_AS_VERB': 2, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(eval '(+ 1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(eval '(+ 1 2 3))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(eval '(+ 1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(eval '(+ 1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(eval (list '+ 4 5))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(eval (list '+ 4 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-16: Macro pattern library

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 5, 'HIGH_LENGTH': 2}
    - [LOW_GROUNDING] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — user_msg 202 words
    - [LOW_GROUNDING] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — user_msg 202 words

## Grade 11

### G11-02: Method call syntax

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [HIGH_LENGTH] form=`(.toUpperCase "abc")` — user_msg 208 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(.toUpperCase "abc")` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(.toUpperCase "abc")` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G11-06: new and dot-construct

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'CONCEPT_AS_VERB': 4}
    - [LOW_GROUNDING] form=`(String. "go")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(String. "go")` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(String. "go")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(String. "go")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(new String "leap")` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(new String "leap")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-07: Arrays

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CONCEPT_AS_VERB': 2}
    - [LOW_GROUNDING] form=`(let [a (int-array [10 20 30])] (aget a 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [a (int-array [10 20 30])] (aget a 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [a (int-array [10 20 30])] (aget a 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(let [a (int-array [1 2 3])] (alength a))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(let [a (int-array [1 2 3])] (alength a))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G11-08: Type hints

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 3, 'LOW_GROUNDING': 3}
    - [CONCEPT_AS_VERB] form=`(let [^String s "abc"] (.toUpperCase s))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(let [^String s "abc"] (.toUpperCase s))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(let [^String s "abc"] (.toUpperCase s))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(let [^String s "abc"] (.toUpperCase s))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(let [^String s "abc"] (.toUpperCase s))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(let [^String s "abc"] (.toUpperCase s))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-09: Checked vs unchecked math

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(+ 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(+ 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(+ 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-14: Debugging host leaks

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [HIGH_LENGTH] form=`(try (Math/sqrt 4) (catch Exception _ :err))` — user_msg 229 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(try (Math/sqrt 4) (catch Exception _ :err))` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(try (Math/sqrt 4) (catch Exception _ :err))` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

## Grade 12

### G12-01: Transducers introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [CAP_PRONOUN_MID_SENTENCE] form=`(into [] (map inc) [1 2 3])` — ', She composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(into [] (map inc) [1 2 3])` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G12-02: Transducer composition

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CAP_PRONOUN_MID_SENTENCE': 1, 'POST_COMMA_CAPITAL_PRONOUN': 1}
    - [HIGH_LENGTH] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — user_msg 207 words
    - [CAP_PRONOUN_MID_SENTENCE] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    - [POST_COMMA_CAPITAL_PRONOUN] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}

### G12-06: clojure.spec

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into milkmaid prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — tortoise-hare-specific imagery 'wooden sign nailed to a tree' leaks into milkmaid prose

### G12-17: Library design patterns

- examples: 3
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2, 'LOW_GROUNDING': 3}
    - [FOREIGN_FABLE_IMAGERY] form=`(= [1 2 3] (vec '(1 2 3)))` — tortoise-hare-specific imagery 'leather notebook' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`(= [1 2 3] (vec '(1 2 3)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(= [1 2 3] (vec '(1 2 3)))` — tortoise-hare-specific imagery 'small audience of forest creatures' leaks into milkmaid prose
    - [LOW_GROUNDING] form=`(= [1 2 3] (vec '(1 2 3)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= [1 2 3] (vec '(1 2 3)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

---

## Summary

### Issue counts (across all examples × 3 records)

- **LOW_GROUNDING**: 478
- **CAP_PRONOUN_MID_SENTENCE**: 98
- **POST_COMMA_CAPITAL_PRONOUN**: 97
- **FOREIGN_FABLE_IMAGERY**: 35
- **CONCEPT_AS_VERB**: 32
- **HIGH_LENGTH**: 22
- **BOOL_LEAK_RESOLUTION**: 6
- **FORM_LEAK**: 3
- **LOWERCASE_CONCEPT_AFTER_PERIOD**: 3
- **ANSWER_LEAK**: 1
- **ANSWER_LEAK_STRING**: 1
- **SMALL_INT_LEAK**: 1
- **DOUBLE_PREP**: 1

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 97 | — |
| 2 | 22 | 88 | 117 | — |
| 3 | 18 | 31 | 17 | — |
| 4 | 20 | 39 | 23 | — |
| 5 | 22 | 39 | 11 | — |
| 6 | 16 | 33 | 82 | — |
| 7 | 18 | 36 | 99 | — |
| 8 | 16 | 31 | 99 | — |
| 9 | 18 | 34 | 89 | — |
| 10 | 16 | 36 | 102 | — |
| 11 | 14 | 29 | 30 | — |
| 12 | 18 | 37 | 12 | — |

### Sample issues by severity

#### LOW_GROUNDING

- `G1-01` (form `0`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    by the farm, before the cocks had finished crowing, Trudi had set out with the milk and a head full of plans.

Halfway through the race, Trudi stopped near the farm and refused to
continue until someone could prove what the form `0`
evaluated to. Trudi called it impossible.
Perpetua, walking up at h...
    ```
- `G1-01` (form `0`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    By the time Natalya had reached the second milestone by the village, the milk had become eggs, and the eggs a flock.

With a twig, Natalya marked out a wager in the village: whoever
guessed the result of `0` first would win the right to
choose the next contest. Baltasar, in the patient measure of on...
    ```
- `G1-01` (form `0`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    at the farm, where the lane bends past the old hedge, Theodora began to add up coins she had not yet earned.

At a moss-covered milestone near the farm, Theodora sketched a small
wager into the path: whoever guessed the result of `0`
first would win the right to set the next race. Domenica,
as a mil...
    ```
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
    Every step of the road carried the soft sound of liquid against tin and the louder sound of a daydream gathering speed.

A small audience of forest creatures had gathered along the road to watch
Floarea attempt to outwit Petra at reading the REPL.
Petra pointed to the integer 0 and read out the form...
    ```

#### FOREIGN_FABLE_IMAGERY

- `G1-01` (form `0`): tortoise-hare-specific imagery 'moss-covered milestone' leaks into milkmaid prose
    ```
    at the farm, where the lane bends past the old hedge, Theodora began to add up coins she had not yet earned.

At a moss-covered milestone near the farm, Theodora sketched a small
wager into the path: whoever guessed the result of `0`
first would win the right to set the next race. Domenica,
as a mil...
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
- `G1-02` (form `7`): tortoise-hare-specific imagery 'moss-covered milestone' leaks into milkmaid prose
    ```
    Milk does not forgive a tilted head, but a dreaming mind seldom remembers as much.

At a moss-covered milestone at the edge of the hilltop, Marta sketched a small
wager into the path: whoever guessed the result of `7`
first would win the right to set the next race. Walther,
with the long-breathed pa...
    ```

#### CAP_PRONOUN_MID_SENTENCE

- `G1-09` (form `(= 'hare 'hare)`): ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    ```
    Long before the market opened its stalls, a young woman had already spent her milk three times in her head.

Two chalk marks were written on the dairy wall: 'hare' and 'hare'. The milkmaid nodded, guessing they were the same. The farmer asked: but are those symbols truly equal? Let us read them thro...
    ```
- `G1-16` (form `(zero? 5)`): ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    ```
    Solveig had walked this road by the market a hundred times before, but never quite so dreamily.

Another pile sat on the table: five copper coins, jingling and bright. The farmer chalked a form to test whether this full pile was zero.

She needed the coin-counter predicate to read this pile and answ...
    ```
- `G1-16` (form `(pos? 7)`): ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

The farmer held a pile of seven gold coins on the sunny side of the table. The coins caught the light. She chalked a form to ask: is this pile on the plus side — positive?

She needed a predicate t...
    ```
- `G1-16` (form `(pos? 7)`): ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    ```
    in the village, where the lane bends past the old hedge, Sinead began to add up coins she had not yet earned.

The farmer held a pile of seven gold coins on the sunny side of the table. The coins caught the light. She chalked a form to ask: is this pile on the plus side — positive?

She needed a pre...
    ```
- `G1-16` (form `(neg? 4)`): ', He composed…' (capitalized pronoun mid-sentence after comma — should be lowercase)
    ```
    in the market, before the cocks had finished crowing, Czeslawa had set out with the milk and a head full of plans.

The farmer held a pile of four coins on the light side of the table. She chalked a form to test whether this bright pile was on the dark side — negative.

She needed the dark-test pred...
    ```

#### POST_COMMA_CAPITAL_PRONOUN

- `G1-09` (form `(= 'hare 'hare)`): capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    ```
    Long before the market opened its stalls, a young woman had already spent her milk three times in her head.

Two chalk marks were written on the dairy wall: 'hare' and 'hare'. The milkmaid nodded, guessing they were the same. The farmer asked: but are those symbols truly equal? Let us read them thro...
    ```
- `G1-15` (form `(= 1 1)`): capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    ```
    There was once a milkmaid who walked to market with a pail of fresh milk balanced upon her head.

One morning, He walked Adriana through a series of gates on the path. The first
gate was open, the second was open, but the third gate's rule said 'closed.' "Here," he
said, pointing. "The form for the ...
    ```
- `G1-15` (form `(= :hare :hare)`): capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    ```
    Tamara had walked this road in the meadow a hundred times before, but never quite so dreamily.

One morning, He walked Tamara through a series of gates on the path. The first
gate was open, the second was open, but the third gate's rule said 'closed.' "Here," he
said, pointing. "The form for the key...
    ```
- `G1-16` (form `(zero? 5)`): capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    ```
    Solveig had walked this road by the market a hundred times before, but never quite so dreamily.

Another pile sat on the table: five copper coins, jingling and bright. The farmer chalked a form to test whether this full pile was zero.

She needed the coin-counter predicate to read this pile and answ...
    ```
- `G1-16` (form `(pos? 7)`): capitalized pronoun (He/She/They) immediately after a comma in a continuation clause — the story-scaffold template should use {X_he_she} (lowercase) here, not {X_he_she_cap}
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

The farmer held a pile of seven gold coins on the sunny side of the table. The coins caught the light. She chalked a form to ask: is this pile on the plus side — positive?

She needed a predicate t...
    ```

#### ANSWER_LEAK

- `G2-10` (form `(* 3 3 3 3)`): answer 81 in narrative
    ```
    It happened at the farm, on the morning Solvi took the milk to market and her thoughts ran ahead of her feet.

The farmer had a four-dimensional arrangement of coins (a thought experiment): 3 coins in each dimension. She wondered what the total count would be if she could stack all dimensions at onc...
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
- `G7-05` (form `(some? nil)`): resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    ```
    She had not yet sold the milk and yet had already chosen the ribbons she would wear at the dance.

Clara gazed at an empty basket that had held cream, now containing nothing—nil, a void.

Is the void something? Is nothing one of something's cousins? She wanted to test carefully.

Nil is the empty pa...
    ```

#### HIGH_LENGTH

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
- `G4-11` (form `(count #{1 1 1})`): user_msg 204 words
    ```
    On market mornings, the dairy yard smelled of damp grass and warm tin, and the future seemed safely arrangeable.

The milkmaid tried to record the price 1 three times over — once as she heard it, once as she wrote it down, once as she repeated it aloud. But the set refused to store the duplicate.

S...
    ```
- `G5-10` (form `(map #(* % %) [1 2 3 4])`): user_msg 201 words
    ```
    Every step of the road carried the soft sound of liquid against tin and the louder sound of a daydream gathering speed.

The milkmaid fitted a squaring rule to her milk-strainer and poured four counts through it: one, two, three, four. Each piece would come out multiplied by itself on the far side.
...
    ```
- `G5-22` (form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n)`): user_msg 205 words
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

The milkmaid walked the daily milking circuit: five stations along the same path, starting with a tally of 1. At each station she multiplied the running tally by the station count, then moved one s...
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
- `G4-16` (form `(into #{} [1 2 2 3])`): form '(into #{} [1 2 2 3])' appears in user_msg of a goal-style subject
    ```
    It was near the hilltop, on a fair-weather morning, that Thalia began the long walk to market.

The milkmaid held a basket with four items: 1, 2, 2, 3 — but two of them were the same price. She held a milk-strainer over an empty set-pail, preparing to pour the basket's contents through.

She needed ...
    ```

#### CONCEPT_AS_VERB

- `G6-01` (form `(name 'clojure.string)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    It was the season of new chicks and first cheeses, and every small profit felt like the start of a larger one.

She declared, "I will invent new names for the prices each time I visit the market!"
But he only shook his head. "No, Katarzyna. To extract the string form of a quoted namespace symbol, yo...
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
- `G6-06` (form `(:private (meta 'x))`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    On market mornings, the dairy yard smelled of damp grass and warm tin, and the future seemed safely arrangeable.

She declared, "I will invent new names for the prices each time I visit the market!"
But she only shook her head. "No, Ursula. To check whether the :private flag is present in the metada...
    ```

#### LOWERCASE_CONCEPT_AFTER_PERIOD

- `G7-05` (form `(first nil)`): sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    ```
    The cows had given generously that dawn, and the pail was heavier than usual, and the imagination was heavier still.

She claimed, "I can get the first element of nil while running and juggling!" But he
knew better. "In the real meadow, a stumble spills the pail. But in the practice meadow — the REP...
    ```
- `G7-06` (form `(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exception e 0)`): sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    ```
    Some plans grow gently from the ground up; others are built from the rooftop down, and topple just as fast.

She claimed, "I can call a function with a positive precondition on a negative number, catching the failure while running and juggling!" But she
knew better. "In the real meadow, a stumble sp...
    ```
- `G7-06` (form `(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exception e 0)`): sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    ```
    On market mornings, the dairy yard smelled of damp grass and warm tin, and the future seemed safely arrangeable.

She claimed, "I can call a function with a positive precondition on a negative number, catching the failure while running and juggling!" But she
knew better. "In the real meadow, a stumb...
    ```

#### ANSWER_LEAK_STRING

- `G7-10` (form `(:doc (meta '^{:doc "adds two"} plus))`): answer string 'adds two' appears in user_msg
    ```
    It was the season of new chicks and first cheeses, and every small profit felt like the start of a larger one.

Clara found an old scroll marking the symbol 'plus' with notes written in the margins: 'adds two'.

She wanted to read the attached documentation note. What words were written in those mar...
    ```

#### SMALL_INT_LEAK

- `G9-02` (form `(do (def counter (atom 0)) (swap! counter inc) @counter)`): small-int answer 1 leaks via resolution-slot phrasing
    ```
    Long before the market opened its stalls, a young woman had already spent her milk three times in her head.

The milkmaid hung a fresh tally-slate by the dairy door with the number 0 chalked at the top — the starting count for the day's deliveries. The first pail went out; the slate needed updating....
    ```

#### DOUBLE_PREP

- `G9-18` (form `(do (def lock (Object.)) (locking lock 42))`): verb+preposition followed by {place} which already carries its own preposition
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

The farmer showed the milkmaid the simplest possible padlocked section: just a plain value inside the lock. The padlock was real — it acquired the monitor — but the body needed no computation.

She...
    ```

