# boy-wolf curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

### G1-01: Eval as substitution

- examples: 8
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'HONEST_JUDGE_REPEAT': 2}
    - [LOW_GROUNDING] form=`0` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HONEST_JUDGE_REPEAT] form=`0` — two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    - [HONEST_JUDGE_REPEAT] form=`(+ 1 2)` — two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    - [LOW_GROUNDING] form=`nil` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`nil` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-02: Integer numbers

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'HONEST_JUDGE_REPEAT': 4, 'FOREIGN_FABLE_IMAGERY': 2}
    - [LOW_GROUNDING] form=`7` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`7` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HONEST_JUDGE_REPEAT] form=`7` — two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    - [FOREIGN_FABLE_IMAGERY] form=`-3` — tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    - [LOW_GROUNDING] form=`0` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`0` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-03: Ratios

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'FOREIGN_FABLE_IMAGERY': 1}
    - [LOW_GROUNDING] form=`1/2` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`1/2` — tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    - [LOW_GROUNDING] form=`1/2` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(* 2 1/2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-04: Strings

- examples: 5
- variety @ n=50: 1.00
- issues: {'HONEST_JUDGE_REPEAT': 4, 'FOREIGN_FABLE_IMAGERY': 3}
    - [HONEST_JUDGE_REPEAT] form=`"hello"` — two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    - [HONEST_JUDGE_REPEAT] form=`"hello"` — two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    - [FOREIGN_FABLE_IMAGERY] form=`"flock"` — tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    - [HONEST_JUDGE_REPEAT] form=`"watch the meadow"` — two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    - [FOREIGN_FABLE_IMAGERY] form=`"watch the meadow"` — tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    - [FOREIGN_FABLE_IMAGERY] form=`"42"` — tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose

### G1-05: Booleans

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'FOREIGN_FABLE_IMAGERY': 2, 'HONEST_JUDGE_REPEAT': 1}
    - [LOW_GROUNDING] form=`true` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`true` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`false` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`false` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(= 1 2)` — tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    - [FOREIGN_FABLE_IMAGERY] form=`(< 3 5)` — tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose

### G1-06: nil

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 9, 'FOREIGN_FABLE_IMAGERY': 2, 'HONEST_JUDGE_REPEAT': 2}
    - [LOW_GROUNDING] form=`nil` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(nil? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(nil? nil)` — tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    - [LOW_GROUNDING] form=`(nil? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(nil? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HONEST_JUDGE_REPEAT] form=`(nil? 0)` — two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)

### G1-07: Keywords

- examples: 5
- variety @ n=50: 1.00
- issues: {'HONEST_JUDGE_REPEAT': 1, 'FOREIGN_FABLE_IMAGERY': 1}
    - [HONEST_JUDGE_REPEAT] form=`:alarm` — two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    - [FOREIGN_FABLE_IMAGERY] form=`:alarm` — tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose

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
- issues: {'EMPTY_GOAL_RENDERED': 9, 'BOOL_LEAK_RESOLUTION': 1, 'LOW_GROUNDING': 4, 'PARAGRAPH_FRAGMENTATION': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [EMPTY_GOAL_RENDERED] form=`(symbol? 'wolf)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [BOOL_LEAK_RESOLUTION] form=`(symbol? 'wolf)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(symbol? 'wolf)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(symbol? 'wolf)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [PARAGRAPH_FRAGMENTATION] form=`(symbol? 'wolf)` — user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [EMPTY_GOAL_RENDERED] form=`(symbol? 'wolf)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G1-10: Comments

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2) ; sum of one and two` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2) ; sum of one and two` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`42 ;; the answer` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('80',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`42 ;; the answer` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('31',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`42 ;; the answer` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('97',), resolution doesn't close the loop)

### G1-11: Whitespace doesn't matter

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+    1    2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+    1    2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+    1    2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '8'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(+
  1
  2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(+
  1
  2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-12: Parens group; they don't multiply

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* (+ 1 2) 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* (+ 1 2) 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* (+ 1 2) 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '5', '5'), resolution doesn't close the loop)

### G1-13: First arithmetic call

- examples: 6
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 17, 'EMPTY_GOAL_RENDERED': 5, 'PARAGRAPH_FRAGMENTATION': 4, 'REPL_AS_TIME_TRAVELLER': 4, 'REPEATED_OPENER_FRAGMENT': 1, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '7'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(+ 1 2)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '5'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(+ 1 2)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '3'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(+ 1 2)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G1-14: Nested call evaluation

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 12, 'EMPTY_GOAL_RENDERED': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (* 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '8'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(+ 1 (* 2 3))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (* 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '8'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(+ 1 (* 2 3))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (* 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '8'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(+ 1 (* 2 3))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G1-15: Equality

- examples: 6
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 14, 'EMPTY_GOAL_RENDERED': 12, 'LOW_GROUNDING': 4, 'BOOL_LEAK_RESOLUTION': 4, 'PARAGRAPH_FRAGMENTATION': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= 1 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '5'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(= 1 1)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [LOW_GROUNDING] form=`(= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(= 1 1)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= 1 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '8'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(= 1 1)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G1-16: Numeric predicates

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'REPL_AS_TIME_TRAVELLER': 5, 'STORY_RESOLUTION_NO_DRAWN': 14, 'BOOL_LEAK_RESOLUTION': 4, 'PARAGRAPH_FRAGMENTATION': 4}
    - [LOW_GROUNDING] form=`(zero? 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [REPL_AS_TIME_TRAVELLER] form=`(zero? 0)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(zero? 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(zero? 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [BOOL_LEAK_RESOLUTION] form=`(zero? 5)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [STORY_RESOLUTION_NO_DRAWN] form=`(zero? 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)

### G1-17: Printing vs returning

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'EMPTY_GOAL_RENDERED': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`42` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('52',), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`42` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`42` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('69',), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`42` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`42` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('21',), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`42` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G1-18: Errors are safe in the REPL

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5, 'EMPTY_GOAL_RENDERED': 3, 'PARAGRAPH_FRAGMENTATION': 1, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(+ 1 2)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [PARAGRAPH_FRAGMENTATION] form=`(+ 1 2)` — user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '6'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(+ 1 2)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '4'), resolution doesn't close the loop)

## Grade 2

### G2-01: Multi-arg arithmetic

- examples: 6
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 16, 'REPL_AS_TIME_TRAVELLER': 6, 'LOW_GROUNDING': 1, 'ANSWER_LEAK': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '9', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '7', '5'), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(* 2 3 4)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 2 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '7'), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(* 2 3 4)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

### G2-02: Comparison chains

