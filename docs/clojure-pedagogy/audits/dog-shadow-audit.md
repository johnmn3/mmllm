# dog-shadow curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

### G1-01: Eval as substitution

- examples: 4
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`nil` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-02: Integer numbers

- examples: 6
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 5}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`-25` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`-25` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`12345` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`12345` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`12345` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-03: Ratios

- examples: 5
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 5, 'DOUBLE_NAME_INTRO': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`1/2` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`3/4` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(+ 1/2 1/4)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [DOUBLE_NAME_INTRO] form=`(+ 1/2 1/4)` — character 'Pumpernickel the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(+ 1/2 1/4)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [DOUBLE_NAME_INTRO] form=`(- 1 1/3)` — character 'Whatsit the dog' introduced twice within 200 chars — drop the second 'the dog'

### G1-04: Strings

- examples: 5
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 4, 'DOUBLE_NAME_INTRO': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`"race"` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [DOUBLE_NAME_INTRO] form=`"race"` — character 'Gizmo the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`"slow and steady"` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [DOUBLE_NAME_INTRO] form=`"slow and steady"` — character 'Watcher the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`""` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`"42"` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-05: Booleans

- examples: 6
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 5, 'DOUBLE_NAME_INTRO': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`true` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`true` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(= 1 1)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [DOUBLE_NAME_INTRO] form=`(= 1 2)` — character 'Leo the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(< 3 5)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(> 3 5)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-06: nil

- examples: 5
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2, 'DOUBLE_NAME_INTRO': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(nil? 0)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [DOUBLE_NAME_INTRO] form=`(nil? 0)` — character 'Buttermilk the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(nil? false)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [DOUBLE_NAME_INTRO] form=`(= nil nil)` — character 'Doodle the dog' introduced twice within 200 chars — drop the second 'the dog'

### G1-07: Keywords

- examples: 5
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'DOUBLE_NAME_INTRO': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`:hare` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [DOUBLE_NAME_INTRO] form=`:hare` — character 'Tucker the dog' introduced twice within 200 chars — drop the second 'the dog'

### G1-08: Characters

- examples: 4
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`\T` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [DOUBLE_NAME_INTRO] form=`\T` — character 'Winston the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(char? \h)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(char? \h)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-09: Symbols vs values

- examples: 4
- variety @ n=50: 1.00
- issues: {'ONLY_SHOOK_HEAD_TIC': 1, 'HIGH_LENGTH': 2, 'REPL_TRIPLE_VOICE': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [ONLY_SHOOK_HEAD_TIC] form=`(symbol? 'hare)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [HIGH_LENGTH] form=`(symbol? 42)` — user_msg 209 words
    - [REPL_TRIPLE_VOICE] form=`(symbol? "tortoise")` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [CLAUSE_STACK_OVERFLOW] form=`(= 'hare 'hare)` — sentence with 5 commas reads as AI-output cadence: "The\nreflection in the stream looks like a bone, but the scratch that\nsays 'bone'"
    - [HIGH_LENGTH] form=`(= 'hare 'hare)` — user_msg 209 words
    - [REPL_TRIPLE_VOICE] form=`(= 'hare 'hare)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G1-10: Comments

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'REPL_TRIPLE_VOICE': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(+ 1 2) ;; sum of one and two` — user_msg 203 words
    - [REPL_TRIPLE_VOICE] form=`(+ 1 2) ;; sum of one and two` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [CLAUSE_STACK_OVERFLOW] form=`(+ 1 2) ;; sum of one and two` — sentence with 6 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'

### G1-11: Whitespace doesn't matter

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'THE_FORM_OVERUSE': 1}
    - [HIGH_LENGTH] form=`(+
  1
  2)` — user_msg 211 words
    - [THE_FORM_OVERUSE] form=`(+
  1
  2)` — `the form` appears 5 times in user_msg (template tic — vary references)

### G1-12: Parens group; they don't multiply

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'HIGH_LENGTH': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(+ 2 3)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'
    - [HIGH_LENGTH] form=`(* (+ 1 2) 3)` — user_msg 205 words

### G1-13: First arithmetic call

- examples: 6
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 3, 'REPL_AS_TIME_TRAVELLER': 3, 'NARRATIVE_NUMERAL_HARDCODE': 15, 'RESOLUTION_GENERIC': 2, 'SENTENCE_START_LOWER_PRONOUN': 1}
    - [REPL_TRIPLE_VOICE] form=`(+ 1 2)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_AS_TIME_TRAVELLER] form=`(+ 1 2)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(- 5 3)` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(- 5 3)` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(- 5 3)` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(* 4 5)` — parametric example has hard-coded English numeral 'four piles' in a story slot — the actual draws may differ from this fixed count

### G1-14: Nested call evaluation

- examples: 4
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 2, 'RESOLUTION_GENERIC': 3, 'REPL_AS_TIME_TRAVELLER': 2, 'DOUBLE_NAME_INTRO': 1}
    - [REPL_TRIPLE_VOICE] form=`(+ 1 (* 2 3))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`(* (+ 1 2) (+ 3 4))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [RESOLUTION_GENERIC] form=`(* (+ 1 2) (+ 3 4))` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    - [REPL_AS_TIME_TRAVELLER] form=`(- 100 (* 5 5))` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [RESOLUTION_GENERIC] form=`(- 100 (* 5 5))` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    - [RESOLUTION_GENERIC] form=`(- 100 (* 5 5))` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values

### G1-15: Equality

- examples: 6
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [WRONG_FABLE_LITERAL] form=`(= 1 1)` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [CLAUSE_STACK_OVERFLOW] form=`(= "a" "a")` — sentence with 6 commas reads as AI-output cadence: 'The verdict follows that\nrule exactly, the way a steady current keeps its line."'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(= 1 1 1 1)` — parametric example has hard-coded English numeral 'four numbers' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(= 1 1 1 1)` — parametric example has hard-coded English numeral 'four numbers' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(= 1 1 1 1)` — parametric example has hard-coded English numeral 'four numbers' in a story slot — the actual draws may differ from this fixed count

### G1-16: Numeric predicates

- examples: 6
- variety @ n=50: 1.00
- issues: {'REPL_AS_TIME_TRAVELLER': 2, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'RESOLUTION_GENERIC': 3, 'REPL_TRIPLE_VOICE': 2}
    - [REPL_AS_TIME_TRAVELLER] form=`(zero? 0)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(zero? 5)` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(zero? 5)` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [RESOLUTION_GENERIC] form=`(zero? 5)` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(zero? 5)` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [REPL_AS_TIME_TRAVELLER] form=`(pos? -2)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

### G1-17: Printing vs returning

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [REPL_TRIPLE_VOICE] form=`42` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`42` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`42` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [CLAUSE_STACK_OVERFLOW] form=`(+ 1 2)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'

### G1-18: Errors are safe in the REPL

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1}
    - [REPL_TRIPLE_VOICE] form=`(* 7 6)` — user_msg mentions 'REPL' 4 times — the REPL personification should appear at most twice per record (submit + return)

## Grade 2

### G2-01: Multi-arg arithmetic

- examples: 6
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 12, 'PARAGRAPH_FRAGMENTATION': 1, 'META_FILLER_RESOLUTION': 2, 'REPL_AS_TIME_TRAVELLER': 1, 'RESOLUTION_GENERIC': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(+ 1 2 3 4)` — parametric example has hard-coded English numeral 'four bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(+ 1 2 3 4)` — parametric example has hard-coded English numeral 'four bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(+ 1 2 3 4)` — parametric example has hard-coded English numeral 'four bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(* 2 3 4)` — parametric example has hard-coded English numeral 'three piles' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(* 2 3 4)` — parametric example has hard-coded English numeral 'three piles' in a story slot — the actual draws may differ from this fixed count
    - [PARAGRAPH_FRAGMENTATION] form=`(* 2 3 4)` — user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G2-02: Comparison chains

- examples: 5
- variety @ n=50: 1.00
- issues: {'RESOLUTION_GENERIC': 3, 'REPL_AS_TIME_TRAVELLER': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'GENERIC_RESOLUTION_TAIL': 3}
    - [RESOLUTION_GENERIC] form=`(< 1 2 3)` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    - [REPL_AS_TIME_TRAVELLER] form=`(< 3 2 1)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [RESOLUTION_GENERIC] form=`(< 3 2 1)` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(<= 1 1 2)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(<= 1 1 2)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(<= 1 1 2)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count

### G2-03: not= and = with multiple args

- examples: 5
- variety @ n=50: 1.00
- issues: {'REPL_AS_TIME_TRAVELLER': 4, 'BOOL_LEAK_RESOLUTION': 1, 'NARRATIVE_NUMERAL_HARDCODE': 9, 'CLAUSE_STACK_OVERFLOW': 1}
    - [REPL_AS_TIME_TRAVELLER] form=`(not= 1 2)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [REPL_AS_TIME_TRAVELLER] form=`(not= 1 1)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [BOOL_LEAK_RESOLUTION] form=`(= 1 1 1)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(= 1 1 1)` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(= 1 1 1)` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(= 1 1 1)` — sentence with 5 commas reads as AI-output cadence: 'A reflection lies; a tally does not." To test whether 1, 1, and 1 are all equal,'

### G2-04: min and max

- examples: 5
- variety @ n=50: 1.00
- issues: {'REPL_AS_TIME_TRAVELLER': 1, 'RESOLUTION_GENERIC': 3, 'CLAUSE_STACK_OVERFLOW': 3, 'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [REPL_AS_TIME_TRAVELLER] form=`(min 1 2 3)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [RESOLUTION_GENERIC] form=`(max 1 2 3)` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    - [RESOLUTION_GENERIC] form=`(min 7 3 9 1 5)` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    - [CLAUSE_STACK_OVERFLOW] form=`(min 7 3 9 1 5)` — sentence with 7 commas reads as AI-output cadence: 'A reflection lies; a tally does not." To find the minimum of 4, 3, 6, 0, and 4,\n'
    - [CLAUSE_STACK_OVERFLOW] form=`(min 7 3 9 1 5)` — sentence with 7 commas reads as AI-output cadence: 'A reflection lies; a tally does not." To find the minimum of 9, 7, 0, 6, and 0,\n'
    - [RESOLUTION_GENERIC] form=`(max 7 3 9 1 5)` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values

### G2-05: quot, rem, mod

