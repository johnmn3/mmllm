# dog-shadow curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

### G1-01: Eval as substitution

- examples: 4
- variety @ n=50: 1.00
- issues: {'DOUBLE_EMO_INJECTION': 1, 'AS_ONE_WHO_CADENCE': 2, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'LOW_GROUNDING': 2}
    - [DOUBLE_EMO_INJECTION] form=`42` — sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat
    - [AS_ONE_WHO_CADENCE] form=`42` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [AS_ONE_WHO_CADENCE] form=`"hello"` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`nil` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`nil` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`nil` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-02: Integer numbers

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'DOUBLE_EMO_INJECTION': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 5, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`7` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_EMO_INJECTION] form=`-3` — sentence has 2+ distinct EMO-pool phrases ('without complaint or hurry' + 'without complaint') — the character can't earn two emotional registers in the same beat
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`-25` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [DOUBLE_NAME_INTRO] form=`-25` — character 'Sniff the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`-25` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`12345` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-03: Ratios

- examples: 5
- variety @ n=50: 1.00
- issues: {'AS_ONE_WHO_CADENCE': 1, 'LOW_GROUNDING': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 5, 'DOUBLE_NAME_INTRO': 3, 'DOUBLE_EMO_INJECTION': 2}
    - [AS_ONE_WHO_CADENCE] form=`1/2` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [LOW_GROUNDING] form=`1/2` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`1/2` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`3/4` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(+ 1/2 1/4)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [DOUBLE_NAME_INTRO] form=`(+ 1/2 1/4)` — character 'Pumpernickel the dog' introduced twice within 200 chars — drop the second 'the dog'

### G1-04: Strings

- examples: 5
- variety @ n=50: 1.00
- issues: {'DOUBLE_EMO_INJECTION': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 4, 'DOUBLE_NAME_INTRO': 2, 'AS_ONE_WHO_CADENCE': 1}
    - [DOUBLE_EMO_INJECTION] form=`"hello"` — sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`"race"` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [DOUBLE_NAME_INTRO] form=`"race"` — character 'Gizmo the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [AS_ONE_WHO_CADENCE] form=`"slow and steady"` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`"slow and steady"` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [DOUBLE_NAME_INTRO] form=`"slow and steady"` — character 'Watcher the dog' introduced twice within 200 chars — drop the second 'the dog'

### G1-05: Booleans

- examples: 6
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 5, 'LOW_GROUNDING': 2, 'AS_ONE_WHO_CADENCE': 2, 'DOUBLE_NAME_INTRO': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`true` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`true` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`true` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [AS_ONE_WHO_CADENCE] form=`false` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [LOW_GROUNDING] form=`false` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [AS_ONE_WHO_CADENCE] form=`false` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G1-06: nil

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'DOUBLE_EMO_INJECTION': 2, 'AS_ONE_WHO_CADENCE': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 2, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`nil` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_EMO_INJECTION] form=`nil` — sentence has 2+ distinct EMO-pool phrases ('without complaint or hurry' + 'without complaint') — the character can't earn two emotional registers in the same beat
    - [DOUBLE_EMO_INJECTION] form=`(nil? nil)` — sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat
    - [AS_ONE_WHO_CADENCE] form=`(nil? nil)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(nil? 0)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(nil? false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-07: Keywords

- examples: 5
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'PARALLEL_POSSESSIVE_TIC': 1, 'AS_ONE_WHO_CADENCE': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`:hare` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [PARALLEL_POSSESSIVE_TIC] form=`:tortoise` — user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic
    - [AS_ONE_WHO_CADENCE] form=`:winner` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G1-08: Characters

- examples: 4
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 3, 'FORM_DISPLAY_AND_FORM_NOUN': 3}
    - [DOUBLE_NAME_INTRO] form=`\h` — character 'Watchdog the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`\T` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [DOUBLE_NAME_INTRO] form=`\T` — character 'Winston the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(char? \h)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(char? \h)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [DOUBLE_NAME_INTRO] form=`(char? \h)` — character 'Cashew the dog' introduced twice within 200 chars — drop the second 'the dog'

### G1-09: Symbols vs values

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'ONLY_SHOOK_HEAD_TIC': 1, 'HIGH_LENGTH': 3, 'BOOL_LEAK_RESOLUTION': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(symbol? 'hare)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [ONLY_SHOOK_HEAD_TIC] form=`(symbol? 'hare)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [LOW_GROUNDING] form=`(symbol? 'hare)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(symbol? 42)` — user_msg 245 words
    - [BOOL_LEAK_RESOLUTION] form=`(symbol? 42)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(symbol? "tortoise")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-10: Comments

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'LOW_GROUNDING': 1, 'DOUBLE_NAME_INTRO': 1}
    - [HIGH_LENGTH] form=`(+ 1 2) ;; sum of one and two` — user_msg 224 words
    - [CLAUSE_STACK_OVERFLOW] form=`(+ 1 2) ;; sum of one and two` — sentence with 5 commas reads as AI-output cadence: 'To add 2 and 9, with a double-semicolon trailing comment, she, her promise small'
    - [LOW_GROUNDING] form=`(+ 1 2) ;; sum of one and two` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(+ 1 2) ;; sum of one and two` — character 'Louie the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(+ 1 2) ;; sum of one and two` — sentence with 6 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'

### G1-11: Whitespace doesn't matter

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1, 'HIGH_LENGTH': 1, 'THE_FORM_OVERUSE': 1}
    - [DOUBLE_NAME_INTRO] form=`(+    1    2)` — character 'Riley the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [HIGH_LENGTH] form=`(+
  1
  2)` — user_msg 237 words
    - [THE_FORM_OVERUSE] form=`(+
  1
  2)` — `the form` appears 6 times in user_msg (template tic — vary references)

### G1-12: Parens group; they don't multiply

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 2, 'CLAUSE_STACK_OVERFLOW': 1, 'AS_ONE_WHO_CADENCE': 1, 'HIGH_LENGTH': 1, 'ANSWER_LEAK': 2}
    - [DOUBLE_NAME_INTRO] form=`(+ 2 3)` — character 'Topsy the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(+ 2 3)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'
    - [AS_ONE_WHO_CADENCE] form=`(+ 2 3)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [HIGH_LENGTH] form=`(* (+ 1 2) 3)` — user_msg 223 words
    - [ANSWER_LEAK] form=`(* (+ 1 2) 3)` — answer 9 in narrative
    - [ANSWER_LEAK] form=`(* (+ 1 2) 3)` — answer 9 in narrative

### G1-13: First arithmetic call

- examples: 6
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'REPL_AS_TIME_TRAVELLER': 3, 'NARRATIVE_NUMERAL_HARDCODE': 15, 'DOUBLE_NAME_INTRO': 1, 'RESOLUTION_GENERIC': 2, 'AS_ONE_WHO_CADENCE': 3, 'SENTENCE_START_LOWER_PRONOUN': 1}
    - [HIGH_LENGTH] form=`(+ 1 2)` — user_msg 201 words
    - [CLAUSE_STACK_OVERFLOW] form=`(+ 1 2)` — sentence with 5 commas reads as AI-output cadence: 'Snarler the dog, with steady, careful steps, arranged a small heap of bones\non t'
    - [REPL_AS_TIME_TRAVELLER] form=`(+ 1 2)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(- 5 3)` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(- 5 3)` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(- 5 3)` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count

### G1-14: Nested call evaluation

- examples: 4
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'ANSWER_LEAK': 1, 'DOUBLE_NAME_INTRO': 2, 'RESOLUTION_GENERIC': 3, 'PARALLEL_POSSESSIVE_TIC': 1, 'REPL_AS_TIME_TRAVELLER': 2, 'DOUBLE_EMO_INJECTION': 1, 'AS_ONE_WHO_CADENCE': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(+ 1 (* 2 3))` — user_msg 223 words
    - [ANSWER_LEAK] form=`(+ 1 (* 2 3))` — answer 7 in narrative
    - [HIGH_LENGTH] form=`(* (+ 1 2) (+ 3 4))` — user_msg 215 words
    - [DOUBLE_NAME_INTRO] form=`(* (+ 1 2) (+ 3 4))` — character 'Ditto the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [RESOLUTION_GENERIC] form=`(* (+ 1 2) (+ 3 4))` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    - [DOUBLE_NAME_INTRO] form=`(* (+ 1 2) (+ 3 4))` — character 'Doodle the dog' introduced twice within 200 chars — drop the second 'the dog'

### G1-15: Equality

- examples: 6
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'LOW_GROUNDING': 4, 'DOUBLE_NAME_INTRO': 9, 'CLAUSE_STACK_OVERFLOW': 1, 'AS_ONE_WHO_CADENCE': 2, 'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [WRONG_FABLE_LITERAL] form=`(= 1 1)` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [LOW_GROUNDING] form=`(= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(= 1 1)` — character 'Pip the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(= 1 1)` — character 'Pearl the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [DOUBLE_NAME_INTRO] form=`(= 1 2)` — character 'Teddy the dog' introduced twice within 200 chars — drop the second 'the dog'

### G1-16: Numeric predicates

- examples: 6
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 4, 'REPL_AS_TIME_TRAVELLER': 2, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 2, 'DOUBLE_EMO_INJECTION': 2, 'RESOLUTION_GENERIC': 3, 'BOOL_LEAK_RESOLUTION': 2}
    - [DOUBLE_NAME_INTRO] form=`(zero? 0)` — character 'Pumpkin the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [REPL_AS_TIME_TRAVELLER] form=`(zero? 0)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(zero? 5)` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(zero? 5)` — sentence with 5 commas reads as AI-output cadence: 'Gizmo the dog, stepping deliberately, one foot before the next, arranged a small'
    - [DOUBLE_EMO_INJECTION] form=`(zero? 5)` — sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(zero? 5)` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count

### G1-17: Printing vs returning

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [DOUBLE_NAME_INTRO] form=`(+ 1 2)` — character 'Mocha the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(+ 1 2)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'

### G1-18: Errors are safe in the REPL

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'AS_ONE_WHO_CADENCE': 1, 'LOW_GROUNDING': 1, 'DOUBLE_NAME_INTRO': 1}
    - [HIGH_LENGTH] form=`(* 7 6)` — user_msg 216 words
    - [AS_ONE_WHO_CADENCE] form=`(* 7 6)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [LOW_GROUNDING] form=`(* 7 6)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(* 7 6)` — character 'Pickle the dog' introduced twice within 200 chars — drop the second 'the dog'

## Grade 2

### G2-01: Multi-arg arithmetic

- examples: 6
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 12, 'CLAUSE_STACK_OVERFLOW': 2, 'LOW_GROUNDING': 8, 'DOUBLE_NAME_INTRO': 5, 'PARAGRAPH_FRAGMENTATION': 1, 'META_FILLER_RESOLUTION': 2, 'PARALLEL_POSSESSIVE_TIC': 1, 'REPL_AS_TIME_TRAVELLER': 1, 'RESOLUTION_GENERIC': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(+ 1 2 3 4)` — parametric example has hard-coded English numeral 'four bones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(+ 1 2 3 4)` — sentence with 5 commas reads as AI-output cadence: 'Bayer the dog, neither restless nor weary, only steady, arranged a small heap of'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(+ 1 2 3 4)` — parametric example has hard-coded English numeral 'four bones' in a story slot — the actual draws may differ from this fixed count
    - [LOW_GROUNDING] form=`(+ 1 2 3 4)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(+ 1 2 3 4)` — parametric example has hard-coded English numeral 'four bones' in a story slot — the actual draws may differ from this fixed count
    - [LOW_GROUNDING] form=`(+ 1 2 3 4)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-02: Comparison chains

- examples: 5
- variety @ n=50: 1.00
- issues: {'RESOLUTION_GENERIC': 3, 'HIGH_LENGTH': 4, 'BOOL_LEAK_RESOLUTION': 1, 'REPL_AS_TIME_TRAVELLER': 1, 'AS_ONE_WHO_CADENCE': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 3, 'PARALLEL_POSSESSIVE_TIC': 1, 'LOW_GROUNDING': 1, 'GENERIC_RESOLUTION_TAIL': 3}
    - [RESOLUTION_GENERIC] form=`(< 1 2 3)` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    - [HIGH_LENGTH] form=`(< 1 2 3)` — user_msg 203 words
    - [BOOL_LEAK_RESOLUTION] form=`(< 1 2 3)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [REPL_AS_TIME_TRAVELLER] form=`(< 3 2 1)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [RESOLUTION_GENERIC] form=`(< 3 2 1)` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    - [AS_ONE_WHO_CADENCE] form=`(< 3 2 1)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G2-03: not= and = with multiple args

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'REPL_AS_TIME_TRAVELLER': 4, 'BOOL_LEAK_RESOLUTION': 2, 'NARRATIVE_NUMERAL_HARDCODE': 9, 'CLAUSE_STACK_OVERFLOW': 3, 'AS_ONE_WHO_CADENCE': 1, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(not= 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [REPL_AS_TIME_TRAVELLER] form=`(not= 1 2)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [REPL_AS_TIME_TRAVELLER] form=`(not= 1 1)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [BOOL_LEAK_RESOLUTION] form=`(not= 1 1)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(not= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [BOOL_LEAK_RESOLUTION] form=`(= 1 1 1)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead

### G2-04: min and max

- examples: 5
- variety @ n=50: 1.00
- issues: {'REPL_AS_TIME_TRAVELLER': 1, 'RESOLUTION_GENERIC': 3, 'DOUBLE_NAME_INTRO': 3, 'CLAUSE_STACK_OVERFLOW': 5, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'PARALLEL_POSSESSIVE_TIC': 1}
    - [REPL_AS_TIME_TRAVELLER] form=`(min 1 2 3)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [RESOLUTION_GENERIC] form=`(max 1 2 3)` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    - [DOUBLE_NAME_INTRO] form=`(max 1 2 3)` — character 'Sniffer the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [RESOLUTION_GENERIC] form=`(min 7 3 9 1 5)` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    - [CLAUSE_STACK_OVERFLOW] form=`(min 7 3 9 1 5)` — sentence with 7 commas reads as AI-output cadence: 'A reflection lies; a tally does not." To find the minimum of 4, 3, 6, 0, and 4,\n'
    - [CLAUSE_STACK_OVERFLOW] form=`(min 7 3 9 1 5)` — sentence with 7 commas reads as AI-output cadence: 'A reflection lies; a tally does not." To find the minimum of 9, 7, 0, 6, and 0,\n'

### G2-05: quot, rem, mod

- examples: 6
- variety @ n=50: 1.00
- issues: {'RESOLUTION_GENERIC': 5, 'AS_ONE_WHO_CADENCE': 2, 'DOUBLE_NAME_INTRO': 3, 'REPL_AS_TIME_TRAVELLER': 3, 'SMALL_INT_LEAK': 1}
    - [RESOLUTION_GENERIC] form=`(quot 17 5)` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    - [AS_ONE_WHO_CADENCE] form=`(quot 17 5)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [DOUBLE_NAME_INTRO] form=`(quot 17 5)` — character 'Howler the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [REPL_AS_TIME_TRAVELLER] form=`(rem 17 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [RESOLUTION_GENERIC] form=`(rem 17 5)` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    - [RESOLUTION_GENERIC] form=`(rem 17 5)` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values

### G2-06: inc and dec

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'RESOLUTION_GENERIC': 4, 'DOUBLE_NAME_INTRO': 5, 'DOUBLE_EMO_INJECTION': 2, 'PARALLEL_POSSESSIVE_TIC': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'REPL_AS_TIME_TRAVELLER': 2}
    - [LOW_GROUNDING] form=`(inc 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [RESOLUTION_GENERIC] form=`(dec 5)` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    - [DOUBLE_NAME_INTRO] form=`(dec 5)` — character 'Acorn the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [DOUBLE_EMO_INJECTION] form=`(dec 5)` — sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat
    - [DOUBLE_NAME_INTRO] form=`(dec 5)` — character 'Buster the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [RESOLUTION_GENERIC] form=`(inc 0)` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values

### G2-07: Absolute value

- examples: 4
- variety @ n=50: 1.00
- issues: {'REPL_AS_TIME_TRAVELLER': 3, 'AS_ONE_WHO_CADENCE': 2, 'LOW_GROUNDING': 3, 'RESOLUTION_GENERIC': 1}
    - [REPL_AS_TIME_TRAVELLER] form=`(abs 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [AS_ONE_WHO_CADENCE] form=`(abs 5)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [REPL_AS_TIME_TRAVELLER] form=`(abs 5)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [AS_ONE_WHO_CADENCE] form=`(abs 5)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [LOW_GROUNDING] form=`(abs -5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [RESOLUTION_GENERIC] form=`(abs -5)` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values

### G2-08: Arithmetic on ratios

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 6, 'PARAGRAPH_FRAGMENTATION': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'REPL_AS_TIME_TRAVELLER': 1, 'DOUBLE_NAME_INTRO': 1, 'RESOLUTION_GENERIC': 1}
    - [LOW_GROUNDING] form=`(+ 1/2 1/4)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1/2 1/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1/2 1/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(+ 1/2 1/4)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [CLAUSE_STACK_OVERFLOW] form=`(+ 1/2 1/4)` — sentence with 5 commas reads as AI-output cadence: 'To add one-half and one-quarter, he, her breath even, her step even, her thought'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1/2 1/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)

### G2-09: Floats vs ints (the / operator)

- examples: 3
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'REPL_AS_TIME_TRAVELLER': 2, 'RESOLUTION_GENERIC': 1, 'AS_ONE_WHO_CADENCE': 1, 'DOUBLE_NAME_INTRO': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(/ 10 2)` — parametric example has hard-coded English numeral 'Ten bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(/ 10 2)` — parametric example has hard-coded English numeral 'Ten bones' in a story slot — the actual draws may differ from this fixed count
    - [REPL_AS_TIME_TRAVELLER] form=`(/ 10 2)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(/ 10 2)` — parametric example has hard-coded English numeral 'Ten bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(/ 10 3)` — parametric example has hard-coded English numeral 'three piles' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(/ 10 3)` — parametric example has hard-coded English numeral 'three piles' in a story slot — the actual draws may differ from this fixed count

### G2-10: Powers via repeated multiplication

- examples: 4
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'DOUBLE_NAME_INTRO': 3, 'LOW_GROUNDING': 1, 'AS_ONE_WHO_CADENCE': 1, 'RESOLUTION_GENERIC': 2, 'DOUBLE_EMO_INJECTION': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(* 2 2 2)` — sentence with 5 commas reads as AI-output cadence: 'To multiply 2 by itself three times, she, her breath even, her step even, her th'
    - [DOUBLE_NAME_INTRO] form=`(* 2 2 2)` — character 'Louie the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(* 3 3 3 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(* 3 3 3 3)` — character 'Bingo the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [DOUBLE_NAME_INTRO] form=`(* 3 3 3 3)` — character 'Max the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [AS_ONE_WHO_CADENCE] form=`(* 3 3 3 3)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G2-11: String concatenation with str

- examples: 4
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 2, 'CLAUSE_STACK_OVERFLOW': 5, 'AS_ONE_WHO_CADENCE': 1}
    - [DOUBLE_NAME_INTRO] form=`(str "ab" "cd")` — character 'Riley the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(str 42)` — sentence with 5 commas reads as AI-output cadence: 'Concat two strips\ntogether, and the marks are spliced; cut a substring out, and\n'
    - [CLAUSE_STACK_OVERFLOW] form=`(str 42)` — sentence with 5 commas reads as AI-output cadence: 'Concat two strips\ntogether, and the marks are spliced; cut a substring out, and\n'
    - [AS_ONE_WHO_CADENCE] form=`(str "p" "q" "r")` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [DOUBLE_NAME_INTRO] form=`(str "p" "q" "r")` — character 'Cocoa the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(str 1 "+" 2 "=" 3)` — sentence with 9 commas reads as AI-output cadence: 'Concat two strips\ntogether, and the marks are spliced; cut a substring out, and\n'

### G2-12: print and println — return values

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 2, 'HIGH_LENGTH': 1, 'AS_ONE_WHO_CADENCE': 1}
    - [DOUBLE_NAME_INTRO] form=`(println "hello")` — character 'Topsy the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [HIGH_LENGTH] form=`(println "hello")` — user_msg 202 words
    - [AS_ONE_WHO_CADENCE] form=`(println "hello")` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [DOUBLE_NAME_INTRO] form=`(println "hello")` — character 'Bounder the dog' introduced twice within 200 chars — drop the second 'the dog'

### G2-13: and / or — short circuit, return values

- examples: 6
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 3, 'DOUBLE_NAME_INTRO': 5, 'LOW_GROUNDING': 4, 'DOUBLE_EMO_INJECTION': 2, 'CLAUSE_STACK_OVERFLOW': 4, 'AS_ONE_WHO_CADENCE': 1}
    - [BOOL_LEAK_RESOLUTION] form=`(and true true)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [DOUBLE_NAME_INTRO] form=`(and true true)` — character 'Sooty the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(and true false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [BOOL_LEAK_RESOLUTION] form=`(and true false)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [DOUBLE_EMO_INJECTION] form=`(and true false)` — sentence has 2+ distinct EMO-pool phrases ('without complaint or hurry' + 'without complaint') — the character can't earn two emotional registers in the same beat
    - [CLAUSE_STACK_OVERFLOW] form=`(and true false)` — sentence with 6 commas reads as AI-output cadence: 'The verdict follows that\nrule exactly, the way a steady current keeps its line."'

