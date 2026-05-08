# tortoise-hare curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

### G1-09: Symbols vs values

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(symbol? 42)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('73',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(symbol? 42)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('51',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(symbol? 42)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(symbol? "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('river',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(symbol? "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('cobalt',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(symbol? "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('coral',), resolution doesn't close the loop)

### G1-10: Comments

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2) ; sum of one and two` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2) ; sum of one and two` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`42 ;; the answer` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('32',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`42 ;; the answer` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('80',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`42 ;; the answer` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('74',), resolution doesn't close the loop)

### G1-11: Whitespace doesn't matter

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+    1    2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+    1    2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+    1    2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+
  1
  2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+
  1
  2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '8'), resolution doesn't close the loop)

### G1-12: Parens group; they don't multiply

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5, 'SMALL_INT_LEAK': 1, 'ANSWER_LEAK': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '7'), resolution doesn't close the loop)
    - [SMALL_INT_LEAK] form=`(+ 2 3)` — small-int answer 5 leaks via resolution-slot phrasing
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* (+ 1 2) 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '8'), resolution doesn't close the loop)
    - [ANSWER_LEAK] form=`(* (+ 1 2) 3)` — answer 9 in narrative
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* (+ 1 2) 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '9', '9'), resolution doesn't close the loop)

### G1-13: First arithmetic call

- examples: 6
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 17, 'REPL_AS_TIME_TRAVELLER': 2, 'REPEATED_OPENER_FRAGMENT': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(- 5 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(- 5 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(- 5 3)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

### G1-14: Nested call evaluation

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 12, 'REPL_AS_TIME_TRAVELLER': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (* 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (* 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (* 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '5', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* (+ 1 2) (+ 3 4))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '5', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* (+ 1 2) (+ 3 4))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '3', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* (+ 1 2) (+ 3 4))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '5', '9'), resolution doesn't close the loop)

### G1-15: Equality

- examples: 6
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 16, 'CONCEPT_AS_VERB': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= 1 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= 1 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '9'), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`(= 1 2)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G1-16: Numeric predicates

- examples: 6
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 15, 'REPL_AS_TIME_TRAVELLER': 4}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(zero? 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(zero? 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(zero? 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(zero? 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(zero? 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(pos? 7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)

### G1-17: Printing vs returning

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`42` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('52',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`42` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('87',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`42` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('43',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '9'), resolution doesn't close the loop)

### G1-18: Errors are safe in the REPL

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 7 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 7 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 7 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '8'), resolution doesn't close the loop)

## Grade 2

### G2-01: Multi-arg arithmetic

- examples: 6
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'REPL_AS_TIME_TRAVELLER': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '9', '7'), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(* 1 2 3 4 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [REPL_AS_TIME_TRAVELLER] form=`(* 1 2 3 4 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

### G2-02: Comparison chains

- examples: 5
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'REPL_AS_TIME_TRAVELLER': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(< 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(< 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(< 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '8', '3'), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(<= 1 1 2)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

### G2-03: not= and = with multiple args

- examples: 5
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'REPL_AS_TIME_TRAVELLER': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not= 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not= 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not= 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(= 1 1 2)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [REPL_AS_TIME_TRAVELLER] form=`(= 1 1 2)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

### G2-04: min and max

- examples: 5
- variety @ n=50: 1.00
- issues: {'REPL_AS_TIME_TRAVELLER': 4, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [REPL_AS_TIME_TRAVELLER] form=`(min 1 2 3)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(min 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '3', '3'), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(min 1 2 3)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(min 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(min 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '8'), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(max 1 2 3)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

### G2-05: quot, rem, mod

- examples: 6
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'REPL_AS_TIME_TRAVELLER': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(quot 17 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '17'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(quot 17 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('11', '-15'), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(quot 17 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(quot 17 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-4',), resolution doesn't close the loop)

### G2-06: inc and dec

- examples: 5
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1, 'REPL_AS_TIME_TRAVELLER': 2, 'STORY_RESOLUTION_NO_DRAWN': 1}
    - [ANSWER_LEAK] form=`(inc 5)` — answer 6 in narrative
    - [REPL_AS_TIME_TRAVELLER] form=`(inc 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inc 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(dec 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

### G2-07: Absolute value

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(abs 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(abs 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(abs 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)

### G2-08: Arithmetic on ratios

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'REPL_AS_TIME_TRAVELLER': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1/2 1/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1/2 1/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1/2 1/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(- 1 1/3)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

### G2-09: Floats vs ints (the / operator)

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(/ 10 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '-16'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(/ 10 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '12'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(/ 10 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)

### G2-10: Powers via repeated multiplication

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 2 2 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3', '3'), resolution doesn't close the loop)

### G2-11: String concatenation with str

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(str "ab" "cd")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('saffron', 'indigo'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(str "ab" "cd")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('saffron', 'ochre'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(str "ab" "cd")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('auburn', 'cobalt'), resolution doesn't close the loop)

### G2-12: print and println — return values

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(println "hello")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('amber',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(println "hello")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('cedar',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(println "hello")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('ochre',), resolution doesn't close the loop)

### G2-13: and / or — short circuit, return values

- examples: 6
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 5}
    - [CONCEPT_AS_VERB] form=`(or false true)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(or false false)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(and 1 2 3)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(and 1 2 3)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(or nil false 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G2-14: not — turning truthy to false

- examples: 5
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 2}
    - [CONCEPT_AS_VERB] form=`(not 0)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(not "")` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G2-15: Falsey values: only false and nil

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1, 'CONCEPT_AS_VERB': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if 0 1 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '5'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(if 0 1 0)` — user_msg 205 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if 0 1 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if 0 1 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`(if "" 1 0)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G2-16: Truthy 0 and empty string

- examples: 4
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 4, 'STORY_RESOLUTION_NO_DRAWN': 2}
    - [CONCEPT_AS_VERB] form=`(boolean 0)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`(boolean "")` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(boolean "")` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(boolean nil)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G2-17: Keyword as function for map lookup

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:hare {:hare 1 :tortoise 2})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '7', ':doe'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:hare {:hare 1 :tortoise 2})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '18', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:hare {:hare 1 :tortoise 2})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '20', ':vole'), resolution doesn't close the loop)

### G2-19: Auto-promotion to bigint

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'ANSWER_LEAK': 1, 'REPL_AS_TIME_TRAVELLER': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 1000000 1000000)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('1048576', '1048576'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 1000000 1000000)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10000000', '10000000'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 1000000 1000000)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('2147483647', '2147483647'), resolution doesn't close the loop)
    - [ANSWER_LEAK] form=`(+ 99999999999 1)` — answer 100000000000 in narrative
    - [REPL_AS_TIME_TRAVELLER] form=`(+ 99999999999 1)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [REPL_AS_TIME_TRAVELLER] form=`(+ 99999999999 1)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

### G2-20: Counting

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 4}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '7'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '5', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '16', '20'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count [])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count [])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-21: String length and substring

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('alder',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('pewter',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('auburn',), resolution doesn't close the loop)

### G2-22: Compose pure arithmetic (multi-step calculation)

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(- (* 5 4) 7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(- (* 5 4) 7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(- (* 5 4) 7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '3'), resolution doesn't close the loop)

## Grade 3

### G3-01: def — top-level binding

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 42) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('28',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 42) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('38',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 42) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('84',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def y 7) y)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def y 7) y)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)