- examples: 6
- variety @ n=50: 1.00
- issues: {'RESOLUTION_GENERIC': 5, 'REPL_AS_TIME_TRAVELLER': 3}
    - [RESOLUTION_GENERIC] form=`(quot 17 5)` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    - [REPL_AS_TIME_TRAVELLER] form=`(rem 17 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [RESOLUTION_GENERIC] form=`(rem 17 5)` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    - [RESOLUTION_GENERIC] form=`(rem 17 5)` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    - [REPL_AS_TIME_TRAVELLER] form=`(mod 17 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [RESOLUTION_GENERIC] form=`(quot 100 7)` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values

### G2-06: inc and dec

- examples: 5
- variety @ n=50: 1.00
- issues: {'RESOLUTION_GENERIC': 4, 'REPL_AS_TIME_TRAVELLER': 2}
    - [RESOLUTION_GENERIC] form=`(dec 5)` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    - [RESOLUTION_GENERIC] form=`(inc 0)` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    - [RESOLUTION_GENERIC] form=`(dec 0)` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    - [RESOLUTION_GENERIC] form=`(dec 0)` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    - [REPL_AS_TIME_TRAVELLER] form=`(inc -1)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [REPL_AS_TIME_TRAVELLER] form=`(inc -1)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

### G2-07: Absolute value

- examples: 4
- variety @ n=50: 1.00
- issues: {'REPL_AS_TIME_TRAVELLER': 3, 'PARAGRAPH_FRAGMENTATION': 2, 'RESOLUTION_GENERIC': 1}
    - [REPL_AS_TIME_TRAVELLER] form=`(abs 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [REPL_AS_TIME_TRAVELLER] form=`(abs 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [PARAGRAPH_FRAGMENTATION] form=`(abs -5)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [RESOLUTION_GENERIC] form=`(abs -5)` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    - [PARAGRAPH_FRAGMENTATION] form=`(abs 0)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [REPL_AS_TIME_TRAVELLER] form=`(abs (- 3 8))` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

### G2-08: Arithmetic on ratios

- examples: 3
- variety @ n=50: 1.00
- issues: {'PARAGRAPH_FRAGMENTATION': 3, 'REPL_AS_TIME_TRAVELLER': 1, 'DOUBLE_NAME_INTRO': 1, 'RESOLUTION_GENERIC': 1}
    - [PARAGRAPH_FRAGMENTATION] form=`(+ 1/2 1/4)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [REPL_AS_TIME_TRAVELLER] form=`(* 2/3 3/4)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [DOUBLE_NAME_INTRO] form=`(* 2/3 3/4)` — character 'Ebony the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [RESOLUTION_GENERIC] form=`(* 2/3 3/4)` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    - [PARAGRAPH_FRAGMENTATION] form=`(- 1 1/3)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [PARAGRAPH_FRAGMENTATION] form=`(- 1 1/3)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G2-09: Floats vs ints (the / operator)

- examples: 3
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'REPL_AS_TIME_TRAVELLER': 2, 'RESOLUTION_GENERIC': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(/ 10 2)` — parametric example has hard-coded English numeral 'Ten bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(/ 10 2)` — parametric example has hard-coded English numeral 'Ten bones' in a story slot — the actual draws may differ from this fixed count
    - [REPL_AS_TIME_TRAVELLER] form=`(/ 10 2)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(/ 10 2)` — parametric example has hard-coded English numeral 'Ten bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(/ 10 3)` — parametric example has hard-coded English numeral 'three piles' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(/ 10 3)` — parametric example has hard-coded English numeral 'three piles' in a story slot — the actual draws may differ from this fixed count

### G2-10: Powers via repeated multiplication

- examples: 4
- variety @ n=50: 1.00
- issues: {'RESOLUTION_GENERIC': 2, 'PARAGRAPH_FRAGMENTATION': 1}
    - [RESOLUTION_GENERIC] form=`(* 3 3 3 3)` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    - [PARAGRAPH_FRAGMENTATION] form=`(* 10 10)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [RESOLUTION_GENERIC] form=`(* 10 10)` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values

### G2-11: String concatenation with str

- examples: 4
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4}
    - [CLAUSE_STACK_OVERFLOW] form=`(str 42)` — sentence with 5 commas reads as AI-output cadence: 'Concat two strips\ntogether, and the marks are spliced; cut a substring out, and\n'
    - [CLAUSE_STACK_OVERFLOW] form=`(str 42)` — sentence with 5 commas reads as AI-output cadence: 'Concat two strips\ntogether, and the marks are spliced; cut a substring out, and\n'
    - [CLAUSE_STACK_OVERFLOW] form=`(str 1 "+" 2 "=" 3)` — sentence with 9 commas reads as AI-output cadence: 'Concat two strips\ntogether, and the marks are spliced; cut a substring out, and\n'
    - [CLAUSE_STACK_OVERFLOW] form=`(str 1 "+" 2 "=" 3)` — sentence with 8 commas reads as AI-output cadence: 'Cut from one position to another and\nyou get a smaller strip, the original untou'

### G2-13: and / or — short circuit, return values

- examples: 6
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 1, 'CLAUSE_STACK_OVERFLOW': 3, 'DOUBLE_NAME_INTRO': 1}
    - [BOOL_LEAK_RESOLUTION] form=`(and true false)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [CLAUSE_STACK_OVERFLOW] form=`(and true false)` — sentence with 6 commas reads as AI-output cadence: 'The verdict follows that\nrule exactly, the way a steady current keeps its line."'
    - [DOUBLE_NAME_INTRO] form=`(and 1 2 3)` — character 'Pearl the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(and 1 2 3)` — sentence with 6 commas reads as AI-output cadence: 'To apply and to 6, 9, and 2,\nshe composed the logical and, submitted the form,\na'
    - [CLAUSE_STACK_OVERFLOW] form=`(or nil false 5)` — sentence with 6 commas reads as AI-output cadence: 'To apply or to nil, false, and 1,\nshe composed the logical or, submitted the for'

### G2-14: not — turning truthy to false

- examples: 5
- variety @ n=50: 1.00
- issues: {'PARAGRAPH_FRAGMENTATION': 3, 'CLAUSE_STACK_OVERFLOW': 2, 'DOUBLE_NAME_INTRO': 1}
    - [PARAGRAPH_FRAGMENTATION] form=`(not true)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [CLAUSE_STACK_OVERFLOW] form=`(not false)` — sentence with 6 commas reads as AI-output cadence: 'The verdict follows that\nrule exactly, the way a steady current keeps its line."'
    - [PARAGRAPH_FRAGMENTATION] form=`(not false)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [PARAGRAPH_FRAGMENTATION] form=`(not nil)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [CLAUSE_STACK_OVERFLOW] form=`(not 0)` — sentence with 6 commas reads as AI-output cadence: 'The verdict follows that\nrule exactly, the way a steady current keeps its line."'
    - [DOUBLE_NAME_INTRO] form=`(not 0)` — character 'Max the dog' introduced twice within 200 chars — drop the second 'the dog'

### G2-15: Falsey values: only false and nil

- examples: 4
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1}
    - [WRONG_FABLE_LITERAL] form=`(if 0 1 0)` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg

### G2-16: Truthy 0 and empty string

- examples: 4
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(boolean "")` — sentence with 6 commas reads as AI-output cadence: 'The verdict follows that\nrule exactly, the way a steady current keeps its line."'
    - [CLAUSE_STACK_OVERFLOW] form=`(boolean "")` — sentence with 6 commas reads as AI-output cadence: 'The verdict follows that\nrule exactly, the way a steady current keeps its line."'

### G2-18: Quoting symbols

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 5, 'ONLY_SHOOK_HEAD_TIC': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(= (quote tortoise) 'tortoise)` — sentence with 5 commas reads as AI-output cadence: "Quoting tells the runtime: don't run this, just hand it\nback as the shape it is."
    - [CLAUSE_STACK_OVERFLOW] form=`(= (quote tortoise) 'tortoise)` — sentence with 5 commas reads as AI-output cadence: "Quoting tells the runtime: don't run this, just hand it\nback as the shape it is."
    - [CLAUSE_STACK_OVERFLOW] form=`(= (quote tortoise) 'tortoise)` — sentence with 5 commas reads as AI-output cadence: "The\nreflection in the stream looks like a bone, but the scratch that\nsays 'bone'"
    - [CLAUSE_STACK_OVERFLOW] form=`(count '(1 2 3))` — sentence with 6 commas reads as AI-output cadence: "Quoting tells the runtime: don't run this, just hand it\nback as the shape it is."
    - [CLAUSE_STACK_OVERFLOW] form=`(count '(1 2 3))` — sentence with 5 commas reads as AI-output cadence: 'To\ncount the elements in a quoted list of the integers 1, 2, and 3, he composed '
    - [ONLY_SHOOK_HEAD_TIC] form=`(count '(1 2 3))` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

### G2-19: Auto-promotion to bigint

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 2, 'RESOLUTION_REPL_DOUBLED': 3, 'REPL_AS_TIME_TRAVELLER': 2, 'DOUBLE_NAME_INTRO': 1, 'RESOLUTION_GENERIC': 2}
    - [REPL_TRIPLE_VOICE] form=`(* 1000000 1000000)` — user_msg mentions 'REPL' 4 times — the REPL personification should appear at most twice per record (submit + return)
    - [RESOLUTION_REPL_DOUBLED] form=`(* 1000000 1000000)` — story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat
    - [REPL_AS_TIME_TRAVELLER] form=`(* 1000000 1000000)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [DOUBLE_NAME_INTRO] form=`(* 1000000 1000000)` — character 'Inky the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [RESOLUTION_REPL_DOUBLED] form=`(* 1000000 1000000)` — story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat
    - [REPL_AS_TIME_TRAVELLER] form=`(* 1000000 1000000)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

### G2-20: Counting

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 5, 'HIGH_LENGTH': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3])` — sentence with 9 commas reads as AI-output cadence: 'The runtime does this for any collection — vector, list, map,\nstring." To count '
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3])` — sentence with 9 commas reads as AI-output cadence: 'The runtime does this for any collection — vector, list, map,\nstring." To count '
    - [HIGH_LENGTH] form=`(count [1 2 3])` — user_msg 210 words
    - [CLAUSE_STACK_OVERFLOW] form=`(count "hello")` — sentence with 7 commas reads as AI-output cadence: 'The runtime does this for any collection — vector, list, map,\nstring." To count '
    - [CLAUSE_STACK_OVERFLOW] form=`(count [])` — sentence with 7 commas reads as AI-output cadence: 'The runtime does this for any collection — vector, list, map,\nstring." To count '
    - [CLAUSE_STACK_OVERFLOW] form=`(count [])` — sentence with 7 commas reads as AI-output cadence: 'The runtime does this for any collection — vector, list, map,\nstring." To count '

### G2-21: String length and substring

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(count "tortoise")` — sentence with 5 commas reads as AI-output cadence: 'Concat two strips\ntogether, and the marks are spliced; cut a substring out, and\n'
    - [CLAUSE_STACK_OVERFLOW] form=`(count "tortoise")` — sentence with 5 commas reads as AI-output cadence: 'Concat two strips\ntogether, and the marks are spliced; cut a substring out, and\n'

### G2-22: Compose pure arithmetic (multi-step calculation)

- examples: 3
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'REPL_AS_TIME_TRAVELLER': 2}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(- (* 5 4) 7)` — parametric example has hard-coded English numeral 'four piles' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(- (* 5 4) 7)` — parametric example has hard-coded English numeral 'four piles' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(- (* 5 4) 7)` — parametric example has hard-coded English numeral 'four piles' in a story slot — the actual draws may differ from this fixed count
    - [REPL_AS_TIME_TRAVELLER] form=`(quot (+ 100 50) 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [REPL_AS_TIME_TRAVELLER] form=`(quot (+ 100 50) 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

## Grade 3

### G3-03: let — local binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 3}
    - [HIGH_LENGTH] form=`(let [x 3] (+ x 1))` — user_msg 225 words
    - [HIGH_LENGTH] form=`(let [n 10] (* n n))` — user_msg 223 words
    - [HIGH_LENGTH] form=`(let [a 5] a)` — user_msg 227 words

### G3-04: let — multi-binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(let [x 5 y 3] (- x y))` — user_msg 209 words
    - [HIGH_LENGTH] form=`(let [x 5 y 3] (- x y))` — user_msg 208 words
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [a 2 b 3 c 4] (+ a b c))` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [a 2 b 3 c 4] (+ a b c))` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a 2 b 3 c 4] (+ a b c))` — sentence with 7 commas reads as AI-output cadence: 'Tracker the dog, with even breath and steady step,\nheld his grip steady and did '
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [a 2 b 3 c 4] (+ a b c))` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count

### G3-05: let — shadowing outer def

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def x 10) (let [x 99] x))` — sentence with 5 commas reads as AI-output cadence: 'Howler the dog, untroubled by what others thought,\nheld his grip steady and did '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def x 10) (let [x 99] x) x)` — sentence with 5 commas reads as AI-output cadence: 'Step past the\nform\'s edge and the mouth is empty again." To define x, shadow it '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def x 10) (let [x 99] x) x)` — sentence with 5 commas reads as AI-output cadence: 'Step past the\nform\'s edge and the mouth is empty again." To define x, shadow it '

### G3-06: let — binding can reference prior

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'CLAUSE_STACK_OVERFLOW': 2, 'HIGH_LENGTH': 4}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [a 5 b (* a 2)] b)` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a 5 b (* a 2)] b)` — sentence with 5 commas reads as AI-output cadence: 'Winston the dog, with hard, hungry eyes,\nhad already let her jaws fall open at a'
    - [HIGH_LENGTH] form=`(let [a 5 b (* a 2)] b)` — user_msg 240 words
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [a 5 b (* a 2)] b)` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [HIGH_LENGTH] form=`(let [a 5 b (* a 2)] b)` — user_msg 242 words
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [a 5 b (* a 2)] b)` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count

### G3-07: fn — anonymous function

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`((fn [a b] (* a b)) 3 4)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G3-08: fn — multi-arg

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`((fn [a b c] (+ a b c)) 1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'To create an anonymous function with three parameters that adds them and apply i'
    - [CLAUSE_STACK_OVERFLOW] form=`((fn [a b c] (+ a b c)) 1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'To create an anonymous function with three parameters that adds them and apply i'

### G3-09: defn — shorthand

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 2, 'RESOLUTION_REPL_DOUBLED': 3, 'HIGH_LENGTH': 1, 'REPL_TRIPLE_VOICE': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — sentence with 6 commas reads as AI-output cadence: 'To define a function add3 that adds three arguments, then call it with 4, 8, and'
    - [RESOLUTION_REPL_DOUBLED] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat
    - [HIGH_LENGTH] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — user_msg 241 words
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [REPL_TRIPLE_VOICE] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 1.00
- issues: {'PARAGRAPH_FRAGMENTATION': 1, 'CONCEPT_AS_VERB': 3}
    - [PARAGRAPH_FRAGMENTATION] form=`(#(+ % 1) 5)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [CONCEPT_AS_VERB] form=`(#(+ % 1) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(#(+ % 1) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(#(* %1 %2) 3 4)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G3-11: Substitution rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`((fn [x] (* x x)) 6)` — user_msg 203 words

### G3-12: Scope vs namespace

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def g 5) (let [g 99] (+ g 1)))` — sentence with 6 commas reads as AI-output cadence: 'To define g at the top level, shadow it in a let with a different value, and com'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def g 5) (let [g 99] (+ g 1)))` — sentence with 5 commas reads as AI-output cadence: 'The next dog along the bank\nreads the freshest scratch — whatever the latest mar'

### G3-13: fn body returns last form

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [HIGH_LENGTH] form=`((fn [x] x x x 99) 1)` — user_msg 240 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] x x x 99) 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] x x x 99) 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] x x x 99) 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99',), resolution doesn't close the loop)

### G3-14: do form

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(do 1 2 3)` — user_msg 213 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do 1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'

### G3-15: Side-effects in body

- examples: 1
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'HIGH_LENGTH': 1, 'SENTENCE_START_LOWER_PRONOUN': 1}
    - [WRONG_FABLE_LITERAL] form=`(do (println "hi") 42)` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [HIGH_LENGTH] form=`(do (println "hi") 42)` — user_msg 215 words
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do (println "hi") 42)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation

### G3-18: When to name vs inline

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'THE_FORM_OVERUSE': 1}
    - [HIGH_LENGTH] form=`(let [n 5] (* n n n))` — user_msg 220 words
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(* 5 5 5)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(* 5 5 5)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [THE_FORM_OVERUSE] form=`(* 5 5 5)` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(* 5 5 5)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count

## Grade 4

### G4-01: Vector literal

- examples: 3
- variety @ n=50: 1.00
- issues: {'PARAMETRIC_LITERAL_NUMERALS': 3, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'REPL_TRIPLE_VOICE': 2}
    - [PARAMETRIC_LITERAL_NUMERALS] form=`[1 2 3]` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [NARRATIVE_NUMERAL_HARDCODE] form=`[1 2 3]` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [PARAMETRIC_LITERAL_NUMERALS] form=`[1 2 3]` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [NARRATIVE_NUMERAL_HARDCODE] form=`[1 2 3]` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [PARAMETRIC_LITERAL_NUMERALS] form=`[1 2 3]` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [NARRATIVE_NUMERAL_HARDCODE] form=`[1 2 3]` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count

### G4-02: nth — vector access

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'REPL_TRIPLE_VOICE': 2}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 0)` — parametric example has hard-coded English numeral 'three bone' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 0)` — parametric example has hard-coded English numeral 'three bone' in a story slot — the actual draws may differ from this fixed count
    - [REPL_TRIPLE_VOICE] form=`(nth [10 20 30] 0)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 0)` — parametric example has hard-coded English numeral 'three bone' in a story slot — the actual draws may differ from this fixed count
    - [REPL_TRIPLE_VOICE] form=`(nth [10 20 30] 0)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 2)` — parametric example has hard-coded English numeral 'three piles' in a story slot — the actual draws may differ from this fixed count

### G4-03: conj — append to vector

- examples: 2
- variety @ n=50: 1.00
- issues: {'PARAMETRIC_LITERAL_NUMERALS': 3}
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(conj [1 2] 3)` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(conj [1 2] 3)` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(conj [1 2] 3)` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces

### G4-04: List literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'HANGING_FORM_THAT': 1, 'PARAGRAPH_FRAGMENTATION': 1, 'REPL_TRIPLE_VOICE': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`'(1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'To create a list containing 1, 2, and 3\nproperly, he wrote a list literal carefu'
    - [HANGING_FORM_THAT] form=`'()` — 'form that <noun>' rendered without a verb — template should be 'form for {concept_phrase}'
    - [PARAGRAPH_FRAGMENTATION] form=`'()` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G4-05: cons — prepend to seq

- examples: 1
- variety @ n=50: 1.00
- issues: {'PARAMETRIC_LITERAL_NUMERALS': 3, 'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(cons 0 '(1 2 3))` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(cons 0 '(1 2 3))` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(cons 0 '(1 2 3))` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(cons 0 '(1 2 3))` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(cons 0 '(1 2 3))` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(cons 0 '(1 2 3))` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count

### G4-08: assoc — map update

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1}
    - [REPL_TRIPLE_VOICE] form=`(assoc {:a 1} :a 99)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G4-10: keys and vals

- examples: 1
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [REPL_TRIPLE_VOICE] form=`(count (keys {:a 1 :b 2 :c 3}))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [CLAUSE_STACK_OVERFLOW] form=`(count (keys {:a 1 :b 2 :c 3}))` — sentence with 5 commas reads as AI-output cadence: 'To count how many keys are in a map binding :a, :b, and :c\nproperly, he wrote co'