### G2-14: not — turning truthy to false

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'DOUBLE_NAME_INTRO': 7, 'CLAUSE_STACK_OVERFLOW': 2, 'AS_ONE_WHO_CADENCE': 2}
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(not true)` — character 'Ace the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [DOUBLE_NAME_INTRO] form=`(not false)` — character 'Shadow the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(not false)` — sentence with 6 commas reads as AI-output cadence: 'The verdict follows that\nrule exactly, the way a steady current keeps its line."'
    - [AS_ONE_WHO_CADENCE] form=`(not false)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [AS_ONE_WHO_CADENCE] form=`(not nil)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G2-15: Falsey values: only false and nil

- examples: 4
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'DOUBLE_NAME_INTRO': 1, 'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [WRONG_FABLE_LITERAL] form=`(if 0 1 0)` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [DOUBLE_NAME_INTRO] form=`(if 0 1 0)` — character 'Pip the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [HIGH_LENGTH] form=`(if 0 1 0)` — user_msg 211 words
    - [CLAUSE_STACK_OVERFLOW] form=`(if 0 1 0)` — sentence with 5 commas reads as AI-output cadence: 'To use if to return 8 when the condition is 0 (then-branch) and 0 otherwise (els'

### G2-16: Truthy 0 and empty string

- examples: 4
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 2, 'AS_ONE_WHO_CADENCE': 1, 'LOW_GROUNDING': 4, 'CLAUSE_STACK_OVERFLOW': 2}
    - [DOUBLE_NAME_INTRO] form=`(boolean 0)` — character 'Pumpkin the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [AS_ONE_WHO_CADENCE] form=`(boolean 0)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [LOW_GROUNDING] form=`(boolean "")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(boolean "")` — sentence with 6 commas reads as AI-output cadence: 'The verdict follows that\nrule exactly, the way a steady current keeps its line."'
    - [CLAUSE_STACK_OVERFLOW] form=`(boolean "")` — sentence with 6 commas reads as AI-output cadence: 'The verdict follows that\nrule exactly, the way a steady current keeps its line."'
    - [LOW_GROUNDING] form=`(boolean nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-17: Keyword as function for map lookup

- examples: 3
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'AS_ONE_WHO_CADENCE': 1, 'PARALLEL_POSSESSIVE_TIC': 1}
    - [DOUBLE_NAME_INTRO] form=`(:hare {:hare 1 :tortoise 2})` — character 'Pathfinder the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(:hare {:hare 1 :tortoise 2})` — sentence with 6 commas reads as AI-output cadence: 'Pumpkin the dog, her breath even, her step even, her thought even, pointed to a '
    - [AS_ONE_WHO_CADENCE] form=`(:tortoise {:hare 1 :tortoise 2})` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [PARALLEL_POSSESSIVE_TIC] form=`(:missing {:hare 1})` — user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic

### G2-18: Quoting symbols

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'HIGH_LENGTH': 2, 'BOOL_LEAK_RESOLUTION': 2, 'CLAUSE_STACK_OVERFLOW': 7, 'DOUBLE_NAME_INTRO': 2, 'AS_ONE_WHO_CADENCE': 1, 'ONLY_SHOOK_HEAD_TIC': 1}
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(symbol? (quote hare))` — user_msg 229 words
    - [BOOL_LEAK_RESOLUTION] form=`(symbol? (quote hare))` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [CLAUSE_STACK_OVERFLOW] form=`(symbol? (quote hare))` — sentence with 5 commas reads as AI-output cadence: 'To ask whether long-form quoting of the name hare produces a symbol, using symbo'
    - [HIGH_LENGTH] form=`(symbol? (quote hare))` — user_msg 231 words
    - [BOOL_LEAK_RESOLUTION] form=`(symbol? (quote hare))` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead

### G2-19: Auto-promotion to bigint

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'REPL_AS_TIME_TRAVELLER': 2, 'DOUBLE_NAME_INTRO': 2, 'RESOLUTION_GENERIC': 2, 'AS_ONE_WHO_CADENCE': 1, 'META_FILLER_RESOLUTION': 1}
    - [HIGH_LENGTH] form=`(* 1000000 1000000)` — user_msg 204 words
    - [REPL_AS_TIME_TRAVELLER] form=`(* 1000000 1000000)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [DOUBLE_NAME_INTRO] form=`(* 1000000 1000000)` — character 'Inky the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [REPL_AS_TIME_TRAVELLER] form=`(* 1000000 1000000)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [RESOLUTION_GENERIC] form=`(+ 99999999999 1)` — user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    - [AS_ONE_WHO_CADENCE] form=`(+ 99999999999 1)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G2-20: Counting

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'CLAUSE_STACK_OVERFLOW': 6, 'HIGH_LENGTH': 1, 'AS_ONE_WHO_CADENCE': 2}
    - [LOW_GROUNDING] form=`(count [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3])` — sentence with 9 commas reads as AI-output cadence: 'The runtime does this for any collection — vector, list, map,\nstring." To count '
    - [LOW_GROUNDING] form=`(count [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3])` — sentence with 9 commas reads as AI-output cadence: 'The runtime does this for any collection — vector, list, map,\nstring." To count '
    - [HIGH_LENGTH] form=`(count [1 2 3])` — user_msg 241 words
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To count the elements in the vector containing 1, 2, and 3, she, as one who has '

### G2-21: String length and substring

- examples: 3
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'AS_ONE_WHO_CADENCE': 1, 'HIGH_LENGTH': 2}
    - [DOUBLE_NAME_INTRO] form=`(count "tortoise")` — character 'Biscuit the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(count "tortoise")` — sentence with 5 commas reads as AI-output cadence: 'Concat two strips\ntogether, and the marks are spliced; cut a substring out, and\n'
    - [CLAUSE_STACK_OVERFLOW] form=`(count "tortoise")` — sentence with 5 commas reads as AI-output cadence: 'Concat two strips\ntogether, and the marks are spliced; cut a substring out, and\n'
    - [AS_ONE_WHO_CADENCE] form=`(count "hare")` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [HIGH_LENGTH] form=`(count (subs "tortoise" 0 3))` — user_msg 204 words
    - [HIGH_LENGTH] form=`(count (subs "tortoise" 0 3))` — user_msg 205 words

### G2-22: Compose pure arithmetic (multi-step calculation)

- examples: 3
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'DOUBLE_NAME_INTRO': 1, 'HIGH_LENGTH': 2, 'ANSWER_LEAK': 2, 'DOUBLE_EMO_INJECTION': 1, 'REPL_AS_TIME_TRAVELLER': 2}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(- (* 5 4) 7)` — parametric example has hard-coded English numeral 'four piles' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(- (* 5 4) 7)` — parametric example has hard-coded English numeral 'four piles' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_NAME_INTRO] form=`(- (* 5 4) 7)` — character 'Nosey the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(- (* 5 4) 7)` — parametric example has hard-coded English numeral 'four piles' in a story slot — the actual draws may differ from this fixed count
    - [HIGH_LENGTH] form=`(+ (* 3 8) (* 2 4))` — user_msg 217 words
    - [ANSWER_LEAK] form=`(+ (* 3 8) (* 2 4))` — answer 32 in narrative

## Grade 3

### G3-02: def — redefinition

- examples: 1
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`(do (def x 1) (def x 99) x)` — character 'Houndsman the dog' introduced twice within 200 chars — drop the second 'the dog'

### G3-03: let — local binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 3, 'THE_FORM_OVERUSE': 2, 'DOUBLE_NAME_INTRO': 1, 'AS_ONE_WHO_CADENCE': 1}
    - [HIGH_LENGTH] form=`(let [x 3] (+ x 1))` — user_msg 269 words
    - [THE_FORM_OVERUSE] form=`(let [x 3] (+ x 1))` — `the form` appears 6 times in user_msg (template tic — vary references)
    - [DOUBLE_NAME_INTRO] form=`(let [n 10] (* n n))` — character 'Rex the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [HIGH_LENGTH] form=`(let [n 10] (* n n))` — user_msg 255 words
    - [HIGH_LENGTH] form=`(let [a 5] a)` — user_msg 252 words
    - [THE_FORM_OVERUSE] form=`(let [a 5] a)` — `the form` appears 6 times in user_msg (template tic — vary references)

### G3-04: let — multi-binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 3, 'CLAUSE_STACK_OVERFLOW': 3, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'ANSWER_LEAK': 1}
    - [HIGH_LENGTH] form=`(let [x 5 y 3] (- x y))` — user_msg 229 words
    - [CLAUSE_STACK_OVERFLOW] form=`(let [x 5 y 3] (- x y))` — sentence with 5 commas reads as AI-output cadence: 'To bind x to 4 and y to 7, then subtract y from x, he, with steady, careful step'
    - [HIGH_LENGTH] form=`(let [x 5 y 3] (- x y))` — user_msg 239 words
    - [HIGH_LENGTH] form=`(let [x 5 y 3] (- x y))` — user_msg 238 words
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [a 2 b 3 c 4] (+ a b c))` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [a 2 b 3 c 4] (+ a b c))` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count

### G3-05: let — shadowing outer def

- examples: 2
- variety @ n=50: 1.00
- issues: {'AS_ONE_WHO_CADENCE': 1, 'CLAUSE_STACK_OVERFLOW': 3, 'HIGH_LENGTH': 1, 'THE_FORM_OVERUSE': 1, 'LOW_GROUNDING': 1, 'DOUBLE_NAME_INTRO': 1}
    - [AS_ONE_WHO_CADENCE] form=`(do (def x 10) (let [x 99] x))` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def x 10) (let [x 99] x))` — sentence with 5 commas reads as AI-output cadence: 'Howler the dog, untroubled by what others thought,\nheld his grip steady and did '
    - [HIGH_LENGTH] form=`(do (def x 10) (let [x 99] x))` — user_msg 227 words
    - [THE_FORM_OVERUSE] form=`(do (def x 10) (let [x 99] x))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [LOW_GROUNDING] form=`(do (def x 10) (let [x 99] x) x)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do (def x 10) (let [x 99] x) x)` — character 'Buster the dog' introduced twice within 200 chars — drop the second 'the dog'

### G3-06: let — binding can reference prior

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'AS_ONE_WHO_CADENCE': 2, 'HIGH_LENGTH': 4, 'THE_FORM_OVERUSE': 4, 'CLAUSE_STACK_OVERFLOW': 5, 'DOUBLE_NAME_INTRO': 1, 'ANSWER_LEAK': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [a 5 b (* a 2)] b)` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [AS_ONE_WHO_CADENCE] form=`(let [a 5 b (* a 2)] b)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [HIGH_LENGTH] form=`(let [a 5 b (* a 2)] b)` — user_msg 274 words
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [a 5 b (* a 2)] b)` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [THE_FORM_OVERUSE] form=`(let [a 5 b (* a 2)] b)` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a 5 b (* a 2)] b)` — sentence with 5 commas reads as AI-output cadence: 'To bind a to 5, then bind b to twice a, and return b, she, in the slow rhythm of'

