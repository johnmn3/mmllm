# dog-shadow curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

### G1-01: Eval as substitution

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`nil` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`nil` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-02: Integer numbers

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`7` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`-25` — character 'Sniff the dog' introduced twice within 200 chars — drop the second 'the dog'

### G1-03: Ratios

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'DOUBLE_NAME_INTRO': 3}
    - [LOW_GROUNDING] form=`1/2` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(+ 1/2 1/4)` — character 'Pumpernickel the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [DOUBLE_NAME_INTRO] form=`(- 1 1/3)` — character 'Snowball the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [DOUBLE_NAME_INTRO] form=`(- 1 1/3)` — character 'Whatsit the dog' introduced twice within 200 chars — drop the second 'the dog'

### G1-04: Strings

- examples: 5
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 2}
    - [DOUBLE_NAME_INTRO] form=`"race"` — character 'Gizmo the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [DOUBLE_NAME_INTRO] form=`"slow and steady"` — character 'Watcher the dog' introduced twice within 200 chars — drop the second 'the dog'

### G1-05: Booleans

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'DOUBLE_NAME_INTRO': 2}
    - [LOW_GROUNDING] form=`true` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`false` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(= 1 1)` — character 'Fudge the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [DOUBLE_NAME_INTRO] form=`(= 1 2)` — character 'Leo the dog' introduced twice within 200 chars — drop the second 'the dog'

### G1-06: nil

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`nil` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(nil? false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(nil? false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(= nil nil)` — character 'Doodle the dog' introduced twice within 200 chars — drop the second 'the dog'

### G1-08: Characters

- examples: 4
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 3}
    - [DOUBLE_NAME_INTRO] form=`\h` — character 'Watchdog the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [DOUBLE_NAME_INTRO] form=`\T` — character 'Winston the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [DOUBLE_NAME_INTRO] form=`(char? \h)` — character 'Cashew the dog' introduced twice within 200 chars — drop the second 'the dog'

### G1-09: Symbols vs values

- examples: 4
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 8, 'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 2, 'BOOL_LEAK_RESOLUTION': 3, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(symbol? 'hare)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(symbol? 'hare)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(symbol? 42)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('51',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(symbol? 42)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(symbol? 42)` — user_msg 212 words
    - [BOOL_LEAK_RESOLUTION] form=`(symbol? 42)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead

### G1-10: Comments

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5, 'LOW_GROUNDING': 1, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2) ;; sum of one and two` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(+ 1 2) ;; sum of one and two` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(+ 1 2) ;; sum of one and two` — character 'Louie the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2) ;; sum of one and two` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`42 ;; the answer` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('39',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`42 ;; the answer` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('93',), resolution doesn't close the loop)

### G1-11: Whitespace doesn't matter

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1, 'HIGH_LENGTH': 1, 'THE_FORM_OVERUSE': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+    1    2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+    1    2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+    1    2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(+    1    2)` — character 'Riley the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+
  1
  2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+
  1
  2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)

### G1-12: Parens group; they don't multiply

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5, 'DOUBLE_NAME_INTRO': 2, 'ANSWER_LEAK': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '7'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(+ 2 3)` — character 'Topsy the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [ANSWER_LEAK] form=`(* (+ 1 2) 3)` — answer 9 in narrative
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* (+ 1 2) 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '9', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* (+ 1 2) 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)

### G1-13: First arithmetic call

- examples: 6
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 18, 'REPL_AS_TIME_TRAVELLER': 3, 'DOUBLE_NAME_INTRO': 1, 'SENTENCE_START_LOWER_PRONOUN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '8'), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(+ 1 2)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(- 5 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(- 5 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '6'), resolution doesn't close the loop)

### G1-14: Nested call evaluation