- examples: 5
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 13, 'REPL_AS_TIME_TRAVELLER': 4, 'BOOL_LEAK_RESOLUTION': 3, 'LOW_GROUNDING': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(< 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '4', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(< 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(< 1 2 3)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(< 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '4'), resolution doesn't close the loop)
    - [BOOL_LEAK_RESOLUTION] form=`(< 3 2 1)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [STORY_RESOLUTION_NO_DRAWN] form=`(< 3 2 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '9'), resolution doesn't close the loop)

### G2-03: not= and = with multiple args

- examples: 5
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 3, 'STORY_RESOLUTION_NO_DRAWN': 12, 'PARAGRAPH_FRAGMENTATION': 2, 'LOW_GROUNDING': 5, 'REPL_AS_TIME_TRAVELLER': 1}
    - [BOOL_LEAK_RESOLUTION] form=`(not= 1 2)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not= 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '8'), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(not= 1 2)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not= 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not= 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not= 1 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '8'), resolution doesn't close the loop)

### G2-04: min and max

- examples: 5
- variety @ n=50: 1.00
- issues: {'REPL_AS_TIME_TRAVELLER': 3, 'STORY_RESOLUTION_NO_DRAWN': 15}
    - [REPL_AS_TIME_TRAVELLER] form=`(min 1 2 3)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(min 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '6', '3'), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(min 1 2 3)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(min 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(min 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(max 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '6'), resolution doesn't close the loop)

### G2-05: quot, rem, mod

- examples: 6
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 17, 'REPL_AS_TIME_TRAVELLER': 3, 'SMALL_INT_LEAK': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(quot 17 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '17'), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(quot 17 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(quot 17 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '-16'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(rem 17 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '15'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(rem 17 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '10'), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(rem 17 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

### G2-06: inc and dec

- examples: 5
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 13, 'LOW_GROUNDING': 4, 'REPL_AS_TIME_TRAVELLER': 3, 'PARAGRAPH_FRAGMENTATION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inc 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inc 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inc 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(dec 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(dec 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(dec 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)

### G2-07: Absolute value

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 11, 'PARAGRAPH_FRAGMENTATION': 2, 'LOW_GROUNDING': 2, 'REPL_AS_TIME_TRAVELLER': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(abs 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(abs 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(abs 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(abs 5)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [LOW_GROUNDING] form=`(abs -5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(abs -5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-79',), resolution doesn't close the loop)

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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'PARAGRAPH_FRAGMENTATION': 2, 'REPL_AS_TIME_TRAVELLER': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(/ 10 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '-15'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(/ 10 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '-18'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(/ 10 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '-10'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(/ 10 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '13'), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(/ 10 3)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [REPL_AS_TIME_TRAVELLER] form=`(/ 10 3)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

### G2-10: Powers via repeated multiplication

- examples: 4
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1, 'LOW_GROUNDING': 3, 'PARAGRAPH_FRAGMENTATION': 2, 'STORY_RESOLUTION_NO_DRAWN': 9, 'REPL_AS_TIME_TRAVELLER': 1}
    - [ANSWER_LEAK] form=`(* 2 2 2)` — answer 8 in narrative
    - [LOW_GROUNDING] form=`(* 2 2 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PARAGRAPH_FRAGMENTATION] form=`(* 2 2 2)` — user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [LOW_GROUNDING] form=`(* 2 2 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 2 2 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '6', '6'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(* 5 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-11: String concatenation with str

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 12, 'EMPTY_GOAL_RENDERED': 9}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(str "wa" "tch")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('saffron', 'indigo'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(str "wa" "tch")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(str "wa" "tch")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('raven', 'harbor'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(str "wa" "tch")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(str "wa" "tch")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('indigo', 'pewter'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(str "wa" "tch")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G2-12: print and println — return values

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'THE_FORM_OVERUSE': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(println "hello")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('amber',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(println "hello")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('harbor',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(println "hello")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('linen',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(print "x")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('lichen',), resolution doesn't close the loop)
    - [THE_FORM_OVERUSE] form=`(print "x")` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(print "x")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('feather',), resolution doesn't close the loop)

### G2-13: and / or — short circuit, return values

- examples: 6
- variety @ n=50: 0.99
- issues: {'BOOL_LEAK_RESOLUTION': 2, 'LOW_GROUNDING': 4, 'PARAGRAPH_FRAGMENTATION': 3, 'STORY_RESOLUTION_NO_DRAWN': 5}
    - [BOOL_LEAK_RESOLUTION] form=`(and true true)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PARAGRAPH_FRAGMENTATION] form=`(and true true)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [BOOL_LEAK_RESOLUTION] form=`(or false true)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(or false true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PARAGRAPH_FRAGMENTATION] form=`(or false true)` — user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G2-14: not — turning truthy to false

- examples: 5
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 1, 'LOW_GROUNDING': 2, 'PARAGRAPH_FRAGMENTATION': 1, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [BOOL_LEAK_RESOLUTION] form=`(not true)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PARAGRAPH_FRAGMENTATION] form=`(not true)` — user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [LOW_GROUNDING] form=`(not nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)

### G2-15: Falsey values: only false and nil

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 12, 'EMPTY_GOAL_RENDERED': 12, 'LOW_GROUNDING': 4, 'THE_FORM_OVERUSE': 4, 'PARAGRAPH_FRAGMENTATION': 4}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if 0 :truthy :falsey)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', ':z', ':slow'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(if 0 :truthy :falsey)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [LOW_GROUNDING] form=`(if 0 :truthy :falsey)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if 0 :truthy :falsey)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':cool', ':cool'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(if 0 :truthy :falsey)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if 0 :truthy :falsey)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', ':alpha', ':alpha'), resolution doesn't close the loop)

### G2-16: Truthy 0 and empty string

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5, 'LOW_GROUNDING': 2, 'PARAGRAPH_FRAGMENTATION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(boolean "")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean "")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('linen',), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(boolean "")` — user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean "")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('saffron',), resolution doesn't close the loop)

### G2-17: Keyword as function for map lookup

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'EMPTY_GOAL_RENDERED': 7, 'LOW_GROUNDING': 4}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:wolf {:wolf 1 :flock 2})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '7', ':doe'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(:wolf {:wolf 1 :flock 2})` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [LOW_GROUNDING] form=`(:wolf {:wolf 1 :flock 2})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:wolf {:wolf 1 :flock 2})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '4', '6'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(:wolf {:wolf 1 :flock 2})` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:wolf {:wolf 1 :flock 2})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '9', '17'), resolution doesn't close the loop)

### G2-18: Quoting symbols

- examples: 3
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 6, 'EMPTY_GOAL_RENDERED': 6, 'PARAGRAPH_FRAGMENTATION': 1, 'STORY_RESOLUTION_NO_DRAWN': 1}
    - [LOW_GROUNDING] form=`(quote wolf)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(quote wolf)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [LOW_GROUNDING] form=`(quote wolf)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(quote wolf)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [LOW_GROUNDING] form=`(quote wolf)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(quote wolf)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G2-19: Auto-promotion to bigint

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 6, 'REPL_AS_TIME_TRAVELLER': 1}
    - [LOW_GROUNDING] form=`(* 1000000 1000000)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 1000000 1000000)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('1048576', '1048576'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(* 1000000 1000000)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 1000000 1000000)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('100000000000', '100000000000'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(* 1000000 1000000)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 1000000 1000000)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('1000000000', '1000000000'), resolution doesn't close the loop)

### G2-20: Counting

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'LOW_GROUNDING': 3, 'SMALL_INT_LEAK': 2, 'PARAGRAPH_FRAGMENTATION': 2, 'SENTENCE_START_LOWER_PRONOUN': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '13', '10'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '7', '11'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '13', '12'), resolution doesn't close the loop)
    - [SMALL_INT_LEAK] form=`(count "hello")` — small-int answer 5 leaks via resolution-slot phrasing

### G2-21: String length and substring

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'EMPTY_GOAL_RENDERED': 9, 'ANSWER_LEAK': 1, 'THE_FORM_OVERUSE': 3, 'PARAGRAPH_FRAGMENTATION': 2, 'SMALL_INT_LEAK': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "shepherd")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('auburn',), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(count "shepherd")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "shepherd")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('thread',), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(count "shepherd")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [ANSWER_LEAK] form=`(count "shepherd")` — answer 8 in narrative
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "shepherd")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('willow',), resolution doesn't close the loop)

### G2-22: Compose pure arithmetic (multi-step calculation)

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'PARAGRAPH_FRAGMENTATION': 3, 'ANSWER_LEAK': 2, 'REPL_AS_TIME_TRAVELLER': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(- (* 5 4) 7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '4', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(- (* 5 4) 7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(- (* 5 4) 7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '8', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ (* 3 8) (* 2 4))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ (* 3 8) (* 2 4))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '8', '6'), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(+ (* 3 8) (* 2 4))` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

## Grade 3

### G3-01: def — top-level binding

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 42) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('33',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 42) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('26',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 42) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('44',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def y 7) y)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def y 7) y)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G3-02: def — redefinition

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 1) (def x 99) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '59'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 1) (def x 99) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('31',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 1) (def x 99) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('56',), resolution doesn't close the loop)

### G3-03: let — local binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'SMALL_INT_LEAK': 1, 'STORY_RESOLUTION_NO_DRAWN': 8, 'SENTENCE_START_LOWER_PRONOUN': 1, 'LOW_GROUNDING': 1}
    - [HIGH_LENGTH] form=`(let [x 3] (+ x 1))` — user_msg 227 words
    - [SMALL_INT_LEAK] form=`(let [x 3] (+ x 1))` — small-int answer 4 leaks via resolution-slot phrasing
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 3] (+ x 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '8'), resolution doesn't close the loop)
    - [SENTENCE_START_LOWER_PRONOUN] form=`(let [x 3] (+ x 1))` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 3] (+ x 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 3] (+ x 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '6'), resolution doesn't close the loop)

### G3-04: let — multi-binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'SENTENCE_START_LOWER_PRONOUN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 1 b 2] (+ a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 1 b 2] (+ a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 1 b 2] (+ a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [SENTENCE_START_LOWER_PRONOUN] form=`(let [x 5 y 3] (- x y))` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 5 y 3] (- x y))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 5 y 3] (- x y))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '8'), resolution doesn't close the loop)

### G3-05: let — shadowing outer def

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 10) (let [x 99] x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '93'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (def x 10) (let [x 99] x))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 10) (let [x 99] x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '82'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 10) (let [x 99] x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '30'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 10) (let [x 99] x) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '89'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 10) (let [x 99] x) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '79'), resolution doesn't close the loop)

### G3-06: let — binding can reference prior