### G3-07: fn — anonymous function

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 2, 'AS_ONE_WHO_CADENCE': 1, 'CONCEPT_AS_VERB': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (+ x 1)) 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`((fn [x] (+ x 1)) 4)` — character 'Tucker the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (+ x 1)) 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`((fn [x] (+ x 1)) 4)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (+ x 1)) 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`((fn [a b] (* a b)) 3 4)` — character 'Zoomer the dog' introduced twice within 200 chars — drop the second 'the dog'

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
- issues: {'LOW_GROUNDING': 2, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 2, 'HIGH_LENGTH': 1, 'AS_ONE_WHO_CADENCE': 1}
    - [LOW_GROUNDING] form=`(do (defn dbl [x] (* x 2)) (dbl 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defn dbl [x] (* x 2)) (dbl 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — sentence with 6 commas reads as AI-output cadence: 'To define a function add3 that adds three arguments, then call it with 4, 8, and'
    - [HIGH_LENGTH] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — user_msg 257 words
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 1.00
- issues: {'PARAGRAPH_FRAGMENTATION': 1, 'CONCEPT_AS_VERB': 3, 'DOUBLE_NAME_INTRO': 2}
    - [PARAGRAPH_FRAGMENTATION] form=`(#(+ % 1) 5)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [CONCEPT_AS_VERB] form=`(#(+ % 1) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(#(+ % 1) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [DOUBLE_NAME_INTRO] form=`(#(* %1 %2) 3 4)` — character 'Louie the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CONCEPT_AS_VERB] form=`(#(* %1 %2) 3 4)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [DOUBLE_NAME_INTRO] form=`(#(* %1 %2) 3 4)` — character 'Bingo the dog' introduced twice within 200 chars — drop the second 'the dog'

### G3-11: Substitution rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'HIGH_LENGTH': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a 7] (+ a a))` — sentence with 5 commas reads as AI-output cadence: 'Riley the dog, with steady, careful steps,\nheld her grip steady and did the care'
    - [HIGH_LENGTH] form=`((fn [x] (* x x)) 6)` — user_msg 229 words

### G3-12: Scope vs namespace

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def g 5) (let [g 99] (+ g 1)))` — sentence with 6 commas reads as AI-output cadence: 'To define g at the top level, shadow it in a let with a different value, and com'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def g 5) (let [g 99] (+ g 1)))` — sentence with 5 commas reads as AI-output cadence: 'The next dog along the bank\nreads the freshest scratch — whatever the latest mar'

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
- issues: {'HIGH_LENGTH': 1, 'LOW_GROUNDING': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(do 1 2 3)` — user_msg 232 words
    - [LOW_GROUNDING] form=`(do 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do 1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'
    - [LOW_GROUNDING] form=`(do 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (+ 1 1) (+ 2 2) (+ 3 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G3-15: Side-effects in body

- examples: 1
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'LOW_GROUNDING': 2, 'DOUBLE_NAME_INTRO': 1, 'HIGH_LENGTH': 1, 'SENTENCE_START_LOWER_PRONOUN': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [WRONG_FABLE_LITERAL] form=`(do (println "hi") 42)` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [LOW_GROUNDING] form=`(do (println "hi") 42)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do (println "hi") 42)` — character 'Pip the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [HIGH_LENGTH] form=`(do (println "hi") 42)` — user_msg 236 words
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do (println "hi") 42)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [CLAUSE_STACK_OVERFLOW] form=`(do (println "hi") 42)` — sentence with 6 commas reads as AI-output cadence: 'To execute a print statement for side-effects, then return a different value, he'

### G3-16: Name collision: namespace vs let

- examples: 1
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1, 'LOW_GROUNDING': 1}
    - [DOUBLE_NAME_INTRO] form=`(let [+ 99] +)` — character 'Pumpkin the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(let [+ 99] +)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G3-17: Naming conventions (kebab-case)

- examples: 1
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`(let [hare-speed 4 tortoise-speed 1] (- hare-speed` — character 'Pathfinder the dog' introduced twice within 200 chars — drop the second 'the dog'

### G3-18: When to name vs inline

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'AS_ONE_WHO_CADENCE': 1, 'HIGH_LENGTH': 2, 'THE_FORM_OVERUSE': 2, 'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(let [n 5] (* n n n))` — sentence with 5 commas reads as AI-output cadence: 'Jet the dog, as a tortoise walks, neither hurrying nor stopping,\nheld her grip s'
    - [AS_ONE_WHO_CADENCE] form=`(let [n 5] (* n n n))` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [HIGH_LENGTH] form=`(let [n 5] (* n n n))` — user_msg 249 words
    - [THE_FORM_OVERUSE] form=`(let [n 5] (* n n n))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(* 5 5 5)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [HIGH_LENGTH] form=`(* 5 5 5)` — user_msg 218 words

## Grade 4

### G4-01: Vector literal

- examples: 3
- variety @ n=50: 1.00
- issues: {'PARAMETRIC_LITERAL_NUMERALS': 3, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'DOUBLE_EMO_INJECTION': 1}
    - [PARAMETRIC_LITERAL_NUMERALS] form=`[1 2 3]` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [NARRATIVE_NUMERAL_HARDCODE] form=`[1 2 3]` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [PARAMETRIC_LITERAL_NUMERALS] form=`[1 2 3]` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [NARRATIVE_NUMERAL_HARDCODE] form=`[1 2 3]` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [PARAMETRIC_LITERAL_NUMERALS] form=`[1 2 3]` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [NARRATIVE_NUMERAL_HARDCODE] form=`[1 2 3]` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count

### G4-02: nth — vector access

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'HIGH_LENGTH': 2, 'CLAUSE_STACK_OVERFLOW': 2}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 0)` — parametric example has hard-coded English numeral 'three bone' in a story slot — the actual draws may differ from this fixed count
    - [HIGH_LENGTH] form=`(nth [10 20 30] 0)` — user_msg 209 words
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 0)` — parametric example has hard-coded English numeral 'three bone' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(nth [10 20 30] 0)` — sentence with 5 commas reads as AI-output cadence: 'To get the element at index 0 of a vector containing 10, 20, and 30, she, with t'
    - [HIGH_LENGTH] form=`(nth [10 20 30] 0)` — user_msg 206 words
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 0)` — parametric example has hard-coded English numeral 'three bone' in a story slot — the actual draws may differ from this fixed count

### G4-03: conj — append to vector

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'PARAMETRIC_LITERAL_NUMERALS': 3, 'AS_ONE_WHO_CADENCE': 2, 'CLAUSE_STACK_OVERFLOW': 1, 'PARALLEL_POSSESSIVE_TIC': 1}
    - [HIGH_LENGTH] form=`(conj [1 2] 3)` — user_msg 207 words
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(conj [1 2] 3)` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [AS_ONE_WHO_CADENCE] form=`(conj [1 2] 3)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(conj [1 2] 3)` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [CLAUSE_STACK_OVERFLOW] form=`(conj [1 2] 3)` — sentence with 5 commas reads as AI-output cadence: 'Sprocket the dog, her face quiet, her hands quieter still, pointed to a hollow l'
    - [PARALLEL_POSSESSIVE_TIC] form=`(conj [1 2] 3)` — user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic

### G4-04: List literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 2, 'HANGING_FORM_THAT': 1, 'DOUBLE_NAME_INTRO': 2}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`'(1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'Skippy the dog, neither restless nor weary, only steady, pointed to a hollow log'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`'(1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'To create a list containing 1, 2, and 3\nproperly, he wrote a list literal carefu'
    - [HANGING_FORM_THAT] form=`'()` — 'form that <noun>' rendered without a verb — template should be 'form for {concept_phrase}'

### G4-05: cons — prepend to seq

- examples: 1
- variety @ n=50: 1.00
- issues: {'PARAMETRIC_LITERAL_NUMERALS': 3, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'DOUBLE_EMO_INJECTION': 2}
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(cons 0 '(1 2 3))` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(cons 0 '(1 2 3))` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_EMO_INJECTION] form=`(cons 0 '(1 2 3))` — sentence has 2+ distinct EMO-pool phrases ('without complaint or hurry' + 'without complaint') — the character can't earn two emotional registers in the same beat
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(cons 0 '(1 2 3))` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(cons 0 '(1 2 3))` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(cons 0 '(1 2 3))` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces

### G4-06: Map literal

- examples: 1
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`{:hare 1 :tortoise 2}` — character 'Keeper the dog' introduced twice within 200 chars — drop the second 'the dog'

### G4-07: get — map lookup

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 2}
    - [DOUBLE_NAME_INTRO] form=`(get {:a 1 :b 2} :a)` — character 'Tucker the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [DOUBLE_NAME_INTRO] form=`(get {:a 1} :missing :default)` — character 'Buster the dog' introduced twice within 200 chars — drop the second 'the dog'

### G4-08: assoc — map update

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_EMO_INJECTION': 1}
    - [DOUBLE_EMO_INJECTION] form=`(assoc {:a 1} :b 2)` — sentence has 2+ distinct EMO-pool phrases ('without complaint or hurry' + 'without complaint') — the character can't earn two emotional registers in the same beat

### G4-09: dissoc — map remove key

- examples: 1
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1, 'AS_ONE_WHO_CADENCE': 1}
    - [DOUBLE_NAME_INTRO] form=`(dissoc {:a 1 :b 2} :a)` — character 'Charlie the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [AS_ONE_WHO_CADENCE] form=`(dissoc {:a 1 :b 2} :a)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G4-10: keys and vals

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(count (keys {:a 1 :b 2 :c 3}))` — sentence with 5 commas reads as AI-output cadence: 'To count how many keys are in a map binding :a, :b, and :c, she, with the soft p'
    - [CLAUSE_STACK_OVERFLOW] form=`(count (keys {:a 1 :b 2 :c 3}))` — sentence with 5 commas reads as AI-output cadence: 'To count how many keys are in a map binding :a, :b, and :c\nproperly, he wrote co'

### G4-11: Set literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_EMO_INJECTION': 1, 'AS_ONE_WHO_CADENCE': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(count #{1 2 3})` — sentence with 5 commas reads as AI-output cadence: 'Alabaster the dog, as a millwheel turns, slow and sure, pointed to a hollow log '
    - [DOUBLE_EMO_INJECTION] form=`(count #{1 1 1})` — sentence has 2+ distinct EMO-pool phrases ('without complaint or hurry' + 'without complaint') — the character can't earn two emotional registers in the same beat
    - [AS_ONE_WHO_CADENCE] form=`(count #{1 1 1})` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G4-12: Set membership

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'CLAUSE_STACK_OVERFLOW': 3, 'DOUBLE_NAME_INTRO': 1, 'PARALLEL_POSSESSIVE_TIC': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(contains? #{1 2 3} 2)` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(contains? #{1 2 3} 2)` — sentence with 5 commas reads as AI-output cadence: 'To check whether 2 is a member of a set containing 1, 2, and 3\nproperly, he wrot'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(contains? #{1 2 3} 2)` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_NAME_INTRO] form=`(contains? #{1 2 3} 2)` — character 'Marble the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(contains? #{1 2 3} 2)` — sentence with 5 commas reads as AI-output cadence: 'Marble the dog, her face quiet, her hands quieter still, pointed to a hollow log'
    - [PARALLEL_POSSESSIVE_TIC] form=`(contains? #{1 2 3} 2)` — user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic

### G4-13: count — universal

- examples: 4
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 3, 'DOUBLE_NAME_INTRO': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count [1 2 3 4 5])` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3 4 5])` — sentence with 7 commas reads as AI-output cadence: 'To count the elements in a vector containing 1, 2, 3, 4, and 5, he, as a hen sit'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count [1 2 3 4 5])` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count [1 2 3 4 5])` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_NAME_INTRO] form=`(count {:a 1 :b 2})` — character 'Plum the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(count #{:a :b :c})` — sentence with 5 commas reads as AI-output cadence: 'To count the elements in a set containing the keywords :a, :b, and :c\nproperly, '

### G4-14: empty?

- examples: 3
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 3, 'AS_ONE_WHO_CADENCE': 2, 'DOUBLE_NAME_INTRO': 1}
    - [BOOL_LEAK_RESOLUTION] form=`(empty? [])` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [AS_ONE_WHO_CADENCE] form=`(empty? [])` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [AS_ONE_WHO_CADENCE] form=`(empty? [])` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [BOOL_LEAK_RESOLUTION] form=`(empty? [1])` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [BOOL_LEAK_RESOLUTION] form=`(empty? [1])` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [DOUBLE_NAME_INTRO] form=`(empty? [1])` — character 'Pickles the dog' introduced twice within 200 chars — drop the second 'the dog'

### G4-15: first, rest, last

- examples: 3
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'NARRATIVE_NUMERAL_HARDCODE': 9, 'CLAUSE_STACK_OVERFLOW': 4, 'DOUBLE_NAME_INTRO': 1}
    - [WRONG_FABLE_LITERAL] form=`(first [10 20 30])` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(first [10 20 30])` — parametric example has hard-coded English numeral 'three bone' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(first [10 20 30])` — parametric example has hard-coded English numeral 'three bone' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(first [10 20 30])` — sentence with 6 commas reads as AI-output cadence: 'To get the first element of a vector containing 10, 20, and 30, she, neither res'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(first [10 20 30])` — parametric example has hard-coded English numeral 'three bone' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_NAME_INTRO] form=`(first [10 20 30])` — character 'Wallace the dog' introduced twice within 200 chars — drop the second 'the dog'

### G4-16: into and conj on collections

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'DOUBLE_NAME_INTRO': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(into [] '(1 2 3))` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_NAME_INTRO] form=`(into [] '(1 2 3))` — character 'Pumpkin the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(into [] '(1 2 3))` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(into [] '(1 2 3))` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_NAME_INTRO] form=`(into [] '(1 2 3))` — character 'Tippet the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] '(1 2 3))` — sentence with 6 commas reads as AI-output cadence: 'The receiver is patient; the gap is exact." To\nconvert a list containing 1, 2, a'

### G4-17: Immutability — assoc returns new

- examples: 1
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`(let [m {:a 1}] (assoc m :a 99) m)` — character 'Pathfinder the dog' introduced twice within 200 chars — drop the second 'the dog'

### G4-18: Equality of vectors and lists

- examples: 1
- variety @ n=50: 1.00
- issues: {'PARALLEL_POSSESSIVE_TIC': 1}
    - [PARALLEL_POSSESSIVE_TIC] form=`(= [1 2 3] '(1 2 3))` — user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic

### G4-19: range and seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 2, 'DOUBLE_NAME_INTRO': 1, 'AS_ONE_WHO_CADENCE': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (range 5))` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(count (range 5))` — sentence with 6 commas reads as AI-output cadence: 'The range is a promise of five bones (0, 1, 2, 3, 4), and count consumes that pr'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (range 5))` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (range 5))` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(count (range 5))` — sentence with 6 commas reads as AI-output cadence: 'The range is a promise of five bones (0, 1, 2, 3, 4), and count consumes that pr'
    - [DOUBLE_NAME_INTRO] form=`(first (range 1 100))` — character 'Barker the dog' introduced twice within 200 chars — drop the second 'the dog'

### G4-20: Collection vs sequence

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'AS_ONE_WHO_CADENCE': 1, 'DOUBLE_NAME_INTRO': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(count (seq [1 2 3]))` — sentence with 5 commas reads as AI-output cadence: 'To convert a vector containing 1, 2, and 3 to a sequence and count its elements\n'
    - [AS_ONE_WHO_CADENCE] form=`(count (seq [1 2 3]))` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [CLAUSE_STACK_OVERFLOW] form=`(count (seq [1 2 3]))` — sentence with 5 commas reads as AI-output cadence: 'To convert a vector containing 1, 2, and 3 to a sequence and count its elements\n'
    - [DOUBLE_NAME_INTRO] form=`(seq [])` — character 'Snowball the dog' introduced twice within 200 chars — drop the second 'the dog'

## Grade 5

### G5-01: if

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'LOW_GROUNDING': 3, 'DOUBLE_NAME_INTRO': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'HIGH_LENGTH': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(if true :a :b)` — sentence with 5 commas reads as AI-output cadence: 'The runtime checks the\ncondition, walks the right arm, and the unrun arm is just'
    - [LOW_GROUNDING] form=`(if true :a :b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(if true :a :b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(if false :a :b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(if false :a :b)` — sentence with 5 commas reads as AI-output cadence: 'The runtime checks the\ncondition, walks the right arm, and the unrun arm is just'
    - [DOUBLE_NAME_INTRO] form=`(if false :a :b)` — character 'Pippin the dog' introduced twice within 200 chars — drop the second 'the dog'

### G5-02: if as expression

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(+ 1 (if true 10 20))` — user_msg 253 words

### G5-03: when

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'AS_ONE_WHO_CADENCE': 1, 'LOW_GROUNDING': 2}
    - [HIGH_LENGTH] form=`(when true :yes)` — user_msg 224 words
    - [AS_ONE_WHO_CADENCE] form=`(when true :yes)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [LOW_GROUNDING] form=`(when true :yes)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(when false :yes)` — user_msg 219 words
    - [LOW_GROUNDING] form=`(when false :yes)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G5-04: cond

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — sentence with 5 commas reads as AI-output cadence: 'Whatever the condition evaluates to, that\ndecides." To walk three condition-ston'

### G5-05: cond — :else

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(cond false :a false :b :else :c)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(cond false :a false :b :else :c)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(cond false :a false :b :else :c)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(cond false :a false :b :else :c)` — sentence with 5 commas reads as AI-output cadence: 'The runtime checks the\ncondition, walks the right arm, and the unrun arm is just'