- examples: 4
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'STORY_RESOLUTION_NO_DRAWN': 12, 'ANSWER_LEAK': 1, 'DOUBLE_NAME_INTRO': 2, 'REPL_AS_TIME_TRAVELLER': 2}
    - [HIGH_LENGTH] form=`(+ 1 (* 2 3))` — user_msg 217 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (* 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (* 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '8'), resolution doesn't close the loop)
    - [ANSWER_LEAK] form=`(+ 1 (* 2 3))` — answer 7 in narrative
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (* 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '7'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(* (+ 1 2) (+ 3 4))` — user_msg 209 words

### G1-15: Equality

- examples: 6
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'LOW_GROUNDING': 4, 'DOUBLE_NAME_INTRO': 9, 'STORY_RESOLUTION_NO_DRAWN': 13}
    - [WRONG_FABLE_LITERAL] form=`(= 1 1)` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [LOW_GROUNDING] form=`(= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(= 1 1)` — character 'Pip the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(= 1 1)` — character 'Pearl the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)

### G1-16: Numeric predicates

- examples: 6
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 16, 'DOUBLE_NAME_INTRO': 4, 'REPL_AS_TIME_TRAVELLER': 2, 'BOOL_LEAK_RESOLUTION': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(zero? 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(zero? 0)` — character 'Pumpkin the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [REPL_AS_TIME_TRAVELLER] form=`(zero? 0)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(zero? 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(zero? 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(zero? 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G1-17: Printing vs returning

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`42` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('52',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`42` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('82',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`42` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('78',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(+ 1 2)` — character 'Mocha the dog' introduced twice within 200 chars — drop the second 'the dog'

### G1-18: Errors are safe in the REPL

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 4, 'LOW_GROUNDING': 1, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 7 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '6'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(* 7 6)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(* 7 6)` — character 'Pickle the dog' introduced twice within 200 chars — drop the second 'the dog'

## Grade 2

### G2-01: Multi-arg arithmetic

- examples: 6
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 17, 'DOUBLE_NAME_INTRO': 5, 'REPL_AS_TIME_TRAVELLER': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '3', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '5'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(+ 1 2 3 4)` — character 'Pearl the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 2 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 2 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '7'), resolution doesn't close the loop)

### G2-02: Comparison chains

- examples: 5
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'HIGH_LENGTH': 4, 'BOOL_LEAK_RESOLUTION': 1, 'REPL_AS_TIME_TRAVELLER': 1, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(< 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '4'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(< 1 2 3)` — user_msg 203 words
    - [BOOL_LEAK_RESOLUTION] form=`(< 1 2 3)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [STORY_RESOLUTION_NO_DRAWN] form=`(< 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '6', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(< 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '8'), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(< 3 2 1)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

### G2-03: not= and = with multiple args

- examples: 5
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 13, 'LOW_GROUNDING': 3, 'REPL_AS_TIME_TRAVELLER': 4, 'BOOL_LEAK_RESOLUTION': 2, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not= 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '8'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(not= 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [REPL_AS_TIME_TRAVELLER] form=`(not= 1 2)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not= 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '3'), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(not= 1 1)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not= 1 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '9'), resolution doesn't close the loop)

### G2-04: min and max

- examples: 5
- variety @ n=50: 1.00
- issues: {'REPL_AS_TIME_TRAVELLER': 1, 'STORY_RESOLUTION_NO_DRAWN': 14, 'DOUBLE_NAME_INTRO': 3}
    - [REPL_AS_TIME_TRAVELLER] form=`(min 1 2 3)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(min 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '3', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(min 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(min 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '8', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(max 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '8', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(max 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '7'), resolution doesn't close the loop)

### G2-05: quot, rem, mod

- examples: 6
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 18, 'DOUBLE_NAME_INTRO': 3, 'REPL_AS_TIME_TRAVELLER': 3, 'SMALL_INT_LEAK': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(quot 17 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '17'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(quot 17 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '-15'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(quot 17 5)` — character 'Howler the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(quot 17 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '5'), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(rem 17 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(rem 17 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '-17'), resolution doesn't close the loop)

### G2-06: inc and dec

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 11, 'DOUBLE_NAME_INTRO': 5, 'REPL_AS_TIME_TRAVELLER': 2}
    - [LOW_GROUNDING] form=`(inc 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inc 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inc 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(dec 5)` — character 'Acorn the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(dec 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(dec 5)` — character 'Buster the dog' introduced twice within 200 chars — drop the second 'the dog'

### G2-07: Absolute value

- examples: 4
- variety @ n=50: 1.00
- issues: {'REPL_AS_TIME_TRAVELLER': 3, 'STORY_RESOLUTION_NO_DRAWN': 8, 'LOW_GROUNDING': 3}
    - [REPL_AS_TIME_TRAVELLER] form=`(abs 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [REPL_AS_TIME_TRAVELLER] form=`(abs 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(abs 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(abs 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(abs -5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-22',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(abs -5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-08: Arithmetic on ratios

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 9, 'REPL_AS_TIME_TRAVELLER': 1, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(+ 1/2 1/4)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1/2 1/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1/2 1/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1/2 1/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(* 2/3 3/4)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 2/3 3/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3', '4'), resolution doesn't close the loop)

### G2-09: Floats vs ints (the / operator)

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'REPL_AS_TIME_TRAVELLER': 2, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(/ 10 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '-16'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(/ 10 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-18',), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(/ 10 2)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(/ 10 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '10'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(/ 10 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '13'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(/ 10 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('19', '15'), resolution doesn't close the loop)

### G2-10: Powers via repeated multiplication

- examples: 4
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 3, 'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 1}
    - [DOUBLE_NAME_INTRO] form=`(* 2 2 2)` — character 'Louie the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 2 2 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '4', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 5 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 5 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 5 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(* 3 3 3 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-11: String concatenation with str

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(str "ab" "cd")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('saffron', 'indigo'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(str "ab" "cd")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('harbor', 'myrrh'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(str "ab" "cd")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('feather', 'ochre'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(str "ab" "cd")` — character 'Riley the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [DOUBLE_NAME_INTRO] form=`(str "p" "q" "r")` — character 'Cocoa the dog' introduced twice within 200 chars — drop the second 'the dog'

### G2-12: print and println — return values

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(println "hello")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('amber',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(println "hello")` — character 'Topsy the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(println "hello")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('feather',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(println "hello")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('saffron',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(println "hello")` — character 'Bounder the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(print "x")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('garnet',), resolution doesn't close the loop)

### G2-13: and / or — short circuit, return values

- examples: 6
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 3, 'DOUBLE_NAME_INTRO': 5, 'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 5}
    - [BOOL_LEAK_RESOLUTION] form=`(and true true)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [DOUBLE_NAME_INTRO] form=`(and true true)` — character 'Sooty the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(and true false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [BOOL_LEAK_RESOLUTION] form=`(and true false)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [BOOL_LEAK_RESOLUTION] form=`(or false true)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(or false true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-14: not — turning truthy to false

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'DOUBLE_NAME_INTRO': 7, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(not true)` — character 'Ace the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [DOUBLE_NAME_INTRO] form=`(not false)` — character 'Shadow the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(not 0)` — character 'Max the dog' introduced twice within 200 chars — drop the second 'the dog'

### G2-15: Falsey values: only false and nil

- examples: 4
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'STORY_RESOLUTION_NO_DRAWN': 12, 'DOUBLE_NAME_INTRO': 1, 'HIGH_LENGTH': 1}
    - [WRONG_FABLE_LITERAL] form=`(if 0 1 0)` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if 0 1 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(if 0 1 0)` — character 'Pip the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [HIGH_LENGTH] form=`(if 0 1 0)` — user_msg 211 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if 0 1 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '8', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if 0 1 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)

### G2-16: Truthy 0 and empty string

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5, 'DOUBLE_NAME_INTRO': 2, 'LOW_GROUNDING': 4}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(boolean 0)` — character 'Pumpkin the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(boolean "")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean "")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('coral',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean "")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('coral',), resolution doesn't close the loop)

### G2-17: Keyword as function for map lookup

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:hare {:hare 1 :tortoise 2})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '7', ':doe'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(:hare {:hare 1 :tortoise 2})` — character 'Pathfinder the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:hare {:hare 1 :tortoise 2})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '11', ':wren'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:hare {:hare 1 :tortoise 2})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '5', '14'), resolution doesn't close the loop)

### G2-18: Quoting symbols

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 8, 'BOOL_LEAK_RESOLUTION': 2, 'HIGH_LENGTH': 1, 'DOUBLE_NAME_INTRO': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [BOOL_LEAK_RESOLUTION] form=`(symbol? (quote hare))` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(symbol? (quote hare))` — user_msg 201 words
    - [BOOL_LEAK_RESOLUTION] form=`(symbol? (quote hare))` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-19: Auto-promotion to bigint

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'REPL_AS_TIME_TRAVELLER': 2, 'DOUBLE_NAME_INTRO': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 1000000 1000000)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('1048576', '1048576'), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(* 1000000 1000000)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 1000000 1000000)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('100000000000', '100000000000'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(* 1000000 1000000)` — character 'Inky the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [REPL_AS_TIME_TRAVELLER] form=`(* 1000000 1000000)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 1000000 1000000)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9007199254740992', '9007199254740992'), resolution doesn't close the loop)

### G2-20: Counting

- examples: 3
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1, 'PROCEDURAL_OPENER': 2}
    - [LOW_GROUNDING] form=`(count [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '7'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '7', '11'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(count [1 2 3])` — user_msg 201 words
    - [LOW_GROUNDING] form=`(count [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-21: String length and substring

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('alder',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(count "tortoise")` — character 'Biscuit the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('river',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('willow',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('pebble',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('willow',), resolution doesn't close the loop)

### G2-22: Compose pure arithmetic (multi-step calculation)

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1, 'HIGH_LENGTH': 2, 'ANSWER_LEAK': 2, 'REPL_AS_TIME_TRAVELLER': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(- (* 5 4) 7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '6', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(- (* 5 4) 7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(- (* 5 4) 7)` — character 'Nosey the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(- (* 5 4) 7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '9', '6'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(+ (* 3 8) (* 2 4))` — user_msg 211 words
    - [ANSWER_LEAK] form=`(+ (* 3 8) (* 2 4))` — answer 32 in narrative

## Grade 3

### G3-01: def — top-level binding

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 42) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('28',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 42) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('36',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 42) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('52',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def y 7) y)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def y 7) y)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def y 7) y)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)

### G3-02: def — redefinition

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 1) (def x 99) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('78',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 1) (def x 99) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '47'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (def x 1) (def x 99) x)` — character 'Houndsman the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 1) (def x 99) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('73',), resolution doesn't close the loop)

### G3-03: let — local binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 3, 'STORY_RESOLUTION_NO_DRAWN': 8, 'THE_FORM_OVERUSE': 2, 'DOUBLE_NAME_INTRO': 1}
    - [HIGH_LENGTH] form=`(let [x 3] (+ x 1))` — user_msg 263 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 3] (+ x 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '8'), resolution doesn't close the loop)
    - [THE_FORM_OVERUSE] form=`(let [x 3] (+ x 1))` — `the form` appears 6 times in user_msg (template tic — vary references)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 3] (+ x 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [n 10] (* n n))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(let [n 10] (* n n))` — character 'Rex the dog' introduced twice within 200 chars — drop the second 'the dog'

### G3-04: let — multi-binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'HIGH_LENGTH': 3, 'ANSWER_LEAK': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 1 b 2] (+ a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 1 b 2] (+ a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 1 b 2] (+ a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '8'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(let [x 5 y 3] (- x y))` — user_msg 223 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 5 y 3] (- x y))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '7'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(let [x 5 y 3] (- x y))` — user_msg 233 words

### G3-05: let — shadowing outer def

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 1, 'THE_FORM_OVERUSE': 1, 'LOW_GROUNDING': 1, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 10) (let [x 99] x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '93'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 10) (let [x 99] x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '31'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(do (def x 10) (let [x 99] x))` — user_msg 221 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 10) (let [x 99] x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '70'), resolution doesn't close the loop)
    - [THE_FORM_OVERUSE] form=`(do (def x 10) (let [x 99] x))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [LOW_GROUNDING] form=`(do (def x 10) (let [x 99] x) x)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G3-06: let — binding can reference prior

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 4, 'THE_FORM_OVERUSE': 4, 'DOUBLE_NAME_INTRO': 1, 'ANSWER_LEAK': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 5 b (* a 2)] b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(let [a 5 b (* a 2)] b)` — user_msg 267 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 5 b (* a 2)] b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [THE_FORM_OVERUSE] form=`(let [a 5 b (* a 2)] b)` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [HIGH_LENGTH] form=`(let [a 5 b (* a 2)] b)` — user_msg 263 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 5 b (* a 2)] b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '4'), resolution doesn't close the loop)

### G3-07: fn — anonymous function

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 2, 'CONCEPT_AS_VERB': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (+ x 1)) 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`((fn [x] (+ x 1)) 4)` — character 'Tucker the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (+ x 1)) 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (+ x 1)) 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`((fn [a b] (* a b)) 3 4)` — character 'Zoomer the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CONCEPT_AS_VERB] form=`((fn [a b] (* a b)) 3 4)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G3-08: fn — multi-arg

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`((fn [a b c] (+ a b c)) 1 2 3)` — user_msg 208 words

### G3-09: defn — shorthand

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 1, 'HIGH_LENGTH': 1}
    - [LOW_GROUNDING] form=`(do (defn dbl [x] (* x 2)) (dbl 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defn dbl [x] (* x 2)) (dbl 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn dbl [x] (* x 2)) (dbl 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '7'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — user_msg 257 words

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 3, 'DOUBLE_NAME_INTRO': 2}
    - [CONCEPT_AS_VERB] form=`(#(+ % 1) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(#(+ % 1) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [DOUBLE_NAME_INTRO] form=`(#(* %1 %2) 3 4)` — character 'Louie the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CONCEPT_AS_VERB] form=`(#(* %1 %2) 3 4)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [DOUBLE_NAME_INTRO] form=`(#(* %1 %2) 3 4)` — character 'Bingo the dog' introduced twice within 200 chars — drop the second 'the dog'

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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def g 5) (let [g 99] (+ g 1)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '84', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def g 5) (let [g 99] (+ g 1)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('55',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def g 5) (let [g 99] (+ g 1)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('30',), resolution doesn't close the loop)

### G3-13: fn body returns last form

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 2, 'DOUBLE_NAME_INTRO': 1}
    - [HIGH_LENGTH] form=`((fn [x] x x x 99) 1)` — user_msg 252 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] x x x 99) 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`((fn [x] x x x 99) 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] x x x 99) 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`((fn [x] x x x 99) 1)` — character 'Sooty the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`((fn [x] x x x 99) 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G3-14: do form

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [LOW_GROUNDING] form=`(do 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '8'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '8'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '7'), resolution doesn't close the loop)

### G3-15: Side-effects in body

- examples: 1
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1, 'HIGH_LENGTH': 1, 'SENTENCE_START_LOWER_PRONOUN': 1}
    - [WRONG_FABLE_LITERAL] form=`(do (println "hi") 42)` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [LOW_GROUNDING] form=`(do (println "hi") 42)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (println "hi") 42)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('65', 'thread'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (println "hi") 42)` — character 'Pip the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [HIGH_LENGTH] form=`(do (println "hi") 42)` — user_msg 230 words
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do (println "hi") 42)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation

### G3-16: Name collision: namespace vs let

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [+ 99] +)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('49',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(let [+ 99] +)` — character 'Pumpkin the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(let [+ 99] +)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [+ 99] +)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('32',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [+ 99] +)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('50',), resolution doesn't close the loop)

### G3-17: Naming conventions (kebab-case)

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [hare-speed 4 tortoise-speed 1] (- hare-speed` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(let [hare-speed 4 tortoise-speed 1] (- hare-speed` — character 'Pathfinder the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [hare-speed 4 tortoise-speed 1] (- hare-speed` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [hare-speed 4 tortoise-speed 1] (- hare-speed` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)

### G3-18: When to name vs inline

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5, 'HIGH_LENGTH': 2, 'THE_FORM_OVERUSE': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [n 5] (* n n n))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [n 5] (* n n n))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(let [n 5] (* n n n))` — user_msg 243 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [n 5] (* n n n))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [THE_FORM_OVERUSE] form=`(let [n 5] (* n n n))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 5 5 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '7', '7'), resolution doesn't close the loop)

## Grade 4

### G4-01: Vector literal

- examples: 3
- variety @ n=50: 1.00
- issues: {'PARAMETRIC_LITERAL_NUMERALS': 3, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [PARAMETRIC_LITERAL_NUMERALS] form=`[1 2 3]` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [STORY_RESOLUTION_NO_DRAWN] form=`[1 2 3]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '7'), resolution doesn't close the loop)
    - [PARAMETRIC_LITERAL_NUMERALS] form=`[1 2 3]` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [STORY_RESOLUTION_NO_DRAWN] form=`[1 2 3]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '12', '4'), resolution doesn't close the loop)
    - [PARAMETRIC_LITERAL_NUMERALS] form=`[1 2 3]` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [STORY_RESOLUTION_NO_DRAWN] form=`[1 2 3]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '11', '5'), resolution doesn't close the loop)

### G4-02: nth — vector access

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 4}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(nth [10 20 30] 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '19', '19'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(nth [10 20 30] 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '13', '15'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(nth [10 20 30] 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '9', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(nth [10 20 30] 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '17', '7'), resolution doesn't close the loop)

### G4-03: conj — append to vector

- examples: 2
- variety @ n=50: 1.00
- issues: {'PARAMETRIC_LITERAL_NUMERALS': 3, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(conj [1 2] 3)` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [STORY_RESOLUTION_NO_DRAWN] form=`(conj [1 2] 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '6', '17'), resolution doesn't close the loop)
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(conj [1 2] 3)` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [STORY_RESOLUTION_NO_DRAWN] form=`(conj [1 2] 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '6', '18'), resolution doesn't close the loop)
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(conj [1 2] 3)` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [STORY_RESOLUTION_NO_DRAWN] form=`(conj [1 2] 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '11', '16'), resolution doesn't close the loop)

### G4-04: List literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'HANGING_FORM_THAT': 1, 'DOUBLE_NAME_INTRO': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '7', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '9', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '14'), resolution doesn't close the loop)
    - [HANGING_FORM_THAT] form=`'()` — 'form that <noun>' rendered without a verb — template should be 'form for {concept_phrase}'
    - [STORY_RESOLUTION_NO_DRAWN] form=`'()` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '14', '18'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`'()` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '15', '17'), resolution doesn't close the loop)

### G4-05: cons — prepend to seq

- examples: 1
- variety @ n=50: 1.00
- issues: {'PARAMETRIC_LITERAL_NUMERALS': 3, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(cons 0 '(1 2 3))` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cons 0 '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '17', '9'), resolution doesn't close the loop)
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(cons 0 '(1 2 3))` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cons 0 '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '10', '6'), resolution doesn't close the loop)
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(cons 0 '(1 2 3))` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cons 0 '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('19', '8', '8'), resolution doesn't close the loop)

### G4-06: Map literal

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`{:hare 1 :tortoise 2}` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '3', ':raspberry'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`{:hare 1 :tortoise 2}` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '12', '12'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`{:hare 1 :tortoise 2}` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '20', '6'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`{:hare 1 :tortoise 2}` — character 'Keeper the dog' introduced twice within 200 chars — drop the second 'the dog'

### G4-07: get — map lookup

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(get {:a 1 :b 2} :a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '5', ':raspberry'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(get {:a 1 :b 2} :a)` — character 'Tucker the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(get {:a 1 :b 2} :a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '19', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(get {:a 1 :b 2} :a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '14', '10'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(get {:a 1} :missing :default)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '14', '3'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(get {:a 1} :missing :default)` — character 'Buster the dog' introduced twice within 200 chars — drop the second 'the dog'

### G4-08: assoc — map update

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(assoc {:a 1} :b 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '11', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(assoc {:a 1} :b 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', ':persimmon', ':guava'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(assoc {:a 1} :b 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', ':kiwi', ':apricot'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(assoc {:a 1} :a 99)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '9', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(assoc {:a 1} :a 99)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '18', '57'), resolution doesn't close the loop)

### G4-09: dissoc — map remove key

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 2, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(dissoc {:a 1 :b 2} :a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '10', ':plum'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(dissoc {:a 1 :b 2} :a)` — character 'Charlie the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(dissoc {:a 1 :b 2} :a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '5', ':kumquat'), resolution doesn't close the loop)

### G4-10: keys and vals

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (keys {:a 1 :b 2 :c 3}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '7', ':tangerine'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (keys {:a 1 :b 2 :c 3}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '13', ':peach'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (keys {:a 1 :b 2 :c 3}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '7', ':berry'), resolution doesn't close the loop)

### G4-11: Set literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count #{1 2 3})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '8', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count #{1 2 3})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '15', '20'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count #{1 2 3})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13',), resolution doesn't close the loop)

### G4-12: Set membership

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(contains? #{1 2 3} 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '18', '12'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(contains? #{1 2 3} 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '9', '4'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(contains? #{1 2 3} 2)` — character 'Marble the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(contains? #{1 2 3} 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '9', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(contains? #{1 2 3} 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(contains? #{1 2 3} 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '4', '14'), resolution doesn't close the loop)

### G4-13: count — universal

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 11, 'DOUBLE_NAME_INTRO': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3 4 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '15', '15'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3 4 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '14', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count {:a 1 :b 2})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '17', ':orange'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(count {:a 1 :b 2})` — character 'Plum the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count {:a 1 :b 2})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '17', '14'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count {:a 1 :b 2})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '3', '9'), resolution doesn't close the loop)

### G4-14: empty?

- examples: 3
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 3, 'STORY_RESOLUTION_NO_DRAWN': 9, 'DOUBLE_NAME_INTRO': 1}
    - [BOOL_LEAK_RESOLUTION] form=`(empty? [])` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [STORY_RESOLUTION_NO_DRAWN] form=`(empty? [])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '3', '16'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(empty? [])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '4', '17'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(empty? [])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '14', '16'), resolution doesn't close the loop)
    - [BOOL_LEAK_RESOLUTION] form=`(empty? [1])` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [STORY_RESOLUTION_NO_DRAWN] form=`(empty? [1])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '14', '14'), resolution doesn't close the loop)

### G4-15: first, rest, last

- examples: 3
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'STORY_RESOLUTION_NO_DRAWN': 8, 'DOUBLE_NAME_INTRO': 1}
    - [WRONG_FABLE_LITERAL] form=`(first [10 20 30])` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first [10 20 30])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '6', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first [10 20 30])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('19', '16', '20'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first [10 20 30])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '12', '19'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(first [10 20 30])` — character 'Wallace the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(last [10 20 30])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '4', '16'), resolution doesn't close the loop)

### G4-16: into and conj on collections

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 3, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '15', '20'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(into [] '(1 2 3))` — character 'Pumpkin the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '14', '17'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '11', '9'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(into [] '(1 2 3))` — character 'Tippet the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into #{} [1 2 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G4-17: Immutability — assoc returns new

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :a 99) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '7', '95'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(let [m {:a 1}] (assoc m :a 99) m)` — character 'Pathfinder the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :a 99) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('11', '16', '69'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :a 99) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '5', '76'), resolution doesn't close the loop)

### G4-18: Equality of vectors and lists

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= [1 2 3] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '6', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= [1 2 3] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '8', '14'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= [1 2 3] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '6', '18'), resolution doesn't close the loop)

### G4-19: range and seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (range 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (range 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first (range 1 100))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('114',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first (range 1 100))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('261',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first (range 1 100))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '464'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(first (range 1 100))` — character 'Barker the dog' introduced twice within 200 chars — drop the second 'the dog'

### G4-20: Collection vs sequence

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (seq [1 2 3]))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (seq [1 2 3]))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '7', '11'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (seq [1 2 3]))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '9', '14'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(seq [])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '7', '12'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(seq [])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '13', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(seq [])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '3', '6'), resolution doesn't close the loop)

## Grade 5

### G5-01: if

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'LOW_GROUNDING': 3, 'DOUBLE_NAME_INTRO': 1, 'HIGH_LENGTH': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if true :a :b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':b', ':open'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(if true :a :b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if true :a :b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':x', ':west'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(if true :a :b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if true :a :b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':delta', ':south'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if false :a :b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':west', ':warm'), resolution doesn't close the loop)

### G5-02: if as expression

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (if true 10 20))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '10'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(+ 1 (if true 10 20))` — user_msg 253 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (if true 10 20))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '13', '19'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (if true 10 20))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '4', '17'), resolution doesn't close the loop)

### G5-03: when

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 2}
    - [HIGH_LENGTH] form=`(when true :yes)` — user_msg 218 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true :yes)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':north',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true :yes)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':low',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(when true :yes)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true :yes)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':north',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when false :yes)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':first',), resolution doesn't close the loop)

### G5-04: cond

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '3', '6'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', ':far', ':high'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '8', '3'), resolution doesn't close the loop)

### G5-05: cond — :else

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(cond false :a false :b :else :c)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(cond false :a false :b :else :c)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(cond false :a false :b :else :c)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G5-06: case

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(case 2 1 :one 2 :two 3 :three :default)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(case 2 1 :one 2 :two 3 :three :default)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '6', ':c'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(case 2 1 :one 2 :two 3 :three :default)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '9', '5'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(case 2 1 :one 2 :two 3 :three :default)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(case 2 1 :one 2 :two 3 :three :default)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '8', ':far'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(case 99 1 :one 2 :two :default)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('79', '79', ':gamma'), resolution doesn't close the loop)

### G5-07: and / or as control flow

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 1, 'HIGH_LENGTH': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(and 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(and 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '4'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(and 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(and 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(or nil false :found)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':soft',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(or nil false :found)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':gamma',), resolution doesn't close the loop)

### G5-08: not

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not (> 1 2))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not (> 1 2))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(not (> 1 2))` — character 'Watchdog the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not (> 1 2))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(not (> 1 2))` — character 'Snowball the dog' introduced twice within 200 chars — drop the second 'the dog'

### G5-10: map

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'COLLECTION_LEAK': 1, 'STORY_RESOLUTION_NO_DRAWN': 1}
    - [HIGH_LENGTH] form=`(map inc [1 2 3])` — user_msg 218 words
    - [COLLECTION_LEAK] form=`(map inc [1 2 3])` — elements of expected [2, 3, 4] appear comma-separated in user_msg (collection answer leak)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map inc [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '7', '14'), resolution doesn't close the loop)

### G5-11: filter

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 1, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(filter even? [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '8', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(filter even? [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '15', '20'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(filter even? [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(filter pos? [-2 -1 0 1 2])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '8'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(filter pos? [-2 -1 0 1 2])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(filter pos? [-2 -1 0 1 2])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '20', '14'), resolution doesn't close the loop)

### G5-12: reduce

- examples: 3
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 2, 'ANSWER_LEAK': 2, 'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 5}
    - [HIGH_LENGTH] form=`(reduce + [1 2 3 4])` — user_msg 226 words
    - [ANSWER_LEAK] form=`(reduce + [1 2 3 4])` — answer 10 in narrative
    - [LOW_GROUNDING] form=`(reduce + [1 2 3 4])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce + [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '18', '12'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(reduce + [1 2 3 4])` — user_msg 222 words
    - [ANSWER_LEAK] form=`(reduce + [1 2 3 4])` — answer 10 in narrative

### G5-13: reduce with init

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1, 'STORY_RESOLUTION_NO_DRAWN': 5, 'DOUBLE_NAME_INTRO': 2, 'LOW_GROUNDING': 1, 'HIGH_LENGTH': 1}
    - [ANSWER_LEAK] form=`(reduce + 100 [1 2 3])` — answer 106 in narrative
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce + 100 [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('492', '15', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce + 100 [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('464', '11', '18'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(reduce + 100 [1 2 3])` — character 'Jasper the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(reduce + 0 [])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce + 0 [])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '4', '20'), resolution doesn't close the loop)

### G5-14: apply

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 3, 'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 1, 'DOUBLE_NAME_INTRO': 1}
    - [HIGH_LENGTH] form=`(apply + [1 2 3 4])` — user_msg 234 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(apply + [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '3', '16'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(apply + [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '4', '17'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(apply + [1 2 3 4])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(apply + [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '14', '16'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(apply max [3 1 4 1 5])` — user_msg 222 words

### G5-15: comp

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'DOUBLE_NAME_INTRO': 2, 'HIGH_LENGTH': 1, 'ANSWER_LEAK': 1, 'CONCEPT_AS_VERB': 1}
    - [WRONG_FABLE_LITERAL] form=`((comp inc inc) 5)` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [DOUBLE_NAME_INTRO] form=`((comp inc inc) 5)` — character 'Pip the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [HIGH_LENGTH] form=`((comp inc inc) 5)` — user_msg 228 words
    - [ANSWER_LEAK] form=`((comp inc inc) 5)` — answer 7 in narrative
    - [DOUBLE_NAME_INTRO] form=`((comp str inc) 9)` — character 'Pearl the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CONCEPT_AS_VERB] form=`((comp str inc) 9)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G5-16: partial

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1, 'CONCEPT_AS_VERB': 1}
    - [DOUBLE_NAME_INTRO] form=`((partial + 10) 5)` — character 'Pumpkin the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CONCEPT_AS_VERB] form=`((partial + 10) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G5-17: juxt

- examples: 1
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1, 'HIGH_LENGTH': 1}
    - [DOUBLE_NAME_INTRO] form=`((juxt inc dec) 5)` — character 'Pathfinder the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [HIGH_LENGTH] form=`((juxt inc dec) 5)` — user_msg 212 words

### G5-18: some

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1, 'STORY_RESOLUTION_NO_DRAWN': 4, 'HIGH_LENGTH': 2, 'PREDICATE_QUESTION_COLLISION': 2}
    - [DOUBLE_NAME_INTRO] form=`(some even? [1 3 5 8 7])` — character 'Almond the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(some even? [1 3 5 8 7])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '6', '18'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(some neg? [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '11', '18'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(some neg? [1 2 3])` — user_msg 225 words
    - [PREDICATE_QUESTION_COLLISION] form=`(some neg? [1 2 3])` — predicate-suffix ``?`` collides with the question framing's trailing ``?`` or ``.``
    - [STORY_RESOLUTION_NO_DRAWN] form=`(some neg? [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '11', '9'), resolution doesn't close the loop)

### G5-19: every?

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'PREDICATE_QUESTION_COLLISION': 1, 'BOOL_LEAK_RESOLUTION': 1, 'STORY_RESOLUTION_NO_DRAWN': 4, 'DOUBLE_NAME_INTRO': 1, 'LOW_GROUNDING': 1}
    - [HIGH_LENGTH] form=`(every? pos? [1 2 3])` — user_msg 221 words
    - [PREDICATE_QUESTION_COLLISION] form=`(every? pos? [1 2 3])` — predicate-suffix ``?`` collides with the question framing's trailing ``?`` or ``.``
    - [BOOL_LEAK_RESOLUTION] form=`(every? pos? [1 2 3])` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [STORY_RESOLUTION_NO_DRAWN] form=`(every? pos? [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '8', '19'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(every? pos? [1 2 3])` — character 'Tracksman the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(every? even? [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '14', '3'), resolution doesn't close the loop)

### G5-20: take and drop

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(take 3 [10 20 30 40 50])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '18', '16'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(take 3 [10 20 30 40 50])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '12', '12'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(drop 2 [10 20 30 40 50])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '7', '12'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(drop 2 [10 20 30 40 50])` — character 'Snowball the dog' introduced twice within 200 chars — drop the second 'the dog'

### G5-21: distinct and sort

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [DOUBLE_NAME_INTRO] form=`(distinct [1 1 2 3 3 4])` — character 'Biscuit the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(distinct [1 1 2 3 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '17', '13'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(distinct [1 1 2 3 3 4])` — character 'Warden the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(sort [3 1 2])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '10', '19'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(sort [3 1 2])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '9', '8'), resolution doesn't close the loop)

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
- issues: {'LOW_GROUNDING': 5, 'HIGH_LENGTH': 2, 'ANSWER_LEAK_STRING': 1, 'WRONG_FABLE_LITERAL': 1, 'DOUBLE_NAME_INTRO': 1, 'BOOL_LEAK_RESOLUTION': 1}
    - [LOW_GROUNDING] form=`(name 'foo.bar)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name 'foo.bar)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(name 'foo.bar)` — user_msg 201 words
    - [ANSWER_LEAK_STRING] form=`(name 'foo.bar)` — answer string 'foo.bar' appears in user_msg
    - [LOW_GROUNDING] form=`(name 'clojure.string)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name 'clojure.string)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-02: ns form

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'BOOL_LEAK_RESOLUTION': 1}
    - [LOW_GROUNDING] form=`(name 'race.tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name 'race.tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name 'race.tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 'race.tortoise 'race.tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [BOOL_LEAK_RESOLUTION] form=`(= 'race.tortoise 'race.tortoise)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead

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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 12, 'DOUBLE_NAME_INTRO': 2, 'LOW_GROUNDING': 3, 'ANSWER_LEAK_STRING': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "hello")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('ember',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "hello")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('linen',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(clojure.string/upper-case "hello")` — character 'Howler the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "hello")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('raven',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/reverse "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(clojure.string/reverse "abc")` — character 'Howler the dog' introduced twice within 200 chars — drop the second 'the dog'

### G6-07: Public vs private API

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta '^:private hidden)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private', ':private'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(boolean (:private (meta '^:private hidden)))` — character 'Tucker the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta '^:private hidden)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private', ':private'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta '^:private hidden)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private', ':private'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta 'public)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(boolean (:private (meta 'public)))` — character 'Zoomer the dog' introduced twice within 200 chars — drop the second 'the dog'

### G6-08: Circular dependencies

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "a")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('candle',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "a")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('pewter',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "a")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('thistle',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(= 'a.b 'a.b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 'a.b 'a.b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-09: Loading order

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 5, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 1 b (+ a 1)] (+ a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '4'), resolution doesn't close the loop)

### G6-10: Leiningen and deps.edn

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 2, 'LOW_GROUNDING': 1, 'HEDGING_NEAR_FORM': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:deps {:deps {:a 1 :b 2}})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '13', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:deps {:deps {:a 1 :b 2}})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '13', ':warm'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(:deps {:deps {:a 1 :b 2}})` — character 'Cream the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(:deps {:deps {:a 1 :b 2}})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:deps {:deps {:a 1 :b 2}})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '19', '4'), resolution doesn't close the loop)
    - [HEDGING_NEAR_FORM] form=`(:deps {:deps {:a 1 :b 2}})` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value

### G6-11: Classpath

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [LOW_GROUNDING] form=`(clojure.string/split "src:test" #":")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "src:test" #":")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':test', 'src:test'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "src:test" #":")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':test', 'src:test'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "src:test" #":")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':test', 'src:test'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count ["src" "test" "resources"])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('src', 'test', 'resources'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count ["src" "test" "resources"])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('src', 'test', 'resources'), resolution doesn't close the loop)

### G6-12: Multiple files in one project

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(count ['race.tortoise 'race.hare 'race.shared])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(map name ['race.tortoise 'race.hare])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(map name ['race.tortoise 'race.hare])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-13: Aliasing conventions

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [HIGH_LENGTH] form=`(let [s clojure.string/upper-case] (s "hare"))` — user_msg 219 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [s clojure.string/upper-case] (s "hare"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('auburn',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(let [s clojure.string/upper-case] (s "hare"))` — user_msg 225 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [s clojure.string/upper-case] (s "hare"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('myrrh',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [s clojure.string/upper-case] (s "hare"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('coral',), resolution doesn't close the loop)

### G6-14: Import for host classes

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(symbol? 'java.util.List)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(symbol? 'java.util.List)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name 'java.util.Map)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(name 'java.util.Map)` — character 'Shadow the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(name 'java.util.Map)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name 'java.util.Map)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-15: Namespace meta

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 2, 'HIGH_LENGTH': 1}
    - [WRONG_FABLE_LITERAL] form=`(:doc (meta '\{:doc "steady wins"\} race))` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:doc (meta '\{:doc "steady wins"\} race))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':doc', ':doc', 'steady wins'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(:doc (meta '\{:doc "steady wins"\} race))` — character 'Pip the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:doc (meta '\{:doc "steady wins"\} race))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':doc', ':doc', 'steady wins'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(:doc (meta '\{:doc "steady wins"\} race))` — user_msg 205 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:doc (meta '\{:doc "steady wins"\} race))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':doc', ':doc', 'steady wins'), resolution doesn't close the loop)

### G6-16: Cleaning up requires

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'DOUBLE_NAME_INTRO': 2, 'BOOL_LEAK_RESOLUTION': 1}
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.string)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(contains? #{'clojure.string} 'clojure.string)` — character 'Pumpkin the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.string)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.string)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.set)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.set)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 7

### G7-01: throw

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(try (throw (Exception. "bad")) (catch Exception e` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "bad")) (catch Exception e` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1', 'bad'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(try (throw (Exception. "bad")) (catch Exception e` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "bad")) (catch Exception e` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1', 'bad'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "bad")) (catch Exception e` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1', 'bad'), resolution doesn't close the loop)

### G7-02: try / catch

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 3, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (/ 1 0) (catch Exception e -1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '-61'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (/ 1 0) (catch Exception e -1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '6', '-25'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (/ 1 0) (catch Exception e -1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '-12'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(try 42 (catch Exception e :caught))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try 42 (catch Exception e :caught))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('23', ':cool'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(try 42 (catch Exception e :caught))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-03: try / finally

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(try 7 (finally (prn :cleanup)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try (try (/ 1 0) (finally (prn :ran))) (catch Exc` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try (try (/ 1 0) (finally (prn :ran))) (catch Exc` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-04: ex-info

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', 'bad'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', 'bad'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — character 'Silver the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-05: nil punning

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 10, 'STORY_RESOLUTION_NO_DRAWN': 2, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(some? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(some? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(some? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(some? 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(some? 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(some? 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)

### G7-06: pre and post conditions

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exce` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exce` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exce` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-07: assert

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'DOUBLE_NAME_INTRO': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(do (assert (= 1 1)) 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do (assert (= 1 1)) 1)` — character 'Tucker the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '9'), resolution doesn't close the loop)

### G7-08: prn and pprint

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`(with-out-str (prn :hare))` — character 'Ebony the dog' introduced twice within 200 chars — drop the second 'the dog'

### G7-09: tap>

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(tap> :hello)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(tap> :hello)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(tap> 42)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(tap> 42)` — character 'Mochi the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(tap> 42)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(tap> 42)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-11: Reading stack traces

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'ANSWER_LEAK_STRING': 1}
    - [LOW_GROUNDING] form=`(try (throw (Exception. "oops")) (catch Exception ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(try (throw (Exception. "oops")) (catch Exception ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)
    - [ANSWER_LEAK_STRING] form=`(try (throw (ex-info "trouble" {})) (catch Excepti` — answer string 'trouble' appears in user_msg

### G7-12: slurp and spit

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 2, 'ANSWER_LEAK': 1}
    - [LOW_GROUNDING] form=`(count "hare
tortoise
")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "hare
tortoise
")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('amber',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(count "hare
tortoise
")` — character 'Topsy the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [ANSWER_LEAK] form=`(count "hare
tortoise
")` — answer 14 in narrative
    - [LOW_GROUNDING] form=`(count "hare
tortoise
")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "hare
tortoise
")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('feather',), resolution doesn't close the loop)

### G7-13: line-seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(count (clojure.string/split-lines "a\nb\nc"))` — character 'Sooty the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-14: with-open

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(with-out-str (println "hare"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (println "hare"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-15: *in* and *out*

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'LOW_GROUNDING': 6, 'DOUBLE_NAME_INTRO': 2}
    - [WRONG_FABLE_LITERAL] form=`(with-out-str (print "x"))` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [LOW_GROUNDING] form=`(with-out-str (print "x"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(with-out-str (print "x"))` — character 'Pip the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(with-out-str (print "x"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (print "x"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (println))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-16: edn read

- examples: 3
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 5, 'DOUBLE_NAME_INTRO': 2, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(clojure.edn/read-string "42")` — character 'Pumpkin the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "{:a 1}")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', '{:a 1}'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "{:a 1}")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', '{:a 1}'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "{:a 1}")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', '{:a 1}'), resolution doesn't close the loop)

### G7-17: JSON roundtrip

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 5, 'DOUBLE_NAME_INTRO': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-18: Shell command

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 2}
    - [LOW_GROUNDING] form=`(:cmd {:cmd "ls" :args ["-l"]})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:cmd {:cmd "ls" :args ["-l"]})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '16', ':north'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(:cmd {:cmd "ls" :args ["-l"]})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:cmd {:cmd "ls" :args ["-l"]})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '7', ':beta'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(:cmd {:cmd "ls" :args ["-l"]})` — character 'Almond the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(:cmd {:cmd "ls" :args ["-l"]})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 8

### G8-01: Why polymorphism

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':tortoise', ':else'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':tortoise', ':else'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':tortoise', ':else'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(let [speak (fn [k] (cond (= k :hare) "swift" (= k` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [speak (fn [k] (cond (= k :hare) "swift" (= k` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hedgehog', ':marten', ':marten'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(let [speak (fn [k] (cond (= k :hare) "swift" (= k` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-02: deftype introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 1, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)

### G8-03: defrecord introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'ANSWER_LEAK_STRING': 1, 'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 3}
    - [HIGH_LENGTH] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — user_msg 206 words
    - [ANSWER_LEAK_STRING] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — answer string ':slow' appears in user_msg
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':pace', ':slow', 'Alice'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':pace', ':slow', 'Alice'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':pace', ':slow', 'Alice'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defrecord Runner [name pace]) (:name (->Runne` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-04: Protocol definition

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — character 'Silver the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Greet (hail [this])) (some? Greet` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Greet (hail [this])) (some? Greet` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-05: Protocol extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('swift', 'hare'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('swift', 'hare'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('swift', 'hare'), resolution doesn't close the loop)

### G8-06: Protocol method dispatch

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-07: Record implementing protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 2}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':swift', 'Pip'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — character 'Tucker the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':swift', 'Pip'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':swift', 'Pip'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (defrecord T` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-08: Multimethod defmulti

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmulti pace :species) (defmethod pace :hare` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':species', ':hare', ':swift'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmulti pace :species) (defmethod pace :hare` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':species', ':hare', ':swift'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmulti pace :species) (defmethod pace :hare` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':species', ':hare', ':swift'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (defmulti tag :kind) (defmethod tag :stone [_]` — character 'Ebony the dog' introduced twice within 200 chars — drop the second 'the dog'

### G8-09: Multimethod defmethod

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`(do (defmulti pace :species) (defmethod pace :hare` — character 'Mochi the dog' introduced twice within 200 chars — drop the second 'the dog'

### G8-10: Multimethod vs protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'DOUBLE_NAME_INTRO': 2}
    - [LOW_GROUNDING] form=`(do (defprotocol Show (show [this])) (extend-proto` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do (defprotocol Show (show [this])) (extend-proto` — character 'Louie the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(do (defprotocol Show (show [this])) (extend-proto` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do (defprotocol Show (show [this])) (extend-proto` — character 'Bingo the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(do (defprotocol Show (show [this])) (extend-proto` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-11: Protocol vs Java interface

- examples: 1
- variety @ n=50: 0.98
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol IPace (run [this])) (extend-proto` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-12: extend-type on built-in types

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1, 'LOW_GROUNDING': 3}
    - [DOUBLE_NAME_INTRO] form=`(do (defprotocol Pace (speed [this])) (extend-type` — character 'Topsy the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-type` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-type` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-type` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-13: this-style vs fn-style

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Named (name-of [this])) (defrecor` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':n', 'Zephyr'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Named (name-of [this])) (defrecor` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':n', 'Zephyr'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (defprotocol Named (name-of [this])) (defrecor` — character 'Sooty the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-14: Protocols don't inherit

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [HIGH_LENGTH] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg 216 words
    - [LOW_GROUNDING] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)

### G8-15: derive and isa? — multimethod hierarchy

- examples: 3
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'DOUBLE_NAME_INTRO': 3, 'BOOL_LEAK_RESOLUTION': 2, 'LOW_GROUNDING': 5}
    - [WRONG_FABLE_LITERAL] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [DOUBLE_NAME_INTRO] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — character 'Pip the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [BOOL_LEAK_RESOLUTION] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(isa? java.lang.Long java.lang.Number)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(isa? java.lang.Long java.lang.Number)` — character 'Pearl the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(isa? java.lang.Long java.lang.Number)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-16: Abstract design with protocols

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 2}
    - [LOW_GROUNDING] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':leap', ':plod'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — character 'Pumpkin the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':leap', ':plod'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 9

### G9-01: Immutability as default — review

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :b 2) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '6', ':kumquat'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :b 2) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '12', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [v [1 2 3]] (conj v 4) v)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '10', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [v [1 2 3]] (conj v 4) v)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '9', '10'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [v [1 2 3]] (conj v 4) v)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '12', '20'), resolution doesn't close the loop)

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
- issues: {'HIGH_LENGTH': 1, 'LOW_GROUNDING': 4, 'DOUBLE_NAME_INTRO': 1}
    - [HIGH_LENGTH] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg 240 words
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom :start)) (reset! a :done) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom :start)) (reset! a :done) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do (def a (atom :start)) (reset! a :done) @a)` — character 'Pumpernickel the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(do (def a (atom :start)) (reset! a :done) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-04: Atom CAS semantics

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — character 'Silver the dog' introduced twice within 200 chars — drop the second 'the dog'
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
- issues: {'LOW_GROUNDING': 1, 'DOUBLE_NAME_INTRO': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — character 'Tucker the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('100', '7'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` — character 'Zoomer the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('100', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('100', '7'), resolution doesn't close the loop)

### G9-08: dosync and alter

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '5'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — character 'Ebony the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '5'), resolution doesn't close the loop)

### G9-09: Ref vs atom

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — character 'Mochi the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-10: Agent introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'DOUBLE_NAME_INTRO': 2}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do (def ag (agent 5)) (send ag + 10) (await ag) @` — character 'Louie the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [DOUBLE_NAME_INTRO] form=`(do (def ag (agent 5)) (send ag + 10) (await ag) @` — character 'Bingo the dog' introduced twice within 200 chars — drop the second 'the dog'

### G9-11: send and send-off

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 4}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send-off ag inc) (await ag` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send-off ag inc) (await ag` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-12: await — synchronizing on agents

- examples: 1
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1, 'LOW_GROUNDING': 1}
    - [DOUBLE_NAME_INTRO] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — character 'Topsy the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-13: future introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'LOW_GROUNDING': 3, 'DOUBLE_NAME_INTRO': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [HIGH_LENGTH] form=`@(future (+ 1 2))` — user_msg 210 words
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`@(future (+ 1 2))` — character 'Sooty the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`@(future (* 6 7))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '7'), resolution doesn't close the loop)

### G9-14: deref @ shorthand

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) (deref a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (def a (atom 7)) (deref a))` — character 'Shadow the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) (deref a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)

### G9-15: promise — deliver and deref

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'LOW_GROUNDING': 1, 'DOUBLE_NAME_INTRO': 2, 'ANSWER_LEAK_STRING': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [WRONG_FABLE_LITERAL] form=`(do (def p (promise)) (deliver p :done) @p)` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [LOW_GROUNDING] form=`(do (def p (promise)) (deliver p :done) @p)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do (def p (promise)) (deliver p :done) @p)` — character 'Pip the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [ANSWER_LEAK_STRING] form=`(do (def p (promise)) (deliver p :done) @p)` — answer string ':done' appears in user_msg
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def p (promise)) (deliver p 42) @p)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (def p (promise)) (deliver p 42) @p)` — character 'Pearl the dog' introduced twice within 200 chars — drop the second 'the dog'

### G9-16: volatile — when STM is too heavy

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def v (volatile! 5)) (vreset! v 99) @v)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '99'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def v (volatile! 5)) (vreset! v 99) @v)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '99'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (def v (volatile! 5)) (vreset! v 99) @v)` — character 'Topsy the dog' introduced twice within 200 chars — drop the second 'the dog'

### G9-17: binding — thread-local

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — character 'Pathfinder the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'HIGH_LENGTH': 2, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
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
- issues: {'LOW_GROUNDING': 6, 'THE_FORM_OVERUSE': 3, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [THE_FORM_OVERUSE] form=`(quote (+ 1 2))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [LOW_GROUNDING] form=`'(1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '3', '3'), resolution doesn't close the loop)

### G10-02: syntax-quote

- examples: 2
- variety @ n=50: 1.00
- issues: {'THE_FORM_OVERUSE': 3, 'LOW_GROUNDING': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1, 'HIGH_LENGTH': 1}
    - [THE_FORM_OVERUSE] form=`(let [x 10] `(+ ~x ~x))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [THE_FORM_OVERUSE] form=`(let [x 10] `(+ ~x ~x))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [LOW_GROUNDING] form=`(let [xs [1 2 3]] `(list ~@xs))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [xs [1 2 3]] `(list ~@xs))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(let [xs [1 2 3]] `(list ~@xs))` — character 'Bingo the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [HIGH_LENGTH] form=`(let [xs [1 2 3]] `(list ~@xs))` — user_msg 213 words

### G10-03: defmacro introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [HIGH_LENGTH] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg 234 words
    - [LOW_GROUNDING] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G10-04: Macro expansion rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 3, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(when true 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(macroexpand-1 '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(when true 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(macroexpand-1 '(when true 1))` — character 'Silver the dog' introduced twice within 200 chars — drop the second 'the dog'
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
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 7, 'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1, 'WRONG_FABLE_LITERAL': 1}
    - [LOW_GROUNDING] form=`(when true 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(when true 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(when true 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '5'), resolution doesn't close the loop)

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'DOUBLE_NAME_INTRO': 2, 'ANSWER_LEAK': 2, 'HIGH_LENGTH': 3, 'STORY_RESOLUTION_NO_DRAWN': 4, 'CONCEPT_AS_VERB': 1}
    - [LOW_GROUNDING] form=`(-> 5 inc inc inc)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(-> 5 inc inc inc)` — character 'Tucker the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [ANSWER_LEAK] form=`(-> 5 inc inc inc)` — answer 8 in narrative
    - [DOUBLE_NAME_INTRO] form=`(-> 5 inc inc inc)` — character 'Zoomer the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [HIGH_LENGTH] form=`(-> 5 inc inc inc)` — user_msg 240 words
    - [ANSWER_LEAK] form=`(-> 5 inc inc inc)` — answer 8 in narrative

### G10-08: Macro vs fn

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'ANSWER_LEAK': 1, 'DOUBLE_NAME_INTRO': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [ANSWER_LEAK] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — answer 7 in narrative
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — character 'Snowball the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [DOUBLE_NAME_INTRO] form=`(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3` — character 'Chestnut the dog' introduced twice within 200 chars — drop the second 'the dog'

### G10-09: Hygiene and gensym

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(symbol? (gensym))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('x_', 'x_'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — character 'Mochi the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('x_', 'x_'), resolution doesn't close the loop)

### G10-10: Anaphoric macros are confusing

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 2}
    - [HIGH_LENGTH] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — user_msg 206 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(if-let [x 7] (* x x) 0)` — character 'Louie the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [DOUBLE_NAME_INTRO] form=`(if-let [x 7] (* x x) 0)` — character 'Bingo the dog' introduced twice within 200 chars — drop the second 'the dog'

### G10-11: Reader macros overview

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 8, 'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 1, 'ANSWER_LEAK': 1}
    - [LOW_GROUNDING] form=`'(1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '8', '5'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`'(1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '15', '20'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`'(1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13',), resolution doesn't close the loop)

### G10-12: Tagged literals

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'DOUBLE_NAME_INTRO': 1, 'BOOL_LEAK_RESOLUTION': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(inst? #inst "2024-01-01")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(inst? #inst "2024-01-01")` — character 'Topsy the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(inst? #inst "2024-01-01")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(inst? #inst "2024-01-01")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [BOOL_LEAK_RESOLUTION] form=`(uuid? #uuid "00000000-0000-0000-0000-000000000000` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(uuid? #uuid "00000000-0000-0000-0000-000000000000` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-13: Data readers and EDN extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'DOUBLE_NAME_INTRO': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(clojure.edn/read-string "42")` — character 'Sooty the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "[:a :b :c]")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "[:a :b :c]")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b', ':c'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "[:a :b :c]")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b', ':c'), resolution doesn't close the loop)

### G10-14: eval (the function)

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1, 'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [ANSWER_LEAK] form=`(eval '(+ 1 2 3))` — answer 6 in narrative
    - [LOW_GROUNDING] form=`(eval '(+ 1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(eval (list '+ 4 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval (list '+ 4 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '5'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(eval (list '+ 4 5))` — character 'Shadow the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(eval (list '+ 4 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-15: When not to write a macro

- examples: 2
- variety @ n=50: 0.99
- issues: {'WRONG_FABLE_LITERAL': 1, 'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 2, 'LOW_GROUNDING': 1}
    - [WRONG_FABLE_LITERAL] form=`(do "a function suffices when no syntax shaping is` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "a function suffices when no syntax shaping is` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', 'thread'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do "a function suffices when no syntax shaping is` — character 'Pip the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "a function suffices when no syntax shaping is` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', 'alder'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "a function suffices when no syntax shaping is` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', 'indigo'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do "prefer fn unless you must shape syntax" (map ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-16: Macro pattern library

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(do (defmacro with-steady-pace [& body] `(let [pac` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro with-steady-pace [& body] `(let [pac` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':slow-and-steady'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (defmacro with-steady-pace [& body] `(let [pac` — character 'Pumpkin the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(do (defmacro with-steady-pace [& body] `(let [pac` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro with-steady-pace [& body] `(let [pac` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':slow-and-steady'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro with-steady-pace [& body] `(let [pac` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':slow-and-steady'), resolution doesn't close the loop)

## Grade 11

### G11-01: JVM vs CLR vs JS vs Python (host overview)

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'DOUBLE_NAME_INTRO': 2}
    - [LOW_GROUNDING] form=`(do "Clojure runs on multiple hosts: JVM, CLR, JS,` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do "Clojure runs on multiple hosts: JVM, CLR, JS,` — character 'Runner the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScr` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScr` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScr` — character 'Pippin the dog' introduced twice within 200 chars — drop the second 'the dog'

### G11-02: Method call syntax

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 1, 'BOOL_LEAK_RESOLUTION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(.startsWith "hare-tortoise" "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('hare-tortoise', 'hare'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(.startsWith "hare-tortoise" "hare")` — user_msg 209 words
    - [BOOL_LEAK_RESOLUTION] form=`(.startsWith "hare-tortoise" "hare")` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [STORY_RESOLUTION_NO_DRAWN] form=`(.startsWith "hare-tortoise" "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('hare-tortoise', 'hare'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(.startsWith "hare-tortoise" "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('hare-tortoise', 'hare'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(. "abc" toUpperCase)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)

### G11-03: Static method call

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [HIGH_LENGTH] form=`(Math/abs -7)` — user_msg 221 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)

### G11-04: Field access

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('ochre',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('apple',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('harbor',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('bridge',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('candle',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('myrtle',), resolution doesn't close the loop)

### G11-05: Import form

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(do "(:import (java.util Date)) imports a host cla` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "(:import (java.util Date)) imports a host cla` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do "(:import (java.util Date)) imports a host cla` — character 'Howler the dog' introduced twice within 200 chars — drop the second 'the dog'

### G11-06: new and dot-construct

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [LOW_GROUNDING] form=`(String. "go")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(String. "go")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('go',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(String. "go")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('go',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(String. "go")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(String. "go")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('go',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(new String "jump")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-07: Arrays

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 2}
    - [DOUBLE_NAME_INTRO] form=`(let [a (int-array [10 20 30])] (aget a 1))` — character 'Tucker the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [DOUBLE_NAME_INTRO] form=`(let [a (int-array [1 2 3])] (alength a))` — character 'Zoomer the dog' introduced twice within 200 chars — drop the second 'the dog'

### G11-08: Type hints

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 2, 'PROCEDURAL_OPENER': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [^String s "abc"] (.toUpperCase s))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [^String s "abc"] (.toUpperCase s))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [^String s "abc"] (.toUpperCase s))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do "type hints are metadata that guide compilatio` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "type hints are metadata that guide compilatio` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PROCEDURAL_OPENER] form=`(do "type hints are metadata that guide compilatio` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence

### G11-09: Checked vs unchecked math

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'REPL_AS_TIME_TRAVELLER': 2, 'STORY_RESOLUTION_NO_DRAWN': 1}
    - [LOW_GROUNDING] form=`(+ 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [REPL_AS_TIME_TRAVELLER] form=`(+ 1 2)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '7'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do "*unchecked-math* turns off overflow checking ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [REPL_AS_TIME_TRAVELLER] form=`(do "*unchecked-math* turns off overflow checking ` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

### G11-10: ClojureScript overview

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'DOUBLE_NAME_INTRO': 2, 'HEDGING_NEAR_FORM': 1}
    - [LOW_GROUNDING] form=`(do "ClojureScript compiles to JavaScript via the ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do "ClojureScript compiles to JavaScript via the ` — character 'Louie the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(do "cljs runs in browsers and Node, with JS inter` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "cljs runs in browsers and Node, with JS inter` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [LOW_GROUNDING] form=`(do "cljs runs in browsers and Node, with JS inter` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do "cljs runs in browsers and Node, with JS inter` — character 'Warden the dog' introduced twice within 200 chars — drop the second 'the dog'

### G11-11: cljs / JavaScript interop

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(do "(js/console.log x) calls a JS global; (.-foo ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "(js/console.log x) calls a JS global; (.-foo ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-12: Basilisp overview (Python host)

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'HEDGING_NEAR_FORM': 1}
    - [LOW_GROUNDING] form=`(do "basilisp is a Clojure-like Lisp implemented o` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "basilisp is a Clojure-like Lisp implemented o` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [LOW_GROUNDING] form=`(do "basilisp is a Clojure-like Lisp implemented o` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "basilisp interops with Python via the same do` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-13: Cross-platform .cljc and reader-conditionals

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'LOW_GROUNDING': 2, 'DOUBLE_NAME_INTRO': 1}
    - [WRONG_FABLE_LITERAL] form=`(do "#?(:clj … :cljs …) selects a form per host at` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [LOW_GROUNDING] form=`(do "#?(:clj … :cljs …) selects a form per host at` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do ".cljc files share code across multiple hosts"` — character 'Champ the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(do ".cljc files share code across multiple hosts"` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-14: Debugging host leaks

- examples: 2
- variety @ n=50: 1.00
- issues: {'PROCEDURAL_OPENER': 1, 'LOW_GROUNDING': 2, 'DOUBLE_NAME_INTRO': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [PROCEDURAL_OPENER] form=`(do "host stack traces leak through interop; learn` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    - [LOW_GROUNDING] form=`(do "host stack traces leak through interop; learn` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do "host stack traces leak through interop; learn` — character 'Shadow the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(do "host stack traces leak through interop; learn` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (Math/sqrt 4) (catch Exception _ :err))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', ':err'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(try (Math/sqrt 4) (catch Exception _ :err))` — character 'Shadow the dog' introduced twice within 200 chars — drop the second 'the dog'

## Grade 12

### G12-01: Transducers introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'COLLECTION_LEAK': 1, 'WRONG_FABLE_LITERAL': 1}
    - [HIGH_LENGTH] form=`(into [] (map inc) [1 2 3])` — user_msg 257 words
    - [COLLECTION_LEAK] form=`(into [] (map inc) [1 2 3])` — elements of expected [2, 3, 4] appear comma-separated in user_msg (collection answer leak)
    - [WRONG_FABLE_LITERAL] form=`(into [] (filter even?) [1 2 3 4 5])` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg

### G12-02: Transducer composition

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', '5'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — user_msg 207 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', '5'), resolution doesn't close the loop)

### G12-03: into with a transducer (xform)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'COLLECTION_LEAK': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [HIGH_LENGTH] form=`(into #{} (map inc) [1 2 3])` — user_msg 265 words
    - [COLLECTION_LEAK] form=`(into #{} (map inc) [1 2 3])` — elements of expected {2, 3, 4} appear comma-separated in user_msg (collection answer leak)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (take 3) (range 100))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '100'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (take 3) (range 100))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '100'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (take 3) (range 100))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '100'), resolution doesn't close the loop)

