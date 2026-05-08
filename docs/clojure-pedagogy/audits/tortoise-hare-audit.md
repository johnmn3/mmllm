# tortoise-hare curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

### G1-01: Eval as substitution

- examples: 4
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 3}
    - [DOUBLE_NAME_INTRO] form=`0` — character 'Ivy the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [DOUBLE_NAME_INTRO] form=`"hello"` — character 'Bunny the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [DOUBLE_NAME_INTRO] form=`nil` — character 'Ivy the hare' introduced twice within 200 chars — drop the second 'the hare'

### G1-02: Integer numbers

- examples: 6
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 4, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [DOUBLE_NAME_INTRO] form=`7` — character 'Giggle the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [DOUBLE_NAME_INTRO] form=`-25` — character 'Filbert the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [DOUBLE_NAME_INTRO] form=`-25` — character 'Hasty the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [DOUBLE_NAME_INTRO] form=`12345` — character 'Ferret the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`12345` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-03: Ratios

- examples: 5
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(* 2 1/2)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-04: Strings

- examples: 5
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [DOUBLE_NAME_INTRO] form=`"hello"` — character 'Fleeting the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`"42"` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-05: Booleans

- examples: 6
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2, 'DOUBLE_NAME_INTRO': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`true` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`true` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [DOUBLE_NAME_INTRO] form=`(< 3 5)` — character 'Moor the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [DOUBLE_NAME_INTRO] form=`(< 3 5)` — character 'Marigold the hare' introduced twice within 200 chars — drop the second 'the hare'

### G1-06: nil

- examples: 5
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 2, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [DOUBLE_NAME_INTRO] form=`nil` — character 'Skim the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(nil? nil)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [DOUBLE_NAME_INTRO] form=`(nil? false)` — character 'Dappling the hare' introduced twice within 200 chars — drop the second 'the hare'

### G1-07: Keywords

- examples: 5
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`:hare` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`:tortoise` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [DOUBLE_NAME_INTRO] form=`:tortoise` — character 'Finch the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`:winner` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-08: Characters

- examples: 4
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 4, 'STRING_AS_CHAR_MISCLAIM': 6, 'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [DOUBLE_NAME_INTRO] form=`\h` — character 'Stoneheart the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [STRING_AS_CHAR_MISCLAIM] form=`\space` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    - [STRING_AS_CHAR_MISCLAIM] form=`\space` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`\space` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [STRING_AS_CHAR_MISCLAIM] form=`\space` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    - [DOUBLE_NAME_INTRO] form=`\space` — character 'Chitter the hare' introduced twice within 200 chars — drop the second 'the hare'

### G1-09: Symbols vs values

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(symbol? "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('river',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(symbol? "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('cobalt',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(symbol? "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('coral',), resolution doesn't close the loop)

### G1-10: Comments

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2) ; sum of one and two` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2) ; sum of one and two` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(+ 1 2) ; sum of one and two` — sentence with 5 commas reads as AI-output cadence: 'To add 3 and 2, with a single-semicolon trailing comment, she, with steady, care'
    - [STORY_RESOLUTION_NO_DRAWN] form=`42 ;; the answer` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('32',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`42 ;; the answer` — character 'Bulk the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [STORY_RESOLUTION_NO_DRAWN] form=`42 ;; the answer` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('80',), resolution doesn't close the loop)

### G1-11: Whitespace doesn't matter

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+    1    2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+    1    2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+    1    2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(+    1    2)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+
  1
  2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+
  1
  2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '8'), resolution doesn't close the loop)

### G1-12: Parens group; they don't multiply

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5, 'CLAUSE_STACK_OVERFLOW': 3, 'SMALL_INT_LEAK': 1, 'ANSWER_LEAK': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '7'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(+ 2 3)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'
    - [SMALL_INT_LEAK] form=`(+ 2 3)` — small-int answer 5 leaks via resolution-slot phrasing
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* (+ 1 2) 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '8'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(* (+ 1 2) 3)` — sentence with 5 commas reads as AI-output cadence: 'Mossback chalked two nested fences on the path: an inner fence holding the plus-'

### G1-13: First arithmetic call

- examples: 6
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 17, 'PARAGRAPH_FRAGMENTATION': 3, 'DOUBLE_NAME_INTRO': 5, 'REPL_AS_TIME_TRAVELLER': 2, 'REPEATED_OPENER_FRAGMENT': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '7'), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(+ 1 2)` — user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '6'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(+ 1 2)` — character 'Bedrock the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(- 5 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)

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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 16, 'CLAUSE_STACK_OVERFLOW': 6, 'CONCEPT_AS_VERB': 3, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= 1 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '5'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(= 1 1)` — sentence with 5 commas reads as AI-output cadence: 'The gate\'s hinge is tight,\nthe rule is fixed." To test whether 1 equals 1 with ='
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= 1 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '9'), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`(= 1 2)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3'), resolution doesn't close the loop)

### G1-16: Numeric predicates