### G5-06: case

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'CLAUSE_STACK_OVERFLOW': 3, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(case 2 1 :one 2 :two 3 :three :default)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(case 2 1 :one 2 :two 3 :three :default)` — sentence with 5 commas reads as AI-output cadence: 'The runtime checks the\ncondition, walks the right arm, and the unrun arm is just'
    - [LOW_GROUNDING] form=`(case 2 1 :one 2 :two 3 :three :default)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(case 99 1 :one 2 :two :default)` — sentence with 5 commas reads as AI-output cadence: 'The runtime checks the\ncondition, walks the right arm, and the unrun arm is just'
    - [DOUBLE_NAME_INTRO] form=`(case 99 1 :one 2 :two :default)` — character 'Pouncer the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(case 99 1 :one 2 :two :default)` — sentence with 5 commas reads as AI-output cadence: 'The runtime checks the\ncondition, walks the right arm, and the unrun arm is just'

### G5-07: and / or as control flow

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(and 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(or nil false :found)` — user_msg 232 words
    - [CLAUSE_STACK_OVERFLOW] form=`(or nil false :found)` — sentence with 6 commas reads as AI-output cadence: 'The REPL let the crossing-conditions decide:\n\nThe REPL walked the first gate, fo'

### G5-08: not

- examples: 1
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [DOUBLE_NAME_INTRO] form=`(not (> 1 2))` — character 'Watchdog the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [DOUBLE_NAME_INTRO] form=`(not (> 1 2))` — character 'Snowball the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(not (> 1 2))` — sentence with 6 commas reads as AI-output cadence: 'The verdict follows that\nrule exactly, the way a steady current keeps its line."'

### G5-10: map

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'COLLECTION_LEAK': 1, 'CLAUSE_STACK_OVERFLOW': 3, 'AS_ONE_WHO_CADENCE': 1}
    - [HIGH_LENGTH] form=`(map inc [1 2 3])` — user_msg 227 words
    - [COLLECTION_LEAK] form=`(map inc [1 2 3])` — elements of expected [2, 3, 4] appear comma-separated in user_msg (collection answer leak)
    - [CLAUSE_STACK_OVERFLOW] form=`(map inc [1 2 3])` — sentence with 8 commas reads as AI-output cadence: 'To pour the vector containing 1, 2, 3 through a sieve whose rule is inc, collect'
    - [CLAUSE_STACK_OVERFLOW] form=`(map inc [1 2 3])` — sentence with 7 commas reads as AI-output cadence: 'Zoomer the dog shook\nhis head and went on with the work: to pour the vector cont'
    - [CLAUSE_STACK_OVERFLOW] form=`(map #(* % %) [1 2 3 4])` — sentence with 8 commas reads as AI-output cadence: 'Leaper the dog shook\nhis head and went on with the work: to apply a squaring ope'
    - [AS_ONE_WHO_CADENCE] form=`(map #(* % %) [1 2 3 4])` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G5-11: filter

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'LOW_GROUNDING': 1, 'DOUBLE_NAME_INTRO': 1, 'AS_ONE_WHO_CADENCE': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(filter even? [1 2 3 4])` — sentence with 7 commas reads as AI-output cadence: 'The receiver is patient; the gap is exact." To\nkeep the even elements from the v'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(filter pos? [-2 -1 0 1 2])` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(filter pos? [-2 -1 0 1 2])` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [LOW_GROUNDING] form=`(filter pos? [-2 -1 0 1 2])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(filter pos? [-2 -1 0 1 2])` — character 'Noodle the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(filter pos? [-2 -1 0 1 2])` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count

### G5-12: reduce

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 6, 'ANSWER_LEAK': 2, 'CLAUSE_STACK_OVERFLOW': 9, 'LOW_GROUNDING': 1, 'DOUBLE_EMO_INJECTION': 1, 'AS_ONE_WHO_CADENCE': 1}
    - [HIGH_LENGTH] form=`(reduce + [1 2 3 4])` — user_msg 265 words
    - [ANSWER_LEAK] form=`(reduce + [1 2 3 4])` — answer 10 in narrative
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + [1 2 3 4])` — sentence with 6 commas reads as AI-output cadence: 'To walk the row of pebbles 1, 2, 3, 4 carrying a tally that combines each with +'
    - [HIGH_LENGTH] form=`(reduce + [1 2 3 4])` — user_msg 257 words
    - [ANSWER_LEAK] form=`(reduce + [1 2 3 4])` — answer 10 in narrative
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + [1 2 3 4])` — sentence with 6 commas reads as AI-output cadence: 'To walk the row of pebbles 1, 2, 3, 4 carrying a tally that combines each with +'

### G5-13: reduce with init

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'ANSWER_LEAK': 1, 'CLAUSE_STACK_OVERFLOW': 3, 'DOUBLE_NAME_INTRO': 2, 'LOW_GROUNDING': 1}
    - [HIGH_LENGTH] form=`(reduce + 100 [1 2 3])` — user_msg 231 words
    - [ANSWER_LEAK] form=`(reduce + 100 [1 2 3])` — answer 106 in narrative
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + 100 [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To fold + over the vector containing 1, 2, 3 starting from an initial accumulato'
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + 100 [1 2 3])` — sentence with 9 commas reads as AI-output cadence: 'The runtime does this for any collection — vector, list, map,\nstring." To fold +'
    - [DOUBLE_NAME_INTRO] form=`(reduce + 100 [1 2 3])` — character 'Jasper the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + 100 [1 2 3])` — sentence with 9 commas reads as AI-output cadence: 'The runtime does this for any collection — vector, list, map,\nstring." To fold +'

### G5-14: apply

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 3, 'NARRATIVE_NUMERAL_HARDCODE': 6, 'CLAUSE_STACK_OVERFLOW': 4, 'AS_ONE_WHO_CADENCE': 2, 'LOW_GROUNDING': 1, 'DOUBLE_NAME_INTRO': 1}
    - [HIGH_LENGTH] form=`(apply + [1 2 3 4])` — user_msg 244 words
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply + [1 2 3 4])` — parametric example has hard-coded English numeral 'four bones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(apply + [1 2 3 4])` — sentence with 6 commas reads as AI-output cadence: 'To apply + to the elements of the vector containing 1, 2, 3, and 4, he, in the p'
    - [AS_ONE_WHO_CADENCE] form=`(apply + [1 2 3 4])` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply + [1 2 3 4])` — parametric example has hard-coded English numeral 'four bones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(apply + [1 2 3 4])` — sentence with 6 commas reads as AI-output cadence: 'To apply + to the elements of the vector containing 1, 2, 3, and 4, he composed\n'

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
- issues: {'PARALLEL_POSSESSIVE_TIC': 1, 'DOUBLE_NAME_INTRO': 1, 'HIGH_LENGTH': 2, 'PREDICATE_QUESTION_COLLISION': 2, 'CLAUSE_STACK_OVERFLOW': 2}
    - [PARALLEL_POSSESSIVE_TIC] form=`(some even? [1 3 5 8 7])` — user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic
    - [DOUBLE_NAME_INTRO] form=`(some even? [1 3 5 8 7])` — character 'Almond the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [HIGH_LENGTH] form=`(some neg? [1 2 3])` — user_msg 236 words
    - [PREDICATE_QUESTION_COLLISION] form=`(some neg? [1 2 3])` — predicate-suffix ``?`` collides with the question framing's trailing ``?`` or ``.``
    - [CLAUSE_STACK_OVERFLOW] form=`(some neg? [1 2 3])` — sentence with 7 commas reads as AI-output cadence: 'To check if any element in the vector containing 1, 2, and 3 is negative, she, w'
    - [HIGH_LENGTH] form=`(some neg? [1 2 3])` — user_msg 237 words

### G5-19: every?

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'PREDICATE_QUESTION_COLLISION': 1, 'BOOL_LEAK_RESOLUTION': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_EMO_INJECTION': 1, 'DOUBLE_NAME_INTRO': 1, 'PARALLEL_POSSESSIVE_TIC': 1, 'LOW_GROUNDING': 1}
    - [HIGH_LENGTH] form=`(every? pos? [1 2 3])` — user_msg 232 words
    - [PREDICATE_QUESTION_COLLISION] form=`(every? pos? [1 2 3])` — predicate-suffix ``?`` collides with the question framing's trailing ``?`` or ``.``
    - [BOOL_LEAK_RESOLUTION] form=`(every? pos? [1 2 3])` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [CLAUSE_STACK_OVERFLOW] form=`(every? pos? [1 2 3])` — sentence with 7 commas reads as AI-output cadence: 'To check if all elements in the vector containing 1, 2, and 3 are positive, she,'
    - [DOUBLE_EMO_INJECTION] form=`(every? pos? [1 2 3])` — sentence has 2+ distinct EMO-pool phrases ('without complaint or hurry' + 'without complaint') — the character can't earn two emotional registers in the same beat
    - [DOUBLE_NAME_INTRO] form=`(every? pos? [1 2 3])` — character 'Tracksman the dog' introduced twice within 200 chars — drop the second 'the dog'

### G5-20: take and drop

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'CLAUSE_STACK_OVERFLOW': 3, 'DOUBLE_NAME_INTRO': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(take 3 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(take 3 [10 20 30 40 50])` — sentence with 8 commas reads as AI-output cadence: 'Zoomer the dog shook\nhis head and went on with the work: to take the first 3 ele'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(take 3 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(take 3 [10 20 30 40 50])` — sentence with 8 commas reads as AI-output cadence: 'Slate the dog shook\nhis head and went on with the work: to take the first 3 elem'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(take 3 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(drop 2 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count

### G5-21: distinct and sort

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 2, 'CLAUSE_STACK_OVERFLOW': 5, 'AS_ONE_WHO_CADENCE': 2}
    - [DOUBLE_NAME_INTRO] form=`(distinct [1 1 2 3 3 4])` — character 'Biscuit the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(distinct [1 1 2 3 3 4])` — sentence with 9 commas reads as AI-output cadence: 'The receiver is patient; the gap is exact." To\nremove duplicate elements from th'
    - [AS_ONE_WHO_CADENCE] form=`(distinct [1 1 2 3 3 4])` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [CLAUSE_STACK_OVERFLOW] form=`(distinct [1 1 2 3 3 4])` — sentence with 9 commas reads as AI-output cadence: 'Marley the dog shook\nhis head and went on with the work: to remove duplicate ele'
    - [DOUBLE_NAME_INTRO] form=`(distinct [1 1 2 3 3 4])` — character 'Warden the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(distinct [1 1 2 3 3 4])` — sentence with 5 commas reads as AI-output cadence: 'What Clojure form computes the sequence produced by passing 1, 1, 2, 3, 3, 4 thr'

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
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(clojure.string/upper-case "hare")` — user_msg 208 words

### G6-04: refer and use

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(= (clojure.string/upper-case "x") (clojure.string` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= (clojure.string/upper-case "x") (clojure.string` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-05: Fully qualified names

- examples: 4
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 2, 'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 3, 'ANSWER_LEAK_STRING': 2}
    - [DOUBLE_NAME_INTRO] form=`(clojure.string/upper-case "hello")` — character 'Howler the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/reverse "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(clojure.string/reverse "abc")` — character 'Howler the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/reverse "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/reverse "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(namespace :owner/item)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-07: Public vs private API

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 2, 'AS_ONE_WHO_CADENCE': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta '^:private hidden)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private', ':private'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(boolean (:private (meta '^:private hidden)))` — character 'Tucker the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta '^:private hidden)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private', ':private'), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(boolean (:private (meta '^:private hidden)))` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta '^:private hidden)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private', ':private'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta 'public)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private',), resolution doesn't close the loop)

### G6-08: Circular dependencies

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(= 'a.b 'a.b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 'a.b 'a.b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-09: Loading order

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 2}
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(let [a 1 b (+ a 1)] (+ a b))` — character 'Peach the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a 1 b (+ a 1)] (+ a b))` — sentence with 6 commas reads as AI-output cadence: 'To bind a to 1, bind b to a plus 1, then return the sum of a and b, the\nscratch '
    - [LOW_GROUNDING] form=`(let [a 1 b (+ a 1)] (+ a b))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-10: Leiningen and deps.edn

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 2, 'LOW_GROUNDING': 1, 'HEDGING_NEAR_FORM': 1}
    - [DOUBLE_NAME_INTRO] form=`(:deps {:deps {:a 1 :b 2}})` — character 'Cream the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(:deps {:deps {:a 1 :b 2}})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(:deps {:deps {:a 1 :b 2}})` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [DOUBLE_NAME_INTRO] form=`(get-in {:paths ["src"]} [:paths 0])` — character 'Cream the dog' introduced twice within 200 chars — drop the second 'the dog'

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
- issues: {'HIGH_LENGTH': 2, 'AS_ONE_WHO_CADENCE': 1}
    - [HIGH_LENGTH] form=`(let [s clojure.string/upper-case] (s "hare"))` — user_msg 219 words
    - [HIGH_LENGTH] form=`(let [s clojure.string/upper-case] (s "hare"))` — user_msg 225 words
    - [AS_ONE_WHO_CADENCE] form=`(let [s clojure.string/upper-case] (s "hare"))` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G6-14: Import for host classes

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'LOW_GROUNDING': 3, 'AS_ONE_WHO_CADENCE': 2, 'DOUBLE_NAME_INTRO': 1}
    - [HIGH_LENGTH] form=`(symbol? 'java.util.List)` — user_msg 223 words
    - [CLAUSE_STACK_OVERFLOW] form=`(symbol? 'java.util.List)` — sentence with 5 commas reads as AI-output cadence: 'To test whether a Java class name written as a quoted symbol is a symbol, he, go'
    - [LOW_GROUNDING] form=`(symbol? 'java.util.List)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [AS_ONE_WHO_CADENCE] form=`(symbol? 'java.util.List)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [LOW_GROUNDING] form=`(name 'java.util.Map)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(name 'java.util.Map)` — character 'Shadow the dog' introduced twice within 200 chars — drop the second 'the dog'

### G6-15: Namespace meta

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 2, 'HIGH_LENGTH': 1}
    - [WRONG_FABLE_LITERAL] form=`(:doc (meta '\{:doc "steady wins"\} race))` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:doc (meta '\{:doc "steady wins"\} race))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':doc', ':doc', 'steady wins'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(:doc (meta '\{:doc "steady wins"\} race))` — character 'Pip the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:doc (meta '\{:doc "steady wins"\} race))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':doc', ':doc', 'steady wins'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(:doc (meta '\{:doc "steady wins"\} race))` — user_msg 229 words
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
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1}
    - [LOW_GROUNDING] form=`(try (throw (Exception. "bad")) (catch Exception e` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "bad")) (catch Exception e` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1', 'bad'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(try (throw (Exception. "bad")) (catch Exception e` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "bad")) (catch Exception e` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1', 'bad'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(try (throw (Exception. "bad")) (catch Exception e` — user_msg 210 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "bad")) (catch Exception e` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1', 'bad'), resolution doesn't close the loop)

### G7-02: try / catch

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'AS_ONE_WHO_CADENCE': 1, 'LOW_GROUNDING': 3, 'DOUBLE_NAME_INTRO': 1}
    - [HIGH_LENGTH] form=`(try (/ 1 0) (catch Exception e -1))` — user_msg 211 words
    - [AS_ONE_WHO_CADENCE] form=`(try (/ 1 0) (catch Exception e -1))` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [LOW_GROUNDING] form=`(try 42 (catch Exception e :caught))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try 42 (catch Exception e :caught))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(try 42 (catch Exception e :caught))` — character 'Milo the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(try 42 (catch Exception e :caught))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-03: try / finally

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'AS_ONE_WHO_CADENCE': 1, 'LOW_GROUNDING': 3}
    - [HIGH_LENGTH] form=`(try 7 (finally (prn :cleanup)))` — user_msg 221 words
    - [AS_ONE_WHO_CADENCE] form=`(try 7 (finally (prn :cleanup)))` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
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
- issues: {'LOW_GROUNDING': 9, 'AS_ONE_WHO_CADENCE': 1, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(some? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(some? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(some? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(some? 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(first nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [AS_ONE_WHO_CADENCE] form=`(first nil)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

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
- issues: {'LOW_GROUNDING': 1, 'DOUBLE_NAME_INTRO': 1, 'AS_ONE_WHO_CADENCE': 1, 'CLAUSE_STACK_OVERFLOW': 2}
    - [LOW_GROUNDING] form=`(do (assert (= 1 1)) 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do (assert (= 1 1)) 1)` — character 'Tucker the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [AS_ONE_WHO_CADENCE] form=`(do (assert (= 1 1)) 1)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [CLAUSE_STACK_OVERFLOW] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — sentence with 5 commas reads as AI-output cadence: 'To\nassert that 7 equals 9, catch the failure, and return a numeric code required'
    - [CLAUSE_STACK_OVERFLOW] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — sentence with 5 commas reads as AI-output cadence: 'The REPL is forgiving in a\nway that a real crossing is not." To assert that 0 eq'

