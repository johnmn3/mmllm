# milkmaid curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

### G1-01: Eval as substitution

- examples: 4
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'LOW_GROUNDING': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`nil` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`nil` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-02: Integer numbers

- examples: 6
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 3, 'LOW_GROUNDING': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`-3` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`-3` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`0` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`-25` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-03: Ratios

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [LOW_GROUNDING] form=`1/2` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(+ 1/2 1/4)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(+ 1/2 1/4)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-05: Booleans

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'FORM_DISPLAY_AND_FORM_NOUN': 4}
    - [LOW_GROUNDING] form=`true` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`false` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`false` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`false` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(= 1 1)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-06: nil

- examples: 5
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 3, 'LOW_GROUNDING': 4}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(nil? nil)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(nil? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(nil? nil)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(nil? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(nil? 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(nil? false)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-07: Keywords

- examples: 5
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`:hare` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(= :hare :hare)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-08: Characters

- examples: 4
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 3, 'STRING_AS_CHAR_MISCLAIM': 6}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`\h` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`\space` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [STRING_AS_CHAR_MISCLAIM] form=`\space` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    - [STRING_AS_CHAR_MISCLAIM] form=`\space` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    - [STRING_AS_CHAR_MISCLAIM] form=`\space` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    - [STRING_AS_CHAR_MISCLAIM] form=`\T` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)

### G1-09: Symbols vs values

- examples: 4
- variety @ n=50: 1.00
- issues: {'PRONOUN_BEFORE_NAME': 2, 'PARALLEL_POSSESSIVE_TIC': 1, 'LOW_GROUNDING': 1}
    - [PRONOUN_BEFORE_NAME] form=`(symbol? 'hare)` — sentence-initial 'She' appears before any named character is introduced
    - [PARALLEL_POSSESSIVE_TIC] form=`(symbol? 'hare)` — user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic
    - [PRONOUN_BEFORE_NAME] form=`(symbol? "tortoise")` — sentence-initial 'She' appears before any named character is introduced
    - [LOW_GROUNDING] form=`(= 'hare 'hare)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-10: Comments

- examples: 2
- variety @ n=50: 1.00
- issues: {'THE_FORM_OVERUSE': 1, 'DOUBLE_EMO_INJECTION': 1, 'REPL_TRIPLE_VOICE': 1}
    - [THE_FORM_OVERUSE] form=`(+ 1 2) ; sum of one and two` — `the form` appears 6 times in user_msg (template tic — vary references)
    - [DOUBLE_EMO_INJECTION] form=`(+ 1 2) ; sum of one and two` — sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat
    - [REPL_TRIPLE_VOICE] form=`(+ 1 2) ; sum of one and two` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G1-11: Whitespace doesn't matter

- examples: 2
- variety @ n=50: 1.00
- issues: {'THE_FORM_OVERUSE': 2, 'CLAUSE_STACK_OVERFLOW': 1, 'POINTED_AND_SAID_TIC': 1, 'PARALLEL_POSSESSIVE_TIC': 1}
    - [THE_FORM_OVERUSE] form=`(+    1    2)` — `the form` appears 6 times in user_msg (template tic — vary references)
    - [THE_FORM_OVERUSE] form=`(+
  1
  2)` — `the form` appears 6 times in user_msg (template tic — vary references)
    - [CLAUSE_STACK_OVERFLOW] form=`(+
  1
  2)` — sentence with 6 commas reads as AI-output cadence: 'Xaverius, her face quiet, her hands quieter still, pointed and said: "The chalk '
    - [POINTED_AND_SAID_TIC] form=`(+
  1
  2)` — user_msg uses 'X, [appositive], pointed and said:' — overused AI dialogue cadence
    - [PARALLEL_POSSESSIVE_TIC] form=`(+
  1
  2)` — user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic

### G1-12: Parens group; they don't multiply

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'POINTED_AND_SAID_TIC': 1, 'THE_FORM_OVERUSE': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(+ 2 3)` — sentence with 5 commas reads as AI-output cadence: 'Theophilus, with the steady measure of a long walker, pointed and said: "The cha'
    - [POINTED_AND_SAID_TIC] form=`(+ 2 3)` — user_msg uses 'X, [appositive], pointed and said:' — overused AI dialogue cadence
    - [THE_FORM_OVERUSE] form=`(+ 2 3)` — `the form` appears 6 times in user_msg (template tic — vary references)
    - [THE_FORM_OVERUSE] form=`(* (+ 1 2) 3)` — `the form` appears 6 times in user_msg (template tic — vary references)
    - [THE_FORM_OVERUSE] form=`(* (+ 1 2) 3)` — `the form` appears 6 times in user_msg (template tic — vary references)

### G1-13: First arithmetic call

- examples: 6
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'REPL_TRIPLE_VOICE': 1, 'ANSWER_LEAK': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(* 4 5)` — parametric example has hard-coded English numeral 'four piles' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(* 4 5)` — parametric example has hard-coded English numeral 'four piles' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(* 4 5)` — parametric example has hard-coded English numeral 'four piles' in a story slot — the actual draws may differ from this fixed count
    - [REPL_TRIPLE_VOICE] form=`(/ 10 2)` — user_msg mentions 'REPL' 5 times — the REPL personification should appear at most twice per record (submit + return)
    - [ANSWER_LEAK] form=`(- 20 7)` — answer 13 in narrative

### G1-14: Nested call evaluation

- examples: 4
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1, 'PRONOUN_BEFORE_NAME': 1, 'REPL_TRIPLE_VOICE': 1}
    - [ANSWER_LEAK] form=`(+ 1 (* 2 3))` — answer 7 in narrative
    - [PRONOUN_BEFORE_NAME] form=`(+ 1 (* 2 3))` — sentence-initial 'She' appears before any named character is introduced
    - [REPL_TRIPLE_VOICE] form=`(- 100 (* 5 5))` — user_msg mentions 'REPL' 4 times — the REPL personification should appear at most twice per record (submit + return)

### G1-15: Equality

- examples: 6
- variety @ n=50: 1.00
- issues: {'DOUBLE_EMO_IN_SENTENCE': 4, 'DOUBLE_EMO_INJECTION': 4, 'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [DOUBLE_EMO_IN_SENTENCE] form=`(= 1 1)` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(= 1 1)` — sentence has 2+ distinct EMO-pool phrases ('with a calm that nothing seeme' + 'as if the prize already sat in') — the character can't earn two emotional registers in the same beat
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(= 1 1)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [DOUBLE_EMO_IN_SENTENCE] form=`(= 1 2)` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(= 1 2)` — sentence has 2+ distinct EMO-pool phrases ('with a calm that nothing seeme' + 'with a smug grin') — the character can't earn two emotional registers in the same beat
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(= 1 2)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-16: Numeric predicates

- examples: 6
- variety @ n=50: 1.00
- issues: {'PRONOUN_BEFORE_NAME': 2, 'LOW_GROUNDING': 1, 'DOUBLE_EMO_INJECTION': 1}
    - [PRONOUN_BEFORE_NAME] form=`(zero? 5)` — sentence-initial 'She' appears before any named character is introduced
    - [LOW_GROUNDING] form=`(pos? 7)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_EMO_INJECTION] form=`(neg? -3)` — sentence has 2+ distinct EMO-pool phrases ('without complaint or hurry' + 'without complaint') — the character can't earn two emotional registers in the same beat
    - [PRONOUN_BEFORE_NAME] form=`(neg? -3)` — sentence-initial 'She' appears before any named character is introduced

### G1-17: Printing vs returning

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'POINTED_AND_SAID_TIC': 2, 'PRONOUN_BEFORE_NAME': 1, 'PROCEDURAL_OPENER': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`42` — sentence with 5 commas reads as AI-output cadence: 'Urbanus, settled in for a long wait, pointed and said: "The chalk marks explain '
    - [POINTED_AND_SAID_TIC] form=`42` — user_msg uses 'X, [appositive], pointed and said:' — overused AI dialogue cadence
    - [CLAUSE_STACK_OVERFLOW] form=`42` — sentence with 5 commas reads as AI-output cadence: 'Anselmo, with steady breath and a careful eye, pointed and said: "The chalk mark'
    - [POINTED_AND_SAID_TIC] form=`42` — user_msg uses 'X, [appositive], pointed and said:' — overused AI dialogue cadence
    - [PRONOUN_BEFORE_NAME] form=`42` — sentence-initial 'She' appears before any named character is introduced
    - [PROCEDURAL_OPENER] form=`(+ 1 2)` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence

### G1-18: Errors are safe in the REPL

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOWERCASE_CONCEPT_AFTER_PERIOD': 2, 'PRONOUN_BEFORE_NAME': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'REPL_TRIPLE_VOICE': 1}
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(+ 1 2)` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    - [PRONOUN_BEFORE_NAME] form=`(+ 1 2)` — sentence-initial 'She' appears before any named character is introduced
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(* 7 6)` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(* 7 6)` — parametric example has hard-coded English numeral 'seven piles' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(* 7 6)` — parametric example has hard-coded English numeral 'seven piles' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(* 7 6)` — parametric example has hard-coded English numeral 'seven piles' in a story slot — the actual draws may differ from this fixed count

## Grade 2

### G2-01: Multi-arg arithmetic

- examples: 6
- variety @ n=50: 1.00
- issues: {'PARALLEL_POSSESSIVE_TIC': 2, 'NARRATIVE_NUMERAL_HARDCODE': 12, 'CLAUSE_STACK_OVERFLOW': 2, 'DOUBLE_EMO_INJECTION': 3}
    - [PARALLEL_POSSESSIVE_TIC] form=`(+ 1 2 3 4)` — user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(* 2 3 4)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(* 2 3 4)` — sentence with 5 commas reads as AI-output cadence: 'Vespasia only shook her\nhead, stepping deliberately, one foot before the next, a'
    - [DOUBLE_EMO_INJECTION] form=`(* 2 3 4)` — sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(* 2 3 4)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(* 2 3 4)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count

### G2-02: Comparison chains

- examples: 5
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 9, 'PRONOUN_BEFORE_NAME': 2, 'HIGH_LENGTH': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(< 3 2 1)` — parametric example has hard-coded English numeral 'three piles' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(< 3 2 1)` — parametric example has hard-coded English numeral 'three piles' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(< 3 2 1)` — parametric example has hard-coded English numeral 'three piles' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(<= 1 1 2)` — parametric example has hard-coded English numeral 'three piles' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(<= 1 1 2)` — parametric example has hard-coded English numeral 'three piles' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(<= 1 1 2)` — parametric example has hard-coded English numeral 'three piles' in a story slot — the actual draws may differ from this fixed count

### G2-03: not= and = with multiple args

- examples: 5
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(not= 1 2)` — sentence with 6 commas reads as AI-output cadence: 'Theophilus only shook his\nhead, her breath even, her step even, her thought even'
    - [CLAUSE_STACK_OVERFLOW] form=`(= 1 1 1)` — sentence with 6 commas reads as AI-output cadence: '"To test whether 1, 1, and 1 are all equal, we must count — truly count, and the'
    - [CLAUSE_STACK_OVERFLOW] form=`(= 1 1 1)` — sentence with 6 commas reads as AI-output cadence: '"To test whether 1, 1, and 1 are all equal, we must count — truly count, and the'

### G2-04: min and max

- examples: 5
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 12, 'CLAUSE_STACK_OVERFLOW': 5}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(max 1 2 3)` — parametric example has hard-coded English numeral 'three piles' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(max 1 2 3)` — parametric example has hard-coded English numeral 'three piles' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(max 1 2 3)` — parametric example has hard-coded English numeral 'three piles' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(max 1 2 3)` — sentence with 6 commas reads as AI-output cadence: '"To find the maximum of 1, 5, and 3, we must count — truly count, and the maximu'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(min 7 3 9 1 5)` — parametric example has hard-coded English numeral 'five counts' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(min 7 3 9 1 5)` — sentence with 8 commas reads as AI-output cadence: '"To find the minimum of 2, 9, 9, 7, and 0, we must count — truly count, and the '

### G2-05: quot, rem, mod

- examples: 6
- variety @ n=50: 1.00
- issues: {'PROCEDURAL_OPENER': 1, 'DOUBLE_EMO_INJECTION': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'PRONOUN_BEFORE_NAME': 4, 'ANSWER_LEAK': 1, 'PARALLEL_POSSESSIVE_TIC': 1}
    - [PROCEDURAL_OPENER] form=`(quot 17 5)` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    - [DOUBLE_EMO_INJECTION] form=`(quot 17 5)` — sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat
    - [CLAUSE_STACK_OVERFLOW] form=`(quot 17 5)` — sentence with 6 commas reads as AI-output cadence: 'Theodoric only shook his\nhead, her breath even, her step even, her thought even,'
    - [CLAUSE_STACK_OVERFLOW] form=`(rem 17 5)` — sentence with 6 commas reads as AI-output cadence: 'Maximilian only shook his\nhead, her breath even, her step even, her thought even'
    - [PRONOUN_BEFORE_NAME] form=`(mod 17 5)` — sentence-initial 'She' appears before any named character is introduced
    - [PRONOUN_BEFORE_NAME] form=`(mod 17 5)` — sentence-initial 'She' appears before any named character is introduced

### G2-06: inc and dec

- examples: 5
- variety @ n=50: 1.00
- issues: {'PRONOUN_BEFORE_NAME': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_EMO_INJECTION': 1, 'LOW_GROUNDING': 1, 'PARALLEL_POSSESSIVE_TIC': 1}
    - [PRONOUN_BEFORE_NAME] form=`(inc 5)` — sentence-initial 'She' appears before any named character is introduced
    - [CLAUSE_STACK_OVERFLOW] form=`(inc 5)` — sentence with 5 commas reads as AI-output cadence: 'Zerlina only shook her\nhead, stepping deliberately, one foot before the next, an'
    - [DOUBLE_EMO_INJECTION] form=`(inc 5)` — sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat
    - [LOW_GROUNDING] form=`(inc 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PARALLEL_POSSESSIVE_TIC] form=`(dec 0)` — user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic

### G2-07: Absolute value

- examples: 4
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'DOUBLE_EMO_INJECTION': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(abs 5)` — sentence with 5 commas reads as AI-output cadence: 'Euclid only shook his\nhead, her steps unhurried, her mind clear, and began sorti'
    - [DOUBLE_EMO_INJECTION] form=`(abs 5)` — sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat
    - [CLAUSE_STACK_OVERFLOW] form=`(abs (- 3 8))` — sentence with 5 commas reads as AI-output cadence: 'Sigismund only shook his\nhead, with steady, careful steps, and began sorting the'

### G2-08: Arithmetic on ratios

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1/2 1/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(+ 1/2 1/4)` — sentence with 5 commas reads as AI-output cadence: 'Konstantin only shook his\nhead, with steady, road-tested feet, and began sorting'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1/2 1/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1/2 1/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 2/3 3/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 2/3 3/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3', '4'), resolution doesn't close the loop)

### G2-09: Floats vs ints (the / operator)

- examples: 3
- variety @ n=50: 1.00
- issues: {'PRONOUN_BEFORE_NAME': 2, 'DOUBLE_EMO_INJECTION': 1}
    - [PRONOUN_BEFORE_NAME] form=`(/ 10 3)` — sentence-initial 'She' appears before any named character is introduced
    - [PRONOUN_BEFORE_NAME] form=`(/ 1.0 2)` — sentence-initial 'She' appears before any named character is introduced
    - [DOUBLE_EMO_INJECTION] form=`(/ 1.0 2)` — sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat

### G2-10: Powers via repeated multiplication

- examples: 4
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 2, 'PARAGRAPH_FRAGMENTATION': 4}
    - [ANSWER_LEAK] form=`(* 5 5)` — answer 25 in narrative
    - [PARAGRAPH_FRAGMENTATION] form=`(* 5 5)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [ANSWER_LEAK] form=`(* 3 3 3 3)` — answer 81 in narrative
    - [PARAGRAPH_FRAGMENTATION] form=`(* 3 3 3 3)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [PARAGRAPH_FRAGMENTATION] form=`(* 10 10)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [PARAGRAPH_FRAGMENTATION] form=`(* 10 10)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G2-11: String concatenation with str

- examples: 4
- variety @ n=50: 1.00
- issues: {'PRONOUN_BEFORE_NAME': 2, 'PARAGRAPH_FRAGMENTATION': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'LOW_GROUNDING': 1}
    - [PRONOUN_BEFORE_NAME] form=`(str 42)` — sentence-initial 'She' appears before any named character is introduced
    - [PARAGRAPH_FRAGMENTATION] form=`(str "p" "q" "r")` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(str 1 "+" 2 "=" 3)` — parametric example has hard-coded English numeral 'five elements' in a story slot — the actual draws may differ from this fixed count
    - [PRONOUN_BEFORE_NAME] form=`(str 1 "+" 2 "=" 3)` — sentence-initial 'She' appears before any named character is introduced
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(str 1 "+" 2 "=" 3)` — parametric example has hard-coded English numeral 'five elements' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(str 1 "+" 2 "=" 3)` — parametric example has hard-coded English numeral 'five elements' in a story slot — the actual draws may differ from this fixed count

### G2-12: print and println — return values

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3, 'POINTED_AND_SAID_TIC': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(println "hello")` — sentence with 5 commas reads as AI-output cadence: 'Theophilus, without lifting her voice or quickening her step, pointed and said: '
    - [POINTED_AND_SAID_TIC] form=`(println "hello")` — user_msg uses 'X, [appositive], pointed and said:' — overused AI dialogue cadence
    - [CLAUSE_STACK_OVERFLOW] form=`(println "hello")` — sentence with 5 commas reads as AI-output cadence: 'Maximilian, with the unrushed care of a long task, pointed and said: "The chalk '
    - [POINTED_AND_SAID_TIC] form=`(println "hello")` — user_msg uses 'X, [appositive], pointed and said:' — overused AI dialogue cadence
    - [CLAUSE_STACK_OVERFLOW] form=`(println "hello")` — sentence with 5 commas reads as AI-output cadence: 'Apollonia, with the slow certainty of the sun, pointed and said: "The chalk mark'
    - [POINTED_AND_SAID_TIC] form=`(println "hello")` — user_msg uses 'X, [appositive], pointed and said:' — overused AI dialogue cadence