- examples: 6
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 15, 'DOUBLE_NAME_INTRO': 3, 'REPL_AS_TIME_TRAVELLER': 4}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(zero? 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(zero? 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(zero? 0)` — character 'Sorrel the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [REPL_AS_TIME_TRAVELLER] form=`(zero? 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(zero? 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(zero? 5)` — character 'Galop the hare' introduced twice within 200 chars — drop the second 'the hare'

### G1-17: Printing vs returning

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`42` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('52',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`42` — character 'Mallow the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [STORY_RESOLUTION_NO_DRAWN] form=`42` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('87',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`42` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('43',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`42` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '9'), resolution doesn't close the loop)

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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_NAME_INTRO': 1, 'REPL_AS_TIME_TRAVELLER': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1 2 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '9', '7'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(* 2 3 4)` — sentence with 5 commas reads as AI-output cadence: 'To multiply 5, 0, and 7, she, untroubled by what others thought, composed the mu'
    - [DOUBLE_NAME_INTRO] form=`(+ 1 2 3 4 5 6 7 8 9 10)` — character 'Root the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [REPL_AS_TIME_TRAVELLER] form=`(* 1 2 3 4 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

### G2-02: Comparison chains

- examples: 5
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 3, 'REPL_AS_TIME_TRAVELLER': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(< 1 2 3)` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(< 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '4'), resolution doesn't close the loop)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(< 1 2 3)` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(< 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(< 1 2 3)` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(< 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '8', '3'), resolution doesn't close the loop)

### G2-03: not= and = with multiple args

- examples: 5
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'REPL_AS_TIME_TRAVELLER': 2, 'DOUBLE_NAME_INTRO': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(= 1 1 1)` — sentence with 5 commas reads as AI-output cadence: 'To test whether 1, 1, and 1 are all equal, he, saying very little, composed the '
    - [CLAUSE_STACK_OVERFLOW] form=`(= 1 1 1)` — sentence with 6 commas reads as AI-output cadence: 'To test whether 1, 1, and 1 are all equal, she, with steady, careful steps, comp'
    - [REPL_AS_TIME_TRAVELLER] form=`(= 1 1 2)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [DOUBLE_NAME_INTRO] form=`(= 1 1 2)` — character 'Fleetpaw the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [REPL_AS_TIME_TRAVELLER] form=`(= 1 1 2)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

### G2-04: min and max

- examples: 5
- variety @ n=50: 1.00
- issues: {'REPL_AS_TIME_TRAVELLER': 4, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 4}
    - [REPL_AS_TIME_TRAVELLER] form=`(min 1 2 3)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(min 1 2 3)` — parametric example has hard-coded English numeral 'three heaps' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(min 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '3', '3'), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(min 1 2 3)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(min 1 2 3)` — parametric example has hard-coded English numeral 'three heaps' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(min 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '3'), resolution doesn't close the loop)

### G2-05: quot, rem, mod

- examples: 6
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'REPL_AS_TIME_TRAVELLER': 1, 'DOUBLE_NAME_INTRO': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(quot 17 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '17'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(quot 17 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('11', '-15'), resolution doesn't close the loop)
    - [REPL_AS_TIME_TRAVELLER] form=`(quot 17 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [STORY_RESOLUTION_NO_DRAWN] form=`(quot 17 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-4',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(rem 17 5)` — character 'Sageback the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [DOUBLE_NAME_INTRO] form=`(rem 100 7)` — character 'Fen the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'

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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 3, 'REPL_AS_TIME_TRAVELLER': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1/2 1/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(+ 1/2 1/4)` — character 'Stoneheart the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1/2 1/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1/2 1/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(* 2/3 3/4)` — character 'Hushwise the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [DOUBLE_NAME_INTRO] form=`(- 1 1/3)` — character 'Bide the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'

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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 1, 'DOUBLE_NAME_INTRO': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 2 2 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3', '3'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(* 3 3 3 3)` — character 'Sienna the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [DOUBLE_NAME_INTRO] form=`(* 3 3 3 3)` — character 'Mossfoot the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'

### G2-11: String concatenation with str

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 4, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(str "ab" "cd")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('saffron', 'indigo'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(str "ab" "cd")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('saffron', 'ochre'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(str "ab" "cd")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('auburn', 'cobalt'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(str 42)` — sentence with 5 commas reads as AI-output cadence: 'Concat strings together,\nand the threads are spliced; cut a substring out, and y'
    - [DOUBLE_NAME_INTRO] form=`(str "p" "q" "r")` — character 'Racer the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [CLAUSE_STACK_OVERFLOW] form=`(str 1 "+" 2 "=" 3)` — sentence with 9 commas reads as AI-output cadence: 'Concat strings together,\nand the threads are spliced; cut a substring out, and y'

### G2-12: print and println — return values

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`(println "hello")` — character 'Pebblepaw the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'

### G2-13: and / or — short circuit, return values

- examples: 6
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4, 'CONCEPT_AS_VERB': 5, 'DOUBLE_NAME_INTRO': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(or false true)` — sentence with 5 commas reads as AI-output cadence: 'The gate\'s hinge is tight,\nthe rule is fixed." To test false or true with the or'
    - [CONCEPT_AS_VERB] form=`(or false true)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(or false false)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CLAUSE_STACK_OVERFLOW] form=`(or false false)` — sentence with 5 commas reads as AI-output cadence: 'The gate\'s hinge is tight,\nthe rule is fixed." To test false or false with the o'
    - [CONCEPT_AS_VERB] form=`(and 1 2 3)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [DOUBLE_NAME_INTRO] form=`(and 1 2 3)` — character 'Hazel the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'

### G2-14: not — turning truthy to false

- examples: 5
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 2, 'CONCEPT_AS_VERB': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [DOUBLE_NAME_INTRO] form=`(not nil)` — character 'Briar the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [CONCEPT_AS_VERB] form=`(not 0)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [DOUBLE_NAME_INTRO] form=`(not 0)` — character 'Slatekin the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [CLAUSE_STACK_OVERFLOW] form=`(not "")` — sentence with 5 commas reads as AI-output cadence: 'The gate\'s hinge is tight,\nthe rule is fixed." To negate the empty string, he co'
    - [CONCEPT_AS_VERB] form=`(not "")` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G2-15: Falsey values: only false and nil

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 3, 'HIGH_LENGTH': 1, 'CONCEPT_AS_VERB': 1, 'DOUBLE_NAME_INTRO': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if 0 1 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '5'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(if 0 1 0)` — sentence with 5 commas reads as AI-output cadence: 'The gate\'s hinge is tight,\nthe rule is fixed." To use if to return 2 when the co'
    - [HIGH_LENGTH] form=`(if 0 1 0)` — user_msg 205 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if 0 1 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if 0 1 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`(if "" 1 0)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G2-16: Truthy 0 and empty string

- examples: 4
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 4, 'STORY_RESOLUTION_NO_DRAWN': 2, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_NAME_INTRO': 2}
    - [CONCEPT_AS_VERB] form=`(boolean 0)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(boolean 0)` — sentence with 5 commas reads as AI-output cadence: 'The gate\'s hinge is tight,\nthe rule is fixed." To convert 1 to a boolean, she co'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(boolean "")` — character 'Galop the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [CONCEPT_AS_VERB] form=`(boolean "")` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G2-17: Keyword as function for map lookup

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:hare {:hare 1 :tortoise 2})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '7', ':doe'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(:hare {:hare 1 :tortoise 2})` — character 'Heft the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:hare {:hare 1 :tortoise 2})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '18', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:hare {:hare 1 :tortoise 2})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '20', ':vole'), resolution doesn't close the loop)

### G2-18: Quoting symbols

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 5}
    - [CLAUSE_STACK_OVERFLOW] form=`(symbol? (quote hare))` — sentence with 5 commas reads as AI-output cadence: 'To ask whether long-form quoting of the name hare produces a symbol, using symbo'
    - [CLAUSE_STACK_OVERFLOW] form=`(= (quote tortoise) 'tortoise)` — sentence with 5 commas reads as AI-output cadence: 'To compare the result of long-form quoting of tortoise against the apostrophe-sh'
    - [CLAUSE_STACK_OVERFLOW] form=`(count '(1 2 3))` — sentence with 5 commas reads as AI-output cadence: 'To count the elements in a quoted list of the integers 1, 2, and 3, she, without'
    - [CLAUSE_STACK_OVERFLOW] form=`(count '(1 2 3))` — sentence with 5 commas reads as AI-output cadence: 'They are not\nthe same thing — and Clojure lets you talk about either one."\nTo co'
    - [CLAUSE_STACK_OVERFLOW] form=`(count '(1 2 3))` — sentence with 5 commas reads as AI-output cadence: 'To count the elements in a quoted list of the integers 1, 2, and 3, she, with ey'

### G2-19: Auto-promotion to bigint

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'ANSWER_LEAK': 1, 'REPL_AS_TIME_TRAVELLER': 2, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 1000000 1000000)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('1048576', '1048576'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 1000000 1000000)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10000000', '10000000'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 1000000 1000000)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('2147483647', '2147483647'), resolution doesn't close the loop)
    - [ANSWER_LEAK] form=`(+ 99999999999 1)` — answer 100000000000 in narrative
    - [REPL_AS_TIME_TRAVELLER] form=`(+ 99999999999 1)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [DOUBLE_NAME_INTRO] form=`(+ 99999999999 1)` — character 'Heather the hare' introduced twice within 200 chars — drop the second 'the hare'

### G2-20: Counting

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 2, 'CLAUSE_STACK_OVERFLOW': 1, 'LOW_GROUNDING': 4}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '7'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(count [1 2 3])` — character 'Tor the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3])` — sentence with 9 commas reads as AI-output cadence: 'The runtime does this for any\ncollection — vector, list, map, string." To count '
    - [LOW_GROUNDING] form=`(count [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '5', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '16', '20'), resolution doesn't close the loop)

### G2-21: String length and substring

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 2, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('alder',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(count "tortoise")` — sentence with 5 commas reads as AI-output cadence: 'Concat strings together,\nand the threads are spliced; cut a substring out, and y'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('pewter',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "tortoise")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('auburn',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(count "hare")` — character 'Whorl the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [CLAUSE_STACK_OVERFLOW] form=`(count (subs "tortoise" 0 3))` — sentence with 5 commas reads as AI-output cadence: 'Cut from one\nposition to another and you get a smaller thread, the original\nunto'

### G2-22: Compose pure arithmetic (multi-step calculation)

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_NAME_INTRO': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(+ (* 3 8) (* 2 4))` — sentence with 5 commas reads as AI-output cadence: 'To compute the product of 1 and 1, add the product of 3 and 4, he, with steady, '
    - [DOUBLE_NAME_INTRO] form=`(+ (* 3 8) (* 2 4))` — character 'Burden the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'

## Grade 3

### G3-01: def — top-level binding

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 42) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('28',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 42) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('38',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 42) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('84',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (def y 7) y)` — character 'Cobblestone the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'

### G3-02: def — redefinition

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 1) (def x 99) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('78',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 1) (def x 99) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('36',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 1) (def x 99) x)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '86'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def x 1) (def x 99) x)` — sentence with 5 commas reads as AI-output cadence: 'To bind x to 7, then redefine it as 86 and return it, the\nsign had to be read ex'

### G3-03: let — local binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'STORY_RESOLUTION_NO_DRAWN': 2}
    - [HIGH_LENGTH] form=`(let [x 3] (+ x 1))` — user_msg 232 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [x 3] (+ x 1))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 5] a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 5] a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)

### G3-04: let — multi-binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'CLAUSE_STACK_OVERFLOW': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 1 b 2] (+ a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 1 b 2] (+ a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 1 b 2] (+ a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 5 y 3] (- x y))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 5 y 3] (- x y))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 5 y 3] (- x y))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)

### G3-05: let — shadowing outer def

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 3, 'HIGH_LENGTH': 1}
    - [LOW_GROUNDING] form=`(do (def x 10) (let [x 99] x))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 10) (let [x 99] x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '93'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (def x 10) (let [x 99] x))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 10) (let [x 99] x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('11', '31'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def x 10) (let [x 99] x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('54',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (def x 10) (let [x 99] x) x)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G3-06: let — binding can reference prior

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 5, 'CLAUSE_STACK_OVERFLOW': 2, 'HIGH_LENGTH': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 5 b (* a 2)] b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 5 b (* a 2)] b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '6', '7'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — sentence with 6 commas reads as AI-output cadence: 'Step past the form\'s edge and the pouch is empty\nagain." To bind a to 7, b to a+'
    - [HIGH_LENGTH] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — user_msg 224 words

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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [a b c] (+ a b c)) 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`((fn [a b c] (+ a b c)) 1 2 3)` — character 'Whiskling the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [CLAUSE_STACK_OVERFLOW] form=`((fn [a b c] (+ a b c)) 1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'To\ncreate an anonymous function with three parameters that adds them and apply i'
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [a b c] (+ a b c)) 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`((fn [a b c] (+ a b c)) 1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'To create an anonymous function with three parameters that adds them and apply i'
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [a b c] (+ a b c)) 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G3-09: defn — shorthand

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CONCEPT_AS_VERB] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3', '7'), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3', '5'), resolution doesn't close the loop)

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CONCEPT_AS_VERB': 2, 'DOUBLE_NAME_INTRO': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [HIGH_LENGTH] form=`(#(+ % 1) 5)` — user_msg 205 words
    - [CONCEPT_AS_VERB] form=`(#(+ % 1) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(#(+ % 1) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [DOUBLE_NAME_INTRO] form=`(#(+ % 1) 5)` — character 'Steadypaw the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def g 5) (let [g 99] (+ g 1)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '84', '8'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def g 5) (let [g 99] (+ g 1)))` — sentence with 6 commas reads as AI-output cadence: 'To define g at the top level, shadow it in a let with a different value, and com'
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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '5', '8'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do 1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (+ 1 1) (+ 2 2) (+ 3 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '4', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (+ 1 1) (+ 2 2) (+ 3 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '7', '3'), resolution doesn't close the loop)

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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 1, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [+ 99] +)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('88',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(let [+ 99] +)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [+ 99] +)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('29',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [+ 99] +)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('33',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(let [+ 99] +)` — character 'Sorrel the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'

### G3-17: Naming conventions (kebab-case)

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 2, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [hare-speed 4 tortoise-speed 1] (- hare-speed` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(let [hare-speed 4 tortoise-speed 1] (- hare-speed` — character 'Heft the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 2, 'CLAUSE_STACK_OVERFLOW': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`[1 2 3]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`[1 2 3]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '14', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`[1 2 3]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('19', '15', '12'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`[1 2 3]` — character 'Quick the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [CLAUSE_STACK_OVERFLOW] form=`[1 2 3]` — sentence with 5 commas reads as AI-output cadence: 'To create a vector containing 1, 2, and 3 properly,\nhe wrote a vector of three n'
    - [STORY_RESOLUTION_NO_DRAWN] form=`[]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '18', '19'), resolution doesn't close the loop)

### G4-02: nth — vector access

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 0)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(nth [10 20 30] 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '10', '15'), resolution doesn't close the loop)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 0)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(nth [10 20 30] 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '13', '13'), resolution doesn't close the loop)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 0)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(nth [10 20 30] 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '14'), resolution doesn't close the loop)

### G4-03: conj — append to vector

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(conj [1 2] 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '6', '17'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(conj [1 2] 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '12', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(conj [1 2] 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '13', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(conj [] :hare)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '8', '19'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(conj [] :hare)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '14', '6'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(conj [] :hare)` — character 'Quickfoot the hare' introduced twice within 200 chars — drop the second 'the hare'

### G4-04: List literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '7', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '7', '10'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`'(1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'To create a list containing 1, 2, and 3, she, untroubled by what others thought,'
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '6', '8'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`'(1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'To create a list containing 1, 2, and 3, he, saying very little, composed a list'
    - [STORY_RESOLUTION_NO_DRAWN] form=`'()` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '18', '15'), resolution doesn't close the loop)

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
- issues: {'DOUBLE_NAME_INTRO': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [DOUBLE_NAME_INTRO] form=`(assoc {:a 1} :b 2)` — character 'Whiskling the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(assoc {:a 1} :a 99)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '95', ':strawberry'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(assoc {:a 1} :a 99)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '9', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(assoc {:a 1} :a 99)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '4', '98'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(assoc {:a 1} :a 99)` — character 'Marmot the hare' introduced twice within 200 chars — drop the second 'the hare'

### G4-09: dissoc — map remove key

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(dissoc {:a 1 :b 2} :a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '10', ':plum'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(dissoc {:a 1 :b 2} :a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '11', ':lime'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(dissoc {:a 1 :b 2} :a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '6', ':kiwi'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(dissoc {:a 1 :b 2} :a)` — character 'Marsh the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'

### G4-10: keys and vals

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (keys {:a 1 :b 2 :c 3}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '7', ':tangerine'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(count (keys {:a 1 :b 2 :c 3}))` — sentence with 5 commas reads as AI-output cadence: 'To count how many keys are in a map binding :a, :b, and :c, she, saying very lit'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (keys {:a 1 :b 2 :c 3}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '3', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (keys {:a 1 :b 2 :c 3}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '9', ':guava'), resolution doesn't close the loop)

### G4-11: Set literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count #{1 2 3})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '8', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count #{1 2 3})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '15', '20'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count #{1 2 3})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '19', '20'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(count #{1 1 1})` — character 'Calmway the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'

### G4-12: Set membership

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(contains? #{1 2 3} 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '18', '12'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(contains? #{1 2 3} 2)` — sentence with 5 commas reads as AI-output cadence: 'To check whether 2 is a member of a set containing 1, 2, and 3 properly,\nshe wro'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(contains? #{1 2 3} 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '7', '14'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(contains? #{1 2 3} 2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '10', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(contains? #{1 2 3} 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '9', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(contains? #{1 2 3} 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '8', '10'), resolution doesn't close the loop)

### G4-13: count — universal

- examples: 4
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'STORY_RESOLUTION_NO_DRAWN': 12, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_NAME_INTRO': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count [1 2 3 4 5])` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3 4 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '15', '15'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3 4 5])` — sentence with 8 commas reads as AI-output cadence: 'To count the elements in a vector containing 1, 2, 3, 4, and 5, he, with steady,'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count [1 2 3 4 5])` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count [1 2 3 4 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '14', '6'), resolution doesn't close the loop)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count [1 2 3 4 5])` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count

### G4-14: empty?

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'PARAGRAPH_FRAGMENTATION': 1, 'DOUBLE_NAME_INTRO': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(empty? [])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '3', '16'), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(empty? [])` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [STORY_RESOLUTION_NO_DRAWN] form=`(empty? [])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '7', '18'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(empty? [])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '18', '8'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(empty? [1])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('11', '19'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(empty? [1])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '10', '13'), resolution doesn't close the loop)

### G4-15: first, rest, last

- examples: 3
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 9, 'STORY_RESOLUTION_NO_DRAWN': 9, 'CLAUSE_STACK_OVERFLOW': 4}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(first [10 20 30])` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first [10 20 30])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '5', '4'), resolution doesn't close the loop)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(first [10 20 30])` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first [10 20 30])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '13', '18'), resolution doesn't close the loop)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(first [10 20 30])` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first [10 20 30])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '7', '7'), resolution doesn't close the loop)

### G4-16: into and conj on collections

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('15', '13', '20'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '18', '16'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '3', '19'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] '(1 2 3))` — sentence with 6 commas reads as AI-output cadence: 'Firm the tortoise shook\nher head and went on with the work: to\nconvert a list co'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into #{} [1 2 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into #{} [1 2 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G4-17: Immutability — assoc returns new

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :a 99) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '7', '95'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(let [m {:a 1}] (assoc m :a 99) m)` — character 'Heft the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :a 99) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '20', '18'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :a 99) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '9', '93'), resolution doesn't close the loop)

### G4-18: Equality of vectors and lists

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= [1 2 3] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '6', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= [1 2 3] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '7', '13'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= [1 2 3] '(1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '3', '6'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(= [1 2 3] '(1 2 3))` — sentence with 5 commas reads as AI-output cadence: 'To test whether a vector with elements 1, 2, 3 equals a list with the same eleme'

### G4-19: range and seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (range 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (range 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (range 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first (range 1 100))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '121'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first (range 1 100))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '366'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(first (range 1 100))` — character 'Stoneback the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'

### G4-20: Collection vs sequence

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (seq [1 2 3]))` — parametric example has hard-coded English numeral 'three elements' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (seq [1 2 3]))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '7'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(count (seq [1 2 3]))` — character 'Tuftkin the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [CLAUSE_STACK_OVERFLOW] form=`(count (seq [1 2 3]))` — sentence with 5 commas reads as AI-output cadence: 'To convert a vector containing 1, 2, and 3 to a sequence and count its elements '
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (seq [1 2 3]))` — parametric example has hard-coded English numeral 'three elements' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (seq [1 2 3]))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '5', '5'), resolution doesn't close the loop)

## Grade 5

### G5-01: if

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'CLAUSE_STACK_OVERFLOW': 3, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if true :a :b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':b', ':open'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(if true :a :b)` — sentence with 5 commas reads as AI-output cadence: 'The\ntrail is long and effort is precious — the runtime checks the\ncondition, wal'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if true :a :b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':soft', ':y'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if true :a :b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':north', ':high'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if false :a :b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':c', ':x'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if false :a :b)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':c', ':gamma'), resolution doesn't close the loop)

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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true :yes)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':north',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true :yes)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':first',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true :yes)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':cool',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(when true :yes)` — sentence with 5 commas reads as AI-output cadence: 'The\ntrail is long and effort is precious — the runtime checks the\ncondition, wal'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when false :yes)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':north',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when false :yes)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':z',), resolution doesn't close the loop)

### G5-04: cond

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '3', '6'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '7', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '8', '6'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — sentence with 5 commas reads as AI-output cadence: 'The trail is the trail; whatever\nthe condition evaluates to, that decides which '

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
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_NAME_INTRO': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(case 99 1 :one 2 :two :default)` — sentence with 5 commas reads as AI-output cadence: 'The\ntrail is long and effort is precious — the runtime checks the\ncondition, wal'
    - [DOUBLE_NAME_INTRO] form=`(case 99 1 :one 2 :two :default)` — character 'Tarry the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'