### G7-08: prn and pprint

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_NAME_INTRO': 1}
    - [HIGH_LENGTH] form=`(with-out-str (prn 42))` — user_msg 206 words
    - [CLAUSE_STACK_OVERFLOW] form=`(with-out-str (prn 42))` — sentence with 5 commas reads as AI-output cadence: 'To print the number 42 and capture the output string, he, her breath even, her s'
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
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3, 'AS_ONE_WHO_CADENCE': 1, 'ANSWER_LEAK_STRING': 1}
    - [LOW_GROUNDING] form=`(try (throw (Exception. "oops")) (catch Exception ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(try (throw (Exception. "oops")) (catch Exception ` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)
    - [ANSWER_LEAK_STRING] form=`(try (throw (ex-info "trouble" {})) (catch Excepti` — answer string 'trouble' appears in user_msg

### G7-12: slurp and spit

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'DOUBLE_NAME_INTRO': 2, 'CLAUSE_STACK_OVERFLOW': 2, 'ANSWER_LEAK': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(count "hare
tortoise
")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(count "hare
tortoise
")` — character 'Topsy the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(count "hare
tortoise
")` — sentence with 5 commas reads as AI-output cadence: 'Message-bones are how the two meet — a\nvalue crosses out and becomes scratches o'
    - [ANSWER_LEAK] form=`(count "hare
tortoise
")` — answer 14 in narrative
    - [CLAUSE_STACK_OVERFLOW] form=`(count "hare
tortoise
")` — sentence with 5 commas reads as AI-output cadence: 'To count every character in a two-line string ending each line with a newline-ma'
    - [LOW_GROUNDING] form=`(count "hare
tortoise
")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-13: line-seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 4, 'DOUBLE_NAME_INTRO': 1, 'DOUBLE_EMO_INJECTION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(count (clojure.string/split-lines "a\nb\nc"))` — character 'Sooty the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)

### G7-14: with-open

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'LOW_GROUNDING': 2}
    - [HIGH_LENGTH] form=`(with-out-str (println "hare"))` — user_msg 211 words
    - [LOW_GROUNDING] form=`(with-out-str (println "hare"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (println "hare"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-15: *in* and *out*

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'LOW_GROUNDING': 5, 'DOUBLE_NAME_INTRO': 2}
    - [WRONG_FABLE_LITERAL] form=`(with-out-str (print "x"))` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [LOW_GROUNDING] form=`(with-out-str (print "x"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(with-out-str (print "x"))` — character 'Pip the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(with-out-str (print "x"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (println))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(with-out-str (println))` — character 'Pearl the dog' introduced twice within 200 chars — drop the second 'the dog'

### G7-16: edn read

- examples: 3
- variety @ n=50: 1.00
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
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 4, 'HIGH_LENGTH': 1, 'DOUBLE_NAME_INTRO': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — user_msg 213 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-18: Shell command

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'DOUBLE_NAME_INTRO': 2}
    - [LOW_GROUNDING] form=`(:cmd {:cmd "ls" :args ["-l"]})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(:cmd {:cmd "ls" :args ["-l"]})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(:cmd {:cmd "ls" :args ["-l"]})` — character 'Almond the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(:cmd {:cmd "ls" :args ["-l"]})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count (:args {:cmd "echo" :args ["hello" "world"]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count (:args {:cmd "echo" :args ["hello" "world"]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 8

### G8-01: Why polymorphism

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1, 'LOW_GROUNDING': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':tortoise', ':else'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':tortoise', ':else'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — user_msg 227 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':tortoise', ':else'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(let [speak (fn [k] (cond (= k :hare) "swift" (= k` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [speak (fn [k] (cond (= k :hare) "swift" (= k` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-02: deftype introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 2, 'HIGH_LENGTH': 1, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — sentence with 5 commas reads as AI-output cadence: 'Faster,\nmore focused, less convenient." To define a type Pebble with a color fie'
    - [LOW_GROUNDING] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-03: defrecord introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'ANSWER_LEAK_STRING': 1, 'STORY_RESOLUTION_NO_DRAWN': 6, 'AS_ONE_WHO_CADENCE': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'LOW_GROUNDING': 3}
    - [HIGH_LENGTH] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — user_msg 229 words
    - [ANSWER_LEAK_STRING] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — answer string ':slow' appears in user_msg
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':pace', ':slow', 'Alice'), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':pace', ':slow', 'Alice'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':pace', ':slow', 'Alice'), resolution doesn't close the loop)

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
- issues: {'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 5}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('swift', 'hare'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 6 commas reads as AI-output cadence: 'The runtime looks up which breed the\ndog is, then runs that breed\'s answer." To '
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('swift', 'hare'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-06: Protocol method dispatch

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 6, 'LOW_GROUNDING': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'Any dog\nthat learns the signals may join the pack." To define a protocol Pace wi'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, extend it to both String and Long t'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 6 commas reads as AI-output cadence: 'The runtime looks up which breed the\ndog is, then runs that breed\'s answer." To '

### G8-07: Record implementing protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 2, 'CLAUSE_STACK_OVERFLOW': 4, 'AS_ONE_WHO_CADENCE': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':swift', 'Pip'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — character 'Tucker the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':swift', 'Pip'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, define a record Hare that implement'
    - [AS_ONE_WHO_CADENCE] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G8-08: Multimethod defmulti

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 4, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmulti pace :species) (defmethod pace :hare` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':species', ':hare', ':swift'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(do (defmulti pace :species) (defmethod pace :hare` — user_msg 225 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmulti pace :species) (defmethod pace :hare` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':species', ':hare', ':swift'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 5 commas reads as AI-output cadence: "To declare a sorting-table named pace that reads each runner's :species stamp; a"
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmulti pace :species) (defmethod pace :hare` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':species', ':hare', ':swift'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 5 commas reads as AI-output cadence: 'The runtime reads it, finds the matching pile,\nand runs that one." To declare a '

### G8-09: Multimethod defmethod

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 5, 'DOUBLE_NAME_INTRO': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 6 commas reads as AI-output cadence: 'The runtime reads it, finds the matching pile,\nand runs that one." To define a m'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 5 commas reads as AI-output cadence: 'To define a multimethod pace that dispatches on :species with methods for both :'
    - [DOUBLE_NAME_INTRO] form=`(do (defmulti pace :species) (defmethod pace :hare` — character 'Mochi the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 6 commas reads as AI-output cadence: 'The runtime reads it, finds the matching pile,\nand runs that one." To define a m'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 6 commas reads as AI-output cadence: 'The runtime reads it, finds the matching pile,\nand runs that one." To define a m'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 6 commas reads as AI-output cadence: 'The runtime reads it, finds the matching pile,\nand runs that one." To define a m'

### G8-10: Multimethod vs protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 3, 'LOW_GROUNDING': 3, 'DOUBLE_NAME_INTRO': 2}
    - [HIGH_LENGTH] form=`(do (defmulti show identity) (defmethod show :rabb` — user_msg 212 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti show identity) (defmethod show :rabb` — sentence with 5 commas reads as AI-output cadence: 'To define a multimethod show that dispatches on identity with a method for one s'
    - [LOW_GROUNDING] form=`(do (defprotocol Show (show [this])) (extend-proto` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do (defprotocol Show (show [this])) (extend-proto` — character 'Louie the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Show (show [this])) (extend-proto` — sentence with 7 commas reads as AI-output cadence: 'The runtime reads it, finds the matching pile,\nand runs that one." To define a p'
    - [LOW_GROUNDING] form=`(do (defprotocol Show (show [this])) (extend-proto` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-11: Protocol vs Java interface

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'CLAUSE_STACK_OVERFLOW': 3, 'HIGH_LENGTH': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol IPace (run [this])) (extend-proto` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol IPace (run [this])) (extend-proto` — sentence with 6 commas reads as AI-output cadence: 'The runtime looks up which breed the\ndog is, then runs that breed\'s answer." To '
    - [HIGH_LENGTH] form=`(do (defprotocol IPace (run [this])) (extend-proto` — user_msg 220 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol IPace (run [this])) (extend-proto` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol IPace with method run, extend it to String type, then call '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol IPace (run [this])) (extend-proto` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol IPace with method run, extend it to String type, then call '

### G8-12: extend-type on built-in types

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 5, 'LOW_GROUNDING': 3, 'HIGH_LENGTH': 1}
    - [DOUBLE_NAME_INTRO] form=`(do (defprotocol Pace (speed [this])) (extend-type` — character 'Topsy the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-type` — sentence with 6 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, use extend-type to attach it to Lon'
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-type` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-type` — sentence with 7 commas reads as AI-output cadence: 'The runtime reads it, finds the matching pile,\nand runs that one." To define a p'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-type` — sentence with 6 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, use extend-type to attach it to Lon'
    - [HIGH_LENGTH] form=`(do (defprotocol Pace (speed [this])) (extend-type` — user_msg 211 words

### G8-13: this-style vs fn-style

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'STORY_RESOLUTION_NO_DRAWN': 6, 'PARAGRAPH_FRAGMENTATION': 1, 'CLAUSE_STACK_OVERFLOW': 6, 'LOW_GROUNDING': 4, 'DOUBLE_NAME_INTRO': 1, 'DOUBLE_EMO_INJECTION': 1}
    - [HIGH_LENGTH] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg 216 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Named (name-of [this])) (defrecor` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':n', 'Zephyr'), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Named (name-of [this])) (defrecor` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Named with method name-of, define a record that uses this t'
    - [LOW_GROUNDING] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Named (name-of [this])) (defrecor` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':n', 'Zephyr'), resolution doesn't close the loop)

### G8-14: Protocols don't inherit

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 3, 'LOW_GROUNDING': 1, 'AS_ONE_WHO_CADENCE': 1}
    - [HIGH_LENGTH] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg 246 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — sentence with 6 commas reads as AI-output cadence: 'To define two protocols A and B, each with a method, extend both to String type '
    - [LOW_GROUNDING] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — sentence with 6 commas reads as AI-output cadence: 'Any dog\nthat learns the signals may join the pack." To define two protocols A an'

### G8-15: derive and isa? — multimethod hierarchy

- examples: 3
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'DOUBLE_NAME_INTRO': 3, 'CLAUSE_STACK_OVERFLOW': 3, 'HIGH_LENGTH': 1, 'BOOL_LEAK_RESOLUTION': 2, 'LOW_GROUNDING': 4}
    - [WRONG_FABLE_LITERAL] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [DOUBLE_NAME_INTRO] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — character 'Pip the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — sentence with 6 commas reads as AI-output cadence: 'The runtime reads it, finds the matching pile,\nand runs that one." To establish '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — sentence with 5 commas reads as AI-output cadence: 'To establish a type relationship where ::hare is a type of ::runner, then check '
    - [HIGH_LENGTH] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — user_msg 212 words
    - [BOOL_LEAK_RESOLUTION] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead

### G8-16: Abstract design with protocols

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 2, 'CLAUSE_STACK_OVERFLOW': 3, 'PARAGRAPH_FRAGMENTATION': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':leap', ':plod'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — character 'Pumpkin the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — sentence with 5 commas reads as AI-output cadence: 'Any dog\nthat learns the signals may join the pack." To define a protocol Move wi'
    - [LOW_GROUNDING] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':leap', ':plod'), resolution doesn't close the loop)

## Grade 9

### G9-01: Immutability as default — review

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [v [1 2 3]] (conj v 4) v)` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [v [1 2 3]] (conj v 4) v)` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(let [v [1 2 3]] (conj v 4) v)` — sentence with 5 commas reads as AI-output cadence: 'Bingo the dog, as a tortoise walks, neither hurrying nor stopping, pointed to a '
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [v [1 2 3]] (conj v 4) v)` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count

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
- issues: {'HIGH_LENGTH': 1, 'CONCEPT_PHRASE_COMMA_LIST': 9, 'CLAUSE_STACK_OVERFLOW': 9, 'AS_ONE_WHO_CADENCE': 1, 'LOW_GROUNDING': 4, 'DOUBLE_NAME_INTRO': 1}
    - [HIGH_LENGTH] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg 240 words
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 7 commas reads as AI-output cadence: 'To set up a shared notebook starting at 0, atomically add one to its page, then '
    - [AS_ONE_WHO_CADENCE] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 7 commas reads as AI-output cadence: 'To set up a shared notebook starting at 0, atomically add one to its page, then '

### G9-04: Atom CAS semantics

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 6, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — concept_phrase 'atom, CAS, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — sentence with 7 commas reads as AI-output cadence: 'The\nruntime sees to that — no two writers stomp on each other\'s\nwork." To constr'
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — concept_phrase 'atom, CAS, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [DOUBLE_NAME_INTRO] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — character 'Silver the dog' introduced twice within 200 chars — drop the second 'the dog'

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
- issues: {'LOW_GROUNDING': 1, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'DOUBLE_NAME_INTRO': 2, 'CLAUSE_STACK_OVERFLOW': 6, 'AS_ONE_WHO_CADENCE': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — concept_phrase 'ref, dosync, alter, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [DOUBLE_NAME_INTRO] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — character 'Tucker the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 8 commas reads as AI-output cadence: 'The\nruntime sees to that — no two writers stomp on each other\'s\nwork." To constr'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — concept_phrase 'ref, dosync, alter, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 8 commas reads as AI-output cadence: 'To construct a ref holding 0, perform a transactional alter by applying inc insi'

### G9-08: dosync and alter

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 6, 'PARAGRAPH_FRAGMENTATION': 1, 'LOW_GROUNDING': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CONCEPT_PHRASE_COMMA_LIST': 3, 'DOUBLE_NAME_INTRO': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — sentence with 6 commas reads as AI-output cadence: 'To construct refs a and b, perform a coordinated transaction that alters both by'
    - [PARAGRAPH_FRAGMENTATION] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — sentence with 8 commas reads as AI-output cadence: 'To construct refs a and b, perform a coordinated transaction that alters both by'
    - [LOW_GROUNDING] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — sentence with 6 commas reads as AI-output cadence: 'The\ncount changes only when one of us scratches a new one — and only\nas the runt'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '5'), resolution doesn't close the loop)

### G9-09: Ref vs atom

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 6, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 7 commas reads as AI-output cadence: 'The\ncount changes only when one of us scratches a new one — and only\nas the runt'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 7 commas reads as AI-output cadence: 'To construct an atom holding 0, atomically swap it by applying inc, and derefere'
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-10: Agent introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 6, 'LOW_GROUNDING': 2, 'DOUBLE_NAME_INTRO': 2}
    - [HIGH_LENGTH] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg 216 words
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 10 commas reads as AI-output cadence: 'To construct an agent holding 0, asynchronously send inc to it, await its comple'
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 10 commas reads as AI-output cadence: 'The result will be there when you\nask for it — sometimes you have to wait for th'

### G9-11: send and send-off

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 5, 'HIGH_LENGTH': 1}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 10 commas reads as AI-output cadence: 'The result will be there when you\nask for it — sometimes you have to wait for th'
    - [HIGH_LENGTH] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg 222 words
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 9 commas reads as AI-output cadence: 'To construct an agent holding 0, use send to asynchronously apply inc, await its'

### G9-12: await — synchronizing on agents

- examples: 1
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 3, 'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 3, 'LOW_GROUNDING': 1}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — concept_phrase 'agent, double send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [DOUBLE_NAME_INTRO] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — character 'Topsy the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 9 commas reads as AI-output cadence: 'To construct an agent holding 0, asynchronously send inc twice, synchronize with'
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — concept_phrase 'agent, double send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 9 commas reads as AI-output cadence: 'The runtime makes that easier than it sounds." To construct an agent holding 0, '

### G9-13: future introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 4, 'LOW_GROUNDING': 2, 'DOUBLE_NAME_INTRO': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'PARAGRAPH_FRAGMENTATION': 1, 'DOUBLE_EMO_INJECTION': 1}
    - [HIGH_LENGTH] form=`@(future (+ 1 2))` — user_msg 238 words
    - [CONCEPT_PHRASE_COMMA_LIST] form=`@(future (+ 1 2))` — concept_phrase 'future, add, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`@(future (+ 1 2))` — sentence with 6 commas reads as AI-output cadence: 'To dispatch a runner to compute the sum of 1 and 2; later, ask the runner for th'
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`@(future (+ 1 2))` — concept_phrase 'future, add, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [DOUBLE_NAME_INTRO] form=`@(future (+ 1 2))` — character 'Sooty the dog' introduced twice within 200 chars — drop the second 'the dog'