### G2-13: and / or — short circuit, return values

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'REPEATED_OPENER_FRAGMENT': 1, 'DOUBLE_EMO_IN_SENTENCE': 1, 'DOUBLE_EMO_INJECTION': 1, 'BOOL_LEAK_RESOLUTION': 1, 'PARAGRAPH_FRAGMENTATION': 2, 'NARRATIVE_NUMERAL_HARDCODE': 6}
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(and true false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [REPEATED_OPENER_FRAGMENT] form=`(or false true)` — opener fragment 'pail balanced carefully on her head' also appears later in user_msg
    - [DOUBLE_EMO_IN_SENTENCE] form=`(or false false)` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(or false false)` — sentence has 2+ distinct EMO-pool phrases ('neither restless nor weary, on' + 'his chest thrown out before hi') — the character can't earn two emotional registers in the same beat
    - [LOW_GROUNDING] form=`(or false false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-14: not — turning truthy to false

- examples: 5
- variety @ n=50: 1.00
- issues: {'DOUBLE_EMO_IN_SENTENCE': 4, 'DOUBLE_EMO_INJECTION': 4, 'LOW_GROUNDING': 4, 'BOOL_LEAK_RESOLUTION': 2, 'PARAGRAPH_FRAGMENTATION': 1}
    - [DOUBLE_EMO_IN_SENTENCE] form=`(not true)` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(not true)` — sentence has 2+ distinct EMO-pool phrases ('her breath even, her step even' + 'with the loud bark of a sure w') — the character can't earn two emotional registers in the same beat
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_EMO_IN_SENTENCE] form=`(not false)` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(not false)` — sentence has 2+ distinct EMO-pool phrases ('her quiet hands at her quiet s' + 'his voice loud over the quiet ') — the character can't earn two emotional registers in the same beat
    - [BOOL_LEAK_RESOLUTION] form=`(not false)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead

### G2-15: Falsey values: only false and nil

- examples: 4
- variety @ n=50: 1.00
- issues: {'DOUBLE_EMO_IN_SENTENCE': 3, 'DOUBLE_EMO_INJECTION': 3, 'LOW_GROUNDING': 1}
    - [DOUBLE_EMO_IN_SENTENCE] form=`(if 0 1 0)` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(if 0 1 0)` — sentence has 2+ distinct EMO-pool phrases ('sure of the win, head held hig' + 'with the calm of long custom') — the character can't earn two emotional registers in the same beat
    - [DOUBLE_EMO_IN_SENTENCE] form=`(if "" 1 0)` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(if "" 1 0)` — sentence has 2+ distinct EMO-pool phrases ('with the slow grace of a creat' + 'sure of the win, head held hig') — the character can't earn two emotional registers in the same beat
    - [DOUBLE_EMO_IN_SENTENCE] form=`(if "" 1 0)` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(if "" 1 0)` — sentence has 2+ distinct EMO-pool phrases ('with a calm that nothing seeme' + 'with a smug grin') — the character can't earn two emotional registers in the same beat

### G2-16: Truthy 0 and empty string

- examples: 4
- variety @ n=50: 1.00
- issues: {'DOUBLE_EMO_IN_SENTENCE': 1, 'DOUBLE_EMO_INJECTION': 2, 'LOW_GROUNDING': 1}
    - [DOUBLE_EMO_IN_SENTENCE] form=`(boolean "")` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(boolean "")` — sentence has 2+ distinct EMO-pool phrases ("with a hen's long stillness on" + 'with quiet steps, taking the l') — the character can't earn two emotional registers in the same beat
    - [DOUBLE_EMO_INJECTION] form=`(boolean nil)` — sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat
    - [LOW_GROUNDING] form=`(boolean false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-17: Keyword as function for map lookup

- examples: 3
- variety @ n=50: 1.00
- issues: {'PRONOUN_BEFORE_NAME': 2, 'PARALLEL_POSSESSIVE_TIC': 1, 'LOW_GROUNDING': 1}
    - [PRONOUN_BEFORE_NAME] form=`(:hare {:hare 1 :tortoise 2})` — sentence-initial 'She' appears before any named character is introduced
    - [PRONOUN_BEFORE_NAME] form=`(:hare {:hare 1 :tortoise 2})` — sentence-initial 'She' appears before any named character is introduced
    - [PARALLEL_POSSESSIVE_TIC] form=`(:tortoise {:hare 1 :tortoise 2})` — user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic
    - [LOW_GROUNDING] form=`(:tortoise {:hare 1 :tortoise 2})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-18: Quoting symbols

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'BOOL_LEAK_RESOLUTION': 1, 'DOUBLE_EMO_IN_SENTENCE': 1, 'DOUBLE_EMO_INJECTION': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [LOW_GROUNDING] form=`(= (quote tortoise) 'tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [BOOL_LEAK_RESOLUTION] form=`(= (quote tortoise) 'tortoise)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(= (quote tortoise) 'tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_EMO_IN_SENTENCE] form=`(= (quote tortoise) 'tortoise)` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(= (quote tortoise) 'tortoise)` — sentence has 2+ distinct EMO-pool phrases ('with the ringing pride of a ha' + 'settled in for a long wait') — the character can't earn two emotional registers in the same beat
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count '(1 2 3))` — parametric example has hard-coded English numeral 'three elements' in a story slot — the actual draws may differ from this fixed count

### G2-19: Auto-promotion to bigint

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 2, 'PRONOUN_BEFORE_NAME': 1, 'ANSWER_LEAK': 1}
    - [REPL_TRIPLE_VOICE] form=`(* 1000000 1000000)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`(* 1000000 1000000)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [PRONOUN_BEFORE_NAME] form=`(+ 99999999999 1)` — sentence-initial 'She' appears before any named character is introduced
    - [ANSWER_LEAK] form=`(+ 99999999999 1)` — answer 100000000000 in narrative

### G2-20: Counting

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'LOWERCASE_CONCEPT_AFTER_PERIOD': 3, 'PARALLEL_POSSESSIVE_TIC': 1, 'PRONOUN_BEFORE_NAME': 3, 'DOUBLED_PLACE': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'That is how to\ncount the elements in the vector containing 1, 2, and 3 — walk th'
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(count [1 2 3])` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    - [CLAUSE_STACK_OVERFLOW] form=`(count "hello")` — sentence with 5 commas reads as AI-output cadence: 'She, her face quiet, her hands quieter still, explained, "the count operation is'
    - [PARALLEL_POSSESSIVE_TIC] form=`(count "hello")` — user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(count "hello")` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    - [PRONOUN_BEFORE_NAME] form=`(count "hello")` — sentence-initial 'She' appears before any named character is introduced

### G2-21: String length and substring

- examples: 3
- variety @ n=50: 1.00
- issues: {'SMALL_INT_LEAK': 1, 'PARAGRAPH_FRAGMENTATION': 1, 'PRONOUN_BEFORE_NAME': 1}
    - [SMALL_INT_LEAK] form=`(count "hare")` — small-int answer 4 leaks via resolution-slot phrasing
    - [PARAGRAPH_FRAGMENTATION] form=`(count "hare")` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [PRONOUN_BEFORE_NAME] form=`(count (subs "tortoise" 0 3))` — sentence-initial 'He' appears before any named character is introduced

### G2-22: Compose pure arithmetic (multi-step calculation)

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'ANSWER_LEAK': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(- (* 5 4) 7)` — sentence with 5 commas reads as AI-output cadence: '"To compute 7 times 8, then subtract 0, we must count — truly count, and the nes'
    - [ANSWER_LEAK] form=`(+ (* 3 8) (* 2 4))` — answer 32 in narrative
    - [ANSWER_LEAK] form=`(+ (* 3 8) (* 2 4))` — answer 32 in narrative

## Grade 3

### G3-02: def — redefinition

- examples: 1
- variety @ n=50: 1.00
- issues: {'DOUBLE_EMO_INJECTION': 1, 'ONLY_SHOOK_HEAD_TIC': 1}
    - [DOUBLE_EMO_INJECTION] form=`(do (def x 1) (def x 99) x)` — sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat
    - [ONLY_SHOOK_HEAD_TIC] form=`(do (def x 1) (def x 99) x)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

### G3-03: let — local binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'DOUBLE_EMO_IN_SENTENCE': 1, 'DOUBLE_EMO_INJECTION': 1, 'CLAUSE_STACK_OVERFLOW': 3}
    - [DOUBLE_EMO_IN_SENTENCE] form=`(let [x 3] (+ x 1))` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(let [x 3] (+ x 1))` — sentence has 2+ distinct EMO-pool phrases ('with a pride that filled him f' + 'with the soft patience of runn') — the character can't earn two emotional registers in the same beat
    - [CLAUSE_STACK_OVERFLOW] form=`(let [x 3] (+ x 1))` — sentence with 6 commas reads as AI-output cadence: 'Why, I\'ve already tucked the answer into my apron-pocket," she, sure of the win,'
    - [CLAUSE_STACK_OVERFLOW] form=`(let [n 10] (* n n))` — sentence with 5 commas reads as AI-output cadence: 'Why, I\'ve already tucked the answer into my apron-pocket," she, as if the race w'
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a 5] a)` — sentence with 5 commas reads as AI-output cadence: 'Why, I\'ve already tucked the answer into my apron-pocket," she, his chest thrown'

### G3-04: let — multi-binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'ONLY_SHOOK_HEAD_TIC': 1, 'DOUBLE_EMO_IN_SENTENCE': 1, 'DOUBLE_EMO_INJECTION': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'ANSWER_LEAK': 2}
    - [ONLY_SHOOK_HEAD_TIC] form=`(let [a 1 b 2] (+ a b))` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [DOUBLE_EMO_IN_SENTENCE] form=`(let [x 5 y 3] (- x y))` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(let [x 5 y 3] (- x y))` — sentence has 2+ distinct EMO-pool phrases ('with the broad pride of a long' + 'with the steady breathing of a') — the character can't earn two emotional registers in the same beat
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [a 2 b 3 c 4] (+ a b c))` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [ANSWER_LEAK] form=`(let [a 2 b 3 c 4] (+ a b c))` — answer 9 in narrative
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [a 2 b 3 c 4] (+ a b c))` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count

### G3-05: let — shadowing outer def

- examples: 2
- variety @ n=50: 1.00
- issues: {'PARAGRAPH_FRAGMENTATION': 1, 'DOUBLE_EMO_IN_SENTENCE': 2, 'DOUBLE_EMO_INJECTION': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [PARAGRAPH_FRAGMENTATION] form=`(do (def x 10) (let [x 99] x))` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [DOUBLE_EMO_IN_SENTENCE] form=`(do (def x 10) (let [x 99] x))` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(do (def x 10) (let [x 99] x))` — sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'as a young rooster crows above') — the character can't earn two emotional registers in the same beat
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def x 10) (let [x 99] x) x)` — sentence with 5 commas reads as AI-output cadence: 'Why, I\'ve already tucked the answer into my apron-pocket," she, with the warm pr'
    - [DOUBLE_EMO_IN_SENTENCE] form=`(do (def x 10) (let [x 99] x) x)` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(do (def x 10) (let [x 99] x) x)` — sentence has 2+ distinct EMO-pool phrases ('with no need to hurry the work' + 'puffed up with pride') — the character can't earn two emotional registers in the same beat

### G3-06: let — binding can reference prior

- examples: 2
- variety @ n=50: 1.00
- issues: {'ONLY_SHOOK_HEAD_TIC': 2, 'HIGH_LENGTH': 1, 'ANSWER_LEAK': 2, 'PARAGRAPH_FRAGMENTATION': 1}
    - [ONLY_SHOOK_HEAD_TIC] form=`(let [a 5 b (* a 2)] b)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [HIGH_LENGTH] form=`(let [a 5 b (* a 2)] b)` — user_msg 219 words
    - [ANSWER_LEAK] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — answer 8 in narrative
    - [ONLY_SHOOK_HEAD_TIC] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [PARAGRAPH_FRAGMENTATION] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [ANSWER_LEAK] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — answer 8 in narrative

### G3-07: fn — anonymous function

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_EMO_IN_SENTENCE': 1, 'DOUBLE_EMO_INJECTION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (+ x 1)) 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (+ x 1)) 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (+ x 1)) 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [a b] (* a b)) 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [DOUBLE_EMO_IN_SENTENCE] form=`((fn [a b] (* a b)) 3 4)` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`((fn [a b] (* a b)) 3 4)` — sentence has 2+ distinct EMO-pool phrases ('neither restless nor weary, on' + 'with great whoops of laughter') — the character can't earn two emotional registers in the same beat

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
- issues: {'DOUBLE_EMO_IN_SENTENCE': 1, 'DOUBLE_EMO_INJECTION': 1, 'ANSWER_LEAK': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'HIGH_LENGTH': 1}
    - [DOUBLE_EMO_IN_SENTENCE] form=`(do (defn dbl [x] (* x 2)) (dbl 5))` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(do (defn dbl [x] (* x 2)) (dbl 5))` — sentence has 2+ distinct EMO-pool phrases ('with the warm pride that goes ' + 'with a calm that nothing seeme') — the character can't earn two emotional registers in the same beat
    - [ANSWER_LEAK] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — answer 6 in narrative
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — sentence with 5 commas reads as AI-output cadence: 'Skip a step, and you skip part of the multi-argument function definition and cal'
    - [HIGH_LENGTH] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — user_msg 224 words

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_EMO_IN_SENTENCE': 1, 'DOUBLE_EMO_INJECTION': 1, 'HIGH_LENGTH': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(+ % 1) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [DOUBLE_EMO_IN_SENTENCE] form=`(#(+ % 1) 5)` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(#(+ % 1) 5)` — sentence has 2+ distinct EMO-pool phrases ('with a laugh that carried over' + 'with the steady turn of a mill') — the character can't earn two emotional registers in the same beat
    - [HIGH_LENGTH] form=`(#(+ % 1) 5)` — user_msg 221 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(+ % 1) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(+ % 1) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)

### G3-11: Substitution rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'ONLY_SHOOK_HEAD_TIC': 2, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [ONLY_SHOOK_HEAD_TIC] form=`(let [a 7] (+ a a))` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (* x x)) 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [ONLY_SHOOK_HEAD_TIC] form=`((fn [x] (* x x)) 6)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (* x x)) 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`((fn [x] (* x x)) 6)` — sentence with 5 commas reads as AI-output cadence: 'Why, I\'ve already tucked the answer into my apron-pocket," she, with a laugh tha'
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (* x x)) 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)

### G3-12: Scope vs namespace

- examples: 1
- variety @ n=50: 1.00
- issues: {'PARALLEL_POSSESSIVE_TIC': 1, 'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [PARALLEL_POSSESSIVE_TIC] form=`(do (def g 5) (let [g 99] (+ g 1)))` — user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic
    - [HIGH_LENGTH] form=`(do (def g 5) (let [g 99] (+ g 1)))` — user_msg 219 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def g 5) (let [g 99] (+ g 1)))` — sentence with 7 commas reads as AI-output cadence: 'To define g at the top level, shadow it in a let with a different value, and com'

### G3-13: fn body returns last form

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] x x x 99) 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`((fn [x] x x x 99) 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] x x x 99) 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] x x x 99) 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99',), resolution doesn't close the loop)

### G3-14: do form

- examples: 2
- variety @ n=50: 0.99
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'POINTED_AND_SAID_TIC': 1, 'THE_FORM_OVERUSE': 3, 'LOW_GROUNDING': 1, 'PRONOUN_BEFORE_NAME': 1, 'PARALLEL_POSSESSIVE_TIC': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do 1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'Theodoric, with the steady breathing of a long walker, pointed and said: "The ch'
    - [POINTED_AND_SAID_TIC] form=`(do 1 2 3)` — user_msg uses 'X, [appositive], pointed and said:' — overused AI dialogue cadence
    - [THE_FORM_OVERUSE] form=`(do 1 2 3)` — `the form` appears 6 times in user_msg (template tic — vary references)
    - [LOW_GROUNDING] form=`(do 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [THE_FORM_OVERUSE] form=`(do (+ 1 1) (+ 2 2) (+ 3 3))` — `the form` appears 6 times in user_msg (template tic — vary references)
    - [PRONOUN_BEFORE_NAME] form=`(do (+ 1 1) (+ 2 2) (+ 3 3))` — sentence-initial 'He' appears before any named character is introduced

### G3-15: Side-effects in body

- examples: 1
- variety @ n=50: 1.00
- issues: {'DOUBLE_EMO_IN_SENTENCE': 1, 'DOUBLE_EMO_INJECTION': 1, 'HIGH_LENGTH': 1}
    - [DOUBLE_EMO_IN_SENTENCE] form=`(do (println "hi") 42)` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(do (println "hi") 42)` — sentence has 2+ distinct EMO-pool phrases ('with a calm that nothing seeme' + 'as if the prize already sat in') — the character can't earn two emotional registers in the same beat
    - [HIGH_LENGTH] form=`(do (println "hi") 42)` — user_msg 207 words

### G3-18: When to name vs inline

- examples: 2
- variety @ n=50: 1.00
- issues: {'ONLY_SHOOK_HEAD_TIC': 2, 'DOUBLE_EMO_IN_SENTENCE': 2, 'DOUBLE_EMO_INJECTION': 2, 'PRONOUN_BEFORE_NAME': 1}
    - [ONLY_SHOOK_HEAD_TIC] form=`(let [n 5] (* n n n))` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [ONLY_SHOOK_HEAD_TIC] form=`(let [n 5] (* n n n))` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [DOUBLE_EMO_IN_SENTENCE] form=`(* 5 5 5)` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(* 5 5 5)` — sentence has 2+ distinct EMO-pool phrases ('as a young captain walks befor' + 'with no need to hurry the work') — the character can't earn two emotional registers in the same beat
    - [PRONOUN_BEFORE_NAME] form=`(* 5 5 5)` — sentence-initial 'She' appears before any named character is introduced
    - [DOUBLE_EMO_IN_SENTENCE] form=`(* 5 5 5)` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described

## Grade 4

### G4-01: Vector literal

- examples: 3
- variety @ n=50: 1.00
- issues: {'DOUBLE_EMO_INJECTION': 1, 'FORM_LEAK': 2, 'LOW_GROUNDING': 2}
    - [DOUBLE_EMO_INJECTION] form=`[1 2 3]` — sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat
    - [FORM_LEAK] form=`["a" "b"]` — form '["a" "b"]' appears in user_msg of a goal-style subject
    - [LOW_GROUNDING] form=`["a" "b"]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FORM_LEAK] form=`["a" "b"]` — form '["a" "b"]' appears in user_msg of a goal-style subject
    - [LOW_GROUNDING] form=`["a" "b"]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-02: nth — vector access

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_EMO_IN_SENTENCE': 2, 'CLAUSE_STACK_OVERFLOW': 2, 'DOUBLE_EMO_INJECTION': 2}
    - [DOUBLE_EMO_IN_SENTENCE] form=`(nth [10 20 30] 0)` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [CLAUSE_STACK_OVERFLOW] form=`(nth [10 20 30] 0)` — sentence with 6 commas reads as AI-output cadence: 'To get the element at index 0 of a vector containing 10, 20, and 30, produce a f'
    - [DOUBLE_EMO_INJECTION] form=`(nth [10 20 30] 0)` — sentence has 2+ distinct EMO-pool phrases ('without raising her voice at t' + 'with the easy swagger of a qui') — the character can't earn two emotional registers in the same beat
    - [DOUBLE_EMO_IN_SENTENCE] form=`(nth [10 20 30] 2)` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [CLAUSE_STACK_OVERFLOW] form=`(nth [10 20 30] 2)` — sentence with 6 commas reads as AI-output cadence: 'To get the element at index 2 of a vector containing 10, 20, and 30, produce a f'
    - [DOUBLE_EMO_INJECTION] form=`(nth [10 20 30] 2)` — sentence has 2+ distinct EMO-pool phrases ('his nose lifted toward the bri' + 'with eyes always on the path') — the character can't earn two emotional registers in the same beat

### G4-03: conj — append to vector

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'DOUBLE_EMO_INJECTION': 1, 'FORM_LEAK': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(conj [1 2] 3)` — parametric example has hard-coded English numeral 'three items' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_EMO_INJECTION] form=`(conj [1 2] 3)` — sentence has 2+ distinct EMO-pool phrases ('without complaint or hurry' + 'without complaint') — the character can't earn two emotional registers in the same beat
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(conj [1 2] 3)` — parametric example has hard-coded English numeral 'three items' in a story slot — the actual draws may differ from this fixed count
    - [FORM_LEAK] form=`(conj [1 2] 3)` — form '(conj [1 2] 3)' appears in user_msg of a goal-style subject
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(conj [1 2] 3)` — parametric example has hard-coded English numeral 'three items' in a story slot — the actual draws may differ from this fixed count

### G4-04: List literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'DOUBLE_EMO_IN_SENTENCE': 3, 'CLAUSE_STACK_OVERFLOW': 2, 'DOUBLE_EMO_INJECTION': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three items' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_EMO_IN_SENTENCE] form=`'(1 2 3)` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [CLAUSE_STACK_OVERFLOW] form=`'(1 2 3)` — sentence with 6 commas reads as AI-output cadence: 'To create a list containing 1, 2, and 3, produce a form that builds a new basket'
    - [DOUBLE_EMO_INJECTION] form=`'(1 2 3)` — sentence has 2+ distinct EMO-pool phrases ('with the steady walk of a tort' + 'sure of the win, head held hig') — the character can't earn two emotional registers in the same beat
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three items' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three items' in a story slot — the actual draws may differ from this fixed count