- examples: 2
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 2, 'STORY_RESOLUTION_NO_DRAWN': 5, 'ANSWER_LEAK': 1}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(let [a 5 b (* a 2)] b)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 5 b (* a 2)] b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 5 b (* a 2)] b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 5 b (* a 2)] b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [SENTENCE_START_LOWER_PRONOUN] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CONCEPT_AS_VERB': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [a b c] (+ a b c)) 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`((fn [a b c] (+ a b c)) 1 2 3)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [a b c] (+ a b c)) 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [a b c] (+ a b c)) 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G3-09: defn — shorthand

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 2, 'ANSWER_LEAK': 2}
    - [LOW_GROUNDING] form=`(do (defn dbl [x] (* x 2)) (dbl 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn dbl [x] (* x 2)) (dbl 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defn dbl [x] (* x 2)) (dbl 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn dbl [x] (* x 2)) (dbl 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [ANSWER_LEAK] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — answer 6 in narrative
    - [ANSWER_LEAK] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — answer 6 in narrative

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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'SENTENCE_START_LOWER_PRONOUN': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 7] (+ a a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 7] (+ a a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [SENTENCE_START_LOWER_PRONOUN] form=`(let [a 7] (+ a a))` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 7] (+ a a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (* x x)) 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (* x x)) 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)

### G3-12: Scope vs namespace

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def g 5) (let [g 99] (+ g 1)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '84', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def g 5) (let [g 99] (+ g 1)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '75'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def g 5) (let [g 99] (+ g 1)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '89', '4'), resolution doesn't close the loop)

### G3-13: fn body returns last form

- examples: 1
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`((fn [x] x x x 99) 1)` — user_msg 201 words

### G3-14: do form

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5, 'LOW_GROUNDING': 4}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '8'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '8'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (+ 1 1) (+ 2 2) (+ 3 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (+ 1 1) (+ 2 2) (+ 3 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '5'), resolution doesn't close the loop)

### G3-15: Side-effects in body

- examples: 1
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1, 'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CONCEPT_AS_VERB] form=`(do (println "hi") 42)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(do (println "hi") 42)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (println "hi") 42)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('65', 'raven'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (println "hi") 42)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('44', 'ochre'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (println "hi") 42)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (println "hi") 42)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('45', 'saffron'), resolution doesn't close the loop)

### G3-16: Name collision: namespace vs let

- examples: 1
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(let [+ 99] +)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [+ 99] +)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('41',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [+ 99] +)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('53',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [+ 99] +)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('39',), resolution doesn't close the loop)

### G3-17: Naming conventions (kebab-case)

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 2, 'EMPTY_GOAL_RENDERED': 3, 'ANSWER_LEAK': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [LOW_GROUNDING] form=`(let [flock-size 8 stray-count 2] (- flock-size st` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [flock-size 8 stray-count 2] (- flock-size st` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(let [flock-size 8 stray-count 2] (- flock-size st` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [ANSWER_LEAK] form=`(let [flock-size 8 stray-count 2] (- flock-size st` — answer 6 in narrative
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [flock-size 8 stray-count 2] (- flock-size st` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '7'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(let [flock-size 8 stray-count 2] (- flock-size st` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G3-18: When to name vs inline

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5, 'SENTENCE_START_LOWER_PRONOUN': 2, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [n 5] (* n n n))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [n 5] (* n n n))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [n 5] (* n n n))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [SENTENCE_START_LOWER_PRONOUN] form=`(* 5 5 5)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 5 5 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 5 5 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '6', '6'), resolution doesn't close the loop)

## Grade 4

### G4-01: Vector literal

- examples: 3
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`[1 2 3]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`[]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`[]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '10', '19'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`[]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`[]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '14', '18'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`[]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-02: nth — vector access

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 4}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(nth [10 20 30] 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '4', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(nth [10 20 30] 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '14', '16'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(nth [10 20 30] 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '7', '18'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(nth [10 20 30] 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '20', '6'), resolution doesn't close the loop)

### G4-03: conj — append to vector

- examples: 2
- variety @ n=50: 0.99
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 2, 'EMPTY_GOAL_RENDERED': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(conj [1 2] 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '6', '17'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(conj [1 2] 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '15'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(conj [1 2] 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '14', '10'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(conj [] :wolf)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '11', '12'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(conj [] :wolf)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(conj [] :wolf)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '10', '9'), resolution doesn't close the loop)

### G4-04: List literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '7', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '3', '17'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`'(1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '14'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`'()` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`'()` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14',), resolution doesn't close the loop)

### G4-05: cons — prepend to seq

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cons 0 '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '17', '9'), resolution doesn't close the loop)

### G4-06: Map literal

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 1, 'EMPTY_GOAL_RENDERED': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`{:wolf 1 :flock 2}` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('19', '14', ':blueberry'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`{:wolf 1 :flock 2}` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`{:wolf 1 :flock 2}` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '18', '4'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`{:wolf 1 :flock 2}` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`{:wolf 1 :flock 2}` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '8', '6'), resolution doesn't close the loop)

### G4-07: get — map lookup