### G9-14: deref @ shorthand

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'PARAGRAPH_FRAGMENTATION': 2, 'AS_ONE_WHO_CADENCE': 1, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(do (def a (atom 7)) @a)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(do (def a (atom 7)) @a)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) (deref a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)

### G9-15: promise — deliver and deref

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'LOW_GROUNDING': 1, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'DOUBLE_NAME_INTRO': 2, 'CLAUSE_STACK_OVERFLOW': 5, 'ANSWER_LEAK_STRING': 1, 'PARAGRAPH_FRAGMENTATION': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [WRONG_FABLE_LITERAL] form=`(do (def p (promise)) (deliver p :done) @p)` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [LOW_GROUNDING] form=`(do (def p (promise)) (deliver p :done) @p)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def p (promise)) (deliver p :done) @p)` — concept_phrase 'promise, deliver, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [DOUBLE_NAME_INTRO] form=`(do (def p (promise)) (deliver p :done) @p)` — character 'Pip the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def p (promise)) (deliver p :done) @p)` — sentence with 7 commas reads as AI-output cadence: 'The runtime makes that easier than it sounds." To construct a promise, deliver a'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def p (promise)) (deliver p :done) @p)` — concept_phrase 'promise, deliver, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose

### G9-16: volatile — when STM is too heavy

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 6, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [LOW_GROUNDING] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — concept_phrase 'volatile, vswap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — sentence with 8 commas reads as AI-output cadence: 'to\nwrite atomically, no matter who else is sniffing." To\nconstruct a volatile ho'
    - [LOW_GROUNDING] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — concept_phrase 'volatile, vswap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — sentence with 8 commas reads as AI-output cadence: 'If two dogs arrive at once, the runtime makes sure only one of us\ngoes through a'

### G9-17: binding — thread-local

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 6, 'PARAGRAPH_FRAGMENTATION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — concept_phrase 'dynamic var, binding, read' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [DOUBLE_NAME_INTRO] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — character 'Pathfinder the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — sentence with 7 commas reads as AI-output cadence: 'The\nruntime sees to that — no two writers stomp on each other\'s\nwork." To define'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — concept_phrase 'dynamic var, binding, read' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 6, 'HIGH_LENGTH': 2, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — concept_phrase 'lock, locking, arithmetic' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — sentence with 7 commas reads as AI-output cadence: 'The\ncount changes only when one of us scratches a new one — and only\nas the runt'
    - [HIGH_LENGTH] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg 257 words
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — concept_phrase 'lock, locking, arithmetic' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — sentence with 8 commas reads as AI-output cadence: 'To create an object to use as a monitor, acquire the lock, and evaluate an addit'

## Grade 10

