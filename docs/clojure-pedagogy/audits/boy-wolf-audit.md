# boy-wolf curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

### G1-01: Eval as substitution

- examples: 8
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'HONEST_JUDGE_REPEAT': 2, 'FORM_DISPLAY_AND_FORM_NOUN': 5}
    - [LOW_GROUNDING] form=`0` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HONEST_JUDGE_REPEAT] form=`0` — two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    - [HONEST_JUDGE_REPEAT] form=`(+ 1 2)` — two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(* 4 5)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(- 10 (+ 2 3))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(+ 1 (* 2 3))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-02: Integer numbers

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'HONEST_JUDGE_REPEAT': 4, 'FORM_DISPLAY_AND_FORM_NOUN': 4, 'FOREIGN_FABLE_IMAGERY': 2}
    - [LOW_GROUNDING] form=`7` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`7` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HONEST_JUDGE_REPEAT] form=`7` — two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`-3` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FOREIGN_FABLE_IMAGERY] form=`-3` — tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    - [LOW_GROUNDING] form=`0` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-03: Ratios

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'FOREIGN_FABLE_IMAGERY': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 5}
    - [LOW_GROUNDING] form=`1/2` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`1/2` — tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    - [LOW_GROUNDING] form=`1/2` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`3/4` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(+ 1/2 1/4)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(+ 1/2 1/4)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-04: Strings

- examples: 5
- variety @ n=50: 1.00
- issues: {'HONEST_JUDGE_REPEAT': 4, 'FORM_DISPLAY_AND_FORM_NOUN': 2, 'FOREIGN_FABLE_IMAGERY': 3}
    - [HONEST_JUDGE_REPEAT] form=`"hello"` — two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    - [HONEST_JUDGE_REPEAT] form=`"hello"` — two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`"flock"` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FOREIGN_FABLE_IMAGERY] form=`"flock"` — tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    - [HONEST_JUDGE_REPEAT] form=`"watch the meadow"` — two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    - [FOREIGN_FABLE_IMAGERY] form=`"watch the meadow"` — tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose

### G1-05: Booleans

- examples: 6
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 5, 'LOW_GROUNDING': 4, 'FOREIGN_FABLE_IMAGERY': 2, 'HONEST_JUDGE_REPEAT': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`true` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`true` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`true` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`true` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`false` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`false` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-06: nil