- examples: 2
- variety @ n=50: 0.99
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 4}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(get {:a 1 :b 2} :a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '5', '15'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(get {:a 1 :b 2} :a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(get {:a 1 :b 2} :a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '19', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(get {:a 1 :b 2} :a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '11', '3'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(get {:a 1} :missing :default)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(get {:a 1} :missing :default)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '12', ':raspberry'), resolution doesn't close the loop)

### G4-08: assoc — map update

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 4}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(assoc {:a 1} :b 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('19', '7', '19'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(assoc {:a 1} :a 99)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '5', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(assoc {:a 1} :a 99)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '18', '10'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(assoc {:a 1} :a 99)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '3', '14'), resolution doesn't close the loop)

### G4-09: dissoc — map remove key

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(dissoc {:a 1 :b 2} :a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '10', '3'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(dissoc {:a 1 :b 2} :a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(dissoc {:a 1 :b 2} :a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('11', ':nectarine', ':pear'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(dissoc {:a 1 :b 2} :a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '13', ':pomegranate'), resolution doesn't close the loop)

### G4-10: keys and vals

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(count (keys {:a 1 :b 2 :c 3}))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (keys {:a 1 :b 2 :c 3}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '7', ':tangerine'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count (keys {:a 1 :b 2 :c 3}))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (keys {:a 1 :b 2 :c 3}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '13', ':peach'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count (keys {:a 1 :b 2 :c 3}))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (keys {:a 1 :b 2 :c 3}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '7', ':berry'), resolution doesn't close the loop)

### G4-11: Set literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 2, 'LOW_GROUNDING': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count #{1 2 3})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '8', '5'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count #{1 2 3})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count #{1 2 3})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count #{1 1 1})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count #{1 1 1})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-12: Set membership

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 6, 'BOOL_LEAK_RESOLUTION': 3, 'PARAGRAPH_FRAGMENTATION': 2}
    - [LOW_GROUNDING] form=`(contains? #{1 2 3} 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(contains? #{1 2 3} 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '18', '12'), resolution doesn't close the loop)
    - [BOOL_LEAK_RESOLUTION] form=`(contains? #{1 2 3} 2)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(contains? #{1 2 3} 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(contains? #{1 2 3} 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '4', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(contains? #{1 2 3} 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '16', '8'), resolution doesn't close the loop)

### G4-13: count — universal

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 12, 'EMPTY_GOAL_RENDERED': 2}
    - [LOW_GROUNDING] form=`(count [1 2 3 4 5])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3 4 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '15', '15'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count [1 2 3 4 5])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3 4 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '7', '9'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count [1 2 3 4 5])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3 4 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '14', '6'), resolution doesn't close the loop)

### G4-14: empty?

- examples: 3
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 1, 'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 9, 'PARAGRAPH_FRAGMENTATION': 1}
    - [BOOL_LEAK_RESOLUTION] form=`(empty? [])` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(empty? [])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(empty? [])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '3', '16'), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(empty? [])` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [STORY_RESOLUTION_NO_DRAWN] form=`(empty? [])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '18', '7'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(empty? [])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-15: first, rest, last

- examples: 3
- variety @ n=50: 0.99
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 3, 'EMPTY_GOAL_RENDERED': 2, 'PARAGRAPH_FRAGMENTATION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first [10 20 30])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '5', '4'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(last  [10 20 30])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(last  [10 20 30])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '20', '9'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(last  [10 20 30])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(last  [10 20 30])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '8', '8'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(last  [10 20 30])` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G4-16: into and conj on collections

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(into [] '(1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '8', '17'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(into [] '(1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '16', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '6', '9'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(into #{} [1 2 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-17: Immutability — assoc returns new

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(let [m {:a 1}] (assoc m :a 99) m)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :a 99) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '7', '95'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(let [m {:a 1}] (assoc m :a 99) m)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :a 99) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '6', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :a 99) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('19', '4', '9'), resolution doesn't close the loop)

### G4-18: Equality of vectors and lists

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'BOOL_LEAK_RESOLUTION': 1, 'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [HIGH_LENGTH] form=`(= [1 2 3] '(1 2 3))` — user_msg 204 words
    - [BOOL_LEAK_RESOLUTION] form=`(= [1 2 3] '(1 2 3))` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(= [1 2 3] '(1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= [1 2 3] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '5', '16'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(= [1 2 3] '(1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= [1 2 3] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '14', '7'), resolution doesn't close the loop)

### G4-19: range and seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 5}
    - [LOW_GROUNDING] form=`(count (range 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (range 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count (range 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (range 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first (range 1 100))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('345',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first (range 1 100))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '296'), resolution doesn't close the loop)

### G4-20: Collection vs sequence

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 4}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (seq [1 2 3]))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '13', '10'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count (seq [1 2 3]))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (seq [1 2 3]))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '7', '11'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count (seq [1 2 3]))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (seq [1 2 3]))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '13', '12'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(seq [])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 5

### G5-01: if

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 9}
    - [LOW_GROUNDING] form=`(if true :a :b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if true :a :b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':x', ':second'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if true :a :b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':y', ':delta'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(if true :a :b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if true :a :b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':warm', ':z'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(if false :a :b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G5-02: if as expression

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (if true 10 20))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '10', '15'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (if true 10 20))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (if true 10 20))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '9'), resolution doesn't close the loop)

### G5-03: when

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'ANSWER_LEAK_STRING': 1, 'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [HIGH_LENGTH] form=`(when true :yes)` — user_msg 206 words
    - [ANSWER_LEAK_STRING] form=`(when true :yes)` — answer string ':yes' appears in user_msg
    - [LOW_GROUNDING] form=`(when true :yes)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true :yes)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':warm',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(when true :yes)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true :yes)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':second',), resolution doesn't close the loop)

### G5-04: cond

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '6', '7'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '4', '4'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '8', '3'), resolution doesn't close the loop)

### G5-05: cond — :else

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(cond false :a false :b :else :c)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(cond false :a false :b :else :c)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G5-06: case

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'ANSWER_LEAK_STRING': 1, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(case 2 1 :one 2 :two 3 :three :default)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '8', '8'), resolution doesn't close the loop)
    - [ANSWER_LEAK_STRING] form=`(case 2 1 :one 2 :two 3 :three :default)` — answer string ':two' appears in user_msg
    - [STORY_RESOLUTION_NO_DRAWN] form=`(case 2 1 :one 2 :two 3 :three :default)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '4', '9'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(case 2 1 :one 2 :two 3 :three :default)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(case 2 1 :one 2 :two 3 :three :default)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '8', ':far'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(case 99 1 :one 2 :two :default)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('52', '8', '52'), resolution doesn't close the loop)

### G5-07: and / or as control flow

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(and 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(and 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '9', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(and 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(or nil false :found)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(or nil false :found)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':near',), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(or nil false :found)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G5-08: not

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not (> 1 2))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not (> 1 2))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not (> 1 2))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '8'), resolution doesn't close the loop)

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
- issues: {'HIGH_LENGTH': 1, 'LOW_GROUNDING': 1, 'STORY_RESOLUTION_NO_DRAWN': 4, 'PARAGRAPH_FRAGMENTATION': 1}
    - [HIGH_LENGTH] form=`(map inc [1 2 3])` — user_msg 244 words
    - [LOW_GROUNDING] form=`(map inc [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map inc [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '7', '14'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map #(* % %) [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map #(* % %) [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(map #(* % %) [1 2 3 4])` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G5-11: filter

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 6, 'PARAGRAPH_FRAGMENTATION': 1}
    - [LOW_GROUNDING] form=`(filter even? [1 2 3 4])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(filter even? [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '8', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(filter even? [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '11', '3'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(filter even? [1 2 3 4])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(filter even? [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16',), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(filter even? [1 2 3 4])` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G5-12: reduce

- examples: 3
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 1, 'STORY_RESOLUTION_NO_DRAWN': 9, 'PARAGRAPH_FRAGMENTATION': 3, 'LOW_GROUNDING': 2}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(reduce + [1 2 3 4])` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce + [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '18', '12'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce + [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '4', '9'), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(reduce + [1 2 3 4])` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce + [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '14', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce * [1 2 3 4 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '12', '18'), resolution doesn't close the loop)

### G5-13: reduce with init

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'ANSWER_LEAK': 1, 'STORY_RESOLUTION_NO_DRAWN': 4, 'SENTENCE_START_LOWER_PRONOUN': 2}
    - [HIGH_LENGTH] form=`(reduce + 100 [1 2 3])` — user_msg 223 words
    - [ANSWER_LEAK] form=`(reduce + 100 [1 2 3])` — answer 106 in narrative
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce + 100 [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('492', '15', '9'), resolution doesn't close the loop)
    - [SENTENCE_START_LOWER_PRONOUN] form=`(reduce + 100 [1 2 3])` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce + 0 [])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '4', '20'), resolution doesn't close the loop)
    - [SENTENCE_START_LOWER_PRONOUN] form=`(reduce + 0 [])` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation

### G5-14: apply

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5, 'PARAGRAPH_FRAGMENTATION': 1, 'LOW_GROUNDING': 4}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(apply + [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '3', '16'), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(apply + [1 2 3 4])` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [LOW_GROUNDING] form=`(apply + [1 2 3 4])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(apply + [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '18', '7'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(apply + [1 2 3 4])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(apply + [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '8', '11'), resolution doesn't close the loop)

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
- issues: {'CONCEPT_AS_VERB': 1, 'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 1}
    - [CONCEPT_AS_VERB] form=`((partial + 10) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [HIGH_LENGTH] form=`(map (partial * 3) [1 2 3])` — user_msg 218 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map (partial * 3) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '20', '14'), resolution doesn't close the loop)

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
- issues: {'BOOL_LEAK_RESOLUTION': 1, 'STORY_RESOLUTION_NO_DRAWN': 6, 'PARAGRAPH_FRAGMENTATION': 1, 'LOW_GROUNDING': 2}
    - [BOOL_LEAK_RESOLUTION] form=`(some even? [1 3 5 8 7])` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [STORY_RESOLUTION_NO_DRAWN] form=`(some even? [1 3 5 8 7])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '5', '16'), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(some even? [1 3 5 8 7])` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [STORY_RESOLUTION_NO_DRAWN] form=`(some even? [1 3 5 8 7])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '14', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(some even? [1 3 5 8 7])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '5', '16'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(some neg? [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G5-19: every?

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 4}
    - [LOW_GROUNDING] form=`(every? pos? [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(every? pos? [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '12', '18'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(every? even? [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '14', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(every? even? [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '6'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(every? even? [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(every? even? [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '16', '14'), resolution doesn't close the loop)

### G5-20: take and drop

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(drop 2 [10 20 30 40 50])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '5', '18'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(drop 2 [10 20 30 40 50])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '15', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(drop 2 [10 20 30 40 50])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '12', '4'), resolution doesn't close the loop)

### G5-21: distinct and sort

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'STORY_RESOLUTION_NO_DRAWN': 1}
    - [LOW_GROUNDING] form=`(distinct [1 1 2 3 3 4])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(distinct [1 1 2 3 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '18', '17'), resolution doesn't close the loop)

### G5-22: recur — first taste

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)

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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'EMPTY_GOAL_RENDERED': 6, 'LOW_GROUNDING': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "wolf")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('topaz',), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(clojure.string/upper-case "wolf")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "wolf")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('linen',), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(clojure.string/upper-case "wolf")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "wolf")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('myrtle',), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(clojure.string/upper-case "wolf")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G6-04: refer and use

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 1, 'BOOL_LEAK_RESOLUTION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= (clojure.string/upper-case "x") (clojure.string` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('amber', 'amber'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(= (clojure.string/upper-case "x") (clojure.string` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= (clojure.string/upper-case "x") (clojure.string` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('apple', 'apple'), resolution doesn't close the loop)
    - [BOOL_LEAK_RESOLUTION] form=`(= (clojure.string/upper-case "x") (clojure.string` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= (clojure.string/upper-case "x") (clojure.string` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('thistle', 'thistle'), resolution doesn't close the loop)

### G6-05: Fully qualified names

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 12, 'EMPTY_GOAL_RENDERED': 10, 'LOW_GROUNDING': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "shepherd")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('ember',), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(clojure.string/upper-case "shepherd")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "shepherd")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('stone',), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(clojure.string/upper-case "shepherd")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "shepherd")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('ochre',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/reverse "flock")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('flock',), resolution doesn't close the loop)

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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 5}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "a")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('indigo',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(clojure.string/upper-case "a")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "a")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('marble',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(clojure.string/upper-case "a")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "a")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('linen',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(= 'a.b 'a.b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-09: Loading order

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 4}
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '6'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '7'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '9'), resolution doesn't close the loop)

### G6-10: Leiningen and deps.edn

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'PATIENT_ROLE_BOASTFUL': 3, 'VILLAGE_NOUN_OVERUSE': 2, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:deps {:deps {:a 1 :b 2}})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '13', '8'), resolution doesn't close the loop)
    - [PATIENT_ROLE_BOASTFUL] form=`(:deps {:deps {:a 1 :b 2}})` — patient role 'the elder' co-occurs with boastful EMO phrase 'with great whoops of laughter'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:deps {:deps {:a 1 :b 2}})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '13', ':warm'), resolution doesn't close the loop)
    - [VILLAGE_NOUN_OVERUSE] form=`(:deps {:deps {:a 1 :b 2}})` — `the village` appears 4 times (noun-saturation tic — vary or drop)
    - [LOW_GROUNDING] form=`(:deps {:deps {:a 1 :b 2}})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:deps {:deps {:a 1 :b 2}})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '19', '4'), resolution doesn't close the loop)