### G4-11: Set literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'PARAGRAPH_FRAGMENTATION': 1, 'REPL_TRIPLE_VOICE': 1}
    - [PARAGRAPH_FRAGMENTATION] form=`(count #{1 1 1})` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [REPL_TRIPLE_VOICE] form=`(count #{1 1 1})` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G4-12: Set membership

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'CLAUSE_STACK_OVERFLOW': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(contains? #{1 2 3} 2)` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(contains? #{1 2 3} 2)` — sentence with 5 commas reads as AI-output cadence: 'To check whether 2 is a member of a set containing 1, 2, and 3\nproperly, he wrot'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(contains? #{1 2 3} 2)` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(contains? #{1 2 3} 2)` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(contains? #{1 2 3} 4)` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(contains? #{1 2 3} 4)` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count

### G4-13: count — universal

- examples: 4
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'NUMERAL_LIST_IN_GOAL': 3, 'REPL_TRIPLE_VOICE': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count [1 2 3 4 5])` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [NUMERAL_LIST_IN_GOAL] form=`(count [1 2 3 4 5])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [REPL_TRIPLE_VOICE] form=`(count [1 2 3 4 5])` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count [1 2 3 4 5])` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [NUMERAL_LIST_IN_GOAL] form=`(count [1 2 3 4 5])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count [1 2 3 4 5])` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count

### G4-14: empty?

- examples: 3
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 3, 'PARAGRAPH_FRAGMENTATION': 2}
    - [REPL_TRIPLE_VOICE] form=`(empty? [])` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [PARAGRAPH_FRAGMENTATION] form=`(empty? [1])` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [REPL_TRIPLE_VOICE] form=`(empty? [1])` — user_msg mentions 'REPL' 4 times — the REPL personification should appear at most twice per record (submit + return)
    - [PARAGRAPH_FRAGMENTATION] form=`(empty? [1])` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [REPL_TRIPLE_VOICE] form=`(empty? [1])` — user_msg mentions 'REPL' 4 times — the REPL personification should appear at most twice per record (submit + return)

### G4-15: first, rest, last

- examples: 3
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'NARRATIVE_NUMERAL_HARDCODE': 9, 'REPL_TRIPLE_VOICE': 2, 'CLAUSE_STACK_OVERFLOW': 2}
    - [WRONG_FABLE_LITERAL] form=`(first [10 20 30])` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(first [10 20 30])` — parametric example has hard-coded English numeral 'three bone' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(first [10 20 30])` — parametric example has hard-coded English numeral 'three bone' in a story slot — the actual draws may differ from this fixed count
    - [REPL_TRIPLE_VOICE] form=`(first [10 20 30])` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(first [10 20 30])` — parametric example has hard-coded English numeral 'three bone' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(last [10 20 30])` — parametric example has hard-coded English numeral 'three heaps' in a story slot — the actual draws may differ from this fixed count

### G4-16: into and conj on collections

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(into [] '(1 2 3))` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(into [] '(1 2 3))` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(into [] '(1 2 3))` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] '(1 2 3))` — sentence with 6 commas reads as AI-output cadence: 'The receiver is patient; the gap is exact." To\nconvert a list containing 1, 2, a'

### G4-19: range and seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'REPL_TRIPLE_VOICE': 3, 'CLAUSE_STACK_OVERFLOW': 2}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (range 5))` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [REPL_TRIPLE_VOICE] form=`(count (range 5))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [CLAUSE_STACK_OVERFLOW] form=`(count (range 5))` — sentence with 6 commas reads as AI-output cadence: 'The range is a promise of five bones (0, 1, 2, 3, 4), and count consumes that pr'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (range 5))` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (range 5))` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [REPL_TRIPLE_VOICE] form=`(count (range 5))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G4-20: Collection vs sequence

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(count (seq [1 2 3]))` — sentence with 5 commas reads as AI-output cadence: 'To convert a vector containing 1, 2, and 3 to a sequence and count its elements\n'
    - [CLAUSE_STACK_OVERFLOW] form=`(count (seq [1 2 3]))` — sentence with 5 commas reads as AI-output cadence: 'To convert a vector containing 1, 2, and 3 to a sequence and count its elements\n'

## Grade 5

### G5-01: if

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(if true :a :b)` — sentence with 5 commas reads as AI-output cadence: 'The runtime checks the\ncondition, walks the right arm, and the unrun arm is just'
    - [CLAUSE_STACK_OVERFLOW] form=`(if false :a :b)` — sentence with 5 commas reads as AI-output cadence: 'The runtime checks the\ncondition, walks the right arm, and the unrun arm is just'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(if (> 5 3) :a :b)` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(if (> 5 3) :a :b)` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(if (> 5 3) :a :b)` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count

### G5-02: if as expression

- examples: 1
- variety @ n=50: 1.00
- issues: {'RESOLUTION_REPL_DOUBLED': 3, 'HIGH_LENGTH': 1, 'REPL_TRIPLE_VOICE': 1}
    - [RESOLUTION_REPL_DOUBLED] form=`(+ 1 (if true 10 20))` — story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat
    - [HIGH_LENGTH] form=`(+ 1 (if true 10 20))` — user_msg 222 words
    - [REPL_TRIPLE_VOICE] form=`(+ 1 (if true 10 20))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [RESOLUTION_REPL_DOUBLED] form=`(+ 1 (if true 10 20))` — story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat
    - [RESOLUTION_REPL_DOUBLED] form=`(+ 1 (if true 10 20))` — story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat

### G5-04: cond

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — sentence with 5 commas reads as AI-output cadence: 'Whatever the condition evaluates to, that\ndecides." To walk three condition-ston'

### G5-05: cond — :else

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(cond false :a false :b :else :c)` — sentence with 5 commas reads as AI-output cadence: 'The runtime checks the\ncondition, walks the right arm, and the unrun arm is just'

### G5-06: case

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(case 2 1 :one 2 :two 3 :three :default)` — sentence with 5 commas reads as AI-output cadence: 'The runtime checks the\ncondition, walks the right arm, and the unrun arm is just'
    - [CLAUSE_STACK_OVERFLOW] form=`(case 99 1 :one 2 :two :default)` — sentence with 5 commas reads as AI-output cadence: 'The runtime checks the\ncondition, walks the right arm, and the unrun arm is just'
    - [CLAUSE_STACK_OVERFLOW] form=`(case 99 1 :one 2 :two :default)` — sentence with 5 commas reads as AI-output cadence: 'The runtime checks the\ncondition, walks the right arm, and the unrun arm is just'

### G5-07: and / or as control flow

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(or nil false :found)` — user_msg 204 words
    - [CLAUSE_STACK_OVERFLOW] form=`(or nil false :found)` — sentence with 6 commas reads as AI-output cadence: 'The REPL let the crossing-conditions decide:\n\nThe REPL walked the first gate, fo'

### G5-08: not

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(not (> 1 2))` — sentence with 6 commas reads as AI-output cadence: 'The verdict follows that\nrule exactly, the way a steady current keeps its line."'

### G5-10: map

- examples: 2
- variety @ n=50: 1.00
- issues: {'COLLECTION_LEAK': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'NUMERAL_LIST_IN_GOAL': 3}
    - [COLLECTION_LEAK] form=`(map inc [1 2 3])` — elements of expected [2, 3, 4] appear comma-separated in user_msg (collection answer leak)
    - [CLAUSE_STACK_OVERFLOW] form=`(map inc [1 2 3])` — sentence with 7 commas reads as AI-output cadence: 'Zoomer the dog shook\nhis head and went on with the work: to pour the vector cont'
    - [NUMERAL_LIST_IN_GOAL] form=`(map #(* % %) [1 2 3 4])` — goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(map #(* % %) [1 2 3 4])` — goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(map #(* % %) [1 2 3 4])` — goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(map #(* % %) [1 2 3 4])` — sentence with 8 commas reads as AI-output cadence: 'Leaper the dog shook\nhis head and went on with the work: to apply a squaring ope'

### G5-11: filter

- examples: 2
- variety @ n=50: 1.00
- issues: {'NUMERAL_LIST_IN_GOAL': 6, 'CLAUSE_STACK_OVERFLOW': 2, 'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [NUMERAL_LIST_IN_GOAL] form=`(filter even? [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(filter even? [1 2 3 4])` — sentence with 7 commas reads as AI-output cadence: 'The receiver is patient; the gap is exact." To\nkeep the even elements from the v'
    - [NUMERAL_LIST_IN_GOAL] form=`(filter even? [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(filter even? [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(filter pos? [-2 -1 0 1 2])` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [NUMERAL_LIST_IN_GOAL] form=`(filter pos? [-2 -1 0 1 2])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing

### G5-12: reduce

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'NUMERAL_LIST_IN_GOAL': 9, 'CLAUSE_STACK_OVERFLOW': 5}
    - [HIGH_LENGTH] form=`(reduce + [1 2 3 4])` — user_msg 226 words
    - [NUMERAL_LIST_IN_GOAL] form=`(reduce + [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [HIGH_LENGTH] form=`(reduce + [1 2 3 4])` — user_msg 218 words
    - [NUMERAL_LIST_IN_GOAL] form=`(reduce + [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(reduce + [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + [1 2 3 4])` — sentence with 10 commas reads as AI-output cadence: 'The runtime does this for any collection — vector, list, map,\nstring." To walk t'

### G5-13: reduce with init

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'HIGH_LENGTH': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + 100 [1 2 3])` — sentence with 9 commas reads as AI-output cadence: 'The runtime does this for any collection — vector, list, map,\nstring." To fold +'
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + 100 [1 2 3])` — sentence with 9 commas reads as AI-output cadence: 'The runtime does this for any collection — vector, list, map,\nstring." To fold +'
    - [HIGH_LENGTH] form=`(reduce + 0 [])` — user_msg 212 words

### G5-14: apply

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 3, 'NARRATIVE_NUMERAL_HARDCODE': 6, 'NUMERAL_LIST_IN_GOAL': 6, 'CLAUSE_STACK_OVERFLOW': 4}
    - [HIGH_LENGTH] form=`(apply + [1 2 3 4])` — user_msg 230 words
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply + [1 2 3 4])` — parametric example has hard-coded English numeral 'four bones' in a story slot — the actual draws may differ from this fixed count
    - [NUMERAL_LIST_IN_GOAL] form=`(apply + [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(apply + [1 2 3 4])` — sentence with 6 commas reads as AI-output cadence: 'To apply + to the elements of the vector containing 1, 2, 3, and 4, he, with the'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply + [1 2 3 4])` — parametric example has hard-coded English numeral 'four bones' in a story slot — the actual draws may differ from this fixed count
    - [NUMERAL_LIST_IN_GOAL] form=`(apply + [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing

### G5-15: comp

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'HIGH_LENGTH': 1, 'ANSWER_LEAK': 1, 'CONCEPT_AS_VERB': 1}
    - [WRONG_FABLE_LITERAL] form=`((comp inc inc) 5)` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [HIGH_LENGTH] form=`((comp inc inc) 5)` — user_msg 211 words
    - [ANSWER_LEAK] form=`((comp inc inc) 5)` — answer 7 in narrative
    - [CONCEPT_AS_VERB] form=`((comp str inc) 9)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G5-16: partial

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`((partial + 10) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G5-18: some

- examples: 2
- variety @ n=50: 1.00
- issues: {'NUMERAL_LIST_IN_GOAL': 3, 'HIGH_LENGTH': 2, 'PREDICATE_QUESTION_COLLISION': 2}
    - [NUMERAL_LIST_IN_GOAL] form=`(some even? [1 3 5 8 7])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(some even? [1 3 5 8 7])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(some even? [1 3 5 8 7])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [HIGH_LENGTH] form=`(some neg? [1 2 3])` — user_msg 205 words
    - [PREDICATE_QUESTION_COLLISION] form=`(some neg? [1 2 3])` — predicate-suffix ``?`` collides with the question framing's trailing ``?`` or ``.``
    - [HIGH_LENGTH] form=`(some neg? [1 2 3])` — user_msg 206 words

### G5-19: every?

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'PREDICATE_QUESTION_COLLISION': 1}
    - [HIGH_LENGTH] form=`(every? pos? [1 2 3])` — user_msg 202 words
    - [PREDICATE_QUESTION_COLLISION] form=`(every? pos? [1 2 3])` — predicate-suffix ``?`` collides with the question framing's trailing ``?`` or ``.``

### G5-20: take and drop

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'NUMERAL_LIST_IN_GOAL': 6, 'CLAUSE_STACK_OVERFLOW': 3, 'STORY_SLOT_NOUN_REPEAT': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(take 3 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [NUMERAL_LIST_IN_GOAL] form=`(take 3 [10 20 30 40 50])` — goal_text contains 6 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(take 3 [10 20 30 40 50])` — sentence with 8 commas reads as AI-output cadence: 'Zoomer the dog shook\nhis head and went on with the work: to take the first 3 ele'
    - [STORY_SLOT_NOUN_REPEAT] form=`(take 3 [10 20 30 40 50])` — the noun 'the first three' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(take 3 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [NUMERAL_LIST_IN_GOAL] form=`(take 3 [10 20 30 40 50])` — goal_text contains 6 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing

### G5-21: distinct and sort

- examples: 2
- variety @ n=50: 1.00
- issues: {'NUMERAL_LIST_IN_GOAL': 3, 'CLAUSE_STACK_OVERFLOW': 5}
    - [NUMERAL_LIST_IN_GOAL] form=`(distinct [1 1 2 3 3 4])` — goal_text contains 6 numerals across 5 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(distinct [1 1 2 3 3 4])` — sentence with 9 commas reads as AI-output cadence: 'The receiver is patient; the gap is exact." To\nremove duplicate elements from th'
    - [NUMERAL_LIST_IN_GOAL] form=`(distinct [1 1 2 3 3 4])` — goal_text contains 6 numerals across 5 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(distinct [1 1 2 3 3 4])` — sentence with 9 commas reads as AI-output cadence: 'Marley the dog shook\nhis head and went on with the work: to remove duplicate ele'
    - [NUMERAL_LIST_IN_GOAL] form=`(distinct [1 1 2 3 3 4])` — goal_text contains 6 numerals across 5 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(distinct [1 1 2 3 3 4])` — sentence with 5 commas reads as AI-output cadence: 'What Clojure form computes the sequence produced by passing 1, 1, 2, 3, 3, 4 thr'

### G5-22: recur — first taste

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 3, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [HIGH_LENGTH] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — user_msg 220 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — user_msg 217 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — user_msg 215 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)

## Grade 6

### G6-01: Namespace as file

- examples: 3
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'DOUBLE_NAME_INTRO': 1}
    - [WRONG_FABLE_LITERAL] form=`(name 'clojure.string)` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [DOUBLE_NAME_INTRO] form=`(symbol? 'tortoise.race)` — character 'Apricot the dog' introduced twice within 200 chars — drop the second 'the dog'

### G6-09: Loading order

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 2}
    - [DOUBLE_NAME_INTRO] form=`(let [a 1 b (+ a 1)] (+ a b))` — character 'Peach the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a 1 b (+ a 1)] (+ a b))` — sentence with 6 commas reads as AI-output cadence: 'To bind a to 1, bind b to a plus 1, then return the sum of a and b, the\nscratch '
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a 1 b (+ a 1)] (+ a b))` — sentence with 5 commas reads as AI-output cadence: 'The next dog along the bank\nreads the freshest scratch — whatever the latest mar'

### G6-10: Leiningen and deps.edn

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HEDGING_NEAR_FORM] form=`(:deps {:deps {:a 1 :b 2}})` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(:deps {:deps {:a 1 :b 2}})` — sentence with 5 commas reads as AI-output cadence: 'Pewter the dog, with eyes always on the path, who had simply walked to a flat st'