### G12-05: Channels and pipelines

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(do "pipe, mult, mix, pipeline-async route values ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "pipe, mult, mix, pipeline-async route values ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do "pipe, mult, mix, pipeline-async route values ` — character 'Howler the dog' introduced twice within 200 chars — drop the second 'the dog'

### G12-06: clojure.spec

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1}
    - [HEDGING_NEAR_FORM] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value

### G12-07: Spec generators

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1}
    - [HEDGING_NEAR_FORM] form=`(do "spec generators turn specs into property-base` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value

### G12-08: clojure.test

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'DOUBLE_NAME_INTRO': 1}
    - [HEDGING_NEAR_FORM] form=`(= (+ 1 2) 3)` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [DOUBLE_NAME_INTRO] form=`(do "(deftest …), (is …), (testing …) are the core` — character 'Zippy the dog' introduced twice within 200 chars — drop the second 'the dog'

### G12-09: Test fixtures

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'HEDGING_NEAR_FORM': 1}
    - [LOW_GROUNDING] form=`(do "(use-fixtures :each f) wraps every deftest in` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "fixtures provide setup/teardown around deftes` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "fixtures provide setup/teardown around deftes` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [LOW_GROUNDING] form=`(do "fixtures provide setup/teardown around deftes` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-10: Property-based testing

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'HEDGING_NEAR_FORM': 2}
    - [LOW_GROUNDING] form=`(= (reverse (reverse [1 2 3])) [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(= (reverse (reverse [1 2 3])) [1 2 3])` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [LOW_GROUNDING] form=`(do "test.check generates inputs and checks proper` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "test.check generates inputs and checks proper` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [LOW_GROUNDING] form=`(do "test.check generates inputs and checks proper` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-11: Leiningen project.clj

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(do "project.clj declares :dependencies, :main, :p` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "project.clj declares :dependencies, :main, :p` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-12: deps.edn projects

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'HEDGING_NEAR_FORM': 1}
    - [LOW_GROUNDING] form=`(do "deps.edn declares :deps and :aliases for the ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "deps.edn declares :deps and :aliases for the ` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [LOW_GROUNDING] form=`(do "deps.edn declares :deps and :aliases for the ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "deps.edn is read by the official `clj`/`cloju` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-13: Aliases and tools

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'LOW_GROUNDING': 2, 'DOUBLE_NAME_INTRO': 1}
    - [WRONG_FABLE_LITERAL] form=`(do "`clj -M:test` runs the :test alias from deps.` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [LOW_GROUNDING] form=`(do "`clj -M:test` runs the :test alias from deps.` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do "aliases compose extra paths, deps, and main o` — character 'Champ the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(do "aliases compose extra paths, deps, and main o` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-14: Pedestal / Ring (web stack brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1, 'LOW_GROUNDING': 2}
    - [DOUBLE_NAME_INTRO] form=`(do "Ring models HTTP as request-map -> response-m` — character 'Shadow the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(do "Ring models HTTP as request-map -> response-m` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "Pedestal layers interceptors over Ring for ri` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-15: Datomic / XTDB (datalog db brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'LOW_GROUNDING': 3, 'HEDGING_NEAR_FORM': 1}
    - [WRONG_FABLE_LITERAL] form=`(do "Datomic and XTDB are immutable, time-aware da` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [LOW_GROUNDING] form=`(do "Datomic and XTDB are immutable, time-aware da` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "Datomic and XTDB are immutable, time-aware da` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "Datomic and XTDB are immutable, time-aware da` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [LOW_GROUNDING] form=`(do "queries are written in datalog over EDN-shape` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-16: Reagent (cljs UI brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(do "components are functions returning Hiccup vec` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "components are functions returning Hiccup vec` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "components are functions returning Hiccup vec` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-17: Library design patterns

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(do "good libraries expose data, then functions, t` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= [1 2 3] (vec '(1 2 3)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-18: Clojure style guide

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4}
    - [LOW_GROUNDING] form=`(do "kebab-case names, two-space indent, threading` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "kebab-case names, two-space indent, threading` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "prefer pure functions, name predicates with ?` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "prefer pure functions, name predicates with ?` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

---

## Summary

### Issue counts (across all examples × 3 records)

- **STORY_RESOLUTION_NO_DRAWN**: 818
- **LOW_GROUNDING**: 413
- **DOUBLE_NAME_INTRO**: 222
- **HIGH_LENGTH**: 78
- **REPL_AS_TIME_TRAVELLER**: 31
- **BOOL_LEAK_RESOLUTION**: 24
- **ANSWER_LEAK**: 17
- **THE_FORM_OVERUSE**: 16
- **WRONG_FABLE_LITERAL**: 16
- **HEDGING_NEAR_FORM**: 11
- **PARAMETRIC_LITERAL_NUMERALS**: 9
- **CONCEPT_AS_VERB**: 7
- **ANSWER_LEAK_STRING**: 6
- **PROCEDURAL_OPENER**: 4
- **COLLECTION_LEAK**: 3
- **PREDICATE_QUESTION_COLLISION**: 3
- **SENTENCE_START_LOWER_PRONOUN**: 2
- **SMALL_INT_LEAK**: 1
- **HANGING_FORM_THAT**: 1

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 172 | — |
| 2 | 22 | 88 | 312 | — |
| 3 | 18 | 31 | 131 | — |
| 4 | 20 | 39 | 137 | — |
| 5 | 22 | 39 | 147 | — |
| 6 | 16 | 33 | 117 | — |
| 7 | 18 | 36 | 140 | — |
| 8 | 16 | 31 | 130 | — |
| 9 | 18 | 34 | 106 | — |
| 10 | 16 | 36 | 160 | — |
| 11 | 14 | 29 | 75 | — |
| 12 | 18 | 37 | 55 | — |

### Sample issues by severity

#### LOW_GROUNDING

- `G1-01` (form `nil`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    A reflection is a strange kind of promise: present and unreachable, and very hard to argue with.

A few stream-side creatures had gathered on the bank by the pond to
watch Steel the dog attempt to outwit Yappy the dog at reading
the REPL. The water moved on, the bridge held its shadow, and
Yappy poi...
    ```
- `G1-01` (form `nil`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    Ace had found the bone near the road and was carrying it home with no small amount of pride.

Halfway across the bridge, Hugo the dog stopped on the road and refused
to take another step until someone could prove what the form
`nil` evaluated to. The reflection below glittered.
Hugo called the answe...
    ```
- `G1-02` (form `7`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    It was an afternoon of quiet sky and steady current, and the world below the surface seemed almost solid.

A few stream-side creatures had gathered on the bank at the village to
watch Honey the dog attempt to outwit Hound the dog at reading
the REPL. The water moved on, the bridge held its shadow, a...
    ```
- `G1-03` (form `1/2`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    in the forest, the stream ran clear enough to mirror anything that passed above it, and Leo passed above it.

Leo the dog had been keeping a small bark-scratch tally of
every form he had successfully evaluated — each new
mark deepening the line and crowding out the day's wishful guesses.
Today at th...
    ```
- `G1-05` (form `true`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    There was once a dog who carried a fine bone home along a path that crossed a stream by an old wooden bridge.

A few stream-side creatures had gathered on the bank near the meadow to
watch Riley the dog attempt to outwit Yipper the dog at reading
the REPL. The water moved on, the bridge held its sha...
    ```

#### DOUBLE_NAME_INTRO

- `G1-02` (form `-25`): character 'Sniff the dog' introduced twice within 200 chars — drop the second 'the dog'
    ```
    Sniff the dog was halfway home at the edge of the forest when the water played its old trick on a young dog.

Sniff the dog had been showing Bailey the dog how the REPL works,
the stream cool against their paws and the bridge's shadow long.
"Look here," he said, pointing to the integer -60.
"You han...
    ```
- `G1-03` (form `(+ 1/2 1/4)`): character 'Pumpernickel the dog' introduced twice within 200 chars — drop the second 'the dog'
    ```
    It was on the beach, on the wooden bridge above the slow brook, that Pumpernickel the dog looked down at the water.

Loki the dog chalked a wager on a flat stone by the beach: whoever
predicted the result of `(+ 1/2 1/4)` would set who crossed the
bridge first. Pumpernickel the dog, with the slow gr...
    ```
- `G1-03` (form `(- 1 1/3)`): character 'Snowball the dog' introduced twice within 200 chars — drop the second 'the dog'
    ```
    Snowball the dog was crossing the stream at the edge of the forest when he caught a glimpse of his own reflection.

Snowball the dog had been keeping a small bark-scratch tally of
every form he had successfully evaluated — each new
mark deepening the line and crowding out the day's wishful guesses.
...
    ```
- `G1-03` (form `(- 1 1/3)`): character 'Whatsit the dog' introduced twice within 200 chars — drop the second 'the dog'
    ```
    It was on the river bank, on the wooden bridge above the slow brook, that Whatsit the dog looked down at the water.

With a twig, Bounder the dog marked a wager into the wet sand along the river bank:
whoever guessed the result of `(- 7 1/3)` first would choose
which bone to carry. Whatsit the dog, ...
    ```
- `G1-04` (form `"race"`): character 'Gizmo the dog' introduced twice within 200 chars — drop the second 'the dog'
    ```
    near the village, where the path crosses the stream, Gizmo the dog trotted home with a fine bone in his teeth.

A few stream-side creatures had gathered on the bank near the village to
watch Tucker the dog attempt to outwit Gizmo the dog at reading
the REPL. The water moved on, the bridge held its s...
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

- `G1-09` (form `(symbol? 42)`): user_msg 212 words
    ```
    Silver had crossed this bridge a hundred times by the village, but never with so fine a bone clamped in his jaws.

Patch the hound stood at the stream's edge, holding two objects side by side: a scratch-mark on bark and a smooth stone bearing the number 68. "This one is the symbol," Patch said, tapp...
    ```
- `G1-09` (form `(= 'hare 'hare)`): user_msg 208 words
    ```
    in the meadow, where the boards of the bridge meet the stones of the path, Jack the dog caught sight of himself in the stream.

Rex the hound laid two scratch-marks side by side on bark near the forest. Both marks said the same thing: hare, hare. "Are these two scratches the same name?" Rex asked. "...
    ```
- `G1-11` (form `(+
  1
  2)`): user_msg 203 words
    ```
    A dog with a bone in his jaws is a happy creature; a dog who looks too hard at the water may not be.

Patch the hound marked a form on a long bark-strip at the stream's edge but spread the tokens across many lines, each indented neatly. "Does the layout change what the form says?" his packmate asked...
    ```
- `G1-14` (form `(+ 1 (* 2 3))`): user_msg 217 words
    ```
    The stream ran clear that afternoon, and the bridge cast a long trembling shadow across the water.

Patch the hound marked a nested form on bark near the river bank. Inside the outer addition lived a multiplication. "The inner form runs first," Patch said. "Its answer becomes food for the outer form...
    ```
- `G1-14` (form `(* (+ 1 2) (+ 3 4))`): user_msg 209 words
    ```
    Henry had found the bone in the meadow and was carrying it home with no small amount of pride.

Rex the hound marked two nested forms side by side on a flat stone. The left nested form was an addition; the right was another. "Both run first," Rex said. "Then their two answers become the operands of ...
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

#### THE_FORM_OVERUSE

- `G1-11` (form `(+
  1
  2)`): `the form` appears 5 times in user_msg (template tic — vary references)
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
at the front, the rest trailing behind. The river ran past, and
the bones stayed in their order, each one waiting to be rea...
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

#### PROCEDURAL_OPENER

- `G2-20` (form `(count "hello")`): user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    ```
    It was along the road, on the wooden bridge above the slow brook, that Boomer the dog looked down at the water.

To count the characters in the string myrtle, he composed the count operation and submitted the form. The REPL walked the bone-row carrying the tally:

Question: write a Clojure expressio...
    ```
- `G2-20` (form `(count [])`): user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    ```
    It happened on the road, on the very bridge Tiggs the dog crossed every day, that he stopped longer than he should have.

To count the elements in an empty vector, she composed the count operation and submitted the form. The REPL walked the bone-row carrying the tally:

What Clojure form computes th...
    ```
- `G11-08` (form `(do "type hints are metadata that guide compilation" :studie`): user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    ```
    On a path that ran beside the stream, a dog was carrying his supper home and looking pleased with himself.

To understand that type hints guide compilation, he composed the purpose of type hints in Clojure and submitted the form. The REPL — calling into the kennel-master's shed — returned:

Question...
    ```
- `G11-14` (form `(do "host stack traces leak through interop; learn to read t`): user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    ```
    The stream ran clear that afternoon, and the bridge cast a long trembling shadow across the water.

To learn to read and debug host runtime errors, he composed debugging host-runtime errors and submitted the form. The REPL — calling into the kennel-master's shed — returned:

Write a Clojure expressi...
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
at the front, the rest trailing behind. The river ran past, and
the bones stayed in their order, each one waiting t...
    ```
- `G4-01` (form `[1 2 3]`): parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    ```
    Sooty had crossed this bridge a hundred times near the river bank, but never with so fine a bone clamped in his jaws.

Sooty the dog, as a hen sits the long sit upon her eggs, pointed to a hollow log on the river bank,
its inside lined with bones tucked into named slots — the wood
cool, the slots so...
    ```
- `G4-01` (form `[1 2 3]`): parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    ```
    It is one of the oldest tricks of light to make one bone seem like two and to make a fool of the unwary.

Woofer the dog, untroubled by what others thought, pointed to a hollow log along the river bank,
its inside lined with bones tucked into named slots — the wood
cool, the slots solid. "Whatever I...
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

Sprocket the dog, her face quiet, her hands quieter still, pointed to a hollow log by the forest,
its inside lined with bones tucked into named slots — the wood
cool, the slots solid. "Whatev...
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

#### HEDGING_NEAR_FORM

- `G6-10` (form `(:deps {:deps {:a 1 :b 2}})`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    The water beneath the bridge was unhurried that day, and any creature looking down would see a perfect copy of itself.

A wager was set at the village: produce the value before the next ripple
crossed the pond. Pebble the dog bolted into a flurry of guesses,
calling out numbers and second-guessing h...
    ```
- `G11-10` (form `(do "cljs runs in browsers and Node, with JS interop syntax"`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    It is one of the oldest tricks of light to make one bone seem like two and to make a fool of the unwary.

A wager was set by the village: produce the value before the next ripple
crossed the pond. Collie the dog bolted into a flurry of guesses,
calling out numbers and second-guessing himself about
w...
    ```
- `G11-12` (form `(do "basilisp is a Clojure-like Lisp implemented on Python" `): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    at the edge of the meadow, where the path crosses the stream, Topsy the dog trotted home with a fine bone in his teeth.

A wager was set at the edge of the meadow: produce the value before the next ripple
crossed the pond. Trailblazer the dog bolted into a flurry of guesses,
calling out numbers and ...
    ```
- `G12-06` (form `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42)`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    Cooper had carried his prize all the way from the village, and near the road the bridge offered him an unwelcome second look.

A wager was set along the road: produce the value before the next ripple
crossed the pond. Pathfinder the dog bolted into a flurry of guesses,
calling out numbers and second...
    ```
- `G12-07` (form `(do "spec generators turn specs into property-based test inp`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    Gus had carried his prize all the way from the village, and on the beach the bridge offered him an unwelcome second look.

A wager was set by the beach: produce the value before the next ripple
crossed the pond. Pointer the dog bolted into a flurry of guesses,
calling out numbers and second-guessing...
    ```