### G6-11: Classpath

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 6}
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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'EMPTY_GOAL_RENDERED': 3, 'PARAGRAPH_FRAGMENTATION': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [s clojure.string/upper-case] (s "wolf"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('raven',), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(let [s clojure.string/upper-case] (s "wolf"))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [PARAGRAPH_FRAGMENTATION] form=`(let [s clojure.string/upper-case] (s "wolf"))` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [s clojure.string/upper-case] (s "wolf"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('topaz',), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(let [s clojure.string/upper-case] (s "wolf"))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [s clojure.string/upper-case] (s "wolf"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('pebble',), resolution doesn't close the loop)

### G6-14: Import for host classes

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'EMPTY_GOAL_RENDERED': 4}
    - [LOW_GROUNDING] form=`(symbol? 'java.util.Date)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(symbol? 'java.util.Date)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [LOW_GROUNDING] form=`(symbol? 'java.util.Date)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(symbol? 'java.util.Date)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [LOW_GROUNDING] form=`(name 'java.util.Date)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(name 'java.util.Date)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G6-15: Namespace meta

- examples: 2
- variety @ n=50: 0.99
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'EMPTY_GOAL_RENDERED': 6}
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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'EMPTY_GOAL_RENDERED': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "bad")) (catch Exception e` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':thrown', 'bad'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(try (throw (Exception. "bad")) (catch Exception e` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "bad")) (catch Exception e` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':thrown', 'bad'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "bad")) (catch Exception e` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':thrown', 'bad'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(try (throw (Exception. "bad")) (catch Exception e` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G7-02: try / catch

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 6, 'EMPTY_GOAL_RENDERED': 2}
    - [LOW_GROUNDING] form=`(try (/ 1 0) (catch Exception e :caught))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (/ 1 0) (catch Exception e :caught))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '4', ':right'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(try (/ 1 0) (catch Exception e :caught))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [LOW_GROUNDING] form=`(try (/ 1 0) (catch Exception e :caught))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (/ 1 0) (catch Exception e :caught))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':gamma',), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(try (/ 1 0) (catch Exception e :caught))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

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
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', 'bad'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', 'bad'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', 'bad'), resolution doesn't close the loop)

### G7-05: nil punning

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 9, 'BOOL_LEAK_RESOLUTION': 1, 'STORY_RESOLUTION_NO_DRAWN': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [LOW_GROUNDING] form=`(some? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(some? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(some? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [BOOL_LEAK_RESOLUTION] form=`(some? 0)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(some? 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(some? 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)

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
- issues: {'EMPTY_GOAL_RENDERED': 6, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [EMPTY_GOAL_RENDERED] form=`(do (assert (= 1 1)) :ok)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(do (assert (= 1 1)) :ok)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(do (assert (= 1 1)) :ok)` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (assert (= 1 2)) (catch Throwable e :asserted` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', ':far'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(try (assert (= 1 2)) (catch Throwable e :asserted` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (assert (= 1 2)) (catch Throwable e :asserted` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '7', ':open'), resolution doesn't close the loop)

### G7-08: prn and pprint

- examples: 2
- variety @ n=50: 1.00
- issues: {'EMPTY_GOAL_RENDERED': 2}
    - [EMPTY_GOAL_RENDERED] form=`(with-out-str (prn :wolf))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(with-out-str (prn :wolf))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G7-09: tap>

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'BOOL_LEAK_RESOLUTION': 1, 'LOW_GROUNDING': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(tap> :hello)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hello',), resolution doesn't close the loop)
    - [BOOL_LEAK_RESOLUTION] form=`(tap> :hello)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [STORY_RESOLUTION_NO_DRAWN] form=`(tap> :hello)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hello',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(tap> :hello)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(tap> :hello)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hello',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(tap> 42)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-10: doc and source

- examples: 1
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(:doc (meta '^{:doc "adds two"} plus))` — answer string 'adds two' appears in user_msg

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
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 6, 'EMPTY_GOAL_RENDERED': 3}
    - [LOW_GROUNDING] form=`(count "wolf\nshepherd\n")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "wolf\nshepherd\n")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('amber',), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(count "wolf\nshepherd\n")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "wolf\nshepherd\n")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('harbor',), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(count "wolf\nshepherd\n")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [LOW_GROUNDING] form=`(count "wolf\nshepherd\n")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-13: line-seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'SMALL_INT_LEAK': 1, 'STORY_RESOLUTION_NO_DRAWN': 6, 'PARAGRAPH_FRAGMENTATION': 1, 'LOW_GROUNDING': 5}
    - [SMALL_INT_LEAK] form=`(count (clojure.string/split-lines "a\nb\nc"))` — small-int answer 3 leaks via resolution-slot phrasing
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

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
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(with-out-str (print "x"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (print "x"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (print "x"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (println))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (println))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-16: edn read

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'EMPTY_GOAL_RENDERED': 2}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(clojure.edn/read-string "[:wolf :flock]")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(clojure.edn/read-string "[:wolf :flock]")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G7-17: JSON roundtrip

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'PARAGRAPH_FRAGMENTATION': 1}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PARAGRAPH_FRAGMENTATION] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-18: Shell command

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [LOW_GROUNDING] form=`(:cmd {:cmd "ls" :args ["-l"]})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:cmd {:cmd "ls" :args ["-l"]})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '3', ':beta'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(:cmd {:cmd "ls" :args ["-l"]})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:cmd {:cmd "ls" :args ["-l"]})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '7', ':open'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(:cmd {:cmd "ls" :args ["-l"]})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:cmd {:cmd "ls" :args ["-l"]})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '19', ':soft'), resolution doesn't close the loop)

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
- issues: {'ANSWER_LEAK_STRING': 1, 'HONEST_JUDGE_REPEAT': 1, 'LOW_GROUNDING': 2}
    - [ANSWER_LEAK_STRING] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — answer string ':number' appears in user_msg
    - [HONEST_JUDGE_REPEAT] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    - [LOW_GROUNDING] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-06: Protocol method dispatch

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 3, 'PARAGRAPH_FRAGMENTATION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Alarm (sound [this])) (extend-pro` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-alarm', ':long-alarm'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Alarm (sound [this])) (extend-pro` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-alarm', ':long-alarm'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Alarm (sound [this])) (extend-pro` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-alarm', ':long-alarm'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defprotocol Alarm (sound [this])) (extend-pro` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Alarm (sound [this])) (extend-pro` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':string-alarm', ':long-alarm'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defprotocol Alarm (sound [this])) (extend-pro` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

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

### G8-09: Multimethod defmethod

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(do (defmulti reply :role) (defmethod reply :sheph` — answer string ':measured' appears in user_msg

### G8-10: Multimethod vs protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(do (defmulti show identity) (defmethod show :wolf` — answer string 'howl' appears in user_msg

### G8-11: Protocol vs Java interface

- examples: 1
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(do (defprotocol IAlarm (raise [this])) (extend-pr` — answer string ':raised' appears in user_msg

### G8-13: this-style vs fn-style

- examples: 2
- variety @ n=50: 0.99
- issues: {'ANSWER_LEAK_STRING': 1, 'WRONG_FABLE_LITERAL': 1, 'LOW_GROUNDING': 2}
    - [ANSWER_LEAK_STRING] form=`(do (defprotocol Named (name-of [this])) (defrecor` — answer string 'Pip' appears in user_msg
    - [WRONG_FABLE_LITERAL] form=`(do (defprotocol Named (name-of [this])) (defrecor` — tortoise-hare ghost name 'Pip' appears in boy-wolf user_msg
    - [LOW_GROUNDING] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-14: Protocols don't inherit

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3, 'PARAGRAPH_FRAGMENTATION': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [LOW_GROUNDING] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)

### G8-15: derive and isa? — multimethod hierarchy

- examples: 3
- variety @ n=50: 0.99
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'EMPTY_GOAL_RENDERED': 3, 'LOW_GROUNDING': 6, 'BOOL_LEAK_RESOLUTION': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (derive ::shepherd ::villager) (isa? ::shepher` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':shepherd', ':villager', ':shepherd'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(do (derive ::shepherd ::villager) (isa? ::shepher` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (derive ::shepherd ::villager) (isa? ::shepher` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':shepherd', ':villager', ':shepherd'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(do (derive ::shepherd ::villager) (isa? ::shepher` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (derive ::shepherd ::villager) (isa? ::shepher` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':shepherd', ':villager', ':shepherd'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(do (derive ::shepherd ::villager) (isa? ::shepher` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G8-16: Abstract design with protocols

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'ANSWER_LEAK_STRING': 1, 'HONEST_JUDGE_REPEAT': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol Watch (look [this])) (defrecord S` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Sound (cry [this])) (defrecord Sh` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Sound (cry [this])) (defrecord Sh` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [ANSWER_LEAK_STRING] form=`(do (defprotocol Sound (cry [this])) (defrecord Sh` — answer string ':calm' appears in user_msg
    - [HONEST_JUDGE_REPEAT] form=`(do (defprotocol Sound (cry [this])) (defrecord Sh` — two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)

## Grade 9

### G9-01: Immutability as default — review

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :b 2) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', ':lime', ':kiwi'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :b 2) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '4', '19'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :b 2) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '14', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [v [1 2 3]] (conj v 4) v)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '6', '20'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [v [1 2 3]] (conj v 4) v)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '8', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [v [1 2 3]] (conj v 4) v)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '7', '3'), resolution doesn't close the loop)

### G9-02: Why state at all

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4}
    - [LOW_GROUNDING] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def progress (atom :idle)) (reset! progress :` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def progress (atom :idle)) (reset! progress :` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def progress (atom :idle)) (reset! progress :` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-03: Atom introduction

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom :start)) (reset! a :done) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-04: Atom CAS semantics

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-05: Watch on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':w',), resolution doesn't close the loop)
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
- issues: {'LOW_GROUNDING': 2, 'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg 218 words
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('100', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('100', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('100', '7'), resolution doesn't close the loop)

### G9-08: dosync and alter

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
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
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [HIGH_LENGTH] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg 212 words
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ag (agent 5)) (send ag + 10) (await ag) @` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '10'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ag (agent 5)) (send ag + 10) (await ag) @` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '10'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ag (agent 5)) (send ag + 10) (await ag) @` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '10'), resolution doesn't close the loop)

### G9-11: send and send-off

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send-off ag inc) (await ag` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send-off ag inc) (await ag` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-12: await — synchronizing on agents

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-13: future introduction

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`@(future (* 6 7))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`@(future (* 6 7))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`@(future (* 6 7))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '7'), resolution doesn't close the loop)

### G9-15: promise — deliver and deref

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [LOW_GROUNDING] form=`(do (def p (promise)) (deliver p :done) @p)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def p (promise)) (deliver p :done) @p)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':done',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def p (promise)) (deliver p :done) @p)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':done',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (def p (promise)) (deliver p :done) @p)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def p (promise)) (deliver p :done) @p)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':done',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def p (promise)) (deliver p 42) @p)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)