### G6-12: Multiple files in one project

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`(count ['race.tortoise 'race.hare 'race.shared])` — character 'Topsy the dog' introduced twice within 200 chars — drop the second 'the dog'

### G6-14: Import for host classes

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_SLOT_NOUN_REPEAT': 3}
    - [STORY_SLOT_NOUN_REPEAT] form=`(name 'java.util.Map)` — the noun 'the kennel-master' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(name 'java.util.Map)` — the noun 'the kennel-master' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(name 'java.util.Map)` — the noun 'the kennel-master' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats

### G6-15: Namespace meta

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'REPL_TRIPLE_VOICE': 2, 'HIGH_LENGTH': 1}
    - [WRONG_FABLE_LITERAL] form=`(:doc (meta '\{:doc "steady wins"\} race))` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [REPL_TRIPLE_VOICE] form=`(:doc (meta '\{:doc "steady wins"\} race))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [HIGH_LENGTH] form=`(:doc (meta '\{:doc "steady wins"\} race))` — user_msg 220 words
    - [REPL_TRIPLE_VOICE] form=`(:author (meta '\{:author "Aesop"\} race))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

## Grade 7

### G7-01: throw

- examples: 1
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1}
    - [REPL_TRIPLE_VOICE] form=`(try (throw (Exception. "bad")) (catch Exception e` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G7-02: try / catch

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1}
    - [REPL_TRIPLE_VOICE] form=`(try (/ 1 0) (catch Exception e -1))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G7-03: try / finally

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1}
    - [REPL_TRIPLE_VOICE] form=`(try 7 (finally (prn :cleanup)))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G7-05: nil punning

- examples: 4
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1}
    - [REPL_TRIPLE_VOICE] form=`(first nil)` — user_msg mentions 'REPL' 4 times — the REPL personification should appear at most twice per record (submit + return)

### G7-07: assert

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — sentence with 5 commas reads as AI-output cadence: 'To\nassert that 7 equals 9, catch the failure, and return a numeric code required'
    - [CLAUSE_STACK_OVERFLOW] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — sentence with 5 commas reads as AI-output cadence: 'The REPL is forgiving in a\nway that a real crossing is not." To assert that 0 eq'

### G7-08: prn and pprint

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1, 'DOUBLE_NAME_INTRO': 1}
    - [REPL_TRIPLE_VOICE] form=`(with-out-str (prn 42))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [DOUBLE_NAME_INTRO] form=`(with-out-str (prn :hare))` — character 'Ebony the dog' introduced twice within 200 chars — drop the second 'the dog'

### G7-09: tap>

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 4}
    - [REPL_TRIPLE_VOICE] form=`(tap> :hello)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`(tap> 42)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`(tap> 42)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`(tap> 42)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G7-10: doc and source

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(:doc (meta '^{:doc "adds two"} plus))` — sentence with 5 commas reads as AI-output cadence: 'To extract the :doc metadata value from a symbol, she, neither restless nor wear'

### G7-11: Reading stack traces

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)

### G7-12: slurp and spit

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'REPL_TRIPLE_VOICE': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(count "hare
tortoise
")` — sentence with 5 commas reads as AI-output cadence: 'Message-bones are how the two meet — a\nvalue crosses out and becomes scratches o'
    - [CLAUSE_STACK_OVERFLOW] form=`(count "hare
tortoise
")` — sentence with 5 commas reads as AI-output cadence: 'To count every character in a two-line string ending each line with a newline-ma'
    - [REPL_TRIPLE_VOICE] form=`(count "hare
tortoise
")` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`(clojure.string/split "a\nb\nc" #"\n")` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G7-13: line-seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'REPL_TRIPLE_VOICE': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first (clojure.string/split-lines "first\nsecond"` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('first\\nsecond',), resolution doesn't close the loop)
    - [REPL_TRIPLE_VOICE] form=`(first (clojure.string/split-lines "first\nsecond"` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first (clojure.string/split-lines "first\nsecond"` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('first\\nsecond',), resolution doesn't close the loop)

### G7-14: with-open

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(with-out-str (println "hare"))` — user_msg 201 words

### G7-15: *in* and *out*

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'REPL_TRIPLE_VOICE': 2}
    - [WRONG_FABLE_LITERAL] form=`(with-out-str (print "x"))` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [REPL_TRIPLE_VOICE] form=`(with-out-str (print "x"))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`(with-out-str (println))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G7-16: edn read

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'REPL_TRIPLE_VOICE': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(clojure.edn/read-string "{:a 1}")` — sentence with 5 commas reads as AI-output cadence: 'To parse an edn map from a string, she, with the slow certainty of the sun, comp'
    - [REPL_TRIPLE_VOICE] form=`(clojure.edn/read-string "[:hare :tortoise]")` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`(clojure.edn/read-string "[:hare :tortoise]")` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G7-17: JSON roundtrip

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — user_msg 207 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b'), resolution doesn't close the loop)

## Grade 8

### G8-02: deftype introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 2, 'HIGH_LENGTH': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — sentence with 5 commas reads as AI-output cadence: 'Faster,\nmore focused, less convenient." To define a type Pebble with a color fie'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — sentence with 5 commas reads as AI-output cadence: 'Faster,\nmore focused, less convenient." To define a type Pebble with a color fie'
    - [HIGH_LENGTH] form=`(do (deftype Stone [weight]) (.-weight (Stone. 7))` — user_msg 203 words

### G8-03: defrecord introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — sentence with 6 commas reads as AI-output cadence: 'Faster,\nmore focused, less convenient." To define a Runner case with two named c'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defrecord Runner [name pace]) (:name (->Runne` — sentence with 6 commas reads as AI-output cadence: 'Faster,\nmore focused, less convenient." To define a record type named Runner wit'

### G8-05: Protocol extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 5}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('swift', 'hare'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 6 commas reads as AI-output cadence: 'The runtime looks up which breed the\ndog is, then runs that breed\'s answer." To '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('swift', 'hare'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('swift', 'hare'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'The runtime\nreads from the ledger whenever the call goes out." To\ndefine a proto'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', ':number'), resolution doesn't close the loop)

### G8-06: Protocol method dispatch

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'Any dog\nthat learns the signals may join the pack." To define a protocol Pace wi'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, extend it to both String and Long t'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 6 commas reads as AI-output cadence: 'The runtime looks up which breed the\ndog is, then runs that breed\'s answer." To '

### G8-07: Record implementing protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 4}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':swift', 'Pip'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':swift', 'Pip'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, define a record Hare that implement'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':swift', 'Pip'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, define a record Hare that implement'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord T` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':steady', 'Shelly'), resolution doesn't close the loop)

### G8-08: Multimethod defmulti

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmulti pace :species) (defmethod pace :hare` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':species', ':hare', ':swift'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmulti pace :species) (defmethod pace :hare` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':species', ':hare', ':swift'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmulti pace :species) (defmethod pace :hare` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':species', ':hare', ':swift'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 5 commas reads as AI-output cadence: 'The runtime reads it, finds the matching pile,\nand runs that one." To declare a '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti tag :kind) (defmethod tag :stone [_]` — sentence with 6 commas reads as AI-output cadence: 'To define a multimethod tag that dispatches on the :kind key, add a method for :'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti tag :kind) (defmethod tag :stone [_]` — sentence with 5 commas reads as AI-output cadence: 'The original stone doesn\'t change; the runtime\njust learns one more route." To d'

### G8-09: Multimethod defmethod

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 5}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 6 commas reads as AI-output cadence: 'The runtime reads it, finds the matching pile,\nand runs that one." To define a m'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 5 commas reads as AI-output cadence: 'To define a multimethod pace that dispatches on :species with methods for both :'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 6 commas reads as AI-output cadence: 'The runtime reads it, finds the matching pile,\nand runs that one." To define a m'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 6 commas reads as AI-output cadence: 'The runtime reads it, finds the matching pile,\nand runs that one." To define a m'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 6 commas reads as AI-output cadence: 'The runtime reads it, finds the matching pile,\nand runs that one." To define a m'

### G8-10: Multimethod vs protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Show (show [this])) (extend-proto` — sentence with 7 commas reads as AI-output cadence: 'The runtime reads it, finds the matching pile,\nand runs that one." To define a p'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Show (show [this])) (extend-proto` — sentence with 7 commas reads as AI-output cadence: 'The runtime reads it, finds the matching pile,\nand runs that one." To define a p'

### G8-11: Protocol vs Java interface

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol IPace (run [this])) (extend-proto` — sentence with 6 commas reads as AI-output cadence: 'The runtime looks up which breed the\ndog is, then runs that breed\'s answer." To '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol IPace (run [this])) (extend-proto` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol IPace with method run, extend it to String type, then call '

### G8-12: extend-type on built-in types

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 4}
    - [DOUBLE_NAME_INTRO] form=`(do (defprotocol Pace (speed [this])) (extend-type` — character 'Topsy the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-type` — sentence with 6 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, use extend-type to attach it to Lon'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-type` — sentence with 7 commas reads as AI-output cadence: 'The runtime reads it, finds the matching pile,\nand runs that one." To define a p'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-type` — sentence with 6 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, use extend-type to attach it to Lon'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-type` — sentence with 7 commas reads as AI-output cadence: 'The runtime reads it, finds the matching pile,\nand runs that one." To define a p'

### G8-13: this-style vs fn-style

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'PARAGRAPH_FRAGMENTATION': 1, 'CLAUSE_STACK_OVERFLOW': 4}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Named (name-of [this])) (defrecor` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':n', 'Zephyr'), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Named (name-of [this])) (defrecor` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':n', 'Zephyr'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Named (name-of [this])) (defrecor` — sentence with 5 commas reads as AI-output cadence: 'Any dog\nthat learns the signals may join the pack." To define a protocol Named w'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Named (name-of [this])) (defrecor` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':n', 'Zephyr'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Named (name-of [this])) (defrecor` — sentence with 5 commas reads as AI-output cadence: 'Any dog\nthat learns the signals may join the pack." To define a protocol Named w'

### G8-14: Protocols don't inherit

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — sentence with 6 commas reads as AI-output cadence: 'Any dog\nthat learns the signals may join the pack." To define two protocols A an'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — sentence with 6 commas reads as AI-output cadence: 'To define two protocols A and B, each with a method, extend both to String type '

### G8-15: derive and isa? — multimethod hierarchy

- examples: 3
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'CLAUSE_STACK_OVERFLOW': 3, 'BOOL_LEAK_RESOLUTION': 1, 'PARAGRAPH_FRAGMENTATION': 1, 'DOUBLE_NAME_INTRO': 1}
    - [WRONG_FABLE_LITERAL] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [CLAUSE_STACK_OVERFLOW] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — sentence with 6 commas reads as AI-output cadence: 'The runtime reads it, finds the matching pile,\nand runs that one." To establish '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — sentence with 5 commas reads as AI-output cadence: 'To establish a type relationship where ::hare is a type of ::runner, then check '
    - [CLAUSE_STACK_OVERFLOW] form=`(isa? java.lang.Long java.lang.Number)` — sentence with 5 commas reads as AI-output cadence: 'The runtime reads it, finds the matching pile,\nand runs that one." To check whet'
    - [BOOL_LEAK_RESOLUTION] form=`(isa? java.lang.String java.lang.Number)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [PARAGRAPH_FRAGMENTATION] form=`(isa? java.lang.String java.lang.Number)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G8-16: Abstract design with protocols

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 2, 'PARAGRAPH_FRAGMENTATION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':leap', ':plod'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — sentence with 5 commas reads as AI-output cadence: 'Any dog\nthat learns the signals may join the pack." To define a protocol Move wi'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':leap', ':plod'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — sentence with 6 commas reads as AI-output cadence: 'The runtime looks up which breed the\ndog is, then runs that breed\'s answer." To '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':leap', ':plod'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Sound (cry [this])) (defrecord Ha` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':thump', ':hiss'), resolution doesn't close the loop)

## Grade 9

### G9-01: Immutability as default — review

- examples: 2
- variety @ n=50: 1.00
- issues: {'RESOLUTION_REPL_DOUBLED': 3, 'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [RESOLUTION_REPL_DOUBLED] form=`(let [m {:a 1}] (assoc m :b 2) m)` — story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat
    - [RESOLUTION_REPL_DOUBLED] form=`(let [m {:a 1}] (assoc m :b 2) m)` — story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat
    - [RESOLUTION_REPL_DOUBLED] form=`(let [m {:a 1}] (assoc m :b 2) m)` — story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [v [1 2 3]] (conj v 4) v)` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [v [1 2 3]] (conj v 4) v)` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [v [1 2 3]] (conj v 4) v)` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count

### G9-02: Why state at all

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 5, 'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — sentence with 8 commas reads as AI-output cadence: 'If two dogs arrive at once, the runtime makes sure only one of us\ngoes through a'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — sentence with 8 commas reads as AI-output cadence: 'to\nwrite atomically, no matter who else is sniffing." To\nconstruct an atom holdi'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — sentence with 7 commas reads as AI-output cadence: 'The\ncount changes only when one of us scratches a new one — and only\nas the runt'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def progress (atom :idle)) (reset! progress :` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':idle', ':running'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def progress (atom :idle)) (reset! progress :` — sentence with 8 commas reads as AI-output cadence: 'to\nwrite atomically, no matter who else is sniffing." To\nconstruct an atom holdi'
    - [HIGH_LENGTH] form=`(do (def progress (atom :idle)) (reset! progress :` — user_msg 208 words

### G9-03: Atom introduction

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CONCEPT_PHRASE_COMMA_LIST': 9, 'CLAUSE_STACK_OVERFLOW': 8}
    - [HIGH_LENGTH] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg 203 words
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 7 commas reads as AI-output cadence: 'To set up a shared notebook starting at 0, atomically add one to its page, then '
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 7 commas reads as AI-output cadence: 'The\ncount changes only when one of us scratches a new one — and only\nas the runt'

### G9-04: Atom CAS semantics

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 6}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — concept_phrase 'atom, CAS, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — sentence with 7 commas reads as AI-output cadence: 'The\nruntime sees to that — no two writers stomp on each other\'s\nwork." To constr'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — concept_phrase 'atom, CAS, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — sentence with 7 commas reads as AI-output cadence: 'The\ncount changes only when one of us scratches a new one — and only\nas the runt'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — concept_phrase 'atom, CAS, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — sentence with 7 commas reads as AI-output cadence: 'The\ncount changes only when one of us scratches a new one — and only\nas the runt'

### G9-05: Watch on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':w',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — sentence with 8 commas reads as AI-output cadence: 'If two dogs arrive at once, the runtime makes sure only one of us\ngoes through a'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':w',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — sentence with 7 commas reads as AI-output cadence: 'The\nruntime sees to that — no two writers stomp on each other\'s\nwork." To constr'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':w',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — sentence with 7 commas reads as AI-output cadence: 'The\ncount changes only when one of us scratches a new one — and only\nas the runt'

### G9-06: Validator on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — sentence with 5 commas reads as AI-output cadence: 'validator on it, atomically swap by applying inc, and dereference, he composed a'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — sentence with 5 commas reads as AI-output cadence: 'validator on it, atomically swap by applying inc, and dereference, he composed\na'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — sentence with 5 commas reads as AI-output cadence: 'validator on it, atomically swap by applying inc, and dereference, he\ncomposed a'

### G9-07: Ref introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 6}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — concept_phrase 'ref, dosync, alter, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 8 commas reads as AI-output cadence: 'The\nruntime sees to that — no two writers stomp on each other\'s\nwork." To constr'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — concept_phrase 'ref, dosync, alter, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 8 commas reads as AI-output cadence: 'To construct a ref holding 0, perform a transactional alter by applying inc insi'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — concept_phrase 'ref, dosync, alter, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 8 commas reads as AI-output cadence: 'To construct a ref holding 0, perform a transactional alter by applying inc insi'

### G9-08: dosync and alter

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 5, 'PARAGRAPH_FRAGMENTATION': 1, 'CONCEPT_PHRASE_COMMA_LIST': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — sentence with 6 commas reads as AI-output cadence: 'To construct refs a and b, perform a coordinated transaction that alters both by'
    - [PARAGRAPH_FRAGMENTATION] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — sentence with 6 commas reads as AI-output cadence: 'The\ncount changes only when one of us scratches a new one — and only\nas the runt'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — concept_phrase 'ref, dosync, alter, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — sentence with 8 commas reads as AI-output cadence: 'To construct a ref holding 10, perform a transactional alter by applying + with '
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — concept_phrase 'ref, dosync, alter, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose

### G9-09: Ref vs atom

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 6}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 7 commas reads as AI-output cadence: 'The\ncount changes only when one of us scratches a new one — and only\nas the runt'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 7 commas reads as AI-output cadence: 'To construct an atom holding 0, atomically swap it by applying inc, and derefere'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 7 commas reads as AI-output cadence: 'The\nruntime sees to that — no two writers stomp on each other\'s\nwork." To constr'

### G9-10: Agent introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 6}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 5 commas reads as AI-output cadence: 'She, neither restless nor weary but steady, composed agent, send, await, deref w'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 10 commas reads as AI-output cadence: 'The result will be there when you\nask for it — sometimes you have to wait for th'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 10 commas reads as AI-output cadence: 'The result will be there when you\nask for it — sometimes you have to wait for th'

### G9-11: send and send-off

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 5}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 10 commas reads as AI-output cadence: 'The result will be there when you\nask for it — sometimes you have to wait for th'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 5 commas reads as AI-output cadence: 'She, with the steady breathing of a long walker, composed agent, send, await, de'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 9 commas reads as AI-output cadence: 'To construct an agent holding 0, use send to asynchronously apply inc, await its'

### G9-12: await — synchronizing on agents

- examples: 1
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 3, 'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 3}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — concept_phrase 'agent, double send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [DOUBLE_NAME_INTRO] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — character 'Topsy the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 9 commas reads as AI-output cadence: 'To construct an agent holding 0, asynchronously send inc twice, synchronize with'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — concept_phrase 'agent, double send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 9 commas reads as AI-output cadence: 'The runtime makes that easier than it sounds." To construct an agent holding 0, '
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — concept_phrase 'agent, double send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose

### G9-13: future introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 2, 'PARAGRAPH_FRAGMENTATION': 1}
    - [HIGH_LENGTH] form=`@(future (+ 1 2))` — user_msg 204 words
    - [CONCEPT_PHRASE_COMMA_LIST] form=`@(future (+ 1 2))` — concept_phrase 'future, add, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CONCEPT_PHRASE_COMMA_LIST] form=`@(future (+ 1 2))` — concept_phrase 'future, add, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CONCEPT_PHRASE_COMMA_LIST] form=`@(future (+ 1 2))` — concept_phrase 'future, add, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CONCEPT_PHRASE_COMMA_LIST] form=`@(future (* 6 7))` — concept_phrase 'future, multiply, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`@(future (* 6 7))` — sentence with 6 commas reads as AI-output cadence: 'The runtime makes that easier than it sounds." To construct a future that multip'

### G9-14: deref @ shorthand

- examples: 2
- variety @ n=50: 1.00
- issues: {'PARAGRAPH_FRAGMENTATION': 2}
    - [PARAGRAPH_FRAGMENTATION] form=`(do (def a (atom 7)) @a)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [PARAGRAPH_FRAGMENTATION] form=`(do (def a (atom 7)) (deref a))` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G9-15: promise — deliver and deref

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 4, 'PARAGRAPH_FRAGMENTATION': 1}
    - [WRONG_FABLE_LITERAL] form=`(do (def p (promise)) (deliver p :done) @p)` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def p (promise)) (deliver p :done) @p)` — concept_phrase 'promise, deliver, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def p (promise)) (deliver p :done) @p)` — sentence with 7 commas reads as AI-output cadence: 'The runtime makes that easier than it sounds." To construct a promise, deliver a'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def p (promise)) (deliver p :done) @p)` — concept_phrase 'promise, deliver, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def p (promise)) (deliver p :done) @p)` — sentence with 7 commas reads as AI-output cadence: 'To construct a promise, deliver a completion keyword to it, and dereference to g'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def p (promise)) (deliver p :done) @p)` — concept_phrase 'promise, deliver, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose

### G9-16: volatile — when STM is too heavy

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 5, 'PARAGRAPH_FRAGMENTATION': 1}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — concept_phrase 'volatile, vswap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — sentence with 8 commas reads as AI-output cadence: 'to\nwrite atomically, no matter who else is sniffing." To\nconstruct a volatile ho'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — concept_phrase 'volatile, vswap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — sentence with 8 commas reads as AI-output cadence: 'If two dogs arrive at once, the runtime makes sure only one of us\ngoes through a'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — concept_phrase 'volatile, vswap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — sentence with 7 commas reads as AI-output cadence: 'The\nruntime sees to that — no two writers stomp on each other\'s\nwork." To constr'

### G9-17: binding — thread-local

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 5, 'PARAGRAPH_FRAGMENTATION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — concept_phrase 'dynamic var, binding, read' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — sentence with 7 commas reads as AI-output cadence: 'The\nruntime sees to that — no two writers stomp on each other\'s\nwork." To define'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — concept_phrase 'dynamic var, binding, read' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — sentence with 7 commas reads as AI-output cadence: 'To define a dynamic var *p* as 1, use binding to rebind it to 99, and read its v'

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 4, 'HIGH_LENGTH': 2}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — concept_phrase 'lock, locking, arithmetic' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — sentence with 7 commas reads as AI-output cadence: 'The\ncount changes only when one of us scratches a new one — and only\nas the runt'
    - [HIGH_LENGTH] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg 221 words
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — concept_phrase 'lock, locking, arithmetic' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [HIGH_LENGTH] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg 223 words
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — concept_phrase 'lock, locking, arithmetic' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose

## Grade 10

### G10-01: quote, unquote, unquote-splice

- examples: 3
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'THE_FORM_OVERUSE': 2, 'ONLY_SHOOK_HEAD_TIC': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [THE_FORM_OVERUSE] form=`'(1 2 3)` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [THE_FORM_OVERUSE] form=`'(1 2 3)` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [ONLY_SHOOK_HEAD_TIC] form=`(let [x 5] `(a ~x b))` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

### G10-02: syntax-quote

- examples: 2
- variety @ n=50: 1.00
- issues: {'THE_FORM_OVERUSE': 3, 'HIGH_LENGTH': 1, 'ONLY_SHOOK_HEAD_TIC': 1}
    - [THE_FORM_OVERUSE] form=`(let [x 10] `(+ ~x ~x))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [THE_FORM_OVERUSE] form=`(let [x 10] `(+ ~x ~x))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [HIGH_LENGTH] form=`(let [xs [1 2 3]] `(list ~@xs))` — user_msg 211 words
    - [THE_FORM_OVERUSE] form=`(let [xs [1 2 3]] `(list ~@xs))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [ONLY_SHOOK_HEAD_TIC] form=`(let [xs [1 2 3]] `(list ~@xs))` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

### G10-03: defmacro introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg 213 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` — sentence with 5 commas reads as AI-output cadence: 'A rule takes a *form* and makes a different *form* — only\nthen does the runtime '

### G10-04: Macro expansion rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(macroexpand-1 '(or a b))` — sentence with 5 commas reads as AI-output cadence: 'You set the rule\nonce, and any mark that uses it gets rewritten on the way to th'

### G10-05: macroexpand

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(macroexpand '(-> 1 inc inc))` — sentence with 5 commas reads as AI-output cadence: 'You set the rule\nonce, and any mark that uses it gets rewritten on the way to th'

### G10-06: when and when-not as macros

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'WRONG_FABLE_LITERAL': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(when true 1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'You set the rule\nonce, and any mark that uses it gets rewritten on the way to th'
    - [WRONG_FABLE_LITERAL] form=`(when-not false :ok)` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 3, 'ANSWER_LEAK': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'CONCEPT_AS_VERB': 1}
    - [HIGH_LENGTH] form=`(-> 5 inc inc inc)` — user_msg 226 words
    - [ANSWER_LEAK] form=`(-> 5 inc inc inc)` — answer 7 in narrative
    - [HIGH_LENGTH] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — user_msg 216 words
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — parametric example has hard-coded English numeral 'four bones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — sentence with 7 commas reads as AI-output cadence: 'To thread a vector through filter, map, and reduce using thread-last, she, with '
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — parametric example has hard-coded English numeral 'four bones' in a story slot — the actual draws may differ from this fixed count

### G10-08: Macro vs fn

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3` — character 'Chestnut the dog' introduced twice within 200 chars — drop the second 'the dog'

### G10-10: Anaphoric macros are confusing

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)

### G10-11: Reader macros overview

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'ANSWER_LEAK': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(#(* % %) 6)` — user_msg 221 words
    - [ANSWER_LEAK] form=`(#(* % %) 6)` — answer 36 in narrative
    - [CLAUSE_STACK_OVERFLOW] form=`[1 #_ 2 3]` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'
    - [HIGH_LENGTH] form=`[1 #_ 2 3]` — user_msg 201 words

### G10-12: Tagged literals

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(inst? #inst "2024-01-01")` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'
    - [CLAUSE_STACK_OVERFLOW] form=`(inst? #inst "2024-01-01")` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'
    - [HIGH_LENGTH] form=`(uuid? #uuid "00000000-0000-0000-0000-000000000000` — user_msg 207 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(uuid? #uuid "00000000-0000-0000-0000-000000000000` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('00000000', '-0000', '-0000'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(uuid? #uuid "00000000-0000-0000-0000-000000000000` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('00000000', '-0000', '-0000'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(uuid? #uuid "00000000-0000-0000-0000-000000000000` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('00000000', '-0000', '-0000'), resolution doesn't close the loop)

### G10-13: Data readers and EDN extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(clojure.edn/read-string "[:a :b :c]")` — user_msg 209 words

### G10-14: eval (the function)

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1, 'CLAUSE_STACK_OVERFLOW': 2}
    - [ANSWER_LEAK] form=`(eval '(+ 1 2 3))` — answer 6 in narrative
    - [CLAUSE_STACK_OVERFLOW] form=`(eval '(+ 1 2 3))` — sentence with 5 commas reads as AI-output cadence: 'You set the rule\nonce, and any mark that uses it gets rewritten on the way to th'
    - [CLAUSE_STACK_OVERFLOW] form=`(eval (list '+ 4 5))` — sentence with 5 commas reads as AI-output cadence: 'You set the rule\nonce, and any mark that uses it gets rewritten on the way to th'

### G10-15: When not to write a macro

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1}
    - [WRONG_FABLE_LITERAL] form=`(do "a function suffices when no syntax shaping is` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg

### G10-16: Macro pattern library

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro with-steady-pace [& body] `(let [pac` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':slow-and-steady'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmacro with-steady-pace [& body] `(let [pac` — sentence with 5 commas reads as AI-output cadence: 'You set the rule\nonce, and any mark that uses it gets rewritten on the way to th'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro with-steady-pace [& body] `(let [pac` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':slow-and-steady'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro with-steady-pace [& body] `(let [pac` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':slow-and-steady'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':slow',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':slow',), resolution doesn't close the loop)

## Grade 11

### G11-01: JVM vs CLR vs JS vs Python (host overview)

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 2}
    - [DOUBLE_NAME_INTRO] form=`(do "Clojure runs on multiple hosts: JVM, CLR, JS,` — character 'Runner the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [DOUBLE_NAME_INTRO] form=`(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScr` — character 'Pippin the dog' introduced twice within 200 chars — drop the second 'the dog'

### G11-02: Method call syntax

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [HIGH_LENGTH] form=`(.startsWith "hare-tortoise" "hare")` — user_msg 203 words
    - [PARAGRAPH_FRAGMENTATION] form=`(. "abc" toUpperCase)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G11-03: Static method call

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(Math/abs -7)` — user_msg 224 words
    - [CLAUSE_STACK_OVERFLOW] form=`(Math/max 3 9)` — sentence with 5 commas reads as AI-output cadence: 'The runtime moves a value across the\nboundary, calls the human-side tool, and br'

### G11-04: Field access

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(count "tortoise")` — sentence with 5 commas reads as AI-output cadence: 'The runtime moves a value across the\nboundary, calls the human-side tool, and br'
    - [CLAUSE_STACK_OVERFLOW] form=`(count "hare")` — sentence with 5 commas reads as AI-output cadence: 'The runtime moves a value across the\nboundary, calls the human-side tool, and br'
    - [CLAUSE_STACK_OVERFLOW] form=`(count "hare")` — sentence with 5 commas reads as AI-output cadence: 'The runtime moves a value across the\nboundary, calls the human-side tool, and br'

### G11-07: Arrays

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a (int-array [10 20 30])] (aget a 1))` — sentence with 5 commas reads as AI-output cadence: 'The runtime moves a value across the\nboundary, calls the human-side tool, and br'
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a (int-array [1 2 3])] (alength a))` — sentence with 5 commas reads as AI-output cadence: 'The runtime moves a value across the\nboundary, calls the human-side tool, and br'

### G11-08: Type hints

- examples: 2
- variety @ n=50: 1.00
- issues: {'PARAGRAPH_FRAGMENTATION': 1}
    - [PARAGRAPH_FRAGMENTATION] form=`(let [^String s "abc"] (.toUpperCase s))` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G11-09: Checked vs unchecked math

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_AS_TIME_TRAVELLER': 2}
    - [REPL_AS_TIME_TRAVELLER] form=`(+ 1 2)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [REPL_AS_TIME_TRAVELLER] form=`(do "*unchecked-math* turns off overflow checking ` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