- examples: 5
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 5, 'LOW_GROUNDING': 9, 'FOREIGN_FABLE_IMAGERY': 2, 'HONEST_JUDGE_REPEAT': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`nil` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`nil` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(nil? nil)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(nil? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(nil? nil)` — tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    - [LOW_GROUNDING] form=`(nil? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-07: Keywords

- examples: 5
- variety @ n=50: 1.00
- issues: {'HONEST_JUDGE_REPEAT': 1, 'FOREIGN_FABLE_IMAGERY': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [HONEST_JUDGE_REPEAT] form=`:alarm` — two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    - [FOREIGN_FABLE_IMAGERY] form=`:alarm` — tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(= :wolf :wolf)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-08: Characters

- examples: 4
- variety @ n=50: 1.00
- issues: {'VILLAGE_NOUN_OVERUSE': 1, 'STRING_AS_CHAR_MISCLAIM': 7, 'HONEST_JUDGE_REPEAT': 1, 'FOREIGN_FABLE_IMAGERY': 3}
    - [VILLAGE_NOUN_OVERUSE] form=`\w` — `the village` appears 4 times (noun-saturation tic — vary or drop)
    - [STRING_AS_CHAR_MISCLAIM] form=`\w` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    - [HONEST_JUDGE_REPEAT] form=`\w` — two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    - [STRING_AS_CHAR_MISCLAIM] form=`\w` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    - [FOREIGN_FABLE_IMAGERY] form=`\w` — tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    - [STRING_AS_CHAR_MISCLAIM] form=`\w` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)

### G1-09: Symbols vs values

- examples: 4
- variety @ n=50: 0.99
- issues: {'EMPTY_GOAL_RENDERED': 9, 'BOOL_LEAK_RESOLUTION': 1, 'LOW_GROUNDING': 4, 'PARAGRAPH_FRAGMENTATION': 1, 'ONLY_SHOOK_HEAD_TIC': 3}
    - [EMPTY_GOAL_RENDERED] form=`(symbol? 'wolf)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [BOOL_LEAK_RESOLUTION] form=`(symbol? 'wolf)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(symbol? 'wolf)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(symbol? 'wolf)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [PARAGRAPH_FRAGMENTATION] form=`(symbol? 'wolf)` — user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [EMPTY_GOAL_RENDERED] form=`(symbol? 'wolf)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G1-10: Comments

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(+ 1 2) ; sum of one and two` — sentence with 5 commas reads as AI-output cadence: 'To add 1 and 2, with a single-semicolon trailing comment, he composed\nthe additi'
    - [CLAUSE_STACK_OVERFLOW] form=`(+ 1 2) ; sum of one and two` — sentence with 5 commas reads as AI-output cadence: 'To add 6 and 4, with a single-semicolon trailing comment, she composed\nthe addit'

### G1-11: Whitespace doesn't matter

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(+
  1
  2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(+
  1
  2)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'
    - [LOW_GROUNDING] form=`(+
  1
  2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-13: First arithmetic call

- examples: 6
- variety @ n=50: 1.00
- issues: {'EMPTY_GOAL_RENDERED': 5, 'PARAGRAPH_FRAGMENTATION': 4, 'REPL_AS_TIME_TRAVELLER': 4, 'REPEATED_OPENER_FRAGMENT': 1, 'LOW_GROUNDING': 1}
    - [EMPTY_GOAL_RENDERED] form=`(+ 1 2)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(+ 1 2)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(+ 1 2)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [PARAGRAPH_FRAGMENTATION] form=`(- 5 3)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [PARAGRAPH_FRAGMENTATION] form=`(- 5 3)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [EMPTY_GOAL_RENDERED] form=`(* 4 5)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G1-14: Nested call evaluation

- examples: 4
- variety @ n=50: 1.00
- issues: {'EMPTY_GOAL_RENDERED': 3}
    - [EMPTY_GOAL_RENDERED] form=`(+ 1 (* 2 3))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(+ 1 (* 2 3))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(+ 1 (* 2 3))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G1-15: Equality

- examples: 6
- variety @ n=50: 1.00
- issues: {'EMPTY_GOAL_RENDERED': 12, 'CLAUSE_STACK_OVERFLOW': 5, 'LOW_GROUNDING': 4, 'BOOL_LEAK_RESOLUTION': 4, 'PARAGRAPH_FRAGMENTATION': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [EMPTY_GOAL_RENDERED] form=`(= 1 1)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [CLAUSE_STACK_OVERFLOW] form=`(= 1 1)` — sentence with 5 commas reads as AI-output cadence: 'An empty bucket, a zero-tally, a sleeping\nflock — every one of those still swing'
    - [LOW_GROUNDING] form=`(= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(= 1 1)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(= 1 1)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(= 1 2)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G1-16: Numeric predicates

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'REPL_AS_TIME_TRAVELLER': 5, 'BOOL_LEAK_RESOLUTION': 4, 'PARAGRAPH_FRAGMENTATION': 3}
    - [LOW_GROUNDING] form=`(zero? 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [REPL_AS_TIME_TRAVELLER] form=`(zero? 0)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [BOOL_LEAK_RESOLUTION] form=`(zero? 5)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [PARAGRAPH_FRAGMENTATION] form=`(zero? 5)` — user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [REPL_AS_TIME_TRAVELLER] form=`(zero? 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [REPL_AS_TIME_TRAVELLER] form=`(pos? 7)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

### G1-17: Printing vs returning

- examples: 2
- variety @ n=50: 1.00
- issues: {'EMPTY_GOAL_RENDERED': 6, 'CLAUSE_STACK_OVERFLOW': 1}
    - [EMPTY_GOAL_RENDERED] form=`42` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [CLAUSE_STACK_OVERFLOW] form=`42` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'
    - [EMPTY_GOAL_RENDERED] form=`42` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`42` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(+ 1 2)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(+ 1 2)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G1-18: Errors are safe in the REPL

- examples: 2
- variety @ n=50: 1.00
- issues: {'EMPTY_GOAL_RENDERED': 3, 'PARAGRAPH_FRAGMENTATION': 1, 'LOW_GROUNDING': 1}
    - [EMPTY_GOAL_RENDERED] form=`(+ 1 2)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [PARAGRAPH_FRAGMENTATION] form=`(+ 1 2)` — user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [EMPTY_GOAL_RENDERED] form=`(+ 1 2)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(+ 1 2)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [LOW_GROUNDING] form=`(* 7 6)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 2

### G2-01: Multi-arg arithmetic

- examples: 6
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'REPL_AS_TIME_TRAVELLER': 6, 'LOW_GROUNDING': 1, 'ANSWER_LEAK': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(+ 1 2 3 4)` — sentence with 6 commas reads as AI-output cadence: 'To add 8, 7, 5, and 7, he\ncomposed the multi-arg sum, submitted it to the REPL, '
    - [REPL_AS_TIME_TRAVELLER] form=`(* 2 3 4)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [REPL_AS_TIME_TRAVELLER] form=`(* 2 3 4)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [CLAUSE_STACK_OVERFLOW] form=`(* 2 3 4)` — sentence with 5 commas reads as AI-output cadence: 'To multiply 5, 2, and 8, he\ncomposed the multi-arg product, submitted it to the '
    - [REPL_AS_TIME_TRAVELLER] form=`(- 100 1 2 3)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [LOW_GROUNDING] form=`(+ 1 2 3 4 5 6 7 8 9 10)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-02: Comparison chains

- examples: 5
- variety @ n=50: 1.00
- issues: {'REPL_AS_TIME_TRAVELLER': 4, 'BOOL_LEAK_RESOLUTION': 3, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'LOW_GROUNDING': 2}
    - [REPL_AS_TIME_TRAVELLER] form=`(< 1 2 3)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [BOOL_LEAK_RESOLUTION] form=`(< 3 2 1)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(<= 1 1 2)` — parametric example has hard-coded English numeral 'three bundles' in a story slot — the actual draws may differ from this fixed count
    - [LOW_GROUNDING] form=`(<= 1 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [REPL_AS_TIME_TRAVELLER] form=`(<= 1 1 2)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(<= 1 1 2)` — parametric example has hard-coded English numeral 'three bundles' in a story slot — the actual draws may differ from this fixed count

### G2-03: not= and = with multiple args

- examples: 5
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 3, 'FORM_DISPLAY_AND_FORM_NOUN': 2, 'PARAGRAPH_FRAGMENTATION': 2, 'LOW_GROUNDING': 4, 'REPL_AS_TIME_TRAVELLER': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 2}
    - [BOOL_LEAK_RESOLUTION] form=`(not= 1 2)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(not= 1 2)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [PARAGRAPH_FRAGMENTATION] form=`(not= 1 2)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [LOW_GROUNDING] form=`(not= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [REPL_AS_TIME_TRAVELLER] form=`(= 1 1 1)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

### G2-04: min and max

- examples: 5
- variety @ n=50: 1.00
- issues: {'REPL_AS_TIME_TRAVELLER': 3, 'FORM_DISPLAY_AND_FORM_NOUN': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [REPL_AS_TIME_TRAVELLER] form=`(min 1 2 3)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [REPL_AS_TIME_TRAVELLER] form=`(min 1 2 3)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(min 1 2 3)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(max 1 2 3)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(max 1 2 3)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [REPL_AS_TIME_TRAVELLER] form=`(max 7 3 9 1 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

### G2-05: quot, rem, mod

- examples: 6
- variety @ n=50: 1.00
- issues: {'REPL_AS_TIME_TRAVELLER': 3, 'SMALL_INT_LEAK': 1}
    - [REPL_AS_TIME_TRAVELLER] form=`(quot 17 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [REPL_AS_TIME_TRAVELLER] form=`(rem 17 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [SMALL_INT_LEAK] form=`(mod 17 5)` — small-int answer 2 leaks via resolution-slot phrasing
    - [REPL_AS_TIME_TRAVELLER] form=`(quot 100 7)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

### G2-06: inc and dec

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'REPL_AS_TIME_TRAVELLER': 3, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [LOW_GROUNDING] form=`(inc 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [REPL_AS_TIME_TRAVELLER] form=`(inc 0)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [LOW_GROUNDING] form=`(inc 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [REPL_AS_TIME_TRAVELLER] form=`(dec 0)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [REPL_AS_TIME_TRAVELLER] form=`(dec 0)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [LOW_GROUNDING] form=`(inc -1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-07: Absolute value

- examples: 4
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2, 'PARAGRAPH_FRAGMENTATION': 2, 'LOW_GROUNDING': 2, 'REPL_AS_TIME_TRAVELLER': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(abs 5)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [PARAGRAPH_FRAGMENTATION] form=`(abs 5)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [LOW_GROUNDING] form=`(abs -5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(abs -5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(abs -5)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [PARAGRAPH_FRAGMENTATION] form=`(abs -5)` — user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G2-08: Arithmetic on ratios

- examples: 3
- variety @ n=50: 0.99
- issues: {'REPL_AS_TIME_TRAVELLER': 2, 'EMPTY_GOAL_RENDERED': 5, 'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [REPL_AS_TIME_TRAVELLER] form=`(+ 1/2 1/4)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [EMPTY_GOAL_RENDERED] form=`(+ 1/2 1/4)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(+ 1/2 1/4)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [LOW_GROUNDING] form=`(* 2/3 3/4)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 2/3 3/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3', '4'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(* 2/3 3/4)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-09: Floats vs ints (the / operator)

- examples: 3
- variety @ n=50: 1.00
- issues: {'PARAGRAPH_FRAGMENTATION': 2, 'REPL_AS_TIME_TRAVELLER': 2}
    - [PARAGRAPH_FRAGMENTATION] form=`(/ 10 3)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [REPL_AS_TIME_TRAVELLER] form=`(/ 10 3)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [PARAGRAPH_FRAGMENTATION] form=`(/ 1.0 2)` — user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [REPL_AS_TIME_TRAVELLER] form=`(/ 1.0 2)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

### G2-10: Powers via repeated multiplication

- examples: 4
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1, 'LOW_GROUNDING': 3, 'PARAGRAPH_FRAGMENTATION': 2, 'REPL_AS_TIME_TRAVELLER': 1}
    - [ANSWER_LEAK] form=`(* 2 2 2)` — answer 8 in narrative
    - [LOW_GROUNDING] form=`(* 2 2 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PARAGRAPH_FRAGMENTATION] form=`(* 2 2 2)` — user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [LOW_GROUNDING] form=`(* 2 2 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(* 5 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PARAGRAPH_FRAGMENTATION] form=`(* 5 5)` — user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G2-11: String concatenation with str

- examples: 4
- variety @ n=50: 1.00
- issues: {'EMPTY_GOAL_RENDERED': 9, 'CLAUSE_STACK_OVERFLOW': 3}
    - [EMPTY_GOAL_RENDERED] form=`(str "wa" "tch")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(str "wa" "tch")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(str "wa" "tch")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(str "flock")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(str "flock")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(str "flock")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G2-12: print and println — return values

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2, 'THE_FORM_OVERUSE': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(print "x")` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [THE_FORM_OVERUSE] form=`(print "x")` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(print "x")` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [THE_FORM_OVERUSE] form=`(print "x")` — `the form` appears 5 times in user_msg (template tic — vary references)

### G2-13: and / or — short circuit, return values

- examples: 6
- variety @ n=50: 0.99
- issues: {'BOOL_LEAK_RESOLUTION': 2, 'LOW_GROUNDING': 4, 'PARAGRAPH_FRAGMENTATION': 3, 'CLAUSE_STACK_OVERFLOW': 10, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [BOOL_LEAK_RESOLUTION] form=`(and true true)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PARAGRAPH_FRAGMENTATION] form=`(and true true)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [CLAUSE_STACK_OVERFLOW] form=`(and true true)` — sentence with 5 commas reads as AI-output cadence: 'To test whether two trues both pass through an and-chain of gates, she\ncomposed '
    - [CLAUSE_STACK_OVERFLOW] form=`(and true true)` — sentence with 5 commas reads as AI-output cadence: 'If it shuts, the chain stops there — the gates\nbehind it never see the value at '
    - [CLAUSE_STACK_OVERFLOW] form=`(and true false)` — sentence with 5 commas reads as AI-output cadence: 'To test true and false with the and operator, he\ncomposed the logical and, submi'

### G2-14: not — turning truthy to false

- examples: 5
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'LOW_GROUNDING': 2, 'PARAGRAPH_FRAGMENTATION': 1, 'CLAUSE_STACK_OVERFLOW': 8}
    - [BOOL_LEAK_RESOLUTION] form=`(not true)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(not true)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PARAGRAPH_FRAGMENTATION] form=`(not true)` — user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [CLAUSE_STACK_OVERFLOW] form=`(not true)` — sentence with 5 commas reads as AI-output cadence: 'An empty bucket, a zero-tally, a sleeping\nflock — every one of those still swing'
    - [CLAUSE_STACK_OVERFLOW] form=`(not false)` — sentence with 5 commas reads as AI-output cadence: 'To negate the value false, he\ncomposed the logical not, submitted the form, and '

### G2-15: Falsey values: only false and nil

- examples: 4
- variety @ n=50: 1.00
- issues: {'EMPTY_GOAL_RENDERED': 12, 'CLAUSE_STACK_OVERFLOW': 3, 'LOW_GROUNDING': 4, 'FORM_DISPLAY_AND_FORM_NOUN': 4, 'THE_FORM_OVERUSE': 4, 'PARAGRAPH_FRAGMENTATION': 4}
    - [EMPTY_GOAL_RENDERED] form=`(if 0 :truthy :falsey)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [CLAUSE_STACK_OVERFLOW] form=`(if 0 :truthy :falsey)` — sentence with 5 commas reads as AI-output cadence: 'An empty bucket, a zero-tally, a sleeping\nflock — every one of those still swing'
    - [LOW_GROUNDING] form=`(if 0 :truthy :falsey)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(if 0 :truthy :falsey)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(if 0 :truthy :falsey)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(if "" :truthy :falsey)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G2-16: Truthy 0 and empty string

- examples: 4
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 5, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'PARAGRAPH_FRAGMENTATION': 1, 'LOW_GROUNDING': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(boolean 0)` — sentence with 5 commas reads as AI-output cadence: 'To convert 3 to a boolean, she\ncomposed the boolean conversion, submitted the fo'
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(boolean "")` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [PARAGRAPH_FRAGMENTATION] form=`(boolean "")` — user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [CLAUSE_STACK_OVERFLOW] form=`(boolean "")` — sentence with 5 commas reads as AI-output cadence: 'To convert the empty string to a boolean, she\ncomposed the boolean conversion, s'
    - [CLAUSE_STACK_OVERFLOW] form=`(boolean nil)` — sentence with 5 commas reads as AI-output cadence: 'An empty bucket, a zero-tally, a sleeping\nflock — every one of those still swing'
    - [CLAUSE_STACK_OVERFLOW] form=`(boolean false)` — sentence with 5 commas reads as AI-output cadence: 'An empty bucket, a zero-tally, a sleeping\nflock — every one of those still swing'

### G2-17: Keyword as function for map lookup

- examples: 3
- variety @ n=50: 1.00
- issues: {'EMPTY_GOAL_RENDERED': 7, 'LOW_GROUNDING': 4, 'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [EMPTY_GOAL_RENDERED] form=`(:wolf {:wolf 1 :flock 2})` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [LOW_GROUNDING] form=`(:wolf {:wolf 1 :flock 2})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(:wolf {:wolf 1 :flock 2})` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(:wolf {:wolf 1 :flock 2})` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(:flock {:wolf 1 :flock 2})` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(:flock {:wolf 1 :flock 2})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-18: Quoting symbols

- examples: 3
- variety @ n=50: 0.99
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 4, 'LOW_GROUNDING': 6, 'EMPTY_GOAL_RENDERED': 6, 'PARAGRAPH_FRAGMENTATION': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(quote wolf)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(quote wolf)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(quote wolf)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(quote wolf)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(quote wolf)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(quote wolf)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G2-19: Auto-promotion to bigint

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'REPL_AS_TIME_TRAVELLER': 1}
    - [LOW_GROUNDING] form=`(* 1000000 1000000)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(* 1000000 1000000)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(* 1000000 1000000)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [REPL_AS_TIME_TRAVELLER] form=`(+ 99999999999 1)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

### G2-20: Counting

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'ONLY_SHOOK_HEAD_TIC': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'SMALL_INT_LEAK': 2, 'FORM_DISPLAY_AND_FORM_NOUN': 2, 'PARAGRAPH_FRAGMENTATION': 2, 'SENTENCE_START_LOWER_PRONOUN': 2}
    - [LOW_GROUNDING] form=`(count [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [ONLY_SHOOK_HEAD_TIC] form=`(count [1 2 3])` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [LOW_GROUNDING] form=`(count [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'The runtime does this the same way for any kind of collection."\nTo count the ele'
    - [SMALL_INT_LEAK] form=`(count "hello")` — small-int answer 5 leaks via resolution-slot phrasing
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(count "hello")` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G2-21: String length and substring

- examples: 3
- variety @ n=50: 1.00
- issues: {'EMPTY_GOAL_RENDERED': 9, 'ANSWER_LEAK': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 3, 'THE_FORM_OVERUSE': 3, 'PARAGRAPH_FRAGMENTATION': 2, 'SMALL_INT_LEAK': 1}
    - [EMPTY_GOAL_RENDERED] form=`(count "shepherd")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(count "shepherd")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [ANSWER_LEAK] form=`(count "shepherd")` — answer 8 in narrative
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(count "shepherd")` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [THE_FORM_OVERUSE] form=`(count "shepherd")` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [EMPTY_GOAL_RENDERED] form=`(count "shepherd")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G2-22: Compose pure arithmetic (multi-step calculation)

- examples: 3
- variety @ n=50: 1.00
- issues: {'PARAGRAPH_FRAGMENTATION': 3, 'ANSWER_LEAK': 2, 'REPL_AS_TIME_TRAVELLER': 1}
    - [PARAGRAPH_FRAGMENTATION] form=`(+ (* 3 8) (* 2 4))` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [ANSWER_LEAK] form=`(quot (+ 100 50) 5)` — answer 30 in narrative
    - [PARAGRAPH_FRAGMENTATION] form=`(quot (+ 100 50) 5)` — user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [REPL_AS_TIME_TRAVELLER] form=`(quot (+ 100 50) 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [ANSWER_LEAK] form=`(quot (+ 100 50) 5)` — answer 30 in narrative
    - [PARAGRAPH_FRAGMENTATION] form=`(quot (+ 100 50) 5)` — user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

## Grade 3

### G3-02: def — redefinition

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def x 1) (def x 99) x)` — sentence with 5 commas reads as AI-output cadence: 'To bind x to 7, then redefine it as 59 and return it, he composed the redefined '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def x 1) (def x 99) x)` — sentence with 5 commas reads as AI-output cadence: 'To bind x to 1, then redefine it as 56 and return it, the notice had to be read '

### G3-03: let — local binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'SMALL_INT_LEAK': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'SENTENCE_START_LOWER_PRONOUN': 1, 'LOW_GROUNDING': 1}
    - [HIGH_LENGTH] form=`(let [x 3] (+ x 1))` — user_msg 227 words
    - [SMALL_INT_LEAK] form=`(let [x 3] (+ x 1))` — small-int answer 4 leaks via resolution-slot phrasing
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [x 3] (+ x 1))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [SENTENCE_START_LOWER_PRONOUN] form=`(let [x 3] (+ x 1))` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [LOW_GROUNDING] form=`(let [a 5] a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G3-04: let — multi-binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(let [x 5 y 3] (- x y))` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [a 2 b 3 c 4] (+ a b c))` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [a 2 b 3 c 4] (+ a b c))` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [a 2 b 3 c 4] (+ a b c))` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count

### G3-05: let — shadowing outer def

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(do (def x 10) (let [x 99] x))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def x 10) (let [x 99] x) x)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G3-06: let — binding can reference prior

- examples: 2
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 2, 'CLAUSE_STACK_OVERFLOW': 1, 'ANSWER_LEAK': 1}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(let [a 5 b (* a 2)] b)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a 5 b (* a 2)] b)` — sentence with 5 commas reads as AI-output cadence: 'Step past the form\'s\nedge and the pouch is empty again." To bind a to 5, then bi'
    - [SENTENCE_START_LOWER_PRONOUN] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [ANSWER_LEAK] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — answer 8 in narrative

### G3-07: fn — anonymous function

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 1, 'SMALL_INT_LEAK': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (+ x 1)) 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (+ x 1)) 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`((fn [x] (+ x 1)) 4)` — user_msg 223 words
    - [SMALL_INT_LEAK] form=`((fn [x] (+ x 1)) 4)` — small-int answer 5 leaks via resolution-slot phrasing
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (+ x 1)) 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [a b] (* a b)) 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)

### G3-08: fn — multi-arg

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CONCEPT_AS_VERB': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [a b c] (+ a b c)) 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`((fn [a b c] (+ a b c)) 1 2 3)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [a b c] (+ a b c)) 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [a b c] (+ a b c)) 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`((fn [a b c] (+ a b c)) 1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'The earlier steps prepare the way; the last\nstep is the answer." To create an an'

### G3-09: defn — shorthand

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'ANSWER_LEAK': 2, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(do (defn dbl [x] (* x 2)) (dbl 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defn dbl [x] (* x 2)) (dbl 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [ANSWER_LEAK] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — answer 6 in narrative
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [ANSWER_LEAK] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — answer 6 in narrative
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1, 'CONCEPT_AS_VERB': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [ANSWER_LEAK] form=`(#(+ % 1) 5)` — answer 6 in narrative
    - [CONCEPT_AS_VERB] form=`(#(+ % 1) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(* %1 %2) 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(* %1 %2) 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`(#(* %1 %2) 3 4)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(* %1 %2) 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)

### G3-11: Substitution rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(let [a 7] (+ a a))` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (* x x)) 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (* x x)) 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [SENTENCE_START_LOWER_PRONOUN] form=`((fn [x] (* x x)) 6)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (* x x)) 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)

### G3-12: Scope vs namespace

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def g 5) (let [g 99] (+ g 1)))` — sentence with 6 commas reads as AI-output cadence: 'To define g at the top level, shadow it in a let with a different value, and com'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def g 5) (let [g 99] (+ g 1)))` — sentence with 6 commas reads as AI-output cadence: 'To define g at the top level, shadow it in a let with a different value, and com'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def g 5) (let [g 99] (+ g 1)))` — sentence with 5 commas reads as AI-output cadence: "The next shepherd along the path reads what's there now —\nwhatever the latest ch"

### G3-13: fn body returns last form

- examples: 1
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`((fn [x] x x x 99) 1)` — user_msg 201 words

### G3-14: do form

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'LOW_GROUNDING': 4, 'CLAUSE_STACK_OVERFLOW': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(do 1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(do 1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [LOW_GROUNDING] form=`(do 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do 1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(do 1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [LOW_GROUNDING] form=`(do (+ 1 1) (+ 2 2) (+ 3 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G3-15: Side-effects in body

- examples: 1
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1, 'LOW_GROUNDING': 2}
    - [CONCEPT_AS_VERB] form=`(do (println "hi") 42)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(do (println "hi") 42)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (println "hi") 42)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G3-16: Name collision: namespace vs let

- examples: 1
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 1}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(let [+ 99] +)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation

### G3-17: Naming conventions (kebab-case)

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'EMPTY_GOAL_RENDERED': 3, 'ANSWER_LEAK': 1}
    - [LOW_GROUNDING] form=`(let [flock-size 8 stray-count 2] (- flock-size st` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(let [flock-size 8 stray-count 2] (- flock-size st` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [ANSWER_LEAK] form=`(let [flock-size 8 stray-count 2] (- flock-size st` — answer 6 in narrative
    - [EMPTY_GOAL_RENDERED] form=`(let [flock-size 8 stray-count 2] (- flock-size st` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [LOW_GROUNDING] form=`(let [flock-size 8 stray-count 2] (- flock-size st` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(let [flock-size 8 stray-count 2] (- flock-size st` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G3-18: When to name vs inline

- examples: 2
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 2, 'LOW_GROUNDING': 1}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(* 5 5 5)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [SENTENCE_START_LOWER_PRONOUN] form=`(* 5 5 5)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [LOW_GROUNDING] form=`(* 5 5 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 4

### G4-01: Vector literal

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'LOW_GROUNDING': 5}
    - [CLAUSE_STACK_OVERFLOW] form=`[1 2 3]` — sentence with 5 commas reads as AI-output cadence: 'To create a vector containing 1, 2, and 3 properly, she wrote\na vector of three '
    - [LOW_GROUNDING] form=`[1 2 3]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`[]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`[]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`[]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`["a" "b"]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-02: nth — vector access

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'CLAUSE_STACK_OVERFLOW': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 0)` — parametric example has hard-coded English numeral 'three bundles' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(nth [10 20 30] 0)` — sentence with 5 commas reads as AI-output cadence: 'To get the element at index 0 of a vector containing 10, 20, and 30 properly, he'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 0)` — parametric example has hard-coded English numeral 'three bundles' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 0)` — parametric example has hard-coded English numeral 'three bundles' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(nth [10 20 30] 0)` — sentence with 5 commas reads as AI-output cadence: 'To get the element at index 0 of a vector containing 10, 20, and 30 properly, he'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 2)` — parametric example has hard-coded English numeral 'three bundles' in a story slot — the actual draws may differ from this fixed count

### G4-03: conj — append to vector

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'EMPTY_GOAL_RENDERED': 1}
    - [LOW_GROUNDING] form=`(conj [] :wolf)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(conj [] :wolf)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [EMPTY_GOAL_RENDERED] form=`(conj [] :wolf)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G4-04: List literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'LOW_GROUNDING': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [LOW_GROUNDING] form=`'(1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`'()` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`'()` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-06: Map literal

- examples: 1
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'EMPTY_GOAL_RENDERED': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`{:wolf 1 :flock 2}` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [EMPTY_GOAL_RENDERED] form=`{:wolf 1 :flock 2}` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G4-07: get — map lookup

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4}
    - [LOW_GROUNDING] form=`(get {:a 1 :b 2} :a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(get {:a 1} :missing :default)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(get {:a 1} :missing :default)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(get {:a 1} :missing :default)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-09: dissoc — map remove key

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(dissoc {:a 1 :b 2} :a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-10: keys and vals

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(count (keys {:a 1 :b 2 :c 3}))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count (keys {:a 1 :b 2 :c 3}))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(count (keys {:a 1 :b 2 :c 3}))` — sentence with 5 commas reads as AI-output cadence: 'To count how many keys are in a map binding :a, :b, and :c properly, he wrote\nco'

### G4-11: Set literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(count #{1 1 1})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count #{1 1 1})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-12: Set membership

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'BOOL_LEAK_RESOLUTION': 3, 'FORM_DISPLAY_AND_FORM_NOUN': 2, 'PARAGRAPH_FRAGMENTATION': 2}
    - [LOW_GROUNDING] form=`(contains? #{1 2 3} 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(contains? #{1 2 3} 2)` — sentence with 5 commas reads as AI-output cadence: 'To check whether 2 is a member of a set containing 1, 2, and 3 properly, he wrot'
    - [BOOL_LEAK_RESOLUTION] form=`(contains? #{1 2 3} 2)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(contains? #{1 2 3} 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [BOOL_LEAK_RESOLUTION] form=`(contains? #{1 2 3} 4)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(contains? #{1 2 3} 4)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G4-13: count — universal

- examples: 4
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'LOW_GROUNDING': 4, 'EMPTY_GOAL_RENDERED': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3 4 5])` — sentence with 5 commas reads as AI-output cadence: 'Carol laid out five fleeces in a wool-basket, weight-tagged 1, 2, 3, 4, 5'
    - [LOW_GROUNDING] form=`(count [1 2 3 4 5])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count [1 2 3 4 5])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count {:a 1 :b 2})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count #{:a :b :c})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(count "shepherd")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G4-14: empty?

- examples: 3
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'LOW_GROUNDING': 3}
    - [BOOL_LEAK_RESOLUTION] form=`(empty? [])` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(empty? [])` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(empty? [])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(empty? [1])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(empty? [1])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-15: first, rest, last

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'NARRATIVE_NUMERAL_HARDCODE': 6, 'LOW_GROUNDING': 3, 'EMPTY_GOAL_RENDERED': 2, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(first [10 20 30])` — sentence with 5 commas reads as AI-output cadence: 'To get the first element of a vector containing 10, 20, and 30 properly, he wrot'
    - [CLAUSE_STACK_OVERFLOW] form=`(first [10 20 30])` — sentence with 5 commas reads as AI-output cadence: 'To get the first element of a vector containing 10, 20, and 30 properly, he wrot'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(last  [10 20 30])` — parametric example has hard-coded English numeral 'three bundles' in a story slot — the actual draws may differ from this fixed count
    - [LOW_GROUNDING] form=`(last  [10 20 30])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(last  [10 20 30])` — parametric example has hard-coded English numeral 'three bundles' in a story slot — the actual draws may differ from this fixed count
    - [LOW_GROUNDING] form=`(last  [10 20 30])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-16: into and conj on collections

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CLAUSE_STACK_OVERFLOW': 2}
    - [LOW_GROUNDING] form=`(into [] '(1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] '(1 2 3))` — sentence with 6 commas reads as AI-output cadence: 'Margarethe shook her head and went on\nwith the work: to convert a list containin'
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] '(1 2 3))` — sentence with 5 commas reads as AI-output cadence: 'To convert a list containing 1, 2, and 3 into a vector, he composed building a v'
    - [LOW_GROUNDING] form=`(into #{} [1 2 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(into #{} [1 2 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-17: Immutability — assoc returns new

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(let [m {:a 1}] (assoc m :a 99) m)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [m {:a 1}] (assoc m :a 99) m)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-18: Equality of vectors and lists

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'BOOL_LEAK_RESOLUTION': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'LOW_GROUNDING': 2}
    - [HIGH_LENGTH] form=`(= [1 2 3] '(1 2 3))` — user_msg 213 words
    - [BOOL_LEAK_RESOLUTION] form=`(= [1 2 3] '(1 2 3))` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(= [1 2 3] '(1 2 3))` — parametric example has hard-coded English numeral 'three items' in a story slot — the actual draws may differ from this fixed count
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(= [1 2 3] '(1 2 3))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(= [1 2 3] '(1 2 3))` — parametric example has hard-coded English numeral 'three items' in a story slot — the actual draws may differ from this fixed count
    - [LOW_GROUNDING] form=`(= [1 2 3] '(1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-19: range and seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'LOW_GROUNDING': 2}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (range 5))` — parametric example has hard-coded English numeral 'five numbers' in a story slot — the actual draws may differ from this fixed count
    - [LOW_GROUNDING] form=`(count (range 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (range 5))` — parametric example has hard-coded English numeral 'five numbers' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (range 5))` — parametric example has hard-coded English numeral 'five numbers' in a story slot — the actual draws may differ from this fixed count
    - [LOW_GROUNDING] form=`(count (range 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-20: Collection vs sequence

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'LOW_GROUNDING': 2}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (seq [1 2 3]))` — parametric example has hard-coded English numeral 'three items' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (seq [1 2 3]))` — parametric example has hard-coded English numeral 'three items' in a story slot — the actual draws may differ from this fixed count
    - [LOW_GROUNDING] form=`(count (seq [1 2 3]))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (seq [1 2 3]))` — parametric example has hard-coded English numeral 'three items' in a story slot — the actual draws may differ from this fixed count
    - [LOW_GROUNDING] form=`(count (seq [1 2 3]))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 5

### G5-01: if

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'CLAUSE_STACK_OVERFLOW': 1, 'HIGH_LENGTH': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [LOW_GROUNDING] form=`(if true :a :b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(if true :a :b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(if false :a :b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(if false :a :b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(if false :a :b)` — sentence with 5 commas reads as AI-output cadence: 'The runtime checks the condition, walks the right arm,\nand the unwalked arm is j'
    - [HIGH_LENGTH] form=`(if (> 5 3) :a :b)` — user_msg 203 words

### G5-03: when

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'ANSWER_LEAK_STRING': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'LOW_GROUNDING': 5, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(when true :yes)` — user_msg 212 words
    - [ANSWER_LEAK_STRING] form=`(when true :yes)` — answer string ':yes' appears in user_msg
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(when true :yes)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(when true :yes)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(when true :yes)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(when true :yes)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G5-04: cond

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — sentence with 5 commas reads as AI-output cadence: 'Whatever the condition evaluates to, that decides." To walk three condition-ston'

### G5-05: cond — :else

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(cond false :a false :b :else :c)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(cond false :a false :b :else :c)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(cond false :a false :b :else :c)` — sentence with 5 commas reads as AI-output cadence: 'The runtime checks the condition, walks the right arm,\nand the unwalked arm is j'

### G5-06: case

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'ANSWER_LEAK_STRING': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'LOW_GROUNDING': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(case 2 1 :one 2 :two 3 :three :default)` — user_msg 206 words
    - [ANSWER_LEAK_STRING] form=`(case 2 1 :one 2 :two 3 :three :default)` — answer string ':two' appears in user_msg
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(case 2 1 :one 2 :two 3 :three :default)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(case 2 1 :one 2 :two 3 :three :default)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(case 99 1 :one 2 :two :default)` — sentence with 5 commas reads as AI-output cadence: 'The runtime checks the condition, walks the right arm,\nand the unwalked arm is j'

### G5-07: and / or as control flow

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'LOW_GROUNDING': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(and 1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'An empty bucket, a zero-tally, a sleeping\nflock — every one of those still swing'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(or nil false :found)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [LOW_GROUNDING] form=`(or nil false :found)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PARAGRAPH_FRAGMENTATION] form=`(or nil false :found)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(or nil false :found)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(or nil false :found)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count

### G5-08: not

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(not (> 1 2))` — sentence with 5 commas reads as AI-output cadence: 'To negate the result of checking whether 9 is greater than 1, she\ncomposed the n'
    - [CLAUSE_STACK_OVERFLOW] form=`(not (> 1 2))` — sentence with 5 commas reads as AI-output cadence: 'An empty bucket, a zero-tally, a sleeping\nflock — every one of those still swing'

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
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 5, 'STORY_RESOLUTION_NO_DRAWN': 3, 'PARAGRAPH_FRAGMENTATION': 1}
    - [HIGH_LENGTH] form=`(map inc [1 2 3])` — user_msg 253 words
    - [CLAUSE_STACK_OVERFLOW] form=`(map inc [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'To pour the vector containing 1, 2, 3 through a sieve whose rule is inc, collect'
    - [CLAUSE_STACK_OVERFLOW] form=`(map inc [1 2 3])` — sentence with 7 commas reads as AI-output cadence: 'Romualda shook her head and went on\nwith the work: to pour the vector containing'
    - [CLAUSE_STACK_OVERFLOW] form=`(map inc [1 2 3])` — sentence with 7 commas reads as AI-output cadence: 'Cassandra shook her head and went on\nwith the work: to pour the vector containin'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map #(* % %) [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(map #(* % %) [1 2 3 4])` — sentence with 8 commas reads as AI-output cadence: 'Romualda shook her head and went on\nwith the work: to apply a squaring operation'

### G5-11: filter

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'PARAGRAPH_FRAGMENTATION': 1, 'CLAUSE_STACK_OVERFLOW': 2}
    - [LOW_GROUNDING] form=`(filter even? [1 2 3 4])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PARAGRAPH_FRAGMENTATION] form=`(filter even? [1 2 3 4])` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [CLAUSE_STACK_OVERFLOW] form=`(filter even? [1 2 3 4])` — sentence with 6 commas reads as AI-output cadence: 'To keep the even elements from the vector containing 1, 2, 3, and 4, he composed'
    - [CLAUSE_STACK_OVERFLOW] form=`(filter pos? [-2 -1 0 1 2])` — sentence with 8 commas reads as AI-output cadence: 'Magnus shook his head and went on\nwith the work: to keep the positive elements f'
    - [LOW_GROUNDING] form=`(filter pos? [-2 -1 0 1 2])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(filter pos? [-2 -1 0 1 2])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G5-12: reduce

- examples: 3
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 1, 'ANSWER_LEAK': 1, 'PARAGRAPH_FRAGMENTATION': 3, 'CLAUSE_STACK_OVERFLOW': 6, 'ONLY_SHOOK_HEAD_TIC': 1, 'LOW_GROUNDING': 1}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(reduce + [1 2 3 4])` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [ANSWER_LEAK] form=`(reduce + [1 2 3 4])` — answer 10 in narrative
    - [PARAGRAPH_FRAGMENTATION] form=`(reduce + [1 2 3 4])` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + [1 2 3 4])` — sentence with 5 commas reads as AI-output cadence: 'To walk the row of pebbles 1, 2, 3, 4 carrying a tally that combines each with +'
    - [ONLY_SHOOK_HEAD_TIC] form=`(reduce + [1 2 3 4])` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [PARAGRAPH_FRAGMENTATION] form=`(reduce * [1 2 3 4 5])` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G5-13: reduce with init

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'ANSWER_LEAK': 1, 'SENTENCE_START_LOWER_PRONOUN': 2, 'CLAUSE_STACK_OVERFLOW': 1, 'ONLY_SHOOK_HEAD_TIC': 1}
    - [HIGH_LENGTH] form=`(reduce + 100 [1 2 3])` — user_msg 229 words
    - [ANSWER_LEAK] form=`(reduce + 100 [1 2 3])` — answer 106 in narrative
    - [SENTENCE_START_LOWER_PRONOUN] form=`(reduce + 100 [1 2 3])` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + 100 [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'The runtime does this the same way for any kind of collection."\nTo fold + over t'
    - [SENTENCE_START_LOWER_PRONOUN] form=`(reduce + 0 [])` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [ONLY_SHOOK_HEAD_TIC] form=`(reduce + 0 [])` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

### G5-14: apply

- examples: 2
- variety @ n=50: 1.00
- issues: {'PARAGRAPH_FRAGMENTATION': 1, 'LOW_GROUNDING': 4, 'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [PARAGRAPH_FRAGMENTATION] form=`(apply + [1 2 3 4])` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [LOW_GROUNDING] form=`(apply + [1 2 3 4])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(apply + [1 2 3 4])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply max [3 1 4 1 5])` — parametric example has hard-coded English numeral 'five numbers' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply max [3 1 4 1 5])` — parametric example has hard-coded English numeral 'five numbers' in a story slot — the actual draws may differ from this fixed count
    - [LOW_GROUNDING] form=`(apply max [3 1 4 1 5])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G5-15: comp

- examples: 2
- variety @ n=50: 0.99
- issues: {'CONCEPT_AS_VERB': 3, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CONCEPT_AS_VERB] form=`((comp inc inc) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`((comp inc inc) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`((comp inc inc) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`((comp inc inc) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((comp inc inc) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`((comp str inc) 9)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G5-16: partial

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'HIGH_LENGTH': 1}
    - [CONCEPT_AS_VERB] form=`((partial + 10) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CLAUSE_STACK_OVERFLOW] form=`(map (partial * 3) [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'The earlier steps prepare the way; the last\nstep is the answer." To apply a part'
    - [HIGH_LENGTH] form=`(map (partial * 3) [1 2 3])` — user_msg 224 words

### G5-17: juxt

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CONCEPT_AS_VERB': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`((juxt inc dec) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`((juxt inc dec) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`((juxt inc dec) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((juxt inc dec) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`((juxt inc dec) 5)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G5-18: some

- examples: 2
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 1, 'PARAGRAPH_FRAGMENTATION': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'LOW_GROUNDING': 2}
    - [BOOL_LEAK_RESOLUTION] form=`(some even? [1 3 5 8 7])` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [PARAGRAPH_FRAGMENTATION] form=`(some even? [1 3 5 8 7])` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [CLAUSE_STACK_OVERFLOW] form=`(some even? [1 3 5 8 7])` — sentence with 7 commas reads as AI-output cadence: 'To check if any element in the vector containing 1, 3, 5, 8, and 7 is even, she '
    - [LOW_GROUNDING] form=`(some neg? [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(some neg? [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G5-19: every?

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'LOW_GROUNDING': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(every? pos? [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'Octavia shook her head and went on\nwith the work: to check if all elements in th'
    - [LOW_GROUNDING] form=`(every? pos? [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(every? even? [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'Diogenes shook his head and went on\nwith the work: to check if all elements in t'
    - [LOW_GROUNDING] form=`(every? even? [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G5-20: take and drop

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(drop 2 [10 20 30 40 50])` — sentence with 8 commas reads as AI-output cadence: 'Octavia shook her head and went on\nwith the work: to drop the first 2 elements f'
    - [CLAUSE_STACK_OVERFLOW] form=`(drop 2 [10 20 30 40 50])` — sentence with 8 commas reads as AI-output cadence: 'Gerhardt shook his head and went on\nwith the work: to drop the first 2 elements '

### G5-21: distinct and sort

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 5}
    - [CLAUSE_STACK_OVERFLOW] form=`(distinct [1 1 2 3 3 4])` — sentence with 5 commas reads as AI-output cadence: 'Write a form whose evaluation gives the sequence produced by passing 1, 1, 2, 3,'
    - [CLAUSE_STACK_OVERFLOW] form=`(distinct [1 1 2 3 3 4])` — sentence with 5 commas reads as AI-output cadence: 'What Clojure form computes the sequence produced by passing 1, 1, 2, 3, 3, 4 thr'
    - [CLAUSE_STACK_OVERFLOW] form=`(distinct [1 1 2 3 3 4])` — sentence with 8 commas reads as AI-output cadence: 'To remove duplicate elements from the vector containing 1, 1, 2, 3, 3, and 4, he'
    - [CLAUSE_STACK_OVERFLOW] form=`(sort [3 1 2])` — sentence with 6 commas reads as AI-output cadence: 'Romualda shook her head and went on\nwith the work: to sort the vector containing'
    - [CLAUSE_STACK_OVERFLOW] form=`(sort [3 1 2])` — sentence with 5 commas reads as AI-output cadence: 'To sort the vector containing 3, 1, and 2 in ascending order, she composed sorti'

### G5-22: recur — first taste

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — sentence with 5 commas reads as AI-output cadence: 'To walk a small circuit five times, multiplying a running tally by the current s'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — sentence with 6 commas reads as AI-output cadence: 'With one, the\nwalker knows when the circuit is done and the answer is the final\n'

## Grade 6

### G6-01: Namespace as file

- examples: 3
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 8, 'ANSWER_LEAK_STRING': 1, 'PARAGRAPH_FRAGMENTATION': 5, 'EMPTY_GOAL_RENDERED': 3, 'BOOL_LEAK_RESOLUTION': 2}
    - [LOW_GROUNDING] form=`(name 'foo.bar)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name 'foo.bar)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [ANSWER_LEAK_STRING] form=`(name 'foo.bar)` — answer string 'foo.bar' appears in user_msg
    - [LOW_GROUNDING] form=`(name 'foo.bar)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PARAGRAPH_FRAGMENTATION] form=`(name 'foo.bar)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [LOW_GROUNDING] form=`(name 'clojure.string)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-02: ns form

- examples: 2
- variety @ n=50: 1.00
- issues: {'EMPTY_GOAL_RENDERED': 5, 'LOW_GROUNDING': 5}
    - [EMPTY_GOAL_RENDERED] form=`(name 'village.shepherd)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [LOW_GROUNDING] form=`(name 'village.shepherd)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name 'village.shepherd)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(name 'village.shepherd)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [LOW_GROUNDING] form=`(= 'village.shepherd 'village.shepherd)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(= 'village.shepherd 'village.shepherd)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G6-03: require

- examples: 2
- variety @ n=50: 1.00
- issues: {'EMPTY_GOAL_RENDERED': 6, 'LOW_GROUNDING': 3}
    - [EMPTY_GOAL_RENDERED] form=`(clojure.string/upper-case "wolf")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(clojure.string/upper-case "wolf")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(clojure.string/upper-case "wolf")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [LOW_GROUNDING] form=`(clojure.string/lower-case "WOLF")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(clojure.string/lower-case "WOLF")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [LOW_GROUNDING] form=`(clojure.string/lower-case "WOLF")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-04: refer and use

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'HIGH_LENGTH': 1, 'BOOL_LEAK_RESOLUTION': 1}
    - [LOW_GROUNDING] form=`(= (clojure.string/upper-case "x") (clojure.string` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(= (clojure.string/upper-case "x") (clojure.string` — user_msg 201 words
    - [BOOL_LEAK_RESOLUTION] form=`(= (clojure.string/upper-case "x") (clojure.string` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead

### G6-05: Fully qualified names

- examples: 4
- variety @ n=50: 1.00
- issues: {'EMPTY_GOAL_RENDERED': 10, 'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [EMPTY_GOAL_RENDERED] form=`(clojure.string/upper-case "shepherd")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(clojure.string/upper-case "shepherd")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/reverse "flock")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('flock',), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(clojure.string/reverse "flock")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/reverse "flock")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('flock',), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(clojure.string/reverse "flock")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'BOOL_LEAK_RESOLUTION': 1, 'VILLAGE_NOUN_OVERUSE': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta '^:private hidden)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private', ':private'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta '^:private hidden)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private', ':private'), resolution doesn't close the loop)
    - [BOOL_LEAK_RESOLUTION] form=`(boolean (:private (meta '^:private hidden)))` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta '^:private hidden)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private', ':private'), resolution doesn't close the loop)
    - [VILLAGE_NOUN_OVERUSE] form=`(boolean (:private (meta '^:private hidden)))` — `the village` appears 4 times (noun-saturation tic — vary or drop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta 'public)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private',), resolution doesn't close the loop)

### G6-08: Circular dependencies

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(clojure.string/upper-case "a")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.string/upper-case "a")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 'a.b 'a.b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 'a.b 'a.b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 'a.b 'a.b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-09: Loading order

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a 1 b (+ a 1)] (+ a b))` — sentence with 6 commas reads as AI-output cadence: 'To bind a to 1, bind b to a plus 1, then return the sum of a and b, the notice h'
    - [LOW_GROUNDING] form=`(let [a 1 b (+ a 1)] (+ a b))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [a 1 b (+ a 1)] (+ a b))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-10: Leiningen and deps.edn

- examples: 2
- variety @ n=50: 1.00
- issues: {'PATIENT_ROLE_BOASTFUL': 3, 'VILLAGE_NOUN_OVERUSE': 2, 'LOW_GROUNDING': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [PATIENT_ROLE_BOASTFUL] form=`(:deps {:deps {:a 1 :b 2}})` — patient role 'the elder' co-occurs with boastful EMO phrase 'with great whoops of laughter'
    - [VILLAGE_NOUN_OVERUSE] form=`(:deps {:deps {:a 1 :b 2}})` — `the village` appears 4 times (noun-saturation tic — vary or drop)
    - [LOW_GROUNDING] form=`(:deps {:deps {:a 1 :b 2}})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(:deps {:deps {:a 1 :b 2}})` — sentence with 6 commas reads as AI-output cadence: 'To extract the value at the :deps key from a nested map,\nthe elder, letting the '
    - [PATIENT_ROLE_BOASTFUL] form=`(get-in {:paths ["src"]} [:paths 0])` — patient role 'the elder' co-occurs with boastful EMO phrase 'with the swagger of an unrepen'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(get-in {:paths ["src"]} [:paths 0])` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':paths', ':paths', 'src'), resolution doesn't close the loop)

### G6-11: Classpath

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(clojure.string/split "src:test" #":")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "src:test" #":")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':test', 'src:test'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "src:test" #":")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':test', 'src:test'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(clojure.string/split "src:test" #":")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "src:test" #":")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':test', 'src:test'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count ["src" "test" "resources"])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('src', 'test', 'resources'), resolution doesn't close the loop)

### G6-12: Multiple files in one project

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'EMPTY_GOAL_RENDERED': 4}
    - [LOW_GROUNDING] form=`(count ['village.shepherd 'village.elder 'village.` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(count ['village.shepherd 'village.elder 'village.` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [LOW_GROUNDING] form=`(count ['village.shepherd 'village.elder 'village.` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(count ['village.shepherd 'village.elder 'village.` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(count ['village.shepherd 'village.elder 'village.` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [LOW_GROUNDING] form=`(map name ['village.shepherd 'village.elder])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-13: Aliasing conventions

- examples: 1
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2, 'EMPTY_GOAL_RENDERED': 3, 'PARAGRAPH_FRAGMENTATION': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [s clojure.string/upper-case] (s "wolf"))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [EMPTY_GOAL_RENDERED] form=`(let [s clojure.string/upper-case] (s "wolf"))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [PARAGRAPH_FRAGMENTATION] form=`(let [s clojure.string/upper-case] (s "wolf"))` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [EMPTY_GOAL_RENDERED] form=`(let [s clojure.string/upper-case] (s "wolf"))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [s clojure.string/upper-case] (s "wolf"))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [EMPTY_GOAL_RENDERED] form=`(let [s clojure.string/upper-case] (s "wolf"))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G6-14: Import for host classes

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'EMPTY_GOAL_RENDERED': 4, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(symbol? 'java.util.Date)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(symbol? 'java.util.Date)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [LOW_GROUNDING] form=`(symbol? 'java.util.Date)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(symbol? 'java.util.Date)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [LOW_GROUNDING] form=`(name 'java.util.Date)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(name 'java.util.Date)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G6-15: Namespace meta

- examples: 2
- variety @ n=50: 0.99
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'EMPTY_GOAL_RENDERED': 6, 'ONLY_SHOOK_HEAD_TIC': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:doc (meta '^{:doc "trust the runtime"} village))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':doc', ':doc', 'trust the runtime'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(:doc (meta '^{:doc "trust the runtime"} village))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:doc (meta '^{:doc "trust the runtime"} village))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':doc', ':doc', 'trust the runtime'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(:doc (meta '^{:doc "trust the runtime"} village))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:doc (meta '^{:doc "trust the runtime"} village))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':doc', ':doc', 'trust the runtime'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(:doc (meta '^{:doc "trust the runtime"} village))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G6-16: Cleaning up requires

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'BOOL_LEAK_RESOLUTION': 1}
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.string)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.set)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.set)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [BOOL_LEAK_RESOLUTION] form=`(contains? #{'clojure.string} 'clojure.set)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.set)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 7

### G7-01: throw

- examples: 1
- variety @ n=50: 0.98
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'EMPTY_GOAL_RENDERED': 2, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "bad")) (catch Exception e` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':thrown', 'bad'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(try (throw (Exception. "bad")) (catch Exception e` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "bad")) (catch Exception e` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':thrown', 'bad'), resolution doesn't close the loop)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(try (throw (Exception. "bad")) (catch Exception e` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "bad")) (catch Exception e` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':thrown', 'bad'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(try (throw (Exception. "bad")) (catch Exception e` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G7-02: try / catch

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'EMPTY_GOAL_RENDERED': 2}
    - [LOW_GROUNDING] form=`(try (/ 1 0) (catch Exception e :caught))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(try (/ 1 0) (catch Exception e :caught))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [LOW_GROUNDING] form=`(try (/ 1 0) (catch Exception e :caught))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(try (/ 1 0) (catch Exception e :caught))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [LOW_GROUNDING] form=`(try (/ 1 0) (catch Exception e :caught))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try 42 (catch Exception e :caught))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-03: try / finally

- examples: 2
- variety @ n=50: 0.99
- issues: {'EMPTY_GOAL_RENDERED': 6}
    - [EMPTY_GOAL_RENDERED] form=`(try 7 (finally :cleanup))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(try 7 (finally :cleanup))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(try 7 (finally :cleanup))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(try (try (/ 1 0) (finally :ran)) (catch Exception` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(try (try (/ 1 0) (finally :ran)) (catch Exception` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(try (try (/ 1 0) (finally :ran)) (catch Exception` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G7-04: ex-info

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 2}
    - [LOW_GROUNDING] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', 'bad'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', 'bad'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', 'bad'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(try (throw (ex-info "x" {:k :v})) (catch Exceptio` — sentence with 5 commas reads as AI-output cadence: 'To throw an ex-info with data, catch it, and extract the value at key :k require'

### G7-05: nil punning

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 9, 'BOOL_LEAK_RESOLUTION': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [LOW_GROUNDING] form=`(some? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(some? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(some? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [BOOL_LEAK_RESOLUTION] form=`(some? 0)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(some? 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(some? 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-06: pre and post conditions

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'EMPTY_GOAL_RENDERED': 3}
    - [LOW_GROUNDING] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exce` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exce` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exce` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G7-07: assert

- examples: 2
- variety @ n=50: 1.00
- issues: {'EMPTY_GOAL_RENDERED': 6, 'CLAUSE_STACK_OVERFLOW': 1}
    - [EMPTY_GOAL_RENDERED] form=`(do (assert (= 1 1)) :ok)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(do (assert (= 1 1)) :ok)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(do (assert (= 1 1)) :ok)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(try (assert (= 1 2)) (catch Throwable e :asserted` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(try (assert (= 1 2)) (catch Throwable e :asserted` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [CLAUSE_STACK_OVERFLOW] form=`(try (assert (= 1 2)) (catch Throwable e :asserted` — sentence with 5 commas reads as AI-output cadence: 'To , she composed an assert that fails, caught by surrounding try, placed\nthe fo'

### G7-08: prn and pprint

- examples: 2
- variety @ n=50: 1.00
- issues: {'ONLY_SHOOK_HEAD_TIC': 2, 'EMPTY_GOAL_RENDERED': 2}
    - [ONLY_SHOOK_HEAD_TIC] form=`(with-out-str (prn 42))` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [EMPTY_GOAL_RENDERED] form=`(with-out-str (prn :wolf))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(with-out-str (prn :wolf))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [ONLY_SHOOK_HEAD_TIC] form=`(with-out-str (prn :wolf))` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

### G7-09: tap>

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'BOOL_LEAK_RESOLUTION': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'LOW_GROUNDING': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(tap> :hello)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hello',), resolution doesn't close the loop)
    - [BOOL_LEAK_RESOLUTION] form=`(tap> :hello)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(tap> :hello)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(tap> :hello)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hello',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(tap> :hello)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(tap> :hello)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hello',), resolution doesn't close the loop)

### G7-10: doc and source

- examples: 1
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [ANSWER_LEAK_STRING] form=`(:doc (meta '^{:doc "adds two"} plus))` — answer string 'adds two' appears in user_msg
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(:doc (meta '^{:doc "adds two"} plus))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G7-11: Reading stack traces

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 6, 'PARAGRAPH_FRAGMENTATION': 1}
    - [LOW_GROUNDING] form=`(try (throw (Exception. "oops")) (catch Exception ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(try (throw (Exception. "oops")) (catch Exception ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(try (throw (Exception. "oops")) (catch Exception ` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [LOW_GROUNDING] form=`(try (throw (Exception. "oops")) (catch Exception ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-12: slurp and spit

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'EMPTY_GOAL_RENDERED': 3, 'ONLY_SHOOK_HEAD_TIC': 3, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(count "wolf\nshepherd\n")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(count "wolf\nshepherd\n")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(count "wolf\nshepherd\n")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [ONLY_SHOOK_HEAD_TIC] form=`(count "wolf\nshepherd\n")` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [LOW_GROUNDING] form=`(count "wolf\nshepherd\n")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(count "wolf\nshepherd\n")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G7-13: line-seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'SMALL_INT_LEAK': 1, 'STORY_RESOLUTION_NO_DRAWN': 6, 'PARAGRAPH_FRAGMENTATION': 1, 'LOW_GROUNDING': 5, 'ONLY_SHOOK_HEAD_TIC': 2}
    - [SMALL_INT_LEAK] form=`(count (clojure.string/split-lines "a\nb\nc"))` — small-int answer 3 leaks via resolution-slot phrasing
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [ONLY_SHOOK_HEAD_TIC] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

### G7-14: with-open

- examples: 1
- variety @ n=50: 1.00
- issues: {'EMPTY_GOAL_RENDERED': 3, 'PARAGRAPH_FRAGMENTATION': 1}
    - [EMPTY_GOAL_RENDERED] form=`(with-out-str (println "wolf"))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [PARAGRAPH_FRAGMENTATION] form=`(with-out-str (println "wolf"))` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [EMPTY_GOAL_RENDERED] form=`(with-out-str (println "wolf"))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(with-out-str (println "wolf"))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G7-15: *in* and *out*

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 5, 'ONLY_SHOOK_HEAD_TIC': 1}
    - [LOW_GROUNDING] form=`(with-out-str (print "x"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (print "x"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (print "x"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (println))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [ONLY_SHOOK_HEAD_TIC] form=`(with-out-str (println))` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [LOW_GROUNDING] form=`(with-out-str (println))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-16: edn read

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'ONLY_SHOOK_HEAD_TIC': 1, 'EMPTY_GOAL_RENDERED': 2}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [ONLY_SHOOK_HEAD_TIC] form=`(clojure.edn/read-string "42")` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [EMPTY_GOAL_RENDERED] form=`(clojure.edn/read-string "[:wolf :flock]")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(clojure.edn/read-string "[:wolf :flock]")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G7-17: JSON roundtrip

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'PARAGRAPH_FRAGMENTATION': 1, 'ONLY_SHOOK_HEAD_TIC': 1}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PARAGRAPH_FRAGMENTATION] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [ONLY_SHOOK_HEAD_TIC] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-18: Shell command

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6}
    - [LOW_GROUNDING] form=`(:cmd {:cmd "ls" :args ["-l"]})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(:cmd {:cmd "ls" :args ["-l"]})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(:cmd {:cmd "ls" :args ["-l"]})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count (:args {:cmd "echo" :args ["hello" "world"]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count (:args {:cmd "echo" :args ["hello" "world"]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count (:args {:cmd "echo" :args ["hello" "world"]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 8

### G8-01: Why polymorphism

- examples: 2
- variety @ n=50: 0.99
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'EMPTY_GOAL_RENDERED': 6, 'HIGH_LENGTH': 1, 'LOW_GROUNDING': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :wolf) "howl" (= k :flo` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':wolf', ':flock', ':else'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(defn speak [k] (cond (= k :wolf) "howl" (= k :flo` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :wolf) "howl" (= k :flo` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':wolf', ':flock', ':else'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(defn speak [k] (cond (= k :wolf) "howl" (= k :flo` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [HIGH_LENGTH] form=`(defn speak [k] (cond (= k :wolf) "howl" (= k :flo` — user_msg 208 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :wolf) "howl" (= k :flo` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':wolf', ':flock', ':else'), resolution doesn't close the loop)

### G8-02: deftype introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 2}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do (deftype Lantern [color]) (.-color (Lantern. "` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Lantern [color]) (.-color (Lantern. "` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('amber',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (deftype Lantern [color]) (.-color (Lantern. "` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Lantern [color]) (.-color (Lantern. "` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('amber',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (deftype Lantern [color]) (.-color (Lantern. "` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Lantern [color]) (.-color (Lantern. "` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('amber',), resolution doesn't close the loop)

### G8-03: defrecord introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'SENTENCE_START_LOWER_PRONOUN': 1, 'ANSWER_LEAK_STRING': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defrecord Watcher [name post]) (:post (->Watc` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':post', ':hilltop', 'shepherd'), resolution doesn't close the loop)
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do (defrecord Watcher [name post]) (:post (->Watc` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defrecord Watcher [name post]) (:post (->Watc` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':post', ':hilltop', 'shepherd'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defrecord Watcher [name post]) (:post (->Watc` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':post', ':hilltop', 'shepherd'), resolution doesn't close the loop)
    - [ANSWER_LEAK_STRING] form=`(do (defrecord Watcher [name post]) (:name (->Watc` — answer string 'elder' appears in user_msg
    - [ANSWER_LEAK_STRING] form=`(do (defrecord Watcher [name post]) (:name (->Watc` — answer string 'elder' appears in user_msg

### G8-04: Protocol definition

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(do (defprotocol Alarm (sound [this])) (some? Alar` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Alarm (sound [this])) (some? Alar` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Alarm (sound [this])) (some? Alar` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Greet (hail [this])) (some? Greet` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Greet (hail [this])) (some? Greet` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-05: Protocol extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1, 'HONEST_JUDGE_REPEAT': 1, 'LOW_GROUNDING': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [ANSWER_LEAK_STRING] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — answer string ':number' appears in user_msg
    - [HONEST_JUDGE_REPEAT] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    - [LOW_GROUNDING] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol named Greet with one method hail, extend it to Long type wi'
    - [LOW_GROUNDING] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-06: Protocol method dispatch

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 1, 'LOW_GROUNDING': 3, 'PARAGRAPH_FRAGMENTATION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Alarm (sound [this])) (extend-pro` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-alarm', ':long-alarm'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Alarm (sound [this])) (extend-pro` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-alarm', ':long-alarm'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Alarm (sound [this])) (extend-pro` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-alarm', ':long-alarm'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Alarm (sound [this])) (extend-pro` — sentence with 5 commas reads as AI-output cadence: "The runtime looks up which species the shepherd is, then runs that\nspecies' answ"
    - [LOW_GROUNDING] form=`(do (defprotocol Alarm (sound [this])) (extend-pro` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Alarm (sound [this])) (extend-pro` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':string-alarm', ':long-alarm'), resolution doesn't close the loop)

### G8-07: Record implementing protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'HONEST_JUDGE_REPEAT': 1}
    - [ANSWER_LEAK_STRING] form=`(do (defprotocol Alarm (sound [this])) (defrecord ` — answer string ':cry' appears in user_msg
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Alarm (sound [this])) (defrecord ` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':cry', 'Pip'), resolution doesn't close the loop)
    - [ANSWER_LEAK_STRING] form=`(do (defprotocol Alarm (sound [this])) (defrecord ` — answer string ':cry' appears in user_msg
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Alarm (sound [this])) (defrecord ` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':cry', 'Pip'), resolution doesn't close the loop)
    - [ANSWER_LEAK_STRING] form=`(do (defprotocol Alarm (sound [this])) (defrecord ` — answer string ':cry' appears in user_msg
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Alarm (sound [this])) (defrecord ` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':cry', 'Pip'), resolution doesn't close the loop)

### G8-08: Multimethod defmulti

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti reply :role) (defmethod reply :sheph` — sentence with 6 commas reads as AI-output cadence: 'The runtime reads it, finds the matching pen,\nand routes that one." To find what'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti reply :role) (defmethod reply :sheph` — sentence with 6 commas reads as AI-output cadence: 'The runtime reads it, finds the matching pen,\nand routes that one." To find what'

### G8-09: Multimethod defmethod

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4, 'ANSWER_LEAK_STRING': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti reply :role) (defmethod reply :sheph` — sentence with 5 commas reads as AI-output cadence: 'To find what reply returns for {:role :elder}, she composed\ntwo defmethod entrie'
    - [ANSWER_LEAK_STRING] form=`(do (defmulti reply :role) (defmethod reply :sheph` — answer string ':measured' appears in user_msg
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti reply :role) (defmethod reply :sheph` — sentence with 5 commas reads as AI-output cadence: 'To find what reply returns for {:role :stranger} when :default falls through, sh'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti reply :role) (defmethod reply :sheph` — sentence with 6 commas reads as AI-output cadence: 'The runtime reads it, finds the matching pen,\nand routes that one." To find what'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti reply :role) (defmethod reply :sheph` — sentence with 5 commas reads as AI-output cadence: 'To find what reply returns for {:role :stranger} when :default falls through, he'

### G8-10: Multimethod vs protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [ANSWER_LEAK_STRING] form=`(do (defmulti show identity) (defmethod show :wolf` — answer string 'howl' appears in user_msg
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti show identity) (defmethod show :wolf` — sentence with 5 commas reads as AI-output cadence: 'The dispatch\nfunction is the reader; the gate is the router." To compute the str'

### G8-11: Protocol vs Java interface

- examples: 1
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(do (defprotocol IAlarm (raise [this])) (extend-pr` — answer string ':raised' appears in user_msg

### G8-12: extend-type on built-in types

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Alarm (sound [this])) (extend-typ` — sentence with 5 commas reads as AI-output cadence: 'The dispatch\nfunction is the reader; the gate is the router." To compute the key'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Alarm (sound [this])) (extend-typ` — sentence with 5 commas reads as AI-output cadence: 'To compute the keyword sound returns for 5, she composed\nextend-type used to att'

### G8-13: this-style vs fn-style

- examples: 2
- variety @ n=50: 0.99
- issues: {'ANSWER_LEAK_STRING': 1, 'WRONG_FABLE_LITERAL': 1, 'LOW_GROUNDING': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [ANSWER_LEAK_STRING] form=`(do (defprotocol Named (name-of [this])) (defrecor` — answer string 'Pip' appears in user_msg
    - [WRONG_FABLE_LITERAL] form=`(do (defprotocol Named (name-of [this])) (defrecor` — tortoise-hare ghost name 'Pip' appears in boy-wolf user_msg
    - [LOW_GROUNDING] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Tagged (tag-of [this])) (defrecor` — sentence with 5 commas reads as AI-output cadence: "The runtime looks up which species the shepherd is, then runs that\nspecies' answ"

### G8-14: Protocols don't inherit

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3, 'PARAGRAPH_FRAGMENTATION': 1, 'CLAUSE_STACK_OVERFLOW': 2}
    - [LOW_GROUNDING] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [LOW_GROUNDING] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — sentence with 8 commas reads as AI-output cadence: "The runtime looks up which species the shepherd is, then runs that\nspecies' answ"

### G8-15: derive and isa? — multimethod hierarchy

- examples: 3
- variety @ n=50: 0.99
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'EMPTY_GOAL_RENDERED': 3, 'CLAUSE_STACK_OVERFLOW': 2, 'LOW_GROUNDING': 6, 'BOOL_LEAK_RESOLUTION': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (derive ::shepherd ::villager) (isa? ::shepher` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':shepherd', ':villager', ':shepherd'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(do (derive ::shepherd ::villager) (isa? ::shepher` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (derive ::shepherd ::villager) (isa? ::shepher` — sentence with 5 commas reads as AI-output cadence: 'The runtime reads it, finds the matching pen,\nand routes that one." To , he\ncomp'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (derive ::shepherd ::villager) (isa? ::shepher` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':shepherd', ':villager', ':shepherd'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(do (derive ::shepherd ::villager) (isa? ::shepher` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (derive ::shepherd ::villager) (isa? ::shepher` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':shepherd', ':villager', ':shepherd'), resolution doesn't close the loop)

### G8-16: Abstract design with protocols

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'LOW_GROUNDING': 3, 'ANSWER_LEAK_STRING': 1, 'HONEST_JUDGE_REPEAT': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Watch (look [this])) (defrecord S` — sentence with 6 commas reads as AI-output cadence: "The runtime looks up which species the shepherd is, then runs that\nspecies' answ"
    - [LOW_GROUNDING] form=`(do (defprotocol Watch (look [this])) (defrecord S` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Sound (cry [this])) (defrecord Sh` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Sound (cry [this])) (defrecord Sh` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [ANSWER_LEAK_STRING] form=`(do (defprotocol Sound (cry [this])) (defrecord Sh` — answer string ':calm' appears in user_msg
    - [HONEST_JUDGE_REPEAT] form=`(do (defprotocol Sound (cry [this])) (defrecord Sh` — two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)

## Grade 9

### G9-01: Immutability as default — review

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(let [m {:a 1}] (assoc m :b 2) m)` — sentence with 7 commas reads as AI-output cadence: 'To bind a map m, call assoc to add :b 0 to a new map, then return the unchanged '
    - [CLAUSE_STACK_OVERFLOW] form=`(let [m {:a 1}] (assoc m :b 2) m)` — sentence with 7 commas reads as AI-output cadence: 'To bind a map m, call assoc to add :b 5 to a new map, then return the unchanged '

### G9-02: Why state at all

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 5, 'LOW_GROUNDING': 4}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — sentence with 7 commas reads as AI-output cadence: 'To construct an atom holding 0 as counter, atomically swap it by applying inc, a'
    - [LOW_GROUNDING] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — sentence with 7 commas reads as AI-output cadence: 'The page\nchanges only when someone writes — and only as the REPL allows." To\ncon'
    - [LOW_GROUNDING] form=`(do (def progress (atom :idle)) (reset! progress :` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def progress (atom :idle)) (reset! progress :` — sentence with 7 commas reads as AI-output cadence: 'The REPL sees to that —\nno two writers stomp on each other\'s chalk." To construc'
    - [LOW_GROUNDING] form=`(do (def progress (atom :idle)) (reset! progress :` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-03: Atom introduction

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'CONCEPT_PHRASE_COMMA_LIST': 9, 'CLAUSE_STACK_OVERFLOW': 8}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 5 commas reads as AI-output cadence: 'To construct an atom holding 0, atomically swap it by applying inc, and derefere'
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 7 commas reads as AI-output cadence: 'To construct an atom holding 0, atomically swap it by applying inc, and derefere'

### G9-04: Atom CAS semantics

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'LOW_GROUNDING': 1, 'CLAUSE_STACK_OVERFLOW': 3}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — concept_phrase 'atom, CAS, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — concept_phrase 'atom, CAS, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — sentence with 7 commas reads as AI-output cadence: 'The page\nchanges only when someone writes — and only as the REPL allows." To\ncon'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — concept_phrase 'atom, CAS, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 5)) (compare-and-set! a 0 99) @a)` — concept_phrase 'atom, failed CAS, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose

### G9-05: Watch on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 2, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':w',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — sentence with 8 commas reads as AI-output cadence: 'If two of us arrive at once, the REPL holds one of us at the\nthreshold so the sl'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':w',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':w',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — sentence with 7 commas reads as AI-output cadence: 'The REPL sees to that —\nno two writers stomp on each other\'s chalk." To construc'

### G9-06: Validator on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3, 'LOW_GROUNDING': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — sentence with 5 commas reads as AI-output cadence: 'validator on it, atomically swap by applying inc, and dereference, she composed\n'
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — sentence with 5 commas reads as AI-output cadence: 'validator on it, atomically swap by applying inc, and dereference, he composed\na'
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — sentence with 5 commas reads as AI-output cadence: 'validator on it, atomically swap by applying inc, and dereference,\nhe composed a'

### G9-07: Ref introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 6, 'LOW_GROUNDING': 2, 'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — concept_phrase 'ref, dosync, alter, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 8 commas reads as AI-output cadence: 'To construct a ref holding 0, perform a transactional alter by applying inc insi'
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — concept_phrase 'ref, dosync, alter, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 8 commas reads as AI-output cadence: 'To construct a ref holding 0, perform a transactional alter by applying inc insi'
    - [HIGH_LENGTH] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg 218 words

### G9-08: dosync and alter

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4, 'LOW_GROUNDING': 1, 'CONCEPT_PHRASE_COMMA_LIST': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — sentence with 7 commas reads as AI-output cadence: 'If two of us arrive at once, the REPL holds one of us at the\nthreshold so the sl'
    - [LOW_GROUNDING] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — sentence with 6 commas reads as AI-output cadence: 'The page\nchanges only when someone writes — and only as the REPL allows." To\ncon'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — concept_phrase 'ref, dosync, alter, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — sentence with 9 commas reads as AI-output cadence: 'If two of us arrive at once, the REPL holds one of us at the\nthreshold so the sl'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — concept_phrase 'ref, dosync, alter, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose

### G9-09: Ref vs atom

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 6}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 7 commas reads as AI-output cadence: 'The REPL sees to that —\nno two writers stomp on each other\'s chalk." To construc'
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 5 commas reads as AI-output cadence: 'To construct an atom holding 0, atomically swap it by applying inc, and derefere'

### G9-10: Agent introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'LOW_GROUNDING': 2, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 5, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [HIGH_LENGTH] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg 212 words
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 7 commas reads as AI-output cadence: 'To construct an agent holding 0, use send to asynchronously apply inc, await its'
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose

### G9-11: send and send-off

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 4}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 10 commas reads as AI-output cadence: 'The result will\nbe there when you ask for it — sometimes you have to wait for th'
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 7 commas reads as AI-output cadence: 'To construct an agent holding 0, use send to asynchronously apply inc, await its'

### G9-12: await — synchronizing on agents

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'CONCEPT_PHRASE_COMMA_LIST': 3, 'CLAUSE_STACK_OVERFLOW': 3}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — concept_phrase 'agent, double send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 9 commas reads as AI-output cadence: 'To construct an agent holding 0, asynchronously send inc twice, synchronize with'
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — concept_phrase 'agent, double send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 9 commas reads as AI-output cadence: 'The\nruntime makes that easier than it sounds." To construct an agent holding 0, '

### G9-13: future introduction

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 3, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 3, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`@(future (+ 1 2))` — concept_phrase 'future, add, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`@(future (+ 1 2))` — concept_phrase 'future, add, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`@(future (+ 1 2))` — concept_phrase 'future, add, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose

### G9-15: promise — deliver and deref

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 5}
    - [LOW_GROUNDING] form=`(do (def p (promise)) (deliver p :done) @p)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def p (promise)) (deliver p :done) @p)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':done',), resolution doesn't close the loop)
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def p (promise)) (deliver p :done) @p)` — concept_phrase 'promise, deliver, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def p (promise)) (deliver p :done) @p)` — sentence with 8 commas reads as AI-output cadence: 'The result will\nbe there when you ask for it — sometimes you have to wait for th'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def p (promise)) (deliver p :done) @p)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':done',), resolution doesn't close the loop)
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def p (promise)) (deliver p :done) @p)` — concept_phrase 'promise, deliver, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose

### G9-16: volatile — when STM is too heavy

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 5, 'LOW_GROUNDING': 1}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — concept_phrase 'volatile, vswap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — sentence with 7 commas reads as AI-output cadence: 'To construct a volatile holding 0, perform a non-transactional swap by applying '
    - [LOW_GROUNDING] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — concept_phrase 'volatile, vswap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — sentence with 8 commas reads as AI-output cadence: 'If two of us arrive at once, the REPL holds one of us at the\nthreshold so the sl'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — concept_phrase 'volatile, vswap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose

### G9-17: binding — thread-local

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 5, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — concept_phrase 'dynamic var, binding, read' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — sentence with 7 commas reads as AI-output cadence: 'The REPL sees to that —\nno two writers stomp on each other\'s chalk." To define a'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — concept_phrase 'dynamic var, binding, read' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — sentence with 8 commas reads as AI-output cadence: 'If two of us arrive at once, the REPL holds one of us at the\nthreshold so the sl'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — concept_phrase 'dynamic var, binding, read' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — sentence with 5 commas reads as AI-output cadence: 'To define a dynamic var *p* as 1, use binding to rebind it to 99, and read its v'

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'PARAGRAPH_FRAGMENTATION': 3, 'CLAUSE_STACK_OVERFLOW': 6}
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — concept_phrase 'lock, locking, arithmetic' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [PARAGRAPH_FRAGMENTATION] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — sentence with 5 commas reads as AI-output cadence: 'To create an object to use as a monitor, acquire the lock, and evaluate an addit'
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — concept_phrase 'lock, locking, arithmetic' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose

## Grade 10

### G10-01: quote, unquote, unquote-splice

- examples: 3
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 4, 'FORM_DISPLAY_AND_FORM_NOUN': 2, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'ONLY_SHOOK_HEAD_TIC': 1}
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(quote (+ 1 2))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`'(1 2 3)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G10-02: syntax-quote

- examples: 2
- variety @ n=50: 1.00
- issues: {'ONLY_SHOOK_HEAD_TIC': 2, 'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 2}
    - [ONLY_SHOOK_HEAD_TIC] form=`(let [x 10] `(+ ~x ~x))` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [xs [1 2 3]] `(list ~@xs))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(let [xs [1 2 3]] `(list ~@xs))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [xs [1 2 3]] `(list ~@xs))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(let [xs [1 2 3]] `(list ~@xs))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [xs [1 2 3]] `(list ~@xs))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G10-03: defmacro introduction

- examples: 2
- variety @ n=50: 0.99
- issues: {'SENTENCE_START_LOWER_PRONOUN': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-04: Macro expansion rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 3, 'SENTENCE_START_LOWER_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(macroexpand-1 '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(when true 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(macroexpand-1 '(when true 1))` — sentence with 5 commas reads as AI-output cadence: 'You write the rule\nonce, and any form that names it gets rewritten on the way in'
    - [LOW_GROUNDING] form=`(macroexpand-1 '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(when true 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(macroexpand-1 '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-05: macroexpand

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'CLAUSE_STACK_OVERFLOW': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [LOW_GROUNDING] form=`(macroexpand '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(macroexpand '(when true 1))` — sentence with 5 commas reads as AI-output cadence: 'You write the rule\nonce, and any form that names it gets rewritten on the way in'
    - [LOW_GROUNDING] form=`(macroexpand '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(macroexpand '(-> 1 inc inc))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(macroexpand '(-> 1 inc inc))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(macroexpand '(-> 1 inc inc))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-06: when and when-not as macros

- examples: 3
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 2, 'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 3, 'REPEATED_OPENER_FRAGMENT': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(when true 1 2 3)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [LOW_GROUNDING] form=`(when true 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(when true 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [SENTENCE_START_LOWER_PRONOUN] form=`(when false 1 2 3)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when-not false :ok)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':ok',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(when-not false :ok)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 2, 'CONCEPT_AS_VERB': 3, 'LOW_GROUNDING': 5, 'PARAGRAPH_FRAGMENTATION': 2, 'CLAUSE_STACK_OVERFLOW': 2}
    - [ANSWER_LEAK] form=`(-> 5 inc inc inc)` — answer 8 in narrative
    - [CONCEPT_AS_VERB] form=`(-> 5 inc inc inc)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(-> 5 inc inc inc)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [ANSWER_LEAK] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — answer 8 in narrative
    - [PARAGRAPH_FRAGMENTATION] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [CLAUSE_STACK_OVERFLOW] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — sentence with 5 commas reads as AI-output cadence: 'To thread a vector through filter, map, and reduce using thread-last, she chalke'

### G10-08: Macro vs fn

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'SENTENCE_START_LOWER_PRONOUN': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — sentence with 5 commas reads as AI-output cadence: 'You write the rule\nonce, and any form that names it gets rewritten on the way in'
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)

### G10-09: Hygiene and gensym

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(symbol? (gensym))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(symbol? (gensym))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('x_', 'x_'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('x_', 'x_'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('x_', 'x_'), resolution doesn't close the loop)

### G10-10: Anaphoric macros are confusing

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'ANSWER_LEAK': 1, 'EXPECTED_META_PHRASE': 1, 'SENTENCE_START_LOWER_PRONOUN': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — user_msg 206 words
    - [ANSWER_LEAK] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — answer 10 in narrative
    - [EXPECTED_META_PHRASE] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — user_msg uses 'the expected X' meta-language — describes the answer in graders'-vocabulary instead of letting the runtime's return speak for itself
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [CLAUSE_STACK_OVERFLOW] form=`(if-let [x 7] (* x x) 0)` — sentence with 5 commas reads as AI-output cadence: 'You write the rule\nonce, and any form that names it gets rewritten on the way in'

### G10-11: Reader macros overview

- examples: 3
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'LOW_GROUNDING': 6, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [LOW_GROUNDING] form=`'(1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`'(1 2 3)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(* % %) 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)

### G10-12: Tagged literals

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(inst? #inst "2024-01-01")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inst? #inst "2024-01-01")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('2024', '-01', '-01'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inst? #inst "2024-01-01")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('2024', '-01', '-01'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(inst? #inst "2024-01-01")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inst? #inst "2024-01-01")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('2024', '-01', '-01'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(inst? #inst "2024-01-01")` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'

### G10-13: Data readers and EDN extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "[:a :b :c]")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "[:a :b :c]")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b', ':c'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "[:a :b :c]")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b', ':c'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "[:a :b :c]")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-14: eval (the function)

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'SENTENCE_START_LOWER_PRONOUN': 2, 'LOW_GROUNDING': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval '(+ 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval '(+ 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [SENTENCE_START_LOWER_PRONOUN] form=`(eval '(+ 1 2 3))` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval '(+ 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [SENTENCE_START_LOWER_PRONOUN] form=`(eval (list '+ 4 5))` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [LOW_GROUNDING] form=`(eval (list '+ 4 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-15: When not to write a macro

- examples: 2
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 2, 'LOW_GROUNDING': 1}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do "a function suffices when no syntax shaping is` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do "a function suffices when no syntax shaping is` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [LOW_GROUNDING] form=`(do "prefer fn unless you must shape syntax" (map ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-16: Macro pattern library

- examples: 2
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 1, 'LOW_GROUNDING': 1, 'ANSWER_LEAK_STRING': 1}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do (defmacro with-careful-watch [& body] `(let [p` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [LOW_GROUNDING] form=`(do (defmacro with-careful-watch [& body] `(let [p` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [ANSWER_LEAK_STRING] form=`(do (defmacro def-watch [name v] `(def ~name ~v)) ` — answer string ':alert' appears in user_msg

## Grade 11

### G11-01: JVM vs CLR vs JS vs Python (host overview)

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'PATIENT_ROLE_BOASTFUL': 1, 'LOW_GROUNDING': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "Clojure runs on multiple hosts: JVM, CLR, JS,` — sentence with 6 commas reads as AI-output cadence: 'To understand that Clojure runs on multiple hosts,\nthe elder, with eyes always o'
    - [PATIENT_ROLE_BOASTFUL] form=`(do "Clojure runs on multiple hosts: JVM, CLR, JS,` — patient role 'the elder' co-occurs with boastful EMO phrase 'boasting at every'
    - [CLAUSE_STACK_OVERFLOW] form=`(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScr` — sentence with 6 commas reads as AI-output cadence: 'To name the Clojure implementations for different north,\nthe elder, untroubled b'
    - [LOW_GROUNDING] form=`(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScr` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-02: Method call syntax

- examples: 8
- variety @ n=50: 1.00
- issues: {'EMPTY_GOAL_RENDERED': 8, 'CLAUSE_STACK_OVERFLOW': 6, 'LOW_GROUNDING': 4, 'HIGH_LENGTH': 2, 'ANSWER_LEAK_STRING': 2, 'STORY_RESOLUTION_NO_DRAWN': 12}
    - [EMPTY_GOAL_RENDERED] form=`(.startsWith "shepherd-elder" "shepherd")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [CLAUSE_STACK_OVERFLOW] form=`(.startsWith "shepherd-elder" "shepherd")` — sentence with 6 commas reads as AI-output cadence: "When we need a smith's tool, the runtime\ncarries the value over the wall, asks t"
    - [LOW_GROUNDING] form=`(.startsWith "shepherd-elder" "shepherd")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(.startsWith "shepherd-elder" "shepherd")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [CLAUSE_STACK_OVERFLOW] form=`(.startsWith "shepherd-elder" "shepherd")` — sentence with 6 commas reads as AI-output cadence: "When we need a smith's tool, the runtime\ncarries the value over the wall, asks t"
    - [HIGH_LENGTH] form=`(. "abc" toUpperCase)` — user_msg 201 words

### G11-03: Static method call

- examples: 6
- variety @ n=50: 1.00
- issues: {'PROCEDURAL_OPENER': 2, 'CLAUSE_STACK_OVERFLOW': 4, 'STORY_RESOLUTION_NO_DRAWN': 9, 'EMPTY_GOAL_RENDERED': 5}
    - [PROCEDURAL_OPENER] form=`(Math/abs -7)` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    - [CLAUSE_STACK_OVERFLOW] form=`(Math/max 3 9)` — sentence with 6 commas reads as AI-output cadence: "When we need a smith's tool, the runtime\ncarries the value over the wall, asks t"
    - [CLAUSE_STACK_OVERFLOW] form=`(Math/max 3 9)` — sentence with 6 commas reads as AI-output cadence: "When we need a smith's tool, the runtime\ncarries the value over the wall, asks t"
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)
    - [PROCEDURAL_OPENER] form=`(Math/abs -7)` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)

### G11-04: Field access

- examples: 6
- variety @ n=50: 1.00
- issues: {'EMPTY_GOAL_RENDERED': 15, 'PARAGRAPH_FRAGMENTATION': 1}
    - [EMPTY_GOAL_RENDERED] form=`(count "shepherd")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(count "shepherd")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(count "shepherd")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(count "flock")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(count "flock")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(count "shepherd")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G11-05: Import form

- examples: 2
- variety @ n=50: 1.00
- issues: {'PATIENT_ROLE_BOASTFUL': 1, 'VILLAGE_NOUN_OVERUSE': 1, 'LOW_GROUNDING': 1}
    - [PATIENT_ROLE_BOASTFUL] form=`(do "(:import (java.util Date)) imports a host cla` — patient role 'the elder' co-occurs with boastful EMO phrase 'with a smug grin'
    - [VILLAGE_NOUN_OVERUSE] form=`(do "(:import (java.util Date)) imports a host cla` — `the village` appears 4 times (noun-saturation tic — vary or drop)
    - [LOW_GROUNDING] form=`(do "import is a top-of-file ns clause" :studied)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-06: new and dot-construct

- examples: 6
- variety @ n=50: 1.00
- issues: {'EMPTY_GOAL_RENDERED': 14}
    - [EMPTY_GOAL_RENDERED] form=`(String. "hello")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(new String "world")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(new String "world")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(new String "world")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(String. "hello")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(new String "world")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G11-07: Arrays

- examples: 6
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3, 'LOW_GROUNDING': 4, 'EMPTY_GOAL_RENDERED': 5, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a (int-array [1 2 3])] (alength a))` — sentence with 6 commas reads as AI-output cadence: "When we need a smith's tool, the runtime\ncarries the value over the wall, asks t"
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a (int-array [1 2 3])] (alength a))` — sentence with 6 commas reads as AI-output cadence: "When we need a smith's tool, the runtime\ncarries the value over the wall, asks t"
    - [LOW_GROUNDING] form=`(let [a (int-array [5 10 15])] (aget a 0))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [a (int-array [5 10 15])] (aget a 0))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(let [a (int-array [5 10 15])] (aget a 0))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(let [a (int-array [5 10 15])] (aget a 0))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G11-08: Type hints

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 12, 'CLAUSE_STACK_OVERFLOW': 3}
    - [LOW_GROUNDING] form=`(do "type hints are metadata that guide compilatio` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "type hints are metadata that guide compilatio` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "type hints are metadata that guide compilatio` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [^String s "abc"] (.toUpperCase s))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [^String s "abc"] (.toUpperCase s))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [^String s "abc"] (.toUpperCase s))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)

### G11-09: Checked vs unchecked math

- examples: 2
- variety @ n=50: 1.00
- issues: {'EMPTY_GOAL_RENDERED': 3, 'LOW_GROUNDING': 2, 'PROCEDURAL_OPENER': 1, 'REPL_AS_TIME_TRAVELLER': 1}
    - [EMPTY_GOAL_RENDERED] form=`(+ 1 2)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [LOW_GROUNDING] form=`(+ 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(+ 1 2)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(+ 1 2)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [LOW_GROUNDING] form=`(do "*unchecked-math* turns off overflow checking ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PROCEDURAL_OPENER] form=`(do "*unchecked-math* turns off overflow checking ` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence

### G11-10: ClojureScript overview

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'PATIENT_ROLE_BOASTFUL': 1, 'VILLAGE_NOUN_OVERUSE': 1}
    - [LOW_GROUNDING] form=`(do "ClojureScript compiles to JavaScript via the ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do "ClojureScript compiles to JavaScript via the ` — sentence with 6 commas reads as AI-output cadence: 'To understand how ClojureScript compiles to JavaScript,\nthe elder, saying very l'
    - [LOW_GROUNDING] form=`(do "cljs runs in browsers and Node, with JS inter` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PATIENT_ROLE_BOASTFUL] form=`(do "cljs runs in browsers and Node, with JS inter` — patient role 'the elder' co-occurs with boastful EMO phrase 'with a smug grin'
    - [VILLAGE_NOUN_OVERUSE] form=`(do "cljs runs in browsers and Node, with JS inter` — `the village` appears 4 times (noun-saturation tic — vary or drop)
    - [LOW_GROUNDING] form=`(do "cljs runs in browsers and Node, with JS inter` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-11: cljs / JavaScript interop

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'CLAUSE_STACK_OVERFLOW': 1, 'AI_OUTPUT_CADENCE': 1}
    - [LOW_GROUNDING] form=`(do "(js/console.log x) calls a JS global; (.-foo ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do "(js/console.log x) calls a JS global; (.-foo ` — sentence with 6 commas reads as AI-output cadence: 'To understand how ClojureScript calls JavaScript globals and reads fields,\nthe e'
    - [LOW_GROUNDING] form=`(do "js/<name> namespaces JS globals; .- prefix ma` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [AI_OUTPUT_CADENCE] form=`(do "js/<name> namespaces JS globals; .- prefix ma` — user_msg has 'with the X of one who Y' elaborate-clause-stack cadence (reads like model output, not storybook prose)

### G11-12: Basilisp overview (Python host)

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPEATED_OPENER_FRAGMENT': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'PATIENT_ROLE_BOASTFUL': 1, 'VILLAGE_NOUN_OVERUSE': 1, 'LOW_GROUNDING': 2}
    - [REPEATED_OPENER_FRAGMENT] form=`(do "basilisp is a Clojure-like Lisp implemented o` — opener fragment 'at the edge of the meadow,' also appears later in user_msg
    - [CLAUSE_STACK_OVERFLOW] form=`(do "basilisp is a Clojure-like Lisp implemented o` — sentence with 6 commas reads as AI-output cadence: 'To understand that basilisp is Clojure on Python,\nthe elder, with eyes always on'
    - [PATIENT_ROLE_BOASTFUL] form=`(do "basilisp is a Clojure-like Lisp implemented o` — patient role 'the elder' co-occurs with boastful EMO phrase 'with a smug grin'
    - [VILLAGE_NOUN_OVERUSE] form=`(do "basilisp is a Clojure-like Lisp implemented o` — `the village` appears 4 times (noun-saturation tic — vary or drop)
    - [LOW_GROUNDING] form=`(do "basilisp interops with Python via the same do` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "basilisp interops with Python via the same do` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-13: Cross-platform .cljc and reader-conditionals

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3, 'LOW_GROUNDING': 1, 'AI_OUTPUT_CADENCE': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "#?(:clj … :cljs …) selects a form per host at` — sentence with 6 commas reads as AI-output cadence: 'To learn how reader-conditionals choose code per host,\nthe elder, with eyes alwa'
    - [CLAUSE_STACK_OVERFLOW] form=`(do "#?(:clj … :cljs …) selects a form per host at` — sentence with 6 commas reads as AI-output cadence: 'To learn how reader-conditionals choose code per host,\nthe elder, without compla'
    - [CLAUSE_STACK_OVERFLOW] form=`(do ".cljc files share code across multiple hosts"` — sentence with 6 commas reads as AI-output cadence: 'To understand the role of .hard files,\nthe elder, stepping deliberately, compose'
    - [LOW_GROUNDING] form=`(do ".cljc files share code across multiple hosts"` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [AI_OUTPUT_CADENCE] form=`(do ".cljc files share code across multiple hosts"` — user_msg has 'with the X of one who Y' elaborate-clause-stack cadence (reads like model output, not storybook prose)

### G11-14: Debugging host leaks

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'PROCEDURAL_OPENER': 1, 'CLAUSE_STACK_OVERFLOW': 7, 'STORY_RESOLUTION_NO_DRAWN': 9, 'EMPTY_GOAL_RENDERED': 6}
    - [LOW_GROUNDING] form=`(do "host stack traces leak through interop; learn` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PROCEDURAL_OPENER] form=`(do "host stack traces leak through interop; learn` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    - [CLAUSE_STACK_OVERFLOW] form=`(do "host stack traces leak through interop; learn` — sentence with 6 commas reads as AI-output cadence: "When we need a smith's tool, the runtime\ncarries the value over the wall, asks t"
    - [CLAUSE_STACK_OVERFLOW] form=`(do "host stack traces leak through interop; learn` — sentence with 6 commas reads as AI-output cadence: "When we need a smith's tool, the runtime\ncarries the value over the wall, asks t"
    - [CLAUSE_STACK_OVERFLOW] form=`(try (Math/sqrt 4) (catch Exception _ :err))` — sentence with 6 commas reads as AI-output cadence: "When we need a smith's tool, the runtime\ncarries the value over the wall, asks t"
    - [CLAUSE_STACK_OVERFLOW] form=`(try (Math/sqrt 4) (catch Exception _ :err))` — sentence with 6 commas reads as AI-output cadence: "When we need a smith's tool, the runtime\ncarries the value over the wall, asks t"

## Grade 12

### G12-01: Transducers introduction

- examples: 2
- variety @ n=50: 0.99
- issues: {'CLAUSE_STACK_OVERFLOW': 4, 'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'PARAGRAPH_FRAGMENTATION': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] (map inc) [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'Josephina shook her head and went on\nwith the work: to use the map-inc transduce'
    - [HIGH_LENGTH] form=`(into [] (map inc) [1 2 3])` — user_msg 218 words
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] (map inc) [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To use the map-inc transducer with into to increment the vector containing 1, 2,'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (filter even?) [1 2 3 4 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', '5'), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(into [] (filter even?) [1 2 3 4 5])` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] (filter even?) [1 2 3 4 5])` — sentence with 7 commas reads as AI-output cadence: 'To use the filter-even transducer with into to keep only the even numbers from t'

### G12-02: Transducer composition

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4}
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — sentence with 8 commas reads as AI-output cadence: 'Leopold shook his head and went on\nwith the work: to compose map-inc and filter-'
    - [CLAUSE_STACK_OVERFLOW] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — sentence with 6 commas reads as AI-output cadence: 'What Clojure form computes the sum accumulated via transduce using the composed '
    - [CLAUSE_STACK_OVERFLOW] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — sentence with 6 commas reads as AI-output cadence: 'Write a Clojure expression that computes the sum accumulated via transduce using'
    - [CLAUSE_STACK_OVERFLOW] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — sentence with 6 commas reads as AI-output cadence: 'Write a form whose evaluation gives the sum accumulated via transduce using the '

### G12-03: into with a transducer (xform)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'COLLECTION_LEAK': 1, 'CLAUSE_STACK_OVERFLOW': 2}
    - [HIGH_LENGTH] form=`(into #{} (map inc) [1 2 3])` — user_msg 213 words
    - [COLLECTION_LEAK] form=`(into #{} (map inc) [1 2 3])` — elements of expected {2, 3, 4} appear comma-separated in user_msg (collection answer leak)
    - [CLAUSE_STACK_OVERFLOW] form=`(into #{} (map inc) [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To use the map-inc transducer with into to create a set from the incremented ele'
    - [CLAUSE_STACK_OVERFLOW] form=`(into #{} (map inc) [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'Iustinian shook his head and went on\nwith the work: to use the map-inc transduce'

### G12-04: core.async introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'VILLAGE_NOUN_OVERUSE': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [VILLAGE_NOUN_OVERUSE] form=`(do "go-blocks let you write async code as if it w` — `the village` appears 4 times (noun-saturation tic — vary or drop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do "go-blocks let you write async code as if it w` — sentence with 6 commas reads as AI-output cadence: 'To learn how go-blocks let you write asynchronous code in a synchronous style,\nt'

### G12-05: Channels and pipelines

- examples: 2
- variety @ n=50: 1.00
- issues: {'PATIENT_ROLE_BOASTFUL': 1, 'VILLAGE_NOUN_OVERUSE': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'LOW_GROUNDING': 1}
    - [PATIENT_ROLE_BOASTFUL] form=`(do "pipe, mult, mix, pipeline-async route values ` — patient role 'the elder' co-occurs with boastful EMO phrase 'with a smug grin'
    - [VILLAGE_NOUN_OVERUSE] form=`(do "pipe, mult, mix, pipeline-async route values ` — `the village` appears 4 times (noun-saturation tic — vary or drop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do "pipe, mult, mix, pipeline-async route values ` — sentence with 5 commas reads as AI-output cadence: 'To study how pipe, mult, mix, and pipeline-async route values across channels, h'
    - [LOW_GROUNDING] form=`(do "pipelines transform streams of values channel` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-06: clojure.spec

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'VILLAGE_NOUN_OVERUSE': 2, 'PATIENT_ROLE_BOASTFUL': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':as'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':as'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':as'), resolution doesn't close the loop)
    - [VILLAGE_NOUN_OVERUSE] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — `the village` appears 4 times (noun-saturation tic — vary or drop)
    - [PATIENT_ROLE_BOASTFUL] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — patient role 'the elder' co-occurs with boastful EMO phrase 'with the swagger of an unrepen'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':as'), resolution doesn't close the loop)

### G12-07: Spec generators

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'PATIENT_ROLE_BOASTFUL': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "s/exercise produces sample inputs for a spec"` — sentence with 6 commas reads as AI-output cadence: 'To study how s/exercise produces sample inputs from a spec,\nthe elder, untrouble'
    - [PATIENT_ROLE_BOASTFUL] form=`(do "s/exercise produces sample inputs for a spec"` — patient role 'the elder' co-occurs with boastful EMO phrase 'puffed up with pride'
    - [CLAUSE_STACK_OVERFLOW] form=`(do "spec generators turn specs into property-base` — sentence with 6 commas reads as AI-output cadence: 'To understand how coral,\nthe elder, letting the runtime have the last word, comp'

### G12-08: clojure.test

- examples: 2
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 1, 'PARAGRAPH_FRAGMENTATION': 1, 'PATIENT_ROLE_BOASTFUL': 1, 'VILLAGE_NOUN_OVERUSE': 1, 'LOW_GROUNDING': 1}
    - [BOOL_LEAK_RESOLUTION] form=`(= (+ 1 2) 3)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [PARAGRAPH_FRAGMENTATION] form=`(= (+ 1 2) 3)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [PATIENT_ROLE_BOASTFUL] form=`(do "(deftest …), (is …), (testing …) are the core` — patient role 'the elder' co-occurs with boastful EMO phrase 'with great whoops of laughter'
    - [VILLAGE_NOUN_OVERUSE] form=`(do "(deftest …), (is …), (testing …) are the core` — `the village` appears 4 times (noun-saturation tic — vary or drop)
    - [LOW_GROUNDING] form=`(do "(deftest …), (is …), (testing …) are the core` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-09: Test fixtures

- examples: 2
- variety @ n=50: 1.00
- issues: {'AI_OUTPUT_CADENCE': 1, 'LOW_GROUNDING': 1}
    - [AI_OUTPUT_CADENCE] form=`(do "(use-fixtures :each f) wraps every deftest in` — user_msg has 'with the X of one who Y' elaborate-clause-stack cadence (reads like model output, not storybook prose)
    - [LOW_GROUNDING] form=`(do "fixtures provide setup/teardown around deftes` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-10: Property-based testing

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_LEAK': 1, 'BOOL_LEAK_RESOLUTION': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'PATIENT_ROLE_BOASTFUL': 1, 'VILLAGE_NOUN_OVERUSE': 1, 'LOW_GROUNDING': 1}
    - [FORM_LEAK] form=`(= (reverse (reverse [1 2 3])) [1 2 3])` — form '(= (reverse (reverse [1 2 3])) [1 2 3])' appears in user_msg of a goal-style subject
    - [BOOL_LEAK_RESOLUTION] form=`(= (reverse (reverse [1 2 3])) [1 2 3])` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [CLAUSE_STACK_OVERFLOW] form=`(= (reverse (reverse [1 2 3])) [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'To verify the property that reversing a vector twice returns the original vector'
    - [CLAUSE_STACK_OVERFLOW] form=`(= (reverse (reverse [1 2 3])) [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'To verify the property that reversing a vector twice returns the original vector'
    - [PATIENT_ROLE_BOASTFUL] form=`(do "test.check generates inputs and checks proper` — patient role 'the elder' co-occurs with boastful EMO phrase 'with a smug grin'
    - [VILLAGE_NOUN_OVERUSE] form=`(do "test.check generates inputs and checks proper` — `the village` appears 4 times (noun-saturation tic — vary or drop)

### G12-11: Leiningen project.clj

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'CLAUSE_STACK_OVERFLOW': 1, 'AI_OUTPUT_CADENCE': 1}
    - [LOW_GROUNDING] form=`(do "project.clj declares :dependencies, :main, :p` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do "project.clj declares :dependencies, :main, :p` — sentence with 8 commas reads as AI-output cadence: 'To study the project.clj file and how it declares dependencies, main entry point'
    - [LOW_GROUNDING] form=`(do "Leiningen reads project.clj at the project ro` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [AI_OUTPUT_CADENCE] form=`(do "Leiningen reads project.clj at the project ro` — user_msg has 'with the X of one who Y' elaborate-clause-stack cadence (reads like model output, not storybook prose)

### G12-12: deps.edn projects

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPEATED_OPENER_FRAGMENT': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'PATIENT_ROLE_BOASTFUL': 1, 'VILLAGE_NOUN_OVERUSE': 1, 'LOW_GROUNDING': 2, 'PARAGRAPH_FRAGMENTATION': 1}
    - [REPEATED_OPENER_FRAGMENT] form=`(do "deps.edn declares :deps and :aliases for the ` — opener fragment 'at the edge of the meadow,' also appears later in user_msg
    - [CLAUSE_STACK_OVERFLOW] form=`(do "deps.edn declares :deps and :aliases for the ` — sentence with 6 commas reads as AI-output cadence: 'To study the deps.edn file and how it declares dependencies and aliases for the '
    - [PATIENT_ROLE_BOASTFUL] form=`(do "deps.edn declares :deps and :aliases for the ` — patient role 'the elder' co-occurs with boastful EMO phrase 'with a smug grin'
    - [VILLAGE_NOUN_OVERUSE] form=`(do "deps.edn declares :deps and :aliases for the ` — `the village` appears 4 times (noun-saturation tic — vary or drop)
    - [LOW_GROUNDING] form=`(do "deps.edn is read by the official `clj`/`cloju` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PARAGRAPH_FRAGMENTATION] form=`(do "deps.edn is read by the official `clj`/`cloju` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G12-13: Aliases and tools

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4, 'LOW_GROUNDING': 1, 'AI_OUTPUT_CADENCE': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "`clj -M:test` runs the :test alias from deps.` — sentence with 6 commas reads as AI-output cadence: 'To study how the clj command with -M flag runs aliases defined in deps.edn,\nthe '
    - [CLAUSE_STACK_OVERFLOW] form=`(do "`clj -M:test` runs the :test alias from deps.` — sentence with 6 commas reads as AI-output cadence: 'To study how the clj command with -M flag runs aliases defined in deps.edn,\nthe '
    - [CLAUSE_STACK_OVERFLOW] form=`(do "aliases compose extra paths, deps, and main o` — sentence with 10 commas reads as AI-output cadence: 'To understand how hard compose extra classpath entries, dependencies, and JVM op'
    - [LOW_GROUNDING] form=`(do "aliases compose extra paths, deps, and main o` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [AI_OUTPUT_CADENCE] form=`(do "aliases compose extra paths, deps, and main o` — user_msg has 'with the X of one who Y' elaborate-clause-stack cadence (reads like model output, not storybook prose)
    - [CLAUSE_STACK_OVERFLOW] form=`(do "aliases compose extra paths, deps, and main o` — sentence with 6 commas reads as AI-output cadence: 'To understand how low compose extra classpath entries, dependencies, and JVM opt'

### G12-14: Pedestal / Ring (web stack brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'PATIENT_ROLE_BOASTFUL': 1, 'VILLAGE_NOUN_OVERUSE': 1}
    - [LOW_GROUNDING] form=`(do "Pedestal layers interceptors over Ring for ri` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "Pedestal layers interceptors over Ring for ri` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PATIENT_ROLE_BOASTFUL] form=`(do "Pedestal layers interceptors over Ring for ri` — patient role 'the elder' co-occurs with boastful EMO phrase 'with the swagger of an unrepen'
    - [VILLAGE_NOUN_OVERUSE] form=`(do "Pedestal layers interceptors over Ring for ri` — `the village` appears 4 times (noun-saturation tic — vary or drop)

### G12-15: Datomic / XTDB (datalog db brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'VILLAGE_NOUN_OVERUSE': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'PATIENT_ROLE_BOASTFUL': 1}
    - [LOW_GROUNDING] form=`(do "Datomic and XTDB are immutable, time-aware da` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [VILLAGE_NOUN_OVERUSE] form=`(do "Datomic and XTDB are immutable, time-aware da` — `the village` appears 4 times (noun-saturation tic — vary or drop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do "Datomic and XTDB are immutable, time-aware da` — sentence with 8 commas reads as AI-output cadence: 'To study Datomic and XTDB as immutable, time-aware database systems using datalo'
    - [CLAUSE_STACK_OVERFLOW] form=`(do "Datomic and XTDB are immutable, time-aware da` — sentence with 8 commas reads as AI-output cadence: 'To study Datomic and XTDB as immutable, time-aware database systems using datalo'
    - [PATIENT_ROLE_BOASTFUL] form=`(do "queries are written in datalog over EDN-shape` — patient role 'the elder' co-occurs with boastful EMO phrase 'with great whoops of laughter'

### G12-16: Reagent (cljs UI brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'LOW_GROUNDING': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "Reagent wraps React with Hiccup-shaped Clojur` — sentence with 6 commas reads as AI-output cadence: 'To study how thread structures,\nthe elder, untroubled by what others thought, co'
    - [LOW_GROUNDING] form=`(do "components are functions returning Hiccup vec` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-17: Library design patterns

- examples: 3
- variety @ n=50: 1.00
- issues: {'PATIENT_ROLE_BOASTFUL': 5, 'VILLAGE_NOUN_OVERUSE': 5, 'CLAUSE_STACK_OVERFLOW': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [PATIENT_ROLE_BOASTFUL] form=`(do "good libraries expose data, then functions, t` — patient role 'the elder' co-occurs with boastful EMO phrase 'boasting at every'
    - [VILLAGE_NOUN_OVERUSE] form=`(do "good libraries expose data, then functions, t` — `the village` appears 4 times (noun-saturation tic — vary or drop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do "small public API surface, plain data inputs, ` — sentence with 6 commas reads as AI-output cadence: 'To understand the Clojure convention of a small public API surface with plain da'
    - [PATIENT_ROLE_BOASTFUL] form=`(do "small public API surface, plain data inputs, ` — patient role 'the elder' co-occurs with boastful EMO phrase 'with a smug grin'
    - [VILLAGE_NOUN_OVERUSE] form=`(do "small public API surface, plain data inputs, ` — `the village` appears 4 times (noun-saturation tic — vary or drop)
    - [PATIENT_ROLE_BOASTFUL] form=`(= [1 2 3] (vec '(1 2 3)))` — patient role 'the elder' co-occurs with boastful EMO phrase 'puffed up with pride'

### G12-18: Clojure style guide

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'AI_OUTPUT_CADENCE': 1}
    - [LOW_GROUNDING] form=`(do "kebab-case names, two-space indent, threading` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do "prefer pure functions, name predicates with ?` — sentence with 8 commas reads as AI-output cadence: 'To learn the Clojure naming conventions: pure function preference, question-mark'
    - [AI_OUTPUT_CADENCE] form=`(do "prefer pure functions, name predicates with ?` — user_msg has 'with the X of one who Y' elaborate-clause-stack cadence (reads like model output, not storybook prose)
    - [CLAUSE_STACK_OVERFLOW] form=`(do "prefer pure functions, name predicates with ?` — sentence with 8 commas reads as AI-output cadence: 'To learn the Clojure naming conventions: pure function preference, question-mark'

---

## Summary

### Issue counts (across all examples × 3 records)

- **LOW_GROUNDING**: 419
- **CLAUSE_STACK_OVERFLOW**: 275
- **STORY_RESOLUTION_NO_DRAWN**: 231
- **EMPTY_GOAL_RENDERED**: 230
- **FORM_DISPLAY_AND_FORM_NOUN**: 76
- **PARAGRAPH_FRAGMENTATION**: 76
- **CONCEPT_PHRASE_COMMA_LIST**: 75
- **NARRATIVE_NUMERAL_HARDCODE**: 60
- **REPL_AS_TIME_TRAVELLER**: 38
- **BOOL_LEAK_RESOLUTION**: 34
- **SENTENCE_START_LOWER_PRONOUN**: 27
- **ANSWER_LEAK_STRING**: 22
- **VILLAGE_NOUN_OVERUSE**: 21
- **ONLY_SHOOK_HEAD_TIC**: 20
- **PATIENT_ROLE_BOASTFUL**: 20
- **HIGH_LENGTH**: 19
- **HONEST_JUDGE_REPEAT**: 18
- **ANSWER_LEAK**: 15
- **FOREIGN_FABLE_IMAGERY**: 14
- **CONCEPT_AS_VERB**: 12
- **THE_FORM_OVERUSE**: 9
- **STRING_AS_CHAR_MISCLAIM**: 7
- **SMALL_INT_LEAK**: 7
- **AI_OUTPUT_CADENCE**: 6
- **REPEATED_OPENER_FRAGMENT**: 4
- **PROCEDURAL_OPENER**: 4
- **WRONG_FABLE_LITERAL**: 1
- **EXPECTED_META_PHRASE**: 1
- **COLLECTION_LEAK**: 1
- **FORM_LEAK**: 1

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 80 | 185 | — |
| 2 | 22 | 88 | 255 | — |
| 3 | 18 | 31 | 76 | — |
| 4 | 20 | 39 | 99 | — |
| 5 | 22 | 39 | 117 | — |
| 6 | 16 | 33 | 140 | — |
| 7 | 18 | 36 | 132 | — |
| 8 | 16 | 31 | 107 | — |
| 9 | 18 | 34 | 217 | — |
| 10 | 16 | 36 | 134 | — |
| 11 | 14 | 58 | 184 | — |
| 12 | 18 | 37 | 97 | — |

### Sample issues by severity

#### LOW_GROUNDING

- `G1-01` (form `0`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    The wolves of those hills were rare but not absent, and the shepherds knew it was safer to be vigilant than clever.

The elder of the village kept a small slate in the village, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the val...
    ```
- `G1-01` (form `nil`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    A boy with too little to do and too loud a voice is a small danger to himself and a larger one to his village.

Halfway through the morning watch, Cesare called out
at the edge of the hilltop, demanding a verdict on the form `nil` and refusing
to come back to the flock until somebody confirmed it. C...
    ```
- `G1-01` (form `nil`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    Voica had cried wolf once already, in the forest, and the villagers had laughed but not entirely.

A small slate sat on a flat stone near the forest; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `nil`, and the ...
    ```
- `G1-02` (form `7`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    The villagers had agreed that any cry of wolf would bring them running with their sticks and lanterns.

A small crowd of villagers had gathered in the forest to watch
Giulia attempt to predict, off the cuff, what the REPL would
return. Konstantin pointed to the integer 0 and read out the
form aloud:...
    ```
- `G1-02` (form `7`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    near the hilltop, on a slope above the village, Zenta watched his flock and his shadow grow longer.

The elder of the village kept a small slate near the hilltop, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the integer 1. Anselm...
    ```

#### HONEST_JUDGE_REPEAT

- `G1-01` (form `0`): two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    ```
    The wolves of those hills were rare but not absent, and the shepherds knew it was safer to be vigilant than clever.

The elder of the village kept a small slate in the village, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the val...
    ```
- `G1-01` (form `(+ 1 2)`): two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    ```
    On those slopes, trust was a thing the village extended freely, and a thing it could not afford to lose.

The elder of the village kept a small slate in the village, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the form (+ 6 0). ...
    ```
- `G1-02` (form `7`): two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    ```
    near the hilltop, on a slope above the village, Zenta watched his flock and his shadow grow longer.

The elder of the village kept a small slate near the hilltop, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the integer 1. Anselm...
    ```
- `G1-02` (form `0`): two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    ```
    Long days alone with a flock can teach patience, or they can teach mischief, depending on the boy.

The elder of the village kept a small slate near the orchard, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the integer 2. Walther...
    ```
- `G1-02` (form `100`): two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    ```
    There was once a shepherd boy whose afternoons were long and whose imagination was longer.

The elder of the village kept a small slate at the edge of the meadow, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the integer 639. Xave...
    ```

#### FORM_DISPLAY_AND_FORM_NOUN

- `G1-01` (form `(* 4 5)`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    There was once a shepherd boy whose afternoons were long and whose imagination was longer.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(* 7 4)`, and the line
abo...
    ```
- `G1-01` (form `(- 10 (+ 2 3))`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    Bronislava had been minding the sheep near the woods since the first light, and the day was wearing thin.

A small crowd of villagers had gathered in the woods to watch
Bronislava attempt to predict, off the cuff, what the REPL would
return. Vespasia pointed to the nested form (- 1 (+ 7 2)) and read...
    ```
- `G1-01` (form `(+ 1 (* 2 3))`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    Danuta had been minding the sheep by the woods since the first light, and the day was wearing thin.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(+ 1 (* 4 0))`, a...
    ```
- `G1-01` (form `"hello"`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    Long days alone with a flock can teach patience, or they can teach mischief, depending on the boy.

A small slate sat on a flat stone near the meadow; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `"stone"`, and...
    ```
- `G1-01` (form `nil`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    Voica had cried wolf once already, in the forest, and the villagers had laughed but not entirely.

A small slate sat on a flat stone near the forest; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `nil`, and the ...
    ```

#### FOREIGN_FABLE_IMAGERY

- `G1-02` (form `-3`): tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    ```
    The villagers had agreed that any cry of wolf would bring them running with their sticks and lanterns.

Ulvilda kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today atop the hilltop the next entry was
the integer -95. Dmitri peered over her shoulder
a...
    ```
- `G1-02` (form `-25`): tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    ```
    The villagers had agreed that any cry of wolf would bring them running with their sticks and lanterns.

Gunhilda kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today by the farm the next entry was
the integer -85. Sebastien peered over her shoulder
at...
    ```
- `G1-03` (form `1/2`): tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    ```
    The sheep had grazed peacefully all morning, and there was nothing at all the matter, which was exactly the problem.

Gildas kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the hilltop the next entry was
the ratio 1/2. Karin peered over his ...
    ```
- `G1-04` (form `"flock"`): tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    ```
    Tunde was supposed to keep the sheep safe; instead, at the village, he kept inventing reasons for the village to run.

Theodelinda kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the village the next entry was
the string "topaz". Tunde peere...
    ```
- `G1-04` (form `"watch the meadow"`): tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    ```
    at the farm, on a slope above the village, Yara watched his flock and his shadow grow longer.

Walpurga kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the farm the next entry was
the string "lichen". Yara peered over her shoulder
at the for...
    ```

#### VILLAGE_NOUN_OVERUSE

- `G1-08` (form `\w`): `the village` appears 4 times (noun-saturation tic — vary or drop)
    ```
    When Andrej called out in the village the first time, the village came running, and the sheep stayed exactly as they were.

Andrej called down from a stone at the village where someone had
chalked the character \indigo on a flat board. Andrej, with a smug grin,
declared he already knew what would co...
    ```
- `G6-07` (form `(boolean (:private (meta '^:private hidden)))`): `the village` appears 4 times (noun-saturation tic — vary or drop)
    ```
    It happened at the edge of the orchard, on a hill where shouting carries far and trust carries further, until it doesn't.

Carol showed Tom two entries in the village log-book. One symbol, `hidden`, carried a private marker in its margin. Carol asked Tom to convert the raw answer to a simple true or...
    ```
- `G6-10` (form `(:deps {:deps {:a 1 :b 2}})`): `the village` appears 4 times (noun-saturation tic — vary or drop)
    ```
    Melina had cried wolf once already, near the road, and the villagers had laughed but not entirely.

At the village notice-stone on the road, the question of the day was
posted: how to extract the value at the :deps key from a nested map. Melina, with great whoops of laughter, started
to shout an ans...
    ```
- `G6-10` (form `(get-in {:paths ["src"]} [:paths 0])`): `the village` appears 4 times (noun-saturation tic — vary or drop)
    ```
    Melina had cried wolf once already, near the road, and the villagers had laughed but not entirely.

At the village notice-stone on the road, the question of the day was
posted: how to extract the first entry from the :paths vector in a deps-style map. Melina, with the swagger of an unrepentant fibbe...
    ```
- `G11-05` (form `(do "(:import (java.util Date)) imports a host class" :impor`): `the village` appears 4 times (noun-saturation tic — vary or drop)
    ```
    Floarea was supposed to keep the sheep safe; instead, on the road, he kept inventing reasons for the village to run.

At the village notice-stone on the road, the question of the day was
posted: how to understand how to import a host class into a namespace. Floarea, with a smug grin, started
to shou...
    ```

#### STRING_AS_CHAR_MISCLAIM

- `G1-08` (form `\w`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    When Andrej called out in the village the first time, the village came running, and the sheep stayed exactly as they were.

Andrej called down from a stone at the village where someone had
chalked the character \indigo on a flat board. Andrej, with a smug grin,
declared he already knew what would co...
    ```
- `G1-08` (form `\w`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    Some games seem harmless until the moment they are needed in earnest, and then they cost everything.

The elder of the village kept a small slate near the orchard, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the character \marbl...
    ```
- `G1-08` (form `\w`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    Iarlaith was a clever boy, and by the forest cleverness had begun to look very much like trouble.

Crispin kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today by the forest the next entry was
the character \linen. Iarlaith peered over his shoulder
at...
    ```
- `G1-08` (form `\space`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    The pasture lay below a rocky lookout, and the sheep were easier to count than the hours.

Manfred called down from a stone by the meadow where someone had
chalked the character \space on a flat board. Manfred, as if the village would always believe,
declared he already knew what would come back. Cr...
    ```
- `G1-08` (form `\space`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    Wojciech had cried wolf once already, near the forest, and the villagers had laughed but not entirely.

Casimir had been trying to teach Wojciech how the REPL
works. "Look here," he said, pointing to the character \space.
"You hand the form `"marble"` to the runtime, and the runtime hands
you back w...
    ```

#### EMPTY_GOAL_RENDERED

- `G1-09` (form `(symbol? 'wolf)`): user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    ```
    The lambs were milling in the lower meadow when the boy first thought of the joke he should not have made.

Walburga, boasting at every turn, tried to fetch the value that the
chalk mark should carry, insisting it must be there waiting.
Drusilla picked up the slate and pointed: the mark itself is
al...
    ```
- `G1-09` (form `(symbol? 'wolf)`): user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    ```
    There is a difference between a real alarm and a bored one, and the village knew the difference well.

Tom had chalked a label on the slate for a flock pen. Carol stood with a carved tag from the live sheep itself.

The village's notes must not mix chalk marks with the things they name. Tom had to t...
    ```
- `G1-09` (form `(symbol? 'wolf)`): user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    ```
    Some games seem harmless until the moment they are needed in earnest, and then they cost everything.

Vivien, boasting at every turn, mistook the chalk mark on the slate
for the sheep it pointed to. "It says sheep, so the value must be
a sheep!" Albertina only shook her head: the
mark and the sheep ...
    ```
- `G1-09` (form `'wolf`): user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    ```
    There is a difference between a real alarm and a bored one, and the village knew the difference well.

Ingrid, sounding sure of every word, mistook the chalk mark on the slate
for the sheep it pointed to. "It says sheep, so the value must be
a sheep!" Onorata only shook her head: the
mark and the sh...
    ```
- `G1-09` (form `'wolf`): user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    ```
    It happened in the orchard, on a hill where shouting carries far and trust carries further, until it doesn't.

Rhys pointed at the chalk-mark `wolf` on the slate.
"That's a wolf," he said. Henriette, untroubled by what others thought,
shook her head and pointed at the empty meadow beyond the
pen: "T...
    ```

#### BOOL_LEAK_RESOLUTION

- `G1-09` (form `(symbol? 'wolf)`): resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    ```
    There is a difference between a real alarm and a bored one, and the village knew the difference well.

Tom had chalked a label on the slate for a flock pen. Carol stood with a carved tag from the live sheep itself.

The village's notes must not mix chalk marks with the things they name. Tom had to t...
    ```
- `G1-15` (form `(= 1 2)`): resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    ```
    The lambs were milling in the lower meadow when the boy first thought of the joke he should not have made.

Carol had two tally-marks on a stone by the fold: one from the morning count, one from midday. Tom claimed they must differ because sheep move. Carol wrote them side by side to test.

Before t...
    ```
- `G1-15` (form `(= 1 2)`): resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    ```
    It happened in a quiet season, when the lambs were strong and the days were long enough to grow tired of.

Carol had two tally-marks on a stone by the fold: one from the morning count, one from midday. Tom claimed they must differ because sheep move. Carol wrote them side by side to test.

Before th...
    ```
- `G1-15` (form `(= "a" "a")`): resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    ```
    There is a difference between a real alarm and a bored one, and the village knew the difference well.

Carol had written the letter `a` on the slate twice — once in the morning lesson, once in the afternoon. Tom wondered if the two marks were truly the same mark.

The elder's teaching depended on st...
    ```
- `G1-15` (form `(= 1 1 1 1)`): resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    ```
    Ulrich was a clever boy, and near the village cleverness had begun to look very much like trouble.

Carol had four stones at the fold, each notched once — the morning count from four separate shepherds. They all agreed on the same tally. Carol wrote the multi-arg equality test.

Before the day's wor...
    ```

#### PARAGRAPH_FRAGMENTATION

- `G1-09` (form `(symbol? 'wolf)`): user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    There is a difference between a real alarm and a bored one, and the village knew the difference well.

Tom had chalked a label on the slate for a flock pen. Carol stood with a carved tag from the live sheep itself.

The village's notes must not mix chalk marks with the things they name. Tom had to t...
    ```
- `G1-13` (form `(- 5 3)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    There was once a shepherd boy whose afternoons were long and whose imagination was longer.

Tom had watched some sheep leave the fold that morning and some return by noon. Carol chalked the question on the slate: how many were still grazing?

The village's grazing count had to be exact before the af...
    ```
- `G1-13` (form `(- 5 3)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    by the orchard, on a slope above the village, Helga watched his flock and his shadow grow longer.

Tom had watched some sheep leave the fold that morning and some return by noon. Carol chalked the question on the slate: how many were still grazing?

The village's grazing count had to be exact before...
    ```
- `G1-13` (form `(/ 10 2)`): user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    The wolves of those hills were rare but not absent, and the shepherds knew it was safer to be vigilant than clever.

Carol had coins paid for wool. She and Tom had agreed to split them evenly. Carol wrote the division on the slate.

The split had to be fair and final, no haggling once the slate was ...
    ```
- `G1-13` (form `(+ 7 8)`): user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    Renzo had a fine view at the farm, but a finer talent for stretching a quiet hour into a noisy one.

Tom brought lambs from the north pen, Carol brought lambs from the south. Together they needed the total for the morning record.

The day's first count had to lock in before the flock left for pastur...
    ```

#### ONLY_SHOOK_HEAD_TIC

- `G1-09` (form `(symbol? 'wolf)`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    Some games seem harmless until the moment they are needed in earnest, and then they cost everything.

Vivien, boasting at every turn, mistook the chalk mark on the slate
for the sheep it pointed to. "It says sheep, so the value must be
a sheep!" Albertina only shook her head: the
mark and the sheep ...
    ```
- `G1-09` (form `(symbol? 42)`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    A boy with too little to do and too loud a voice is a small danger to himself and a larger one to his village.

Lena, puffed up with pride, mistook the chalk mark on the slate
for the sheep it pointed to. "It says sheep, so the value must be
a sheep!" Nikodemus only shook his head: the
mark and the ...
    ```
- `G1-09` (form `'wolf`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    There is a difference between a real alarm and a bored one, and the village knew the difference well.

Ingrid, sounding sure of every word, mistook the chalk mark on the slate
for the sheep it pointed to. "It says sheep, so the value must be
a sheep!" Onorata only shook her head: the
mark and the sh...
    ```
- `G2-20` (form `(count [1 2 3])`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    Erich had been told the rules plainly: cry only when the wolf is real, and never when he is bored.

Erich, as if the village would always believe, looked at the flock without bothering
to count and called out what he thought the tally
would be. Lucretius only shook his head and began
the walk. To co...
    ```
- `G5-12` (form `(reduce + [1 2 3 4])`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    When Klaus climbed up to the lookout that morning, he did not yet know that the day would teach a lasting lesson.

Klaus, with great whoops of laughter, looked at the flock without bothering
to count and called out what he thought the tally
would be. Frederica only shook her head and began
the walk....
    ```

#### CLAUSE_STACK_OVERFLOW

- `G1-10` (form `(+ 1 2) ; sum of one and two`): sentence with 5 commas reads as AI-output cadence: 'To add 1 and 2, with a single-semicolon trailing comment, he composed\nthe additi'
    ```
    on the farm, where the path winds up toward the lookout, Yelena watched and waited and watched some more.

Yelena, with a smug grin, glanced at the form and called out
what she thought it would do without paying attention to
the conventions of how it was written. Kasimir only
shook his head — the ru...
    ```
- `G1-10` (form `(+ 1 2) ; sum of one and two`): sentence with 5 commas reads as AI-output cadence: 'To add 6 and 4, with a single-semicolon trailing comment, she composed\nthe addit'
    ```
    It is a serious thing to call for help, and a more serious thing to call for it falsely.

Evangelos, puffed up with pride, glanced at the form and called out
what he thought it would do without paying attention to
the conventions of how it was written. Theodelinda only
shook her head — the runtime r...
    ```
- `G1-11` (form `(+
  1
  2)`): sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'
    ```
    The pasture lay below a rocky lookout, and the sheep were easier to count than the hours.

"A form is what's actually there on the page," Albertina
said, "after the conventions of writing and reading have done
their work. The runtime sees the cleaned-up form, evaluates it,
and gives back what it com...
    ```
- `G1-15` (form `(= 1 1)`): sentence with 5 commas reads as AI-output cadence: 'An empty bucket, a zero-tally, a sleeping\nflock — every one of those still swing'
    ```
    near the hilltop, on a slope above the village, Carys watched his flock and his shadow grow longer.

"Why did the gate stay shut?" Carys asked. Bartholomew,
with the calm of a long watch well kept, leaned on the heavy timber. "Two things and only two things
close these gates: nil and false. An empty...
    ```
- `G1-15` (form `(= 1 2)`): sentence with 5 commas reads as AI-output cadence: 'An empty bucket, a zero-tally, a sleeping\nflock — every one of those still swing'
    ```
    The sheep had grazed peacefully all morning, and there was nothing at all the matter, which was exactly the problem.

"Why did the gate stay shut?" Philippa asked. Konstantin,
untroubled by what others thought, leaned on the heavy timber. "Two things and only two things
close these gates: nil and fa...
    ```

#### REPL_AS_TIME_TRAVELLER

- `G1-13` (form `(* 4 5)`): user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    ```
    When Evangelos called out at the edge of the orchard the first time, the village came running, and the sheep stayed exactly as they were.

Evangelos eyed the grazing flock at the edge of the orchard, boasting at every turn, and called out a
guess about how many sheep were there without bothering to ...
    ```
- `G1-13` (form `(/ 10 2)`): user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    ```
    The lambs were milling in the lower meadow when the boy first thought of the joke he should not have made.

Tamara eyed the grazing flock near the hilltop, puffed up with pride, and called out a
guess about how many sheep were there without bothering to count. Josephina
simply began counting — to di...
    ```
- `G1-13` (form `(- 20 7)`): user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    ```
    The sheep had grazed peacefully all morning, and there was nothing at all the matter, which was exactly the problem.

Emiel eyed the grazing flock along the road, talking past the elder's warning, and called out a
guess about how many sheep were there without bothering to count. Perpetua
simply bega...
    ```
- `G1-13` (form `(- 20 7)`): user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    ```
    It happened in a quiet season, when the lambs were strong and the days were long enough to grow tired of.

Thora eyed the grazing flock near the village, talking past the elder's warning, and called out a
guess about how many sheep were there without bothering to count. Sigismund
simply began counti...
    ```
- `G1-16` (form `(zero? 0)`): user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    ```
    Long days alone with a flock can teach patience, or they can teach mischief, depending on the boy.

Irmgard eyed the grazing flock at the edge of the meadow, boasting at every turn, and called out a
guess about how many sheep were there without bothering to count. Katharina
simply began counting — t...
    ```

#### REPEATED_OPENER_FRAGMENT

- `G1-13` (form `(* 4 5)`): opener fragment 'at the edge of the orchard' also appears later in user_msg
    ```
    When Evangelos called out at the edge of the orchard the first time, the village came running, and the sheep stayed exactly as they were.

Evangelos eyed the grazing flock at the edge of the orchard, boasting at every turn, and called out a
guess about how many sheep were there without bothering to ...
    ```
- `G10-06` (form `(when-not false :ok)`): opener fragment 'at the edge of the forest,' also appears later in user_msg
    ```
    at the edge of the forest, where the path winds up toward the lookout, Giulia watched and waited and watched some more.

Zephaniah sat at a small writing desk at the edge of the forest, slate and chalk
in hand. "A macro," he said, "is a rule that rewrites
the shorthand before the runtime ever sees i...
    ```
- `G11-12` (form `(do "basilisp is a Clojure-like Lisp implemented on Python" `): opener fragment 'at the edge of the meadow,' also appears later in user_msg
    ```
    at the edge of the meadow, on a slope above the village, Calista watched his flock and his shadow grow longer.

The village's rule, by long agreement at the edge of the meadow, was simple: a
question was answered by a form, never by a claim. To understand that basilisp is Clojure on Python,
the elde...
    ```
- `G12-12` (form `(do "deps.edn declares :deps and :aliases for the Clojure CL`): opener fragment 'at the edge of the meadow,' also appears later in user_msg
    ```
    at the edge of the meadow, on a slope above the village, Calista watched his flock and his shadow grow longer.

The village's rule, by long agreement at the edge of the meadow, was simple: a
question was answered by a form, never by a claim. To study the deps.edn file and how it declares dependencie...
    ```

#### NARRATIVE_NUMERAL_HARDCODE

- `G1-15` (form `(= 1 1 1 1)`): parametric example has hard-coded English numeral 'four stones' in a story slot — the actual draws may differ from this fixed count
    ```
    Ulrich was a clever boy, and near the village cleverness had begun to look very much like trouble.

Carol had four stones at the fold, each notched once — the morning count from four separate shepherds. They all agreed on the same tally. Carol wrote the multi-arg equality test.

Before the day's wor...
    ```
- `G1-15` (form `(= 1 1 1 1)`): parametric example has hard-coded English numeral 'four stones' in a story slot — the actual draws may differ from this fixed count
    ```
    The villagers lived just down the slope from where Carlotta stood watch, and they trusted that voice.

Carlotta, as if the village would always believe, watched the fold-gates atop the hilltop and claimed to
know exactly what they would do without checking the condition. "I just know,"
she insisted,...
    ```
- `G1-15` (form `(= 1 1 1 1)`): parametric example has hard-coded English numeral 'four stones' in a story slot — the actual draws may differ from this fixed count
    ```
    The wolves of those hills were rare but not absent, and the shepherds knew it was safer to be vigilant than clever.

"So the gate just says yes or no?" Donata asked.
Valentina, with eyes always on the slate, shook her head and tapped the heavy
timber. "Look closely. The gate carries the actual value...
    ```
- `G2-02` (form `(<= 1 1 2)`): parametric example has hard-coded English numeral 'three bundles' in a story slot — the actual draws may differ from this fixed count
    ```
    Long days alone with a flock can teach patience, or they can teach mischief, depending on the boy.

"Watch the flock," Yolanda said, gesturing at the grazing sheep. "Every
operation either adds a lamb, removes one, or combines what's already there —
the flock grows or shrinks by exactly what you say...
    ```
- `G2-02` (form `(<= 1 1 2)`): parametric example has hard-coded English numeral 'three bundles' in a story slot — the actual draws may differ from this fixed count
    ```
    Long days alone with a flock can teach patience, or they can teach mischief, depending on the boy.

Margarethe eyed the grazing flock in the orchard, boasting at every turn, and called out a
guess about how many sheep were there without bothering to count. Walther
simply began counting — to test whe...
    ```

#### ANSWER_LEAK

- `G2-01` (form `(+ 10 20 30)`): answer 60 in narrative
    ```
    It happened in a quiet season, when the lambs were strong and the days were long enough to grow tired of.

Rafal eyed the grazing flock near the woods, with a smug grin, and called out a
guess about how many sheep were there without bothering to count. Benedict
simply began counting — to add 7, 10, ...
    ```
- `G2-10` (form `(* 2 2 2)`): answer 8 in narrative
    ```
    The hilltop offered a fine view of both the flock and the road below, where help would have to come from.

Carol stacked boxes in a cube pattern: 2 boxes deep, 2 boxes wide, 2 boxes tall. She wanted to know the total volume.

The cube volume required multiplying 2 three times. Tom estimated; Carol d...
    ```
- `G2-21` (form `(count "shepherd")`): answer 8 in narrative
    ```
    The sheep had grazed peacefully all morning, and there was nothing at all the matter, which was exactly the problem.

Carol wrote the word 'willow' on the slate as a long bead-string. She wanted to count every bead in the cord.

The string length mattered for labeling in the ledger. Tom said roughly...
    ```
- `G2-22` (form `(quot (+ 100 50) 5)`): answer 30 in narrative
    ```
    On those slopes, trust was a thing the village extended freely, and a thing it could not afford to lose.

Carol had 590 fleeces in the west field and 73 in the east field. She wanted to divide the combined total equally by 6 buyers.

The quotient after summing mattered for the fair price. Tom said t...
    ```
- `G2-22` (form `(quot (+ 100 50) 5)`): answer 30 in narrative
    ```
    A boy with too little to do and too loud a voice is a small danger to himself and a larger one to his village.

Carol had 597 fleeces in the west field and 81 in the east field. She wanted to divide the combined total equally by 20 buyers.

The quotient after summing mattered for the fair price. Tom...
    ```

#### SMALL_INT_LEAK

- `G2-05` (form `(mod 17 5)`): small-int answer 2 leaks via resolution-slot phrasing
    ```
    It was in the orchard, where the ridge looks down on the houses, that Nikolai first cried wolf.

Carol worked with `mod` to sort lambs by a five-day cycle. On day 12 of the year, she wanted to know which position in the cycle it occupied.

The position in the five-day cycle mattered for rotation. To...
    ```
- `G2-20` (form `(count "hello")`): small-int answer 5 leaks via resolution-slot phrasing
    ```
    Eamon had been told the rules plainly: cry only when the wolf is real, and never when he is bored.

Carol wrote the word 'marble' on the slate and wanted to know how many characters it held.

The character count mattered for the ledger. Tom said five; Carol insisted the form would walk the string an...
    ```
- `G2-20` (form `(count "hello")`): small-int answer 5 leaks via resolution-slot phrasing
    ```
    It was near the hilltop, where the ridge looks down on the houses, that Leonardo first cried wolf.

Carol wrote the word 'myrtle' on the slate and wanted to know how many characters it held.

The character count mattered for the ledger. Tom said five; Carol insisted the form would walk the string an...
    ```
- `G2-21` (form `(count "wolf")`): small-int answer 4 leaks via resolution-slot phrasing
    ```
    On those slopes, trust was a thing the village extended freely, and a thing it could not afford to lose.

Carol wrote 'myrrh' on the slate and wanted to know its length. The name appeared shorter than 'shepherd'.

The comparison mattered for the record. Tom said four; Carol insisted the form would s...
    ```
- `G3-03` (form `(let [x 3] (+ x 1))`): small-int answer 4 leaks via resolution-slot phrasing
    ```
    The lambs were milling in the lower meadow when the boy first thought of the joke he should not have made.

Carol the elder had been counting along a stretch of fence-line at dawn. She slipped a tally-token worth 7 lambs into the small leather belt-pouch at her hip and gave the pouch's contents the ...
    ```

#### STORY_RESOLUTION_NO_DRAWN

- `G2-08` (form `(* 2/3 3/4)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3', '4'), resolution doesn't close the loop)
    ```
    Some games seem harmless until the moment they are needed in earnest, and then they cost everything.

"Watch the flock," Ezekiel said, gesturing at the grazing sheep. "Every
operation either adds a lamb, removes one, or combines what's already there —
the flock grows or shrinks by exactly what you s...
    ```
- `G2-08` (form `(* 2/3 3/4)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3', '4'), resolution doesn't close the loop)
    ```
    It happened by the woods, on a hill where shouting carries far and trust carries further, until it doesn't.

Friedrich, sounding sure of every word, glanced at the flock near the woods and shouted out
what he claimed the count would be, without bothering to tally.
"I know numbers," he insisted. Dome...
    ```
- `G2-08` (form `(* 2/3 3/4)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3', '4'), resolution doesn't close the loop)
    ```
    An empty hour can sometimes be filled with mischief, and mischief once started has a way of escalating.

Elsa eyed the grazing flock at the edge of the woods, with great whoops of laughter, and called out a
guess about how many sheep were there without bothering to count. Urbanus
simply began counti...
    ```
- `G3-07` (form `((fn [x] (+ x 1)) 4)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    ```
    The hilltop offered a fine view of both the flock and the road below, where help would have to come from.

Damien, with great whoops of laughter, began calling out guesses about what the
routine would produce, certain he knew without writing a
thing. Drusilla simply kept chalking on the watchhouse w...
    ```
- `G3-07` (form `((fn [x] (+ x 1)) 4)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    ```
    When Philippa called out by the orchard the first time, the village came running, and the sheep stayed exactly as they were.

Philippa, with the swagger of an unrepentant fibber, began calling out guesses about what the
routine would produce, certain she knew without writing a
thing. Isidora simply ...
    ```

#### THE_FORM_OVERUSE

- `G2-12` (form `(print "x")`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    A boy with too little to do and too loud a voice is a small danger to himself and a larger one to his village.

Carol wanted to write a single character `lichen` to the slate without moving to a new line. She asked what the form would return.

The character needed to appear, and the form's return va...
    ```
- `G2-12` (form `(print "x")`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    in the meadow, in the long grass above the village road, Roswitha settled in for another slow afternoon.

Carol wanted to write a single character `garnet` to the slate without moving to a new line. She asked what the form would return.

The character needed to appear, and the form's return value ha...
    ```
- `G2-15` (form `(if "" :truthy :falsey)`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    The lambs were milling in the lower meadow when the boy first thought of the joke he should not have made.

Carol wrote an empty string on the slate — zero characters, but a string nonetheless. She wanted to know which path the conditional would take.

The gate needed to know if the empty string was...
    ```
- `G2-15` (form `(if "" :truthy :falsey)`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    It happened in a quiet season, when the lambs were strong and the days were long enough to grow tired of.

Carol wrote an empty string on the slate — zero characters, but a string nonetheless. She wanted to know which path the conditional would take.

The gate needed to know if the empty string was ...
    ```
- `G2-15` (form `(if nil :truthy :falsey)`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    There is a difference between a real alarm and a bored one, and the village knew the difference well.

Carol's search for an entry in the ledger came up empty — nil. The conditional needed to know which path a missing value took.

The gate had to decide based on nil. Tom said nothing was nothing; Ca...
    ```

#### SENTENCE_START_LOWER_PRONOUN

- `G2-20` (form `(count [])`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    The villagers lived just down the slope from where Kasper stood watch, and they trusted that voice.

Kasper, in a panic, was beginning to understand: the
tally-stick walk was not magic, only patient. Nikodemus took the
goal — to count the elements in an empty vector — and composed the count operatio...
    ```
- `G2-20` (form `(count [])`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    When Theobald called out by the meadow the first time, the village came running, and the sheep stayed exactly as they were.

Theobald, calling out without confidence anyone would come, was beginning to understand: the
tally-stick walk was not magic, only patient. Magnus took the
goal — to count the ...
    ```
- `G3-03` (form `(let [x 3] (+ x 1))`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    Gudrun had been minding the sheep along the road since the first light, and the day was wearing thin.

Gudrun, wide-eyed with fear, was beginning to understand:
the belt-pouch was not magic, only careful. Cordelia took the
goal — to bind a value of 5 to a local name x for one stretch, then return th...
    ```
- `G3-04` (form `(let [x 5 y 3] (- x y))`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    On a hill above the village, a boy watched sheep, and the sheep watched the grass, and the day moved slowly.

Brendan, with the fear of a watch that no one trusts, was beginning to understand:
the belt-pouch was not magic, only careful. Engelberta took the
goal — to bind x to 3 and y to 7, then subt...
    ```
- `G3-06` (form `(let [a 5 b (* a 2)] b)`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    It is a serious thing to call for help, and a more serious thing to call for it falsely.

Soren, calling out without confidence anyone would come, was beginning to understand:
the belt-pouch was not magic, only careful. Jacquelyn took the
goal — to bind a to 8, then bind b to twice a, and return b —...
    ```

#### HIGH_LENGTH

- `G3-03` (form `(let [x 3] (+ x 1))`): user_msg 227 words
    ```
    The lambs were milling in the lower meadow when the boy first thought of the joke he should not have made.

Carol the elder had been counting along a stretch of fence-line at dawn. She slipped a tally-token worth 7 lambs into the small leather belt-pouch at her hip and gave the pouch's contents the ...
    ```
- `G3-07` (form `((fn [x] (+ x 1)) 4)`): user_msg 223 words
    ```
    It happened at the edge of the orchard, on a hill where shouting carries far and trust carries further, until it doesn't.

On the watchhouse wall, Carol the elder had pinned a small drill-card with no name at the top — just the steps for what to do once an unnamed quantity arrived. Tom waited beside...
    ```
- `G3-13` (form `((fn [x] x x x 99) 1)`): user_msg 201 words
    ```
    On those slopes, trust was a thing the village extended freely, and a thing it could not afford to lose.

Carol had written a drill-card with three steps: read x, read x again, read x a third time. But then she realized the final step should return 99 instead.

Tom asked: if the drill-card lists man...
    ```
- `G4-18` (form `(= [1 2 3] '(1 2 3))`): user_msg 213 words
    ```
    The lambs were milling in the lower meadow when the boy first thought of the joke he should not have made.

Carol held two containers of fleeces: one a wool-basket `[1 2 3]` and another a cord `'(1 2 3)` with three markers strung on it. The containers looked different, but both held the same three i...
    ```
- `G5-01` (form `(if (> 5 3) :a :b)`): user_msg 203 words
    ```
    near the hilltop, on a slope above the village, Tove watched his flock and his shadow grow longer.

Tom stood sorting wool by weight at the watchhouse. Carol had given him a simple rule: if a fleece weighed more than three coins' worth, send it to the dyer; if not, keep it for the lambing-pen. A fle...
    ```

#### CONCEPT_AS_VERB

- `G3-08` (form `((fn [a b c] (+ a b c)) 1 2 3)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    The lambs were milling in the lower meadow when the boy first thought of the joke he should not have made.

"A drill-card is only useful when it runs," Ignatius said,
holding up a slate-card from the watchhouse wall. "You write the steps,
you bring the shepherds, the runtime does the rest." To creat...
    ```
- `G3-10` (form `(#(+ % 1) 5)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    It happened near the woods, on a hill where shouting carries far and trust carries further, until it doesn't.

"A drill-card is only useful when it runs," Kasimir said,
holding up a slate-card from the watchhouse wall. "You write the steps,
you bring the shepherds, the runtime does the rest." To use...
    ```
- `G3-10` (form `(#(* %1 %2) 3 4)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    A boy with too little to do and too loud a voice is a small danger to himself and a larger one to his village.

"A drill-card is only useful when it runs," Leonora said,
holding up a slate-card from the watchhouse wall. "You write the steps,
you bring the shepherds, the runtime does the rest." To us...
    ```
- `G3-15` (form `(do (println "hi") 42)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    near the hilltop, on a slope above the village, Carys watched his flock and his shadow grow longer.

"A drill-card is only useful when it runs," Bartholomew said,
holding up a slate-card from the watchhouse wall. "You write the steps,
you bring the shepherds, the runtime does the rest." To execute a...
    ```
- `G5-15` (form `((comp inc inc) 5)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    near the hilltop, on a slope above the village, Carys watched his flock and his shadow grow longer.

"A drill-card is only useful when it runs," Bartholomew said,
holding up a slate-card from the watchhouse wall. "You write the steps,
you bring the shepherds, the runtime does the rest." To compose t...
    ```

#### ANSWER_LEAK_STRING

- `G5-03` (form `(when true :yes)`): answer string ':yes' appears in user_msg
    ```
    The lambs were milling in the lower meadow when the boy first thought of the joke he should not have made.

Carol posted a watch-order at the fold: if the lambs were restless today, Tom was to ring the bell and post a notice at the village stone. Tom checked the pen, and warm — the lambs were pacing...
    ```
- `G5-06` (form `(case 2 1 :one 2 :two 3 :three :default)`): answer string ':two' appears in user_msg
    ```
    A boy with too little to do and too loud a voice is a small danger to himself and a larger one to his village.

Carol marked east lambing-pens with numbers: 4 for north-fold lambs, 2 for south-fold, 7 for those born late. Tom held a tally-token marked with the number 2. The form would read the token...
    ```
- `G6-01` (form `(name 'foo.bar)`): answer string 'foo.bar' appears in user_msg
    ```
    On a hill above the village, a boy watched sheep, and the sheep watched the grass, and the day moved slowly.

Tom stood at the village notice-post, where scrolls hung labeled with dotted names. Carol showed him the scroll marked `foo.bar`—a namespace written as a symbol.

Tom wanted to know what the...
    ```
- `G7-10` (form `(:doc (meta '^{:doc "adds two"} plus))`): answer string 'adds two' appears in user_msg
    ```
    The hilltop offered a fine view of both the flock and the road below, where help would have to come from.

Carol carved a drill-card on the watchhouse wall. Above the recipe's steps, she chalked a small note: "adds two". Tom asked what the note was for. Carol opened the metadata.

Every drill-card n...
    ```
- `G8-03` (form `(do (defrecord Watcher [name post]) (:name (->Watcher "elder`): answer string 'elder' appears in user_msg
    ```
    When Klara called out on the farm the first time, the village came running, and the sheep stayed exactly as they were.

Klara, as if the village would always believe, peered at the wooden tally-box
without opening it and insisted she could guess what
each compartment held. Cassandra shook her head a...
    ```

#### PATIENT_ROLE_BOASTFUL

- `G6-10` (form `(:deps {:deps {:a 1 :b 2}})`): patient role 'the elder' co-occurs with boastful EMO phrase 'with great whoops of laughter'
    ```
    Melina had cried wolf once already, near the road, and the villagers had laughed but not entirely.

At the village notice-stone on the road, the question of the day was
posted: how to extract the value at the :deps key from a nested map. Melina, with great whoops of laughter, started
to shout an ans...
    ```
- `G6-10` (form `(get-in {:paths ["src"]} [:paths 0])`): patient role 'the elder' co-occurs with boastful EMO phrase 'with the swagger of an unrepen'
    ```
    Melina had cried wolf once already, near the road, and the villagers had laughed but not entirely.

At the village notice-stone on the road, the question of the day was
posted: how to extract the first entry from the :paths vector in a deps-style map. Melina, with the swagger of an unrepentant fibbe...
    ```
- `G6-10` (form `(get-in {:paths ["src"]} [:paths 0])`): patient role 'the elder' co-occurs with boastful EMO phrase 'puffed up with pride'
    ```
    Renzo had a fine view at the edge of the orchard, but a finer talent for stretching a quiet hour into a noisy one.

At the village notice-stone in the orchard, the question of the day was
posted: how to extract the first entry from the :paths vector in a deps-style map. Renzo, puffed up with pride, ...
    ```
- `G11-01` (form `(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :`): patient role 'the elder' co-occurs with boastful EMO phrase 'boasting at every'
    ```
    A boy with too little to do and too loud a voice is a small danger to himself and a larger one to his village.

At the village notice-stone at the farm, the question of the day was
posted: how to understand that Clojure runs on multiple hosts. Calista, boasting at every turn, started
to shout an ans...
    ```
- `G11-05` (form `(do "(:import (java.util Date)) imports a host class" :impor`): patient role 'the elder' co-occurs with boastful EMO phrase 'with a smug grin'
    ```
    Floarea was supposed to keep the sheep safe; instead, on the road, he kept inventing reasons for the village to run.

At the village notice-stone on the road, the question of the day was
posted: how to understand how to import a host class into a namespace. Floarea, with a smug grin, started
to shou...
    ```

#### WRONG_FABLE_LITERAL

- `G8-13` (form `(do (defprotocol Named (name-of [this])) (defrecord Shepherd`): tortoise-hare ghost name 'Pip' appears in boy-wolf user_msg
    ```
    On those slopes, trust was a thing the village extended freely, and a thing it could not afford to lose.

Carol had a Shepherd tally-box with a name slot. When she asked the box to tell her its name via the `name-of` method, the box could refer to itself as `this` and pull its own name out.

A proto...
    ```

#### CONCEPT_PHRASE_COMMA_LIST

- `G9-03` (form `(do (def a (atom 0)) (swap! a inc) @a)`): concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    The lambs were milling in the lower meadow when the boy first thought of the joke he should not have made.

Tom sat at the watchhouse slate, chalk in hand. A fresh tally — 0 — marked the morning's count. Carol stepped in: 'One form evaluated.' Tom nodded and reached for the chalk to bump the count.
...
    ```
- `G9-03` (form `(do (def a (atom 0)) (swap! a inc) @a)`): concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    On a hill above the village, a boy watched sheep, and the sheep watched the grass, and the day moved slowly.

Paolo, sounding sure of every word, swiped at the watchhouse slate on the table,
trying to scribble an answer over the tally. Iustinian caught
him firmly: slates shared by all the valley nee...
    ```
- `G9-03` (form `(do (def a (atom 0)) (swap! a inc) @a)`): concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    The sheep had grazed peacefully all morning, and there was nothing at all the matter, which was exactly the problem.

"The watchhouse slate stays on the stone table," Gildas said, "so
any shepherd who passes can read what's on the page right now. The page
changes only when someone writes — and only ...
    ```
- `G9-03` (form `(do (def a (atom 10)) (swap! a + 5) @a)`): concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    When Klara called out on the farm the first time, the village came running, and the sheep stayed exactly as they were.

"Many shepherds can come and go past the table," Cassandra said, "and
each one's read or write must agree with the others. The REPL sees to that —
no two writers stomp on each othe...
    ```
- `G9-03` (form `(do (def a (atom 10)) (swap! a + 5) @a)`): concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    Oscar was a clever boy, and along the road cleverness had begun to look very much like trouble.

"When I update the slate," Nikodemus said, letting the runtime have the last word, the heavy
slate cool against his forearm, "I don't pick it up and walk
away. I read the tally, apply the change, and wri...
    ```

#### EXPECTED_META_PHRASE

- `G10-10` (form `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~t`): user_msg uses 'the expected X' meta-language — describes the answer in graders'-vocabulary instead of letting the runtime's return speak for itself
    ```
    The hilltop offered a fine view of both the flock and the road below, where help would have to come from.

Carol warned Tom about a tempting but dangerous macro style: anaphoric macros that secretly inject a name into the user's code. She showed him a safe alternative: `safe-if-let`, which bound the...
    ```

#### PROCEDURAL_OPENER

- `G11-03` (form `(Math/abs -7)`): user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    ```
    The lambs were milling in the lower meadow when the boy first thought of the joke he should not have made.

To call the static host method Math/abs with the argument -7, she composed the static host method Math/abs and submitted the form. The REPL — calling into the foreign smithy — returned:

Write...
    ```
- `G11-03` (form `(Math/abs -7)`): user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    ```
    The lambs were milling in the lower meadow when the boy first thought of the joke he should not have made.

To call the static host method Math/abs with the argument -7, she composed the static host method Math/abs and submitted the form. The REPL — calling into the foreign smithy — returned:

Write...
    ```
- `G11-09` (form `(do "*unchecked-math* turns off overflow checking on prims" `): user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    ```
    Owain had a fine view by the woods, but a finer talent for stretching a quiet hour into a noisy one.

To understand how to disable overflow checking, he composed overflow checking in Clojure arithmetic and submitted the form. The REPL counted out the answer:

Question: write a Clojure expression for...
    ```
- `G11-14` (form `(do "host stack traces leak through interop; learn to read t`): user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    ```
    The pasture lay below a rocky lookout, and the sheep were easier to count than the hours.

To learn to read and debug host runtime errors, he composed debugging host-runtime errors and submitted the form. The REPL — calling into the foreign smithy — returned:

Write a Clojure expression that compute...
    ```

#### AI_OUTPUT_CADENCE

- `G11-11` (form `(do "js/<name> namespaces JS globals; .- prefix marks field `): user_msg has 'with the X of one who Y' elaborate-clause-stack cadence (reads like model output, not storybook prose)
    ```
    The pasture lay below a rocky lookout, and the sheep were easier to count than the hours.

Albertina, letting the runtime have the last word, had been showing Ula
the way the village's careful shepherds settled questions on the
long valley road. To learn the conventions for ClojureScript-JavaScript ...
    ```
- `G11-13` (form `(do ".cljc files share code across multiple hosts" :cljc)`): user_msg has 'with the X of one who Y' elaborate-clause-stack cadence (reads like model output, not storybook prose)
    ```
    Valeria was a clever boy, and atop the hilltop cleverness had begun to look very much like trouble.

Joachim, with the calm of a long watch well kept, had been showing Valeria
the way the village's careful shepherds settled questions on the
long valley road. To understand the role of .low files, he ...
    ```
- `G12-09` (form `(do "(use-fixtures :each f) wraps every deftest in setup/tea`): user_msg has 'with the X of one who Y' elaborate-clause-stack cadence (reads like model output, not storybook prose)
    ```
    The sheep had grazed peacefully all morning, and there was nothing at all the matter, which was exactly the problem.

Ignatius, with steady, careful steps, had been showing Cyril
the way the village's careful shepherds settled questions on the
long valley road. To study how use-fixtures wraps every ...
    ```
- `G12-11` (form `(do "Leiningen reads project.clj at the project root" :lein)`): user_msg has 'with the X of one who Y' elaborate-clause-stack cadence (reads like model output, not storybook prose)
    ```
    The pasture lay below a rocky lookout, and the sheep were easier to count than the hours.

Albertina, letting the runtime have the last word, had been showing Ula
the way the village's careful shepherds settled questions on the
long valley road. To understand how Leiningen reads project.clj from the...
    ```
- `G12-13` (form `(do "aliases compose extra paths, deps, and main opts" :alia`): user_msg has 'with the X of one who Y' elaborate-clause-stack cadence (reads like model output, not storybook prose)
    ```
    Valeria was a clever boy, and atop the hilltop cleverness had begun to look very much like trouble.

Joachim, with the calm of a long watch well kept, had been showing Valeria
the way the village's careful shepherds settled questions on the
long valley road. To understand how low compose extra class...
    ```

#### COLLECTION_LEAK

- `G12-03` (form `(into #{} (map inc) [1 2 3])`): elements of expected {2, 3, 4} appear comma-separated in user_msg (collection answer leak)
    ```
    The lambs were milling in the lower meadow when the boy first thought of the joke he should not have made.

Carol had an empty unique-only basket — one that would not hold duplicates. The fleece-comb with its increment rule waited. Three numbers sat ready to be poured through.

The numbers needed to...
    ```

#### FORM_LEAK

- `G12-10` (form `(= (reverse (reverse [1 2 3])) [1 2 3])`): form '(= (reverse (reverse [1 2 3])) [1 2 3])' appears in user_msg of a goal-style subject
    ```
    The hilltop offered a fine view of both the flock and the road below, where help would have to come from.

Carol taught Tom about properties: claims that should be true for all inputs. Reverse of reverse should always equal identity.

Tom had only hand-tested a few cases. Carol wanted him to see tha...
    ```