### G9-16: volatile — when STM is too heavy

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-17: binding — thread-local

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'PARAGRAPH_FRAGMENTATION': 3}
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PARAGRAPH_FRAGMENTATION] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PARAGRAPH_FRAGMENTATION] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PARAGRAPH_FRAGMENTATION] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

## Grade 10

### G10-01: quote, unquote, unquote-splice

- examples: 3
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 1}
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`'(1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '6', '20'), resolution doesn't close the loop)

### G10-02: syntax-quote

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [xs [1 2 3]] `(list ~@xs))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(let [xs [1 2 3]] `(list ~@xs))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [xs [1 2 3]] `(list ~@xs))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(let [xs [1 2 3]] `(list ~@xs))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [xs [1 2 3]] `(list ~@xs))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G10-03: defmacro introduction

- examples: 2
- variety @ n=50: 0.99
- issues: {'SENTENCE_START_LOWER_PRONOUN': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 3}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-04: Macro expansion rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 6, 'SENTENCE_START_LOWER_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(macroexpand-1 '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(when true 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(macroexpand-1 '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(when true 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(macroexpand-1 '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(when true 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)

### G10-05: macroexpand

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4}
    - [LOW_GROUNDING] form=`(macroexpand '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(macroexpand '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(macroexpand '(-> 1 inc inc))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(macroexpand '(-> 1 inc inc))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-06: when and when-not as macros

- examples: 3
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 2, 'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 9, 'REPEATED_OPENER_FRAGMENT': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(when true 1 2 3)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [LOW_GROUNDING] form=`(when true 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '9'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(when true 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '5'), resolution doesn't close the loop)

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1, 'STORY_RESOLUTION_NO_DRAWN': 4, 'CONCEPT_AS_VERB': 3, 'LOW_GROUNDING': 7, 'PARAGRAPH_FRAGMENTATION': 2}
    - [ANSWER_LEAK] form=`(-> 5 inc inc inc)` — answer 8 in narrative
    - [STORY_RESOLUTION_NO_DRAWN] form=`(-> 5 inc inc inc)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`(-> 5 inc inc inc)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(-> 5 inc inc inc)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '8', '8'), resolution doesn't close the loop)

### G10-08: Macro vs fn

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'SENTENCE_START_LOWER_PRONOUN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)