### G3-02: def — redefinition

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 1) (def x 99) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('78',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 1) (def x 99) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('36',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 1) (def x 99) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '86'), resolution doesn't close the loop)

### G3-03: let — local binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 8}
    - [HIGH_LENGTH] form=`(let [x 3] (+ x 1))` — user_msg 232 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 3] (+ x 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 3] (+ x 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 3] (+ x 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [n 10] (* n n))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [n 10] (* n n))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)

### G3-04: let — multi-binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 1 b 2] (+ a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 1 b 2] (+ a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 1 b 2] (+ a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 5 y 3] (- x y))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 5 y 3] (- x y))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 5 y 3] (- x y))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)

### G3-05: let — shadowing outer def

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 1}
    - [LOW_GROUNDING] form=`(do (def x 10) (let [x 99] x))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 10) (let [x 99] x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '93'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (def x 10) (let [x 99] x))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 10) (let [x 99] x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('11', '31'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 10) (let [x 99] x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('54',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (def x 10) (let [x 99] x) x)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G3-06: let — binding can reference prior

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5, 'HIGH_LENGTH': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 5 b (* a 2)] b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 5 b (* a 2)] b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '6', '7'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — user_msg 224 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)

### G3-07: fn — anonymous function

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CONCEPT_AS_VERB] form=`((fn [a b] (* a b)) 3 4)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5, 'CONCEPT_AS_VERB': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn dbl [x] (* x 2)) (dbl 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn dbl [x] (* x 2)) (dbl 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3', '7'), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CONCEPT_AS_VERB': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [HIGH_LENGTH] form=`(#(+ % 1) 5)` — user_msg 205 words
    - [CONCEPT_AS_VERB] form=`(#(+ % 1) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(#(+ % 1) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(* %1 %2) 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(* %1 %2) 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(* %1 %2) 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)

### G3-11: Substitution rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 7] (+ a a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 7] (+ a a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 7] (+ a a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)

### G3-12: Scope vs namespace

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def g 5) (let [g 99] (+ g 1)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '84', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def g 5) (let [g 99] (+ g 1)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '89'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def g 5) (let [g 99] (+ g 1)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '24', '9'), resolution doesn't close the loop)

### G3-13: fn body returns last form

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [HIGH_LENGTH] form=`((fn [x] x x x 99) 1)` — user_msg 201 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] x x x 99) 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] x x x 99) 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] x x x 99) 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99',), resolution doesn't close the loop)

### G3-14: do form

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '5', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (+ 1 1) (+ 2 2) (+ 3 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '4', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (+ 1 1) (+ 2 2) (+ 3 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '7', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (+ 1 1) (+ 2 2) (+ 3 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '8', '5'), resolution doesn't close the loop)

### G3-15: Side-effects in body

- examples: 1
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CONCEPT_AS_VERB] form=`(do (println "hi") 42)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (println "hi") 42)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('65', 'raven'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (println "hi") 42)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('35', 'indigo'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (println "hi") 42)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('35', 'myrtle'), resolution doesn't close the loop)

### G3-16: Name collision: namespace vs let

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [+ 99] +)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('88',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(let [+ 99] +)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [+ 99] +)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('29',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [+ 99] +)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('33',), resolution doesn't close the loop)

### G3-17: Naming conventions (kebab-case)

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [hare-speed 4 tortoise-speed 1] (- hare-speed` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [hare-speed 4 tortoise-speed 1] (- hare-speed` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '5'), resolution doesn't close the loop)

### G3-18: When to name vs inline

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [n 5] (* n n n))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 5 5 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 5 5 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3', '3'), resolution doesn't close the loop)

## Grade 4

### G4-01: Vector literal

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`[1 2 3]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`[1 2 3]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '14', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`[1 2 3]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('19', '15', '12'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`[]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '18', '19'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`[]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '12', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`[]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '9', '14'), resolution doesn't close the loop)