### G11-10: ClojureScript overview

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HEDGING_NEAR_FORM] form=`(do "cljs runs in browsers and Node, with JS inter` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "cljs runs in browsers and Node, with JS inter` — sentence with 5 commas reads as AI-output cadence: 'Roly the dog, settled in for a long wait, who had simply walked to a flat stone '

### G11-12: Basilisp overview (Python host)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HEDGING_NEAR_FORM] form=`(do "basilisp is a Clojure-like Lisp implemented o` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "basilisp is a Clojure-like Lisp implemented o` — sentence with 5 commas reads as AI-output cadence: 'Topsy the dog, settled in for a long wait, who had simply walked to a flat stone'

### G11-13: Cross-platform .cljc and reader-conditionals

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1}
    - [WRONG_FABLE_LITERAL] form=`(do "#?(:clj … :cljs …) selects a form per host at` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg

### G11-14: Debugging host leaks

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(try (Math/sqrt 4) (catch Exception _ :err))` — sentence with 5 commas reads as AI-output cadence: 'The runtime moves a value across the\nboundary, calls the human-side tool, and br'

## Grade 12

### G12-01: Transducers introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'COLLECTION_LEAK': 1, 'NUMERAL_LIST_IN_GOAL': 3, 'WRONG_FABLE_LITERAL': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(into [] (map inc) [1 2 3])` — user_msg 226 words
    - [COLLECTION_LEAK] form=`(into [] (map inc) [1 2 3])` — elements of expected [2, 3, 4] appear comma-separated in user_msg (collection answer leak)
    - [NUMERAL_LIST_IN_GOAL] form=`(into [] (filter even?) [1 2 3 4 5])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(into [] (filter even?) [1 2 3 4 5])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [WRONG_FABLE_LITERAL] form=`(into [] (filter even?) [1 2 3 4 5])` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [NUMERAL_LIST_IN_GOAL] form=`(into [] (filter even?) [1 2 3 4 5])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing

### G12-02: Transducer composition

- examples: 2
- variety @ n=50: 1.00
- issues: {'NUMERAL_LIST_IN_GOAL': 6, 'CLAUSE_STACK_OVERFLOW': 4}
    - [NUMERAL_LIST_IN_GOAL] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — sentence with 8 commas reads as AI-output cadence: 'The receiver is patient; the gap is exact." To\ncompose map-inc and filter-even i'
    - [NUMERAL_LIST_IN_GOAL] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — goal_text contains 6 numerals across 6 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — sentence with 6 commas reads as AI-output cadence: 'Write a form whose evaluation gives the sum accumulated via transduce using the '

### G12-03: into with a transducer (xform)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'COLLECTION_LEAK': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(into #{} (map inc) [1 2 3])` — user_msg 227 words
    - [COLLECTION_LEAK] form=`(into #{} (map inc) [1 2 3])` — elements of expected {2, 3, 4} appear comma-separated in user_msg (collection answer leak)
    - [CLAUSE_STACK_OVERFLOW] form=`(into #{} (map inc) [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'Leo the dog shook\nhis head and went on with the work: to use the map-inc transdu'

### G12-05: Channels and pipelines

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "pipe, mult, mix, pipeline-async route values ` — sentence with 5 commas reads as AI-output cadence: 'Marigold squinted at the goal — to study how pipe, mult, mix, and pipeline-async'

### G12-06: clojure.spec

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1}
    - [HEDGING_NEAR_FORM] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value

### G12-07: Spec generators

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HEDGING_NEAR_FORM] form=`(do "spec generators turn specs into property-base` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "spec generators turn specs into property-base` — sentence with 5 commas reads as AI-output cadence: 'Gus the dog, with even breath and steady step, who had simply walked to a flat s'