### G10-09: Hygiene and gensym

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(symbol? (gensym))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('x_', 'x_'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('x_', 'x_'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('x_', 'x_'), resolution doesn't close the loop)

### G10-10: Anaphoric macros are confusing

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'ANSWER_LEAK': 1, 'EXPECTED_META_PHRASE': 1, 'SENTENCE_START_LOWER_PRONOUN': 1}
    - [HIGH_LENGTH] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — user_msg 206 words
    - [ANSWER_LEAK] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — answer 10 in narrative
    - [EXPECTED_META_PHRASE] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — user_msg uses 'the expected X' meta-language — describes the answer in graders'-vocabulary instead of letting the runtime's return speak for itself
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation

### G10-11: Reader macros overview

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 7, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [LOW_GROUNDING] form=`'(1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '8', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '11', '3'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`'(1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(* % %) 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)

### G10-12: Tagged literals

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [LOW_GROUNDING] form=`(inst? #inst "2024-01-01")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inst? #inst "2024-01-01")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('2024', '-01', '-01'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inst? #inst "2024-01-01")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('2024', '-01', '-01'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(inst? #inst "2024-01-01")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inst? #inst "2024-01-01")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('2024', '-01', '-01'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(uuid? #uuid "00000000-0000-0000-0000-000000000000` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('00000000', '-0000', '-0000'), resolution doesn't close the loop)

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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'SENTENCE_START_LOWER_PRONOUN': 2, 'LOW_GROUNDING': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval '(+ 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval '(+ 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [SENTENCE_START_LOWER_PRONOUN] form=`(eval '(+ 1 2 3))` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval '(+ 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [SENTENCE_START_LOWER_PRONOUN] form=`(eval (list '+ 4 5))` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [LOW_GROUNDING] form=`(eval (list '+ 4 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-15: When not to write a macro

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 4, 'SENTENCE_START_LOWER_PRONOUN': 2, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "a function suffices when no syntax shaping is` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', 'raven'), resolution doesn't close the loop)
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do "a function suffices when no syntax shaping is` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "a function suffices when no syntax shaping is` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', 'ochre'), resolution doesn't close the loop)
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do "a function suffices when no syntax shaping is` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "a function suffices when no syntax shaping is` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', 'saffron'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "prefer fn unless you must shape syntax" (map ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '19', 'myrrh'), resolution doesn't close the loop)

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
- issues: {'PATIENT_ROLE_BOASTFUL': 1, 'LOW_GROUNDING': 1}
    - [PATIENT_ROLE_BOASTFUL] form=`(do "Clojure runs on multiple hosts: JVM, CLR, JS,` — patient role 'the elder' co-occurs with boastful EMO phrase 'boasting at every'
    - [LOW_GROUNDING] form=`(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScr` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-02: Method call syntax

- examples: 8
- variety @ n=50: 1.00
- issues: {'EMPTY_GOAL_RENDERED': 8, 'LOW_GROUNDING': 4, 'HIGH_LENGTH': 2, 'ANSWER_LEAK_STRING': 2, 'STORY_RESOLUTION_NO_DRAWN': 12}
    - [EMPTY_GOAL_RENDERED] form=`(.startsWith "shepherd-elder" "shepherd")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [LOW_GROUNDING] form=`(.startsWith "shepherd-elder" "shepherd")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(.startsWith "shepherd-elder" "shepherd")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [HIGH_LENGTH] form=`(. "abc" toUpperCase)` — user_msg 201 words
    - [ANSWER_LEAK_STRING] form=`(. "abc" toUpperCase)` — answer string 'ABC' appears in user_msg
    - [STORY_RESOLUTION_NO_DRAWN] form=`(.toUpperCase "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)

### G11-03: Static method call

- examples: 6
- variety @ n=50: 1.00
- issues: {'PROCEDURAL_OPENER': 2, 'STORY_RESOLUTION_NO_DRAWN': 9, 'EMPTY_GOAL_RENDERED': 5}
    - [PROCEDURAL_OPENER] form=`(Math/abs -7)` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)
    - [PROCEDURAL_OPENER] form=`(Math/abs -7)` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/min 5 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)

### G11-04: Field access

- examples: 6
- variety @ n=50: 1.00
- issues: {'EMPTY_GOAL_RENDERED': 15, 'STORY_RESOLUTION_NO_DRAWN': 12, 'PARAGRAPH_FRAGMENTATION': 1}
    - [EMPTY_GOAL_RENDERED] form=`(count "shepherd")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(count "shepherd")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(count "shepherd")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(count "flock")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(count "flock")` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "shepherd")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('amber',), resolution doesn't close the loop)

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
- issues: {'LOW_GROUNDING': 4, 'EMPTY_GOAL_RENDERED': 5, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(let [a (int-array [5 10 15])] (aget a 0))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [a (int-array [5 10 15])] (aget a 0))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [EMPTY_GOAL_RENDERED] form=`(let [a (int-array [5 10 15])] (aget a 0))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [EMPTY_GOAL_RENDERED] form=`(let [a (int-array [5 10 15])] (aget a 0))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (int-array [7 8 9])] (alength a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '8', '9'), resolution doesn't close the loop)
    - [EMPTY_GOAL_RENDERED] form=`(let [a (int-array [7 8 9])] (alength a))` — user_msg has 'To , <pronoun> composed' — the {goal_text} placeholder rendered empty (audited by boy-wolf XOE6)

### G11-08: Type hints

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 12}
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
- issues: {'LOW_GROUNDING': 3, 'PATIENT_ROLE_BOASTFUL': 1, 'VILLAGE_NOUN_OVERUSE': 1}
    - [LOW_GROUNDING] form=`(do "ClojureScript compiles to JavaScript via the ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "cljs runs in browsers and Node, with JS inter` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PATIENT_ROLE_BOASTFUL] form=`(do "cljs runs in browsers and Node, with JS inter` — patient role 'the elder' co-occurs with boastful EMO phrase 'with a smug grin'
    - [VILLAGE_NOUN_OVERUSE] form=`(do "cljs runs in browsers and Node, with JS inter` — `the village` appears 4 times (noun-saturation tic — vary or drop)
    - [LOW_GROUNDING] form=`(do "cljs runs in browsers and Node, with JS inter` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-11: cljs / JavaScript interop

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(do "(js/console.log x) calls a JS global; (.-foo ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "js/<name> namespaces JS globals; .- prefix ma` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-12: Basilisp overview (Python host)

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPEATED_OPENER_FRAGMENT': 1, 'PATIENT_ROLE_BOASTFUL': 1, 'VILLAGE_NOUN_OVERUSE': 1, 'LOW_GROUNDING': 2}
    - [REPEATED_OPENER_FRAGMENT] form=`(do "basilisp is a Clojure-like Lisp implemented o` — opener fragment 'at the edge of the meadow,' also appears later in user_msg
    - [PATIENT_ROLE_BOASTFUL] form=`(do "basilisp is a Clojure-like Lisp implemented o` — patient role 'the elder' co-occurs with boastful EMO phrase 'with a smug grin'
    - [VILLAGE_NOUN_OVERUSE] form=`(do "basilisp is a Clojure-like Lisp implemented o` — `the village` appears 4 times (noun-saturation tic — vary or drop)
    - [LOW_GROUNDING] form=`(do "basilisp interops with Python via the same do` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "basilisp interops with Python via the same do` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-13: Cross-platform .cljc and reader-conditionals

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do ".cljc files share code across multiple hosts"` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-14: Debugging host leaks

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'PROCEDURAL_OPENER': 1, 'STORY_RESOLUTION_NO_DRAWN': 9, 'EMPTY_GOAL_RENDERED': 6}
    - [LOW_GROUNDING] form=`(do "host stack traces leak through interop; learn` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PROCEDURAL_OPENER] form=`(do "host stack traces leak through interop; learn` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (Math/sqrt 4) (catch Exception _ :err))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', ':err'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (Math/sqrt 4) (catch Exception _ :err))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', ':err'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (Math/sqrt 4) (catch Exception _ :err))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', ':err'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (Math/abs -42) (catch Exception _ :err))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-42', ':err'), resolution doesn't close the loop)

## Grade 12

### G12-01: Transducers introduction

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'PARAGRAPH_FRAGMENTATION': 2}
    - [HIGH_LENGTH] form=`(into [] (map inc) [1 2 3])` — user_msg 218 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (filter even?) [1 2 3 4 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', '5'), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(into [] (filter even?) [1 2 3 4 5])` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (filter even?) [1 2 3 4 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (filter even?) [1 2 3 4 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', '5'), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(into [] (filter even?) [1 2 3 4 5])` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G12-03: into with a transducer (xform)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'COLLECTION_LEAK': 1}
    - [HIGH_LENGTH] form=`(into #{} (map inc) [1 2 3])` — user_msg 213 words
    - [COLLECTION_LEAK] form=`(into #{} (map inc) [1 2 3])` — elements of expected {2, 3, 4} appear comma-separated in user_msg (collection answer leak)

### G12-04: core.async introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'VILLAGE_NOUN_OVERUSE': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "(chan), (go ...), (<! ...), (>! ...) form the` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':slow', 'amber'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "(chan), (go ...), (<! ...), (>! ...) form the` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':open', 'apple'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "(chan), (go ...), (<! ...), (>! ...) form the` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':high', 'thistle'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "go-blocks let you write async code as if it w` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':right', 'willow'), resolution doesn't close the loop)
    - [VILLAGE_NOUN_OVERUSE] form=`(do "go-blocks let you write async code as if it w` — `the village` appears 4 times (noun-saturation tic — vary or drop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "go-blocks let you write async code as if it w` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':delta', 'lichen'), resolution doesn't close the loop)

### G12-05: Channels and pipelines

- examples: 2
- variety @ n=50: 1.00
- issues: {'PATIENT_ROLE_BOASTFUL': 1, 'STORY_RESOLUTION_NO_DRAWN': 6, 'VILLAGE_NOUN_OVERUSE': 1, 'LOW_GROUNDING': 1}
    - [PATIENT_ROLE_BOASTFUL] form=`(do "pipe, mult, mix, pipeline-async route values ` — patient role 'the elder' co-occurs with boastful EMO phrase 'with a smug grin'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "pipe, mult, mix, pipeline-async route values ` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':west', 'ember'), resolution doesn't close the loop)
    - [VILLAGE_NOUN_OVERUSE] form=`(do "pipe, mult, mix, pipeline-async route values ` — `the village` appears 4 times (noun-saturation tic — vary or drop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "pipe, mult, mix, pipeline-async route values ` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':north', 'stone'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "pipe, mult, mix, pipeline-async route values ` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':c', 'candle'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "pipelines transform streams of values channel` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':z', 'ochre'), resolution doesn't close the loop)

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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'PATIENT_ROLE_BOASTFUL': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "s/exercise produces sample inputs for a spec"` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':warm', 'pewter'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "s/exercise produces sample inputs for a spec"` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':near', 'indigo'), resolution doesn't close the loop)
    - [PATIENT_ROLE_BOASTFUL] form=`(do "s/exercise produces sample inputs for a spec"` — patient role 'the elder' co-occurs with boastful EMO phrase 'puffed up with pride'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "s/exercise produces sample inputs for a spec"` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':soft', 'stone'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "spec generators turn specs into property-base` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':c', 'indigo'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "spec generators turn specs into property-base` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':west', 'ochre'), resolution doesn't close the loop)

### G12-08: clojure.test

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'BOOL_LEAK_RESOLUTION': 1, 'PARAGRAPH_FRAGMENTATION': 1, 'PATIENT_ROLE_BOASTFUL': 1, 'VILLAGE_NOUN_OVERUSE': 1, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= (+ 1 2) 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '5'), resolution doesn't close the loop)
    - [BOOL_LEAK_RESOLUTION] form=`(= (+ 1 2) 3)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= (+ 1 2) 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '8'), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(= (+ 1 2) 3)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= (+ 1 2) 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "(deftest …), (is …), (testing …) are the core` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':soft', 'garnet'), resolution doesn't close the loop)

### G12-09: Test fixtures

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "(use-fixtures :each f) wraps every deftest in` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':fast', 'marble'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "(use-fixtures :each f) wraps every deftest in` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':low', 'cedar'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "(use-fixtures :each f) wraps every deftest in` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':left', 'garnet'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "fixtures provide setup/teardown around deftes` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':far', 'pebble'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do "fixtures provide setup/teardown around deftes` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "fixtures provide setup/teardown around deftes` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':beta', 'thread'), resolution doesn't close the loop)

### G12-10: Property-based testing

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_LEAK': 1, 'BOOL_LEAK_RESOLUTION': 1, 'STORY_RESOLUTION_NO_DRAWN': 6, 'PATIENT_ROLE_BOASTFUL': 1, 'VILLAGE_NOUN_OVERUSE': 1, 'LOW_GROUNDING': 1}
    - [FORM_LEAK] form=`(= (reverse (reverse [1 2 3])) [1 2 3])` — form '(= (reverse (reverse [1 2 3])) [1 2 3])' appears in user_msg of a goal-style subject
    - [BOOL_LEAK_RESOLUTION] form=`(= (reverse (reverse [1 2 3])) [1 2 3])` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= (reverse (reverse [1 2 3])) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '7', '14'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= (reverse (reverse [1 2 3])) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '5', '12'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= (reverse (reverse [1 2 3])) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '3', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "test.check generates inputs and checks proper` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':south', 'feather'), resolution doesn't close the loop)

### G12-11: Leiningen project.clj

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [LOW_GROUNDING] form=`(do "project.clj declares :dependencies, :main, :p` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "project.clj declares :dependencies, :main, :p` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':near', 'saffron'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "project.clj declares :dependencies, :main, :p` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':alpha', 'raven'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "project.clj declares :dependencies, :main, :p` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':south', 'indigo'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do "Leiningen reads project.clj at the project ro` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "Leiningen reads project.clj at the project ro` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':low', 'coral'), resolution doesn't close the loop)

### G12-12: deps.edn projects

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'REPEATED_OPENER_FRAGMENT': 1, 'PATIENT_ROLE_BOASTFUL': 1, 'VILLAGE_NOUN_OVERUSE': 1, 'LOW_GROUNDING': 2, 'PARAGRAPH_FRAGMENTATION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "deps.edn declares :deps and :aliases for the ` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':north', 'amber'), resolution doesn't close the loop)
    - [REPEATED_OPENER_FRAGMENT] form=`(do "deps.edn declares :deps and :aliases for the ` — opener fragment 'at the edge of the meadow,' also appears later in user_msg
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "deps.edn declares :deps and :aliases for the ` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hard', 'harbor'), resolution doesn't close the loop)
    - [PATIENT_ROLE_BOASTFUL] form=`(do "deps.edn declares :deps and :aliases for the ` — patient role 'the elder' co-occurs with boastful EMO phrase 'with a smug grin'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "deps.edn declares :deps and :aliases for the ` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':east', 'linen'), resolution doesn't close the loop)
    - [VILLAGE_NOUN_OVERUSE] form=`(do "deps.edn declares :deps and :aliases for the ` — `the village` appears 4 times (noun-saturation tic — vary or drop)

### G12-13: Aliases and tools

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "`clj -M:test` runs the :test alias from deps.` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':warm', 'raven'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "`clj -M:test` runs the :test alias from deps.` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':far', 'topaz'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "`clj -M:test` runs the :test alias from deps.` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':soft', 'indigo'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "aliases compose extra paths, deps, and main o` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hard', 'cobalt'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do "aliases compose extra paths, deps, and main o` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "aliases compose extra paths, deps, and main o` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':z', 'raven'), resolution doesn't close the loop)

### G12-14: Pedestal / Ring (web stack brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 6, 'PARAGRAPH_FRAGMENTATION': 1, 'PATIENT_ROLE_BOASTFUL': 1, 'VILLAGE_NOUN_OVERUSE': 1}
    - [LOW_GROUNDING] form=`(do "Ring models HTTP as request-map -> response-m` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "Ring models HTTP as request-map -> response-m` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':fast', 'bridge'), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(do "Ring models HTTP as request-map -> response-m` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "Ring models HTTP as request-map -> response-m` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':warm', 'myrrh'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "Ring models HTTP as request-map -> response-m` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':b', 'saffron'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "Pedestal layers interceptors over Ring for ri` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hard', 'apple'), resolution doesn't close the loop)

### G12-15: Datomic / XTDB (datalog db brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'STORY_RESOLUTION_NO_DRAWN': 6, 'VILLAGE_NOUN_OVERUSE': 1, 'PATIENT_ROLE_BOASTFUL': 1}
    - [LOW_GROUNDING] form=`(do "Datomic and XTDB are immutable, time-aware da` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "Datomic and XTDB are immutable, time-aware da` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':second', 'raven'), resolution doesn't close the loop)
    - [VILLAGE_NOUN_OVERUSE] form=`(do "Datomic and XTDB are immutable, time-aware da` — `the village` appears 4 times (noun-saturation tic — vary or drop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "Datomic and XTDB are immutable, time-aware da` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':high', 'ochre'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "Datomic and XTDB are immutable, time-aware da` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':alpha', 'saffron'), resolution doesn't close the loop)
    - [PATIENT_ROLE_BOASTFUL] form=`(do "queries are written in datalog over EDN-shape` — patient role 'the elder' co-occurs with boastful EMO phrase 'with great whoops of laughter'

### G12-16: Reagent (cljs UI brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "Reagent wraps React with Hiccup-shaped Clojur` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':second', 'thread'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "Reagent wraps React with Hiccup-shaped Clojur` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':delta', 'willow'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "Reagent wraps React with Hiccup-shaped Clojur` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':west', 'willow'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "components are functions returning Hiccup vec` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':gamma', 'linen'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "components are functions returning Hiccup vec` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':second', 'saffron'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do "components are functions returning Hiccup vec` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-17: Library design patterns

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'PATIENT_ROLE_BOASTFUL': 5, 'VILLAGE_NOUN_OVERUSE': 5}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "good libraries expose data, then functions, t` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':z', 'willow'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "good libraries expose data, then functions, t` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':north', 'marble'), resolution doesn't close the loop)
    - [PATIENT_ROLE_BOASTFUL] form=`(do "good libraries expose data, then functions, t` — patient role 'the elder' co-occurs with boastful EMO phrase 'boasting at every'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "good libraries expose data, then functions, t` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', 'lichen'), resolution doesn't close the loop)
    - [VILLAGE_NOUN_OVERUSE] form=`(do "good libraries expose data, then functions, t` — `the village` appears 4 times (noun-saturation tic — vary or drop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "small public API surface, plain data inputs, ` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':gamma', 'myrrh'), resolution doesn't close the loop)

### G12-18: Clojure style guide

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "kebab-case names, two-space indent, threading` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':z', 'willow'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "kebab-case names, two-space indent, threading` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':third', 'marble'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do "kebab-case names, two-space indent, threading` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "kebab-case names, two-space indent, threading` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':south', 'auburn'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "prefer pure functions, name predicates with ?` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':alpha', 'coral'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "prefer pure functions, name predicates with ?` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':west', 'marble'), resolution doesn't close the loop)

---

## Summary

### Issue counts (across all examples × 3 records)

- **STORY_RESOLUTION_NO_DRAWN**: 922
- **LOW_GROUNDING**: 439
- **EMPTY_GOAL_RENDERED**: 230
- **PARAGRAPH_FRAGMENTATION**: 82
- **REPL_AS_TIME_TRAVELLER**: 38
- **BOOL_LEAK_RESOLUTION**: 34
- **SENTENCE_START_LOWER_PRONOUN**: 27
- **ANSWER_LEAK_STRING**: 22
- **VILLAGE_NOUN_OVERUSE**: 21
- **PATIENT_ROLE_BOASTFUL**: 20
- **HONEST_JUDGE_REPEAT**: 18
- **HIGH_LENGTH**: 16
- **FOREIGN_FABLE_IMAGERY**: 14
- **ANSWER_LEAK**: 13
- **CONCEPT_AS_VERB**: 12
- **THE_FORM_OVERUSE**: 9
- **STRING_AS_CHAR_MISCLAIM**: 7
- **SMALL_INT_LEAK**: 7
- **REPEATED_OPENER_FRAGMENT**: 4
- **PROCEDURAL_OPENER**: 4
- **WRONG_FABLE_LITERAL**: 1
- **EXPECTED_META_PHRASE**: 1
- **COLLECTION_LEAK**: 1
- **FORM_LEAK**: 1

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 80 | 231 | — |
| 2 | 22 | 88 | 385 | — |
| 3 | 18 | 31 | 118 | — |
| 4 | 20 | 39 | 162 | — |
| 5 | 22 | 39 | 147 | — |
| 6 | 16 | 33 | 160 | — |
| 7 | 18 | 36 | 135 | — |
| 8 | 16 | 31 | 90 | — |
| 9 | 18 | 34 | 73 | — |
| 10 | 16 | 36 | 128 | — |
| 11 | 14 | 58 | 163 | — |
| 12 | 18 | 37 | 151 | — |

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

#### STORY_RESOLUTION_NO_DRAWN

- `G1-09` (form `(symbol? 42)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('51',), resolution doesn't close the loop)
    ```
    An empty hour can sometimes be filled with mischief, and mischief once started has a way of escalating.

Clementine pointed at a name chalked onto the slate in the woods,
then at an actual sheep standing in the fold. "The mark on the
slate is the *name*; the sheep is the *value*. They are not
the sa...
    ```
- `G1-09` (form `(symbol? 42)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('41',), resolution doesn't close the loop)
    ```
    A boy with too little to do and too loud a voice is a small danger to himself and a larger one to his village.

Lena, puffed up with pride, mistook the chalk mark on the slate
for the sheep it pointed to. "It says sheep, so the value must be
a sheep!" Nikodemus only shook his head: the
mark and the ...
    ```
- `G1-09` (form `(symbol? 42)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('67',), resolution doesn't close the loop)
    ```
    Irmgard was supposed to keep the sheep safe; instead, near the farm, he kept inventing reasons for the village to run.

"There's a difference between *labeling* the form and
*evaluating* it," Theophilus said. "Quote in any of its
shapes is the labeling — the runtime hands you back the form,
not its ...
    ```
- `G1-10` (form `(+ 1 2) ; sum of one and two`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    ```
    The hilltop offered a fine view of both the flock and the road below, where help would have to come from.

Carol had chalked an addition on the slate with a dashed line and notes in smaller chalk to the right — annotation only, for the next shepherd's eye.

Tom worried the runtime might mix annotati...
    ```
- `G1-10` (form `(+ 1 2) ; sum of one and two`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '4'), resolution doesn't close the loop)
    ```
    It is a serious thing to call for help, and a more serious thing to call for it falsely.

Evangelos, puffed up with pride, glanced at the form and called out
what he thought it would do without paying attention to
the conventions of how it was written. Theodelinda only
shook her head — the runtime r...
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
- `G4-18` (form `(= [1 2 3] '(1 2 3))`): user_msg 204 words
    ```
    The lambs were milling in the lower meadow when the boy first thought of the joke he should not have made.

Carol held two containers of fleeces: one a wool-basket `[1 2 3]` and another a cord `'(1 2 3)` with three markers strung on it. The containers looked different, but both held the same three i...
    ```
- `G5-03` (form `(when true :yes)`): user_msg 206 words
    ```
    The lambs were milling in the lower meadow when the boy first thought of the joke he should not have made.

Carol posted a watch-order at the fold: if the lambs were restless today, Tom was to ring the bell and post a notice at the village stone. Tom checked the pen, and warm — the lambs were pacing...
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