### G4-05: cons — prepend to seq

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'PARAMETRIC_LITERAL_NUMERALS': 3, 'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [HIGH_LENGTH] form=`(cons 0 '(1 2 3))` — user_msg 209 words
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(cons 0 '(1 2 3))` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(cons 0 '(1 2 3))` — parametric example has hard-coded English numeral 'four items' in a story slot — the actual draws may differ from this fixed count
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(cons 0 '(1 2 3))` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(cons 0 '(1 2 3))` — parametric example has hard-coded English numeral 'four items' in a story slot — the actual draws may differ from this fixed count
    - [HIGH_LENGTH] form=`(cons 0 '(1 2 3))` — user_msg 207 words

### G4-06: Map literal

- examples: 1
- variety @ n=50: 1.00
- issues: {'DOUBLE_EMO_IN_SENTENCE': 2, 'DOUBLE_EMO_INJECTION': 2}
    - [DOUBLE_EMO_IN_SENTENCE] form=`{:hare 1 :tortoise 2}` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`{:hare 1 :tortoise 2}` — sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat
    - [DOUBLE_EMO_IN_SENTENCE] form=`{:hare 1 :tortoise 2}` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`{:hare 1 :tortoise 2}` — sentence has 2+ distinct EMO-pool phrases ('without lifting her voice or q' + 'as if the race were already wo') — the character can't earn two emotional registers in the same beat

### G4-07: get — map lookup

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'DOUBLE_EMO_INJECTION': 1}
    - [LOW_GROUNDING] form=`(get {:a 1} :missing :default)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_EMO_INJECTION] form=`(get {:a 1} :missing :default)` — sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat

### G4-08: assoc — map update

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'FORM_LEAK': 1}
    - [HIGH_LENGTH] form=`(assoc {:a 1} :a 99)` — user_msg 204 words
    - [FORM_LEAK] form=`(assoc {:a 1} :a 99)` — form '(assoc {:a 1} :a 99)' appears in user_msg of a goal-style subject

### G4-09: dissoc — map remove key

- examples: 1
- variety @ n=50: 1.00
- issues: {'PRONOUN_BEFORE_NAME': 1, 'HIGH_LENGTH': 1, 'FORM_LEAK': 1}
    - [PRONOUN_BEFORE_NAME] form=`(dissoc {:a 1 :b 2} :a)` — sentence-initial 'She' appears before any named character is introduced
    - [HIGH_LENGTH] form=`(dissoc {:a 1 :b 2} :a)` — user_msg 214 words
    - [FORM_LEAK] form=`(dissoc {:a 1 :b 2} :a)` — form '(dissoc {:a 1 :b 2} :a)' appears in user_msg of a goal-style subject

### G4-10: keys and vals

- examples: 1
- variety @ n=50: 1.00
- issues: {'DOUBLE_EMO_IN_SENTENCE': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_EMO_INJECTION': 1}
    - [DOUBLE_EMO_IN_SENTENCE] form=`(count (keys {:a 1 :b 2 :c 3}))` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [CLAUSE_STACK_OVERFLOW] form=`(count (keys {:a 1 :b 2 :c 3}))` — sentence with 6 commas reads as AI-output cadence: 'To count how many keys are in a map binding :a, :b, and :c, produce a form that '
    - [DOUBLE_EMO_INJECTION] form=`(count (keys {:a 1 :b 2 :c 3}))` — sentence has 2+ distinct EMO-pool phrases ('her breath even, her step even' + 'tossing back his ears as if to') — the character can't earn two emotional registers in the same beat

### G4-11: Set literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_EMO_IN_SENTENCE': 2, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_EMO_INJECTION': 2, 'HIGH_LENGTH': 2, 'LOW_GROUNDING': 1}
    - [DOUBLE_EMO_IN_SENTENCE] form=`(count #{1 2 3})` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [CLAUSE_STACK_OVERFLOW] form=`(count #{1 2 3})` — sentence with 6 commas reads as AI-output cadence: 'To count the elements in a set containing 1, 2, and 3, produce a form that build'
    - [DOUBLE_EMO_INJECTION] form=`(count #{1 2 3})` — sentence has 2+ distinct EMO-pool phrases ('with the steady turn of a mill' + 'his chest thrown out before hi') — the character can't earn two emotional registers in the same beat
    - [HIGH_LENGTH] form=`(count #{1 2 3})` — user_msg 201 words
    - [DOUBLE_EMO_IN_SENTENCE] form=`(count #{1 1 1})` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(count #{1 1 1})` — sentence has 2+ distinct EMO-pool phrases ('keeping a steady pace through ' + 'his nose lifted toward the bri') — the character can't earn two emotional registers in the same beat

### G4-12: Set membership

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_EMO_IN_SENTENCE': 2, 'CLAUSE_STACK_OVERFLOW': 2, 'DOUBLE_EMO_INJECTION': 2, 'PARALLEL_POSSESSIVE_TIC': 1, 'FORM_LEAK': 2}
    - [DOUBLE_EMO_IN_SENTENCE] form=`(contains? #{1 2 3} 2)` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [CLAUSE_STACK_OVERFLOW] form=`(contains? #{1 2 3} 2)` — sentence with 6 commas reads as AI-output cadence: 'To check whether 2 is a member of a set containing 1, 2, and 3, produce a form t'
    - [DOUBLE_EMO_INJECTION] form=`(contains? #{1 2 3} 2)` — sentence has 2+ distinct EMO-pool phrases ('with the warm pride that goes ' + 'saying very little') — the character can't earn two emotional registers in the same beat
    - [DOUBLE_EMO_IN_SENTENCE] form=`(contains? #{1 2 3} 2)` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [CLAUSE_STACK_OVERFLOW] form=`(contains? #{1 2 3} 2)` — sentence with 6 commas reads as AI-output cadence: 'To check whether 2 is a member of a set containing 1, 2, and 3, produce a form t'
    - [PARALLEL_POSSESSIVE_TIC] form=`(contains? #{1 2 3} 2)` — user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic

### G4-13: count — universal

- examples: 4
- variety @ n=50: 1.00
- issues: {'NUMERAL_LIST_IN_GOAL': 3, 'DOUBLE_EMO_IN_SENTENCE': 2, 'CLAUSE_STACK_OVERFLOW': 3, 'DOUBLE_EMO_INJECTION': 2}
    - [NUMERAL_LIST_IN_GOAL] form=`(count [1 2 3 4 5])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [DOUBLE_EMO_IN_SENTENCE] form=`(count [1 2 3 4 5])` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [NUMERAL_LIST_IN_GOAL] form=`(count [1 2 3 4 5])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3 4 5])` — sentence with 8 commas reads as AI-output cadence: 'To count the elements in a vector containing 1, 2, 3, 4, and 5, produce a form t'
    - [DOUBLE_EMO_INJECTION] form=`(count [1 2 3 4 5])` — sentence has 2+ distinct EMO-pool phrases ('with the loud bark of a sure w' + 'with steady, careful steps') — the character can't earn two emotional registers in the same beat
    - [NUMERAL_LIST_IN_GOAL] form=`(count [1 2 3 4 5])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing

### G4-14: empty?

- examples: 3
- variety @ n=50: 1.00
- issues: {'DOUBLE_EMO_IN_SENTENCE': 2, 'DOUBLE_EMO_INJECTION': 2, 'FORM_LEAK': 2}
    - [DOUBLE_EMO_IN_SENTENCE] form=`(empty? [])` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(empty? [])` — sentence has 2+ distinct EMO-pool phrases ('his eyes bright with the joy o' + 'with a calm that nothing seeme') — the character can't earn two emotional registers in the same beat
    - [FORM_LEAK] form=`(empty? [])` — form '(empty? [])' appears in user_msg of a goal-style subject
    - [FORM_LEAK] form=`(empty? [1])` — form '(empty? [1])' appears in user_msg of a goal-style subject
    - [DOUBLE_EMO_IN_SENTENCE] form=`(empty? [1])` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(empty? [1])` — sentence has 2+ distinct EMO-pool phrases ('stepping high, as proud creatu' + 'with the steady walk of a tort') — the character can't earn two emotional registers in the same beat

### G4-15: first, rest, last

- examples: 3
- variety @ n=50: 1.00
- issues: {'DOUBLE_EMO_IN_SENTENCE': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_EMO_INJECTION': 1}
    - [DOUBLE_EMO_IN_SENTENCE] form=`(first [10 20 30])` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [CLAUSE_STACK_OVERFLOW] form=`(first [10 20 30])` — sentence with 6 commas reads as AI-output cadence: 'To get the first element of a vector containing 10, 20, and 30, produce a form t'
    - [DOUBLE_EMO_INJECTION] form=`(first [10 20 30])` — sentence has 2+ distinct EMO-pool phrases ('with the still patience of a f' + 'his chest thrown out before hi') — the character can't earn two emotional registers in the same beat

### G4-16: into and conj on collections

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'PRONOUN_BEFORE_NAME': 1, 'FORM_LEAK': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(into [] '(1 2 3))` — parametric example has hard-coded English numeral 'three elements' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(into [] '(1 2 3))` — parametric example has hard-coded English numeral 'three elements' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(into [] '(1 2 3))` — parametric example has hard-coded English numeral 'three elements' in a story slot — the actual draws may differ from this fixed count
    - [PRONOUN_BEFORE_NAME] form=`(into #{} [1 2 2 3])` — sentence-initial 'She' appears before any named character is introduced
    - [FORM_LEAK] form=`(into #{} [1 2 2 3])` — form '(into #{} [1 2 2 3])' appears in user_msg of a goal-style subject

### G4-18: Equality of vectors and lists

- examples: 1
- variety @ n=50: 1.00
- issues: {'DOUBLE_EMO_INJECTION': 2, 'DOUBLE_EMO_IN_SENTENCE': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [DOUBLE_EMO_INJECTION] form=`(= [1 2 3] '(1 2 3))` — sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat
    - [DOUBLE_EMO_IN_SENTENCE] form=`(= [1 2 3] '(1 2 3))` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [CLAUSE_STACK_OVERFLOW] form=`(= [1 2 3] '(1 2 3))` — sentence with 6 commas reads as AI-output cadence: 'To test whether a vector with elements 1, 2, 3 equals a list with the same eleme'
    - [DOUBLE_EMO_INJECTION] form=`(= [1 2 3] '(1 2 3))` — sentence has 2+ distinct EMO-pool phrases ('with the soft patience of runn' + 'with great whoops of laughter') — the character can't earn two emotional registers in the same beat

### G4-19: range and seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'DOUBLE_EMO_IN_SENTENCE': 1, 'DOUBLE_EMO_INJECTION': 1, 'LOW_GROUNDING': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(count (range 5))` — sentence with 5 commas reads as AI-output cadence: 'The milkmaid walked the market road, counting off each milestone: 0, 1, 2, 3, 4'
    - [DOUBLE_EMO_IN_SENTENCE] form=`(count (range 5))` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(count (range 5))` — sentence has 2+ distinct EMO-pool phrases ('without raising her voice at t' + 'sure of the win, head held hig') — the character can't earn two emotional registers in the same beat
    - [LOW_GROUNDING] form=`(count (range 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(count (range 5))` — sentence with 5 commas reads as AI-output cadence: 'The milkmaid walked the market road, counting off each milestone: 0, 1, 2, 3, 4'

### G4-20: Collection vs sequence

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_EMO_IN_SENTENCE': 1, 'DOUBLE_EMO_INJECTION': 1}
    - [DOUBLE_EMO_IN_SENTENCE] form=`(seq [])` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(seq [])` — sentence has 2+ distinct EMO-pool phrases ('with the steady walk of a tort' + 'boasting at every turn') — the character can't earn two emotional registers in the same beat

## Grade 5

### G5-01: if

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOWERCASE_CONCEPT_AFTER_PERIOD': 2, 'LOW_GROUNDING': 2, 'PRONOUN_BEFORE_NAME': 1}
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(if true :a :b)` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    - [LOW_GROUNDING] form=`(if true :a :b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(if false :a :b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PRONOUN_BEFORE_NAME] form=`(if (> 5 3) :a :b)` — sentence-initial 'She' appears before any named character is introduced
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(if (> 5 3) :a :b)` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)

### G5-02: if as expression

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOWERCASE_CONCEPT_AFTER_PERIOD': 3}
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(+ 1 (if true 10 20))` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(+ 1 (if true 10 20))` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(+ 1 (if true 10 20))` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)

### G5-03: when

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'LOWERCASE_CONCEPT_AFTER_PERIOD': 1}
    - [LOW_GROUNDING] form=`(when true :yes)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(when true :yes)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(when false :yes)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(when false :yes)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(when false :yes)` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)

### G5-06: case

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOWERCASE_CONCEPT_AFTER_PERIOD': 3, 'PRONOUN_BEFORE_NAME': 1}
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(case 2 1 :one 2 :two 3 :three :default)` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    - [PRONOUN_BEFORE_NAME] form=`(case 2 1 :one 2 :two 3 :three :default)` — sentence-initial 'She' appears before any named character is introduced
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(case 2 1 :one 2 :two 3 :three :default)` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(case 99 1 :one 2 :two :default)` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)

### G5-07: and / or as control flow

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'DOUBLED_PLACE': 1}
    - [LOW_GROUNDING] form=`(and 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(or nil false :found)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLED_PLACE] form=`(or nil false :found)` — location stutter: 'farm on the farm...'
    - [LOW_GROUNDING] form=`(or nil false :found)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G5-08: not

- examples: 1
- variety @ n=50: 1.00
- issues: {'DOUBLE_EMO_IN_SENTENCE': 1, 'DOUBLE_EMO_INJECTION': 1}
    - [DOUBLE_EMO_IN_SENTENCE] form=`(not (> 1 2))` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(not (> 1 2))` — sentence has 2+ distinct EMO-pool phrases ('as a victor walks before a vic' + 'with no need to hurry the work') — the character can't earn two emotional registers in the same beat

### G5-09: fn as value

- examples: 1
- variety @ n=50: 1.00
- issues: {'PARALLEL_POSSESSIVE_TIC': 1}
    - [PARALLEL_POSSESSIVE_TIC] form=`((fn [f x] (f (f x))) inc 5)` — user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic

### G5-10: map

- examples: 2
- variety @ n=50: 1.00
- issues: {'PRONOUN_BEFORE_NAME': 2, 'STORY_RESOLUTION_NO_DRAWN': 3, 'NUMERAL_LIST_IN_GOAL': 3, 'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [PRONOUN_BEFORE_NAME] form=`(map inc [1 2 3])` — sentence-initial 'She' appears before any named character is introduced
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map #(* % %) [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [NUMERAL_LIST_IN_GOAL] form=`(map #(* % %) [1 2 3 4])` — goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map #(* % %) [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(map #(* % %) [1 2 3 4])` — sentence-initial 'She' appears before any named character is introduced
    - [NUMERAL_LIST_IN_GOAL] form=`(map #(* % %) [1 2 3 4])` — goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing

### G5-11: filter

- examples: 2
- variety @ n=50: 1.00
- issues: {'PARAMETRIC_LITERAL_NUMERALS': 3, 'NARRATIVE_NUMERAL_HARDCODE': 6, 'NUMERAL_LIST_IN_GOAL': 6, 'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 3}
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(filter even? [1 2 3 4])` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(filter even? [1 2 3 4])` — parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    - [NUMERAL_LIST_IN_GOAL] form=`(filter even? [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(filter even? [1 2 3 4])` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(filter even? [1 2 3 4])` — parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    - [NUMERAL_LIST_IN_GOAL] form=`(filter even? [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing

### G5-12: reduce

- examples: 3
- variety @ n=50: 1.00
- issues: {'PRONOUN_BEFORE_NAME': 2, 'NUMERAL_LIST_IN_GOAL': 9, 'CLAUSE_STACK_OVERFLOW': 8, 'HIGH_LENGTH': 3, 'ANSWER_LEAK': 1, 'DOUBLE_EMO_INJECTION': 1, 'PARAMETRIC_LITERAL_NUMERALS': 3, 'LOWERCASE_CONCEPT_AFTER_PERIOD': 2}
    - [PRONOUN_BEFORE_NAME] form=`(reduce + [1 2 3 4])` — sentence-initial 'She' appears before any named character is introduced
    - [NUMERAL_LIST_IN_GOAL] form=`(reduce + [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + [1 2 3 4])` — sentence with 8 commas reads as AI-output cadence: 'To walk the row of pebbles 1, 2, 3, 4 carrying a tally that combines each with +'
    - [HIGH_LENGTH] form=`(reduce + [1 2 3 4])` — user_msg 212 words
    - [ANSWER_LEAK] form=`(reduce + [1 2 3 4])` — answer 10 in narrative
    - [NUMERAL_LIST_IN_GOAL] form=`(reduce + [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing

### G5-13: reduce with init

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'HIGH_LENGTH': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + 100 [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'That is how to\nfold + over the vector containing 1, 2, 3 starting from an initia'
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + 100 [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'To fold + over the vector containing 1, 2, 3 starting from an initial accumulato'
    - [HIGH_LENGTH] form=`(reduce + 100 [1 2 3])` — user_msg 204 words

### G5-14: apply

- examples: 2
- variety @ n=50: 1.00
- issues: {'PARAMETRIC_LITERAL_NUMERALS': 3, 'NARRATIVE_NUMERAL_HARDCODE': 6, 'NUMERAL_LIST_IN_GOAL': 6, 'DOUBLE_EMO_IN_SENTENCE': 2, 'DOUBLE_EMO_INJECTION': 2, 'HIGH_LENGTH': 1, 'ANSWER_LEAK': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(apply + [1 2 3 4])` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply + [1 2 3 4])` — parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    - [NUMERAL_LIST_IN_GOAL] form=`(apply + [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(apply + [1 2 3 4])` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply + [1 2 3 4])` — parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_EMO_IN_SENTENCE] form=`(apply + [1 2 3 4])` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described

### G5-15: comp

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_EMO_IN_SENTENCE': 1, 'DOUBLE_EMO_INJECTION': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`((comp inc inc) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [DOUBLE_EMO_IN_SENTENCE] form=`((comp inc inc) 5)` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`((comp inc inc) 5)` — sentence has 2+ distinct EMO-pool phrases ('with a calm that nothing seeme' + 'as if the prize already sat in') — the character can't earn two emotional registers in the same beat
    - [STORY_RESOLUTION_NO_DRAWN] form=`((comp inc inc) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((comp inc inc) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((comp str inc) 9)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)

### G5-16: partial

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'LOW_GROUNDING': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`((partial + 10) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((partial + 10) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '5'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((partial + 10) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '5'), resolution doesn't close the loop)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(map (partial * 3) [1 2 3])` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(map (partial * 3) [1 2 3])` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [LOW_GROUNDING] form=`(map (partial * 3) [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

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
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'NUMERAL_LIST_IN_GOAL': 3, 'CLAUSE_STACK_OVERFLOW': 2, 'PARAMETRIC_LITERAL_NUMERALS': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(some even? [1 3 5 8 7])` — parametric example has hard-coded English numeral 'five counts' in a story slot — the actual draws may differ from this fixed count
    - [NUMERAL_LIST_IN_GOAL] form=`(some even? [1 3 5 8 7])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(some even? [1 3 5 8 7])` — parametric example has hard-coded English numeral 'five counts' in a story slot — the actual draws may differ from this fixed count
    - [NUMERAL_LIST_IN_GOAL] form=`(some even? [1 3 5 8 7])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(some even? [1 3 5 8 7])` — sentence with 5 commas reads as AI-output cadence: '"To\ncheck if any element in the vector containing 1, 3, 5, 8, and 7 is even, sub'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(some even? [1 3 5 8 7])` — parametric example has hard-coded English numeral 'five counts' in a story slot — the actual draws may differ from this fixed count

### G5-19: every?

- examples: 2
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 2, 'PARAMETRIC_LITERAL_NUMERALS': 6, 'NARRATIVE_NUMERAL_HARDCODE': 6, 'CLAUSE_STACK_OVERFLOW': 2, 'HIGH_LENGTH': 1}
    - [BOOL_LEAK_RESOLUTION] form=`(every? pos? [1 2 3])` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(every? pos? [1 2 3])` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(every? pos? [1 2 3])` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(every? pos? [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To check if all elements in the vector containing 1, 2, and 3 are positive, he c'
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(every? pos? [1 2 3])` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(every? pos? [1 2 3])` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count

### G5-20: take and drop

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'NUMERAL_LIST_IN_GOAL': 6, 'CLAUSE_STACK_OVERFLOW': 5, 'PARALLEL_POSSESSIVE_TIC': 1, 'PRONOUN_BEFORE_NAME': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(take 3 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'five counts' in a story slot — the actual draws may differ from this fixed count
    - [NUMERAL_LIST_IN_GOAL] form=`(take 3 [10 20 30 40 50])` — goal_text contains 6 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(take 3 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'five counts' in a story slot — the actual draws may differ from this fixed count
    - [NUMERAL_LIST_IN_GOAL] form=`(take 3 [10 20 30 40 50])` — goal_text contains 6 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(take 3 [10 20 30 40 50])` — sentence with 5 commas reads as AI-output cadence: 'But she must write it —\nthe farmer\'s form, not the milkmaid\'s guess."\n\nQuestion:'
    - [PARALLEL_POSSESSIVE_TIC] form=`(take 3 [10 20 30 40 50])` — user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic

### G5-21: distinct and sort

- examples: 2
- variety @ n=50: 1.00
- issues: {'PARAMETRIC_LITERAL_NUMERALS': 3, 'NUMERAL_LIST_IN_GOAL': 3, 'PRONOUN_BEFORE_NAME': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(distinct [1 1 2 3 3 4])` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [NUMERAL_LIST_IN_GOAL] form=`(distinct [1 1 2 3 3 4])` — goal_text contains 6 numerals across 5 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(distinct [1 1 2 3 3 4])` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [PRONOUN_BEFORE_NAME] form=`(distinct [1 1 2 3 3 4])` — sentence-initial 'She' appears before any named character is introduced
    - [NUMERAL_LIST_IN_GOAL] form=`(distinct [1 1 2 3 3 4])` — goal_text contains 6 numerals across 5 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(distinct [1 1 2 3 3 4])` — sentence with 6 commas reads as AI-output cadence: '"To\nremove duplicate elements from the vector containing 1, 1, 2, 3, 3, and 4, s'

### G5-22: recur — first taste

- examples: 1
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [HIGH_LENGTH] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — user_msg 205 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)

## Grade 6

### G6-01: Namespace as file

- examples: 3
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 2, 'CONCEPT_AS_VERB': 1, 'ONLY_SHOOK_HEAD_TIC': 1}
    - [LOW_GROUNDING] form=`(name 'foo.bar)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(name 'clojure.string)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [ONLY_SHOOK_HEAD_TIC] form=`(name 'clojure.string)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [LOW_GROUNDING] form=`(symbol? 'tortoise.race)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-02: ns form

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(name 'race.tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name 'race.tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-03: require

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1, 'ONLY_SHOOK_HEAD_TIC': 1}
    - [CONCEPT_AS_VERB] form=`(clojure.string/upper-case "hare")` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [ONLY_SHOOK_HEAD_TIC] form=`(clojure.string/upper-case "hare")` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

### G6-05: Fully qualified names

- examples: 4
- variety @ n=50: 0.99
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CONCEPT_AS_VERB': 2, 'ONLY_SHOOK_HEAD_TIC': 2, 'LOW_GROUNDING': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/reverse "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/reverse "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`(clojure.string/reverse "abc")` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/reverse "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [ONLY_SHOOK_HEAD_TIC] form=`(clojure.string/reverse "abc")` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [LOW_GROUNDING] form=`(namespace :owner/item)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-06: Private defs

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 2, 'ONLY_SHOOK_HEAD_TIC': 2}
    - [CONCEPT_AS_VERB] form=`(:private (meta 'x))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [ONLY_SHOOK_HEAD_TIC] form=`(:private (meta 'x))` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [CONCEPT_AS_VERB] form=`(:private (meta 'x))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [ONLY_SHOOK_HEAD_TIC] form=`(:private (meta 'x))` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

### G6-07: Public vs private API

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1, 'ONLY_SHOOK_HEAD_TIC': 1}
    - [CONCEPT_AS_VERB] form=`(boolean (:private (meta 'public)))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [ONLY_SHOOK_HEAD_TIC] form=`(boolean (:private (meta 'public)))` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

### G6-08: Circular dependencies

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 2, 'ONLY_SHOOK_HEAD_TIC': 4}
    - [CONCEPT_AS_VERB] form=`(clojure.string/upper-case "a")` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [ONLY_SHOOK_HEAD_TIC] form=`(clojure.string/upper-case "a")` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [CONCEPT_AS_VERB] form=`(clojure.string/upper-case "a")` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [ONLY_SHOOK_HEAD_TIC] form=`(clojure.string/upper-case "a")` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [ONLY_SHOOK_HEAD_TIC] form=`(= 'a.b 'a.b)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [ONLY_SHOOK_HEAD_TIC] form=`(= 'a.b 'a.b)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

### G6-09: Loading order

- examples: 2
- variety @ n=50: 1.00
- issues: {'ONLY_SHOOK_HEAD_TIC': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'HIGH_LENGTH': 1, 'LOW_GROUNDING': 1, 'PARALLEL_POSSESSIVE_TIC': 1}
    - [ONLY_SHOOK_HEAD_TIC] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — sentence with 5 commas reads as AI-output cadence: 'To define step1 as 1, then define step2 as step1 plus 1, then return step2, writ'
    - [HIGH_LENGTH] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg 210 words
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PARALLEL_POSSESSIVE_TIC] form=`(let [a 1 b (+ a 1)] (+ a b))` — user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a 1 b (+ a 1)] (+ a b))` — sentence with 5 commas reads as AI-output cadence: 'To bind a to 1, bind b to a plus 1, then return the sum of a and b, write a form'

### G6-10: Leiningen and deps.edn

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'HEDGING_NEAR_FORM': 1}
    - [LOW_GROUNDING] form=`(:deps {:deps {:a 1 :b 2}})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(:deps {:deps {:a 1 :b 2}})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(:deps {:deps {:a 1 :b 2}})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(:deps {:deps {:a 1 :b 2}})` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value

### G6-11: Classpath

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'HEDGING_NEAR_FORM': 1, 'DOUBLE_EMO_INJECTION': 1}
    - [LOW_GROUNDING] form=`(clojure.string/split "src:test" #":")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(clojure.string/split "src:test" #":")` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [LOW_GROUNDING] form=`(count ["src" "test" "resources"])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_EMO_INJECTION] form=`(count ["src" "test" "resources"])` — sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat

### G6-12: Multiple files in one project

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(count ['race.tortoise 'race.hare 'race.shared])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(map name ['race.tortoise 'race.hare])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-14: Import for host classes

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1, 'LOW_GROUNDING': 1}
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
- issues: {'ONLY_SHOOK_HEAD_TIC': 1}
    - [ONLY_SHOOK_HEAD_TIC] form=`(contains? #{'clojure.string} 'clojure.string)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

## Grade 7

### G7-01: throw

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'LOW_GROUNDING': 2, 'REPL_TRIPLE_VOICE': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "bad")) (catch Exception e` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1', 'bad'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(try (throw (Exception. "bad")) (catch Exception e` — sentence with 5 commas reads as AI-output cadence: 'Theodelinda, with eyes always on the path, said, "To throw an Exception and catc'
    - [LOW_GROUNDING] form=`(try (throw (Exception. "bad")) (catch Exception e` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "bad")) (catch Exception e` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1', 'bad'), resolution doesn't close the loop)
    - [REPL_TRIPLE_VOICE] form=`(try (throw (Exception. "bad")) (catch Exception e` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [LOW_GROUNDING] form=`(try (throw (Exception. "bad")) (catch Exception e` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-02: try / catch

- examples: 2
- variety @ n=50: 1.00
- issues: {'PRONOUN_BEFORE_NAME': 3, 'CLAUSE_STACK_OVERFLOW': 2, 'DOUBLE_EMO_INJECTION': 1, 'LOW_GROUNDING': 1}
    - [PRONOUN_BEFORE_NAME] form=`(try (/ 1 0) (catch Exception e -1))` — sentence-initial 'She' appears before any named character is introduced
    - [CLAUSE_STACK_OVERFLOW] form=`(try (/ 1 0) (catch Exception e -1))` — sentence with 6 commas reads as AI-output cadence: 'Edmund, stepping deliberately, one foot before the next, said, "To attempt to di'
    - [DOUBLE_EMO_INJECTION] form=`(try (/ 1 0) (catch Exception e -1))` — sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat
    - [PRONOUN_BEFORE_NAME] form=`(try 42 (catch Exception e :caught))` — sentence-initial 'She' appears before any named character is introduced
    - [CLAUSE_STACK_OVERFLOW] form=`(try 42 (catch Exception e :caught))` — sentence with 6 commas reads as AI-output cadence: 'Nathaniel, her breath even, her step even, her thought even, said, "To evaluate '
    - [LOW_GROUNDING] form=`(try 42 (catch Exception e :caught))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-03: try / finally

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'REPL_TRIPLE_VOICE': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(try 7 (finally (prn :cleanup)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [REPL_TRIPLE_VOICE] form=`(try 7 (finally (prn :cleanup)))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [CLAUSE_STACK_OVERFLOW] form=`(try 7 (finally (prn :cleanup)))` — sentence with 7 commas reads as AI-output cadence: 'Brunhilda, her breath even, her step even, her thought even, said, "To evaluate '
    - [LOW_GROUNDING] form=`(try (try (/ 1 0) (finally (prn :ran))) (catch Exc` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [REPL_TRIPLE_VOICE] form=`(try (try (/ 1 0) (finally (prn :ran))) (catch Exc` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [LOW_GROUNDING] form=`(try (try (/ 1 0) (finally (prn :ran))) (catch Exc` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-04: ex-info

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 1, 'REPL_TRIPLE_VOICE': 2}
    - [LOW_GROUNDING] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', 'bad'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', 'bad'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — sentence with 5 commas reads as AI-output cadence: 'Hieronymus, neither restless nor weary, only steady, said, "To throw an ex-info '
    - [LOW_GROUNDING] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', 'bad'), resolution doesn't close the loop)

### G7-05: nil punning

- examples: 4
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 3, 'LOW_GROUNDING': 5, 'REPL_TRIPLE_VOICE': 2, 'LOWERCASE_CONCEPT_AFTER_PERIOD': 1}
    - [BOOL_LEAK_RESOLUTION] form=`(some? nil)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(some? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [BOOL_LEAK_RESOLUTION] form=`(some? nil)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(some? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [BOOL_LEAK_RESOLUTION] form=`(some? 0)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(some? 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-06: pre and post conditions

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3, 'PRONOUN_BEFORE_NAME': 2, 'LOWERCASE_CONCEPT_AFTER_PERIOD': 2}
    - [LOW_GROUNDING] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', ':pre'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', ':pre'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', ':pre'), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — sentence-initial 'She' appears before any named character is introduced

### G7-07: assert

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'REPL_TRIPLE_VOICE': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLED_PLACE': 1}
    - [LOW_GROUNDING] form=`(do (assert (= 1 1)) 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [REPL_TRIPLE_VOICE] form=`(do (assert (= 1 1)) 1)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [LOW_GROUNDING] form=`(do (assert (= 1 1)) 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [REPL_TRIPLE_VOICE] form=`(do (assert (= 1 1)) 1)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [LOW_GROUNDING] form=`(do (assert (= 1 1)) 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [REPL_TRIPLE_VOICE] form=`(do (assert (= 1 1)) 1)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G7-09: tap>

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'PRONOUN_BEFORE_NAME': 2}
    - [LOW_GROUNDING] form=`(tap> :hello)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(tap> 42)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PRONOUN_BEFORE_NAME] form=`(tap> 42)` — sentence-initial 'She' appears before any named character is introduced
    - [PRONOUN_BEFORE_NAME] form=`(tap> 42)` — sentence-initial 'She' appears before any named character is introduced

### G7-10: doc and source

- examples: 1
- variety @ n=50: 1.00
- issues: {'PRONOUN_BEFORE_NAME': 1, 'ANSWER_LEAK_STRING': 1}
    - [PRONOUN_BEFORE_NAME] form=`(:doc (meta '^{:doc "adds two"} plus))` — sentence-initial 'She' appears before any named character is introduced
    - [ANSWER_LEAK_STRING] form=`(:doc (meta '^{:doc "adds two"} plus))` — answer string 'adds two' appears in user_msg

### G7-11: Reading stack traces

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'STORY_RESOLUTION_NO_DRAWN': 6, 'REPL_TRIPLE_VOICE': 2, 'CLAUSE_STACK_OVERFLOW': 2, 'PARALLEL_POSSESSIVE_TIC': 1, 'DOUBLE_EMO_INJECTION': 1}
    - [LOW_GROUNDING] form=`(try (throw (Exception. "oops")) (catch Exception ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)
    - [REPL_TRIPLE_VOICE] form=`(try (throw (Exception. "oops")) (catch Exception ` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [LOW_GROUNDING] form=`(try (throw (Exception. "oops")) (catch Exception ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)
    - [REPL_TRIPLE_VOICE] form=`(try (throw (Exception. "oops")) (catch Exception ` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G7-12: slurp and spit

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(count "hare
tortoise
")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count "hare
tortoise
")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count "hare
tortoise
")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.string/split "a\nb\nc" #"\n")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "a\nb\nc" #"\n")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc', '\\n'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "a\nb\nc" #"\n")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc', '\\n'), resolution doesn't close the loop)

### G7-13: line-seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first (clojure.string/split-lines "morning-delive` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('morning-delivery\\nevening-delivery',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first (clojure.string/split-lines "morning-delive` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('morning-delivery\\nevening-delivery',), resolution doesn't close the loop)

### G7-14: with-open

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(with-out-str (println "hare"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (println "hare"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-15: *in* and *out*

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(with-out-str (print "x"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (print "x"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (println))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (println))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (println))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-16: edn read

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "{:a 1}")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "{:a 1}")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "{:a 1}")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "[:hare :tortoise]")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-17: JSON roundtrip

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-18: Shell command

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(count (:args {:cmd "echo" :args ["hello" "world"]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 8

### G8-01: Why polymorphism

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'PRONOUN_BEFORE_NAME': 1}
    - [LOW_GROUNDING] form=`(let [speak (fn [k] (cond (= k :hare) "swift" (= k` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [speak (fn [k] (cond (= k :hare) "swift" (= k` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PRONOUN_BEFORE_NAME] form=`(let [speak (fn [k] (cond (= k :hare) "swift" (= k` — sentence-initial 'She' appears before any named character is introduced

### G8-02: deftype introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 1, 'LOW_GROUNDING': 2, 'PRONOUN_BEFORE_NAME': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_EMO_INJECTION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — user_msg 204 words
    - [LOW_GROUNDING] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)

### G8-03: defrecord introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'PRONOUN_BEFORE_NAME': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [PRONOUN_BEFORE_NAME] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — sentence-initial 'She' appears before any named character is introduced
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — sentence with 7 commas reads as AI-output cadence: 'So she, her breath even, her step even, her thought even, said, "To define a Run'

### G8-04: Protocol definition

- examples: 2
- variety @ n=50: 0.99
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'LOW_GROUNDING': 4, 'PRONOUN_BEFORE_NAME': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — sentence with 5 commas reads as AI-output cadence: 'Hieronymus, neither restless nor weary, only steady,\nexplained to Maeve: "To fou'
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Greet (hail [this])) (some? Greet` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Greet (hail [this])) (some? Greet` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PRONOUN_BEFORE_NAME] form=`(do (defprotocol Greet (hail [this])) (some? Greet` — sentence-initial 'He' appears before any named character is introduced
    - [LOW_GROUNDING] form=`(do (defprotocol Greet (hail [this])) (some? Greet` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-05: Protocol extension

- examples: 2
- variety @ n=50: 0.98
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CONCEPT_AS_VERB': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('swift', 'hare'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('swift', 'hare'), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('swift', 'hare'), resolution doesn't close the loop)

### G8-06: Protocol method dispatch

- examples: 2
- variety @ n=50: 0.98
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 2, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, extend it to both String and Long t'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, extend it to both String and Long t'
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-07: Record implementing protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CONCEPT_AS_VERB': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (defrecord M` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord M` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':swift', 'Pip'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (defrecord M` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord M` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':swift', 'Pip'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (defrecord M` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord M` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':swift', 'Pip'), resolution doesn't close the loop)

### G8-08: Multimethod defmulti

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 5 commas reads as AI-output cadence: 'To build a sorting-table named pace that reads the :species stamp, add a :hare a'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti tag :kind) (defmethod tag :stone [_]` — sentence with 5 commas reads as AI-output cadence: 'To define multimethod tag dispatching on :kind, add a :stone arm, then call tag '

### G8-09: Multimethod defmethod

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'PARALLEL_POSSESSIVE_TIC': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(do (defmulti pace :species) (defmethod pace :hare` — user_msg 205 words
    - [PARALLEL_POSSESSIVE_TIC] form=`(do (defmulti pace :species) (defmethod pace :hare` — user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 5 commas reads as AI-output cadence: 'Without a stamp, the table cannot route, and the milk cannot flow."\n\nWrite a Clo'

### G8-10: Multimethod vs protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'LOW_GROUNDING': 1}
    - [HIGH_LENGTH] form=`(do (defmulti show identity) (defmethod show :rabb` — user_msg 216 words
    - [HIGH_LENGTH] form=`(do (defprotocol Show (show [this])) (extend-proto` — user_msg 204 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Show (show [this])) (extend-proto` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('str-', 'hare'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Show (show [this])) (extend-proto` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Show with method show, extend it to String type, then call '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Show (show [this])) (extend-proto` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('str-', 'hare'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(do (defprotocol Show (show [this])) (extend-proto` — user_msg 223 words

### G8-11: Protocol vs Java interface

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CONCEPT_AS_VERB': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol IPace (run [this])) (extend-proto` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol IPace (run [this])) (extend-proto` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':ran', 'hare'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(do (defprotocol IPace (run [this])) (extend-proto` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol IPace (run [this])) (extend-proto` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':ran', 'hare'), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`(do (defprotocol IPace (run [this])) (extend-proto` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol IPace (run [this])) (extend-proto` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':ran', 'hare'), resolution doesn't close the loop)

### G8-12: extend-type on built-in types

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'HIGH_LENGTH': 1, 'LOW_GROUNDING': 1, 'PRONOUN_BEFORE_NAME': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-type` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', ':number-pace'), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(do (defprotocol Pace (speed [this])) (extend-type` — user_msg 217 words
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-type` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-type` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', ':number-pace'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-type` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', ':number-pace'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-type` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':string-pace', 'hare'), resolution doesn't close the loop)

### G8-13: this-style vs fn-style

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 4, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Named (name-of [this])) (defrecor` — sentence with 5 commas reads as AI-output cadence: 'Onorata, with the still patience of a fisher,\nexplained to Marina: "To define a '
    - [LOW_GROUNDING] form=`(do (defprotocol Tagged (tag-of [this])) (defrecor` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Tagged (tag-of [this])) (defrecor` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-14: Protocols don't inherit

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 2, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — sentence with 6 commas reads as AI-output cadence: 'Theodoric, untroubled by what others thought,\nexplained to Pernille: "To define '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — sentence with 6 commas reads as AI-output cadence: 'To define two protocols A and B, each with a method, extend both to String type '
    - [LOW_GROUNDING] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)

### G8-15: derive and isa? — multimethod hierarchy

- examples: 3
- variety @ n=50: 0.99
- issues: {'DOUBLE_EMO_INJECTION': 1, 'LOW_GROUNDING': 2}
    - [DOUBLE_EMO_INJECTION] form=`(isa? java.lang.Long java.lang.Number)` — sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat
    - [LOW_GROUNDING] form=`(isa? java.lang.String java.lang.Number)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(isa? java.lang.String java.lang.Number)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-16: Abstract design with protocols

- examples: 2
- variety @ n=50: 0.98
- issues: {'LOW_GROUNDING': 1, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 4, 'CONCEPT_AS_VERB': 4}
    - [LOW_GROUNDING] form=`(do (defprotocol Move (step [this])) (defrecord Mi` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Move (step [this])) (defrecord Mi` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':leap', ':plod'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Move (step [this])) (defrecord Mi` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':leap', ':plod'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Move (step [this])) (defrecord Mi` — sentence with 5 commas reads as AI-output cadence: 'Ulvilda, with the slow grace of a creature unhurried,\nexplained to Genevieve: "T'
    - [CONCEPT_AS_VERB] form=`(do (defprotocol Move (step [this])) (defrecord Mi` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Move (step [this])) (defrecord Mi` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':leap', ':plod'), resolution doesn't close the loop)

## Grade 9

### G9-01: Immutability as default — review

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4, 'DOUBLE_EMO_INJECTION': 3, 'DOUBLE_EMO_IN_SENTENCE': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(let [m {:a 1}] (assoc m :b 2) m)` — sentence with 5 commas reads as AI-output cadence: 'To bind a map m, call assoc to add :b 6 to a new map, then return the unchanged '
    - [DOUBLE_EMO_INJECTION] form=`(let [m {:a 1}] (assoc m :b 2) m)` — sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat
    - [DOUBLE_EMO_IN_SENTENCE] form=`(let [m {:a 1}] (assoc m :b 2) m)` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [CLAUSE_STACK_OVERFLOW] form=`(let [m {:a 1}] (assoc m :b 2) m)` — sentence with 8 commas reads as AI-output cadence: 'To bind a map m, call assoc to add :b 5 to a new map, then return the unchanged '
    - [DOUBLE_EMO_INJECTION] form=`(let [m {:a 1}] (assoc m :b 2) m)` — sentence has 2+ distinct EMO-pool phrases ('as a young captain walks befor' + 'neither restless nor weary, on') — the character can't earn two emotional registers in the same beat
    - [DOUBLE_EMO_IN_SENTENCE] form=`(let [v [1 2 3]] (conj v 4) v)` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described

### G9-02: Why state at all

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 5, 'HIGH_LENGTH': 1, 'SMALL_INT_LEAK': 1, 'LOW_GROUNDING': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — sentence with 6 commas reads as AI-output cadence: "She said untroubled by what others thought, the chalk's edge cool against her\nfi"
    - [HIGH_LENGTH] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — user_msg 206 words
    - [SMALL_INT_LEAK] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — small-int answer 1 leaks via resolution-slot phrasing
    - [LOW_GROUNDING] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — sentence with 5 commas reads as AI-output cadence: 'To construct an atom holding 0 as counter, atomically swap it by applying inc, a'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def progress (atom :idle)) (reset! progress :` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':idle', ':running'), resolution doesn't close the loop)

### G9-03: Atom introduction

- examples: 3
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 9, 'CLAUSE_STACK_OVERFLOW': 4, 'DOUBLE_EMO_INJECTION': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 5 commas reads as AI-output cadence: '"Each farmer submits a form for atom, swap, and deref — a form\nthat reads the cu'
    - [DOUBLE_EMO_INJECTION] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 5 commas reads as AI-output cadence: 'But to change it, atom, swap, and deref happens in\none breath: read the old numb'

### G9-04: Atom CAS semantics

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 6, 'LOW_GROUNDING': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — concept_phrase 'atom, CAS, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — sentence with 6 commas reads as AI-output cadence: "She said with the steady turn of a millwheel, the chalk's edge cool against her\n"
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — concept_phrase 'atom, CAS, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — sentence with 5 commas reads as AI-output cadence: 'But to change it, atom, CAS, deref happens in\none breath: read the old number, a'
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — concept_phrase 'atom, CAS, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose

### G9-05: Watch on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 3}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':w',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — sentence with 5 commas reads as AI-output cadence: 'To construct an atom a, construct a log atom, add a watch to a that conjoins new'
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':w',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — sentence with 5 commas reads as AI-output cadence: 'To construct an atom a, construct a log atom, add a watch to a that conjoins new'

### G9-07: Ref introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 5, 'STORY_RESOLUTION_NO_DRAWN': 3, 'PRONOUN_BEFORE_NAME': 1}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — concept_phrase 'ref, dosync, alter, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 6 commas reads as AI-output cadence: '"Each farmer submits a form for ref, dosync, alter, deref — a form\nthat reads th'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — concept_phrase 'ref, dosync, alter, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 6 commas reads as AI-output cadence: '"Each farmer submits a form for ref, dosync, alter, deref — a form\nthat reads th'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — concept_phrase 'ref, dosync, alter, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 6 commas reads as AI-output cadence: '"Each farmer submits a form for ref, dosync, alter, deref — a form\nthat reads th'

### G9-08: dosync and alter

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 5, 'PRONOUN_BEFORE_NAME': 1, 'CONCEPT_PHRASE_COMMA_LIST': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — sentence with 5 commas reads as AI-output cadence: "That is\nthe slate's promise: construct refs a and b, perform a coordinated trans"
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — sentence with 5 commas reads as AI-output cadence: 'The count will construct refs a and b, perform a coordinated transaction that al'
    - [PRONOUN_BEFORE_NAME] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — sentence-initial 'She' appears before any named character is introduced
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — concept_phrase 'ref, dosync, alter, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — sentence with 5 commas reads as AI-output cadence: 'This form reads the slate, applies ref, dosync, alter, deref, and writes the res'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — concept_phrase 'ref, dosync, alter, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose

### G9-09: Ref vs atom

- examples: 2
- variety @ n=50: 1.00
- issues: {'PRONOUN_BEFORE_NAME': 1, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 5, 'PARALLEL_POSSESSIVE_TIC': 1}
    - [PRONOUN_BEFORE_NAME] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence-initial 'She' appears before any named character is introduced
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 5 commas reads as AI-output cadence: 'The count will construct an atom holding 0, atomically swap it by applying inc, '
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def a (atom 0)) (swap! a inc) @a)` — concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 5 commas reads as AI-output cadence: 'But to change it, atom, swap, deref happens in\none breath: read the old number, '
    - [PARALLEL_POSSESSIVE_TIC] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic

### G9-10: Agent introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'HIGH_LENGTH': 2, 'LOW_GROUNDING': 1, 'CLAUSE_STACK_OVERFLOW': 4}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [HIGH_LENGTH] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg 213 words
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 7 commas reads as AI-output cadence: 'To construct an agent holding 0, asynchronously send inc to it, await its comple'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose

### G9-11: send and send-off

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 3, 'PRONOUN_BEFORE_NAME': 1, 'LOW_GROUNDING': 1, 'DOUBLE_EMO_INJECTION': 1}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 5 commas reads as AI-output cadence: '"To construct an agent holding 0, use send to asynchronously apply inc, await it'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 5 commas reads as AI-output cadence: '"To construct an agent holding 0, use send to asynchronously apply inc, await it'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — concept_phrase 'agent, send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [PRONOUN_BEFORE_NAME] form=`(do (def ag (agent 0)) (send-off ag inc) (await ag` — sentence-initial 'She' appears before any named character is introduced

### G9-12: await — synchronizing on agents

- examples: 1
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 3, 'CLAUSE_STACK_OVERFLOW': 3, 'HIGH_LENGTH': 1, 'LOW_GROUNDING': 1}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — concept_phrase 'agent, double send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 7 commas reads as AI-output cadence: 'To construct an agent holding 0, asynchronously send inc twice, synchronize with'
    - [HIGH_LENGTH] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — user_msg 201 words
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — concept_phrase 'agent, double send, await, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 7 commas reads as AI-output cadence: 'To construct an agent holding 0, asynchronously send inc twice, synchronize with'

### G9-13: future introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_PHRASE_COMMA_LIST] form=`@(future (+ 1 2))` — concept_phrase 'future, add, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CONCEPT_PHRASE_COMMA_LIST] form=`@(future (+ 1 2))` — concept_phrase 'future, add, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CONCEPT_PHRASE_COMMA_LIST] form=`@(future (+ 1 2))` — concept_phrase 'future, add, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [STORY_RESOLUTION_NO_DRAWN] form=`@(future (* 6 7))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '7'), resolution doesn't close the loop)
    - [CONCEPT_PHRASE_COMMA_LIST] form=`@(future (* 6 7))` — concept_phrase 'future, multiply, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose

### G9-14: deref @ shorthand

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 7)) @a)` — sentence with 6 commas reads as AI-output cadence: "He said her breath even, her step even, her thought even, the chalk's edge cool "
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) (deref a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) (deref a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)

### G9-15: promise — deliver and deref

- examples: 2
- variety @ n=50: 0.99
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 4, 'LOW_GROUNDING': 1, 'DOUBLE_EMO_INJECTION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def p (promise)) (deliver p :done) @p)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':done',), resolution doesn't close the loop)
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def p (promise)) (deliver p :done) @p)` — concept_phrase 'promise, deliver, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def p (promise)) (deliver p :done) @p)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':done',), resolution doesn't close the loop)
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def p (promise)) (deliver p :done) @p)` — concept_phrase 'promise, deliver, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def p (promise)) (deliver p :done) @p)` — sentence with 5 commas reads as AI-output cadence: 'To construct a promise, deliver a completion keyword to it, and dereference to g'
    - [LOW_GROUNDING] form=`(do (def p (promise)) (deliver p :done) @p)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-16: volatile — when STM is too heavy

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 6, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — concept_phrase 'volatile, vswap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — sentence with 5 commas reads as AI-output cadence: '"Each farmer submits a form for volatile, vswap, deref — a form\nthat reads the c'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — concept_phrase 'volatile, vswap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — sentence with 5 commas reads as AI-output cadence: 'But to change it, volatile, vswap, deref happens in\none breath: read the old num'
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — concept_phrase 'volatile, vswap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — sentence with 5 commas reads as AI-output cadence: 'The count will construct a volatile holding 0, perform a non-transactional swap '

### G9-17: binding — thread-local

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 5}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — concept_phrase 'dynamic var, binding, read' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — sentence with 5 commas reads as AI-output cadence: 'But to change it, dynamic var, binding, read happens in\none breath: read the old'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — concept_phrase 'dynamic var, binding, read' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — sentence with 5 commas reads as AI-output cadence: 'But to change it, dynamic var, binding, read happens in\none breath: read the old'

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 0.99
- issues: {'CONCEPT_PHRASE_COMMA_LIST': 6, 'CLAUSE_STACK_OVERFLOW': 4, 'GENERIC_RESOLUTION_TAIL': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1, 'DOUBLE_PREP': 1, 'LOW_GROUNDING': 1}
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — concept_phrase 'lock, locking, arithmetic' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — concept_phrase 'lock, locking, arithmetic' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — sentence with 5 commas reads as AI-output cadence: 'But to change it, lock, locking, arithmetic happens in\none breath: read the old '
    - [CONCEPT_PHRASE_COMMA_LIST] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — concept_phrase 'lock, locking, arithmetic' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — sentence with 5 commas reads as AI-output cadence: 'But to change it, lock, locking, arithmetic happens in\none breath: read the old '
    - [GENERIC_RESOLUTION_TAIL] form=`(do (def lock (Object.)) (locking lock 42))` — resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop

## Grade 10

### G10-01: quote, unquote, unquote-splice

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'HIGH_LENGTH': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`'(1 2 3)` — user_msg 204 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 5] `(a ~x b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 5] `(a ~x b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(let [x 5] `(a ~x b))` — user_msg 207 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 5] `(a ~x b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)

### G10-02: syntax-quote

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'HIGH_LENGTH': 1, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 10] `(+ ~x ~x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10',), resolution doesn't close the loop)
    - [HIGH_LENGTH] form=`(let [x 10] `(+ ~x ~x))` — user_msg 205 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 10] `(+ ~x ~x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 10] `(+ ~x ~x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(let [xs [1 2 3]] `(list ~@xs))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-03: defmacro introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_EMO_INJECTION': 2, 'DOUBLE_EMO_IN_SENTENCE': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — sentence with 5 commas reads as AI-output cadence: 'Iustinian, stepping deliberately, one foot before the next, replied, "Each of yo'
    - [DOUBLE_EMO_INJECTION] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat
    - [DOUBLE_EMO_IN_SENTENCE] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — sentence has 2+ distinct EMO-pool phrases ('with the small pride of small ' + 'her breath even, her step even') — the character can't earn two emotional registers in the same beat

### G10-04: Macro expansion rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_EMO_IN_SENTENCE': 2, 'DOUBLE_EMO_INJECTION': 2, 'PARAGRAPH_FRAGMENTATION': 1}
    - [DOUBLE_EMO_IN_SENTENCE] form=`(macroexpand-1 '(when true 1))` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(macroexpand-1 '(when true 1))` — sentence has 2+ distinct EMO-pool phrases ('tossing back his ears as if to' + 'with the steady turn of a mill') — the character can't earn two emotional registers in the same beat
    - [DOUBLE_EMO_IN_SENTENCE] form=`(macroexpand-1 '(when true 1))` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(macroexpand-1 '(when true 1))` — sentence has 2+ distinct EMO-pool phrases ('with the broad pride of a long' + 'neither restless nor weary, on') — the character can't earn two emotional registers in the same beat
    - [PARAGRAPH_FRAGMENTATION] form=`(macroexpand-1 '(when true 1))` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G10-05: macroexpand

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 2, 'DOUBLE_EMO_IN_SENTENCE': 1, 'DOUBLE_EMO_INJECTION': 1}
    - [LOW_GROUNDING] form=`(macroexpand '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(macroexpand '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_EMO_IN_SENTENCE] form=`(macroexpand '(-> 1 inc inc))` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(macroexpand '(-> 1 inc inc))` — sentence has 2+ distinct EMO-pool phrases ('untroubled by what others thou' + 'sure of the win, head held hig') — the character can't earn two emotional registers in the same beat

### G10-06: when and when-not as macros

- examples: 3
- variety @ n=50: 1.00
- issues: {'DOUBLE_EMO_IN_SENTENCE': 2, 'DOUBLE_EMO_INJECTION': 2, 'HIGH_LENGTH': 2, 'LOW_GROUNDING': 2, 'REPL_TRIPLE_VOICE': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'PARALLEL_POSSESSIVE_TIC': 1}
    - [DOUBLE_EMO_IN_SENTENCE] form=`(when true 1 2 3)` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(when true 1 2 3)` — sentence has 2+ distinct EMO-pool phrases ('as if the race were already wo' + 'saying very little') — the character can't earn two emotional registers in the same beat
    - [HIGH_LENGTH] form=`(when true 1 2 3)` — user_msg 215 words
    - [HIGH_LENGTH] form=`(when true 1 2 3)` — user_msg 213 words
    - [LOW_GROUNDING] form=`(when false 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [REPL_TRIPLE_VOICE] form=`(when false 1 2 3)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 2, 'DOUBLE_EMO_IN_SENTENCE': 1, 'DOUBLE_EMO_INJECTION': 1, 'HIGH_LENGTH': 1, 'DOUBLED_PLACE': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'LOW_GROUNDING': 1}
    - [ANSWER_LEAK] form=`(-> 5 inc inc inc)` — answer 8 in narrative
    - [DOUBLE_EMO_IN_SENTENCE] form=`(-> 5 inc inc inc)` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(-> 5 inc inc inc)` — sentence has 2+ distinct EMO-pool phrases ('tossing back his ears as if to' + 'with the steady turn of a mill') — the character can't earn two emotional registers in the same beat
    - [HIGH_LENGTH] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — user_msg 212 words
    - [ANSWER_LEAK] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — answer 8 in narrative
    - [DOUBLED_PLACE] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — location stutter: 'farm on the farm...'

### G10-08: Macro vs fn

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 3, 'DOUBLE_EMO_IN_SENTENCE': 3, 'DOUBLE_EMO_INJECTION': 3, 'ANSWER_LEAK': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [CONCEPT_AS_VERB] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [DOUBLE_EMO_IN_SENTENCE] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — sentence has 2+ distinct EMO-pool phrases ('as a victor walks before a vic' + 'with no need to hurry the work') — the character can't earn two emotional registers in the same beat
    - [ANSWER_LEAK] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — answer 7 in narrative
    - [CONCEPT_AS_VERB] form=`(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)

### G10-09: Hygiene and gensym

- examples: 2
- variety @ n=50: 1.00
- issues: {'GENERIC_RESOLUTION_TAIL': 3, 'DOUBLE_EMO_IN_SENTENCE': 2, 'PARALLEL_POSSESSIVE_TIC': 1, 'DOUBLE_EMO_INJECTION': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [GENERIC_RESOLUTION_TAIL] form=`(symbol? (gensym))` — resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    - [GENERIC_RESOLUTION_TAIL] form=`(symbol? (gensym))` — resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    - [DOUBLE_EMO_IN_SENTENCE] form=`(symbol? (gensym))` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [PARALLEL_POSSESSIVE_TIC] form=`(symbol? (gensym))` — user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic
    - [DOUBLE_EMO_INJECTION] form=`(symbol? (gensym))` — sentence has 2+ distinct EMO-pool phrases ('her face quiet, her hands quie' + 'his nose lifted toward the bri') — the character can't earn two emotional registers in the same beat
    - [GENERIC_RESOLUTION_TAIL] form=`(symbol? (gensym))` — resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop

### G10-10: Anaphoric macros are confusing

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_EMO_IN_SENTENCE': 2, 'DOUBLE_EMO_INJECTION': 2, 'HIGH_LENGTH': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [DOUBLE_EMO_IN_SENTENCE] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — sentence has 2+ distinct EMO-pool phrases ('with a laugh that carried over' + 'with the steady turn of a mill') — the character can't earn two emotional registers in the same beat
    - [HIGH_LENGTH] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — user_msg 209 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)

### G10-11: Reader macros overview

- examples: 3
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'THE_FORM_OVERUSE': 2, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 2, 'CLAUSE_STACK_OVERFLOW': 1, 'POINTED_AND_SAID_TIC': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [THE_FORM_OVERUSE] form=`'(1 2 3)` — `the form` appears 7 times in user_msg (template tic — vary references)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three numbers' in a story slot — the actual draws may differ from this fixed count
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`'(1 2 3)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(* % %) 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)

### G10-12: Tagged literals

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 3, 'POINTED_AND_SAID_TIC': 3, 'LOW_GROUNDING': 1, 'PRONOUN_BEFORE_NAME': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inst? #inst "2024-01-01")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('2024', '-01', '-01'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(inst? #inst "2024-01-01")` — sentence with 5 commas reads as AI-output cadence: 'Theophilus, without lifting her voice or quickening her step, pointed and said: '
    - [POINTED_AND_SAID_TIC] form=`(inst? #inst "2024-01-01")` — user_msg uses 'X, [appositive], pointed and said:' — overused AI dialogue cadence
    - [LOW_GROUNDING] form=`(inst? #inst "2024-01-01")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inst? #inst "2024-01-01")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('2024', '-01', '-01'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inst? #inst "2024-01-01")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('2024', '-01', '-01'), resolution doesn't close the loop)

### G10-13: Data readers and EDN extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 1, 'POINTED_AND_SAID_TIC': 1, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "42")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', '42'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "42")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', '42'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "42")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', '42'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(clojure.edn/read-string "42")` — sentence with 5 commas reads as AI-output cadence: 'Onorata, with the still patience of a fisher, pointed and said: "The chalk marks'
    - [POINTED_AND_SAID_TIC] form=`(clojure.edn/read-string "42")` — user_msg uses 'X, [appositive], pointed and said:' — overused AI dialogue cadence
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "[:a :b :c]")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-14: eval (the function)

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_EMO_IN_SENTENCE': 3, 'DOUBLE_EMO_INJECTION': 3, 'CONCEPT_AS_VERB': 2, 'CLAUSE_STACK_OVERFLOW': 1, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval '(+ 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [DOUBLE_EMO_IN_SENTENCE] form=`(eval '(+ 1 2 3))` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(eval '(+ 1 2 3))` — sentence has 2+ distinct EMO-pool phrases ('as if the prize already sat in' + 'untroubled by what others thou') — the character can't earn two emotional registers in the same beat
    - [CONCEPT_AS_VERB] form=`(eval '(+ 1 2 3))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval '(+ 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [DOUBLE_EMO_IN_SENTENCE] form=`(eval '(+ 1 2 3))` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described

### G10-15: When not to write a macro

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 3, 'DOUBLE_EMO_IN_SENTENCE': 4, 'DOUBLE_EMO_INJECTION': 4, 'HIGH_LENGTH': 1}
    - [CONCEPT_AS_VERB] form=`(do "a function suffices when no syntax shaping is` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [DOUBLE_EMO_IN_SENTENCE] form=`(do "a function suffices when no syntax shaping is` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(do "a function suffices when no syntax shaping is` — sentence has 2+ distinct EMO-pool phrases ('with a calm that nothing seeme' + 'as if the prize already sat in') — the character can't earn two emotional registers in the same beat
    - [DOUBLE_EMO_IN_SENTENCE] form=`(do "a function suffices when no syntax shaping is` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(do "a function suffices when no syntax shaping is` — sentence has 2+ distinct EMO-pool phrases ('with the clear ringing pride o' + 'with no need to hurry the work') — the character can't earn two emotional registers in the same beat
    - [HIGH_LENGTH] form=`(do "a function suffices when no syntax shaping is` — user_msg 201 words

### G10-16: Macro pattern library

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_EMO_IN_SENTENCE': 4, 'DOUBLE_EMO_INJECTION': 4}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':slow-and-steady'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':slow-and-steady'), resolution doesn't close the loop)
    - [DOUBLE_EMO_IN_SENTENCE] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    - [DOUBLE_EMO_INJECTION] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — sentence has 2+ distinct EMO-pool phrases ('as if the matter were already ' + 'with the slow grace of a creat') — the character can't earn two emotional registers in the same beat
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':slow-and-steady'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':slow',), resolution doesn't close the loop)

## Grade 11

### G11-02: Method call syntax

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'DOUBLE_EMO_INJECTION': 1}
    - [HIGH_LENGTH] form=`(.toUpperCase "abc")` — user_msg 208 words
    - [DOUBLE_EMO_INJECTION] form=`(.startsWith "hare-tortoise" "hare")` — sentence has 2+ distinct EMO-pool phrases ('without complaint or hurry' + 'without complaint') — the character can't earn two emotional registers in the same beat

### G11-03: Static method call

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(Math/abs -7)` — sentence with 5 commas reads as AI-output cadence: 'Brunhilda, her breath even, her step even, her thought even, explained: "To call'

### G11-04: Field access

- examples: 2
- variety @ n=50: 1.00
- issues: {'PRONOUN_BEFORE_NAME': 1}
    - [PRONOUN_BEFORE_NAME] form=`(count "hare")` — sentence-initial 'He' appears before any named character is introduced

### G11-05: Import form

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'HEDGING_NEAR_FORM': 1}
    - [LOW_GROUNDING] form=`(do "(:import (java.util Date)) imports a host cla` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do "(:import (java.util Date)) imports a host cla` — sentence with 6 commas reads as AI-output cadence: 'Theodoric, her breath even, her step even, her thought even, had already written'
    - [LOW_GROUNDING] form=`(do "import is a top-of-file ns clause" :studied)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "import is a top-of-file ns clause" :studied)` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [LOW_GROUNDING] form=`(do "import is a top-of-file ns clause" :studied)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-06: new and dot-construct

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 4, 'STORY_RESOLUTION_NO_DRAWN': 3, 'PRONOUN_BEFORE_NAME': 1}
    - [CONCEPT_AS_VERB] form=`(String. "go")` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(new String "leap")` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(new String "leap")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('leap',), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(new String "leap")` — sentence-initial 'She' appears before any named character is introduced
    - [CONCEPT_AS_VERB] form=`(new String "leap")` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(new String "leap")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('leap',), resolution doesn't close the loop)

### G11-07: Arrays

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CONCEPT_AS_VERB': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (int-array [10 20 30])] (aget a 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '20', '30'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (int-array [10 20 30])] (aget a 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '20', '30'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (int-array [10 20 30])] (aget a 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '20', '30'), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`(let [a (int-array [1 2 3])] (alength a))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(let [a (int-array [1 2 3])] (alength a))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G11-08: Type hints

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 3, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CONCEPT_AS_VERB] form=`(let [^String s "abc"] (.toUpperCase s))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [^String s "abc"] (.toUpperCase s))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`(let [^String s "abc"] (.toUpperCase s))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [^String s "abc"] (.toUpperCase s))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`(let [^String s "abc"] (.toUpperCase s))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [^String s "abc"] (.toUpperCase s))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)

### G11-09: Checked vs unchecked math

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do "*unchecked-math* turns off overflow checking ` — user_msg 206 words

### G11-10: ClojureScript overview

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4}
    - [LOW_GROUNDING] form=`(do "ClojureScript compiles to JavaScript via the ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "ClojureScript compiles to JavaScript via the ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "ClojureScript compiles to JavaScript via the ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "cljs runs in browsers and Node, with JS inter` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-11: cljs / JavaScript interop

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'HEDGING_NEAR_FORM': 2}
    - [LOW_GROUNDING] form=`(do "(js/console.log x) calls a JS global; (.-foo ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "(js/console.log x) calls a JS global; (.-foo ` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [LOW_GROUNDING] form=`(do "(js/console.log x) calls a JS global; (.-foo ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "(js/console.log x) calls a JS global; (.-foo ` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [LOW_GROUNDING] form=`(do "js/<name> namespaces JS globals; .- prefix ma` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-12: Basilisp overview (Python host)

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(do "basilisp is a Clojure-like Lisp implemented o` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "basilisp interops with Python via the same do` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-13: Cross-platform .cljc and reader-conditionals

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'HEDGING_NEAR_FORM': 1}
    - [LOW_GROUNDING] form=`(do "#?(:clj … :cljs …) selects a form per host at` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "#?(:clj … :cljs …) selects a form per host at` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "#?(:clj … :cljs …) selects a form per host at` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "#?(:clj … :cljs …) selects a form per host at` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value

### G11-14: Debugging host leaks

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(try (Math/sqrt 4) (catch Exception _ :err))` — user_msg 229 words

## Grade 12

### G12-01: Transducers introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 3, 'NUMERAL_LIST_IN_GOAL': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] (map inc) [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To use the map-inc transducer with into to increment the vector containing 1, 2,'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (filter even?) [1 2 3 4 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', '5'), resolution doesn't close the loop)
    - [NUMERAL_LIST_IN_GOAL] form=`(into [] (filter even?) [1 2 3 4 5])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing

### G12-02: Transducer composition

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'PRONOUN_BEFORE_NAME': 1, 'NUMERAL_LIST_IN_GOAL': 6, 'CLAUSE_STACK_OVERFLOW': 6, 'HIGH_LENGTH': 1, 'DOUBLE_EMO_INJECTION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [PRONOUN_BEFORE_NAME] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — sentence-initial 'She' appears before any named character is introduced
    - [NUMERAL_LIST_IN_GOAL] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — sentence with 5 commas reads as AI-output cadence: '"To\ncompose map-inc and filter-even into a transducer pipeline, then apply it wi'
    - [HIGH_LENGTH] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — user_msg 207 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)

### G12-03: into with a transducer (xform)

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_EMO_INJECTION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into #{} (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into #{} (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [DOUBLE_EMO_INJECTION] form=`(into #{} (map inc) [1 2 3])` — sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into #{} (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G12-05: Channels and pipelines

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'LOW_GROUNDING': 3, 'HEDGING_NEAR_FORM': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "pipe, mult, mix, pipeline-async route values ` — sentence with 5 commas reads as AI-output cadence: 'Maeve squinted at the goal — to study how pipe, mult, mix, and pipeline-async ro'
    - [LOW_GROUNDING] form=`(do "pipe, mult, mix, pipeline-async route values ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do "pipe, mult, mix, pipeline-async route values ` — sentence with 6 commas reads as AI-output cadence: 'Theodoric, her breath even, her step even, her thought even, had already written'
    - [LOW_GROUNDING] form=`(do "pipelines transform streams of values channel` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "pipelines transform streams of values channel` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [LOW_GROUNDING] form=`(do "pipelines transform streams of values channel` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-07: Spec generators

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'HEDGING_NEAR_FORM': 2}
    - [LOW_GROUNDING] form=`(do "s/exercise produces sample inputs for a spec"` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "s/exercise produces sample inputs for a spec"` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [LOW_GROUNDING] form=`(do "s/exercise produces sample inputs for a spec"` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "spec generators turn specs into property-base` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value

### G12-08: clojure.test

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 3, 'LOW_GROUNDING': 1}
    - [HEDGING_NEAR_FORM] form=`(= (+ 1 2) 3)` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [HEDGING_NEAR_FORM] form=`(= (+ 1 2) 3)` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [LOW_GROUNDING] form=`(do "(deftest …), (is …), (testing …) are the core` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "(deftest …), (is …), (testing …) are the core` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value

### G12-10: Property-based testing

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'HEDGING_NEAR_FORM': 1}
    - [LOW_GROUNDING] form=`(= (reverse (reverse [1 2 3])) [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= (reverse (reverse [1 2 3])) [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "test.check generates inputs and checks proper` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "test.check generates inputs and checks proper` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "test.check generates inputs and checks proper` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [LOW_GROUNDING] form=`(do "test.check generates inputs and checks proper` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-11: Leiningen project.clj

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'HEDGING_NEAR_FORM': 2}
    - [LOW_GROUNDING] form=`(do "project.clj declares :dependencies, :main, :p` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "project.clj declares :dependencies, :main, :p` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [LOW_GROUNDING] form=`(do "project.clj declares :dependencies, :main, :p` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "project.clj declares :dependencies, :main, :p` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [LOW_GROUNDING] form=`(do "Leiningen reads project.clj at the project ro` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-12: deps.edn projects

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(do "deps.edn declares :deps and :aliases for the ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "deps.edn is read by the official `clj`/`cloju` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-13: Aliases and tools

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'HEDGING_NEAR_FORM': 1}
    - [LOW_GROUNDING] form=`(do "`clj -M:test` runs the :test alias from deps.` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "`clj -M:test` runs the :test alias from deps.` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "`clj -M:test` runs the :test alias from deps.` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HEDGING_NEAR_FORM] form=`(do "`clj -M:test` runs the :test alias from deps.` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value

### G12-14: Pedestal / Ring (web stack brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(do "Ring models HTTP as request-map -> response-m` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "Pedestal layers interceptors over Ring for ri` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "Pedestal layers interceptors over Ring for ri` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-15: Datomic / XTDB (datalog db brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(do "Datomic and XTDB are immutable, time-aware da` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "queries are written in datalog over EDN-shape` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-16: Reagent (cljs UI brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do "components are functions returning Hiccup vec` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-17: Library design patterns

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(do "good libraries expose data, then functions, t` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= [1 2 3] (vec '(1 2 3)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= [1 2 3] (vec '(1 2 3)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G12-18: Clojure style guide

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(do "prefer pure functions, name predicates with ?` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do "prefer pure functions, name predicates with ?` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

---

## Summary

### Issue counts (across all examples × 3 records)

- **STORY_RESOLUTION_NO_DRAWN**: 243
- **LOW_GROUNDING**: 202
- **CLAUSE_STACK_OVERFLOW**: 194
- **NARRATIVE_NUMERAL_HARDCODE**: 108
- **DOUBLE_EMO_INJECTION**: 106
- **DOUBLE_EMO_IN_SENTENCE**: 75
- **CONCEPT_PHRASE_COMMA_LIST**: 75
- **PRONOUN_BEFORE_NAME**: 58
- **NUMERAL_LIST_IN_GOAL**: 48
- **HIGH_LENGTH**: 46
- **CONCEPT_AS_VERB**: 39
- **PARAMETRIC_LITERAL_NUMERALS**: 24
- **FORM_DISPLAY_AND_FORM_NOUN**: 22
- **ONLY_SHOOK_HEAD_TIC**: 21
- **REPL_TRIPLE_VOICE**: 20
- **PARALLEL_POSSESSIVE_TIC**: 19
- **LOWERCASE_CONCEPT_AFTER_PERIOD**: 19
- **ANSWER_LEAK**: 18
- **HEDGING_NEAR_FORM**: 16
- **POINTED_AND_SAID_TIC**: 13
- **PARAGRAPH_FRAGMENTATION**: 12
- **THE_FORM_OVERUSE**: 11
- **FORM_LEAK**: 10
- **BOOL_LEAK_RESOLUTION**: 9
- **STRING_AS_CHAR_MISCLAIM**: 6
- **GENERIC_RESOLUTION_TAIL**: 6
- **DOUBLED_PLACE**: 4
- **PROCEDURAL_OPENER**: 3
- **SMALL_INT_LEAK**: 2
- **REPEATED_OPENER_FRAGMENT**: 1
- **ANSWER_LEAK_STRING**: 1
- **DOUBLE_PREP**: 1

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 88 | — |
| 2 | 22 | 88 | 172 | — |
| 3 | 18 | 31 | 87 | — |
| 4 | 20 | 39 | 101 | — |
| 5 | 22 | 39 | 193 | — |
| 6 | 16 | 33 | 54 | — |
| 7 | 18 | 36 | 113 | — |
| 8 | 16 | 31 | 115 | — |
| 9 | 18 | 34 | 218 | — |
| 10 | 16 | 36 | 164 | — |
| 11 | 14 | 29 | 48 | — |
| 12 | 18 | 37 | 79 | — |

### Sample issues by severity

#### FORM_DISPLAY_AND_FORM_NOUN

- `G1-01` (form `nil`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

A handful of market-goers had gathered around the dairy cart
at the farm to watch Marzena attempt to outwit
Konstantin at reading the REPL. Konstantin pointed to
the literal nil and read out the fo...
    ```
- `G1-02` (form `-3`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    It was the season of new chicks and first cheeses, and every small profit felt like the start of a larger one.

A handful of market-goers had gathered around the dairy cart
by the village to watch Greta attempt to outwit
Anselmo at reading the REPL. Anselmo pointed to
the integer -97 and read out th...
    ```
- `G1-02` (form `-3`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    near the market, the dairy stood between the lane and the meadow, and the day's milk waited to be carried to town.

A handful of market-goers had gathered around the dairy cart
near the market to watch Paola attempt to outwit
Bartholomew at reading the REPL. Bartholomew pointed to
the integer -54 an...
    ```
- `G1-02` (form `-25`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    Ingrid hummed quietly near the road as she walked, the pail steady and the future already half-spent.

A handful of market-goers had gathered around the dairy cart
on the road to watch Ingrid attempt to outwit
Alaric at reading the REPL. Alaric pointed to
the integer -96 and read out the form aloud:...
    ```
- `G1-03` (form `(+ 1/2 1/4)`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    Between the dairy and the marketplace stretched a road, a hill, and an entire life imagined into being.

A handful of market-goers had gathered around the dairy cart
by the market to watch Klara attempt to outwit
Kasimir at reading the REPL. Kasimir pointed to
the form (+ 1/2 1/4) and read out the f...
    ```

#### LOW_GROUNDING

- `G1-01` (form `nil`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

A handful of market-goers had gathered around the dairy cart
at the farm to watch Marzena attempt to outwit
Konstantin at reading the REPL. Konstantin pointed to
the literal nil and read out the fo...
    ```
- `G1-02` (form `0`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    The road from the farm to the town was long, and a daydream could fit comfortably along its length.

Halfway through the race, Octavia stopped near the orchard and refused to
continue until someone could prove what the form `2`
evaluated to. Octavia called it impossible.
Clementine, walking up at he...
    ```
- `G1-03` (form `1/2`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    Long before the market opened its stalls, a young woman had already spent her milk three times in her head.

Iustinian had been keeping a careful chalk-tally on the dairy
slate of every form he had successfully evaluated —
each entry one more notch toward a steady reckoning. Today near the road,
the...
    ```
- `G1-05` (form `true`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    at the market, where the lane bends past the old hedge, Edyta began to add up coins she had not yet earned.

Halfway through the race, Edyta stopped near the market and refused to
continue until someone could prove what the form `true`
evaluated to. Edyta called it impossible.
Drusilla, walking up a...
    ```
- `G1-05` (form `false`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    It is an old habit to count the worth of a thing before the thing has reached the buyer.

A handful of market-goers had gathered around the dairy cart
near the orchard to watch Friederike attempt to outwit
Theodelinda at reading the REPL. Theodelinda pointed to
the literal false and read out the for...
    ```

#### STRING_AS_CHAR_MISCLAIM

- `G1-08` (form `\space`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    A pail of milk is a small fortune to a careful walker and a lost fortune to a careless one.

A handful of market-goers had gathered around the dairy cart
on the hilltop to watch Evgenia attempt to outwit
Gerhardt at reading the REPL. Gerhardt pointed to
the character \space and read out the form alo...
    ```
- `G1-08` (form `\space`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

Solveig and Nicoletta stopped by the market where someone had
written the character \space on a flat stone. Solveig, tossing his head as a proud horse tosses its mane, declared
that she could see the ans...
    ```
- `G1-08` (form `\space`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    at the market, the road from the farmstead curved gently downhill, and Tudora walked it with her head held high.

A chalk-board nailed beside the market stall in the market carried a puzzle.
The riddle was simple: it asked the reader to evaluate `"marble"`.
Tudora laughed, as a victor walks before a...
    ```
- `G1-08` (form `\T`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    On market mornings, the dairy yard smelled of damp grass and warm tin, and the future seemed safely arrangeable.

A chalk-board nailed beside the market stall at the village carried a puzzle.
The riddle was simple: it asked the reader to evaluate `"harbor"`.
Vivien laughed, as if the race were alrea...
    ```
- `G1-08` (form `\T`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    It is an old habit to count the worth of a thing before the thing has reached the buyer.

A chalk-board nailed beside the market stall at the edge of the hilltop carried a puzzle.
The riddle was simple: it asked the reader to evaluate `"feather"`.
Ninon laughed, as a young rooster crows above the ya...
    ```

#### PRONOUN_BEFORE_NAME

- `G1-09` (form `(symbol? 'hare)`): sentence-initial 'She' appears before any named character is introduced
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

She claimed, swaggering through the underbrush, "I can ask whether a quoted name is a symbol, using the symbol? predicate without opening the pail — I'll
just read the label!" He tapped the pail, t...
    ```
- `G1-09` (form `(symbol? "tortoise")`): sentence-initial 'She' appears before any named character is introduced
    ```
    It is an old habit to count the worth of a thing before the thing has reached the buyer.

She held two pails side by side. One had "butter" chalked on it; the other held actual butter.
She touched the chalk mark and asked, "Is this butter?" She, with the calm of long custom, said, "That is the
chalk...
    ```
- `G1-14` (form `(+ 1 (* 2 3))`): sentence-initial 'She' appears before any named character is introduced
    ```
    It was the kind of morning that tempts a careful person into carelessness through the back door of a happy thought.

She arrived at the market with a handful of copper coins, jingling in
her pocket — the pail was heavy on her arm and the road had been
long. "I know how much I have without counting,"...
    ```
- `G1-16` (form `(zero? 5)`): sentence-initial 'She' appears before any named character is introduced
    ```
    On market mornings, the dairy yard smelled of damp grass and warm tin, and the future seemed safely arrangeable.

She arrived at the market with a handful of copper coins, jingling in
her pocket — the pail was heavy on her arm and the road had been
long. "I know how much I have without counting," sh...
    ```
- `G1-16` (form `(neg? -3)`): sentence-initial 'She' appears before any named character is introduced
    ```
    by the village, the dairy stood between the lane and the meadow, and the day's milk waited to be carried to town.

She arrived at the market with a handful of copper coins, jingling in
her pocket — the pail was heavy on her arm and the road had been
long. "I know how much I have without counting," s...
    ```

#### PARALLEL_POSSESSIVE_TIC

- `G1-09` (form `(symbol? 'hare)`): user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic
    ```
    Halina set out from the farm near the road with the pail balanced carefully on her head.

She, his nose lifted toward the bright sky, held up a pail with a chalk mark on its side — the word
"cream" written in white. "Is this cream?" She asked, pointing at the chalk
mark. Iustinian, her face quiet, h...
    ```
- `G1-11` (form `(+
  1
  2)`): user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic
    ```
    The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

She, puffed up with pride, arrived at the dairy to find the wall covered in chalk
marks above the milk churns. "What are all these notes?" She asked.
Xaverius, her face quiet, her hands quieter still, po...
    ```
- `G2-01` (form `(+ 1 2 3 4)`): user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic
    ```
    It was by the market, on a fair-weather morning, that Liv began the long walk to market.

She arrived at the market with a handful of copper coins, jingling in
her pocket — the pail was heavy on her arm and the road had been
long. "I know how much I have without counting," she boasted, tossing back ...
    ```
- `G2-01` (form `(+ 1 2 3 4 5 6 7 8 9 10)`): user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic
    ```
    at the edge of the hilltop, before the cocks had finished crowing, Xenia had set out with the milk and a head full of plans.

At the market square, Xenia declared to all the traders, "I will add the integers 1 through 15, and I need no
help!" But when she tried to tally the coins in her head, the da...
    ```
- `G2-05` (form `(mod -7 3)`): user_msg uses 'her X Y, her X Yer still' parallel possessive construction — AI tic
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

She arrived at the market with a handful of copper coins, jingling in
her pocket — the pail was heavy on her arm and the road had been
long. "I know how much I have without counting," she boasted, ...
    ```

#### THE_FORM_OVERUSE

- `G1-10` (form `(+ 1 2) ; sum of one and two`): `the form` appears 6 times in user_msg (template tic — vary references)
    ```
    A pail of milk is a small fortune to a careful walker and a lost fortune to a careless one.

Ula peered at Xaverius's dairy wall and saw lines of chalk marks above the form. Some marks were
crossed out, some added. "The form looks like a mess!" She, as a victor walks before a victory is named, cried...
    ```
- `G1-11` (form `(+    1    2)`): `the form` appears 6 times in user_msg (template tic — vary references)
    ```
    The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

Niamh peered at Cassandra's dairy wall and saw lines of chalk marks above the form. Some marks were
crossed out, some added. "The form looks like a mess!" She, with quiet steps, taking the long way, crie...
    ```
- `G1-11` (form `(+
  1
  2)`): `the form` appears 6 times in user_msg (template tic — vary references)
    ```
    A pail of milk is a small fortune to a careful walker and a lost fortune to a careless one.

Dorothea peered at Augusta's dairy wall and saw lines of chalk marks above the form. Some marks were
crossed out, some added. "The form looks like a mess!" She, sure of the win, head held high, cried. August...
    ```
- `G1-12` (form `(+ 2 3)`): `the form` appears 6 times in user_msg (template tic — vary references)
    ```
    Long before the market opened its stalls, a young woman had already spent her milk three times in her head.

Maeve peered at Euclid's dairy wall and saw lines of chalk marks above the form. Some marks were
crossed out, some added. "The form looks like a mess!" She, with a laugh that carried over the...
    ```
- `G1-12` (form `(* (+ 1 2) 3)`): `the form` appears 6 times in user_msg (template tic — vary references)
    ```
    The cows had given generously that dawn, and the pail was heavier than usual, and the imagination was heavier still.

Rosa peered at Mortimer's dairy wall and saw lines of chalk marks above the form. Some marks were
crossed out, some added. "The form looks like a mess!" She, sure of the win, head he...
    ```

#### DOUBLE_EMO_INJECTION

- `G1-10` (form `(+ 1 2) ; sum of one and two`): sentence has 2+ distinct EMO-pool phrases ('stepping deliberately, one foo' + 'stepping deliberately') — the character can't earn two emotional registers in the same beat
    ```
    Yelena carried more than milk that morning on the farm; she carried a whole imagined fortune.

He handed Yelena a piece of chalk. "Write a mark above the churn," he, stepping deliberately, one foot before the next, said,
"that says what we are about to do." Yelena wrote: "Cooling the cream." Then he...
    ```
- `G1-15` (form `(= 1 1)`): sentence has 2+ distinct EMO-pool phrases ('with a calm that nothing seeme' + 'as if the prize already sat in') — the character can't earn two emotional registers in the same beat
    ```
    There was once a milkmaid who walked to market with a pail of fresh milk balanced upon her head.

She, as if the prize already sat in his paw, gazed at a farmyard gate blocking the path and said,
"Surely this gate will swing open!" Urbanus, with a calm that nothing seemed to ruffle, only pointed at ...
    ```
- `G1-15` (form `(= 1 2)`): sentence has 2+ distinct EMO-pool phrases ('with a calm that nothing seeme' + 'with a smug grin') — the character can't earn two emotional registers in the same beat
    ```
    Solange balanced the pail with the ease of long practice, and at the edge of the orchard the road stretched out invitingly.

She, with a smug grin, gazed at a farmyard gate blocking the path and said,
"Surely this gate will swing open!" Crispin, with a calm that nothing seemed to ruffle, only pointe...
    ```
- `G1-15` (form `(= :hare :hare)`): sentence has 2+ distinct EMO-pool phrases ('stepping high, as proud creatu' + 'her steps unhurried, her mind ') — the character can't earn two emotional registers in the same beat
    ```
    It was the kind of morning that tempts a careful person into carelessness through the back door of a happy thought.

She, stepping high, as proud creatures step, gazed at a farmyard gate blocking the path and said,
"Surely this gate will swing open!" Leonora, her steps unhurried, her mind clear, onl...
    ```
- `G1-15` (form `(= :hare :tortoise)`): sentence has 2+ distinct EMO-pool phrases ('without lifting her voice or q' + 'wearing his pride like a brigh') — the character can't earn two emotional registers in the same beat
    ```
    Every step of the road carried the soft sound of liquid against tin and the louder sound of a daydream gathering speed.

She, wearing his pride like a bright cloak, gazed at a farmyard gate blocking the path and said,
"Surely this gate will swing open!" Vespasia, without lifting her voice or quicken...
    ```

#### REPL_TRIPLE_VOICE

- `G1-10` (form `(+ 1 2) ; sum of one and two`): user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

Beside the dairy tally, the milkmaid had chalked a note: '; sum of one and two.' The note was for her own reference — the dairy buyer at market would never see the chalk wall.

She needed a way to ...
    ```
- `G1-13` (form `(/ 10 2)`): user_msg mentions 'REPL' 5 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    The pail sat steady on Fleur's head as she started down the lane in the market.

Ten coins sat on the tally table. The farmer needed to split them evenly into two equal piles. She chalked a form to divide them. The milkmaid guessed aloud, but the farmer asked: let us ask the REPL, and see what each ...
    ```
- `G1-14` (form `(- 100 (* 5 5))`): user_msg mentions 'REPL' 4 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    On market mornings, the dairy yard smelled of damp grass and warm tin, and the future seemed safely arrangeable.

The farmer had one hundred coins on the tally table. Five coins sat in one pile, another five sat beside it. She chalked a form to find what remained when those two groups were multiplie...
    ```
- `G1-18` (form `(* 7 6)`): user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    Giulia balanced the pail with the ease of long practice, and on the road the road stretched out invitingly.

One afternoon, Giulia hurried down the path and tripped. The pail crashed, and the milk was lost.
She wept. But he gathered the pieces of the pail and showed her
the REPL: "Here is the practi...
    ```
- `G2-19` (form `(* 1000000 1000000)`): user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    Marina had walked this road near the farm a hundred times before, but never quite so dreamily.

The farmer had a million coins stacked on one side of the counting table and a million coins stacked on the other side. She wondered what the total would be if she multiplied them together — a vast number...
    ```

#### CLAUSE_STACK_OVERFLOW

- `G1-11` (form `(+
  1
  2)`): sentence with 6 commas reads as AI-output cadence: 'Xaverius, her face quiet, her hands quieter still, pointed and said: "The chalk '
    ```
    The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

She, puffed up with pride, arrived at the dairy to find the wall covered in chalk
marks above the milk churns. "What are all these notes?" She asked.
Xaverius, her face quiet, her hands quieter still, po...
    ```
- `G1-12` (form `(+ 2 3)`): sentence with 5 commas reads as AI-output cadence: 'Theophilus, with the steady measure of a long walker, pointed and said: "The cha'
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

She, as a young captain walks before his first battle, arrived at the dairy to find the wall covered in chalk
marks above the milk churns. "What are all these notes?" She asked.
Theophilus, with th...
    ```
- `G1-17` (form `42`): sentence with 5 commas reads as AI-output cadence: 'Urbanus, settled in for a long wait, pointed and said: "The chalk marks explain '
    ```
    by the market, where the lane bends past the old hedge, Vivien began to add up coins she had not yet earned.

She, stepping high, as proud creatures step, arrived at the dairy to find the wall covered in chalk
marks above the milk churns. "What are all these notes?" She asked.
Urbanus, settled in fo...
    ```
- `G1-17` (form `42`): sentence with 5 commas reads as AI-output cadence: 'Anselmo, with steady breath and a careful eye, pointed and said: "The chalk mark'
    ```
    on the road, before the cocks had finished crowing, Veronika had set out with the milk and a head full of plans.

She, his eyes bright with the joy of being first, arrived at the dairy to find the wall covered in chalk
marks above the milk churns. "What are all these notes?" She asked.
Anselmo, with...
    ```
- `G2-01` (form `(* 2 3 4)`): sentence with 5 commas reads as AI-output cadence: 'Vespasia only shook her\nhead, stepping deliberately, one foot before the next, a'
    ```
    She had not yet sold the milk and yet had already chosen the ribbons she would wear at the dance.

One afternoon, she found a cache of coins hidden in the dairy and tried to guess
the fortune, boasting at every turn, the dairy cool and the imagined market still far away. "Surely I can
see the total ...
    ```

#### POINTED_AND_SAID_TIC

- `G1-11` (form `(+
  1
  2)`): user_msg uses 'X, [appositive], pointed and said:' — overused AI dialogue cadence
    ```
    The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

She, puffed up with pride, arrived at the dairy to find the wall covered in chalk
marks above the milk churns. "What are all these notes?" She asked.
Xaverius, her face quiet, her hands quieter still, po...
    ```
- `G1-12` (form `(+ 2 3)`): user_msg uses 'X, [appositive], pointed and said:' — overused AI dialogue cadence
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

She, as a young captain walks before his first battle, arrived at the dairy to find the wall covered in chalk
marks above the milk churns. "What are all these notes?" She asked.
Theophilus, with th...
    ```
- `G1-17` (form `42`): user_msg uses 'X, [appositive], pointed and said:' — overused AI dialogue cadence
    ```
    by the market, where the lane bends past the old hedge, Vivien began to add up coins she had not yet earned.

She, stepping high, as proud creatures step, arrived at the dairy to find the wall covered in chalk
marks above the milk churns. "What are all these notes?" She asked.
Urbanus, settled in fo...
    ```
- `G1-17` (form `42`): user_msg uses 'X, [appositive], pointed and said:' — overused AI dialogue cadence
    ```
    on the road, before the cocks had finished crowing, Veronika had set out with the milk and a head full of plans.

She, his eyes bright with the joy of being first, arrived at the dairy to find the wall covered in chalk
marks above the milk churns. "What are all these notes?" She asked.
Anselmo, with...
    ```
- `G2-12` (form `(println "hello")`): user_msg uses 'X, [appositive], pointed and said:' — overused AI dialogue cadence
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

She, his nose lifted toward the bright sky, arrived at the dairy to find the wall covered in chalk
marks above the milk churns. "What are all these notes?" She asked.
Theophilus, without lifting he...
    ```

#### NARRATIVE_NUMERAL_HARDCODE

- `G1-13` (form `(* 4 5)`): parametric example has hard-coded English numeral 'four piles' in a story slot — the actual draws may differ from this fixed count
    ```
    Roisin was not a careless girl by nature, but at the edge of the orchard the morning was bright and the daydreams were brighter.

She arrived at the market with a handful of copper coins, jingling in
her pocket — the pail was heavy on her arm and the road had been
long. "I know how much I have witho...
    ```
- `G1-13` (form `(* 4 5)`): parametric example has hard-coded English numeral 'four piles' in a story slot — the actual draws may differ from this fixed count
    ```
    It happened in the market, on the morning Paola took the milk to market and her thoughts ran ahead of her feet.

One afternoon, she found a cache of coins hidden in the dairy and tried to guess
the fortune, stepping high, as proud creatures step, the dairy cool and the imagined market still far away...
    ```
- `G1-13` (form `(* 4 5)`): parametric example has hard-coded English numeral 'four piles' in a story slot — the actual draws may differ from this fixed count
    ```
    The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

Every morning, Estrid carried a pail of milk to the dairy, imagining what the coins would
total. She only smiled and said, "Come. Let us count the coins from yesterday's
sales." Together they counted: on...
    ```
- `G1-18` (form `(* 7 6)`): parametric example has hard-coded English numeral 'seven piles' in a story slot — the actual draws may differ from this fixed count
    ```
    on the hilltop, the road from the farmstead curved gently downhill, and Ingrid walked it with her head held high.

She, as one struts who has never yet been bested, claimed, "I can multiply 7 by 2 while running and juggling!" But she
knew better. "In the real meadow, a stumble spills the pail. But i...
    ```
- `G1-18` (form `(* 7 6)`): parametric example has hard-coded English numeral 'seven piles' in a story slot — the actual draws may differ from this fixed count
    ```
    By the time Danuta had reached the second milestone near the market, the milk had become eggs, and the eggs a flock.

She arrived at the dairy after a long walk, pail intact and milk brimming. He
smiled and asked, "How did you keep the pail so steady?" She, his nose lifted toward the bright sky, rep...
    ```

#### ANSWER_LEAK

- `G1-13` (form `(- 20 7)`): answer 13 in narrative
    ```
    Seren was not a careless girl by nature, but in the orchard the morning was bright and the daydreams were brighter.

She arrived at the market with a handful of copper coins, jingling in
her pocket — the pail was heavy on her arm and the road had been
long. "I know how much I have without counting,"...
    ```
- `G1-14` (form `(+ 1 (* 2 3))`): answer 7 in narrative
    ```
    It was the kind of morning that tempts a careful person into carelessness through the back door of a happy thought.

She arrived at the market with a handful of copper coins, jingling in
her pocket — the pail was heavy on her arm and the road had been
long. "I know how much I have without counting,"...
    ```
- `G2-05` (form `(quot 100 7)`): answer 14 in narrative
    ```
    Between the dairy and the marketplace stretched a road, a hill, and an entire life imagined into being.

The farmer had 163 coins to divide equally among 3 merchants at the market. She gave each merchant the same whole number of coins without any coins left over. She needed to know how many whole co...
    ```
- `G2-10` (form `(* 5 5)`): answer 25 in narrative
    ```
    The road from the farm to the town was long, and a daydream could fit comfortably along its length.

The farmer had a square garden plot: 5 paces wide and 5 paces long. She needed the total area in square paces to know how much seed to sow.

She needed to multiply 6 by itself to find the area of the...
    ```
- `G2-10` (form `(* 3 3 3 3)`): answer 81 in narrative
    ```
    A pail of milk is a small fortune to a careful walker and a lost fortune to a careless one.

The farmer had a four-dimensional arrangement of coins (a thought experiment): 5 coins in each dimension. She wondered what the total count would be if she could stack all dimensions at once.

She needed to ...
    ```

#### DOUBLE_EMO_IN_SENTENCE

- `G1-15` (form `(= 1 1)`): sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    ```
    There was once a milkmaid who walked to market with a pail of fresh milk balanced upon her head.

She, as if the prize already sat in his paw, gazed at a farmyard gate blocking the path and said,
"Surely this gate will swing open!" Urbanus, with a calm that nothing seemed to ruffle, only pointed at ...
    ```
- `G1-15` (form `(= 1 2)`): sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    ```
    Solange balanced the pail with the ease of long practice, and at the edge of the orchard the road stretched out invitingly.

She, with a smug grin, gazed at a farmyard gate blocking the path and said,
"Surely this gate will swing open!" Crispin, with a calm that nothing seemed to ruffle, only pointe...
    ```
- `G1-15` (form `(= :hare :hare)`): sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    ```
    It was the kind of morning that tempts a careful person into carelessness through the back door of a happy thought.

She, stepping high, as proud creatures step, gazed at a farmyard gate blocking the path and said,
"Surely this gate will swing open!" Leonora, her steps unhurried, her mind clear, onl...
    ```
- `G1-15` (form `(= :hare :tortoise)`): sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    ```
    Every step of the road carried the soft sound of liquid against tin and the louder sound of a daydream gathering speed.

She, wearing his pride like a bright cloak, gazed at a farmyard gate blocking the path and said,
"Surely this gate will swing open!" Vespasia, without lifting her voice or quicken...
    ```
- `G2-13` (form `(or false false)`): sentence contains 2 disjoint EMO-pool phrases — two emotional anchors stacked in one sentence read as over-described
    ```
    near the village, the dairy stood between the lane and the meadow, and the day's milk waited to be carried to town.

She, his chest thrown out before him, gazed at a farmyard gate blocking the path and said,
"Surely this gate will swing open!" Onorata, neither restless nor weary, only steady, only p...
    ```

#### PROCEDURAL_OPENER

- `G1-17` (form `(+ 1 2)`): user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    ```
    The pail sat steady on Niamh's head as she started down the lane on the road.

To add 9 and 5 so the REPL returns the result, he composed the addition and submitted the form. The REPL read past the chalk marks and returned:

Write a form whose evaluation gives the value returned by adding 9 and 5....
    ```
- `G1-17` (form `(+ 1 2)`): user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    ```
    It is an old habit to count the worth of a thing before the thing has reached the buyer.

To add 5 and 0 so the REPL returns the result, she composed the addition and submitted the form. The REPL read past the chalk marks and returned:

Write a form whose evaluation gives the value returned by addin...
    ```
- `G2-05` (form `(quot 17 5)`): user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    ```
    She had not yet sold the milk and yet had already chosen the ribbons she would wear at the dance.

To find the integer quotient of 10 divided by 8, he composed the integer quotient and submitted the form. The REPL counted out the coins:

Write a Clojure expression that computes 10 divided by 8, with...
    ```

#### LOWERCASE_CONCEPT_AFTER_PERIOD

- `G1-18` (form `(+ 1 2)`): sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    ```
    Milk does not forgive a tilted head, but a dreaming mind seldom remembers as much.

She, sure of the win, head held high, claimed, "I can add 7 and 7 while running and juggling!" But he
knew better. "In the real meadow, a stumble spills the pail. But in the practice meadow — the REPL — the
safety ne...
    ```
- `G1-18` (form `(* 7 6)`): sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    ```
    on the hilltop, the road from the farmstead curved gently downhill, and Ingrid walked it with her head held high.

She, as one struts who has never yet been bested, claimed, "I can multiply 7 by 2 while running and juggling!" But she
knew better. "In the real meadow, a stumble spills the pail. But i...
    ```
- `G2-20` (form `(count [1 2 3])`): sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    ```
    The cows had given generously that dawn, and the pail was heavier than usual, and the imagination was heavier still.

She arrived at the market breathless. "How many coins do I have?" He, with the steady turn of a millwheel, asked.
She counted on her fingers, looking back at each milestone. "I picke...
    ```
- `G2-20` (form `(count "hello")`): sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    ```
    It was the kind of morning that tempts a careful person into carelessness through the back door of a happy thought.

She arrived at the market breathless. "How many coins do I have?" He, with the steady walk of a tortoise, asked.
She counted on her fingers, looking back at each milestone. "I picked ...
    ```
- `G2-20` (form `(count [])`): sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    ```
    A pail of milk is a small fortune to a careful walker and a lost fortune to a careless one.

She arrived at the market breathless. "How many coins do I have?" She, with a calm that nothing seemed to ruffle, asked.
She counted on her fingers, looking back at each milestone. "I picked up bags at
five ...
    ```

#### HIGH_LENGTH

- `G2-02` (form `(> 5 4 3 2 1)`): user_msg 201 words
    ```
    It was the season of new chicks and first cheeses, and every small profit felt like the start of a larger one.

The farmer had counted five bags of coins from richest to poorest: the first bag held 1 coins, the next held 3, then 1, then 7, then 8. She wondered if the bags truly decreased in size all...
    ```
- `G3-06` (form `(let [a 5 b (* a 2)] b)`): user_msg 219 words
    ```
    The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

The milkmaid had sewn two compartments into her apron-pocket at the start of the morning round: she tucked a count into the first compartment, then reached in to read it while sewing the second compartme...
    ```
- `G3-09` (form `(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))`): user_msg 224 words
    ```
    Every step of the road carried the soft sound of liquid against tin and the louder sound of a daydream gathering speed.

The milkmaid had nailed a three-slot pail-steps card to the market-board under the name add3: three input slots for the morning, midday, and afternoon counts, and a step that summ...
    ```
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

#### STORY_RESOLUTION_NO_DRAWN

- `G2-08` (form `(+ 1/2 1/4)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    ```
    Between the dairy and the marketplace stretched a road, a hill, and an entire life imagined into being.

One afternoon, she found a cache of coins hidden in the dairy and tried to guess
the fortune, with the easy swagger of a quick runner, the dairy cool and the imagined market still far away. "Sure...
    ```
- `G2-08` (form `(+ 1/2 1/4)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    ```
    Milk does not forgive a tilted head, but a dreaming mind seldom remembers as much.

At the market square, Eveline declared to all the traders, "I will add one-half and one-quarter, and I need no
help!" But when she tried to tally the coins in her head, the daydream of fortune turned the
numbers slip...
    ```
- `G2-08` (form `(+ 1/2 1/4)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    ```
    The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

She arrived at the market with a handful of copper coins, jingling in
her pocket — the pail was heavy on her arm and the road had been
long. "I know how much I have without counting," she boasted, with t...
    ```
- `G2-08` (form `(* 2/3 3/4)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3', '4'), resolution doesn't close the loop)
    ```
    It is an old habit to count the worth of a thing before the thing has reached the buyer.

At the market square, Donata declared to all the traders, "I will multiply two-thirds by three-quarters, and I need no
help!" But when she tried to tally the coins in her head, the daydream of fortune turned th...
    ```
- `G2-08` (form `(* 2/3 3/4)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3', '4'), resolution doesn't close the loop)
    ```
    It was by the farm, on a fair-weather morning, that Zara began the long walk to market.

At the market square, Zara declared to all the traders, "I will multiply two-thirds by three-quarters, and I need no
help!" But when she tried to tally the coins in her head, the daydream of fortune turned the
n...
    ```

#### PARAGRAPH_FRAGMENTATION

- `G2-10` (form `(* 5 5)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    The road from the farm to the town was long, and a daydream could fit comfortably along its length.

The farmer had a square garden plot: 5 paces wide and 5 paces long. She needed the total area in square paces to know how much seed to sow.

She needed to multiply 6 by itself to find the area of the...
    ```
- `G2-10` (form `(* 3 3 3 3)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    A pail of milk is a small fortune to a careful walker and a lost fortune to a careless one.

The farmer had a four-dimensional arrangement of coins (a thought experiment): 5 coins in each dimension. She wondered what the total count would be if she could stack all dimensions at once.

She needed to ...
    ```
- `G2-10` (form `(* 10 10)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    Some plans grow gently from the ground up; others are built from the rooftop down, and topple just as fast.

The farmer had a large square market space with stalls arranged in a grid. She needed the total number of stalls to allocate fairly among traders.

She needed to multiply the width by the len...
    ```
- `G2-10` (form `(* 10 10)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    The pail sat steady on Hanna's head as she started down the lane in the orchard.

The farmer had a large square market space with stalls arranged in a grid. She needed the total number of stalls to allocate fairly among traders.

She needed to multiply the width by the length to find the total stall...
    ```
- `G2-11` (form `(str "p" "q" "r")`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    by the orchard, before the cocks had finished crowing, Jadwiga had set out with the milk and a head full of plans.

The milkmaid had three single-character cloth-marks on her shelf. She needed to braid all three together into one continuous strand.

She needed to join three cloth-strands end-to-end ...
    ```

#### REPEATED_OPENER_FRAGMENT

- `G2-13` (form `(or false true)`): opener fragment 'pail balanced carefully on her head' also appears later in user_msg
    ```
    Elsa set out from the farm near the orchard with the pail balanced carefully on her head.

She, tossing back his ears as if to taunt the wind, hurried down the long farm path toward the village, the
heavy pail balanced carefully on her head. But the path was blocked by a chain of gates — one
after a...
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
- `G5-19` (form `(every? pos? [1 2 3])`): resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    ```
    Marina had walked this road near the farm a hundred times before, but never quite so dreamily.

The milkmaid held the `pos?` strainer over the pail and let three counts pass through: one, two, three. She watched each piece hit the mesh — all of them were above zero.

She needed to know whether every...
    ```

#### DOUBLED_PLACE

- `G2-20` (form `(count [])`): location stutter: 'farm by the farm...'
    ```
    Tove set out from the farm by the farm with the pail balanced carefully on her head.

The farmer held an empty basket (an empty vector). She walked the rope road from start to finish but found no pails inside. She wondered what the count would be.

She needed to count the elements in an empty collec...
    ```
- `G5-07` (form `(or nil false :found)`): location stutter: 'farm on the farm...'
    ```
    Zenta set out from the farm on the farm with the pail balanced carefully on her head.

The milkmaid stood at a farmyard gate with three latch-checks in sequence. The first latch returned nothing; the second returned false. The third bore a keyword mark.

She needed the gate to stop at the first latc...
    ```
- `G7-07` (form `(try (assert (= 1 2)) (catch Throwable e 0))`): location stutter: 'farm on the farm...'
    ```
    Katarzyna set out from the farm on the farm with the pail balanced carefully on her head.

Bess stopped and checked: 'Do I have one coin on my left and two coins on my right, and they are equal?' No—they were clearly different.

The assertion was false. Would the error be caught, or would the walk f...
    ```
- `G10-07` (form `(->> [1 2 3 4] (filter even?) (map inc) (reduce +))`): location stutter: 'farm on the farm...'
    ```
    Zenta set out from the farm on the farm with the pail balanced carefully on her head.

The farmer had written a longer pail-steps card: strain the pail through a sieve, ladle the results through a tally, and reduce the tallied pours to a single measure. The milkmaid threaded the vector through all t...
    ```

#### SMALL_INT_LEAK

- `G2-21` (form `(count "hare")`): small-int answer 4 leaks via resolution-slot phrasing
    ```
    Runa balanced the pail with the ease of long practice, and at the edge of the hilltop the road stretched out invitingly.

The milkmaid had woven another cloth-label with the name 'lichen' braided end-to-end. She walked this shorter strand from first character to last, counting each knot.

She needed...
    ```
- `G9-02` (form `(do (def counter (atom 0)) (swap! counter inc) @counter)`): small-int answer 1 leaks via resolution-slot phrasing
    ```
    Long before the market opened its stalls, a young woman had already spent her milk three times in her head.

The milkmaid hung a fresh tally-slate by the dairy door with the number 0 chalked at the top — the starting count for the day's deliveries. The first pail went out; the slate needed updating....
    ```

#### ONLY_SHOOK_HEAD_TIC

- `G3-02` (form `(do (def x 1) (def x 99) x)`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    The cows had given generously that dawn, and the pail was heavier than usual, and the imagination was heavier still.

She, his chest thrown out before him, declared, "I will invent new names for the prices each time I visit the market!"
But he only shook his head. "No, Katarzyna. To bind x to 7, the...
    ```
- `G3-04` (form `(let [a 1 b 2] (+ a b))`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    Sigrid was not a careless girl by nature, but in the market the morning was bright and the daydreams were brighter.

On a bright morning, Sigrid, as a victor walks before a victory is named, announced, "I shall bind a to 7 and b to 6, then add them while I walk to the mill!"
She clutched her pail an...
    ```
- `G3-06` (form `(let [a 5 b (* a 2)] b)`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    Milk does not forgive a tilted head, but a dreaming mind seldom remembers as much.

On a bright morning, Solveig, with the small pride of small triumphs already counted, announced, "I shall bind a to 1, then bind b to twice a, and return b while I walk to the mill!"
She clutched her pail and pretend...
    ```
- `G3-06` (form `(let [a 3 b (+ a 1) c (* b 2)] c)`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    Some plans grow gently from the ground up; others are built from the rooftop down, and topple just as fast.

On a bright morning, Caitlin, with the easy swagger of a quick runner, announced, "I shall bind a to 8, b to a+3, c to 5*b, and return c while I walk to the mill!"
She clutched her pail and p...
    ```
- `G3-11` (form `(let [a 7] (+ a a))`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

On a bright morning, Niamh, his nose lifted toward the bright sky, announced, "I shall bind a to 1 and add a to itself while I walk to the mill!"
She clutched her pail and pretended the answer was alread...
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
- `G4-03` (form `(conj [1 2] 3)`): form '(conj [1 2] 3)' appears in user_msg of a goal-style subject
    ```
    Roisin balanced the pail with the ease of long practice, and atop the hilltop the road stretched out invitingly.

The milkmaid carried a market-basket holding two items: the number 1 in the first compartment, the number 2 in the second. She paused at the roadside, thinking to add one more item.

She...
    ```
- `G4-08` (form `(assoc {:a 1} :a 99)`): form '(assoc {:a 1} :a 99)' appears in user_msg of a goal-style subject
    ```
    It was by the village, on a fair-weather morning, that Tegan began the long walk to market.

The milkmaid's first basket had been marked :a and held the value 1. But after the day's business, she needed the :a compartment to hold a new value instead — 69, a much larger prize.

She needed to change t...
    ```
- `G4-09` (form `(dissoc {:a 1 :b 2} :a)`): form '(dissoc {:a 1 :b 2} :a)' appears in user_msg of a goal-style subject
    ```
    The road from the farm to the town was long, and a daydream could fit comfortably along its length.

The milkmaid's market-basket held two labeled compartments: one marked :a held 1, another marked :b held 2. But the buyer no longer needed the :a label — the milkmaid decided to leave that compartmen...
    ```

#### PARAMETRIC_LITERAL_NUMERALS

- `G4-05` (form `(cons 0 '(1 2 3))`): parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    ```
    She had not yet sold the milk and yet had already chosen the ribbons she would wear at the dance.

The milkmaid had spoken a list aloud: one, two, three. But then she realized she had forgotten the starting point — the zero from which the count should begin. She needed to add it to the front.

She n...
    ```
- `G4-05` (form `(cons 0 '(1 2 3))`): parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    ```
    It was in the orchard, on a fair-weather morning, that Gisele began the long walk to market.

The market-basket held cream in the first slot, skim in the second, curds in the third. Gisele
peered in and guessed, "I know what's here." But he, keeping a steady pace through the work, asked, "How do you...
    ```
- `G4-05` (form `(cons 0 '(1 2 3))`): parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    ```
    Some plans grow gently from the ground up; others are built from the rooftop down, and topple just as fast.

The milkmaid had spoken a list aloud: one, two, three. But then she realized she had forgotten the starting point — the zero from which the count should begin. She needed to add it to the fro...
    ```
- `G5-11` (form `(filter even? [1 2 3 4])`): parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    ```
    The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

One morning, she poured milk through a strainer with no rule written. The strainer
did nothing — every drop fell away, the fresh pail was empty, and the milk pooled cold and useless
on the dairy floor. "...
    ```
- `G5-11` (form `(filter even? [1 2 3 4])`): parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    ```
    Milk does not forgive a tilted head, but a dreaming mind seldom remembers as much.

She stood with a pail of milk and cried, "I can guess which cream belongs in the market
basket!" But he set a milk-strainer between them. "No guessing," he, with the steady turn of a millwheel, said. "To
keep the eve...
    ```

#### NUMERAL_LIST_IN_GOAL

- `G4-13` (form `(count [1 2 3 4 5])`): goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    ```
    Long before the market opened its stalls, a young woman had already spent her milk three times in her head.

The market-basket held cream in the first slot, skim in the second, curds in the third. Karin
peered in and guessed, "I know what's here." But he, with the steady measure of a long walker, as...
    ```
- `G4-13` (form `(count [1 2 3 4 5])`): goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    ```
    Ninon hummed quietly by the village as she walked, the pail steady and the future already half-spent.

Ninon claimed, with the loud bark of a sure winner, "I shall count the elements in a vector containing 1, 2, 3, 4, and 5 by changing the basket as I carry it."
He weighed the basket in his hands, t...
    ```
- `G4-13` (form `(count [1 2 3 4 5])`): goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    ```
    It was by the farm, on a fair-weather morning, that Odile began the long walk to market.

One afternoon, Odile arrived pulling two baskets. "This one has my guess," she, with the clear ringing pride of the favoured, said,
pointing at one. "This one is the form's result," she said, pointing at the ot...
    ```
- `G5-10` (form `(map #(* % %) [1 2 3 4])`): goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    ```
    Yelena carried more than milk that morning on the farm; she carried a whole imagined fortune.

She watched Walther hold a milk-strainer and pour milk while whispering a rule:
"Keep the cream, let the skim fall." The cream flowed into the fresh pail, transformed somehow — thicker,
richer. "Walther, w...
    ```
- `G5-10` (form `(map #(* % %) [1 2 3 4])`): goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    ```
    It was the kind of morning that tempts a careful person into carelessness through the back door of a happy thought.

She watched Octavia hold a milk-strainer and pour milk while whispering a rule:
"Keep the cream, let the skim fall." The cream flowed into the fresh pail, transformed somehow — thicke...
    ```

#### CONCEPT_AS_VERB

- `G6-01` (form `(name 'clojure.string)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    It was the season of new chicks and first cheeses, and every small profit felt like the start of a larger one.

She, his eyes bright with the joy of being first, declared, "I will invent new names for the prices each time I visit the market!"
But he only shook his head. "No, Katarzyna. To extract th...
    ```
- `G6-03` (form `(clojure.string/upper-case "hare")`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    by the farm, before the cocks had finished crowing, Trudi had set out with the milk and a head full of plans.

She, as a young captain walks before his first battle, declared, "I will invent new names for the prices each time I visit the market!"
But she only shook her head. "No, Trudi. To call the ...
    ```
- `G6-05` (form `(clojure.string/reverse "abc")`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    Every step of the road carried the soft sound of liquid against tin and the louder sound of a daydream gathering speed.

She, as a victor walks before a victory is named, declared, "I will invent new names for the prices each time I visit the market!"
But he only shook his head. "No, Wanda. To call ...
    ```
- `G6-05` (form `(name :owner/item)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    The cows had given generously that dawn, and the pail was heavier than usual, and the imagination was heavier still.

She, with the clear ringing pride of the favoured, declared, "I will invent new names for the prices each time I visit the market!"
But he only shook his head. "No, Mira. To extract ...
    ```
- `G6-06` (form `(:private (meta 'x))`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    Some plans grow gently from the ground up; others are built from the rooftop down, and topple just as fast.

She, stepping high, as proud creatures step, declared, "I will invent new names for the prices each time I visit the market!"
But she only shook her head. "No, Slavena. To check whether the :...
    ```

#### HEDGING_NEAR_FORM

- `G6-10` (form `(:deps {:deps {:a 1 :b 2}})`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    By the time Grainne had reached the second milestone in the orchard, the milk had become eggs, and the eggs a flock.

The wager was set by the orchard: produce the value before the breeze had
turned the next leaf. Grainne bolted into a flurry of
guesses, calling out numbers and second-guessing herse...
    ```
- `G6-11` (form `(clojure.string/split "src:test" #":")`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

The wager was set in the orchard: produce the value before the breeze had
turned the next leaf. Lydia bolted into a flurry of
guesses, calling out numbers and second-guessing herself
about whether the go...
    ```
- `G11-05` (form `(do "import is a top-of-file ns clause" :studied)`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    Every step of the road carried the soft sound of liquid against tin and the louder sound of a daydream gathering speed.

The wager was set at the edge of the meadow: produce the value before the breeze had
turned the next leaf. Winifred bolted into a flurry of
guesses, calling out numbers and second...
    ```
- `G11-11` (form `(do "(js/console.log x) calls a JS global; (.-foo o) reads a`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

The wager was set by the orchard: produce the value before the breeze had
turned the next leaf. Lydia bolted into a flurry of
guesses, calling out numbers and second-guessing herself
about whether the go...
    ```
- `G11-11` (form `(do "(js/console.log x) calls a JS global; (.-foo o) reads a`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    The road from the farm to the town was long, and a daydream could fit comfortably along its length.

The wager was set in the market: produce the value before the breeze had
turned the next leaf. Niamh bolted into a flurry of
guesses, calling out numbers and second-guessing herself
about whether the...
    ```

#### ANSWER_LEAK_STRING

- `G7-10` (form `(:doc (meta '^{:doc "adds two"} plus))`): answer string 'adds two' appears in user_msg
    ```
    It was the season of new chicks and first cheeses, and every small profit felt like the start of a larger one.

Clara found an old scroll marking the symbol 'plus' with notes written in the margins: 'adds two'.

She wanted to read the attached documentation note. What words were written in those mar...
    ```

#### CONCEPT_PHRASE_COMMA_LIST

- `G9-03` (form `(do (def a (atom 0)) (swap! a inc) @a)`): concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    Between the dairy and the marketplace stretched a road, a hill, and an entire life imagined into being.

He approached the tally-slate and muttered a form: "The old count is 47. Add 3. The new
count is 50. Write it." In one motion, he read, computed, and wrote. She
watched and asked, "How did you ke...
    ```
- `G9-03` (form `(do (def a (atom 0)) (swap! a inc) @a)`): concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    Long before the market opened its stalls, a young woman had already spent her milk three times in her head.

One morning, three farmers arrived at the slate to update the count. Zara panicked — "Will the count
become a mess?" But he, stepping deliberately, one foot before the next, said no. "Each fa...
    ```
- `G9-03` (form `(do (def a (atom 0)) (swap! a inc) @a)`): concept_phrase 'atom, swap, and deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    On market mornings, the dairy yard smelled of damp grass and warm tin, and the future seemed safely arrangeable.

The tally-slate hung by the dairy door with the day's count chalked across it. Any farmer
who passed could read the slate. She, with the small pride of small triumphs already counted, tr...
    ```
- `G9-03` (form `(do (def a (atom 10)) (swap! a + 5) @a)`): concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    by the farm, before the cocks had finished crowing, Jadwiga had set out with the milk and a head full of plans.

She stood at the dairy door, staring at the tally-slate. "I want to change the count,
but I do not know how," she admitted. Remigius, with a hen's long stillness on the nest, smiled and p...
    ```
- `G9-03` (form `(do (def a (atom 10)) (swap! a + 5) @a)`): concept_phrase 'atom, swap, deref' is a comma-list of bare tokens — rewrite as a noun phrase that flows into subplot prose
    ```
    It was on the farm, on a fair-weather morning, that Sigrid began the long walk to market.

One morning, three farmers arrived at the slate to update the count. Sigrid panicked — "Will the count
become a mess?" But he, with no need to hurry the work, said no. "Each farmer submits a form for atom, swa...
    ```

#### GENERIC_RESOLUTION_TAIL

- `G9-18` (form `(do (def lock (Object.)) (locking lock 42))`): resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    ```
    in the meadow, the road from the farmstead curved gently downhill, and Theodora walked it with her head held high.

Theodora guessed, "I'll just change the count whenever I feel like it!" But he showed
Theodora the slate: two farmers had erased at the same time, and now the count was a scribble,
unr...
    ```
- `G9-18` (form `(do (def lock (Object.)) (locking lock 42))`): resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

The farmer showed the milkmaid the simplest possible padlocked section: just a plain value inside the lock. The padlock was real — it acquired the monitor — but the body needed no computation.

She...
    ```
- `G9-18` (form `(do (def lock (Object.)) (locking lock 42))`): resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    ```
    She had not yet sold the milk and yet had already chosen the ribbons she would wear at the dance.

She stood at the dairy door, staring at the tally-slate. "I want to change the count,
but I do not know how," she admitted. Octavia, settled in for a long wait, smiled and placed a form in
her hand. "H...
    ```
- `G10-09` (form `(symbol? (gensym))`): resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

She, swaggering through the underbrush, asked, "Why does my form not do what I wrote?" He smiled and pulled out
two slips. "This one is what you wrote — your daydream." He showed the first. "This o...
    ```
- `G10-09` (form `(symbol? (gensym))`): resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    ```
    Halina set out from the farm near the road with the pail balanced carefully on her head.

She, his nose lifted toward the bright sky, daydreamed aloud: "I will test that gensym returns a symbol by doing step one,
then step two, then step three." Iustinian, her face quiet, her hands quieter still, li...
    ```

#### DOUBLE_PREP

- `G9-18` (form `(do (def lock (Object.)) (locking lock 42))`): verb+preposition followed by {place} which already carries its own preposition
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

The farmer showed the milkmaid the simplest possible padlocked section: just a plain value inside the lock. The padlock was real — it acquired the monitor — but the body needed no computation.

She...
    ```