### G12-08: clojure.test

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HEDGING_NEAR_FORM] form=`(= (+ 1 2) 3)` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(= (+ 1 2) 3)` — sentence with 5 commas reads as AI-output cadence: "Watchdog the dog, with a hen's long stillness on the nest, who had simply walked"

### G12-09: Test fixtures

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HEDGING_NEAR_FORM] form=`(do "fixtures provide setup/teardown around deftes` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "fixtures provide setup/teardown around deftes` — sentence with 5 commas reads as AI-output cadence: 'Peach the dog, settled in for a long wait, who had simply walked to a flat stone'

### G12-10: Property-based testing

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 2, 'CLAUSE_STACK_OVERFLOW': 2}
    - [HEDGING_NEAR_FORM] form=`(= (reverse (reverse [1 2 3])) [1 2 3])` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(= (reverse (reverse [1 2 3])) [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'Zoomer the dog, with eyes always on the path, who had simply walked to a flat st'
    - [HEDGING_NEAR_FORM] form=`(do "test.check generates inputs and checks proper` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "test.check generates inputs and checks proper` — sentence with 5 commas reads as AI-output cadence: 'Biscuit the dog, with the steady walk of a tortoise, who had simply walked to a '

### G12-12: deps.edn projects

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HEDGING_NEAR_FORM] form=`(do "deps.edn declares :deps and :aliases for the ` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "deps.edn declares :deps and :aliases for the ` — sentence with 5 commas reads as AI-output cadence: 'Topsy the dog, settled in for a long wait, who had simply walked to a flat stone'

### G12-13: Aliases and tools

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1}
    - [WRONG_FABLE_LITERAL] form=`(do "`clj -M:test` runs the :test alias from deps.` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg

### G12-15: Datomic / XTDB (datalog db brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [WRONG_FABLE_LITERAL] form=`(do "Datomic and XTDB are immutable, time-aware da` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [HEDGING_NEAR_FORM] form=`(do "Datomic and XTDB are immutable, time-aware da` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "Datomic and XTDB are immutable, time-aware da` — sentence with 6 commas reads as AI-output cadence: 'Setter the dog, her quiet hands at her quiet sides, who had simply walked to a f'

---

## Summary

### Issue counts (across all examples × 3 records)

- **CLAUSE_STACK_OVERFLOW**: 253
- **NARRATIVE_NUMERAL_HARDCODE**: 138
- **STORY_RESOLUTION_NO_DRAWN**: 84
- **CONCEPT_PHRASE_COMMA_LIST**: 75
- **HIGH_LENGTH**: 58
- **REPL_TRIPLE_VOICE**: 54
- **NUMERAL_LIST_IN_GOAL**: 48
- **REPL_AS_TIME_TRAVELLER**: 31
- **RESOLUTION_GENERIC**: 31
- **PARAGRAPH_FRAGMENTATION**: 28
- **FORM_DISPLAY_AND_FORM_NOUN**: 26
- **DOUBLE_NAME_INTRO**: 24
- **WRONG_FABLE_LITERAL**: 16
- **RESOLUTION_REPL_DOUBLED**: 12
- **HEDGING_NEAR_FORM**: 11
- **PARAMETRIC_LITERAL_NUMERALS**: 9
- **THE_FORM_OVERUSE**: 7
- **CONCEPT_AS_VERB**: 7
- **STORY_SLOT_NOUN_REPEAT**: 6
- **ONLY_SHOOK_HEAD_TIC**: 4
- **ANSWER_LEAK**: 4
- **GENERIC_RESOLUTION_TAIL**: 3
- **BOOL_LEAK_RESOLUTION**: 3
- **COLLECTION_LEAK**: 3
- **PREDICATE_QUESTION_COLLISION**: 3
- **SENTENCE_START_LOWER_PRONOUN**: 2
- **META_FILLER_RESOLUTION**: 2
- **HANGING_FORM_THAT**: 1

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 100 | — |
| 2 | 22 | 88 | 137 | — |
| 3 | 18 | 31 | 58 | — |
| 4 | 20 | 39 | 86 | — |
| 5 | 22 | 39 | 119 | — |
| 6 | 16 | 33 | 15 | — |
| 7 | 18 | 36 | 38 | — |
| 8 | 16 | 31 | 93 | — |
| 9 | 18 | 34 | 183 | — |
| 10 | 16 | 36 | 56 | — |
| 11 | 14 | 29 | 20 | — |
| 12 | 18 | 37 | 38 | — |

### Sample issues by severity

#### FORM_DISPLAY_AND_FORM_NOUN

- `G1-01` (form `nil`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    A reflection is a strange kind of promise: present and unreachable, and very hard to argue with.

A few stream-side creatures had gathered on the bank by the pond to
watch Steel attempt to outwit Yappy the dog at reading
the REPL. The water moved on, the bridge held its shadow, and
Yappy, stepping d...
    ```
- `G1-02` (form `-25`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    Sniff the dog was halfway home at the edge of the forest when the water played its old trick on a young dog.

Sniff had been showing Bailey the dog how the REPL works,
the stream cool against their paws and the bridge's shadow long.
"Look here," he said, pointing to the integer -60.
"You hand the fo...
    ```
- `G1-02` (form `-25`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    Down by the stream where the bank dipped low, the world above was answered politely by the world below.

A few stream-side creatures had gathered on the bank near the village to
watch Chestnut attempt to outwit Oscar the dog at reading
the REPL. The water moved on, the bridge held its shadow, and
Os...
    ```
- `G1-02` (form `12345`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    The bridge had stood there as long as anyone remembered, and so had the temptation it offered to anyone crossing with full jaws.

A few stream-side creatures had gathered on the bank by the forest to
watch Keeper attempt to outwit Russet the dog at reading
the REPL. The water moved on, the bridge he...
    ```
- `G1-02` (form `12345`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    On a path that ran beside the stream, a dog was carrying his supper home and looking pleased with himself.

A few stream-side creatures had gathered on the bank near the forest to
watch Scout attempt to outwit Snuffler the dog at reading
the REPL. The water moved on, the bridge held its shadow, and
...
    ```

#### DOUBLE_NAME_INTRO

- `G1-03` (form `(+ 1/2 1/4)`): character 'Pumpernickel the dog' introduced twice within 200 chars — drop the second 'the dog'
    ```
    It was on the beach, on the wooden bridge above the slow brook, that Pumpernickel the dog looked down at the water.

Loki chalked a wager on a flat stone by the beach: whoever
predicted the result of `(+ 1/2 1/4)` would set who crossed the
bridge first. Pumpernickel the dog, with the slow grace of a...
    ```
- `G1-03` (form `(- 1 1/3)`): character 'Whatsit the dog' introduced twice within 200 chars — drop the second 'the dog'
    ```
    It was on the river bank, on the wooden bridge above the slow brook, that Whatsit the dog looked down at the water.

With a twig, Bounder marked a wager into the wet sand along the river bank:
whoever guessed the result of `(- 7 1/3)` first would choose
which bone to carry. Whatsit the dog, without ...
    ```
- `G1-04` (form `"race"`): character 'Gizmo the dog' introduced twice within 200 chars — drop the second 'the dog'
    ```
    near the village, where the path crosses the stream, Gizmo the dog trotted home with a fine bone in his teeth.

A few stream-side creatures had gathered on the bank near the village to
watch Tucker attempt to outwit Gizmo the dog at reading
the REPL. The water moved on, the bridge held its shadow, a...
    ```
- `G1-04` (form `"slow and steady"`): character 'Watcher the dog' introduced twice within 200 chars — drop the second 'the dog'
    ```
    It was along the road, on the wooden bridge above the slow brook, that Watcher the dog looked down at the water.

A few stream-side creatures had gathered on the bank along the road to
watch Leaper attempt to outwit Watcher the dog at reading
the REPL. The water moved on, the bridge held its shadow,...
    ```
- `G1-05` (form `(= 1 2)`): character 'Leo the dog' introduced twice within 200 chars — drop the second 'the dog'
    ```
    It happened on the river bank, on the very bridge Leo the dog crossed every day, that he stopped longer than he should have.

Stalker and Leo the dog paused on the river bank where
someone had scratched the equality (= 3 2) into the wet sand. The water
ran clear and the bridge cast a long, trembling...
    ```

#### ONLY_SHOOK_HEAD_TIC

- `G1-09` (form `(symbol? 'hare)`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    The water beneath the bridge was unhurried that day, and any creature looking down would see a perfect copy of itself.

Henry, his mind already on the larger share, mistook the name on the bark for the
bone it pointed to. "It says bone, so the value must be the
bone!" Marigold the dog only shook her...
    ```
- `G2-18` (form `(count '(1 2 3))`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    A dog with a bone in his jaws is a happy creature; a dog who looks too hard at the water may not be.

Latte, weighing his neighbour's loaf in his eye, mistook the name on the bark for the
bone it pointed to. "It says bone, so the value must be the
bone!" Cooper the dog only shook his head: the mark
...
    ```
- `G10-01` (form `(let [x 5] `(a ~x b))`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    There is a kind of greed that does not see what it already has, and another kind that mistakes a reflection for a meal.

Runner, with greed running ahead of his good sense, mistook the name on the bark for the
bone it pointed to. "It says bone, so the value must be the
bone!" Mocha the dog only shoo...
    ```
- `G10-02` (form `(let [xs [1 2 3]] `(list ~@xs))`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    Pebble the dog was crossing the stream by the beach when he caught a glimpse of his own reflection.

Pickles, as a crow turns a coin against the sun, mistook the name on the bark for the
bone it pointed to. "It says bone, so the value must be the
bone!" Pebble the dog only shook his head: the mark
a...
    ```

#### HIGH_LENGTH

- `G1-09` (form `(symbol? 42)`): user_msg 209 words
    ```
    Silver had crossed this bridge a hundred times by the village, but never with so fine a bone clamped in his jaws.

Patch the hound stood at the stream's edge, holding two objects side by side: a scratch-mark on bark and a smooth stone bearing the number 68. "This one is the symbol," Patch said, tapp...
    ```
- `G1-09` (form `(= 'hare 'hare)`): user_msg 209 words
    ```
    in the meadow, where the boards of the bridge meet the stones of the path, Jack the dog caught sight of himself in the stream.

Rex the hound laid two scratch-marks side by side on bark near the forest. Both marks said the same thing: hare, hare. "Are these two scratches the same name?" Rex asked. "...
    ```
- `G1-10` (form `(+ 1 2) ;; sum of one and two`): user_msg 203 words
    ```
    The bone was good, the day was warm, and the path was clear, and yet the trouble was already shaped in the water.

Bell the hound wrote a form on a clean strip of bark near the pond, then added a double-semicolon mark followed by a note in plain words. "The note is only for other dogs to read," she ...
    ```
- `G1-11` (form `(+
  1
  2)`): user_msg 211 words
    ```
    A dog with a bone in his jaws is a happy creature; a dog who looks too hard at the water may not be.

Patch the hound marked a form on a long bark-strip at the stream's edge but spread the tokens across many lines, each indented neatly. "Does the layout change what the form says?" his packmate asked...
    ```
- `G1-12` (form `(* (+ 1 2) 3)`): user_msg 205 words
    ```
    On a path that ran beside the stream, a dog was carrying his supper home and looking pleased with himself.

Patch the hound marked a nested form on a flat stone near the bank, with one grouped form tucked inside another. "The inner group runs first," Patch said. "Its value becomes the input to the o...
    ```

#### REPL_TRIPLE_VOICE

- `G1-09` (form `(symbol? "tortoise")`): user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    The bone was good, the day was warm, and the path was clear, and yet the trouble was already shaped in the water.

Patch the hound held a message scratched on bark — not a name to pass around, but a strand of letters. "The reader will treat this as text, not as a symbol the dogs can quote," Patch sa...
    ```
- `G1-09` (form `(= 'hare 'hare)`): user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    in the meadow, where the boards of the bridge meet the stones of the path, Jack the dog caught sight of himself in the stream.

Rex the hound laid two scratch-marks side by side on bark near the forest. Both marks said the same thing: hare, hare. "Are these two scratches the same name?" Rex asked. "...
    ```
- `G1-10` (form `(+ 1 2) ;; sum of one and two`): user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    The bone was good, the day was warm, and the path was clear, and yet the trouble was already shaped in the water.

Bell the hound wrote a form on a clean strip of bark near the pond, then added a double-semicolon mark followed by a note in plain words. "The note is only for other dogs to read," she ...
    ```
- `G1-13` (form `(+ 1 2)`): user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    It happened on a day so ordinary that it seemed impossible anything could have been lost.

Bell the hound sat by a flat stone near the pond and laid out two small piles of bones — one of one bone, one of two — careful with the count.

She wanted the precise size of the heap if both piles were nudged...
    ```
- `G1-13` (form `(/ 10 2)`): user_msg mentions 'REPL' 4 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    The path home wound past a slow brook, and on bright days the brook was full of borrowed shapes.

Patch the hound looked at a heap of ten bones and measured them into two equal piles. "How many bones in each pile?" asked a younger dog. "The runtime can tell us exactly by dividing."

Patch wanted the...
    ```

#### CLAUSE_STACK_OVERFLOW

- `G1-09` (form `(= 'hare 'hare)`): sentence with 5 commas reads as AI-output cadence: "The\nreflection in the stream looks like a bone, but the scratch that\nsays 'bone'"
    ```
    On a path that ran beside the stream, a dog was carrying his supper home and looking pleased with himself.

Oscar, with the still patience of a fisher pointed at a name scratched into the bark near the beach,
then at an actual bone lying on the path. "The mark on the bark
is the *name*; the bone is ...
    ```
- `G1-10` (form `(+ 1 2) ;; sum of one and two`): sentence with 6 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'
    ```
    A dog with a bone in his jaws is a happy creature; a dog who looks too hard at the water may not be.

"A form is what's actually there on the bark," Cocoa, stepping deliberately one foot before the next
said, "after the conventions of writing and reading have done
their work. The runtime sees the cl...
    ```
- `G1-12` (form `(+ 2 3)`): sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'
    ```
    at the edge of the meadow, where the path crosses the stream, Topsy the dog trotted home with a fine bone in his teeth.

"A form is what's actually there on the bark," Topsy, settled in for a long wait
said, "after the conventions of writing and reading have done
their work. The runtime sees the cle...
    ```
- `G1-15` (form `(= "a" "a")`): sentence with 6 commas reads as AI-output cadence: 'The verdict follows that\nrule exactly, the way a steady current keeps its line."'
    ```
    Pearl the dog was crossing the stream at the village when she caught a glimpse of his own reflection.

"Only two things in Clojure close the crossing," Pearl
said, with steady breath and a careful eye: "nil and false. Everything else — zero, the
empty string, an empty list — opens it. The verdict fo...
    ```
- `G1-17` (form `(+ 1 2)`): sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'
    ```
    It was near the pond, on the wooden bridge above the slow brook, that Mocha the dog looked down at the water.

"A form is what's actually there on the bark," Mocha, with steady road-tested feet
said, "after the conventions of writing and reading have done
their work. The runtime sees the cleaned-up ...
    ```

#### THE_FORM_OVERUSE

- `G1-11` (form `(+
  1
  2)`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    A dog with a bone in his jaws is a happy creature; a dog who looks too hard at the water may not be.

Patch the hound marked a form on a long bark-strip at the stream's edge but spread the tokens across many lines, each indented neatly. "Does the layout change what the form says?" his packmate asked...
    ```
- `G3-18` (form `(* 5 5 5)`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    It was at the village, on the wooden bridge above the slow brook, that Muffin the dog looked down at the water.

Patch the hound arrived at the crossing and saw three stones arranged in a pile. "I don't need to name these," he said, "because I will use them just once and the form is so short that th...
    ```
- `G10-01` (form `'(1 2 3)`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    along the road, the stream ran clear enough to mirror anything that passed above it, and Toby passed above it.

"There's a difference between *labeling* the form and
*evaluating* it," Toby, with eyes always on the path said. "Quote in any of its
shapes is the labeling — the runtime hands you back th...
    ```
- `G10-01` (form `'(1 2 3)`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    Some greedy creatures lose what they have to a thief; others lose it to themselves, by way of a careless glance.

"There's a difference between *labeling* the form and
*evaluating* it," Kobe, with the still patience of a fisher said. "Quote in any of its
shapes is the labeling — the runtime hands yo...
    ```
- `G10-02` (form `(let [x 10] `(+ ~x ~x))`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    The water beneath the bridge was unhurried that day, and any creature looking down would see a perfect copy of itself.

"To talk about the form itself rather than evaluating it,"
Teddy, with the slow certainty of the sun said, "you mark the form with a quote-scratch in
front. Quoting tells the runti...
    ```

#### REPL_AS_TIME_TRAVELLER

- `G1-13` (form `(+ 1 2)`): user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    ```
    Charcoal had crossed this bridge a hundred times near the river bank, but never with so fine a bone clamped in his jaws.

Fudge eyed the pile, with the cold appetite of unceasing want, and called out a guess
about how many bones were there without bothering to count.
Charcoal the dog simply began co...
    ```
- `G1-13` (form `(/ 10 2)`): user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    ```
    Auburn had found the bone near the river bank and was carrying it home with no small amount of pride.

Tucker eyed the pile, with hard, hungry eyes, and called out a guess
about how many bones were there without bothering to count.
Auburn the dog simply began counting — to divide 14 by 14 required n...
    ```
- `G1-13` (form `(- 20 7)`): user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    ```
    Tawny the dog was halfway home by the pond when the water played its old trick on a young dog.

Polly eyed the pile, with hard, hungry eyes, and called out a guess
about how many bones were there without bothering to count.
Tawny the dog simply began counting — to subtract 6 from 11 required no
eyeb...
    ```
- `G1-14` (form `(- 100 (* 5 5))`): user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    ```
    Some greedy creatures lose what they have to a thief; others lose it to themselves, by way of a careless glance.

Henry eyed the pile, his thoughts already on more, and called out a guess
about how many bones were there without bothering to count.
Wallace the dog simply began counting — to subtract ...
    ```
- `G1-14` (form `(+ (* 2 3) (* 4 5))`): user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    ```
    It happened along the road, on the very bridge Inky the dog crossed every day, that he stopped longer than he should have.

Charcoal eyed the pile, with hard, hungry eyes, and called out a guess
about how many bones were there without bothering to count.
Inky the dog simply began counting — to add t...
    ```

#### NARRATIVE_NUMERAL_HARDCODE

- `G1-13` (form `(- 5 3)`): parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    ```
    A reflection is a strange kind of promise: present and unreachable, and very hard to argue with.

Mochi, with the slow grace of a creature unhurried, arranged a small heap of bones
near the forest, careful with the count — the bridge's shadow long across
the water, every bone weighing what it weighe...
    ```
- `G1-13` (form `(- 5 3)`): parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    ```
    The bone was good, the day was warm, and the path was clear, and yet the trouble was already shaped in the water.

Mocha, settled in for a long wait, arranged a small heap of bones
near the pond, careful with the count — the bridge's shadow long across
the water, every bone weighing what it weighed....
    ```
- `G1-13` (form `(- 5 3)`): parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    ```
    Retriever the dog was halfway home in the forest when the water played its old trick on a young dog.

Retriever, without complaint or hurry laid bones out on a flat stone near the forest, sorting
them into small piles. "Numbers in Clojure are just like bones
in piles," she said: "you can count them,...
    ```
- `G1-13` (form `(* 4 5)`): parametric example has hard-coded English numeral 'four piles' in a story slot — the actual draws may differ from this fixed count
    ```
    The stream ran clear that afternoon, and the bridge cast a long trembling shadow across the water.

"Watch the pile," Ginger said, with steady road-tested feet, gesturing
at a small heap of bones beside the river. "Every operation
either adds, takes away, or combines what's already there — the
pile ...
    ```
- `G1-13` (form `(* 4 5)`): parametric example has hard-coded English numeral 'four piles' in a story slot — the actual draws may differ from this fixed count
    ```
    The path home wound past a slow brook, and on bright days the brook was full of borrowed shapes.

"Watch the pile," Yipper said, with a calm that nothing seemed to ruffle, gesturing
at a small heap of bones beside the river. "Every operation
either adds, takes away, or combines what's already there ...
    ```

#### RESOLUTION_GENERIC

- `G1-13` (form `(* 4 5)`): user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    ```
    The stream ran clear that afternoon, and the bridge cast a long trembling shadow across the water.

"Watch the pile," Ginger said, with steady road-tested feet, gesturing
at a small heap of bones beside the river. "Every operation
either adds, takes away, or combines what's already there — the
pile ...
    ```
- `G1-13` (form `(* 4 5)`): user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    ```
    The path home wound past a slow brook, and on bright days the brook was full of borrowed shapes.

"Watch the pile," Yipper said, with a calm that nothing seemed to ruffle, gesturing
at a small heap of bones beside the river. "Every operation
either adds, takes away, or combines what's already there ...
    ```
- `G1-14` (form `(* (+ 1 2) (+ 3 4))`): user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    ```
    Doodle the dog was crossing the stream near the meadow when she caught a glimpse of his own reflection.

"Watch the pile," Doodle said, with face quiet and hands quieter still, gesturing
at a small heap of bones beside the river. "Every operation
either adds, takes away, or combines what's already t...
    ```
- `G1-14` (form `(- 100 (* 5 5))`): user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    ```
    Down by the stream where the bank dipped low, the world above was answered politely by the world below.

"Watch the pile," Sniff said, stepping deliberately one foot before the next, gesturing
at a small heap of bones beside the river. "Every operation
either adds, takes away, or combines what's alr...
    ```
- `G1-14` (form `(- 100 (* 5 5))`): user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    ```
    Lunger had crossed this bridge a hundred times along the river bank, but never with so fine a bone clamped in his jaws.

"Watch the pile," Lunger said, neither hastening nor hanging back, gesturing
at a small heap of bones beside the river. "Every operation
either adds, takes away, or combines what'...
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
Pip, with face quiet and hands quieter still said. "You bring the value to the bank, the
runtime checks it, and the conditions gi...
    ```
- `G2-15` (form `(if 0 1 0)`): tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    ```
    near the road, where the path crosses the stream, Pip the dog trotted home with a fine bone in his teeth.

"You can't tell whether the crossing will be open by guessing,"
Pip, with steady road-tested feet said. "You bring the value to the bank, the
runtime checks it, and the conditions give the only...
    ```
- `G3-15` (form `(do (println "hi") 42)`): tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    ```
    near the road, where the path crosses the stream, Pip the dog trotted home with a fine bone in his teeth.

"On any nose-trail," Pip, with steady road-tested feet explained, "the last sniff
is what you carry home." He took the goal — to
execute a print statement for side-effects, then return a differ...
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

"On any nose-trail," Pip, with a calm that nothing seemed to ruffle explained, "the last sniff
is what you carry home." He took the goal — to
compose two inc functions and apply them to 5 — and...
    ```

#### PARAGRAPH_FRAGMENTATION

- `G2-01` (form `(* 2 3 4)`): user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    Leo had carried his prize all the way from the village, and along the road the bridge offered him an unwelcome second look.

Patch the hound gathered three piles of bones near the meadow, each pile marked with a count: 2, 1, and 2.

They wanted the total if each pile was multiplied together — what 2...
    ```
- `G2-07` (form `(abs -5)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    It is one of the oldest tricks of light to make one bone seem like two and to make a fool of the unwary.

Patch the hound held a marked stone carved with negative 5. They wanted to know the distance from zero, ignoring the negative sign entirely.

They needed the magnitude — the pure measure of how ...
    ```
- `G2-07` (form `(abs 0)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    by the river bank, the stream ran clear enough to mirror anything that passed above it, and Otis passed above it.

Bell the hound held a stone marked with zero near the pond. She wanted the absolute value — the distance from zero itself.

She needed to know the magnitude of zero. The absolute value ...
    ```
- `G2-08` (form `(+ 1/2 1/4)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    The bone was good, the day was warm, and the path was clear, and yet the trouble was already shaped in the water.

Rex the hound broke two bones into pieces near the meadow. One bone yielded one-half, the other one-quarter. He wanted to know the combined measure.

He needed the total when the two fr...
    ```
- `G2-08` (form `(- 1 1/3)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    Jack the dog was halfway home near the beach when the water played its old trick on a young dog.

Bell the hound held one whole bone at the stream's edge and removed one-third of it. She wanted to know what fraction remained.

She needed the remainder when one-third was taken from one whole. The sub...
    ```

#### META_FILLER_RESOLUTION

- `G2-01` (form `(- 100 1 2 3)`): user_msg uses generic 'returned exactly' / 'settled with certainty' filler — describe what actually came back, not just that something did
    ```
    at the edge of the forest, the path bends down to meet the water, and Buddy the dog stopped at exactly the wrong moment.

Bell the hound held a great pile of 639 bones by the river bank. Then came three separate losses — first 5, then 7, then 1 bones taken away in turn.

She wanted to know how many ...
    ```
- `G2-01` (form `(- 100 1 2 3)`): user_msg uses generic 'returned exactly' / 'settled with certainty' filler — describe what actually came back, not just that something did
    ```
    by the beach, on a still afternoon by the brook, Saffron learned what a reflection costs the careless.

Bell the hound held a great pile of 422 bones by the river bank. Then came three separate losses — first 1, then 3, then 1 bones taken away in turn.

She wanted to know how many remained after eac...
    ```

#### GENERIC_RESOLUTION_TAIL

- `G2-02` (form `(> 5 4 3 2 1)`): resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    ```
    in the forest, on a still afternoon by the brook, Ziggy learned what a reflection costs the careless.

Ziggy, with the steady breathing of a long walker, arranged a small heap of bones
near the forest, careful with the count — the bridge's shadow long across
the water, every bone weighing what it we...
    ```
- `G2-02` (form `(> 5 4 3 2 1)`): resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    ```
    on the beach, the stream ran clear enough to mirror anything that passed above it, and Whatsit passed above it.

Whatsit, with the slow certainty of the sun, arranged a small heap of bones
near the beach, careful with the count — the bridge's shadow long across
the water, every bone weighing what it...
    ```
- `G2-02` (form `(> 5 4 3 2 1)`): resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    ```
    When Galloper reached the bridge near the pond, she paused to admire the bone he had been so lucky to find.

Galloper, with the still patience of a fisher laid bones out on a flat stone near the pond, sorting
them into small piles. "Numbers in Clojure are just like bones
in piles," she said: "you ca...
    ```

#### BOOL_LEAK_RESOLUTION

- `G2-03` (form `(= 1 1 1)`): resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    ```
    On a path that ran beside the stream, a dog was carrying his supper home and looking pleased with himself.

Bell the hound gathered three bones near the pond, each carved with the same mark: 9. She wanted to test if all three matched each other.

She needed to know if all three marks were identical....
    ```
- `G2-13` (form `(and true false)`): resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    ```
    Cooper the dog was crossing the stream near the forest when he caught a glimpse of his own reflection.

Rex the hound stood at the stream bank facing two test gates placed one after the other. The first bore the mark true, the second false.

He wanted to cross if both gates would let him pass. The a...
    ```
- `G8-15` (form `(isa? java.lang.String java.lang.Number)`): resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    ```
    The water beneath the bridge was unhurried that day, and any creature looking down would see a perfect copy of itself.

Patch the hound asked a second isa? question at the bank: is the String-pack a kind of Number? The Java records would show if there was any family connection.

To know whether Stri...
    ```

#### RESOLUTION_REPL_DOUBLED

- `G2-19` (form `(* 1000000 1000000)`): story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat
    ```
    Peach the dog was crossing the stream near the village when she caught a glimpse of his own reflection.

Rex the hound stood by the river bank with two enormous piles of bones. Each pile held one million bones. He wanted to know the result if he multiplied them together.

He needed the exact product...
    ```
- `G2-19` (form `(* 1000000 1000000)`): story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat
    ```
    It was near the meadow, on the wooden bridge above the slow brook, that Inky the dog looked down at the water.

Bayer eyed the pile, his mouth watering at the thought of more, and called out a guess
about how many bones were there without bothering to count.
Inky the dog simply began counting — to m...
    ```
- `G2-19` (form `(* 1000000 1000000)`): story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat
    ```
    Down by the stream where the bank dipped low, the world above was answered politely by the world below.

Granite eyed the pile, with the sharp hunger that no meal mends, and called out a guess
about how many bones were there without bothering to count.
Biscuit the dog simply began counting — to mult...
    ```
- `G3-09` (form `(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))`): story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat
    ```
    There is a kind of greed that does not see what it already has, and another kind that mistakes a reflection for a meal.

Cooper, as a miser tallies in his sleep, insisted she could just
bound straight to the bone without bothering to follow the
sniff-trail. Drover the dog only smiled and lowered
his...
    ```
- `G3-09` (form `(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))`): story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat
    ```
    A reflection is a strange kind of promise: present and unreachable, and very hard to argue with.

Patch the hound laid out a three-step sniffing-trail at the stream's edge and scratched its name — add3 — into a marker stone beside the path. "This trail takes three counts and gives back their sum," P...
    ```

#### CONCEPT_AS_VERB

- `G3-07` (form `((fn [a b] (* a b)) 3 4)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    by the beach, on a still afternoon by the brook, Jasper learned what a reflection costs the careless.

"A nose-trail is only useful when it gets walked," Jasper, with a calm that nothing seemed to ruffle
said, head low. "You set out the sniffs, you bring the
ingredients, the runtime does the rest." ...
    ```
- `G3-10` (form `(#(+ % 1) 5)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    Bayer had crossed this bridge a hundred times near the forest, but never with so fine a bone clamped in his jaws.

"A nose-trail is only useful when it gets walked," Bayer, with eyes always on the path
said, head low. "You set out the sniffs, you bring the
ingredients, the runtime does the rest." To...
    ```
- `G3-10` (form `(#(+ % 1) 5)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    Beau had found the bone at the edge of the pond and was carrying it home with no small amount of pride.

"A nose-trail is only useful when it gets walked," Beau, neither hastening nor hanging back
said, head low. "You set out the sniffs, you bring the
ingredients, the runtime does the rest." To use ...
    ```
- `G3-10` (form `(#(* %1 %2) 3 4)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    in the meadow, where the boards of the bridge meet the stones of the path, Bingo the dog caught sight of himself in the stream.

"A nose-trail is only useful when it gets walked," Bingo, with the soft patience of running water
said, head low. "You set out the sniffs, you bring the
ingredients, the r...
    ```
- `G5-15` (form `((comp str inc) 9)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    It is one of the oldest tricks of light to make one bone seem like two and to make a fool of the unwary.

"A nose-trail is only useful when it gets walked," Peach, with the soft patience of running water
said, head low. "You set out the sniffs, you bring the
ingredients, the runtime does the rest." ...
    ```

#### STORY_RESOLUTION_NO_DRAWN

- `G3-13` (form `((fn [x] x x x 99) 1)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('99',), resolution doesn't close the loop)
    ```
    It happened on a day so ordinary that it seemed impossible anything could have been lost.

Bell the hound laid out a sniffing-trail at the stream's edge with many scent-marks in a row. "The runtime will follow each sniff," she said, "and check what I named. But only the last sniff is what I carry ho...
    ```
- `G3-13` (form `((fn [x] x x x 99) 1)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('99',), resolution doesn't close the loop)
    ```
    along the river bank, where the path crosses the stream, Sooty the dog trotted home with a fine bone in his teeth.

Sooty, with eyes always on the path put her nose to the ground on the river bank and
worked out a careful sniffing-trail toward the buried bone.
"Recipes in Clojure are like a nose-tra...
    ```
- `G3-13` (form `((fn [x] x x x 99) 1)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('99',), resolution doesn't close the loop)
    ```
    A reflection is a strange kind of promise: present and unreachable, and very hard to argue with.

Peach, with a calm that nothing seemed to ruffle put her nose to the ground by the meadow and
worked out a careful sniffing-trail toward the buried bone.
"Recipes in Clojure are like a nose-trail," she ...
    ```
- `G5-22` (form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    ```
    on the beach, where the path crosses the stream, Hunter the dog trotted home with a fine bone in his teeth.

Bell the hound paced back and forth along a stretch of stream bank near the pond, carrying a small running tally in her jaws. Each pass returned to the same starting point, with the tally a l...
    ```
- `G5-22` (form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    ```
    Russet had found the bone along the river bank and was carrying it home with no small amount of pride.

Bell the hound paced back and forth along a stretch of stream bank near the pond, carrying a small running tally in her jaws. Each pass returned to the same starting point, with the tally a little...
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

Sooty, with a hen's long stillness on the nest, pointed to a hollow log on the river bank,
its inside lined with bones tucked into named slots — the wood
cool, the slots solid. "Wha...
    ```
- `G4-01` (form `[1 2 3]`): parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    ```
    It is one of the oldest tricks of light to make one bone seem like two and to make a fool of the unwary.

Woofer, untroubled by what others thought, pointed to a hollow log along the river bank,
its inside lined with bones tucked into named slots — the wood
cool, the slots solid. "Whatever I want to...
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

Sprocket, with face quiet and hands quieter still, pointed to a hollow log by the forest,
its inside lined with bones tucked into named slots — the wood
cool, the slots solid. "Whatever I wan...
    ```

#### HANGING_FORM_THAT

- `G4-04` (form `'()`): 'form that <noun>' rendered without a verb — template should be 'form for {concept_phrase}'
    ```
    On a path that ran beside the stream, a dog was carrying his supper home and looking pleased with himself.

Patch the hound picked up an empty chain by the bank, a mere collar with no bones attached, and held it up.

Patch wanted the empty chain itself to be a recognizable form that the REPL would h...
    ```

#### NUMERAL_LIST_IN_GOAL

- `G4-13` (form `(count [1 2 3 4 5])`): goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    ```
    It happened on a day so ordinary that it seemed impossible anything could have been lost.

Rex the hound laid out five bones in a hollow log arranged in a neat row: 1, 2, 3, 4, 5. He wanted the precise count of all bones in the cache.

He asked the REPL to tally the bones in the vector and return th...
    ```
- `G4-13` (form `(count [1 2 3 4 5])`): goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    ```
    on the road, on a still afternoon by the brook, Pouncer learned what a reflection costs the careless.

"Watch carefully," Pouncer said, holding open the hollow
log. "Whatever I do to the cache, this one stays exactly as it
was — what I get back is a fresh cache with the change made,
leaving the firs...
    ```
- `G4-13` (form `(count [1 2 3 4 5])`): goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    ```
    When Bruno reached the bridge at the edge of the pond, she paused to admire the bone he had been so lucky to find.

"You can find what you want in a bone-cache several ways,"
Bruno said, without raising her voice at the troubles of the road, gesturing at the hollow log:
"by the scratch above the slo...
    ```
- `G5-10` (form `(map #(* % %) [1 2 3 4])`): goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    ```
    Spaniel had crossed this bridge a hundred times at the village, but never with so fine a bone clamped in his jaws.

Spaniel, with eyes always on the path, stood beside a fallen log laid
across the stream in the village — a gap chewed through its middle, the
water cool and steady beneath. "Whatever r...
    ```
- `G5-10` (form `(map #(* % %) [1 2 3 4])`): goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    ```
    The path home wound past a slow brook, and on bright days the brook was full of borrowed shapes.

Rocco, saying very little, stood beside a fallen log laid
across the stream by the river bank — a gap chewed through its middle, the
water cool and steady beneath. "Whatever rule we choose for the
gap,"...
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

#### ANSWER_LEAK

- `G5-15` (form `((comp inc inc) 5)`): answer 7 in narrative
    ```
    It was an afternoon of quiet sky and steady current, and the world below the surface seemed almost solid.

Patch the hound laid down two nose-trails end to end by the river bank. The first trail was inc, the second trail was inc again. She would chain them together, so what the first trail turned up...
    ```
- `G10-07` (form `(-> 5 inc inc inc)`): answer 7 in narrative
    ```
    Some lessons are taught by mirrors, and some are taught by rivers; this one was taught by both at once.

Bell the hound held the bone marked 4 and laid out a sniffing trail with three increments in order. "Watch the bone pass from sniff to sniff," she said. "Each step takes the previous result as th...
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

#### STORY_SLOT_NOUN_REPEAT

- `G5-20` (form `(take 3 [10 20 30 40 50])`): the noun 'the first three' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    ```
    Zoomer had found the bone in the meadow and was carrying it home with no small amount of pride.

Rocco eyed the bones, as a miser tallies in his sleep, and called out a guess
about what would come out the far side of the gap without
bothering to actually run any through. Zoomer the dog shook
his hea...
    ```
- `G5-20` (form `(take 3 [10 20 30 40 50])`): the noun 'the first three' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    ```
    Down by the stream where the bank dipped low, the world above was answered politely by the world below.

Ace eyed the bones, with the slow secret smile of the covetous, and called out a guess
about what would come out the far side of the gap without
bothering to actually run any through. Slate the d...
    ```
- `G5-20` (form `(take 3 [10 20 30 40 50])`): the noun 'the first three' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    ```
    Down by the stream where the bank dipped low, the world above was answered politely by the world below.

"You can collect the result into any kind of cache you like,"
Marigold, keeping a steady pace through the work said. "A row of bones, a unique-only pile, a sack
of any shape — the gap doesn't car...
    ```
- `G6-14` (form `(name 'java.util.Map)`): the noun 'the kennel-master' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    ```
    near the river bank, where the path crosses the stream, Shadow the dog trotted home with a fine bone in his teeth.

"Each tool in the kennel-master's shed has its own label,"
Shadow, with steady road-tested feet said, "and the right way to call it depends on
which kind of tool it is — some held by a...
    ```
- `G6-14` (form `(name 'java.util.Map)`): the noun 'the kennel-master' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    ```
    Down by the stream where the bank dipped low, the world above was answered politely by the world below.

Barker, with the slow grace of a creature unhurried padded over to the kennel-master's shed near the road
and pulled down a tool the dogs hadn't carved themselves — a
leash, a bowl, a collar. "Th...
    ```

#### HEDGING_NEAR_FORM

- `G6-10` (form `(:deps {:deps {:a 1 :b 2}})`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    The water beneath the bridge was unhurried that day, and any creature looking down would see a perfect copy of itself.

A wager was set at the village: produce the value before the next ripple
crossed the pond. Pebble bolted into a flurry of guesses,
calling out numbers and second-guessing himself a...
    ```
- `G11-10` (form `(do "cljs runs in browsers and Node, with JS interop syntax"`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    It is one of the oldest tricks of light to make one bone seem like two and to make a fool of the unwary.

A wager was set by the village: produce the value before the next ripple
crossed the pond. Collie bolted into a flurry of guesses,
calling out numbers and second-guessing himself about
whether t...
    ```
- `G11-12` (form `(do "basilisp is a Clojure-like Lisp implemented on Python" `): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    at the edge of the meadow, where the path crosses the stream, Topsy the dog trotted home with a fine bone in his teeth.

A wager was set at the edge of the meadow: produce the value before the next ripple
crossed the pond. Trailblazer bolted into a flurry of guesses,
calling out numbers and second-g...
    ```
- `G12-06` (form `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42)`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    Cooper had carried his prize all the way from the village, and near the road the bridge offered him an unwelcome second look.

A wager was set along the road: produce the value before the next ripple
crossed the pond. Pathfinder bolted into a flurry of guesses,
calling out numbers and second-guessin...
    ```
- `G12-07` (form `(do "spec generators turn specs into property-based test inp`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    Gus had carried his prize all the way from the village, and on the beach the bridge offered him an unwelcome second look.

A wager was set by the beach: produce the value before the next ripple
crossed the pond. Pointer bolted into a flurry of guesses,
calling out numbers and second-guessing himself...
    ```

#### CONCEPT_PHRASE_COMMA_LIST

- `G9-03` (form `(do (def a (atom 0)) (swap! a inc) @a)`): concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    Diesel had crossed this bridge a hundred times on the beach, but never with so fine a bone clamped in his jaws.

Bell the hound opened the shared notebook at the stream's edge and scratched a fresh zero onto the first page. This tally-stone would record how many bones the pack had gathered as the da...
    ```
- `G9-03` (form `(do (def a (atom 0)) (swap! a inc) @a)`): concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    in the forest, the stream ran clear enough to mirror anything that passed above it, and Leo passed above it.

Shepherd, his thoughts already on more, swiped a paw across the tally-stone,
trying to scratch an answer over the count. Leo the dog caught
her firmly: tallies shared by all the pack need ca...
    ```
- `G9-03` (form `(do (def a (atom 0)) (swap! a inc) @a)`): concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    It was an afternoon of quiet sky and steady current, and the world below the surface seemed almost solid.

"The tally stays scratched into the stone," Tippet, with the steady breathing of a long walker said,
"so any dog who comes by can read what's there right now. The
count changes only when one of...
    ```
- `G9-03` (form `(do (def a (atom 10)) (swap! a + 5) @a)`): concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    The bridge had stood there as long as anyone remembered, and so had the temptation it offered to anyone crossing with full jaws.

Fudge, his fingers twitching at the thought of profit, swiped a paw across the tally-stone,
trying to scratch an answer over the count. Salty the dog caught
her firmly: t...
    ```
- `G9-03` (form `(do (def a (atom 10)) (swap! a + 5) @a)`): concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    The bone was good, the day was warm, and the path was clear, and yet the trouble was already shaped in the water.

"When I want to update the tally," Ivory, her quiet hands at her quiet sides said, "I don't
pick the stone up and walk away — I read the scratch, apply the
change, and scratch the new c...
    ```