### G10-01: quote, unquote, unquote-splice

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'HIGH_LENGTH': 3, 'THE_FORM_OVERUSE': 3, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'ONLY_SHOOK_HEAD_TIC': 1}
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(quote (+ 1 2))` — user_msg 227 words
    - [THE_FORM_OVERUSE] form=`(quote (+ 1 2))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [LOW_GROUNDING] form=`'(1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-02: syntax-quote

- examples: 2
- variety @ n=50: 1.00
- issues: {'THE_FORM_OVERUSE': 3, 'LOW_GROUNDING': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1, 'HIGH_LENGTH': 1, 'ONLY_SHOOK_HEAD_TIC': 1}
    - [THE_FORM_OVERUSE] form=`(let [x 10] `(+ ~x ~x))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [THE_FORM_OVERUSE] form=`(let [x 10] `(+ ~x ~x))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [LOW_GROUNDING] form=`(let [xs [1 2 3]] `(list ~@xs))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [xs [1 2 3]] `(list ~@xs))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(let [xs [1 2 3]] `(list ~@xs))` — character 'Bingo the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [HIGH_LENGTH] form=`(let [xs [1 2 3]] `(list ~@xs))` — user_msg 241 words

### G10-03: defmacro introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'AS_ONE_WHO_CADENCE': 1, 'LOW_GROUNDING': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg 266 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G10-04: Macro expansion rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 3, 'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(when true 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(macroexpand-1 '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(when true 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(macroexpand-1 '(when true 1))` — character 'Silver the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(macroexpand-1 '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(when true 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)

### G10-05: macroexpand

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(macroexpand '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(macroexpand '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(macroexpand '(-> 1 inc inc))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(macroexpand '(-> 1 inc inc))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(macroexpand '(-> 1 inc inc))` — sentence with 5 commas reads as AI-output cadence: 'You set the rule\nonce, and any mark that uses it gets rewritten on the way to th'

### G10-06: when and when-not as macros

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 7, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_NAME_INTRO': 1, 'WRONG_FABLE_LITERAL': 1}
    - [LOW_GROUNDING] form=`(when true 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(when true 1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'You set the rule\nonce, and any mark that uses it gets rewritten on the way to th'
    - [LOW_GROUNDING] form=`(when true 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(when true 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(when false 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(when false 1 2 3)` — character 'Snort the dog' introduced twice within 200 chars — drop the second 'the dog'

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'DOUBLE_NAME_INTRO': 2, 'ANSWER_LEAK': 3, 'HIGH_LENGTH': 3, 'AS_ONE_WHO_CADENCE': 2, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'CONCEPT_AS_VERB': 1}
    - [LOW_GROUNDING] form=`(-> 5 inc inc inc)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(-> 5 inc inc inc)` — character 'Tucker the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [ANSWER_LEAK] form=`(-> 5 inc inc inc)` — answer 8 in narrative
    - [DOUBLE_NAME_INTRO] form=`(-> 5 inc inc inc)` — character 'Zoomer the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [HIGH_LENGTH] form=`(-> 5 inc inc inc)` — user_msg 246 words
    - [ANSWER_LEAK] form=`(-> 5 inc inc inc)` — answer 8 in narrative

### G10-08: Macro vs fn

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1, 'DOUBLE_NAME_INTRO': 2}
    - [ANSWER_LEAK] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — answer 7 in narrative
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
    - [HIGH_LENGTH] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — user_msg 235 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(if-let [x 7] (* x x) 0)` — character 'Louie the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [DOUBLE_NAME_INTRO] form=`(if-let [x 7] (* x x) 0)` — character 'Bingo the dog' introduced twice within 200 chars — drop the second 'the dog'

### G10-11: Reader macros overview

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 7, 'HIGH_LENGTH': 2, 'ANSWER_LEAK': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'AS_ONE_WHO_CADENCE': 1}
    - [LOW_GROUNDING] form=`'(1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`'(1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`'(1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(#(* % %) 6)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(#(* % %) 6)` — user_msg 239 words
    - [ANSWER_LEAK] form=`(#(* % %) 6)` — answer 36 in narrative

### G10-12: Tagged literals

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'HIGH_LENGTH': 1, 'BOOL_LEAK_RESOLUTION': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'AS_ONE_WHO_CADENCE': 1}
    - [LOW_GROUNDING] form=`(inst? #inst "2024-01-01")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(inst? #inst "2024-01-01")` — character 'Topsy the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(inst? #inst "2024-01-01")` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'
    - [LOW_GROUNDING] form=`(inst? #inst "2024-01-01")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(inst? #inst "2024-01-01")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(inst? #inst "2024-01-01")` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form, evaluates it,\nand gives back what it compu'

### G10-13: Data readers and EDN extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'LOW_GROUNDING': 4, 'DOUBLE_NAME_INTRO': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'AS_ONE_WHO_CADENCE': 1}
    - [HIGH_LENGTH] form=`(clojure.edn/read-string "42")` — user_msg 207 words
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(clojure.edn/read-string "42")` — character 'Sooty the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "[:a :b :c]")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "[:a :b :c]")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b', ':c'), resolution doesn't close the loop)

### G10-14: eval (the function)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'ANSWER_LEAK': 1, 'LOW_GROUNDING': 3, 'CLAUSE_STACK_OVERFLOW': 2, 'AS_ONE_WHO_CADENCE': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [HIGH_LENGTH] form=`(eval '(+ 1 2 3))` — user_msg 233 words
    - [ANSWER_LEAK] form=`(eval '(+ 1 2 3))` — answer 6 in narrative
    - [LOW_GROUNDING] form=`(eval '(+ 1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(eval '(+ 1 2 3))` — sentence with 5 commas reads as AI-output cadence: 'You set the rule\nonce, and any mark that uses it gets rewritten on the way to th'
    - [AS_ONE_WHO_CADENCE] form=`(eval '(+ 1 2 3))` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [LOW_GROUNDING] form=`(eval (list '+ 4 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-15: When not to write a macro

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'DOUBLE_NAME_INTRO': 2, 'AS_ONE_WHO_CADENCE': 1, 'LOW_GROUNDING': 1}
    - [WRONG_FABLE_LITERAL] form=`(do "a function suffices when no syntax shaping is` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [DOUBLE_NAME_INTRO] form=`(do "a function suffices when no syntax shaping is` — character 'Pip the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [AS_ONE_WHO_CADENCE] form=`(do "a function suffices when no syntax shaping is` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [LOW_GROUNDING] form=`(do "prefer fn unless you must shape syntax" (map ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do "prefer fn unless you must shape syntax" (map ` — character 'Winston the dog' introduced twice within 200 chars — drop the second 'the dog'

### G10-16: Macro pattern library

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'HIGH_LENGTH': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [LOW_GROUNDING] form=`(do (defmacro with-steady-pace [& body] `(let [pac` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro with-steady-pace [& body] `(let [pac` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':slow-and-steady'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (defmacro with-steady-pace [& body] `(let [pac` — character 'Pumpkin the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmacro with-steady-pace [& body] `(let [pac` — sentence with 5 commas reads as AI-output cadence: 'You set the rule\nonce, and any mark that uses it gets rewritten on the way to th'
    - [LOW_GROUNDING] form=`(do (defmacro with-steady-pace [& body] `(let [pac` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro with-steady-pace [& body] `(let [pac` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':slow-and-steady'), resolution doesn't close the loop)

## Grade 11

### G11-01: JVM vs CLR vs JS vs Python (host overview)

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'AS_ONE_WHO_CADENCE': 1, 'DOUBLE_NAME_INTRO': 2, 'DOUBLE_EMO_INJECTION': 1}
    - [LOW_GROUNDING] form=`(do "Clojure runs on multiple hosts: JVM, CLR, JS,` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [AS_ONE_WHO_CADENCE] form=`(do "Clojure runs on multiple hosts: JVM, CLR, JS,` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [DOUBLE_NAME_INTRO] form=`(do "Clojure runs on multiple hosts: JVM, CLR, JS,` — character 'Runner the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [DOUBLE_EMO_INJECTION] form=`(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScr` — sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat
    - [LOW_GROUNDING] form=`(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScr` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScr` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-02: Method call syntax

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 1, 'BOOL_LEAK_RESOLUTION': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(.startsWith "hare-tortoise" "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('hare-tortoise', 'hare'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(.startsWith "hare-tortoise" "hare")` — user_msg 233 words
    - [BOOL_LEAK_RESOLUTION] form=`(.startsWith "hare-tortoise" "hare")` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [STORY_RESOLUTION_NO_DRAWN] form=`(.startsWith "hare-tortoise" "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('hare-tortoise', 'hare'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(.startsWith "hare-tortoise" "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('hare-tortoise', 'hare'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(. "abc" toUpperCase)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)

### G11-03: Static method call

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'AS_ONE_WHO_CADENCE': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(Math/abs -7)` — user_msg 249 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)
    - [AS_ONE_WHO_CADENCE] form=`(Math/abs -7)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(Math/max 3 9)` — sentence with 5 commas reads as AI-output cadence: 'The runtime moves a value across the\nboundary, calls the human-side tool, and br'

### G11-04: Field access

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3, 'HIGH_LENGTH': 1, 'DOUBLE_NAME_INTRO': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(count "tortoise")` — sentence with 5 commas reads as AI-output cadence: 'The runtime moves a value across the\nboundary, calls the human-side tool, and br'
    - [HIGH_LENGTH] form=`(count "hare")` — user_msg 219 words
    - [CLAUSE_STACK_OVERFLOW] form=`(count "hare")` — sentence with 5 commas reads as AI-output cadence: 'The runtime moves a value across the\nboundary, calls the human-side tool, and br'
    - [DOUBLE_NAME_INTRO] form=`(count "hare")` — character 'Gizmo the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(count "hare")` — sentence with 5 commas reads as AI-output cadence: 'The runtime moves a value across the\nboundary, calls the human-side tool, and br'

### G11-05: Import form

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'DOUBLE_NAME_INTRO': 1, 'AS_ONE_WHO_CADENCE': 1}
    - [LOW_GROUNDING] form=`(do "(:import (java.util Date)) imports a host cla` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "(:import (java.util Date)) imports a host cla` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do "(:import (java.util Date)) imports a host cla` — character 'Howler the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [AS_ONE_WHO_CADENCE] form=`(do "import is a top-of-file ns clause" :studied)` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

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
- issues: {'DOUBLE_NAME_INTRO': 2, 'CLAUSE_STACK_OVERFLOW': 2, 'AS_ONE_WHO_CADENCE': 1}
    - [DOUBLE_NAME_INTRO] form=`(let [a (int-array [10 20 30])] (aget a 1))` — character 'Tucker the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a (int-array [10 20 30])] (aget a 1))` — sentence with 5 commas reads as AI-output cadence: 'The runtime moves a value across the\nboundary, calls the human-side tool, and br'
    - [AS_ONE_WHO_CADENCE] form=`(let [a (int-array [10 20 30])] (aget a 1))` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [DOUBLE_NAME_INTRO] form=`(let [a (int-array [1 2 3])] (alength a))` — character 'Zoomer the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a (int-array [1 2 3])] (alength a))` — sentence with 5 commas reads as AI-output cadence: 'The runtime moves a value across the\nboundary, calls the human-side tool, and br'

### G11-08: Type hints

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1, 'PARAGRAPH_FRAGMENTATION': 1, 'AS_ONE_WHO_CADENCE': 2, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [^String s "abc"] (.toUpperCase s))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(let [^String s "abc"] (.toUpperCase s))` — user_msg 202 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [^String s "abc"] (.toUpperCase s))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(let [^String s "abc"] (.toUpperCase s))` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [AS_ONE_WHO_CADENCE] form=`(let [^String s "abc"] (.toUpperCase s))` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [^String s "abc"] (.toUpperCase s))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)

### G11-09: Checked vs unchecked math

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'REPL_AS_TIME_TRAVELLER': 2}
    - [LOW_GROUNDING] form=`(+ 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [REPL_AS_TIME_TRAVELLER] form=`(+ 1 2)` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer
    - [LOW_GROUNDING] form=`(do "*unchecked-math* turns off overflow checking ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [REPL_AS_TIME_TRAVELLER] form=`(do "*unchecked-math* turns off overflow checking ` — user_msg uses meta-narrator language that implies the answer pre-existed evaluation — describe the form's evaluation, not a pre-existing 'right' answer

### G11-10: ClojureScript overview

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'DOUBLE_NAME_INTRO': 2, 'PARALLEL_POSSESSIVE_TIC': 1, 'HEDGING_NEAR_FORM': 1}
    - [LOW_GROUNDING] form=`(do "ClojureScript compiles to JavaScript via the ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do "ClojureScript compiles to JavaScript via the ` — character 'Louie the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [PARALLEL_POSSESSIVE_TIC] form=`(do "ClojureScript compiles to JavaScript via the ` — user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic
    - [LOW_GROUNDING] form=`(do "cljs runs in browsers and Node, with JS inter` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "cljs runs in browsers and Node, with JS inter` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [LOW_GROUNDING] form=`(do "cljs runs in browsers and Node, with JS inter` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-11: cljs / JavaScript interop

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'AS_ONE_WHO_CADENCE': 1, 'DOUBLE_EMO_INJECTION': 1}
    - [LOW_GROUNDING] form=`(do "(js/console.log x) calls a JS global; (.-foo ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [AS_ONE_WHO_CADENCE] form=`(do "(js/console.log x) calls a JS global; (.-foo ` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [LOW_GROUNDING] form=`(do "(js/console.log x) calls a JS global; (.-foo ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_EMO_INJECTION] form=`(do "js/<name> namespaces JS globals; .- prefix ma` — sentence has 2+ distinct EMO-pool phrases ('without complaint or hurry' + 'without complaint') — the character can't earn two emotional registers in the same beat

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
- issues: {'WRONG_FABLE_LITERAL': 1, 'LOW_GROUNDING': 2, 'DOUBLE_NAME_INTRO': 1, 'AS_ONE_WHO_CADENCE': 1}
    - [WRONG_FABLE_LITERAL] form=`(do "#?(:clj … :cljs …) selects a form per host at` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [LOW_GROUNDING] form=`(do "#?(:clj … :cljs …) selects a form per host at` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do ".cljc files share code across multiple hosts"` — character 'Champ the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [AS_ONE_WHO_CADENCE] form=`(do ".cljc files share code across multiple hosts"` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [LOW_GROUNDING] form=`(do ".cljc files share code across multiple hosts"` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-14: Debugging host leaks

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'LOW_GROUNDING': 2, 'DOUBLE_NAME_INTRO': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "host stack traces leak through interop; learn` — sentence with 5 commas reads as AI-output cadence: 'To learn to read and debug host runtime errors, he, going slowly, looking twice '
    - [LOW_GROUNDING] form=`(do "host stack traces leak through interop; learn` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do "host stack traces leak through interop; learn` — character 'Shadow the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(do "host stack traces leak through interop; learn` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (Math/sqrt 4) (catch Exception _ :err))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4', ':err'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(try (Math/sqrt 4) (catch Exception _ :err))` — character 'Shadow the dog' introduced twice within 200 chars — drop the second 'the dog'

## Grade 12

### G12-01: Transducers introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'COLLECTION_LEAK': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'WRONG_FABLE_LITERAL': 1}
    - [HIGH_LENGTH] form=`(into [] (map inc) [1 2 3])` — user_msg 257 words
    - [COLLECTION_LEAK] form=`(into [] (map inc) [1 2 3])` — elements of expected [2, 3, 4] appear comma-separated in user_msg (collection answer leak)
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] (map inc) [1 2 3])` — sentence with 7 commas reads as AI-output cadence: 'To use the map-inc transducer with into to increment the vector containing 1, 2,'
    - [WRONG_FABLE_LITERAL] form=`(into [] (filter even?) [1 2 3 4 5])` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] (filter even?) [1 2 3 4 5])` — sentence with 8 commas reads as AI-output cadence: 'Pip the dog shook\nher head and went on with the work: to use the filter-even tra'

### G12-02: Transducer composition

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4, 'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — sentence with 8 commas reads as AI-output cadence: 'The receiver is patient; the gap is exact." To\ncompose map-inc and filter-even i'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', '5'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — sentence with 5 commas reads as AI-output cadence: 'Diesel the dog, her breath even, her step even, her thought even, stood beside a'
    - [HIGH_LENGTH] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — user_msg 207 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', '5'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — sentence with 11 commas reads as AI-output cadence: 'To compose map-inc and filter-even, then use transduce to sum the kept elements '

### G12-03: into with a transducer (xform)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'COLLECTION_LEAK': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'AS_ONE_WHO_CADENCE': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [HIGH_LENGTH] form=`(into #{} (map inc) [1 2 3])` — user_msg 265 words
    - [COLLECTION_LEAK] form=`(into #{} (map inc) [1 2 3])` — elements of expected {2, 3, 4} appear comma-separated in user_msg (collection answer leak)
    - [CLAUSE_STACK_OVERFLOW] form=`(into #{} (map inc) [1 2 3])` — sentence with 7 commas reads as AI-output cadence: 'To use the map-inc transducer with into to create a set from the incremented ele'
    - [AS_ONE_WHO_CADENCE] form=`(into #{} (map inc) [1 2 3])` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [CLAUSE_STACK_OVERFLOW] form=`(into #{} (map inc) [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'Leo the dog shook\nhis head and went on with the work: to use the map-inc transdu'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (take 3) (range 100))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '100'), resolution doesn't close the loop)

### G12-04: core.async introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'PARALLEL_POSSESSIVE_TIC': 2}
    - [PARALLEL_POSSESSIVE_TIC] form=`(do "(chan), (go ...), (<! ...), (>! ...) form the` — user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic
    - [PARALLEL_POSSESSIVE_TIC] form=`(do "go-blocks let you write async code as if it w` — user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic

### G12-05: Channels and pipelines

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'AS_ONE_WHO_CADENCE': 1}
    - [LOW_GROUNDING] form=`(do "pipe, mult, mix, pipeline-async route values ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "pipe, mult, mix, pipeline-async route values ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do "pipe, mult, mix, pipeline-async route values ` — character 'Howler the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(do "pipe, mult, mix, pipeline-async route values ` — sentence with 5 commas reads as AI-output cadence: 'Marigold the dog squinted at the goal — to study how pipe, mult, mix, and pipeli'
    - [AS_ONE_WHO_CADENCE] form=`(do "pipelines transform streams of values channel` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G12-06: clojure.spec

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'DOUBLE_EMO_INJECTION': 1}
    - [HEDGING_NEAR_FORM] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [DOUBLE_EMO_INJECTION] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat

### G12-07: Spec generators

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1}
    - [HEDGING_NEAR_FORM] form=`(do "spec generators turn specs into property-base` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value

### G12-08: clojure.test

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'DOUBLE_EMO_INJECTION': 1, 'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HEDGING_NEAR_FORM] form=`(= (+ 1 2) 3)` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [DOUBLE_EMO_INJECTION] form=`(= (+ 1 2) 3)` — sentence has 2+ distinct EMO-pool phrases ('without complaint or hurry' + 'without complaint') — the character can't earn two emotional registers in the same beat
    - [DOUBLE_NAME_INTRO] form=`(do "(deftest …), (is …), (testing …) are the core` — character 'Zippy the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [CLAUSE_STACK_OVERFLOW] form=`(do "(deftest …), (is …), (testing …) are the core` — sentence with 6 commas reads as AI-output cadence: 'Marble the dog, her breath even, her step even, her thought even, had already wr'

### G12-09: Test fixtures

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'AS_ONE_WHO_CADENCE': 1, 'HEDGING_NEAR_FORM': 1}
    - [LOW_GROUNDING] form=`(do "(use-fixtures :each f) wraps every deftest in` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [AS_ONE_WHO_CADENCE] form=`(do "(use-fixtures :each f) wraps every deftest in` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [LOW_GROUNDING] form=`(do "fixtures provide setup/teardown around deftes` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "fixtures provide setup/teardown around deftes` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [LOW_GROUNDING] form=`(do "fixtures provide setup/teardown around deftes` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-10: Property-based testing

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'HEDGING_NEAR_FORM': 2, 'AS_ONE_WHO_CADENCE': 1}
    - [LOW_GROUNDING] form=`(= (reverse (reverse [1 2 3])) [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(= (reverse (reverse [1 2 3])) [1 2 3])` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [AS_ONE_WHO_CADENCE] form=`(do "test.check generates inputs and checks proper` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [LOW_GROUNDING] form=`(do "test.check generates inputs and checks proper` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "test.check generates inputs and checks proper` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [LOW_GROUNDING] form=`(do "test.check generates inputs and checks proper` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-11: Leiningen project.clj

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'AS_ONE_WHO_CADENCE': 1, 'DOUBLE_EMO_INJECTION': 1}
    - [LOW_GROUNDING] form=`(do "project.clj declares :dependencies, :main, :p` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [AS_ONE_WHO_CADENCE] form=`(do "project.clj declares :dependencies, :main, :p` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [LOW_GROUNDING] form=`(do "project.clj declares :dependencies, :main, :p` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_EMO_INJECTION] form=`(do "Leiningen reads project.clj at the project ro` — sentence has 2+ distinct EMO-pool phrases ('without complaint or hurry' + 'without complaint') — the character can't earn two emotional registers in the same beat

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
- issues: {'WRONG_FABLE_LITERAL': 1, 'LOW_GROUNDING': 2, 'DOUBLE_NAME_INTRO': 1, 'AS_ONE_WHO_CADENCE': 1}
    - [WRONG_FABLE_LITERAL] form=`(do "`clj -M:test` runs the :test alias from deps.` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [LOW_GROUNDING] form=`(do "`clj -M:test` runs the :test alias from deps.` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(do "aliases compose extra paths, deps, and main o` — character 'Champ the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [AS_ONE_WHO_CADENCE] form=`(do "aliases compose extra paths, deps, and main o` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [LOW_GROUNDING] form=`(do "aliases compose extra paths, deps, and main o` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-14: Pedestal / Ring (web stack brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1, 'LOW_GROUNDING': 2, 'CLAUSE_STACK_OVERFLOW': 1, 'PARALLEL_POSSESSIVE_TIC': 1}
    - [DOUBLE_NAME_INTRO] form=`(do "Ring models HTTP as request-map -> response-m` — character 'Shadow the dog' introduced twice within 200 chars — drop the second 'the dog'
    - [LOW_GROUNDING] form=`(do "Ring models HTTP as request-map -> response-m` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do "Pedestal layers interceptors over Ring for ri` — sentence with 5 commas reads as AI-output cadence: 'Berry the dog, her face quiet, her hands quieter still, had already written\nthe '
    - [PARALLEL_POSSESSIVE_TIC] form=`(do "Pedestal layers interceptors over Ring for ri` — user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic
    - [LOW_GROUNDING] form=`(do "Pedestal layers interceptors over Ring for ri` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-15: Datomic / XTDB (datalog db brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 1, 'LOW_GROUNDING': 3, 'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [WRONG_FABLE_LITERAL] form=`(do "Datomic and XTDB are immutable, time-aware da` — tortoise-hare ghost name 'Pip' appears in dog-shadow user_msg
    - [LOW_GROUNDING] form=`(do "Datomic and XTDB are immutable, time-aware da` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "Datomic and XTDB are immutable, time-aware da` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "Datomic and XTDB are immutable, time-aware da` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "Datomic and XTDB are immutable, time-aware da` — sentence with 5 commas reads as AI-output cadence: 'Setter the dog, who had simply walked to a flat stone and\nbegun to write the fam'
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
- issues: {'LOW_GROUNDING': 2, 'AS_ONE_WHO_CADENCE': 1}
    - [LOW_GROUNDING] form=`(do "good libraries expose data, then functions, t` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= [1 2 3] (vec '(1 2 3)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [AS_ONE_WHO_CADENCE] form=`(= [1 2 3] (vec '(1 2 3)))` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence

### G12-18: Clojure style guide

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'AS_ONE_WHO_CADENCE': 1}
    - [LOW_GROUNDING] form=`(do "kebab-case names, two-space indent, threading` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "kebab-case names, two-space indent, threading` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "prefer pure functions, name predicates with ?` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [AS_ONE_WHO_CADENCE] form=`(do "prefer pure functions, name predicates with ?` — user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    - [LOW_GROUNDING] form=`(do "prefer pure functions, name predicates with ?` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

---

## Summary

### Issue counts (across all examples × 3 records)

- **LOW_GROUNDING**: 383
- **CLAUSE_STACK_OVERFLOW**: 325
- **STORY_RESOLUTION_NO_DRAWN**: 225
- **DOUBLE_NAME_INTRO**: 222
- **NARRATIVE_NUMERAL_HARDCODE**: 138
- **HIGH_LENGTH**: 127
- **AS_ONE_WHO_CADENCE**: 99
- **CONCEPT_PHRASE_COMMA_LIST**: 75
- **DOUBLE_EMO_INJECTION**: 31
- **REPL_AS_TIME_TRAVELLER**: 31
- **RESOLUTION_GENERIC**: 31
- **FORM_DISPLAY_AND_FORM_NOUN**: 26
- **BOOL_LEAK_RESOLUTION**: 24
- **ANSWER_LEAK**: 18
- **PARAGRAPH_FRAGMENTATION**: 17
- **PARALLEL_POSSESSIVE_TIC**: 16
- **THE_FORM_OVERUSE**: 16
- **WRONG_FABLE_LITERAL**: 16
- **HEDGING_NEAR_FORM**: 11
- **PARAMETRIC_LITERAL_NUMERALS**: 9
- **CONCEPT_AS_VERB**: 7
- **ANSWER_LEAK_STRING**: 6
- **ONLY_SHOOK_HEAD_TIC**: 4
- **META_FILLER_RESOLUTION**: 3
- **GENERIC_RESOLUTION_TAIL**: 3
- **COLLECTION_LEAK**: 3
- **PREDICATE_QUESTION_COLLISION**: 3
- **SENTENCE_START_LOWER_PRONOUN**: 2
- **SMALL_INT_LEAK**: 1
- **HANGING_FORM_THAT**: 1

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 178 | — |
| 2 | 22 | 88 | 292 | — |
| 3 | 18 | 31 | 109 | — |
| 4 | 20 | 39 | 118 | — |
| 5 | 22 | 39 | 149 | — |
| 6 | 16 | 33 | 94 | — |
| 7 | 18 | 36 | 129 | — |
| 8 | 16 | 31 | 190 | — |
| 9 | 18 | 34 | 276 | — |
| 10 | 16 | 36 | 168 | — |
| 11 | 14 | 29 | 88 | — |
| 12 | 18 | 37 | 82 | — |

### Sample issues by severity

#### DOUBLE_EMO_INJECTION

- `G1-01` (form `42`): sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat
    ```
    Bayer had crossed this bridge a hundred times in the meadow, but never with so fine a bone clamped in his jaws.

With a twig, Bingo the dog marked a wager into the wet sand near the meadow:
whoever guessed the result of `28` first would choose
which bone to carry. Bayer the dog, stepping deliberatel...
    ```
- `G1-02` (form `-3`): sentence has 2+ distinct EMO-pool phrases ('without complaint or hurry' + 'without complaint') — the character can't earn two emotional registers in the same beat
    ```
    Down by the stream where the bank dipped low, the world above was answered politely by the world below.

Toby the dog and Marley the dog paused on the river bank where
someone had scratched the integer -75 into the wet sand. The water
ran clear and the bridge cast a long, trembling shadow.
Toby, puf...
    ```
- `G1-03` (form `(* 2 1/2)`): sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat
    ```
    on the beach, on a still afternoon by the brook, Collie learned what a reflection costs the careless.

With a twig, Houndsman the dog marked a wager into the wet sand near the beach:
whoever guessed the result of `(* 5 1/2)` first would choose
which bone to carry. Collie the dog, stepping deliberate...
    ```
- `G1-03` (form `(- 1 1/3)`): sentence has 2+ distinct EMO-pool phrases ('without complaint or hurry' + 'without complaint') — the character can't earn two emotional registers in the same beat
    ```
    It was on the river bank, on the wooden bridge above the slow brook, that Whatsit the dog looked down at the water.

With a twig, Bounder the dog marked a wager into the wet sand along the river bank:
whoever guessed the result of `(- 7 1/3)` first would choose
which bone to carry. Whatsit the dog, ...
    ```
- `G1-04` (form `"hello"`): sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat
    ```
    It happened on a day so ordinary that it seemed impossible anything could have been lost.

By a flat stone at the stream's edge at the edge of the pond, Buttermilk the dog scratched
a small wager: whoever guessed the result of `"apple"` first
would carry the bone home. The water ran past, indifferen...
    ```

#### AS_ONE_WHO_CADENCE

- `G1-01` (form `42`): user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    ```
    Some greedy creatures lose what they have to a thief; others lose it to themselves, by way of a careless glance.

By a flat stone at the stream's edge near the road, Guardian the dog scratched
a small wager: whoever guessed the result of `36` first
would carry the bone home. The water ran past, indi...
    ```
- `G1-01` (form `"hello"`): user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    ```
    Ranger the dog was crossing the stream on the road when he caught a glimpse of his own reflection.

By a flat stone at the stream's edge on the road, Caramel the dog scratched
a small wager: whoever guessed the result of `"garnet"` first
would carry the bone home. The water ran past, indifferent.
Ra...
    ```
- `G1-03` (form `1/2`): user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    ```
    Diesel had crossed this bridge a hundred times on the beach, but never with so fine a bone clamped in his jaws.

A puzzle was scratched onto the bridge plank near the beach. The riddle
was simple: it asked the reader to evaluate `1/2`.
Sooty laughed, with a pride that filled him from ear-tip to heel...
    ```
- `G1-04` (form `"slow and steady"`): user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    ```
    A reflection is a strange kind of promise: present and unreachable, and very hard to argue with.

Buddy the dog and Milo the dog paused on the river bank where
someone had scratched the string "indigo" into the wet sand. The water
ran clear and the bridge cast a long, trembling shadow.
Buddy, as one...
    ```
- `G1-05` (form `false`): user_msg contains 'as one who…' / 'with the X of one who Y' template-output cadence
    ```
    There is a kind of greed that does not see what it already has, and another kind that mistakes a reflection for a meal.

With a twig, Spot the dog marked a wager into the wet sand in the meadow:
whoever guessed the result of `false` first would choose
which bone to carry. Murphy the dog, in the pati...
    ```

#### FORM_DISPLAY_AND_FORM_NOUN

- `G1-01` (form `nil`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    A reflection is a strange kind of promise: present and unreachable, and very hard to argue with.

A few stream-side creatures had gathered on the bank by the pond to
watch Steel the dog attempt to outwit Yappy the dog at reading
the REPL. The water moved on, the bridge held its shadow, and
Yappy poi...
    ```
- `G1-02` (form `-25`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    Sniff the dog was halfway home at the edge of the forest when the water played its old trick on a young dog.

Sniff the dog had been showing Bailey the dog how the REPL works,
the stream cool against their paws and the bridge's shadow long.
"Look here," he said, pointing to the integer -60.
"You han...
    ```
- `G1-02` (form `-25`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    Down by the stream where the bank dipped low, the world above was answered politely by the world below.

A few stream-side creatures had gathered on the bank near the village to
watch Chestnut the dog attempt to outwit Oscar the dog at reading
the REPL. The water moved on, the bridge held its shadow...
    ```
- `G1-02` (form `12345`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    The bridge had stood there as long as anyone remembered, and so had the temptation it offered to anyone crossing with full jaws.

A few stream-side creatures had gathered on the bank by the forest to
watch Keeper the dog attempt to outwit Russet the dog at reading
the REPL. The water moved on, the b...
    ```
- `G1-02` (form `12345`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    On a path that ran beside the stream, a dog was carrying his supper home and looking pleased with himself.

A few stream-side creatures had gathered on the bank near the forest to
watch Scout the dog attempt to outwit Snuffler the dog at reading
the REPL. The water moved on, the bridge held its shad...
    ```

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

#### PARALLEL_POSSESSIVE_TIC

- `G1-07` (form `:tortoise`): user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic
    ```
    It happened on a day so ordinary that it seemed impossible anything could have been lost.

Max the dog chalked a wager on a flat stone in the meadow: whoever
predicted the result of `:kestrel` would set who crossed the
bridge first. Slate the dog, her face quiet, her hands quieter still, said it wou...
    ```
- `G1-14` (form `(* (+ 1 2) (+ 3 4))`): user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic
    ```
    Doodle the dog was crossing the stream near the meadow when she caught a glimpse of his own reflection.

"Watch the pile," Doodle the dog said, her face quiet, her hands quieter still, gesturing
at a small heap of bones beside the river. "Every operation
either adds, takes away, or combines what's a...
    ```
- `G2-01` (form `(+ 1 2 3 4 5 6 7 8 9 10)`): user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic
    ```
    When Toffee reached the bridge by the village, she paused to admire the bone he had been so lucky to find.

Toffee the dog, her face quiet, her hands quieter still, arranged a small heap of bones
by the village, careful with the count — the bridge's shadow long across
the water, every bone weighing ...
    ```
- `G2-02` (form `(<= 1 1 2)`): user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic
    ```
    The path home wound past a slow brook, and on bright days the brook was full of borrowed shapes.

Pointer the dog, her face quiet, her hands quieter still, arranged a small heap of bones
by the beach, careful with the count — the bridge's shadow long across
the water, every bone weighing what it wei...
    ```
- `G2-04` (form `(min -3 -1 -5)`): user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic
    ```
    Steel the dog was halfway home in the pond when the water played its old trick on a young dog.

Steel the dog, her face quiet, her hands quieter still, arranged a small heap of bones
in the pond, careful with the count — the bridge's shadow long across
the water, every bone weighing what it weighed....
    ```

#### ONLY_SHOOK_HEAD_TIC

- `G1-09` (form `(symbol? 'hare)`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    The water beneath the bridge was unhurried that day, and any creature looking down would see a perfect copy of itself.

Henry the dog, his mind already on the larger share, mistook the name on the bark for the
bone it pointed to. "It says bone, so the value must be the
bone!" Marigold the dog only s...
    ```
- `G2-18` (form `(count '(1 2 3))`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    A dog with a bone in his jaws is a happy creature; a dog who looks too hard at the water may not be.

Latte the dog, as one who would weigh his neighbour's loaf, mistook the name on the bark for the
bone it pointed to. "It says bone, so the value must be the
bone!" Cooper the dog only shook his head...
    ```
- `G10-01` (form `(let [x 5] `(a ~x b))`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    There is a kind of greed that does not see what it already has, and another kind that mistakes a reflection for a meal.

Runner the dog, with greed running ahead of his good sense, mistook the name on the bark for the
bone it pointed to. "It says bone, so the value must be the
bone!" Mocha the dog o...
    ```
- `G10-02` (form `(let [xs [1 2 3]] `(list ~@xs))`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    Pebble the dog was crossing the stream by the beach when he caught a glimpse of his own reflection.

Pickles the dog, as a crow turns a coin against the sun, mistook the name on the bark for the
bone it pointed to. "It says bone, so the value must be the
bone!" Pebble the dog only shook his head: th...
    ```

#### HIGH_LENGTH

- `G1-09` (form `(symbol? 42)`): user_msg 245 words
    ```
    Silver had crossed this bridge a hundred times by the village, but never with so fine a bone clamped in his jaws.

Patch the hound stood at the stream's edge, holding two objects side by side: a scratch-mark on bark and a smooth stone bearing the number 68. "This one is the symbol," Patch said, tapp...
    ```
- `G1-09` (form `(symbol? "tortoise")`): user_msg 224 words
    ```
    The bone was good, the day was warm, and the path was clear, and yet the trouble was already shaped in the water.

Patch the hound held a message scratched on bark — not a name to pass around, but a strand of letters. "The reader will treat this as text, not as a symbol the dogs can quote," Patch sa...
    ```
- `G1-09` (form `(= 'hare 'hare)`): user_msg 236 words
    ```
    in the meadow, where the boards of the bridge meet the stones of the path, Jack the dog caught sight of himself in the stream.

Rex the hound laid two scratch-marks side by side on bark near the forest. Both marks said the same thing: hare, hare. "Are these two scratches the same name?" Rex asked. "...
    ```
- `G1-10` (form `(+ 1 2) ;; sum of one and two`): user_msg 224 words
    ```
    The bone was good, the day was warm, and the path was clear, and yet the trouble was already shaped in the water.

Bell the hound wrote a form on a clean strip of bark near the pond, then added a double-semicolon mark followed by a note in plain words. "The note is only for other dogs to read," she ...
    ```
- `G1-11` (form `(+
  1
  2)`): user_msg 237 words
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
- `G1-13` (form `(+ 1 2)`): sentence with 5 commas reads as AI-output cadence: 'Snarler the dog, with steady, careful steps, arranged a small heap of bones\non t'
    ```
    There is a kind of greed that does not see what it already has, and another kind that mistakes a reflection for a meal.

Snarler the dog, with steady, careful steps, arranged a small heap of bones
on the road, careful with the count — the bridge's shadow long across
the water, every bone weighing wh...
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

#### NARRATIVE_NUMERAL_HARDCODE

- `G1-13` (form `(- 5 3)`): parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    ```
    A reflection is a strange kind of promise: present and unreachable, and very hard to argue with.

Mochi the dog, with the slow grace of a creature unhurried, arranged a small heap of bones
near the forest, careful with the count — the bridge's shadow long across
the water, every bone weighing what i...
    ```
- `G1-13` (form `(- 5 3)`): parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    ```
    The bone was good, the day was warm, and the path was clear, and yet the trouble was already shaped in the water.

Mocha the dog, as one waits who has waited many times before, arranged a small heap of bones
near the pond, careful with the count — the bridge's shadow long across
the water, every bon...
    ```
- `G1-13` (form `(- 5 3)`): parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    ```
    Retriever the dog was halfway home in the forest when the water played its old trick on a young dog.

Retriever the dog laid bones out on a flat stone near the forest, sorting
them into small piles. "Numbers in Clojure are just like bones
in piles," she said: "you can count them, you can
add two pil...
    ```
- `G1-13` (form `(* 4 5)`): parametric example has hard-coded English numeral 'four piles' in a story slot — the actual draws may differ from this fixed count
    ```
    The stream ran clear that afternoon, and the bridge cast a long trembling shadow across the water.

"Watch the pile," Ginger the dog said, in the slow rhythm of one who knows the road, gesturing
at a small heap of bones beside the river. "Every operation
either adds, takes away, or combines what's a...
    ```
- `G1-13` (form `(* 4 5)`): parametric example has hard-coded English numeral 'four piles' in a story slot — the actual draws may differ from this fixed count
    ```
    The path home wound past a slow brook, and on bright days the brook was full of borrowed shapes.

"Watch the pile," Yipper the dog said, with a calm that nothing seemed to ruffle, gesturing
at a small heap of bones beside the river. "Every operation
either adds, takes away, or combines what's alread...
    ```

#### RESOLUTION_GENERIC

- `G1-13` (form `(* 4 5)`): user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    ```
    The stream ran clear that afternoon, and the bridge cast a long trembling shadow across the water.

"Watch the pile," Ginger the dog said, in the slow rhythm of one who knows the road, gesturing
at a small heap of bones beside the river. "Every operation
either adds, takes away, or combines what's a...
    ```
- `G1-13` (form `(* 4 5)`): user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    ```
    The path home wound past a slow brook, and on bright days the brook was full of borrowed shapes.

"Watch the pile," Yipper the dog said, with a calm that nothing seemed to ruffle, gesturing
at a small heap of bones beside the river. "Every operation
either adds, takes away, or combines what's alread...
    ```
- `G1-14` (form `(* (+ 1 2) (+ 3 4))`): user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    ```
    Doodle the dog was crossing the stream near the meadow when she caught a glimpse of his own reflection.

"Watch the pile," Doodle the dog said, her face quiet, her hands quieter still, gesturing
at a small heap of bones beside the river. "Every operation
either adds, takes away, or combines what's a...
    ```
- `G1-14` (form `(- 100 (* 5 5))`): user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    ```
    Down by the stream where the bank dipped low, the world above was answered politely by the world below.

"Watch the pile," Sniff the dog said, stepping deliberately, one foot before the next, gesturing
at a small heap of bones beside the river. "Every operation
either adds, takes away, or combines w...
    ```
- `G1-14` (form `(- 100 (* 5 5))`): user_msg has canned 'the X the operation produced' resolution boilerplate — tie it to the fable's metaphor / drawn values
    ```
    Lunger had crossed this bridge a hundred times along the river bank, but never with so fine a bone clamped in his jaws.

"Watch the pile," Lunger the dog said, neither hastening nor hanging back, gesturing
at a small heap of bones beside the river. "Every operation
either adds, takes away, or combin...
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

#### PARAGRAPH_FRAGMENTATION

- `G2-01` (form `(* 2 3 4)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    Leo had carried his prize all the way from the village, and along the road the bridge offered him an unwelcome second look.

Patch the hound gathered three piles of bones near the meadow, each pile marked with a count: 2, 1, and 2.

They wanted the total if each pile was multiplied together — what 2...
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
- `G2-08` (form `(- 1 1/3)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    There was once a dog who carried a fine bone home along a path that crossed a stream by an old wooden bridge.

Bell the hound held one whole bone at the stream's edge and removed one-third of it. She wanted to know what fraction remained.

She needed the remainder when one-third was taken from one w...
    ```
- `G3-10` (form `(#(+ % 1) 5)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    The bone was good, the day was warm, and the path was clear, and yet the trouble was already shaped in the water.

Rex the hound traced a quick sniffing-path at the bank near the meadow. The marks said "Add one." He did not name this fleeting trail.

The form needed a one-use procedure so compact it...
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
- `G2-19` (form `(+ 99999999999 1)`): user_msg uses generic 'returned exactly' / 'settled with certainty' filler — describe what actually came back, not just that something did
    ```
    When Doodle reached the bridge by the beach, she paused to admire the bone he had been so lucky to find.

Rex the hound held an enormous pile of 99 billion, 999 million bones at the river bank. A single extra bone sat beside the pile. He wanted to know the total.

He needed the exact sum when one bo...
    ```

#### GENERIC_RESOLUTION_TAIL

- `G2-02` (form `(> 5 4 3 2 1)`): resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    ```
    in the forest, on a still afternoon by the brook, Ziggy learned what a reflection costs the careless.

Ziggy the dog, with the steady breathing of a long walker, arranged a small heap of bones
near the forest, careful with the count — the bridge's shadow long across
the water, every bone weighing wh...
    ```
- `G2-02` (form `(> 5 4 3 2 1)`): resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    ```
    on the beach, the stream ran clear enough to mirror anything that passed above it, and Whatsit passed above it.

Whatsit the dog, as the sun moves across the sky, slow and certain, arranged a small heap of bones
near the beach, careful with the count — the bridge's shadow long across
the water, ever...
    ```
- `G2-02` (form `(> 5 4 3 2 1)`): resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    ```
    When Galloper reached the bridge near the pond, she paused to admire the bone he had been so lucky to find.

Galloper the dog laid bones out on a flat stone near the pond, sorting
them into small piles. "Numbers in Clojure are just like bones
in piles," she said: "you can count them, you can
add two...
    ```

#### SMALL_INT_LEAK

- `G2-05` (form `(mod -7 3)`): small-int answer 2 leaks via resolution-slot phrasing
    ```
    It is one of the oldest tricks of light to make one bone seem like two and to make a fool of the unwary.

Bell the hound stood by the river bank holding a negative value — negative seven — and wanted to find its modulo against three. Negative numbers in modulo work in their own way.

She needed to k...
    ```

#### STORY_RESOLUTION_NO_DRAWN

- `G2-08` (form `(+ 1/2 1/4)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    ```
    Slate had found the bone by the village and was carrying it home with no small amount of pride.

"Whatever the pile looks like after the operation,"
Slate the dog said, "the runtime gives the exact count — small
or large, fraction or whole, the answer is precise." To
add one-half and one-quarter, sh...
    ```
- `G2-08` (form `(+ 1/2 1/4)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    ```
    The bone was good, the day was warm, and the path was clear, and yet the trouble was already shaped in the water.

Rex the hound broke two bones into pieces near the meadow. One bone yielded one-half, the other one-quarter. He wanted to know the combined measure.

He needed the total when the two fr...
    ```
- `G2-08` (form `(+ 1/2 1/4)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    ```
    Some lessons are taught by mirrors, and some are taught by rivers; this one was taught by both at once.

Russet the dog, as one waits who has waited many times before, arranged a small heap of bones
at the edge of the meadow, careful with the count — the bridge's shadow long across
the water, every ...
    ```
- `G2-08` (form `(* 2/3 3/4)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3', '4'), resolution doesn't close the loop)
    ```
    There is a kind of greed that does not see what it already has, and another kind that mistakes a reflection for a meal.

"Whatever the pile looks like after the operation,"
Loki the dog said, "the runtime gives the exact count — small
or large, fraction or whole, the answer is precise." To
multiply ...
    ```
- `G2-08` (form `(* 2/3 3/4)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3', '4'), resolution doesn't close the loop)
    ```
    It was near the road, on the wooden bridge above the slow brook, that Ebony the dog looked down at the water.

Snowy the dog eyed the pile, as a crow turns a coin against the sun, and called out a guess
about how many bones were there without bothering to count.
Ebony the dog simply began counting —...
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

#### CONCEPT_PHRASE_COMMA_LIST

- `G9-03` (form `(do (def a (atom 0)) (swap! a inc) @a)`): concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    Diesel had crossed this bridge a hundred times on the beach, but never with so fine a bone clamped in his jaws.

Bell the hound opened the shared notebook at the stream's edge and scratched a fresh zero onto the first page. This tally-stone would record how many bones the pack had gathered as the da...
    ```
- `G9-03` (form `(do (def a (atom 0)) (swap! a inc) @a)`): concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    in the forest, the stream ran clear enough to mirror anything that passed above it, and Leo passed above it.

Shepherd the dog, his thoughts already on more, swiped a paw across the tally-stone,
trying to scratch an answer over the count. Leo the dog caught
her firmly: tallies shared by all the pack...
    ```
- `G9-03` (form `(do (def a (atom 0)) (swap! a inc) @a)`): concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    It was an afternoon of quiet sky and steady current, and the world below the surface seemed almost solid.

"The tally stays scratched into the stone," Tippet the dog said,
"so any dog who comes by can read what's there right now. The
count changes only when one of us scratches a new one — and only
a...
    ```
- `G9-03` (form `(do (def a (atom 10)) (swap! a + 5) @a)`): concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    The bridge had stood there as long as anyone remembered, and so had the temptation it offered to anyone crossing with full jaws.

Fudge the dog, his fingers twitching at the thought of profit, swiped a paw across the tally-stone,
trying to scratch an answer over the count. Salty the dog caught
her f...
    ```
- `G9-03` (form `(do (def a (atom 10)) (swap! a + 5) @a)`): concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    The bone was good, the day was warm, and the path was clear, and yet the trouble was already shaped in the water.

"When I want to update the tally," Ivory the dog said, "I don't
pick the stone up and walk away — I read the scratch, apply the
change, and scratch the new count back, all in a single m...
    ```