### G4-02: nth — vector access

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(nth [10 20 30] 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '10', '15'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(nth [10 20 30] 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '13', '13'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(nth [10 20 30] 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '14'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(nth [10 20 30] 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '9', '19'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(nth [10 20 30] 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(nth [10 20 30] 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '16', '13'), resolution doesn't close the loop)

### G4-03: conj — append to vector

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(conj [1 2] 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '6', '17'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(conj [1 2] 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '12', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(conj [1 2] 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '13', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(conj [] :hare)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '8', '19'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(conj [] :hare)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '14', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(conj [] :hare)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '14', '8'), resolution doesn't close the loop)

### G4-04: List literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '7', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '7', '10'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '6', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`'()` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '18', '15'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`'()` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '17', '15'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`'()` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '15', '17'), resolution doesn't close the loop)

### G4-05: cons — prepend to seq

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cons 0 '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '17', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cons 0 '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '3', '10'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cons 0 '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '13', '7'), resolution doesn't close the loop)

### G4-06: Map literal

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`{:hare 1 :tortoise 2}` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '3', ':raspberry'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`{:hare 1 :tortoise 2}` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '12', '12'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`{:hare 1 :tortoise 2}` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '9', ':mandarin'), resolution doesn't close the loop)

### G4-07: get — map lookup

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'ANSWER_LEAK_STRING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(get {:a 1 :b 2} :a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '17', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(get {:a 1 :b 2} :a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '20', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(get {:a 1 :b 2} :a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '10', ':apple'), resolution doesn't close the loop)
    - [ANSWER_LEAK_STRING] form=`(get {:a 1} :missing :default)` — answer string ':default' appears in user_msg
    - [STORY_RESOLUTION_NO_DRAWN] form=`(get {:a 1} :missing :default)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '15', ':blackberry'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(get {:a 1} :missing :default)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '15', '4'), resolution doesn't close the loop)

### G4-08: assoc — map update

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(assoc {:a 1} :b 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '11', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(assoc {:a 1} :b 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '3', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(assoc {:a 1} :b 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '16', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(assoc {:a 1} :a 99)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '95', ':strawberry'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(assoc {:a 1} :a 99)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '9', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(assoc {:a 1} :a 99)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '4', '98'), resolution doesn't close the loop)

### G4-09: dissoc — map remove key

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(dissoc {:a 1 :b 2} :a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '10', ':plum'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(dissoc {:a 1 :b 2} :a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '11', ':lime'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(dissoc {:a 1 :b 2} :a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '6', ':kiwi'), resolution doesn't close the loop)

### G4-10: keys and vals

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (keys {:a 1 :b 2 :c 3}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '7', ':tangerine'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (keys {:a 1 :b 2 :c 3}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '3', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (keys {:a 1 :b 2 :c 3}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '9', ':guava'), resolution doesn't close the loop)

### G4-11: Set literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count #{1 2 3})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '8', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count #{1 2 3})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '15', '20'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count #{1 2 3})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '19', '20'), resolution doesn't close the loop)

### G4-12: Set membership

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(contains? #{1 2 3} 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '18', '12'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(contains? #{1 2 3} 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '7', '14'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(contains? #{1 2 3} 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '10', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(contains? #{1 2 3} 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '9', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(contains? #{1 2 3} 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '8', '10'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(contains? #{1 2 3} 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '4', '14'), resolution doesn't close the loop)

### G4-13: count — universal

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 12}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3 4 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '15', '15'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3 4 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '14', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3 4 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '20', '19'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count {:a 1 :b 2})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '14', ':nectarine'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count {:a 1 :b 2})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '17', ':orange'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count {:a 1 :b 2})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '6', ':elderberry'), resolution doesn't close the loop)

### G4-14: empty?

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(empty? [])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '3', '16'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(empty? [])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '7', '18'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(empty? [])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '18', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(empty? [1])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('11', '19'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(empty? [1])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '10', '13'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(empty? [1])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '5', '10'), resolution doesn't close the loop)

### G4-15: first, rest, last

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first [10 20 30])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '5', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first [10 20 30])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '13', '18'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first [10 20 30])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '7', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(last [10 20 30])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '16', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(last [10 20 30])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '18', '16'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(last [10 20 30])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '9', '3'), resolution doesn't close the loop)

### G4-16: into and conj on collections

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '13', '20'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '18', '16'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '3', '19'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into #{} [1 2 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into #{} [1 2 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into #{} [1 2 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G4-17: Immutability — assoc returns new

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :a 99) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '7', '95'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :a 99) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '20', '18'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :a 99) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '9', '93'), resolution doesn't close the loop)

### G4-18: Equality of vectors and lists

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= [1 2 3] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '6', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= [1 2 3] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '7', '13'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= [1 2 3] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '3', '6'), resolution doesn't close the loop)

### G4-19: range and seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (range 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (range 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (range 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first (range 1 100))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '121'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first (range 1 100))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '366'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first (range 1 100))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '471'), resolution doesn't close the loop)

### G4-20: Collection vs sequence

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (seq [1 2 3]))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (seq [1 2 3]))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '5', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (seq [1 2 3]))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '16', '20'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(seq [])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '5', '10'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(seq [])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('19', '20', '14'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(seq [])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '13', '3'), resolution doesn't close the loop)

## Grade 5

### G5-01: if

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if true :a :b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':b', ':open'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if true :a :b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':soft', ':y'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if true :a :b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':north', ':high'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if false :a :b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':c', ':x'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if false :a :b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':c', ':gamma'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if false :a :b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':alpha', ':slow'), resolution doesn't close the loop)

### G5-02: if as expression

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (if true 10 20))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '10'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (if true 10 20))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '20'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 (if true 10 20))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '17', '7'), resolution doesn't close the loop)

### G5-03: when

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true :yes)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':north',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true :yes)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':first',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true :yes)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':cool',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when false :yes)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':north',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when false :yes)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':z',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when false :yes)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hard',), resolution doesn't close the loop)

### G5-04: cond

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '3', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '7', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '8', '6'), resolution doesn't close the loop)

### G5-05: cond — :else

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cond false :a false :b :else :c)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':gamma', ':west', ':else'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cond false :a false :b :else :c)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':beta', ':first', ':else'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cond false :a false :b :else :c)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':b', ':gamma', ':else'), resolution doesn't close the loop)

### G5-06: case

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(case 2 1 :one 2 :two 3 :three :default)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '6', ':c'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(case 2 1 :one 2 :two 3 :three :default)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '5', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(case 2 1 :one 2 :two 3 :three :default)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '6', ':soft'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(case 99 1 :one 2 :two :default)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('28', '3', '28'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(case 99 1 :one 2 :two :default)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('38', '8', '38'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(case 99 1 :one 2 :two :default)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('64', '64', '6'), resolution doesn't close the loop)

### G5-07: and / or as control flow

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(and 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(and 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '9', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(and 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(or nil false :found)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':right',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(or nil false :found)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':fast',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(or nil false :found)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':third',), resolution doesn't close the loop)

### G5-08: not

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not (> 1 2))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not (> 1 2))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not (> 1 2))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)

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
- issues: {'HIGH_LENGTH': 1, 'COLLECTION_LEAK': 1, 'STORY_RESOLUTION_NO_DRAWN': 5}
    - [HIGH_LENGTH] form=`(map inc [1 2 3])` — user_msg 213 words
    - [COLLECTION_LEAK] form=`(map inc [1 2 3])` — elements of expected [2, 3, 4] appear comma-separated in user_msg (collection answer leak)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map inc [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '7', '14'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map inc [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '18', '20'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map #(* % %) [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map #(* % %) [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)

### G5-11: filter

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(filter even? [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '8', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(filter even? [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '15', '20'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(filter even? [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '19', '20'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(filter pos? [-2 -1 0 1 2])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '5', '10'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(filter pos? [-2 -1 0 1 2])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '4', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(filter pos? [-2 -1 0 1 2])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '20', '14'), resolution doesn't close the loop)

### G5-12: reduce

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce + [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '18', '12'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce + [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '4', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce + [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '7', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce * [1 2 3 4 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '14', '17'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce * [1 2 3 4 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('19', '19', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce * [1 2 3 4 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '6', '5'), resolution doesn't close the loop)

### G5-13: reduce with init

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce + 100 [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('492', '15', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce + 100 [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('254', '12', '18'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce + 100 [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('604', '12', '15'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce + 0 [])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '14', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce + 0 [])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '17', '14'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce + 0 [])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', '18'), resolution doesn't close the loop)

### G5-14: apply

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CONCEPT_AS_VERB': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(apply + [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '3', '16'), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`(apply + [1 2 3 4])` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(apply + [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '7', '18'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(apply + [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '18', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(apply max [3 1 4 1 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('11', '19'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(apply max [3 1 4 1 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '10', '13'), resolution doesn't close the loop)

### G5-15: comp

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [CONCEPT_AS_VERB] form=`((comp inc inc) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`((comp inc inc) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((comp inc inc) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((comp inc inc) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((comp str inc) 9)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((comp str inc) 9)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)

### G5-16: partial

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CONCEPT_AS_VERB] form=`((partial + 10) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map (partial * 3) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '20', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map (partial * 3) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '10', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map (partial * 3) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '15', '18'), resolution doesn't close the loop)

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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(some even? [1 3 5 8 7])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '6', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(some even? [1 3 5 8 7])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '7', '13'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(some even? [1 3 5 8 7])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '3', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(some neg? [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '13', '10'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(some neg? [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '8', '12'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(some neg? [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '19'), resolution doesn't close the loop)

### G5-19: every?

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(every? pos? [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '3', '10'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(every? pos? [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '4', '11'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(every? pos? [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '14', '13'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(every? even? [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(every? even? [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '10'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(every? even? [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('19', '11', '12'), resolution doesn't close the loop)

### G5-20: take and drop

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(take 3 [10 20 30 40 50])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '17', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(take 3 [10 20 30 40 50])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '19', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(take 3 [10 20 30 40 50])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '16', '20'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(drop 2 [10 20 30 40 50])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '11', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(drop 2 [10 20 30 40 50])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '14', '19'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(drop 2 [10 20 30 40 50])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '3', '17'), resolution doesn't close the loop)

### G5-21: distinct and sort

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(distinct [1 1 2 3 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '14', '15'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(distinct [1 1 2 3 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '10', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(distinct [1 1 2 3 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '12', '15'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(sort [3 1 2])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '7', '18'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(sort [3 1 2])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '6', '13'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(sort [3 1 2])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '9', '8'), resolution doesn't close the loop)

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
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(name 'foo.bar)` — answer string 'foo.bar' appears in user_msg

### G6-03: require

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('cedar',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('cobalt',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('coral',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/lower-case "ZEBRA")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('cedar',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/lower-case "ZEBRA")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('thread',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/lower-case "ZEBRA")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('alder',), resolution doesn't close the loop)

### G6-04: refer and use

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= (clojure.string/upper-case "x") (clojure.string` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('ochre', 'ochre'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= (clojure.string/upper-case "x") (clojure.string` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('myrtle', 'myrtle'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= (clojure.string/upper-case "x") (clojure.string` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('topaz', 'topaz'), resolution doesn't close the loop)

### G6-05: Fully qualified names

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 12}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "hello")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('ember',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "hello")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('cedar',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "hello")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('cedar',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/reverse "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/reverse "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/reverse "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)

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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "a")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('candle',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "a")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('thread',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "a")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('cedar',), resolution doesn't close the loop)

### G6-09: Loading order

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 1 b (+ a 1)] (+ a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '5'), resolution doesn't close the loop)

### G6-13: Aliasing conventions

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [s clojure.string/upper-case] (s "hare"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('auburn',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [s clojure.string/upper-case] (s "hare"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('lichen',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [s clojure.string/upper-case] (s "hare"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('pebble',), resolution doesn't close the loop)

### G6-14: Import for host classes

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(symbol? 'java.util.List)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-15: Namespace meta

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [ANSWER_LEAK_STRING] form=`(:doc (meta '\{:doc "steady wins"\} race))` — answer string 'steady wins' appears in user_msg
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:author (meta '\{:author "Aesop"\} race))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':author', ':author', 'Aesop'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:author (meta '\{:author "Aesop"\} race))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':author', ':author', 'Aesop'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:author (meta '\{:author "Aesop"\} race))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':author', ':author', 'Aesop'), resolution doesn't close the loop)

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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (/ 1 0) (catch Exception e -1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '-61'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (/ 1 0) (catch Exception e -1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-23',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (/ 1 0) (catch Exception e -1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '8', '-13'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try 42 (catch Exception e :caught))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('88', ':west'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try 42 (catch Exception e :caught))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('39', ':north'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try 42 (catch Exception e :caught))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('33', ':third'), resolution doesn't close the loop)

### G7-03: try / finally

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try 7 (finally (prn :cleanup)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', ':cleanup'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try 7 (finally (prn :cleanup)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', ':cleanup'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try 7 (finally (prn :cleanup)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', ':cleanup'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (try (/ 1 0) (finally (prn :ran))) (catch Exc` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1', ':ran'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (try (/ 1 0) (finally (prn :ran))) (catch Exc` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1', ':ran'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (try (/ 1 0) (finally (prn :ran))) (catch Exc` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1', ':ran'), resolution doesn't close the loop)

### G7-04: ex-info

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', 'bad'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', 'bad'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', 'bad'), resolution doesn't close the loop)

### G7-05: nil punning

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(some? 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)

### G7-06: pre and post conditions

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', ':pre'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', ':pre'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', ':pre'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exce` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1', ':pre'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exce` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1', ':pre'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exce` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1', ':pre'), resolution doesn't close the loop)

### G7-07: assert

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '8', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '9'), resolution doesn't close the loop)

### G7-08: prn and pprint

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(with-out-str (prn 42))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(with-out-str (prn 42))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(with-out-str (prn 42))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(with-out-str (prn :hare))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(with-out-str (prn :hare))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(with-out-str (prn :hare))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare',), resolution doesn't close the loop)

### G7-09: tap>

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(tap> :hello)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hello',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(tap> :hello)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hello',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(tap> :hello)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hello',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(tap> 42)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(tap> 42)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(tap> 42)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)

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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'ANSWER_LEAK_STRING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)
    - [ANSWER_LEAK_STRING] form=`(try (throw (ex-info "trouble" {})) (catch Excepti` — answer string 'trouble' appears in user_msg
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "trouble" {})) (catch Excepti` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('trouble',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "trouble" {})) (catch Excepti` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('trouble',), resolution doesn't close the loop)

### G7-12: slurp and spit

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "hare
tortoise
")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('amber',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "hare
tortoise
")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('cedar',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "hare
tortoise
")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('ochre',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "a\nb\nc" #"\n")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc', '\\n'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "a\nb\nc" #"\n")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc', '\\n'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "a\nb\nc" #"\n")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc', '\\n'), resolution doesn't close the loop)

### G7-13: line-seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first (clojure.string/split-lines "first\nsecond"` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('first\\nsecond',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first (clojure.string/split-lines "first\nsecond"` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('first\\nsecond',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first (clojure.string/split-lines "first\nsecond"` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('first\\nsecond',), resolution doesn't close the loop)

### G7-14: with-open

- examples: 1
- variety @ n=50: 0.98
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(with-out-str (println "hare"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('hare',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(with-out-str (println "hare"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('hare',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(with-out-str (println "hare"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('hare',), resolution doesn't close the loop)

### G7-16: edn read

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "42")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', '42'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "42")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', '42'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "42")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', '42'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "{:a 1}")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', '{:a 1}'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "{:a 1}")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', '{:a 1}'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "{:a 1}")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', '{:a 1}'), resolution doesn't close the loop)

### G7-17: JSON roundtrip

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G7-18: Shell command

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:cmd {:cmd "ls" :args ["-l"]})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '16', ':north'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:cmd {:cmd "ls" :args ["-l"]})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '13', ':z'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:cmd {:cmd "ls" :args ["-l"]})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '9', ':cool'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (:args {:cmd "echo" :args ["hello" "world"]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('11', '14', ':north'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (:args {:cmd "echo" :args ["hello" "world"]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '7', ':west'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (:args {:cmd "echo" :args ["hello" "world"]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '11', ':beta'), resolution doesn't close the loop)

## Grade 8

### G8-01: Why polymorphism

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':tortoise', ':else'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':tortoise', ':else'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':tortoise', ':else'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [speak (fn [k] (cond (= k :hare) "swift" (= k` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':fox', ':otter', ':otter'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [speak (fn [k] (cond (= k :hare) "swift" (= k` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':weasel', ':toad', ':toad'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [speak (fn [k] (cond (= k :hare) "swift" (= k` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':tortoise', ':doe', ':doe'), resolution doesn't close the loop)

### G8-02: deftype introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Stone [weight]) (.-weight (Stone. 7))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Stone [weight]) (.-weight (Stone. 7))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(do (deftype Stone [weight]) (.-weight (Stone. 7))` — user_msg 202 words

### G8-03: defrecord introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [HIGH_LENGTH] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — user_msg 207 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':pace', ':slow', 'Alice'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':pace', ':slow', 'Alice'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':pace', ':slow', 'Alice'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defrecord Runner [name pace]) (:name (->Runne` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':name', ':moderate', 'Bob'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defrecord Runner [name pace]) (:name (->Runne` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':name', ':moderate', 'Bob'), resolution doesn't close the loop)

### G8-05: Protocol extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('swift', 'hare'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('swift', 'hare'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('swift', 'hare'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', ':number'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', ':number'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', ':number'), resolution doesn't close the loop)

### G8-06: Protocol method dispatch

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':string-pace', ':long-pace'), resolution doesn't close the loop)

### G8-07: Record implementing protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':swift', 'Pip'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':swift', 'Pip'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':swift', 'Pip'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord T` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':steady', 'Shelly'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord T` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':steady', 'Shelly'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord T` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':steady', 'Shelly'), resolution doesn't close the loop)

### G8-08: Multimethod defmulti

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [HIGH_LENGTH] form=`(do (defmulti pace :species) (defmethod pace :hare` — user_msg 209 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmulti tag :kind) (defmethod tag :stone [_]` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':kind', ':stone', ':hard'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmulti tag :kind) (defmethod tag :stone [_]` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':kind', ':stone', ':hard'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmulti tag :kind) (defmethod tag :stone [_]` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':kind', ':stone', ':hard'), resolution doesn't close the loop)

### G8-09: Multimethod defmethod

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmulti pace :species) (defmethod pace :hare` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':species', ':hare', ':swift'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmulti pace :species) (defmethod pace :hare` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':species', ':hare', ':swift'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmulti pace :species) (defmethod pace :hare` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':species', ':hare', ':swift'), resolution doesn't close the loop)

### G8-10: Multimethod vs protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [HIGH_LENGTH] form=`(do (defprotocol Show (show [this])) (extend-proto` — user_msg 203 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Show (show [this])) (extend-proto` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('str-', 'hare'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Show (show [this])) (extend-proto` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('str-', 'hare'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Show (show [this])) (extend-proto` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('str-', 'hare'), resolution doesn't close the loop)

### G8-11: Protocol vs Java interface

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol IPace (run [this])) (extend-proto` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':ran', 'hare'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol IPace (run [this])) (extend-proto` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':ran', 'hare'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol IPace (run [this])) (extend-proto` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':ran', 'hare'), resolution doesn't close the loop)

### G8-12: extend-type on built-in types

- examples: 2
- variety @ n=50: 0.99
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-type` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', ':number-pace'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-type` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', ':number-pace'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-type` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', ':number-pace'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-type` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':string-pace', 'hare'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-type` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':string-pace', 'hare'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-type` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':string-pace', 'hare'), resolution doesn't close the loop)

### G8-13: this-style vs fn-style

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Named (name-of [this])) (defrecor` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':n', 'Zephyr'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Named (name-of [this])) (defrecor` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':n', 'Zephyr'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Named (name-of [this])) (defrecor` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':n', 'Zephyr'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Tagged (tag-of [this])) (defrecor` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':t', ':grey'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Tagged (tag-of [this])) (defrecor` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':t', ':grey'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Tagged (tag-of [this])) (defrecor` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':t', ':grey'), resolution doesn't close the loop)

### G8-14: Protocols don't inherit

- examples: 1
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [HIGH_LENGTH] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg 220 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)

### G8-15: derive and isa? — multimethod hierarchy

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':runner', ':hare'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':runner', ':hare'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':runner', ':hare'), resolution doesn't close the loop)

### G8-16: Abstract design with protocols

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':leap', ':plod'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':leap', ':plod'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':leap', ':plod'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Sound (cry [this])) (defrecord Ha` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':thump', ':hiss'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Sound (cry [this])) (defrecord Ha` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':thump', ':hiss'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(do (defprotocol Sound (cry [this])) (defrecord Ha` — user_msg 206 words

## Grade 9

### G9-01: Immutability as default — review

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :b 2) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '6', ':kumquat'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :b 2) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '18', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :b 2) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '10', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [v [1 2 3]] (conj v 4) v)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '3', '18'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [v [1 2 3]] (conj v 4) v)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '12', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [v [1 2 3]] (conj v 4) v)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '9', '14'), resolution doesn't close the loop)

### G9-02: Why state at all

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def progress (atom :idle)) (reset! progress :` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':idle', ':running'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def progress (atom :idle)) (reset! progress :` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':idle', ':running'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(do (def progress (atom :idle)) (reset! progress :` — user_msg 204 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def progress (atom :idle)) (reset! progress :` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':idle', ':running'), resolution doesn't close the loop)

### G9-03: Atom introduction

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 10)) (swap! a + 5) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 10)) (swap! a + 5) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 10)) (swap! a + 5) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom :start)) (reset! a :done) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':start', ':done'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom :start)) (reset! a :done) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':start', ':done'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom :start)) (reset! a :done) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':start', ':done'), resolution doesn't close the loop)

### G9-04: Atom CAS semantics

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 5)) (compare-and-set! a 0 99) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '99'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 5)) (compare-and-set! a 0 99) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '99'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 5)) (compare-and-set! a 0 99) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '99'), resolution doesn't close the loop)

### G9-05: Watch on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':w',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':w',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':w',), resolution doesn't close the loop)

### G9-07: Ref introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('100', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('100', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('100', '7'), resolution doesn't close the loop)

### G9-08: dosync and alter

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [HIGH_LENGTH] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — user_msg 209 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '5'), resolution doesn't close the loop)

### G9-10: Agent introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ag (agent 5)) (send ag + 10) (await ag) @` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '10'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ag (agent 5)) (send ag + 10) (await ag) @` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '10'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ag (agent 5)) (send ag + 10) (await ag) @` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '10'), resolution doesn't close the loop)

### G9-13: future introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`@(future (* 6 7))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`@(future (* 6 7))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`@(future (* 6 7))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '7'), resolution doesn't close the loop)

### G9-14: deref @ shorthand

- examples: 2
- variety @ n=50: 0.99
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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def p (promise)) (deliver p :done) @p)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':done',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def p (promise)) (deliver p :done) @p)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':done',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def p (promise)) (deliver p :done) @p)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':done',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def p (promise)) (deliver p 42) @p)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def p (promise)) (deliver p 42) @p)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def p (promise)) (deliver p 42) @p)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)

### G9-16: volatile — when STM is too heavy

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def v (volatile! 5)) (vreset! v 99) @v)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '99'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def v (volatile! 5)) (vreset! v 99) @v)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '99'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(do (def v (volatile! 5)) (vreset! v 99) @v)` — user_msg 201 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def v (volatile! 5)) (vreset! v 99) @v)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '99'), resolution doesn't close the loop)

### G9-17: binding — thread-local

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — user_msg 208 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def lock (Object.)) (locking lock 42))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(do (def lock (Object.)) (locking lock 42))` — user_msg 202 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def lock (Object.)) (locking lock 42))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(do (def lock (Object.)) (locking lock 42))` — user_msg 208 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def lock (Object.)) (locking lock 42))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)

## Grade 10

### G10-01: quote, unquote, unquote-splice

- examples: 3
- variety @ n=50: 1.00
- issues: {'THE_FORM_OVERUSE': 3, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [THE_FORM_OVERUSE] form=`(quote (+ 1 2))` — `the form` appears 6 times in user_msg (template tic — vary references)
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '17', '14'), resolution doesn't close the loop)
    - [THE_FORM_OVERUSE] form=`'(1 2 3)` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '10', '19'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '6', '15'), resolution doesn't close the loop)
    - [THE_FORM_OVERUSE] form=`'(1 2 3)` — `the form` appears 5 times in user_msg (template tic — vary references)

### G10-02: syntax-quote

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'THE_FORM_OVERUSE': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 10] `(+ ~x ~x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10',), resolution doesn't close the loop)
    - [THE_FORM_OVERUSE] form=`(let [x 10] `(+ ~x ~x))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 10] `(+ ~x ~x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 10] `(+ ~x ~x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10',), resolution doesn't close the loop)
    - [THE_FORM_OVERUSE] form=`(let [x 10] `(+ ~x ~x))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [xs [1 2 3]] `(list ~@xs))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G10-03: defmacro introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [HIGH_LENGTH] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg 207 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)

### G10-04: Macro expansion rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(when true 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(when true 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(when true 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(or a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(or a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(or a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)

### G10-05: macroexpand

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(macroexpand '(-> 1 inc inc))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-06: when and when-not as macros

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 9}
    - [LOW_GROUNDING] form=`(when true 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(when true 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(when true 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CONCEPT_AS_VERB': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(-> 5 inc inc inc)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`(-> 5 inc inc inc)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(-> 5 inc inc inc)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(-> 5 inc inc inc)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '14', '10'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '12', '12'), resolution doesn't close the loop)

### G10-08: Macro vs fn

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)

### G10-09: Hygiene and gensym

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('x_', 'x_'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('x_', 'x_'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('x_', 'x_'), resolution doesn't close the loop)

### G10-10: Anaphoric macros are confusing

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if-let [x 7] (* x x) 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if-let [x 7] (* x x) 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if-let [x 7] (* x x) 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)

### G10-11: Reader macros overview

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9}
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '8', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '15', '20'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '19', '20'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(* % %) 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(* % %) 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(* % %) 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)

### G10-12: Tagged literals

- examples: 2
- variety @ n=50: 0.99
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inst? #inst "2024-01-01")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('2024', '-01', '-01'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inst? #inst "2024-01-01")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('2024', '-01', '-01'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inst? #inst "2024-01-01")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('2024', '-01', '-01'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(uuid? #uuid "00000000-0000-0000-0000-000000000000` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('00000000', '-0000', '-0000'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(uuid? #uuid "00000000-0000-0000-0000-000000000000` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('00000000', '-0000', '-0000'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(uuid? #uuid "00000000-0000-0000-0000-000000000000` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('00000000', '-0000', '-0000'), resolution doesn't close the loop)

### G10-13: Data readers and EDN extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "42")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', '42'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "42")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', '42'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "42")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', '42'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "[:a :b :c]")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b', ':c'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "[:a :b :c]")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b', ':c'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "[:a :b :c]")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b', ':c'), resolution doesn't close the loop)

### G10-14: eval (the function)

- examples: 2
- variety @ n=50: 0.99
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval '(+ 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(eval '(+ 1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval '(+ 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval '(+ 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval (list '+ 4 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval (list '+ 4 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '5'), resolution doesn't close the loop)

### G10-15: When not to write a macro

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "a function suffices when no syntax shaping is` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', 'raven'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "a function suffices when no syntax shaping is` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', 'cobalt'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "a function suffices when no syntax shaping is` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', 'myrtle'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "prefer fn unless you must shape syntax" (map ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3', '12'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do "prefer fn unless you must shape syntax" (map ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "prefer fn unless you must shape syntax" (map ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '7', '8'), resolution doesn't close the loop)

### G10-16: Macro pattern library

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':slow-and-steady'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':slow-and-steady'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':slow-and-steady'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':slow',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':slow',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — user_msg 210 words

## Grade 11

### G11-02: Method call syntax

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(.toUpperCase "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(.toUpperCase "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(.toUpperCase "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(. "abc" toUpperCase)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(. "abc" toUpperCase)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(. "abc" toUpperCase)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)

### G11-03: Static method call

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)

### G11-04: Field access

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('ochre',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('myrtle',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('topaz',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('myrrh',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('apple',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('lichen',), resolution doesn't close the loop)

### G11-06: new and dot-construct

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(String. "go")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(new String "jump")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(new String "jump")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-07: Arrays

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (int-array [1 2 3])] (alength a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (int-array [1 2 3])] (alength a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (int-array [1 2 3])] (alength a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G11-08: Type hints

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [^String s "abc"] (.toUpperCase s))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(let [^String s "abc"] (.toUpperCase s))` — user_msg 205 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [^String s "abc"] (.toUpperCase s))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [^String s "abc"] (.toUpperCase s))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do "type hints are metadata that guide compilatio` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-09: Checked vs unchecked math

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)

## Grade 12

### G12-01: Transducers introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(into [] (map inc) [1 2 3])` — user_msg 203 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (filter even?) [1 2 3 4 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (filter even?) [1 2 3 4 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', '5'), resolution doesn't close the loop)

### G12-02: Transducer composition

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', '5'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — user_msg 213 words

### G12-03: into with a transducer (xform)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 6}
    - [HIGH_LENGTH] form=`(into #{} (map inc) [1 2 3])` — user_msg 203 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into #{} (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into #{} (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into #{} (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (take 3) (range 100))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '100'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (take 3) (range 100))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '100'), resolution doesn't close the loop)

### G12-15: Datomic / XTDB (datalog db brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPEATED_OPENER_FRAGMENT': 1}
    - [REPEATED_OPENER_FRAGMENT] form=`(do "queries are written in datalog over EDN-shape` — opener fragment 'at the edge of the garden,' also appears later in user_msg

### G12-18: Clojure style guide

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPEATED_OPENER_FRAGMENT': 1}
    - [REPEATED_OPENER_FRAGMENT] form=`(do "prefer pure functions, name predicates with ?` — opener fragment 'at the edge of the meadow' also appears later in user_msg

---

## Summary

### Issue counts (across all examples × 3 records)

- **STORY_RESOLUTION_NO_DRAWN**: 831
- **CONCEPT_AS_VERB**: 25
- **HIGH_LENGTH**: 25
- **LOW_GROUNDING**: 23
- **REPL_AS_TIME_TRAVELLER**: 22
- **THE_FORM_OVERUSE**: 6
- **ANSWER_LEAK_STRING**: 4
- **ANSWER_LEAK**: 3
- **REPEATED_OPENER_FRAGMENT**: 3
- **SMALL_INT_LEAK**: 1
- **COLLECTION_LEAK**: 1

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 106 | — |
| 2 | 22 | 88 | 86 | — |
| 3 | 18 | 31 | 92 | — |
| 4 | 20 | 39 | 112 | — |
| 5 | 22 | 39 | 118 | — |
| 6 | 16 | 33 | 41 | — |
| 7 | 18 | 36 | 86 | — |
| 8 | 16 | 31 | 78 | — |
| 9 | 18 | 34 | 63 | — |
| 10 | 16 | 36 | 111 | — |
| 11 | 14 | 29 | 28 | — |
| 12 | 18 | 37 | 23 | — |

### Sample issues by severity

#### STORY_RESOLUTION_NO_DRAWN

- `G1-09` (form `(symbol? 42)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('73',), resolution doesn't close the loop)
    ```
    It is one thing to have fast legs and another to know how to use them, as the meadow folk would soon be reminded.

"There's a difference between *labeling* the form and
*evaluating* it," Rhizome the tortoise, stepping deliberately, said. "Quote in any of its
shapes is the labeling — the runtime hand...
    ```
- `G1-09` (form `(symbol? 42)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('51',), resolution doesn't close the loop)
    ```
    Two creatures of very different gait once agreed that the ground between two stones would settle a long argument.

Trundler the tortoise, with eyes always on the path, pointed at a name scratched into the bark
in the forest, then at an actual acorn lying on the path. "The mark on
the bark is the *na...
    ```
- `G1-09` (form `(symbol? 42)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('99',), resolution doesn't close the loop)
    ```
    The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the faster.

Oakheart the tortoise, with eyes always on the path, pointed at a name scratched into the bark
by the garden, then at an actual acorn lying on the path. "The mark on
the bark is the *name*; the...
    ```
- `G1-09` (form `(symbol? "tortoise")`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('river',), resolution doesn't close the loop)
    ```
    Anyone passing near the woods that morning would have seen Twitcher stretching for show while Stem simply began.

"There's a difference between *labeling* the form and
*evaluating* it," Stem the tortoise, without complaint, said. "Quote in any of its
shapes is the labeling — the runtime hands you ba...
    ```
- `G1-09` (form `(symbol? "tortoise")`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('cobalt',), resolution doesn't close the loop)
    ```
    There was once a Hare whose pride matched her feet in speed, and a Tortoise who said nothing about either.

"There's a difference between *labeling* the form and
*evaluating* it," Sloward the tortoise, with steady, careful steps, said. "Quote in any of its
shapes is the labeling — the runtime hands ...
    ```

#### SMALL_INT_LEAK

- `G1-12` (form `(+ 2 3)`): small-int answer 5 leaks via resolution-slot phrasing
    ```
    It happened atop the hilltop, on a morning when the air was kind to swift feet and steady ones alike.

Mossback the tortoise chalked a small expression on the path: the plus-mark, then 2, then 3, all wrapped in a single set of parens. Pip the hare paused — was the answer 6 (parens means multiply, su...
    ```

#### ANSWER_LEAK

- `G1-12` (form `(* (+ 1 2) 3)`): answer 9 in narrative
    ```
    It is one thing to have fast legs and another to know how to use them, as the meadow folk would soon be reminded.

Mossback chalked two nested fences on the path: an inner fence holding the plus-mark, 6, and 9, and an outer fence holding the star-mark, the inner fence, and 9. Pip counted the parens ...
    ```
- `G2-06` (form `(inc 5)`): answer 6 in narrative
    ```
    By the time the dew had lifted, the meadow had gathered to watch the strangest race anyone could remember.

Bramble the hare eyed the heap, boasting at every turn, and called out a guess
about how many acorns were there without bothering to count.
Sienna the tortoise simply began counting — to incre...
    ```
- `G2-19` (form `(+ 99999999999 1)`): answer 100000000000 in narrative
    ```
    near the garden, where the path bends past the elm, Heather the hare taunted Stoneback the tortoise one too many times.

Heather the hare eyed the heap, with great whoops of laughter, and called out a guess
about how many acorns were there without bothering to count.
Stoneback the tortoise simply be...
    ```

#### REPL_AS_TIME_TRAVELLER

- `G1-13` (form `(- 5 3)`): user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    ```
    A path ran from the old oak to the river stone, and on it many a boast had been measured against many a steady step.

Thyme the hare eyed the heap, with a smug grin, and called out a guess
about how many acorns were there without bothering to count.
Saunter the tortoise simply began counting — to su...
    ```
- `G1-13` (form `(+ 7 8)`): user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    ```
    Stoat the hare liked to talk; Branch the tortoise liked to listen, and the rivalry between them had grown into a small legend in the orchard.

Stoat the hare eyed the heap, boasting at every turn, and called out a guess
about how many acorns were there without bothering to count.
Branch the tortoise...
    ```
- `G1-14` (form `(+ (* 2 3) (* 4 5))`): user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    ```
    Some say it began with a yawn and a laugh; others say it began with a quiet refusal to be laughed at.

Lemming the hare eyed the heap, boasting at every turn, and called out a guess
about how many acorns were there without bothering to count.
Stoneback the tortoise simply began counting — to add the...
    ```
- `G1-16` (form `(zero? 5)`): user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    ```
    When Galop the hare declared the race already won, no one yet knew how long the afternoon would be.

Galop the hare eyed the heap, with a smug grin, and called out a guess
about how many acorns were there without bothering to count.
Whorl the tortoise simply began counting — to check whether 8 is ze...
    ```
- `G1-16` (form `(pos? -2)`): user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    ```
    By the time the dew had lifted, the meadow had gathered to watch the strangest race anyone could remember.

Wren the hare eyed the heap, as if the race were already won, and called out a guess
about how many acorns were there without bothering to count.
Cobblestone the tortoise simply began counting...
    ```

#### REPEATED_OPENER_FRAGMENT

- `G1-13` (form `(* 4 5)`): opener fragment 'at the edge of the hilltop,' also appears later in user_msg
    ```
    at the edge of the hilltop, a Hare and a Tortoise once made a wager that the meadow still talks about.

Knurl the tortoise, with steady, careful steps, laid acorns out on a flat stone at the edge of the hilltop, sorting
them into small heaps. "Numbers in Clojure are just like acorns in
heaps," he sa...
    ```
- `G12-15` (form `(do "queries are written in datalog over EDN-shaped data" :d`): opener fragment 'at the edge of the garden,' also appears later in user_msg
    ```
    at the edge of the garden, where the path bends past the elm, Jolt the hare taunted Cairn the tortoise one too many times.

At a moss-covered milestone at the edge of the garden, Jolt the hare sketched a small
wager into the path: whoever could produce a form whose evaluation
would learn how queries...
    ```
- `G12-18` (form `(do "prefer pure functions, name predicates with ?, danger! `): opener fragment 'at the edge of the meadow' also appears later in user_msg
    ```
    A quiet wager passed between Bouncekin and Linger, and at the edge of the meadow the meadow folk gathered to see it answered.

"There is no challenge here," Bouncekin the hare said, with great whoops of laughter.
"Anyone could learn the Clojure naming conventions: pure function preference, question-...
    ```

#### CONCEPT_AS_VERB

- `G1-15` (form `(= 1 2)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    The sun rose in the meadow, and with it the question of who could outrun whom.

"You can't tell which way the gate will swing by guessing,"
Knoll the tortoise, with steady, careful steps, said. "You bring the value to the gate, the
runtime checks it, and the gate gives the only answer that
matters."...
    ```
- `G1-15` (form `(= :hare :hare)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    It happened in a year when the wheat came in early and the children had time to lean against fences and watch.

"You can't tell which way the gate will swing by guessing,"
Tuber the tortoise, with eyes always on the path, said. "You bring the value to the gate, the
runtime checks it, and the gate gi...
    ```
- `G1-15` (form `(= :hare :hare)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    by the woods, a Hare and a Tortoise once made a wager that the meadow still talks about.

"You can't tell which way the gate will swing by guessing,"
Toddle the tortoise, with steady, careful steps, said. "You bring the value to the gate, the
runtime checks it, and the gate gives the only answer tha...
    ```
- `G2-13` (form `(or false true)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    It happened on the road, on a morning when the air was kind to swift feet and steady ones alike.

"You can't tell which way the gate will swing by guessing,"
Tussock the tortoise, stepping deliberately, said. "You bring the value to the gate, the
runtime checks it, and the gate gives the only answer...
    ```
- `G2-13` (form `(or false false)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    The sun rose along the road, and with it the question of who could outrun whom.

"You can't tell which way the gate will swing by guessing,"
Oakheart the tortoise, saying very little, said. "You bring the value to the gate, the
runtime checks it, and the gate gives the only answer that
matters." To ...
    ```

#### HIGH_LENGTH

- `G2-15` (form `(if 0 1 0)`): user_msg 205 words
    ```
    Anyone passing at the edge of the meadow that morning would have seen Tippet stretching for show while Heft simply began.

A wooden gate at the trail's fork had a verdict-stone carved with the number zero. Mossback the tortoise stood before it, confused — zero was nothing, yet the gate stood, not ab...
    ```
- `G3-03` (form `(let [x 3] (+ x 1))`): user_msg 232 words
    ```
    Galop announced the race in a voice loud enough to wake the owls, and Fen accepted with a nod.

Mossback the tortoise had been counting along a stretch of road. She set a single pebble — worth 7 acorns — into the small leather pouch tied at her hip and gave the pouch's contents the local name x.

Ju...
    ```
- `G3-05` (form `(do (def x 10) (let [x 99] x) x)`): user_msg 204 words
    ```
    By the time the dew had lifted, the meadow had gathered to watch the strangest race anyone could remember.

Mossback posted x at 13 on the road sign, then walked a detour where her hip-pouch shadowed x with 21. When she returned to the main road, the pouch was empty; only the road sign stood.

Back ...
    ```
- `G3-06` (form `(let [a 3 b (+ a 1) c (* b 2)] c)`): user_msg 224 words
    ```
    In that part of the woods, no one ever expected the slow to outpace the swift, yet the question was always quietly asked.

Mossback prepared three pouches in order: a held 2 acorns, then b was filled with one more than a, and finally c was loaded with twice whatever b held. Each pouch drew from the ...
    ```
- `G3-10` (form `(#(+ % 1) 5)`): user_msg 205 words
    ```
    Among the small kingdoms of the meadow, swiftness was a kind of currency, and one creature spent it loudly.

Mossback was in a hurry at the roadside and had no time to write a full recipe card. She scratched a quick shorthand mark — `#(+ % 1)` — on a stone and put 5 acorns in front of it immediately...
    ```

#### LOW_GROUNDING

- `G2-20` (form `(count [1 2 3])`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    It happened in a year when the wheat came in early and the children had time to lean against fences and watch.

Sandstone the tortoise walked the row of pebbles by the forest, one paw at a
time, a small slate in hand for the running tally. "Reduce is
this walk," she said: "at each pebble, you combin...
    ```
- `G2-20` (form `(count [])`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    A quiet wager passed between Leveret and Rhizome, and atop the hilltop the meadow folk gathered to see it answered.

Rhizome the tortoise walked the row of pebbles atop the hilltop, one paw at a
time, a small slate in hand for the running tally. "Reduce is
this walk," she said: "at each pebble, you ...
    ```
- `G2-20` (form `(count [])`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    A quiet wager passed between Furrling and Rhizome, and at the edge of the woods the meadow folk gathered to see it answered.

Rhizome the tortoise walked the row of pebbles by the woods, one paw at a
time, a small slate in hand for the running tally. "Reduce is
this walk," he said: "at each pebble, ...
    ```
- `G2-20` (form `(count [])`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    Bistre the tortoise had nothing to prove, but Heath the hare had everything to lose, and the race was on.

Bistre the tortoise walked the row of pebbles by the meadow, one paw at a
time, a small slate in hand for the running tally. "Reduce is
this walk," he said: "at each pebble, you combine
it into...
    ```
- `G3-05` (form `(do (def x 10) (let [x 99] x))`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    Long ago, when wagers were still settled by running rather than talking, two unlikely rivals agreed to a race.

Plod the tortoise patted the pouch at her hip.
"Whatever I tuck in here is in force only while the pouch is
worn," she said, "and only for the form that names
the binding. Step past the fo...
    ```

#### ANSWER_LEAK_STRING

- `G4-07` (form `(get {:a 1} :missing :default)`): answer string ':default' appears in user_msg
    ```
    Among the small kingdoms of the meadow, swiftness was a kind of currency, and one creature spent it loudly.

Mossback the tortoise's basket had one pouch — labeled :a. Pip the hare asked for the contents of a pouch labeled :missing, which had never been stitched into the basket at all.

Rather than ...
    ```
- `G6-01` (form `(name 'foo.bar)`): answer string 'foo.bar' appears in user_msg
    ```
    Some say it began with a yawn and a laugh; others say it began with a quiet refusal to be laughed at.

On the long road, there lay a library shelf holding scrolls. Each scroll had a name — foo.bar, tortoise.race — inscribed on its spine in the style of the land.

Mossback the tortoise needed to know...
    ```
- `G6-15` (form `(:doc (meta '\{:doc "steady wins"\} race))`): answer string 'steady wins' appears in user_msg
    ```
    Two creatures of very different gait once agreed that the ground between two stones would settle a long argument.

On a scroll lay a symbol race, marked with marginalia in the margin: ^{:doc "steady wins"}. The margin held a note — a docstring — explaining what the symbol was about.

Mossback wanted...
    ```
- `G7-11` (form `(try (throw (ex-info "trouble" {})) (catch Exception e (.get`): answer string 'trouble' appears in user_msg
    ```
    Among the small kingdoms of the meadow, swiftness was a kind of currency, and one creature spent it loudly.

Lichen the tortoise, with eyes always on the path, stretched a small net beneath a high jump
at the edge of the woods. "If the runner falls, the net catches them; the run
doesn't end, only th...
    ```

#### COLLECTION_LEAK

- `G5-10` (form `(map inc [1 2 3])`): elements of expected [2, 3, 4] appear comma-separated in user_msg (collection answer leak)
    ```
    Among the small kingdoms of the meadow, swiftness was a kind of currency, and one creature spent it loudly.

A row of three small acorns lay on a flat stone — the morning's first gathering, with counts of 1, 2, and 3.

Each acorn was missing a single bud at the cap. Mossback the tortoise wanted to a...
    ```

#### THE_FORM_OVERUSE

- `G10-01` (form `(quote (+ 1 2))`): `the form` appears 6 times in user_msg (template tic — vary references)
    ```
    Some say it began with a yawn and a laugh; others say it began with a quiet refusal to be laughed at.

Mossback the tortoise had chalked the form `(+ 1 2)` on a strip of bark and set it aside, wanting to hand the form itself to the Hare — not its computed value.

She needed a way to label the form s...
    ```
- `G10-01` (form `'(1 2 3)`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    Brisk the hare was certain she could not lose; Pillow the tortoise was certain of nothing except the next step.

"To talk about the form itself rather than evaluating it,"
Pillow the tortoise, saying very little, said, "you label the form with a chalk mark
in front. Quoting tells the runtime: don't ...
    ```
- `G10-01` (form `'(1 2 3)`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    Chipmunk the hare was certain he could not lose; Shale the tortoise was certain of nothing except the next step.

"To talk about the form itself rather than evaluating it,"
Shale the tortoise, with eyes always on the path, said, "you label the form with a chalk mark
in front. Quoting tells the runti...
    ```
- `G10-02` (form `(let [x 10] `(+ ~x ~x))`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    Spring had loosened the soil and the grasses had grown tall enough to brush a passing flank.

"To talk about the form itself rather than evaluating it,"
Sepia the tortoise, with eyes always on the path, said, "you label the form with a chalk mark
in front. Quoting tells the runtime: don't cook this,...
    ```
- `G10-02` (form `(let [x 10] `(+ ~x ~x))`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    It is one thing to have fast legs and another to know how to use them, as the meadow folk would soon be reminded.

"There's a difference between *labeling* the form and
*evaluating* it," Ravine the tortoise, stepping deliberately, said. "Quote in any of its
shapes is the labeling — the runtime hands...
    ```