### G5-07: and / or as control flow

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(and 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(and 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '9', '9'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(and 1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'The gate\'s hinge is tight,\nthe rule is fixed." To return the last value when all'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(and 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '8'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(or nil false :found)` — character 'Bunneh the hare' introduced twice within 200 chars — drop the second 'the hare'

### G5-08: not

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not (> 1 2))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(not (> 1 2))` — character 'Stoneheart the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(not (> 1 2))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '3'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(not (> 1 2))` — character 'Sageback the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [CLAUSE_STACK_OVERFLOW] form=`(not (> 1 2))` — sentence with 5 commas reads as AI-output cadence: 'The gate\'s hinge is tight,\nthe rule is fixed." To negate the result of checking '
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
- issues: {'HIGH_LENGTH': 1, 'COLLECTION_LEAK': 1, 'STORY_RESOLUTION_NO_DRAWN': 5, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_NAME_INTRO': 1}
    - [HIGH_LENGTH] form=`(map inc [1 2 3])` — user_msg 213 words
    - [COLLECTION_LEAK] form=`(map inc [1 2 3])` — elements of expected [2, 3, 4] appear comma-separated in user_msg (collection answer leak)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map inc [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '7', '14'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(map inc [1 2 3])` — sentence with 8 commas reads as AI-output cadence: 'To pour the vector containing 1, 2, 3 through a sieve whose rule is inc, collect'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map inc [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '18', '20'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map #(* % %) [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)

### G5-11: filter

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(filter even? [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '8', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(filter even? [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '15', '20'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(filter even? [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '19', '20'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(filter pos? [-2 -1 0 1 2])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '5', '10'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(filter pos? [-2 -1 0 1 2])` — character 'Heath the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(filter pos? [-2 -1 0 1 2])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '4', '5'), resolution doesn't close the loop)

### G5-12: reduce

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'CLAUSE_STACK_OVERFLOW': 8, 'DOUBLE_NAME_INTRO': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce + [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('16', '18', '12'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + [1 2 3 4])` — sentence with 6 commas reads as AI-output cadence: 'To walk the row of pebbles 1, 2, 3, 4 carrying a tally that combines each with +'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce + [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '4', '8'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + [1 2 3 4])` — sentence with 10 commas reads as AI-output cadence: 'The runtime does this for any\ncollection — vector, list, map, string." To walk t'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce + [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '7', '6'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + [1 2 3 4])` — sentence with 6 commas reads as AI-output cadence: 'To walk the row of pebbles 1, 2, 3, 4 carrying a tally that combines each with +'

### G5-13: reduce with init

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(reduce + 100 [1 2 3])` — parametric example has hard-coded English numeral 'four values' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + 100 [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To fold + over the vector containing 1, 2, 3 starting from an initial accumulato'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(reduce + 100 [1 2 3])` — parametric example has hard-coded English numeral 'four values' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(reduce + 100 [1 2 3])` — parametric example has hard-coded English numeral 'four values' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(reduce + 0 [])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '14', '8'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(reduce + 0 [])` — character 'Steady the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'

### G5-14: apply

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 3, 'CONCEPT_AS_VERB': 1, 'DOUBLE_NAME_INTRO': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply + [1 2 3 4])` — parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(apply + [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '3', '16'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(apply + [1 2 3 4])` — sentence with 6 commas reads as AI-output cadence: 'To apply + to the elements of the vector containing 1, 2, 3, and 4, she, steppin'
    - [CONCEPT_AS_VERB] form=`(apply + [1 2 3 4])` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply + [1 2 3 4])` — parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(apply + [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '7', '18'), resolution doesn't close the loop)

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
- issues: {'CONCEPT_AS_VERB': 1, 'DOUBLE_NAME_INTRO': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [CONCEPT_AS_VERB] form=`((partial + 10) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [DOUBLE_NAME_INTRO] form=`((partial + 10) 5)` — character 'Roan the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map (partial * 3) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '20', '3'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(map (partial * 3) [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To\napply a partially applied multiplication to each element of the vector contai'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map (partial * 3) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '10', '3'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map (partial * 3) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '15', '18'), resolution doesn't close the loop)

### G5-17: juxt

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`((juxt inc dec) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`((juxt inc dec) 5)` — character 'Heft the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [STORY_RESOLUTION_NO_DRAWN] form=`((juxt inc dec) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((juxt inc dec) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)

### G5-18: some

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 3, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(some even? [1 3 5 8 7])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '6', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(some even? [1 3 5 8 7])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8', '7', '13'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(some even? [1 3 5 8 7])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '3', '6'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(some even? [1 3 5 8 7])` — sentence with 9 commas reads as AI-output cadence: 'To check if any element in the vector containing 1, 3, 5, 8, and 7 is even, he, '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(some neg? [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '13', '10'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(some neg? [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '8', '12'), resolution doesn't close the loop)

### G5-19: every?

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(every? pos? [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '3', '10'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(every? pos? [1 2 3])` — sentence with 7 commas reads as AI-output cadence: 'To check if all elements in the vector containing 1, 2, and 3 are positive, she,'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(every? pos? [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '4', '11'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(every? pos? [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '14', '13'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(every? pos? [1 2 3])` — sentence with 7 commas reads as AI-output cadence: 'To check if all elements in the vector containing 1, 2, and 3 are positive, she,'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(every? even? [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)

### G5-20: take and drop

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 3, 'CLAUSE_STACK_OVERFLOW': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(take 3 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(take 3 [10 20 30 40 50])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '17', '7'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(take 3 [10 20 30 40 50])` — character 'Tuftkin the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [CLAUSE_STACK_OVERFLOW] form=`(take 3 [10 20 30 40 50])` — sentence with 8 commas reads as AI-output cadence: 'Tor the tortoise shook\nher head and went on with the work: to\ntake the first 3 e'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(take 3 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(take 3 [10 20 30 40 50])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '19', '4'), resolution doesn't close the loop)

### G5-21: distinct and sort

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 3, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(distinct [1 1 2 3 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '14', '15'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(distinct [1 1 2 3 3 4])` — sentence with 5 commas reads as AI-output cadence: 'Write a form whose evaluation gives the sequence produced by passing 1, 1, 2, 3,'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(distinct [1 1 2 3 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '10', '9'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(distinct [1 1 2 3 3 4])` — sentence with 5 commas reads as AI-output cadence: 'Write a form whose evaluation gives the sequence produced by passing 1, 1, 2, 3,'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(distinct [1 1 2 3 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '12', '15'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(distinct [1 1 2 3 3 4])` — character 'Gneiss the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'

### G5-22: recur — first taste

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — sentence with 6 commas reads as AI-output cadence: 'With one, the\nrunner knows when the laps are done and the tally is the\nanswer." '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — sentence with 5 commas reads as AI-output cadence: 'To walk a small circuit five times, multiplying a running tally by the current s'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — sentence with 5 commas reads as AI-output cadence: 'To walk a small circuit five times, multiplying a running tally by the current s'

## Grade 6

### G6-01: Namespace as file

- examples: 3
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1, 'DOUBLE_NAME_INTRO': 1}
    - [ANSWER_LEAK_STRING] form=`(name 'foo.bar)` — answer string 'foo.bar' appears in user_msg
    - [DOUBLE_NAME_INTRO] form=`(symbol? 'tortoise.race)` — character 'Moundkin the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'

### G6-03: require

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('cedar',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('cobalt',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('coral',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/lower-case "ZEBRA")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('cedar',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/lower-case "ZEBRA")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('thread',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/lower-case "ZEBRA")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('alder',), resolution doesn't close the loop)

### G6-04: refer and use

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= (clojure.string/upper-case "x") (clojure.string` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('ochre', 'ochre'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(= (clojure.string/upper-case "x") (clojure.string` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('myrtle', 'myrtle'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(= (clojure.string/upper-case "x") (clojure.string` — character 'Fen the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "a")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('candle',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(clojure.string/upper-case "a")` — character 'Whiskling the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "a")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('thread',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/upper-case "a")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('cedar',), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(= 'a.b 'a.b)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G6-09: Loading order

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 2, 'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '5'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(let [a 1 b (+ a 1)] (+ a b))` — character 'Patient the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a 1 b (+ a 1)] (+ a b))` — sentence with 5 commas reads as AI-output cadence: "The road is long but the\nsign holds; the next runner reads what's there now — wh"
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a 1 b (+ a 1)] (+ a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '5'), resolution doesn't close the loop)

### G6-11: Classpath

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HEDGING_NEAR_FORM] form=`(count ["src" "test" "resources"])` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(count ["src" "test" "resources"])` — sentence with 6 commas reads as AI-output cadence: 'Slumber the tortoise, stepping deliberately, simply walked to the slate, wrote\nc'

### G6-13: Aliasing conventions

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [s clojure.string/upper-case] (s "hare"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('auburn',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [s clojure.string/upper-case] (s "hare"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('lichen',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(let [s clojure.string/upper-case] (s "hare"))` — character 'Fern the hare' introduced twice within 200 chars — drop the second 'the hare'
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

### G6-16: Cleaning up requires

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`(contains? #{'clojure.string} 'clojure.string)` — character 'Roan the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'

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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try 42 (catch Exception e :caught))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('88', ':west'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try 42 (catch Exception e :caught))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('39', ':north'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(try 42 (catch Exception e :caught))` — character 'Glen the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try 42 (catch Exception e :caught))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('33', ':third'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(try 42 (catch Exception e :caught))` — character 'Whin the hare' introduced twice within 200 chars — drop the second 'the hare'

### G7-03: try / finally

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(try 7 (finally (prn :cleanup)))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try 7 (finally (prn :cleanup)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', ':cleanup'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try 7 (finally (prn :cleanup)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', ':cleanup'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try 7 (finally (prn :cleanup)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', ':cleanup'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (try (/ 1 0) (finally (prn :ran))) (catch Exc` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1', ':ran'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(try (try (/ 1 0) (finally (prn :ran))) (catch Exc` — character 'Muse the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'

### G7-04: ex-info

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', 'bad'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', 'bad'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', 'bad'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(try (throw (ex-info "x" {:k :v})) (catch Exceptio` — character 'Fen the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [CLAUSE_STACK_OVERFLOW] form=`(try (throw (ex-info "x" {:k :v})) (catch Exceptio` — sentence with 5 commas reads as AI-output cadence: 'The REPL is forgiving in a\nway that a real race is not." To throw an ex-info wit'

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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 2, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '8', '9'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — sentence with 5 commas reads as AI-output cadence: 'The REPL is forgiving in a\nway that a real race is not." To assert that 5 equals'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '9'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — character 'Brisk the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [CLAUSE_STACK_OVERFLOW] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — sentence with 5 commas reads as AI-output cadence: 'To\nassert that 7 equals 9, catch the failure, and return a numeric code required'

### G7-08: prn and pprint

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(with-out-str (prn 42))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(with-out-str (prn 42))` — character 'Stoneheart the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(with-out-str (prn 42))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(with-out-str (prn 42))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(with-out-str (prn :hare))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(with-out-str (prn :hare))` — character 'Hushwise the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'

### G7-09: tap>

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(tap> :hello)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hello',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(tap> :hello)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hello',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(tap> :hello)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hello',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(tap> 42)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(tap> 42)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(tap> 42)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)

### G7-10: doc and source

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:doc (meta '^{:doc "adds two"} plus))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':doc', ':doc', 'adds two'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:doc (meta '^{:doc "adds two"} plus))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':doc', ':doc', 'adds two'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:doc (meta '^{:doc "adds two"} plus))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':doc', ':doc', 'adds two'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(:doc (meta '^{:doc "adds two"} plus))` — character 'Steadypaw the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'

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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "hare
tortoise
")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('amber',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(count "hare
tortoise
")` — sentence with 5 commas reads as AI-output cadence: 'Scrolls are how the two meet — a value\ncrosses out and becomes letters on parchm'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "hare
tortoise
")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('cedar',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "hare
tortoise
")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('ochre',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(count "hare
tortoise
")` — character 'Pebblepaw the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "a\nb\nc" #"\n")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc', '\\n'), resolution doesn't close the loop)

### G7-13: line-seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first (clojure.string/split-lines "first\nsecond"` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('first\\nsecond',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first (clojure.string/split-lines "first\nsecond"` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('first\\nsecond',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(first (clojure.string/split-lines "first\nsecond"` — character 'Whorl the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'

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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "42")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', '42'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "42")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', '42'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(clojure.edn/read-string "42")` — character 'Roan the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "42")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', '42'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "{:a 1}")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', '{:a 1}'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "{:a 1}")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', '{:a 1}'), resolution doesn't close the loop)

### G7-17: JSON roundtrip

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — character 'Mallow the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G7-18: Shell command

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:cmd {:cmd "ls" :args ["-l"]})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '16', ':north'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:cmd {:cmd "ls" :args ["-l"]})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '13', ':z'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:cmd {:cmd "ls" :args ["-l"]})` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('17', '9', ':cool'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (:args {:cmd "echo" :args ["hello" "world"]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('11', '14', ':north'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(count (:args {:cmd "echo" :args ["hello" "world"]` — sentence with 5 commas reads as AI-output cadence: 'The runtime moves a value across\nthe boundary, calls the foreign tool, and bring'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (:args {:cmd "echo" :args ["hello" "world"]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '7', ':west'), resolution doesn't close the loop)

## Grade 8

### G8-01: Why polymorphism

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':tortoise', ':else'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':tortoise', ':else'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':tortoise', ':else'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(let [speak (fn [k] (cond (= k :hare) "swift" (= k` — character 'Pillow the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'

### G8-02: deftype introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 2, 'HIGH_LENGTH': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — sentence with 5 commas reads as AI-output cadence: 'Faster, more\nfocused, less convenient." To define a type Pebble with a color fie'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — sentence with 5 commas reads as AI-output cadence: 'Faster, more\nfocused, less convenient." To define a type Pebble with a color fie'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Stone [weight]) (.-weight (Stone. 7))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)

### G8-03: defrecord introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 2, 'DOUBLE_NAME_INTRO': 1}
    - [HIGH_LENGTH] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — user_msg 207 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':pace', ':slow', 'Alice'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':pace', ':slow', 'Alice'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':pace', ':slow', 'Alice'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — sentence with 6 commas reads as AI-output cadence: 'Faster, more\nfocused, less convenient." To define a Runner case with two named c'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defrecord Runner [name pace]) (:name (->Runne` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':name', ':moderate', 'Bob'), resolution doesn't close the loop)

### G8-04: Protocol definition

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`(do (defprotocol Greet (hail [this])) (some? Greet` — character 'Fen the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'

### G8-05: Protocol extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 5}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('swift', 'hare'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 6 commas reads as AI-output cadence: "The runtime looks up which species the runner\nis, then runs that species' answer"
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('swift', 'hare'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('swift', 'hare'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'The runtime reads from the book whenever the call goes\nout." To define a protoco'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', ':number'), resolution doesn't close the loop)

### G8-06: Protocol method dispatch

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 5}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'Any animal that can sign the book may claim\nmembership." To define a protocol Pa'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'The runtime reads from the book whenever the call goes\nout." To define a protoco'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 6 commas reads as AI-output cadence: "The runtime looks up which species the runner\nis, then runs that species' answer"

### G8-07: Record implementing protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':swift', 'Pip'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, define a record Hare that implement'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':swift', 'Pip'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, define a record Hare that implement'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':swift', 'Pip'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, define a record Hare that implement'

### G8-08: Multimethod defmulti

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 2, 'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [DOUBLE_NAME_INTRO] form=`(do (defmulti pace :species) (defmethod pace :hare` — character 'Whiskling the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [HIGH_LENGTH] form=`(do (defmulti pace :species) (defmethod pace :hare` — user_msg 209 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 5 commas reads as AI-output cadence: 'The runtime reads it, finds the matching arm,\nand runs that one." To declare a s'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmulti tag :kind) (defmethod tag :stone [_]` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':kind', ':stone', ':hard'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (defmulti tag :kind) (defmethod tag :stone [_]` — character 'Hushwise the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmulti tag :kind) (defmethod tag :stone [_]` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':kind', ':stone', ':hard'), resolution doesn't close the loop)

### G8-09: Multimethod defmethod

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 3, 'PARAGRAPH_FRAGMENTATION': 1, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmulti pace :species) (defmethod pace :hare` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':species', ':hare', ':swift'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 6 commas reads as AI-output cadence: 'The runtime reads it, finds the matching arm,\nand runs that one." To define a mu'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmulti pace :species) (defmethod pace :hare` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':species', ':hare', ':swift'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 5 commas reads as AI-output cadence: 'To define a multimethod pace that dispatches on :species with methods for both :'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmulti pace :species) (defmethod pace :hare` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':species', ':hare', ':swift'), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(do (defmulti pace :species) (defmethod pace :hare` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G8-10: Multimethod vs protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1, 'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 3}
    - [DOUBLE_NAME_INTRO] form=`(do (defmulti show identity) (defmethod show :rabb` — character 'Steadypaw the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [HIGH_LENGTH] form=`(do (defprotocol Show (show [this])) (extend-proto` — user_msg 203 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Show (show [this])) (extend-proto` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('str-', 'hare'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Show (show [this])) (extend-proto` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Show with method show, extend it to String type, then call '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Show (show [this])) (extend-proto` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('str-', 'hare'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Show (show [this])) (extend-proto` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Show with method show, extend it to String type, then call '

### G8-11: Protocol vs Java interface

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol IPace (run [this])) (extend-proto` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':ran', 'hare'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol IPace (run [this])) (extend-proto` — sentence with 6 commas reads as AI-output cadence: "The runtime looks up which species the runner\nis, then runs that species' answer"
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol IPace (run [this])) (extend-proto` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':ran', 'hare'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol IPace (run [this])) (extend-proto` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol IPace with method run, extend it to String type, then call '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol IPace (run [this])) (extend-proto` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':ran', 'hare'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol IPace (run [this])) (extend-proto` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol IPace with method run, extend it to String type, then call '

### G8-12: extend-type on built-in types

- examples: 2
- variety @ n=50: 0.99
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 5}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-type` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', ':number-pace'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-type` — sentence with 6 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, use extend-type to attach it to Lon'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-type` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', ':number-pace'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-type` — sentence with 7 commas reads as AI-output cadence: 'The runtime reads it, finds the matching arm,\nand runs that one." To define a pr'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-type` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', ':number-pace'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-type` — sentence with 6 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, use extend-type to attach it to Lon'

### G8-13: this-style vs fn-style

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'PARAGRAPH_FRAGMENTATION': 1, 'CLAUSE_STACK_OVERFLOW': 6, 'DOUBLE_NAME_INTRO': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Named (name-of [this])) (defrecor` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':n', 'Zephyr'), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Named (name-of [this])) (defrecor` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Named with method name-of, define a record that uses this t'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Named (name-of [this])) (defrecor` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':n', 'Zephyr'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Named (name-of [this])) (defrecor` — sentence with 5 commas reads as AI-output cadence: 'Any animal that can sign the book may claim\nmembership." To define a protocol Na'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Named (name-of [this])) (defrecor` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':n', 'Zephyr'), resolution doesn't close the loop)

### G8-14: Protocols don't inherit

- examples: 1
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 3}
    - [HIGH_LENGTH] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg 220 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — sentence with 6 commas reads as AI-output cadence: 'To define two protocols A and B, each with a method, extend both to String type '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — sentence with 6 commas reads as AI-output cadence: 'Any animal that can sign the book may claim\nmembership." To define two protocols'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)

### G8-15: derive and isa? — multimethod hierarchy

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':runner', ':hare'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':runner', ':hare'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — sentence with 5 commas reads as AI-output cadence: 'To establish a type relationship where ::hare is a type of ::runner, then check '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':runner', ':hare'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(isa? java.lang.Long java.lang.Number)` — sentence with 5 commas reads as AI-output cadence: 'The runtime reads it, finds the matching arm,\nand runs that one." To check wheth'

### G8-16: Abstract design with protocols

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 4, 'DOUBLE_NAME_INTRO': 1, 'HIGH_LENGTH': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':leap', ':plod'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — sentence with 5 commas reads as AI-output cadence: 'The runtime reads from the book whenever the call goes\nout." To define a protoco'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':leap', ':plod'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — character 'Roan the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — sentence with 6 commas reads as AI-output cadence: "The runtime looks up which species the runner\nis, then runs that species' answer"
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':leap', ':plod'), resolution doesn't close the loop)

## Grade 9

### G9-01: Immutability as default — review

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :b 2) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '6', ':kumquat'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :b 2) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '18', '9'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [m {:a 1}] (assoc m :b 2) m)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('12', '10', '8'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(let [m {:a 1}] (assoc m :b 2) m)` — character 'Bunneh the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [CLAUSE_STACK_OVERFLOW] form=`(let [m {:a 1}] (assoc m :b 2) m)` — sentence with 7 commas reads as AI-output cadence: 'To bind a map m, call assoc to add :b 2 to a new map, then return the unchanged '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [v [1 2 3]] (conj v 4) v)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('14', '3', '18'), resolution doesn't close the loop)

### G9-02: Why state at all

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 6, 'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — sentence with 8 commas reads as AI-output cadence: 'If two\nanimals arrive at once, the runtime makes sure only one of us\ngoes throug'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — sentence with 8 commas reads as AI-output cadence: 'to write atomically, no matter\nwho else is watching." To construct an atom holdi'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — sentence with 7 commas reads as AI-output cadence: 'The page changes only when someone writes — and only as the\nruntime allows." To '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def progress (atom :idle)) (reset! progress :` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':idle', ':running'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def progress (atom :idle)) (reset! progress :` — sentence with 8 commas reads as AI-output cadence: 'to write atomically, no matter\nwho else is watching." To construct an atom holdi'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def progress (atom :idle)) (reset! progress :` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':idle', ':running'), resolution doesn't close the loop)

### G9-03: Atom introduction

- examples: 3
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 9, 'CLAUSE_STACK_OVERFLOW': 9, 'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 7 commas reads as AI-output cadence: 'To set up a shared notebook starting at 0, atomically add one to its page, then '
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 7 commas reads as AI-output cadence: 'To set up a shared notebook starting at 0, atomically add one to its page, then '
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 7 commas reads as AI-output cadence: 'The page changes only when someone writes — and only as the\nruntime allows." To '

### G9-04: Atom CAS semantics

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 6, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — concept_phrase 'atom, CAS, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — sentence with 7 commas reads as AI-output cadence: 'The runtime sees to that — no two writers stomp on each other\'s\nwork." To constr'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — concept_phrase 'atom, CAS, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — sentence with 7 commas reads as AI-output cadence: 'The page changes only when someone writes — and only as the\nruntime allows." To '
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — concept_phrase 'atom, CAS, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — sentence with 7 commas reads as AI-output cadence: 'The page changes only when someone writes — and only as the\nruntime allows." To '

### G9-05: Watch on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':w',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — sentence with 8 commas reads as AI-output cadence: 'If two\nanimals arrive at once, the runtime makes sure only one of us\ngoes throug'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':w',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — sentence with 7 commas reads as AI-output cadence: 'The runtime sees to that — no two writers stomp on each other\'s\nwork." To constr'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':w',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — sentence with 7 commas reads as AI-output cadence: 'The page changes only when someone writes — and only as the\nruntime allows." To '

### G9-06: Validator on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — sentence with 5 commas reads as AI-output cadence: 'validator on it, atomically swap by applying inc, and dereference, she composed\n'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — sentence with 5 commas reads as AI-output cadence: 'validator on it, atomically swap by applying inc, and dereference, she composed\n'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — sentence with 5 commas reads as AI-output cadence: 'validator on it, atomically swap by applying inc, and dereference, he\ncomposed a'

### G9-07: Ref introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 6, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — concept_phrase 'ref, dosync, alter, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 8 commas reads as AI-output cadence: 'To construct a ref holding 0, perform a transactional alter by applying inc insi'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — concept_phrase 'ref, dosync, alter, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 8 commas reads as AI-output cadence: 'To construct a ref holding 0, perform a transactional alter by applying inc insi'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — concept_phrase 'ref, dosync, alter, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 8 commas reads as AI-output cadence: 'To construct a ref holding 0, perform a transactional alter by applying inc insi'

### G9-08: dosync and alter

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 2, 'CLAUSE_STACK_OVERFLOW': 6, 'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CONCEPT_PHRASE_COMMA_LIST': 3}
    - [DOUBLE_NAME_INTRO] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — character 'Whiskling the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — sentence with 6 commas reads as AI-output cadence: 'To construct refs a and b, perform a coordinated transaction that alters both by'
    - [HIGH_LENGTH] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — user_msg 209 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — sentence with 6 commas reads as AI-output cadence: 'To construct refs a and b, perform a coordinated transaction that alters both by'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — sentence with 6 commas reads as AI-output cadence: 'The page changes only when someone writes — and only as the\nruntime allows." To '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '5'), resolution doesn't close the loop)

### G9-09: Ref vs atom

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 6, 'DOUBLE_NAME_INTRO': 1}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 7 commas reads as AI-output cadence: 'The page changes only when someone writes — and only as the\nruntime allows." To '
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 7 commas reads as AI-output cadence: 'To construct an atom holding 0, atomically swap it by applying inc, and derefere'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 7 commas reads as AI-output cadence: 'The runtime sees to that — no two writers stomp on each other\'s\nwork." To constr'

### G9-10: Agent introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 6, 'DOUBLE_NAME_INTRO': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 9 commas reads as AI-output cadence: 'To construct an agent holding 0, asynchronously send inc to it, await its comple'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 10 commas reads as AI-output cadence: 'The result will be there when you ask\nfor it — sometimes you have to wait for th'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [DOUBLE_NAME_INTRO] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — character 'Steadypaw the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'

### G9-11: send and send-off

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 5}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 10 commas reads as AI-output cadence: 'The result will be there when you ask\nfor it — sometimes you have to wait for th'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 9 commas reads as AI-output cadence: 'To construct an agent holding 0, use send to asynchronously apply inc, await its'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 9 commas reads as AI-output cadence: 'To\nconstruct an agent holding 0, use send to asynchronously apply inc, await its'

### G9-12: await — synchronizing on agents

- examples: 1
- variety @ n=50: 0.98
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 3, 'CLAUSE_STACK_OVERFLOW': 3}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — concept_phrase 'agent, double send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 9 commas reads as AI-output cadence: 'To\nconstruct an agent holding 0, asynchronously send inc twice, synchronize with'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — concept_phrase 'agent, double send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 9 commas reads as AI-output cadence: 'The runtime makes that easier than it sounds." To construct an agent holding 0, '
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — concept_phrase 'agent, double send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 9 commas reads as AI-output cadence: 'To\nconstruct an agent holding 0, asynchronously send inc twice, synchronize with'

### G9-13: future introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 2}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`@(future (+ 1 2))` — concept_phrase 'future, add, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`@(future (+ 1 2))` — sentence with 6 commas reads as AI-output cadence: 'To dispatch a runner to compute the sum of 1 and 2; later, ask the runner for th'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`@(future (+ 1 2))` — concept_phrase 'future, add, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CONCEPT_PHRASE_COMMA_LIST] form=`@(future (+ 1 2))` — concept_phrase 'future, add, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [STORY_RESOLUTION_NO_DRAWN] form=`@(future (* 6 7))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '7'), resolution doesn't close the loop)
    - [CONCEPT_PHRASE_COMMA_LIST] form=`@(future (* 6 7))` — concept_phrase 'future, multiply, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose

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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 4}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def p (promise)) (deliver p :done) @p)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':done',), resolution doesn't close the loop)
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def p (promise)) (deliver p :done) @p)` — concept_phrase 'promise, deliver, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def p (promise)) (deliver p :done) @p)` — sentence with 8 commas reads as AI-output cadence: 'The result will be there when you ask\nfor it — sometimes you have to wait for th'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def p (promise)) (deliver p :done) @p)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':done',), resolution doesn't close the loop)
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def p (promise)) (deliver p :done) @p)` — concept_phrase 'promise, deliver, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def p (promise)) (deliver p :done) @p)` — sentence with 7 commas reads as AI-output cadence: 'To\nconstruct a promise, deliver a completion keyword to it, and dereference to g'

### G9-16: volatile — when STM is too heavy

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 6, 'DOUBLE_NAME_INTRO': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — concept_phrase 'volatile, vswap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — sentence with 7 commas reads as AI-output cadence: 'The page changes only when someone writes — and only as the\nruntime allows." To '
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — concept_phrase 'volatile, vswap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [DOUBLE_NAME_INTRO] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — character 'Roan the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — sentence with 8 commas reads as AI-output cadence: 'If two\nanimals arrive at once, the runtime makes sure only one of us\ngoes throug'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — concept_phrase 'volatile, vswap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose

### G9-17: binding — thread-local

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'DOUBLE_NAME_INTRO': 2, 'CLAUSE_STACK_OVERFLOW': 6, 'HIGH_LENGTH': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — concept_phrase 'dynamic var, binding, read' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [DOUBLE_NAME_INTRO] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — character 'Heft the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — sentence with 7 commas reads as AI-output cadence: 'The runtime sees to that — no two writers stomp on each other\'s\nwork." To define'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — concept_phrase 'dynamic var, binding, read' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 6, 'FORM_DISPLAY_AND_FORM_NOUN': 2, 'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 2}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — concept_phrase 'lock, locking, arithmetic' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — sentence with 7 commas reads as AI-output cadence: 'The page changes only when someone writes — and only as the\nruntime allows." To '
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — concept_phrase 'lock, locking, arithmetic' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — sentence with 8 commas reads as AI-output cadence: 'To create an object to use as a monitor, acquire the lock, and evaluate an addit'
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

## Grade 10

### G10-01: quote, unquote, unquote-splice

- examples: 3
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2, 'THE_FORM_OVERUSE': 3, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(quote (+ 1 2))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [THE_FORM_OVERUSE] form=`(quote (+ 1 2))` — `the form` appears 6 times in user_msg (template tic — vary references)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '17', '14'), resolution doesn't close the loop)
    - [THE_FORM_OVERUSE] form=`'(1 2 3)` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [DOUBLE_NAME_INTRO] form=`'(1 2 3)` — character 'Pillow the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'

### G10-02: syntax-quote

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'THE_FORM_OVERUSE': 3, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 10] `(+ ~x ~x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10',), resolution doesn't close the loop)
    - [THE_FORM_OVERUSE] form=`(let [x 10] `(+ ~x ~x))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 10] `(+ ~x ~x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 10] `(+ ~x ~x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10',), resolution doesn't close the loop)
    - [THE_FORM_OVERUSE] form=`(let [x 10] `(+ ~x ~x))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [xs [1 2 3]] `(list ~@xs))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G10-03: defmacro introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg 207 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` — character 'Skimble the hare' introduced twice within 200 chars — drop the second 'the hare'

### G10-04: Macro expansion rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(when true 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(when true 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(when true 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(or a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(macroexpand-1 '(or a b))` — character 'Fleeting the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(or a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)

### G10-05: macroexpand

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(macroexpand '(-> 1 inc inc))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(macroexpand '(-> 1 inc inc))` — sentence with 5 commas reads as AI-output cadence: 'You write the rule\nonce, and any recipe that uses it gets rewritten on the way t'

### G10-06: when and when-not as macros

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'STORY_RESOLUTION_NO_DRAWN': 9, 'CLAUSE_STACK_OVERFLOW': 6, 'DOUBLE_NAME_INTRO': 2}
    - [LOW_GROUNDING] form=`(when true 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('8',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(when true 1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'You write the rule\nonce, and any recipe that uses it gets rewritten on the way t'
    - [LOW_GROUNDING] form=`(when true 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when true 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(when true 1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'You write the rule\nonce, and any recipe that uses it gets rewritten on the way t'

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CONCEPT_AS_VERB': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'PARAGRAPH_FRAGMENTATION': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(-> 5 inc inc inc)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`(-> 5 inc inc inc)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(-> 5 inc inc inc)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(-> 5 inc inc inc)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', '14', '10'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — sentence with 7 commas reads as AI-output cadence: 'To thread a vector through filter, map, and reduce using thread-last, she, with '

### G10-08: Macro vs fn

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 4}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — character 'Whiskling the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9', '3'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — character 'Sageback the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — character 'Snippet the hare' introduced twice within 200 chars — drop the second 'the hare'

### G10-09: Hygiene and gensym

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('x_', 'x_'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('x_', 'x_'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('x_', 'x_'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — character 'Sprint the hare' introduced twice within 200 chars — drop the second 'the hare'

### G10-10: Anaphoric macros are confusing

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — character 'Steadypaw the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if-let [x 7] (* x x) 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if-let [x 7] (* x x) 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)

### G10-11: Reader macros overview

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('20', '8', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('18', '15', '20'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`'(1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('13', '19', '20'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(* % %) 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(* % %) 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(* % %) 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)

### G10-12: Tagged literals

- examples: 2
- variety @ n=50: 0.99
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inst? #inst "2024-01-01")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('2024', '-01', '-01'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(inst? #inst "2024-01-01")` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inst? #inst "2024-01-01")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('2024', '-01', '-01'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inst? #inst "2024-01-01")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('2024', '-01', '-01'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(inst? #inst "2024-01-01")` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(uuid? #uuid "00000000-0000-0000-0000-000000000000` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('00000000', '-0000', '-0000'), resolution doesn't close the loop)

### G10-13: Data readers and EDN extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 2, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "42")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', '42'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "42")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', '42'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "42")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', '42'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "[:a :b :c]")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b', ':c'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(clojure.edn/read-string "[:a :b :c]")` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "[:a :b :c]")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b', ':c'), resolution doesn't close the loop)

### G10-14: eval (the function)

- examples: 2
- variety @ n=50: 0.99
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval '(+ 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(eval '(+ 1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval '(+ 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(eval '(+ 1 2 3))` — sentence with 5 commas reads as AI-output cadence: 'You write the rule\nonce, and any recipe that uses it gets rewritten on the way t'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval '(+ 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval (list '+ 4 5))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', '5'), resolution doesn't close the loop)

### G10-15: When not to write a macro

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 2, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "a function suffices when no syntax shaping is` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', 'raven'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "a function suffices when no syntax shaping is` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', 'cobalt'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do "a function suffices when no syntax shaping is` — sentence with 5 commas reads as AI-output cadence: 'You write the rule\nonce, and any recipe that uses it gets rewritten on the way t'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "a function suffices when no syntax shaping is` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', 'myrtle'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do "prefer fn unless you must shape syntax" (map ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3', '12'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do "prefer fn unless you must shape syntax" (map ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-16: Macro pattern library

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1, 'HIGH_LENGTH': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':slow-and-steady'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':slow-and-steady'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — character 'Roan the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':slow-and-steady'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':slow',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':slow',), resolution doesn't close the loop)

## Grade 11

### G11-01: JVM vs CLR vs JS vs Python (host overview)

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScr` — character 'Ivy the hare' introduced twice within 200 chars — drop the second 'the hare'

### G11-02: Method call syntax

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(.toUpperCase "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(.toUpperCase "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(.toUpperCase "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(. "abc" toUpperCase)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(. "abc" toUpperCase)` — character 'Tumbler the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(. "abc" toUpperCase)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)

### G11-03: Static method call

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(Math/max 3 9)` — character 'Muse the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [CLAUSE_STACK_OVERFLOW] form=`(Math/max 3 9)` — sentence with 5 commas reads as AI-output cadence: 'The runtime moves a value across\nthe boundary, calls the foreign tool, and bring'

### G11-04: Field access

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'DOUBLE_NAME_INTRO': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(count "tortoise")` — sentence with 5 commas reads as AI-output cadence: 'The runtime moves a value across\nthe boundary, calls the foreign tool, and bring'
    - [DOUBLE_NAME_INTRO] form=`(count "tortoise")` — character 'Fen the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [CLAUSE_STACK_OVERFLOW] form=`(count "tortoise")` — sentence with 5 commas reads as AI-output cadence: 'The runtime moves a value across\nthe boundary, calls the foreign tool, and bring'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('myrrh',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('apple',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('lichen',), resolution doesn't close the loop)

### G11-05: Import form

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1, 'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [DOUBLE_NAME_INTRO] form=`(do "import is a top-of-file ns clause" :studied)` — character 'Sageback the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [HEDGING_NEAR_FORM] form=`(do "import is a top-of-file ns clause" :studied)` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "import is a top-of-file ns clause" :studied)` — sentence with 6 commas reads as AI-output cadence: 'Sepia the tortoise, with eyes always on the path, simply walked to the slate, wr'

### G11-06: new and dot-construct

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(String. "go")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(new String "jump")` — sentence with 5 commas reads as AI-output cadence: 'The runtime moves a value across\nthe boundary, calls the foreign tool, and bring'
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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1, 'HIGH_LENGTH': 1, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [^String s "abc"] (.toUpperCase s))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(let [^String s "abc"] (.toUpperCase s))` — character 'Whiskling the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [HIGH_LENGTH] form=`(let [^String s "abc"] (.toUpperCase s))` — user_msg 205 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [^String s "abc"] (.toUpperCase s))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [^String s "abc"] (.toUpperCase s))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do "type hints are metadata that guide compilatio` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-10: ClojureScript overview

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 2, 'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [DOUBLE_NAME_INTRO] form=`(do "ClojureScript compiles to JavaScript via the ` — character 'Bounce the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [HEDGING_NEAR_FORM] form=`(do "cljs runs in browsers and Node, with JS inter` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "cljs runs in browsers and Node, with JS inter` — sentence with 6 commas reads as AI-output cadence: 'Vine the tortoise, saying very little, simply walked to the slate, wrote\nwhere C'
    - [DOUBLE_NAME_INTRO] form=`(do "cljs runs in browsers and Node, with JS inter` — character 'Fern the hare' introduced twice within 200 chars — drop the second 'the hare'

### G11-12: Basilisp overview (Python host)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 2, 'CLAUSE_STACK_OVERFLOW': 2}
    - [HEDGING_NEAR_FORM] form=`(do "basilisp is a Clojure-like Lisp implemented o` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "basilisp is a Clojure-like Lisp implemented o` — sentence with 6 commas reads as AI-output cadence: 'Meander the tortoise, saying very little, simply walked to the slate, wrote\nthe '
    - [HEDGING_NEAR_FORM] form=`(do "basilisp interops with Python via the same do` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "basilisp interops with Python via the same do` — sentence with 7 commas reads as AI-output cadence: 'Quietkin the tortoise, with steady, careful steps, simply walked to the slate, w'

### G11-13: Cross-platform .cljc and reader-conditionals

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 2}
    - [DOUBLE_NAME_INTRO] form=`(do "#?(:clj … :cljs …) selects a form per host at` — character 'Lithe the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [DOUBLE_NAME_INTRO] form=`(do ".cljc files share code across multiple hosts"` — character 'Steady the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'

### G11-14: Debugging host leaks

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "host stack traces leak through interop; learn` — sentence with 5 commas reads as AI-output cadence: 'The runtime moves a value across\nthe boundary, calls the foreign tool, and bring'

## Grade 12

### G12-01: Transducers introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(into [] (map inc) [1 2 3])` — user_msg 203 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] (map inc) [1 2 3])` — sentence with 7 commas reads as AI-output cadence: 'To use the map-inc transducer with into to increment the vector containing 1, 2,'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (filter even?) [1 2 3 4 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', '5'), resolution doesn't close the loop)

### G12-02: Transducer composition

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 3, 'HIGH_LENGTH': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', '5'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — sentence with 6 commas reads as AI-output cadence: 'Write a form whose evaluation gives the sum accumulated via transduce using the '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', '5'), resolution doesn't close the loop)

### G12-03: into with a transducer (xform)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 2, 'DOUBLE_NAME_INTRO': 1}
    - [HIGH_LENGTH] form=`(into #{} (map inc) [1 2 3])` — user_msg 203 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into #{} (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(into #{} (map inc) [1 2 3])` — sentence with 7 commas reads as AI-output cadence: 'To use the map-inc transducer with into to create a set from the incremented ele'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into #{} (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(into #{} (map inc) [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'Deepen the tortoise shook\nher head and went on with the work: to\nuse the map-inc'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into #{} (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G12-04: core.async introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HEDGING_NEAR_FORM] form=`(do "(chan), (go ...), (<! ...), (>! ...) form the` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "(chan), (go ...), (<! ...), (>! ...) form the` — sentence with 6 commas reads as AI-output cadence: 'Sage the tortoise, with eyes always on the path, simply walked to the slate, wro'

### G12-05: Channels and pipelines

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1, 'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [DOUBLE_NAME_INTRO] form=`(do "pipelines transform streams of values channel` — character 'Sageback the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'
    - [HEDGING_NEAR_FORM] form=`(do "pipelines transform streams of values channel` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "pipelines transform streams of values channel` — sentence with 6 commas reads as AI-output cadence: 'Sepia the tortoise, with eyes always on the path, simply walked to the slate, wr'

### G12-07: Spec generators

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 2, 'CLAUSE_STACK_OVERFLOW': 2, 'DOUBLE_NAME_INTRO': 1}
    - [HEDGING_NEAR_FORM] form=`(do "s/exercise produces sample inputs for a spec"` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "s/exercise produces sample inputs for a spec"` — sentence with 6 commas reads as AI-output cadence: 'Knoll the tortoise, saying very little, simply walked to the slate, wrote\nthe sa'
    - [DOUBLE_NAME_INTRO] form=`(do "spec generators turn specs into property-base` — character 'Brisk the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [HEDGING_NEAR_FORM] form=`(do "spec generators turn specs into property-base` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "spec generators turn specs into property-base` — sentence with 6 commas reads as AI-output cadence: 'Bide the tortoise, stepping deliberately, simply walked to the slate, wrote\nthe '

### G12-08: clojure.test

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 2}
    - [DOUBLE_NAME_INTRO] form=`(= (+ 1 2) 3)` — character 'Whiskling the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [DOUBLE_NAME_INTRO] form=`(= (+ 1 2) 3)` — character 'Sageback the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'

### G12-09: Test fixtures

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`(do "(use-fixtures :each f) wraps every deftest in` — character 'Tit the hare' introduced twice within 200 chars — drop the second 'the hare'

### G12-10: Property-based testing

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1, 'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [DOUBLE_NAME_INTRO] form=`(do "test.check generates inputs and checks proper` — character 'Caper the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [HEDGING_NEAR_FORM] form=`(do "test.check generates inputs and checks proper` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "test.check generates inputs and checks proper` — sentence with 6 commas reads as AI-output cadence: 'Taupe the tortoise, saying very little, simply walked to the slate, wrote\nthe pr'

### G12-12: deps.edn projects

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 2, 'CLAUSE_STACK_OVERFLOW': 2}
    - [HEDGING_NEAR_FORM] form=`(do "deps.edn declares :deps and :aliases for the ` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "deps.edn declares :deps and :aliases for the ` — sentence with 6 commas reads as AI-output cadence: 'Meander the tortoise, saying very little, simply walked to the slate, wrote\nthe '
    - [HEDGING_NEAR_FORM] form=`(do "deps.edn is read by the official `clj`/`cloju` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "deps.edn is read by the official `clj`/`cloju` — sentence with 7 commas reads as AI-output cadence: 'Quietkin the tortoise, with steady, careful steps, simply walked to the slate, w'

### G12-13: Aliases and tools

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 2}
    - [DOUBLE_NAME_INTRO] form=`(do "`clj -M:test` runs the :test alias from deps.` — character 'Lithe the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [DOUBLE_NAME_INTRO] form=`(do "aliases compose extra paths, deps, and main o` — character 'Steady the tortoise' introduced twice within 200 chars — drop the second 'the tortoise'

### G12-14: Pedestal / Ring (web stack brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`(do "Pedestal layers interceptors over Ring for ri` — character 'Scamper the hare' introduced twice within 200 chars — drop the second 'the hare'

### G12-15: Datomic / XTDB (datalog db brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPEATED_OPENER_FRAGMENT': 1, 'DOUBLE_NAME_INTRO': 1}
    - [REPEATED_OPENER_FRAGMENT] form=`(do "queries are written in datalog over EDN-shape` — opener fragment 'at the edge of the garden,' also appears later in user_msg
    - [DOUBLE_NAME_INTRO] form=`(do "queries are written in datalog over EDN-shape` — character 'Jolt the hare' introduced twice within 200 chars — drop the second 'the hare'

### G12-16: Reagent (cljs UI brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 2}
    - [DOUBLE_NAME_INTRO] form=`(do "Reagent wraps React with Hiccup-shaped Clojur` — character 'Buttercup the hare' introduced twice within 200 chars — drop the second 'the hare'
    - [DOUBLE_NAME_INTRO] form=`(do "components are functions returning Hiccup vec` — character 'Galop the hare' introduced twice within 200 chars — drop the second 'the hare'

### G12-17: Library design patterns

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_NAME_INTRO': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "good libraries expose data, then functions, t` — sentence with 5 commas reads as AI-output cadence: 'Halfway through the race, Lightfoot the hare, boasting at every turn, stopped on'
    - [DOUBLE_NAME_INTRO] form=`(= [1 2 3] (vec '(1 2 3)))` — character 'Moor the hare' introduced twice within 200 chars — drop the second 'the hare'

### G12-18: Clojure style guide

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPEATED_OPENER_FRAGMENT': 1}
    - [REPEATED_OPENER_FRAGMENT] form=`(do "prefer pure functions, name predicates with ?` — opener fragment 'at the edge of the meadow' also appears later in user_msg

---

## Summary

### Issue counts (across all examples × 3 records)

- **STORY_RESOLUTION_NO_DRAWN**: 783
- **CLAUSE_STACK_OVERFLOW**: 292
- **DOUBLE_NAME_INTRO**: 182
- **CONCEPT_PHRASE_COMMA_LIST**: 75
- **NARRATIVE_NUMERAL_HARDCODE**: 42
- **CONCEPT_AS_VERB**: 25
- **HIGH_LENGTH**: 25
- **LOW_GROUNDING**: 23
- **REPL_AS_TIME_TRAVELLER**: 22
- **FORM_DISPLAY_AND_FORM_NOUN**: 20
- **HEDGING_NEAR_FORM**: 12
- **PARAGRAPH_FRAGMENTATION**: 10
- **STRING_AS_CHAR_MISCLAIM**: 6
- **THE_FORM_OVERUSE**: 6
- **ANSWER_LEAK_STRING**: 4
- **ANSWER_LEAK**: 3
- **REPEATED_OPENER_FRAGMENT**: 3
- **SMALL_INT_LEAK**: 1
- **COLLECTION_LEAK**: 1

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 164 | — |
| 2 | 22 | 88 | 140 | — |
| 3 | 18 | 31 | 102 | — |
| 4 | 20 | 39 | 160 | — |
| 5 | 22 | 39 | 176 | — |
| 6 | 16 | 33 | 52 | — |
| 7 | 18 | 36 | 104 | — |
| 8 | 16 | 31 | 138 | — |
| 9 | 18 | 34 | 239 | — |
| 10 | 16 | 36 | 154 | — |
| 11 | 14 | 29 | 47 | — |
| 12 | 18 | 37 | 59 | — |

### Sample issues by severity

#### DOUBLE_NAME_INTRO

- `G1-01` (form `0`): character 'Ivy the hare' introduced twice within 200 chars — drop the second 'the hare'
    ```
    Ivy the hare was certain she could not lose; Cobblestone the tortoise was certain of nothing except the next step.

Ivy the hare chalked a wager on a flat stone in the woods: whoever
predicted the result of `1` would set the next race's
distance. Cobblestone the tortoise, with eyes always on the pat...
    ```
- `G1-01` (form `"hello"`): character 'Bunny the hare' introduced twice within 200 chars — drop the second 'the hare'
    ```
    Bunny the hare liked to talk; Cobblestone the tortoise liked to listen, and the rivalry between them had grown into a small legend at the edge of the garden.

"There is no need to evaluate that," Bunny the hare said, boasting at every turn.
"Anyone can see what the string "coral" comes to." Cobblest...
    ```
- `G1-01` (form `nil`): character 'Ivy the hare' introduced twice within 200 chars — drop the second 'the hare'
    ```
    Ivy the hare was certain she could not lose; Cobblestone the tortoise was certain of nothing except the next step.

Ivy the hare chalked a wager on a flat stone in the woods: whoever
predicted the result of `nil` would set the next race's
distance. Cobblestone the tortoise, untroubled by what others...
    ```
- `G1-02` (form `7`): character 'Giggle the hare' introduced twice within 200 chars — drop the second 'the hare'
    ```
    When Giggle the hare declared the race already won, no one yet knew how long the afternoon would be.

At a moss-covered milestone in the orchard, Giggle the hare sketched a small
wager into the path: whoever guessed the result of `1`
first would win the right to set the next race. Hazel the tortoise...
    ```
- `G1-02` (form `-25`): character 'Filbert the hare' introduced twice within 200 chars — drop the second 'the hare'
    ```
    Filbert the hare was certain she could not lose; Calmway the tortoise was certain of nothing except the next step.

Filbert the hare and Calmway the tortoise stopped at the edge of the woods where someone had
written the integer -82 on a flat stone. Filbert, boasting at every turn, declared
that she...
    ```

#### FORM_DISPLAY_AND_FORM_NOUN

- `G1-02` (form `12345`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    A wager was struck under the elm; the runners were named, the course was paced, and the day was set.

A small audience of forest creatures had gathered on the road to watch
Rush the hare attempt to outwit Plodder the tortoise at reading the REPL.
Plodder, saying very little, pointed to the integer 1...
    ```
- `G1-03` (form `(* 2 1/2)`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    It happened in the orchard, on a morning when the air was kind to swift feet and steady ones alike.

A small audience of forest creatures had gathered at the edge of the orchard to watch
Kit the hare attempt to outwit Tendril the tortoise at reading the REPL.
Tendril, stepping deliberately, pointed ...
    ```
- `G1-04` (form `"42"`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    All this took place at the edge of the meadow, where the dust still keeps the shape of the runners' feet.

A small audience of forest creatures had gathered at the edge of the meadow to watch
Chipmunk the hare attempt to outwit Mossback the tortoise at reading the REPL.
Mossback, stepping deliberate...
    ```
- `G1-05` (form `true`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    Long ago, when wagers were still settled by running rather than talking, two unlikely rivals agreed to a race.

Beaver the hare chalked a wager on a flat stone along the road: whoever
predicted the result of `true` would set the next race's
distance. Plod the tortoise, without complaint, said it wou...
    ```
- `G1-05` (form `true`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    There was once a Hare whose pride matched her feet in speed, and a Tortoise who said nothing about either.

A small audience of forest creatures had gathered near the meadow to watch
Speedwell the hare attempt to outwit Sandstone the tortoise at reading the REPL.
Sandstone, with steady, careful step...
    ```

#### STRING_AS_CHAR_MISCLAIM

- `G1-08` (form `\space`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    In that part of the woods, no one ever expected the slow to outpace the swift, yet the question was always quietly asked.

Halfway through the race, Dell the hare, as if the race were already won, stopped atop the hilltop
and refused to continue until someone could prove what the form
`"harbor"` eva...
    ```
- `G1-08` (form `\space`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    Polecat announced the race in a voice loud enough to wake the owls, and Stoneheart accepted with a nod.

"There is no need to evaluate that," Polecat the hare said, with a smug grin.
"Anyone can see what the character \space comes to." Stoneheart the tortoise, who
in the orchard had grown used to su...
    ```
- `G1-08` (form `\space`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    When Chitter the hare declared the race already won, no one yet knew how long the afternoon would be.

A small audience of forest creatures had gathered in the forest to watch
Chitter the hare attempt to outwit Forest the tortoise at reading the REPL.
Forest, without complaint, pointed to the charac...
    ```
- `G1-08` (form `\T`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    atop the hilltop, where the path bends past the elm, Scurry the hare taunted Marrow the tortoise one too many times.

Scurry the hare chalked a wager on a flat stone near the hilltop: whoever
predicted the result of `"candle"` would set the next race's
distance. Marrow the tortoise, untroubled by wh...
    ```
- `G1-08` (form `\T`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    In that part of the woods, no one ever expected the slow to outpace the swift, yet the question was always quietly asked.

Halfway through the race, Mallow the hare, boasting at every turn, stopped at the edge of the meadow
and refused to continue until someone could prove what the form
`"pebble"` e...
    ```

#### STORY_RESOLUTION_NO_DRAWN

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
- `G1-09` (form `(symbol? "tortoise")`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('coral',), resolution doesn't close the loop)
    ```
    It happened near the garden, on a morning when the air was kind to swift feet and steady ones alike.

"To talk about the form itself rather than evaluating it,"
Sloward the tortoise, saying very little, said, "you label the form with a chalk mark
in front. Quoting tells the runtime: don't cook this,...
    ```
- `G1-10` (form `(+ 1 2) ; sum of one and two`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    ```
    Among the small kingdoms of the meadow, swiftness was a kind of currency, and one creature spent it loudly.

Slowpoke the tortoise had scratched an addition on the trail-stone and, beside it, added a small note after a semicolon explaining what the form computed — a scribe's marginal gloss.

Pip the...
    ```
- `G1-10` (form `(+ 1 2) ; sum of one and two`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    ```
    It happened at the edge of the forest, on a morning when the air was kind to swift feet and steady ones alike.

Slowpoke the tortoise had scratched an addition on the trail-stone and, beside it, added a small note after a semicolon explaining what the form computed — a scribe's marginal gloss.

Pip ...
    ```

#### CLAUSE_STACK_OVERFLOW

- `G1-10` (form `(+ 1 2) ; sum of one and two`): sentence with 5 commas reads as AI-output cadence: 'To add 3 and 2, with a single-semicolon trailing comment, she, with steady, care'
    ```
    It happened at the edge of the forest, on a morning when the air was kind to swift feet and steady ones alike.

Slowpoke the tortoise had scratched an addition on the trail-stone and, beside it, added a small note after a semicolon explaining what the form computed — a scribe's marginal gloss.

Pip ...
    ```
- `G1-11` (form `(+    1    2)`): sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'
    ```
    By the time the dew had lifted, the meadow had gathered to watch the strangest race anyone could remember.

"A form is what's actually there on the page," Ooze the tortoise, stepping deliberately, said, "after the conventions of writing and reading have done
their work. The runtime sees the cleaned-...
    ```
- `G1-12` (form `(+ 2 3)`): sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'
    ```
    All this took place at the edge of the meadow, where the dust still keeps the shape of the runners' feet.

"A form is what's actually there on the page," Meander the tortoise, saying very little, said, "after the conventions of writing and reading have done
their work. The runtime sees the cleaned-u...
    ```
- `G1-12` (form `(* (+ 1 2) 3)`): sentence with 5 commas reads as AI-output cadence: 'Mossback chalked two nested fences on the path: an inner fence holding the plus-'
    ```
    Spring had loosened the soil and the grasses had grown tall enough to brush a passing flank.

Mossback chalked two nested fences on the path: an inner fence holding the plus-mark, 2, and 6, and an outer fence holding the star-mark, the inner fence, and 8. Pip counted the parens and declared the resu...
    ```
- `G1-12` (form `(* (+ 1 2) 3)`): sentence with 5 commas reads as AI-output cadence: 'Mossback chalked two nested fences on the path: an inner fence holding the plus-'
    ```
    It is one thing to have fast legs and another to know how to use them, as the meadow folk would soon be reminded.

Mossback chalked two nested fences on the path: an inner fence holding the plus-mark, 6, and 9, and an outer fence holding the star-mark, the inner fence, and 9. Pip counted the parens ...
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

#### PARAGRAPH_FRAGMENTATION

- `G1-13` (form `(+ 1 2)`): user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    By the time the dew had lifted, the meadow had gathered to watch the strangest race anyone could remember.

Mossback had sorted this morning's acorns into two small heaps beside the trail — one heap of 7 and another of 7.

She needed the running total before deciding whether to carry them all or lea...
    ```
- `G1-13` (form `(+ 7 8)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    Lichen the tortoise had nothing to prove, but Jumper the hare had everything to lose, and the race was on.

Bramble the hare had counted 1 acorns beneath the oak and 1 more under the elm. Both heaps sat in separate leaf-cups at the edge of the path.

Bramble needed the combined count to report back ...
    ```
- `G1-13` (form `(- 20 7)`): user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    There is a kind of pride that runs ahead of itself, and a kind of patience that arrives at its own pace.

Slowpoke the tortoise had stockpiled 15 acorns near the hollow log. During the night, squirrels had carried off 3 of them.

Slowpoke needed the remaining count before deciding whether the stockp...
    ```
- `G4-01` (form `[]`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    The sun rose by the woods, and with it the question of who could outrun whom.

Before the morning's foraging began, Mossback the tortoise set her basket on the path with its pebble row still empty — no pebbles, no contents, ready for whatever the meadow would yield.

Pip the hare wanted to see what ...
    ```
- `G4-14` (form `(empty? [])`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    In that part of the woods, no one ever expected the slow to outpace the swift, yet the question was always quietly asked.

Mossback the tortoise set her pebble row on the path before the foray began. No stones had been placed yet — the row was bare.

Pip the hare needed to confirm the row was truly ...
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

#### NARRATIVE_NUMERAL_HARDCODE

- `G2-02` (form `(< 1 2 3)`): parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    ```
    Spring had loosened the soil and the grasses had grown tall enough to brush a passing flank.

"Watch the basket," Sepia the tortoise, with eyes always on the path, said, gesturing at a small
heap of acorns. "Every operation either adds, takes away, or
combines what's already there — the heap grows o...
    ```
- `G2-02` (form `(< 1 2 3)`): parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    ```
    When Heath the hare declared the race already won, no one yet knew how long the afternoon would be.

Hazel the tortoise, without complaint, laid acorns out on a flat stone at the edge of the orchard, sorting
them into small heaps. "Numbers in Clojure are just like acorns in
heaps," he said: "you can...
    ```
- `G2-02` (form `(< 1 2 3)`): parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    ```
    A path ran from the old oak to the river stone, and on it many a boast had been measured against many a steady step.

"Whatever the heap looks like after the operation,"
Boulderkin the tortoise, untroubled by what others thought, said, "the runtime gives the exact count —
small or large, fraction or...
    ```
- `G2-04` (form `(min 1 2 3)`): parametric example has hard-coded English numeral 'three heaps' in a story slot — the actual draws may differ from this fixed count
    ```
    Long ago, when wagers were still settled by running rather than talking, two unlikely rivals agreed to a race.

Jolt the hare eyed the heap, with great whoops of laughter, and called out a guess
about how many acorns were there without bothering to count.
Whorl the tortoise simply began counting — t...
    ```
- `G2-04` (form `(min 1 2 3)`): parametric example has hard-coded English numeral 'three heaps' in a story slot — the actual draws may differ from this fixed count
    ```
    All this took place at the edge of the orchard, where the dust still keeps the shape of the runners' feet.

Lavender the hare eyed the heap, as if the race were already won, and called out a guess
about how many acorns were there without bothering to count.
Pine the tortoise simply began counting — ...
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

#### HEDGING_NEAR_FORM

- `G6-11` (form `(count ["src" "test" "resources"])`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    Spring had loosened the soil and the grasses had grown tall enough to brush a passing flank.

The wager was set by the meadow: produce the value before the breeze had
turned the next leaf. Bounder the hare, with a smug grin, bolted into a flurry
of guesses, calling out numbers and second-guessing hi...
    ```
- `G11-05` (form `(do "import is a top-of-file ns clause" :studied)`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    Hedgehog announced the race in a voice loud enough to wake the owls, and Sepia accepted with a nod.

The wager was set by the orchard: produce the value before the breeze had
turned the next leaf. Hedgehog the hare, swaggering through the underbrush, bolted into a flurry
of guesses, calling out numb...
    ```
- `G11-10` (form `(do "cljs runs in browsers and Node, with JS interop syntax"`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    Spring had loosened the soil and the grasses had grown tall enough to brush a passing flank.

The wager was set on the road: produce the value before the breeze had
turned the next leaf. Bluebell the hare, swaggering through the underbrush, bolted into a flurry
of guesses, calling out numbers and se...
    ```
- `G11-12` (form `(do "basilisp is a Clojure-like Lisp implemented on Python" `): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    All this took place at the edge of the meadow, where the dust still keeps the shape of the runners' feet.

The wager was set at the edge of the meadow: produce the value before the breeze had
turned the next leaf. Whirlikin the hare, boasting at every turn, bolted into a flurry
of guesses, calling o...
    ```
- `G11-12` (form `(do "basilisp interops with Python via the same dot-syntax c`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    Brook was the first to laugh and the first to boast, and Quietkin simply began to walk.

The wager was set near the hilltop: produce the value before the breeze had
turned the next leaf. Brook the hare, boasting at every turn, bolted into a flurry
of guesses, calling out numbers and second-guessing ...
    ```

#### CONCEPT_PHRASE_COMMA_LIST

- `G9-03` (form `(do (def a (atom 0)) (swap! a inc) @a)`): concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    Galop announced the race in a voice loud enough to wake the owls, and Fen accepted with a nod.

The forest's berry-tally lived on a notebook open on the tree stump in the middle of the meadow. Anyone returning from foraging walked up, read the running total, and added their own count.

Today's tally...
    ```
- `G9-03` (form `(do (def a (atom 0)) (swap! a inc) @a)`): concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    The sun rose in the forest, and with it the question of who could outrun whom.

Skitter the hare, with a smug grin, swiped at the notebook on the stump,
trying to scribble an answer over the page. Deepen the tortoise
caught him firmly: notebooks shared by all the meadow
need careful updates, not sna...
    ```
- `G9-03` (form `(do (def a (atom 0)) (swap! a inc) @a)`): concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    Two creatures of very different gait once agreed that the ground between two stones would settle a long argument.

"The notebook stays put on the stump," Roam the tortoise, stepping deliberately, said,
"so any animal who comes by can read what's on the page right
now. The page changes only when some...
    ```
- `G9-03` (form `(do (def a (atom 10)) (swap! a + 5) @a)`): concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    Skimble the hare was certain he could not lose; Muse the tortoise was certain of nothing except the next step.

"Many animals can come and go past the stump," Muse the tortoise, untroubled by what others thought, said, "and each one's read or write must agree with the others.
The runtime sees to tha...
    ```
- `G9-03` (form `(do (def a (atom 10)) (swap! a + 5) @a)`): concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    The morning was bright and the dust on the road was dry, the sort of weather that invites a contest.

"When I want to update the notebook," Hummock the tortoise, untroubled by what others thought, said,
"I don't pick it up and walk away — I read the page, apply the
change, and write it back, all in ...
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

