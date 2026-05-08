# crow-pitcher curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

### G1-01: Eval as substitution

- examples: 4
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`"hello"` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`nil` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-02: Integer numbers

- examples: 6
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`12345` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-05: Booleans

- examples: 6
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`true` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`true` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-07: Keywords

- examples: 5
- variety @ n=50: 1.00
- issues: {'REPEATED_OPENER_FRAGMENT': 1}
    - [REPEATED_OPENER_FRAGMENT] form=`(= :hare :hare)` — opener fragment 'at the edge of the orchard' also appears later in user_msg

### G1-08: Characters

- examples: 4
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'STRING_AS_CHAR_MISCLAIM': 6}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`\h` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [STRING_AS_CHAR_MISCLAIM] form=`\space` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    - [STRING_AS_CHAR_MISCLAIM] form=`\space` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    - [STRING_AS_CHAR_MISCLAIM] form=`\space` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    - [STRING_AS_CHAR_MISCLAIM] form=`\T` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    - [STRING_AS_CHAR_MISCLAIM] form=`\T` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)

### G1-09: Symbols vs values

- examples: 4
- variety @ n=50: 1.00
- issues: {'ONLY_SHOOK_HEAD_TIC': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [ONLY_SHOOK_HEAD_TIC] form=`(symbol? 'hare)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [CLAUSE_STACK_OVERFLOW] form=`(= 'hare 'hare)` — sentence with 5 commas reads as AI-output cadence: "Quoting tells the runtime: don't evaluate this, just hand\nit back as the shape i"

### G1-10: Comments

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'CLAUSE_STACK_OVERFLOW': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(+ 1 2) ; sum of one and two` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [CLAUSE_STACK_OVERFLOW] form=`42 ;; the answer` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'
    - [CLAUSE_STACK_OVERFLOW] form=`42 ;; the answer` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'

### G1-11: Whitespace doesn't matter

- examples: 2
- variety @ n=50: 1.00
- issues: {'ONLY_SHOOK_HEAD_TIC': 1, 'EXPECTED_META_PHRASE': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [ONLY_SHOOK_HEAD_TIC] form=`(+    1    2)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [EXPECTED_META_PHRASE] form=`(+    1    2)` — user_msg uses 'the expected X' meta-language — describes the answer in graders'-vocabulary instead of letting the runtime's return speak for itself
    - [CLAUSE_STACK_OVERFLOW] form=`(+
  1
  2)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'

### G1-12: Parens group; they don't multiply

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'ONLY_SHOOK_HEAD_TIC': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(+ 2 3)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'
    - [CLAUSE_STACK_OVERFLOW] form=`(+ 2 3)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'
    - [ONLY_SHOOK_HEAD_TIC] form=`(* (+ 1 2) 3)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [ONLY_SHOOK_HEAD_TIC] form=`(* (+ 1 2) 3)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

### G1-13: First arithmetic call

- examples: 6
- variety @ n=50: 1.00
- issues: {'PARAGRAPH_FRAGMENTATION': 2}
    - [PARAGRAPH_FRAGMENTATION] form=`(- 20 7)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [PARAGRAPH_FRAGMENTATION] form=`(- 20 7)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G1-15: Equality

- examples: 6
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 5, 'LOW_GROUNDING': 1, 'CLAUSE_STACK_OVERFLOW': 4}
    - [CONCEPT_AS_VERB] form=`(= 1 1)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(= 1 2)` — sentence with 5 commas reads as AI-output cadence: "Murmur the crow, unbothered by the slow progress, paused at the pitcher's rim at"
    - [CLAUSE_STACK_OVERFLOW] form=`(= "a" "a")` — sentence with 5 commas reads as AI-output cadence: "Ash the crow, calm and methodical, paused at the pitcher's rim near the garden,\n"
    - [CONCEPT_AS_VERB] form=`(= :hare :hare)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(= :hare :hare)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G1-17: Printing vs returning

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 3, 'ONLY_SHOOK_HEAD_TIC': 1, 'CLAUSE_STACK_OVERFLOW': 3}
    - [REPL_TRIPLE_VOICE] form=`42` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [ONLY_SHOOK_HEAD_TIC] form=`42` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [REPL_TRIPLE_VOICE] form=`42` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`42` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [CLAUSE_STACK_OVERFLOW] form=`42` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'
    - [CLAUSE_STACK_OVERFLOW] form=`(+ 1 2)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'

### G1-18: Errors are safe in the REPL

- examples: 2
- variety @ n=50: 1.00
- issues: {'EXPECTED_META_PHRASE': 1}
    - [EXPECTED_META_PHRASE] form=`(+ 1 2)` — user_msg uses 'the expected X' meta-language — describes the answer in graders'-vocabulary instead of letting the runtime's return speak for itself

## Grade 2

### G2-01: Multi-arg arithmetic

- examples: 6
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(+ 1 2 3 4 5 6 7 8 9 10)` — parametric example has hard-coded English numeral 'Ten stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(+ 1 2 3 4 5 6 7 8 9 10)` — parametric example has hard-coded English numeral 'Ten stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(+ 1 2 3 4 5 6 7 8 9 10)` — parametric example has hard-coded English numeral 'Ten stones' in a story slot — the actual draws may differ from this fixed count

### G2-03: not= and = with multiple args

- examples: 5
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(not= 1 2)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(not= 1 2)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G2-04: min and max

- examples: 5
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4}
    - [CLAUSE_STACK_OVERFLOW] form=`(min 7 3 9 1 5)` — sentence with 5 commas reads as AI-output cadence: 'Bluster the crow simply began\ncounting carefully — to find the minimum of 6, 4, '
    - [CLAUSE_STACK_OVERFLOW] form=`(min 7 3 9 1 5)` — sentence with 5 commas reads as AI-output cadence: 'Dimsky the crow simply began\ncounting carefully — to find the minimum of 7, 6, 7'
    - [CLAUSE_STACK_OVERFLOW] form=`(max 7 3 9 1 5)` — sentence with 5 commas reads as AI-output cadence: 'To find the maximum of 5, 0, 8, 5, and 3, she composed the maximum of the number'
    - [CLAUSE_STACK_OVERFLOW] form=`(max 7 3 9 1 5)` — sentence with 5 commas reads as AI-output cadence: 'Sapphire the crow simply began\ncounting carefully — to find the maximum of 6, 7,'

### G2-05: quot, rem, mod

- examples: 6
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'PARAGRAPH_FRAGMENTATION': 1, 'REPEATED_OPENER_FRAGMENT': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(rem 17 5)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [PARAGRAPH_FRAGMENTATION] form=`(rem 17 5)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [REPEATED_OPENER_FRAGMENT] form=`(mod 17 5)` — opener fragment 'at the edge of the hilltop' also appears later in user_msg

### G2-06: inc and dec

- examples: 5
- variety @ n=50: 1.00
- issues: {'PARAGRAPH_FRAGMENTATION': 2}
    - [PARAGRAPH_FRAGMENTATION] form=`(inc 0)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [PARAGRAPH_FRAGMENTATION] form=`(inc -1)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G2-07: Absolute value

- examples: 4
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(abs -5)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [PARAGRAPH_FRAGMENTATION] form=`(abs -5)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G2-10: Powers via repeated multiplication

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [LOW_GROUNDING] form=`(* 2 2 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PARAGRAPH_FRAGMENTATION] form=`(* 3 3 3 3)` — user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G2-11: String concatenation with str

- examples: 4
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 5}
    - [CLAUSE_STACK_OVERFLOW] form=`(str 42)` — sentence with 5 commas reads as AI-output cadence: 'Concat strings together, and the vines are spliced; cut a substring\nout, and you'
    - [CLAUSE_STACK_OVERFLOW] form=`(str 42)` — sentence with 5 commas reads as AI-output cadence: 'Concat strings together, and the vines are spliced; cut a substring\nout, and you'
    - [CLAUSE_STACK_OVERFLOW] form=`(str 1 "+" 2 "=" 3)` — sentence with 9 commas reads as AI-output cadence: 'Concat strings together, and the vines are spliced; cut a substring\nout, and you'
    - [CLAUSE_STACK_OVERFLOW] form=`(str 1 "+" 2 "=" 3)` — sentence with 9 commas reads as AI-output cadence: 'Concat strings together, and the vines are spliced; cut a substring\nout, and you'
    - [CLAUSE_STACK_OVERFLOW] form=`(str 1 "+" 2 "=" 3)` — sentence with 9 commas reads as AI-output cadence: 'Concat strings together, and the vines are spliced; cut a substring\nout, and you'

### G2-12: print and println — return values

- examples: 2
- variety @ n=50: 1.00
- issues: {'ONLY_SHOOK_HEAD_TIC': 5}
    - [ONLY_SHOOK_HEAD_TIC] form=`(println "hello")` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [ONLY_SHOOK_HEAD_TIC] form=`(println "hello")` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [ONLY_SHOOK_HEAD_TIC] form=`(print "x")` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [ONLY_SHOOK_HEAD_TIC] form=`(print "x")` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [ONLY_SHOOK_HEAD_TIC] form=`(print "x")` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

### G2-13: and / or — short circuit, return values

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'CLAUSE_STACK_OVERFLOW': 6, 'CONCEPT_AS_VERB': 6}
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(and true true)` — sentence with 5 commas reads as AI-output cadence: 'Windrider the crow, steady in the stone-by-stone approach, paused at the pitcher'
    - [CONCEPT_AS_VERB] form=`(and true false)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(or false true)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(or false false)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G2-14: not — turning truthy to false

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CLAUSE_STACK_OVERFLOW': 2, 'CONCEPT_AS_VERB': 3}
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(not true)` — sentence with 5 commas reads as AI-output cadence: "Spire the crow, patient as the water rose, paused at the pitcher's rim on the hi"
    - [CONCEPT_AS_VERB] form=`(not true)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(not false)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(not false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-15: Falsey values: only false and nil

- examples: 4
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 3, 'CLAUSE_STACK_OVERFLOW': 3, 'REPEATED_OPENER_FRAGMENT': 1}
    - [CONCEPT_AS_VERB] form=`(if 0 1 0)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CLAUSE_STACK_OVERFLOW] form=`(if "" 1 0)` — sentence with 5 commas reads as AI-output cadence: "Murmur the crow, unbothered by the slow progress, paused at the pitcher's rim at"
    - [REPEATED_OPENER_FRAGMENT] form=`(if "" 1 0)` — opener fragment 'the pitcher near the orchard' also appears later in user_msg
    - [CLAUSE_STACK_OVERFLOW] form=`(if nil 1 0)` — sentence with 5 commas reads as AI-output cadence: "Ash the crow, dropping each stone with careful attention, paused at the pitcher'"
    - [CONCEPT_AS_VERB] form=`(if false 1 0)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(if false 1 0)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G2-16: Truthy 0 and empty string

- examples: 4
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 3, 'CLAUSE_STACK_OVERFLOW': 3, 'LOW_GROUNDING': 1}
    - [CONCEPT_AS_VERB] form=`(boolean 0)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CLAUSE_STACK_OVERFLOW] form=`(boolean 0)` — sentence with 5 commas reads as AI-output cadence: "Hum the crow, patient as the water rose, paused at the pitcher's rim in the vill"
    - [CLAUSE_STACK_OVERFLOW] form=`(boolean "")` — sentence with 6 commas reads as AI-output cadence: "Whistle the crow, watching the level lift, drop by drop, paused at the pitcher's"
    - [CONCEPT_AS_VERB] form=`(boolean "")` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CLAUSE_STACK_OVERFLOW] form=`(boolean false)` — sentence with 5 commas reads as AI-output cadence: "Whistle the crow, letting the count rise on its own, paused at the pitcher's rim"
    - [LOW_GROUNDING] form=`(boolean false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-18: Quoting symbols

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 2}
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= (quote tortoise) 'tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= (quote tortoise) 'tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count '(1 2 3))` — parametric example has hard-coded English numeral 'three integers' in a story slot — the actual draws may differ from this fixed count

### G2-19: Auto-promotion to bigint

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1}
    - [ANSWER_LEAK] form=`(+ 99999999999 1)` — answer 100000000000 in narrative

### G2-20: Counting

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'Vellum the crow, deliberate, unhurried by the rising sun, walked the rim of the '

### G2-21: String length and substring

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(count "tortoise")` — sentence with 5 commas reads as AI-output cadence: 'Concat strings together, and the vines are spliced; cut a substring\nout, and you'
    - [CLAUSE_STACK_OVERFLOW] form=`(count (subs "tortoise" 0 3))` — sentence with 6 commas reads as AI-output cadence: 'Concat strings together, and the vines are spliced; cut a substring\nout, and you'

## Grade 3

### G3-03: let — local binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'FORM_DISPLAY_AND_FORM_NOUN': 3, 'THE_FORM_OVERUSE': 3}
    - [HIGH_LENGTH] form=`(let [x 3] (+ x 1))` — user_msg 210 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [x 3] (+ x 1))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [HIGH_LENGTH] form=`(let [x 3] (+ x 1))` — user_msg 208 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [x 3] (+ x 1))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [THE_FORM_OVERUSE] form=`(let [n 10] (* n n))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [n 10] (* n n))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G3-04: let — multi-binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2, 'ANSWER_LEAK': 2, 'THE_FORM_OVERUSE': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [a 1 b 2] (+ a b))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [x 5 y 3] (- x y))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [ANSWER_LEAK] form=`(let [a 2 b 3 c 4] (+ a b c))` — answer 9 in narrative
    - [ANSWER_LEAK] form=`(let [a 2 b 3 c 4] (+ a b c))` — answer 9 in narrative
    - [THE_FORM_OVERUSE] form=`(let [a 2 b 3 c 4] (+ a b c))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a 2 b 3 c 4] (+ a b c))` — sentence with 6 commas reads as AI-output cadence: "Step past the form's edge and the wing opens; the value\nexisted only inside the "

### G3-06: let — binding can reference prior

- examples: 2
- variety @ n=50: 1.00
- issues: {'THE_FORM_OVERUSE': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [THE_FORM_OVERUSE] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — sentence with 6 commas reads as AI-output cadence: "Step past the form's edge and the wing opens; the value\nexisted only inside the "

### G3-08: fn — multi-arg

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'CONCEPT_AS_VERB': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`((fn [a b c] (+ a b c)) 1 2 3)` — sentence with 6 commas reads as AI-output cadence: 'The pitcher is narrow — every step\nmust fit, none can be skipped." To create an '
    - [CONCEPT_AS_VERB] form=`((fn [a b c] (+ a b c)) 1 2 3)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G3-09: defn — shorthand

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'CONCEPT_AS_VERB': 1, 'EXPECTED_META_PHRASE': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [ANSWER_LEAK] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — answer 6 in narrative
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — sentence with 7 commas reads as AI-output cadence: 'The pitcher is narrow — every step\nmust fit, none can be skipped." To define a f'
    - [CONCEPT_AS_VERB] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [EXPECTED_META_PHRASE] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — user_msg uses 'the expected X' meta-language — describes the answer in graders'-vocabulary instead of letting the runtime's return speak for itself
    - [PARAGRAPH_FRAGMENTATION] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`(#(+ % 1) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G3-11: Substitution rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'THE_FORM_OVERUSE': 2}
    - [THE_FORM_OVERUSE] form=`(let [a 7] (+ a a))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [THE_FORM_OVERUSE] form=`((fn [x] (* x x)) 6)` — `the form` appears 5 times in user_msg (template tic — vary references)

### G3-12: Scope vs namespace

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def g 5) (let [g 99] (+ g 1)))` — sentence with 5 commas reads as AI-output cadence: 'To define g at the top level, shadow it in a let with a different value, and com'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def g 5) (let [g 99] (+ g 1)))` — sentence with 5 commas reads as AI-output cadence: 'To define g at the top level, shadow it in a let with a different value, and com'

### G3-13: fn body returns last form

- examples: 1
- variety @ n=50: 1.00
- issues: {'PARAGRAPH_FRAGMENTATION': 2}
    - [PARAGRAPH_FRAGMENTATION] form=`((fn [x] x x x 99) 1)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [PARAGRAPH_FRAGMENTATION] form=`((fn [x] x x x 99) 1)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G3-14: do form

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do 1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'

### G3-18: When to name vs inline

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_LEAK': 1, 'LOW_GROUNDING': 1}
    - [FORM_LEAK] form=`(* 5 5 5)` — form '(* 5 5 5)' appears in user_msg of a goal-style subject
    - [LOW_GROUNDING] form=`(* 5 5 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 4

### G4-01: Vector literal

- examples: 3
- variety @ n=50: 1.00
- issues: {'PARAGRAPH_FRAGMENTATION': 3, 'REPL_TRIPLE_VOICE': 4, 'LOW_GROUNDING': 1}
    - [PARAGRAPH_FRAGMENTATION] form=`[]` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [REPL_TRIPLE_VOICE] form=`[]` — user_msg mentions 'REPL' 4 times — the REPL personification should appear at most twice per record (submit + return)
    - [PARAGRAPH_FRAGMENTATION] form=`[]` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [REPL_TRIPLE_VOICE] form=`[]` — user_msg mentions 'REPL' 4 times — the REPL personification should appear at most twice per record (submit + return)
    - [PARAGRAPH_FRAGMENTATION] form=`[]` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [REPL_TRIPLE_VOICE] form=`[]` — user_msg mentions 'REPL' 4 times — the REPL personification should appear at most twice per record (submit + return)

### G4-02: nth — vector access

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(nth [10 20 30] 0)` — sentence with 5 commas reads as AI-output cadence: 'To get the element at index 0 of a vector containing 10, 20, and 30 properly,\nhe'
    - [CLAUSE_STACK_OVERFLOW] form=`(nth [10 20 30] 2)` — sentence with 5 commas reads as AI-output cadence: 'The pile is heavy; one\nright reach saves a dozen wrong ones." To get the element'

### G4-03: conj — append to vector

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 2}
    - [REPL_TRIPLE_VOICE] form=`(conj [1 2] 3)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`(conj [] :hare)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G4-04: List literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`'(1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'The pile is heavy; one\nright reach saves a dozen wrong ones." To create a list c'
    - [CLAUSE_STACK_OVERFLOW] form=`'(1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'The pile is heavy; one\nright reach saves a dozen wrong ones." To create a list c'

### G4-07: get — map lookup

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'LOW_GROUNDING': 1, 'REPL_TRIPLE_VOICE': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(get {:a 1 :b 2} :a)` — sentence with 5 commas reads as AI-output cadence: "(with {('__kw__', 'plum'): 12, ('__kw__', 'pear'): 2, ('__kw__', 'blackberry'): "
    - [LOW_GROUNDING] form=`(get {:a 1} :missing :default)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [REPL_TRIPLE_VOICE] form=`(get {:a 1} :missing :default)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G4-10: keys and vals

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(count (keys {:a 1 :b 2 :c 3}))` — sentence with 5 commas reads as AI-output cadence: 'The pile is heavy; one\nright reach saves a dozen wrong ones." To count how many '
    - [CLAUSE_STACK_OVERFLOW] form=`(count (keys {:a 1 :b 2 :c 3}))` — sentence with 5 commas reads as AI-output cadence: 'The pile is heavy; one\nright reach saves a dozen wrong ones." To count how many '

### G4-11: Set literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(count #{1 2 3})` — sentence with 5 commas reads as AI-output cadence: 'The pile is heavy; one\nright reach saves a dozen wrong ones." To count the eleme'

### G4-12: Set membership

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3, 'REPL_TRIPLE_VOICE': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(contains? #{1 2 3} 2)` — sentence with 5 commas reads as AI-output cadence: 'To check whether 2 is a member of a set containing 1, 2, and 3 properly,\nhe comp'
    - [CLAUSE_STACK_OVERFLOW] form=`(contains? #{1 2 3} 2)` — sentence with 5 commas reads as AI-output cadence: 'The pile is heavy; one\nright reach saves a dozen wrong ones." To check whether 2'
    - [CLAUSE_STACK_OVERFLOW] form=`(contains? #{1 2 3} 2)` — sentence with 5 commas reads as AI-output cadence: 'The pile is heavy; one\nright reach saves a dozen wrong ones." To check whether 2'
    - [REPL_TRIPLE_VOICE] form=`(contains? #{1 2 3} 4)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G4-13: count — universal

- examples: 4
- variety @ n=50: 1.00
- issues: {'NUMERAL_LIST_IN_GOAL': 3, 'CLAUSE_STACK_OVERFLOW': 5}
    - [NUMERAL_LIST_IN_GOAL] form=`(count [1 2 3 4 5])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3 4 5])` — sentence with 5 commas reads as AI-output cadence: 'To count the elements in a vector containing 1, 2, 3, 4, and 5, he composed the '
    - [NUMERAL_LIST_IN_GOAL] form=`(count [1 2 3 4 5])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3 4 5])` — sentence with 7 commas reads as AI-output cadence: 'The pile is heavy; one\nright reach saves a dozen wrong ones." To count the eleme'
    - [NUMERAL_LIST_IN_GOAL] form=`(count [1 2 3 4 5])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3 4 5])` — sentence with 7 commas reads as AI-output cadence: 'To count the elements in a vector containing 1, 2, 3, 4, and 5 properly,\nshe com'

### G4-14: empty?

- examples: 3
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 2}
    - [REPL_TRIPLE_VOICE] form=`(empty? [])` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`(empty? [1])` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G4-15: first, rest, last

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(last [10 20 30])` — sentence with 5 commas reads as AI-output cadence: 'The pile is heavy; one\nright reach saves a dozen wrong ones." To get the last el'
    - [CLAUSE_STACK_OVERFLOW] form=`(count (rest [10 20 30]))` — sentence with 5 commas reads as AI-output cadence: 'The pile is heavy; one\nright reach saves a dozen wrong ones." To count the eleme'
    - [CLAUSE_STACK_OVERFLOW] form=`(count (rest [10 20 30]))` — sentence with 5 commas reads as AI-output cadence: 'To count the elements remaining after removing the first element from a vector w'

### G4-16: into and conj on collections

- examples: 2
- variety @ n=50: 0.99
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] '(1 2 3))` — sentence with 5 commas reads as AI-output cadence: 'Highwing the crow, deliberate, unhurried by the rising sun, held two decision-ru'
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] '(1 2 3))` — sentence with 5 commas reads as AI-output cadence: 'Smoulder the crow, watching the level lift, drop by drop, held two decision-rule'

### G4-18: Equality of vectors and lists

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(= [1 2 3] '(1 2 3))` — sentence with 5 commas reads as AI-output cadence: 'The pile is heavy; one\nright reach saves a dozen wrong ones." To test whether a '

### G4-19: range and seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (range 5))` — parametric example has hard-coded English numeral 'Five integers' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (range 5))` — parametric example has hard-coded English numeral 'Five integers' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (range 5))` — parametric example has hard-coded English numeral 'Five integers' in a story slot — the actual draws may differ from this fixed count

### G4-20: Collection vs sequence

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'REPL_TRIPLE_VOICE': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(count (seq [1 2 3]))` — sentence with 5 commas reads as AI-output cadence: 'To convert a vector containing 1, 2, and 3 to a sequence and count its elements '
    - [CLAUSE_STACK_OVERFLOW] form=`(count (seq [1 2 3]))` — sentence with 5 commas reads as AI-output cadence: 'The pile is heavy; one\nright reach saves a dozen wrong ones." To convert a vecto'
    - [REPL_TRIPLE_VOICE] form=`(seq [])` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

## Grade 5

### G5-01: if

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(if false :a :b)` — sentence with 5 commas reads as AI-output cadence: 'Pirouette the crow, trusting the process, stone after stone, spread her wings in'

### G5-03: when

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 2, 'LOW_GROUNDING': 2}
    - [ANSWER_LEAK_STRING] form=`(when true :yes)` — answer string ':yes' appears in user_msg
    - [LOW_GROUNDING] form=`(when true :yes)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [ANSWER_LEAK_STRING] form=`(when true :yes)` — answer string ':yes' appears in user_msg
    - [LOW_GROUNDING] form=`(when true :yes)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G5-05: cond — :else

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(cond false :a false :b :else :c)` — sentence with 5 commas reads as AI-output cadence: 'Tailwind the crow, unhurried, form after form, spread his wings at the edge of t'
    - [CLAUSE_STACK_OVERFLOW] form=`(cond false :a false :b :else :c)` — sentence with 5 commas reads as AI-output cadence: 'Mystery the crow, deliberate, unhurried by the rising sun, perched above the pit'
    - [CLAUSE_STACK_OVERFLOW] form=`(cond false :a false :b :else :c)` — sentence with 5 commas reads as AI-output cadence: 'Trill the crow, watching the level lift, drop by drop, perched above the pitcher'

### G5-06: case

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(case 2 1 :one 2 :two 3 :three :default)` — sentence with 5 commas reads as AI-output cadence: 'Onyx the crow, trusting the process, stone after stone, perched above the pitche'

### G5-07: and / or as control flow

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'ANSWER_LEAK_STRING': 1, 'LOW_GROUNDING': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(or nil false :found)` — sentence with 5 commas reads as AI-output cadence: 'Shadow the crow, dropping each stone with careful attention, paused at the pitch'
    - [ANSWER_LEAK_STRING] form=`(or nil false :found)` — answer string ':found' appears in user_msg
    - [LOW_GROUNDING] form=`(or nil false :found)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G5-08: not

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(not (> 1 2))` — sentence with 6 commas reads as AI-output cadence: "Float the crow, trusting the process, stone after stone, paused at the pitcher's"

### G5-10: map

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'NUMERAL_LIST_IN_GOAL': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(map inc [1 2 3])` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(map inc [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'To pour the vector containing 1, 2, 3 through a sieve whose rule is inc, collect'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(map inc [1 2 3])` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(map inc [1 2 3])` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NUMERAL_LIST_IN_GOAL] form=`(map #(* % %) [1 2 3 4])` — goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(map #(* % %) [1 2 3 4])` — goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing

### G5-11: filter

- examples: 2
- variety @ n=50: 1.00
- issues: {'NUMERAL_LIST_IN_GOAL': 6, 'CLAUSE_STACK_OVERFLOW': 2}
    - [NUMERAL_LIST_IN_GOAL] form=`(filter even? [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(filter even? [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(filter even? [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(filter even? [1 2 3 4])` — sentence with 5 commas reads as AI-output cadence: 'Quibble the crow, deliberate, unhurried by the rising sun, held two decision-rul'
    - [NUMERAL_LIST_IN_GOAL] form=`(filter pos? [-2 -1 0 1 2])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(filter pos? [-2 -1 0 1 2])` — sentence with 8 commas reads as AI-output cadence: 'Riddlecaw the crow shook\nher head and went on with the work: to\nkeep the positiv'

### G5-12: reduce

- examples: 3
- variety @ n=50: 1.00
- issues: {'NUMERAL_LIST_IN_GOAL': 9, 'CLAUSE_STACK_OVERFLOW': 6}
    - [NUMERAL_LIST_IN_GOAL] form=`(reduce + [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(reduce + [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + [1 2 3 4])` — sentence with 6 commas reads as AI-output cadence: 'To walk the row of pebbles 1, 2, 3, 4 carrying a tally that combines each with +'
    - [NUMERAL_LIST_IN_GOAL] form=`(reduce + [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(reduce * [1 2 3 4 5])` — goal_text contains 5 numerals across 5 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce * [1 2 3 4 5])` — sentence with 8 commas reads as AI-output cadence: 'To fold * over the vector containing 1, 2, 3, 4, and 5, computing their product,'

### G5-13: reduce with init

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + 100 [1 2 3])` — sentence with 9 commas reads as AI-output cadence: 'The runtime does this for any\ncollection — vector, list, map, string." To fold +'
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + 100 [1 2 3])` — sentence with 9 commas reads as AI-output cadence: 'The runtime does this for any\ncollection — vector, list, map, string." To fold +'
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + 0 [])` — sentence with 5 commas reads as AI-output cadence: 'Whirlwind the crow, unhurried, form after form, walked the rim of the pitcher at'

### G5-14: apply

- examples: 2
- variety @ n=50: 1.00
- issues: {'NUMERAL_LIST_IN_GOAL': 6, 'CLAUSE_STACK_OVERFLOW': 2, 'CONCEPT_AS_VERB': 2}
    - [NUMERAL_LIST_IN_GOAL] form=`(apply + [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(apply + [1 2 3 4])` — sentence with 6 commas reads as AI-output cadence: '(with 18, 3, 16, and 7 folded in)\n\nWrite a Clojure expression that computes the '
    - [NUMERAL_LIST_IN_GOAL] form=`(apply + [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CONCEPT_AS_VERB] form=`(apply + [1 2 3 4])` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [NUMERAL_LIST_IN_GOAL] form=`(apply + [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(apply max [3 1 4 1 5])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing

### G5-16: partial

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1, 'CLAUSE_STACK_OVERFLOW': 2}
    - [CONCEPT_AS_VERB] form=`((partial + 10) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CLAUSE_STACK_OVERFLOW] form=`(map (partial * 3) [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'The pitcher is narrow — every step\nmust fit, none can be skipped." To apply a pa'
    - [CLAUSE_STACK_OVERFLOW] form=`(map (partial * 3) [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To apply a partially applied multiplication to each element of the vector contai'

### G5-17: juxt

- examples: 1
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`((juxt inc dec) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G5-18: some

- examples: 2
- variety @ n=50: 1.00
- issues: {'NUMERAL_LIST_IN_GOAL': 3, 'CLAUSE_STACK_OVERFLOW': 2}
    - [NUMERAL_LIST_IN_GOAL] form=`(some even? [1 3 5 8 7])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(some even? [1 3 5 8 7])` — sentence with 7 commas reads as AI-output cadence: 'To check if any element in the vector containing 1, 3, 5, 8, and 7 is even, she '
    - [NUMERAL_LIST_IN_GOAL] form=`(some even? [1 3 5 8 7])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(some even? [1 3 5 8 7])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(some even? [1 3 5 8 7])` — sentence with 7 commas reads as AI-output cadence: 'To check if any element in the vector containing 1, 3, 5, 8, and 7 is even, she '

### G5-19: every?

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(every? pos? [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'Windrider the crow shook\nher head and went on with the work: to\ncheck if all ele'
    - [CLAUSE_STACK_OVERFLOW] form=`(every? pos? [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To check if all elements in the vector containing 1, 2, and 3 are positive, she '
    - [CLAUSE_STACK_OVERFLOW] form=`(every? even? [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'Shout the crow shook\nher head and went on with the work: to\ncheck if all element'

### G5-20: take and drop

- examples: 2
- variety @ n=50: 1.00
- issues: {'NUMERAL_LIST_IN_GOAL': 6, 'CLAUSE_STACK_OVERFLOW': 2}
    - [NUMERAL_LIST_IN_GOAL] form=`(take 3 [10 20 30 40 50])` — goal_text contains 6 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(take 3 [10 20 30 40 50])` — sentence with 8 commas reads as AI-output cadence: 'Burble the crow shook\nhis head and went on with the work: to\ntake the first 3 el'
    - [NUMERAL_LIST_IN_GOAL] form=`(take 3 [10 20 30 40 50])` — goal_text contains 6 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(take 3 [10 20 30 40 50])` — goal_text contains 6 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(take 3 [10 20 30 40 50])` — sentence with 7 commas reads as AI-output cadence: 'To take the first 3 elements from the vector containing 10, 20, 30, 40, and 50, '
    - [NUMERAL_LIST_IN_GOAL] form=`(drop 2 [10 20 30 40 50])` — goal_text contains 6 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing

### G5-21: distinct and sort

- examples: 2
- variety @ n=50: 1.00
- issues: {'NUMERAL_LIST_IN_GOAL': 3, 'CLAUSE_STACK_OVERFLOW': 3}
    - [NUMERAL_LIST_IN_GOAL] form=`(distinct [1 1 2 3 3 4])` — goal_text contains 6 numerals across 5 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(distinct [1 1 2 3 3 4])` — sentence with 5 commas reads as AI-output cadence: 'Write a form whose evaluation gives the sequence produced by passing 1, 1, 2, 3,'
    - [NUMERAL_LIST_IN_GOAL] form=`(distinct [1 1 2 3 3 4])` — goal_text contains 6 numerals across 5 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(distinct [1 1 2 3 3 4])` — sentence with 9 commas reads as AI-output cadence: 'Shroud the crow shook\nhis head and went on with the work: to\nremove duplicate el'
    - [NUMERAL_LIST_IN_GOAL] form=`(distinct [1 1 2 3 3 4])` — goal_text contains 6 numerals across 5 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(distinct [1 1 2 3 3 4])` — sentence with 5 commas reads as AI-output cadence: 'Question: write a Clojure expression for the sequence produced by passing 1, 1, '

### G5-22: recur — first taste

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'ANSWER_LEAK': 2, 'BAD_PLACE_PREP': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — sentence with 6 commas reads as AI-output cadence: 'To walk a small circuit five times, multiplying a running tally by the current s'
    - [ANSWER_LEAK] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — answer 120 in narrative
    - [BAD_PLACE_PREP] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — 'in the hilltop' (wrong preposition)
    - [ANSWER_LEAK] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — answer 120 in narrative
    - [BAD_PLACE_PREP] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — 'in the hilltop' (wrong preposition)

## Grade 6

### G6-01: Namespace as file

- examples: 3
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1, 'LOW_GROUNDING': 1}
    - [ANSWER_LEAK_STRING] form=`(name 'foo.bar)` — answer string 'foo.bar' appears in user_msg
    - [LOW_GROUNDING] form=`(name 'foo.bar)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-05: Fully qualified names

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/reverse "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/reverse "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/reverse "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(namespace :owner/item)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-09: Loading order

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — sentence with 5 commas reads as AI-output cadence: 'To define step1 as 1, then define step2 as step1 plus 1, then return step2, the '
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a 1 b (+ a 1)] (+ a b))` — sentence with 5 commas reads as AI-output cadence: "The next crow who perches reads what's\nthere now — whatever the latest talon-str"

### G6-11: Classpath

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "src:test" #":")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':test', 'src:test'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "src:test" #":")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':test', 'src:test'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "src:test" #":")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':test', 'src:test'), resolution doesn't close the loop)
    - [HEDGING_NEAR_FORM] form=`(count ["src" "test" "resources"])` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(count ["src" "test" "resources"])` — sentence with 6 commas reads as AI-output cadence: 'Chatter the crow, unhurried, form after form, walked to the slate and began to\nw'

### G6-14: Import for host classes

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(symbol? 'java.util.List)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(name 'java.util.Map)` — sentence with 5 commas reads as AI-output cadence: "The runtime moves a stone across the boundary, calls\nthe human's method, and bri"
    - [LOW_GROUNDING] form=`(name 'java.util.Map)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-16: Cleaning up requires

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.set)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 7

### G7-02: try / catch

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(try 42 (catch Exception e :caught))` — sentence with 5 commas reads as AI-output cadence: 'Eclipse the crow, deliberate, unhurried by the rising sun, spread a patch of sof'

### G7-04: ex-info

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(try (throw (ex-info "x" {:k :v})) (catch Exceptio` — sentence with 5 commas reads as AI-output cadence: 'Caw the crow, deliberate, unhurried by the rising sun, spread a patch of soft mo'

### G7-05: nil punning

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(first nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(first nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(count nil)` — sentence with 5 commas reads as AI-output cadence: 'Riddle the crow, watching the level lift, drop by drop, spread a patch of soft m'

### G7-06: pre and post conditions

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — sentence with 5 commas reads as AI-output cadence: 'Galena the crow, watching the level lift, drop by drop, spread a patch of soft m'

### G7-07: assert

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPEATED_OPENER_FRAGMENT': 1, 'CLAUSE_STACK_OVERFLOW': 3}
    - [REPEATED_OPENER_FRAGMENT] form=`(do (assert (= 1 1)) 1)` — opener fragment 'the pitcher near the farm' also appears later in user_msg
    - [CLAUSE_STACK_OVERFLOW] form=`(do (assert (= 1 1)) 1)` — sentence with 5 commas reads as AI-output cadence: 'Thermal the crow, watching the level lift, drop by drop, spread a patch of soft '
    - [CLAUSE_STACK_OVERFLOW] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — sentence with 5 commas reads as AI-output cadence: 'To assert that 5 equals 0, catch the failure, and return a numeric code, he comp'
    - [CLAUSE_STACK_OVERFLOW] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — sentence with 5 commas reads as AI-output cadence: 'To assert that 5 equals 8, catch the failure, and return a numeric code, she com'

### G7-08: prn and pprint

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(with-out-str (prn :hare))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(with-out-str (prn :hare))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(with-out-str (prn :hare))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare',), resolution doesn't close the loop)

### G7-09: tap>

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'PARAGRAPH_FRAGMENTATION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(tap> :hello)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hello',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(tap> :hello)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hello',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(tap> :hello)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hello',), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(tap> 42)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G7-11: Reading stack traces

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'ANSWER_LEAK_STRING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "trouble" {})) (catch Excepti` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('trouble',), resolution doesn't close the loop)
    - [ANSWER_LEAK_STRING] form=`(try (throw (ex-info "trouble" {})) (catch Excepti` — answer string 'trouble' appears in user_msg
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "trouble" {})) (catch Excepti` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('trouble',), resolution doesn't close the loop)

### G7-12: slurp and spit

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(count "hare
tortoise
")` — sentence with 5 commas reads as AI-output cadence: 'Flat stones are how the two meet — a value crosses out\nand becomes scratches on '

### G7-13: line-seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)

### G7-15: *in* and *out*

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(with-out-str (println))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-16: edn read

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "42")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', '42'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "42")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', '42'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "42")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', '42'), resolution doesn't close the loop)

### G7-17: JSON roundtrip

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b'), resolution doesn't close the loop)

### G7-18: Shell command

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4}
    - [LOW_GROUNDING] form=`(:cmd {:cmd "ls" :args ["-l"]})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(:cmd {:cmd "ls" :args ["-l"]})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count (:args {:cmd "echo" :args ["hello" "world"]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count (:args {:cmd "echo" :args ["hello" "world"]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 8

### G8-01: Why polymorphism

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(let [speak (fn [k] (cond (= k :hare) "swift" (= k` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-02: deftype introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)

### G8-03: defrecord introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [ANSWER_LEAK_STRING] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — answer string ':slow' appears in user_msg
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — sentence with 5 commas reads as AI-output cadence: 'Lighter, more focused." To\ndefine a Runner case with two named compartments, nam'

### G8-05: Protocol extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'The runtime reads from this ledger whenever the call goes out." To\ndefine a prot'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol named Greet with one method hail, extend it to Long type wi'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — sentence with 6 commas reads as AI-output cadence: 'The\nruntime looks up which crow is present, then runs that crow\'s answer."\nTo de'

### G8-06: Protocol method dispatch

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 5, 'ANSWER_LEAK_STRING': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'Any crow who can fulfil the stone-drop call may claim membership."\nTo define a p'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'The runtime reads from this ledger whenever the call goes out." To\ndefine a prot'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 6 commas reads as AI-output cadence: 'The\nruntime looks up which crow is present, then runs that crow\'s answer."\nTo de'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, extend it to both String and Long t'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, extend it to both String and Long t'
    - [ANSWER_LEAK_STRING] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — answer string ':string-pace' appears in user_msg

### G8-07: Record implementing protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4, 'HIGH_LENGTH': 1, 'ANSWER_LEAK_STRING': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (defrecord F` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, define a record Falcon that impleme'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (defrecord F` — sentence with 5 commas reads as AI-output cadence: 'Any crow who can fulfil the stone-drop call may claim membership."\nTo define a p'
    - [HIGH_LENGTH] form=`(do (defprotocol Pace (speed [this])) (defrecord F` — user_msg 201 words
    - [ANSWER_LEAK_STRING] form=`(do (defprotocol Pace (speed [this])) (defrecord F` — answer string ':swift' appears in user_msg
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, define a record Heron that implemen'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, define a record Heron that implemen'

### G8-08: Multimethod defmulti

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 5 commas reads as AI-output cadence: 'The runtime reads it, finds the matching chute, and runs that one." To\ndeclare a'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti tag :kind) (defmethod tag :stone [_]` — sentence with 6 commas reads as AI-output cadence: 'To define a multimethod tag that dispatches on the :kind key, add a method for :'

### G8-09: Multimethod defmethod

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 5 commas reads as AI-output cadence: 'To define a multimethod pace that dispatches on :species with methods for both :'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 5 commas reads as AI-output cadence: 'To define a multimethod pace that dispatches on :species with methods for both :'

### G8-10: Multimethod vs protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti show identity) (defmethod show :rabb` — sentence with 5 commas reads as AI-output cadence: 'To define a multimethod show that dispatches on identity with a method for one s'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Show (show [this])) (extend-proto` — sentence with 7 commas reads as AI-output cadence: 'The runtime reads it, finds the matching chute, and runs that one." To\ndefine a '

### G8-11: Protocol vs Java interface

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol IPace (run [this])) (extend-proto` — sentence with 6 commas reads as AI-output cadence: 'The\nruntime looks up which crow is present, then runs that crow\'s answer."\nTo de'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol IPace (run [this])) (extend-proto` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol IPace with method run, extend it to String type, then call '

### G8-12: extend-type on built-in types

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-type` — sentence with 6 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, use extend-type to attach it to Lon'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-type` — sentence with 7 commas reads as AI-output cadence: 'The runtime reads it, finds the matching chute, and runs that one." To\ndefine a '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-type` — sentence with 6 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, use extend-type to attach it to Lon'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-type` — sentence with 6 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, use extend-type to attach it to Str'

### G8-13: this-style vs fn-style

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Named (name-of [this])) (defrecor` — sentence with 5 commas reads as AI-output cadence: 'Any crow who can fulfil the stone-drop call may claim membership."\nTo define a p'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Tagged (tag-of [this])) (defrecor` — sentence with 5 commas reads as AI-output cadence: 'The runtime reads from this ledger whenever the call goes out." To\ndefine a prot'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Tagged (tag-of [this])) (defrecor` — sentence with 5 commas reads as AI-output cadence: 'Any crow who can fulfil the stone-drop call may claim membership."\nTo define a p'

### G8-14: Protocols don't inherit

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — sentence with 6 commas reads as AI-output cadence: 'Any crow who can fulfil the stone-drop call may claim membership."\nTo define two'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — sentence with 6 commas reads as AI-output cadence: 'The runtime reads from this ledger whenever the call goes out." To\ndefine two pr'

### G8-15: derive and isa? — multimethod hierarchy

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 5, 'LOW_GROUNDING': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — sentence with 6 commas reads as AI-output cadence: 'The runtime reads it, finds the matching chute, and runs that one." To\nestablish'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — sentence with 5 commas reads as AI-output cadence: 'To establish a type relationship where ::hare is a type of ::runner, then check '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — sentence with 6 commas reads as AI-output cadence: 'The runtime reads it, finds the matching chute, and runs that one." To\nestablish'
    - [LOW_GROUNDING] form=`(isa? java.lang.Long java.lang.Number)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(isa? java.lang.Long java.lang.Number)` — sentence with 5 commas reads as AI-output cadence: 'The runtime reads it, finds the matching chute, and runs that one." To\ncheck whe'
    - [CLAUSE_STACK_OVERFLOW] form=`(isa? java.lang.String java.lang.Number)` — sentence with 5 commas reads as AI-output cadence: 'The runtime reads it, finds the matching chute, and runs that one." To\ncheck whe'

### G8-16: Abstract design with protocols

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Move (step [this])) (defrecord Fa` — sentence with 5 commas reads as AI-output cadence: 'The runtime reads from this ledger whenever the call goes out." To\ndefine a prot'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Move (step [this])) (defrecord Fa` — sentence with 6 commas reads as AI-output cadence: 'The\nruntime looks up which crow is present, then runs that crow\'s answer."\nTo de'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Move (step [this])) (defrecord Fa` — sentence with 5 commas reads as AI-output cadence: 'Any crow who can fulfil the stone-drop call may claim membership."\nTo define a p'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Sound (cry [this])) (defrecord Fa` — sentence with 5 commas reads as AI-output cadence: 'Any crow who can fulfil the stone-drop call may claim membership."\nTo define a p'

## Grade 9

### G9-01: Immutability as default — review

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4}
    - [CLAUSE_STACK_OVERFLOW] form=`(let [m {:a 1}] (assoc m :b 2) m)` — sentence with 7 commas reads as AI-output cadence: 'To bind a map m, call assoc to add :b 2 to a new map, then return the unchanged '
    - [CLAUSE_STACK_OVERFLOW] form=`(let [v [1 2 3]] (conj v 4) v)` — sentence with 5 commas reads as AI-output cadence: 'To bind a vector v, call conj to add 5 to a new vector, then return the unchange'
    - [CLAUSE_STACK_OVERFLOW] form=`(let [v [1 2 3]] (conj v 4) v)` — sentence with 5 commas reads as AI-output cadence: 'To bind a vector v, call conj to add 9 to a new vector, then return the unchange'
    - [CLAUSE_STACK_OVERFLOW] form=`(let [v [1 2 3]] (conj v 4) v)` — sentence with 5 commas reads as AI-output cadence: 'To bind a vector v, call conj to add 6 to a new vector, then return the unchange'

### G9-02: Why state at all

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — sentence with 7 commas reads as AI-output cadence: 'To construct an atom holding 0 as counter, atomically swap it by applying inc, a'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — sentence with 7 commas reads as AI-output cadence: 'The marks change only when someone scratches — and only as the\nruntime allows." '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def progress (atom :idle)) (reset! progress :` — sentence with 7 commas reads as AI-output cadence: 'The runtime sees to that — no two crows scratch over each other\'s\nmarks." To con'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def progress (atom :idle)) (reset! progress :` — sentence with 7 commas reads as AI-output cadence: 'The runtime sees to that — no two crows scratch over each other\'s\nmarks." To con'

### G9-03: Atom introduction

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'CLAUSE_STACK_OVERFLOW': 6}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 10)) (swap! a + 5) @a)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees to that — no two crows scratch over each other\'s\nmarks." To con'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 10)) (swap! a + 5) @a)` — sentence with 6 commas reads as AI-output cadence: 'If two crows arrive at once, the runtime makes sure only one\nof us completes the'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 10)) (swap! a + 5) @a)` — sentence with 5 commas reads as AI-output cadence: 'To construct an atom holding 10, atomically swap it by applying + to 5, and dere'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom :start)) (reset! a :done) @a)` — sentence with 5 commas reads as AI-output cadence: 'The marks change only when someone scratches — and only as the\nruntime allows." '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom :start)) (reset! a :done) @a)` — sentence with 6 commas reads as AI-output cadence: 'If two crows arrive at once, the runtime makes sure only one\nof us completes the'

### G9-04: Atom CAS semantics

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 5}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees to that — no two crows scratch over each other\'s\nmarks." To con'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — sentence with 5 commas reads as AI-output cadence: 'The marks change only when someone scratches — and only as the\nruntime allows." '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — sentence with 5 commas reads as AI-output cadence: 'The marks change only when someone scratches — and only as the\nruntime allows." '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 5)) (compare-and-set! a 0 99) @a)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees to that — no two crows scratch over each other\'s\nmarks." To con'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 5)) (compare-and-set! a 0 99) @a)` — sentence with 5 commas reads as AI-output cadence: 'The marks change only when someone scratches — and only as the\nruntime allows." '

### G9-05: Watch on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — sentence with 7 commas reads as AI-output cadence: 'The marks change only when someone scratches — and only as the\nruntime allows." '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — sentence with 7 commas reads as AI-output cadence: 'The runtime sees to that — no two crows scratch over each other\'s\nmarks." To con'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — sentence with 7 commas reads as AI-output cadence: 'The runtime sees to that — no two crows scratch over each other\'s\nmarks." To con'

### G9-06: Validator on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — sentence with 5 commas reads as AI-output cadence: 'validator on it, atomically swap by applying inc, and dereference, he composed\na'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — sentence with 5 commas reads as AI-output cadence: 'validator on it, atomically swap by applying inc, and dereference, he composed\na'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — sentence with 5 commas reads as AI-output cadence: 'validator on it, atomically swap by applying inc, and dereference,\nhe composed a'

### G9-07: Ref introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4, 'DOUBLE_PREP': 1, 'LOW_GROUNDING': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 5 commas reads as AI-output cadence: 'To construct a ref holding 0, perform a transactional alter by applying inc insi'
    - [DOUBLE_PREP] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — verb+preposition followed by {place} which already carries its own preposition
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` — sentence with 5 commas reads as AI-output cadence: 'To construct a ref holding 100, perform a transactional ref-set to 7 inside dosy'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` — sentence with 5 commas reads as AI-output cadence: 'To construct a ref holding 100, perform a transactional ref-set to 7 inside dosy'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees to that — no two crows scratch over each other\'s\nmarks." To con'

### G9-08: dosync and alter

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — sentence with 7 commas reads as AI-output cadence: 'If two crows arrive at once, the runtime makes sure only one\nof us completes the'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — sentence with 6 commas reads as AI-output cadence: 'The marks change only when someone scratches — and only as the\nruntime allows." '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — sentence with 6 commas reads as AI-output cadence: 'If two crows arrive at once, the runtime makes sure only one\nof us completes the'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — sentence with 5 commas reads as AI-output cadence: 'To construct a ref holding 10, perform a transactional alter by applying + with '

### G9-09: Ref vs atom

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3, 'LOW_GROUNDING': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 5 commas reads as AI-output cadence: 'To construct an atom holding 0, atomically swap it by applying inc, and derefere'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 5 commas reads as AI-output cadence: 'To construct an atom holding 0, atomically swap it by applying inc, and derefere'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees to that — no two crows scratch over each other\'s\nmarks." To con'
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-10: Agent introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'CLAUSE_STACK_OVERFLOW': 5}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 6 commas reads as AI-output cadence: 'To construct an agent holding 0, asynchronously send inc to it, await its comple'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 9 commas reads as AI-output cadence: 'The count will be there when you signal for it —\nsometimes you have to wait for '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 8 commas reads as AI-output cadence: 'To construct an agent holding 0, asynchronously send inc to it, await its comple'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 5)) (send ag + 10) (await ag) @` — sentence with 8 commas reads as AI-output cadence: 'The runtime makes that\neasier than it sounds." To construct an agent holding 5, '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 5)) (send ag + 10) (await ag) @` — sentence with 6 commas reads as AI-output cadence: 'To construct an agent holding 5, asynchronously send + with 10 to it, await its '

### G9-11: send and send-off

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 9 commas reads as AI-output cadence: 'The count will be there when you signal for it —\nsometimes you have to wait for '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 8 commas reads as AI-output cadence: 'To construct an agent holding 0, use send to asynchronously apply inc, await its'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send-off ag inc) (await ag` — sentence with 8 commas reads as AI-output cadence: 'To construct an agent holding 0, use send-off to asynchronously apply inc, await'

### G9-12: await — synchronizing on agents

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 8 commas reads as AI-output cadence: 'To construct an agent holding 0, asynchronously send inc twice, synchronize with'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 8 commas reads as AI-output cadence: 'The runtime makes that\neasier than it sounds." To construct an agent holding 0, '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 8 commas reads as AI-output cadence: 'To construct an agent holding 0, asynchronously send inc twice, synchronize with'

### G9-13: future introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-15: promise — deliver and deref

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def p (promise)) (deliver p :done) @p)` — sentence with 5 commas reads as AI-output cadence: 'The runtime makes that\neasier than it sounds." To construct a promise, deliver a'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def p (promise)) (deliver p :done) @p)` — sentence with 5 commas reads as AI-output cadence: 'To construct a promise, deliver a completion keyword to it, and dereference to g'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def p (promise)) (deliver p :done) @p)` — sentence with 5 commas reads as AI-output cadence: 'The runtime makes that\neasier than it sounds." To construct a promise, deliver a'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def p (promise)) (deliver p 42) @p)` — sentence with 5 commas reads as AI-output cadence: 'The runtime makes that\neasier than it sounds." To construct a promise, deliver 4'

### G9-17: binding — thread-local

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 6, 'HIGH_LENGTH': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees to that — no two crows scratch over each other\'s\nmarks." To def'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — sentence with 5 commas reads as AI-output cadence: 'To define a dynamic var *p* as 1, use binding to rebind it to 99, and read its v'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — sentence with 6 commas reads as AI-output cadence: 'If two crows arrive at once, the runtime makes sure only one\nof us completes the'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *` — sentence with 7 commas reads as AI-output cadence: 'The marks change only when someone scratches — and only as the\nruntime allows." '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *` — sentence with 7 commas reads as AI-output cadence: 'To define a dynamic var *p* as 1, use binding to rebind it to 99 inside, and rea'
    - [HIGH_LENGTH] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *` — user_msg 205 words

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_PREP': 2}
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def lock (Object.)) (locking lock 42))` — sentence with 5 commas reads as AI-output cadence: 'The marks change only when someone scratches — and only as the\nruntime allows." '
    - [DOUBLE_PREP] form=`(do (def lock (Object.)) (locking lock 42))` — verb+preposition followed by {place} which already carries its own preposition
    - [DOUBLE_PREP] form=`(do (def lock (Object.)) (locking lock 42))` — verb+preposition followed by {place} which already carries its own preposition

## Grade 10

### G10-01: quote, unquote, unquote-splice

- examples: 3
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'LOW_GROUNDING': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'REPL_TRIPLE_VOICE': 2, 'ONLY_SHOOK_HEAD_TIC': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(quote (+ 1 2))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three number' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three number' in a story slot — the actual draws may differ from this fixed count
    - [REPL_TRIPLE_VOICE] form=`'(1 2 3)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three number' in a story slot — the actual draws may differ from this fixed count

### G10-02: syntax-quote

- examples: 2
- variety @ n=50: 1.00
- issues: {'THE_FORM_OVERUSE': 1, 'ONLY_SHOOK_HEAD_TIC': 2}
    - [THE_FORM_OVERUSE] form=`(let [x 10] `(+ ~x ~x))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [ONLY_SHOOK_HEAD_TIC] form=`(let [xs [1 2 3]] `(list ~@xs))` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [ONLY_SHOOK_HEAD_TIC] form=`(let [xs [1 2 3]] `(list ~@xs))` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

### G10-03: defmacro introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'REPL_TRIPLE_VOICE': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg 223 words
    - [REPL_TRIPLE_VOICE] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` — sentence with 5 commas reads as AI-output cadence: 'A rule takes a\n*form* and makes a different *form* — only then does the runtime '

### G10-04: Macro expansion rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(macroexpand-1 '(or a b))` — sentence with 5 commas reads as AI-output cadence: 'You\nwrite the rule once, and any drop-order that calls it gets rewritten\non the '

### G10-06: when and when-not as macros

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(when true 1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'You\nwrite the rule once, and any drop-order that calls it gets rewritten\non the '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when-not false :ok)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':ok',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when-not false :ok)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':ok',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when-not false :ok)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':ok',), resolution doesn't close the loop)

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 2, 'CLAUSE_STACK_OVERFLOW': 3, 'ANSWER_LEAK': 1, 'LOW_GROUNDING': 1}
    - [CONCEPT_AS_VERB] form=`(-> 5 inc inc inc)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CLAUSE_STACK_OVERFLOW] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — sentence with 7 commas reads as AI-output cadence: 'To thread a vector through filter, map, and reduce using thread-last, he compose'
    - [ANSWER_LEAK] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — answer 8 in narrative
    - [CLAUSE_STACK_OVERFLOW] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — sentence with 5 commas reads as AI-output cadence: 'To thread a vector through filter, map, and reduce using thread-last, she scratc'
    - [CLAUSE_STACK_OVERFLOW] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — sentence with 5 commas reads as AI-output cadence: 'To thread a vector through filter, map, and reduce using thread-last, she scratc'
    - [CONCEPT_AS_VERB] form=`(macroexpand '(-> x f g))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G10-08: Macro vs fn

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — sentence with 5 commas reads as AI-output cadence: 'You\nwrite the rule once, and any drop-order that calls it gets rewritten\non the '

### G10-09: Hygiene and gensym

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — sentence with 5 commas reads as AI-output cadence: 'You\nwrite the rule once, and any drop-order that calls it gets rewritten\non the '
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — sentence with 5 commas reads as AI-output cadence: 'You\nwrite the rule once, and any drop-order that calls it gets rewritten\non the '

### G10-10: Anaphoric macros are confusing

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if-let [x 7] (* x x) 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(if-let [x 7] (* x x) 0)` — sentence with 5 commas reads as AI-output cadence: 'You\nwrite the rule once, and any drop-order that calls it gets rewritten\non the '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if-let [x 7] (* x x) 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if-let [x 7] (* x x) 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)

### G10-11: Reader macros overview

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(* % %) 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(* % %) 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(* % %) 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(#(* % %) 6)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'
    - [STORY_RESOLUTION_NO_DRAWN] form=`[1 #_ 2 3]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`[1 #_ 2 3]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G10-12: Tagged literals

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(inst? #inst "2024-01-01")` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'
    - [CLAUSE_STACK_OVERFLOW] form=`(inst? #inst "2024-01-01")` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(uuid? #uuid "00000000-0000-0000-0000-000000000000` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('00000000', '-0000', '-0000'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(uuid? #uuid "00000000-0000-0000-0000-000000000000` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('00000000', '-0000', '-0000'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(uuid? #uuid "00000000-0000-0000-0000-000000000000` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(uuid? #uuid "00000000-0000-0000-0000-000000000000` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('00000000', '-0000', '-0000'), resolution doesn't close the loop)

### G10-13: Data readers and EDN extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'ONLY_SHOOK_HEAD_TIC': 1}
    - [ONLY_SHOOK_HEAD_TIC] form=`(clojure.edn/read-string "[:a :b :c]")` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

### G10-14: eval (the function)

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 6, 'REPL_TRIPLE_VOICE': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(eval '(+ 1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval '(+ 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [REPL_TRIPLE_VOICE] form=`(eval '(+ 1 2 3))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval '(+ 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(eval '(+ 1 2 3))` — sentence with 5 commas reads as AI-output cadence: 'You\nwrite the rule once, and any drop-order that calls it gets rewritten\non the '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval '(+ 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G10-15: When not to write a macro

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "prefer fn unless you must shape syntax" (map ` — sentence with 5 commas reads as AI-output cadence: 'You\nwrite the rule once, and any drop-order that calls it gets rewritten\non the '

### G10-16: Macro pattern library

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 2, 'ANSWER_LEAK_STRING': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':slow-and-steady'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':slow-and-steady'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':slow-and-steady'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — sentence with 5 commas reads as AI-output cadence: 'You\nwrite the rule once, and any drop-order that calls it gets rewritten\non the '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — sentence with 5 commas reads as AI-output cadence: 'You\nwrite the rule once, and any drop-order that calls it gets rewritten\non the '
    - [ANSWER_LEAK_STRING] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — answer string ':slow' appears in user_msg

## Grade 11

### G11-01: JVM vs CLR vs JS vs Python (host overview)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HEDGING_NEAR_FORM] form=`(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScr` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScr` — sentence with 5 commas reads as AI-output cadence: 'Featherdark the crow, patient as the water rose, walked to the slate and began t'

### G11-02: Method call syntax

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(.toUpperCase "abc")` — sentence with 5 commas reads as AI-output cadence: 'Glint the crow, unhurried, form after form, found a different pitcher atop the h'
    - [CLAUSE_STACK_OVERFLOW] form=`(.startsWith "hare-tortoise" "hare")` — sentence with 5 commas reads as AI-output cadence: "The runtime moves a stone across the boundary, calls\nthe human's method, and bri"
    - [CLAUSE_STACK_OVERFLOW] form=`(.startsWith "hare-tortoise" "hare")` — sentence with 5 commas reads as AI-output cadence: "The runtime moves a stone across the boundary, calls\nthe human's method, and bri"
    - [STORY_RESOLUTION_NO_DRAWN] form=`(. "abc" toUpperCase)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(. "abc" toUpperCase)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(. "abc" toUpperCase)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)

### G11-03: Static method call

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(Math/max 3 9)` — sentence with 5 commas reads as AI-output cadence: "The runtime moves a stone across the boundary, calls\nthe human's method, and bri"

### G11-04: Field access

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(count "tortoise")` — sentence with 5 commas reads as AI-output cadence: "The runtime moves a stone across the boundary, calls\nthe human's method, and bri"
    - [CLAUSE_STACK_OVERFLOW] form=`(count "tortoise")` — sentence with 5 commas reads as AI-output cadence: "The runtime moves a stone across the boundary, calls\nthe human's method, and bri"

### G11-05: Import form

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "import is a top-of-file ns clause" :studied)` — sentence with 5 commas reads as AI-output cadence: 'Indigo the crow, watching the level lift, drop by drop, had already written\nimpo'

### G11-06: new and dot-construct

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'ANSWER_LEAK_STRING': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(String. "go")` — sentence with 5 commas reads as AI-output cadence: 'Galena the crow, watching the level lift, drop by drop, found a different pitche'
    - [ANSWER_LEAK_STRING] form=`(new String "jump")` — answer string 'jump' appears in user_msg

### G11-07: Arrays

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a (int-array [10 20 30])] (aget a 1))` — sentence with 5 commas reads as AI-output cadence: 'Thermal the crow, watching the level lift, drop by drop, found a different pitch'
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a (int-array [1 2 3])] (alength a))` — sentence with 5 commas reads as AI-output cadence: "The runtime moves a stone across the boundary, calls\nthe human's method, and bri"

### G11-08: Type hints

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'LOW_GROUNDING': 1, 'PROCEDURAL_OPENER': 1, 'METAPHOR_DISAPPEARS': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(let [^String s "abc"] (.toUpperCase s))` — sentence with 5 commas reads as AI-output cadence: 'Float the crow, trusting the process, stone after stone, found a different pitch'
    - [LOW_GROUNDING] form=`(do "type hints are metadata that guide compilatio` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PROCEDURAL_OPENER] form=`(do "type hints are metadata that guide compilatio` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    - [METAPHOR_DISAPPEARS] form=`(do "type hints are metadata that guide compilatio` — user_msg has none of the fable's primary metaphor nouns (pitcher, water, pebble, stone...)

### G11-11: cljs / JavaScript interop

- examples: 2
- variety @ n=50: 1.00
- issues: {'META_FILLER_RESOLUTION': 1}
    - [META_FILLER_RESOLUTION] form=`(do "(js/console.log x) calls a JS global; (.-foo ` — user_msg uses generic 'returned exactly' / 'settled with certainty' filler — describe what actually came back, not just that something did

### G11-12: Basilisp overview (Python host)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HEDGING_NEAR_FORM] form=`(do "basilisp is a Clojure-like Lisp implemented o` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "basilisp is a Clojure-like Lisp implemented o` — sentence with 5 commas reads as AI-output cadence: 'Trill the crow, steady in the stone-by-stone approach, walked to the slate and b'

### G11-14: Debugging host leaks

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'PROCEDURAL_OPENER': 2, 'METAPHOR_DISAPPEARS': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(do "host stack traces leak through interop; learn` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PROCEDURAL_OPENER] form=`(do "host stack traces leak through interop; learn` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    - [METAPHOR_DISAPPEARS] form=`(do "host stack traces leak through interop; learn` — user_msg has none of the fable's primary metaphor nouns (pitcher, water, pebble, stone...)
    - [LOW_GROUNDING] form=`(do "host stack traces leak through interop; learn` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PROCEDURAL_OPENER] form=`(do "host stack traces leak through interop; learn` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    - [METAPHOR_DISAPPEARS] form=`(do "host stack traces leak through interop; learn` — user_msg has none of the fable's primary metaphor nouns (pitcher, water, pebble, stone...)

## Grade 12

### G12-01: Transducers introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'NUMERAL_LIST_IN_GOAL': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] (map inc) [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To use the map-inc transducer with into to increment the vector containing 1, 2,'
    - [NUMERAL_LIST_IN_GOAL] form=`(into [] (filter even?) [1 2 3 4 5])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(into [] (filter even?) [1 2 3 4 5])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(into [] (filter even?) [1 2 3 4 5])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing

### G12-02: Transducer composition

- examples: 2
- variety @ n=50: 1.00
- issues: {'NUMERAL_LIST_IN_GOAL': 6, 'CLAUSE_STACK_OVERFLOW': 5}
    - [NUMERAL_LIST_IN_GOAL] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — sentence with 8 commas reads as AI-output cadence: 'Ash the crow shook\nhis head and went on with the work: to\ncompose map-inc and fi'
    - [NUMERAL_LIST_IN_GOAL] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — sentence with 5 commas reads as AI-output cadence: 'Puzzle the crow, trusting the process, stone after stone, held two decision-rule'
    - [NUMERAL_LIST_IN_GOAL] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — goal_text contains 6 numerals across 6 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing

### G12-03: into with a transducer (xform)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 2}
    - [HIGH_LENGTH] form=`(into #{} (map inc) [1 2 3])` — user_msg 208 words
    - [CLAUSE_STACK_OVERFLOW] form=`(into #{} (map inc) [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To use the map-inc transducer with into to create a set from the incremented ele'
    - [CLAUSE_STACK_OVERFLOW] form=`(into #{} (map inc) [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'Cowl the crow shook\nhis head and went on with the work: to\nuse the map-inc trans'

### G12-04: core.async introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HEDGING_NEAR_FORM] form=`(do "(chan), (go ...), (<! ...), (>! ...) form the` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "(chan), (go ...), (<! ...), (>! ...) form the` — sentence with 5 commas reads as AI-output cadence: 'Vane the crow, patient as the water rose, walked to the slate and began to\nwrite'

### G12-05: Channels and pipelines

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "pipe, mult, mix, pipeline-async route values ` — sentence with 6 commas reads as AI-output cadence: 'Halfway through the race, Azure the crow, preening at the thought of knowing, st'
    - [CLAUSE_STACK_OVERFLOW] form=`(do "pipelines transform streams of values channel` — sentence with 5 commas reads as AI-output cadence: 'Indigo the crow, watching the level lift, drop by drop, had already written\nthe '

### G12-06: clojure.spec

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 2}
    - [HEDGING_NEAR_FORM] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [HEDGING_NEAR_FORM] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value

### G12-07: Spec generators

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HEDGING_NEAR_FORM] form=`(do "s/exercise produces sample inputs for a spec"` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "s/exercise produces sample inputs for a spec"` — sentence with 6 commas reads as AI-output cadence: 'Yawp the crow, deliberate, unhurried by the rising sun, walked to the slate and '

### G12-11: Leiningen project.clj

- examples: 2
- variety @ n=50: 1.00
- issues: {'META_FILLER_RESOLUTION': 1}
    - [META_FILLER_RESOLUTION] form=`(do "project.clj declares :dependencies, :main, :p` — user_msg uses generic 'returned exactly' / 'settled with certainty' filler — describe what actually came back, not just that something did

### G12-12: deps.edn projects

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HEDGING_NEAR_FORM] form=`(do "deps.edn declares :deps and :aliases for the ` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "deps.edn declares :deps and :aliases for the ` — sentence with 5 commas reads as AI-output cadence: 'Trill the crow, steady in the stone-by-stone approach, walked to the slate and b'

### G12-13: Aliases and tools

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "aliases compose extra paths, deps, and main o` — sentence with 5 commas reads as AI-output cadence: 'Halfway through the race, Nightshade the crow, with a confident tilt of the head'

### G12-15: Datomic / XTDB (datalog db brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'META_FILLER_RESOLUTION': 1, 'CLAUSE_STACK_OVERFLOW': 3, 'HEDGING_NEAR_FORM': 2}
    - [META_FILLER_RESOLUTION] form=`(do "Datomic and XTDB are immutable, time-aware da` — user_msg uses generic 'returned exactly' / 'settled with certainty' filler — describe what actually came back, not just that something did
    - [CLAUSE_STACK_OVERFLOW] form=`(do "Datomic and XTDB are immutable, time-aware da` — sentence with 5 commas reads as AI-output cadence: 'Banking the crow, letting the count rise on its own, had already written\nthe fam'
    - [HEDGING_NEAR_FORM] form=`(do "queries are written in datalog over EDN-shape` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "queries are written in datalog over EDN-shape` — sentence with 5 commas reads as AI-output cadence: 'Cloudlark the crow, dropping each stone with careful attention, walked to the sl'
    - [HEDGING_NEAR_FORM] form=`(do "queries are written in datalog over EDN-shape` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "queries are written in datalog over EDN-shape` — sentence with 5 commas reads as AI-output cadence: 'Skybound the crow, letting the count rise on its own, walked to the slate and be'

### G12-17: Library design patterns

- examples: 3
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HEDGING_NEAR_FORM] form=`(do "small public API surface, plain data inputs, ` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "small public API surface, plain data inputs, ` — sentence with 5 commas reads as AI-output cadence: 'Gust the crow, calm and methodical, walked to the slate and began to\nwrite the m'

---

## Summary

### Issue counts (across all examples × 3 records)

- **CLAUSE_STACK_OVERFLOW**: 265
- **STORY_RESOLUTION_NO_DRAWN**: 57
- **LOW_GROUNDING**: 52
- **NUMERAL_LIST_IN_GOAL**: 48
- **CONCEPT_AS_VERB**: 29
- **FORM_DISPLAY_AND_FORM_NOUN**: 18
- **REPL_TRIPLE_VOICE**: 18
- **PARAGRAPH_FRAGMENTATION**: 15
- **NARRATIVE_NUMERAL_HARDCODE**: 15
- **ONLY_SHOOK_HEAD_TIC**: 14
- **HEDGING_NEAR_FORM**: 11
- **ANSWER_LEAK_STRING**: 10
- **THE_FORM_OVERUSE**: 8
- **ANSWER_LEAK**: 7
- **STRING_AS_CHAR_MISCLAIM**: 6
- **HIGH_LENGTH**: 6
- **REPEATED_OPENER_FRAGMENT**: 4
- **EXPECTED_META_PHRASE**: 3
- **DOUBLE_PREP**: 3
- **PROCEDURAL_OPENER**: 3
- **METAPHOR_DISAPPEARS**: 3
- **META_FILLER_RESOLUTION**: 3
- **BAD_PLACE_PREP**: 2
- **FORM_LEAK**: 1

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 45 | — |
| 2 | 22 | 88 | 78 | — |
| 3 | 18 | 31 | 33 | — |
| 4 | 20 | 39 | 46 | — |
| 5 | 22 | 39 | 87 | — |
| 6 | 16 | 33 | 17 | — |
| 7 | 18 | 36 | 41 | — |
| 8 | 16 | 31 | 49 | — |
| 9 | 18 | 34 | 72 | — |
| 10 | 16 | 36 | 65 | — |
| 11 | 14 | 29 | 30 | — |
| 12 | 18 | 37 | 38 | — |

### Sample issues by severity

#### FORM_DISPLAY_AND_FORM_NOUN

- `G1-01` (form `"hello"`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    It had been a long, dry summer, and the rivers had pulled back from their banks in a slow and patient retreat.

A small audience of meadow birds had perched on the rim of a tall
pitcher in the garden to watch Soothe the crow attempt to outwit
Pinion the crow at reading the REPL. The day was hot, the...
    ```
- `G1-01` (form `nil`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    Drought has its own quiet way of teaching the difference between thirst and the right answer to thirst.

A small audience of meadow birds had perched on the rim of a tall
pitcher near the garden to watch Brand the crow attempt to outwit
Windrider the crow at reading the REPL. The day was hot, the wa...
    ```
- `G1-02` (form `12345`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    The farmstead had stored what it could, but the heat was honest and the water was patient with no one.

A small audience of meadow birds had perched on the rim of a tall
pitcher near the meadow to watch Pipe the crow attempt to outwit
Malachite the crow at reading the REPL. The day was hot, the wate...
    ```
- `G1-05` (form `true`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    It had been a long, dry summer, and the rivers had pulled back from their banks in a slow and patient retreat.

A small audience of meadow birds had perched on the rim of a tall
pitcher near the garden to watch Dusk the crow attempt to outwit
Emblem the crow at reading the REPL. The day was hot, the...
    ```
- `G1-05` (form `true`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    On the rim of a long-shadowed pitcher, a thirsty bird considered what it had and what it lacked.

A small audience of meadow birds had perched on the rim of a tall
pitcher at the market to watch Cobalt the crow attempt to outwit
Cackle the crow at reading the REPL. The day was hot, the water
inside ...
    ```

#### REPEATED_OPENER_FRAGMENT

- `G1-07` (form `(= :hare :hare)`): opener fragment 'at the edge of the orchard' also appears later in user_msg
    ```
    The orchard at the edge of the orchard had grown quiet in the heat, and Plume was the only sound at midday.

Whisperer the crow chalked a wager on a smooth round pebble at the edge of the orchard: whoever
predicted the result of `(= :wolf :wolf)` would drop his pebble
in the pitcher first. The water...
    ```
- `G2-05` (form `(mod 17 5)`): opener fragment 'at the edge of the hilltop' also appears later in user_msg
    ```
    Glint was no fool, and at the edge of the hilltop the day demanded thinking rather than complaining.

Glint the crow, letting the count rise on its own, arranged a small heap of smooth
stones at the edge of the hilltop, careful with the count. The day was hot and the
water was low; the heap had to r...
    ```
- `G2-15` (form `(if "" 1 0)`): opener fragment 'the pitcher near the orchard' also appears later in user_msg
    ```
    Word had it that Mount had flown over three valleys before finding the pitcher near the orchard.

Mutter the crow swooped toward the pitcher near the orchard, with a confident tilt of the head, certain
the gate would swing open. Mount the crow watched: the only way to know
which way the gate swings ...
    ```
- `G7-07` (form `(do (assert (= 1 1)) 1)`): opener fragment 'the pitcher near the farm' also appears later in user_msg
    ```
    Word had it that Thermal had flown over three valleys before finding the pitcher near the farm.

Thermal the crow, watching the level lift, drop by drop, spread a patch of soft moss beneath
the pitcher near the farm — the day was hot, the throat was narrow, and any
pebble flung wrong without a cushi...
    ```

#### STRING_AS_CHAR_MISCLAIM

- `G1-08` (form `\space`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    It had been a long, dry summer, and the rivers had pulled back from their banks in a slow and patient retreat.

At the foot of a tall pitcher at the edge of the orchard, Cloudshroud the crow sketched a small
wager into the dry dust: whoever guessed the result of `"feather"`
first would claim the coo...
    ```
- `G1-08` (form `\space`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    by the meadow, where the orchard meets the well, an old clay pitcher had stood for as long as anyone could remember.

Halfway to the pitcher, Quirk the crow, preening at the thought of knowing, stopped at the edge of the meadow
and refused to take another step until someone could prove what the
form...
    ```
- `G1-08` (form `\space`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    Some problems cannot be hurried; they only respond to the slow addition of small things.

At the foot of a tall pitcher on the farm, Pitch the crow sketched a small
wager into the dry dust: whoever guessed the result of `"feather"`
first would claim the cool water lying low at the bottom. The throat...
    ```
- `G1-08` (form `\T`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    Buzz arrived near the garden with no plan but a sharp eye and a willingness to take small steps.

Buzz the crow had been trying to teach Sigil the crow how the REPL
works. The day was hot and the water in the nearby pitcher far below
the narrow rim — a fitting backdrop for a lesson about patience.
"...
    ```
- `G1-08` (form `\T`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    in the village, where the heat shimmered above the stones, Inkwell began the slow business of solving thirst.

Inkwell the crow, patient as the water rose, had been keeping a small leather
notebook of every form he had successfully evaluated —
each page like a pebble in the pitcher's growing pile, r...
    ```

#### ONLY_SHOOK_HEAD_TIC

- `G1-09` (form `(symbol? 'hare)`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    On the rim of a long-shadowed pitcher, a thirsty bird considered what it had and what it lacked.

Parchment the crow, with a confident tilt of the head, mistook the chalk mark on the stone
for the stone itself. "It says crow, so the value must be the
crow!" Soar the crow only shook her head: the
mar...
    ```
- `G1-11` (form `(+    1    2)`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    There was once a Crow who had flown a great distance and found nothing in any pond worth dipping a beak.

Cloudshroud the crow, head tilted confidently to one side, glanced at the pitcher-notations and
called out what she thought they would do without paying
attention to the conventions of how they ...
    ```
- `G1-12` (form `(* (+ 1 2) 3)`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    Umbra arrived on the road with no plan but a sharp eye and a willingness to take small steps.

Jet the crow, with a self-satisfied beak-click, glanced at the pitcher-notations and
called out what he thought they would do without paying
attention to the conventions of how they were scratched.
Umbra t...
    ```
- `G1-12` (form `(* (+ 1 2) 3)`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    Cobalt arrived at the edge of the hilltop with no plan but a sharp eye and a willingness to take small steps.

Cipherwing the crow, with a self-satisfied beak-click, glanced at the pitcher-notations and
called out what he thought they would do without paying
attention to the conventions of how they ...
    ```
- `G1-17` (form `42`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    In a long-dry season, Parchment found the pitcher by the garden and began to consider it carefully.

Cloudshroud the crow, ruffling up with certainty, glanced at the pitcher-notations and
called out what he thought they would do without paying
attention to the conventions of how they were scratched....
    ```

#### CLAUSE_STACK_OVERFLOW

- `G1-09` (form `(= 'hare 'hare)`): sentence with 5 commas reads as AI-output cadence: "Quoting tells the runtime: don't evaluate this, just hand\nit back as the shape i"
    ```
    The drought had reached even along the road, and Pipe flew in slow circles searching for water.

"To talk about the form itself rather than evaluating it,"
Pipe the crow, calm and methodical, said, "you mark the form with chalk in front.
Quoting tells the runtime: don't evaluate this, just hand
it b...
    ```
- `G1-10` (form `42 ;; the answer`): sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'
    ```
    Stormcaw circled twice at the market before settling on the rim of the old clay jar, eyes on the water below.

"A form is what's actually there on the pitcher's clay,"
Stormcaw the crow, letting the count rise on its own, said, "after the conventions of writing and
reading have done their work. The ...
    ```
- `G1-10` (form `42 ;; the answer`): sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'
    ```
    There was a pitcher and there was a thirst, and between them lay a question that asked for thought rather than force.

"A form is what's actually there on the pitcher's clay,"
Circle the crow, watching the level lift, drop by drop, said, "after the conventions of writing and
reading have done their ...
    ```
- `G1-11` (form `(+
  1
  2)`): sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'
    ```
    The orchard had not seen a real rain in weeks, and even the lavender stood with its head bowed.

"A form is what's actually there on the pitcher's clay,"
Nightshade the crow, dropping each stone with careful attention, said, "after the conventions of writing and
reading have done their work. The run...
    ```
- `G1-12` (form `(+ 2 3)`): sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'
    ```
    at the edge of the meadow, where the orchard meets the well, an old clay pitcher had stood for as long as anyone could remember.

"A form is what's actually there on the pitcher's clay,"
Trill the crow, steady in the stone-by-stone approach, said, "after the conventions of writing and
reading have d...
    ```

#### EXPECTED_META_PHRASE

- `G1-11` (form `(+    1    2)`): user_msg uses 'the expected X' meta-language — describes the answer in graders'-vocabulary instead of letting the runtime's return speak for itself
    ```
    Whistle circled twice on the farm before settling on the rim of the old clay jar, eyes on the water below.

Korvus scratched a stone-drop form on the market pitcher's clay, pressing extra gaps between each token — wide spaces separating the operator from both stone-counts on the rim.

He needed to c...
    ```
- `G1-18` (form `(+ 1 2)`): user_msg uses 'the expected X' meta-language — describes the answer in graders'-vocabulary instead of letting the runtime's return speak for itself
    ```
    It was the kind of summer that turned every shaded stone into a small kindness.

Sable spread a patch of soft moss on the ground beneath the garden pitcher before dropping any stone — a safety pad in place, ready to catch any mis-drop without harm.

Sable needed to confirm that a well-formed stone-d...
    ```
- `G3-09` (form `(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))`): user_msg uses 'the expected X' meta-language — describes the answer in graders'-vocabulary instead of letting the runtime's return speak for itself
    ```
    A row of pebbles lay at the foot of the wall, sun-warmed, unremarkable, and just heavy enough.

Sable pressed add3 into the village pitcher's rim alongside a three-slot recipe: accept a, b, c, then sum them — carved deep and permanent.

Sable wanted to call add3 with the drawn counts and watch the w...
    ```

#### PARAGRAPH_FRAGMENTATION

- `G1-13` (form `(- 20 7)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    Dimsky alighted on the rim of a jar by the farm and peered down at the small dark gleam below.

Korvus counted twenty smooth stones piled on the road-side pitcher's rim, then moved seven to one side, studying the smaller heap that remained before submitting the form.

He needed the runtime to confir...
    ```
- `G1-13` (form `(- 20 7)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    When the cisterns ran shallow, even the cleverest creatures had to learn the patience of small additions.

Korvus counted twenty smooth stones piled on the road-side pitcher's rim, then moved seven to one side, studying the smaller heap that remained before submitting the form.

He needed the runtim...
    ```
- `G2-05` (form `(rem 17 5)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    Some problems cannot be hurried; they only respond to the slow addition of small things.

Sable had seventeen acorns at the village and pouches of five. After filling as many pouches as possible she wanted to know how many acorns spilled out as the leftover.

She needed the exact leftover count afte...
    ```
- `G2-06` (form `(inc 0)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    The orchard at the edge of the garden had grown quiet in the heat, and Stoop was the only sound at midday.

Sable stood at the empty road pitcher with no stones inside. She held a single stone in her talon and wanted to know the new count after her first drop.

She needed the count after dropping on...
    ```
- `G2-06` (form `(inc -1)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    Sharp had flown all morning in the meadow without finding so much as a damp leaf to rest a beak against.

Caw had a deficit of one at the village pitcher — one below empty. She added a single stone and wanted to know whether the count climbed back to zero.

She needed to know whether adding one ston...
    ```

#### CONCEPT_AS_VERB

- `G1-15` (form `(= 1 1)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    near the road, where the orchard meets the well, an old clay pitcher had stood for as long as anyone could remember.

"You can't tell which way the gate will swing by guessing,"
Banking the crow, steady in the stone-by-stone approach, said. "You bring the form to the gate, the runtime
checks it, and...
    ```
- `G1-15` (form `(= :hare :hare)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    It was the kind of summer that turned every shaded stone into a small kindness.

"You can't tell which way the gate will swing by guessing,"
Smoke the crow, letting the count rise on its own, said. "You bring the form to the gate, the runtime
checks it, and the gate gives the only answer that matter...
    ```
- `G1-15` (form `(= :hare :hare)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    Soot alighted on the rim of a jar along the road and peered down at the small dark gleam below.

"You can't tell which way the gate will swing by guessing,"
Soot the crow, unhurried, form after form, said. "You bring the form to the gate, the runtime
checks it, and the gate gives the only answer tha...
    ```
- `G1-15` (form `(= :hare :tortoise)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    The kitchen garden had been lovingly kept, but the sun that year had been merciless and constant.

"You can't tell which way the gate will swing by guessing,"
Loft the crow, trusting the process, stone after stone, said. "You bring the form to the gate, the runtime
checks it, and the gate gives the ...
    ```
- `G1-15` (form `(= :hare :tortoise)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    The water sat at the bottom of the jar, deep enough to glimpse and far enough to tantalize.

"You can't tell which way the gate will swing by guessing,"
Currents the crow, deliberate, unhurried by the rising sun, said. "You bring the form to the gate, the runtime
checks it, and the gate gives the on...
    ```

#### LOW_GROUNDING

- `G1-15` (form `(= 1 1)`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    Thermal arrived near the road with no plan but a sharp eye and a willingness to take small steps.

Caw held two unmarked stones up at the pitcher's mouth in the village, one in each talon, both carrying the count 0. She set them side by side at the dual-gate check.

Only if both gate-arms confirmed ...
    ```
- `G2-10` (form `(* 2 2 2)`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    The kitchen garden had been lovingly kept, but the sun that year had been merciless and constant.

Korvus scratched three tallies of two into the pitcher's rim at the farm, stacking each layer on the product of the last. He wanted the final compounded count from three doublings.

He needed the resul...
    ```
- `G2-13` (form `(and true true)`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    On the rim of a long-shadowed pitcher, a thirsty bird considered what it had and what it lacked.

Korvus stood at the pitcher's mouth on the road, two gate-arms stretched across it. Both arms were raised open. He needed to know whether the path through both gates was clear.

He needed the final verd...
    ```
- `G2-13` (form `(and true true)`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    In a year when the wells ran low, a single jar of water was a small kingdom unto itself.

Korvus stood at the pitcher's mouth on the road, two gate-arms stretched across it. Both arms were raised open. He needed to know whether the path through both gates was clear.

He needed the final verdict only...
    ```
- `G2-14` (form `(not true)`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    The orchard had not seen a real rain in weeks, and even the lavender stood with its head bowed.

Caw found the gate-arm above the pitcher fully raised open at the meadow. She wanted to know what the pitcher said about the opposite of that state — the gate flipped.

She needed the inverted reading: i...
    ```

#### REPL_TRIPLE_VOICE

- `G1-17` (form `42`): user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    In a long-dry season, Parchment found the pitcher by the garden and began to consider it carefully.

Cloudshroud the crow, ruffling up with certainty, glanced at the pitcher-notations and
called out what he thought they would do without paying
attention to the conventions of how they were scratched....
    ```
- `G1-17` (form `42`): user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    On the rim of a long-shadowed pitcher, a thirsty bird considered what it had and what it lacked.

"There are conventions for how the runtime *reads* a form,"
Twilight the crow, dropping each stone with careful attention, said: "what counts as one token, what's just
spacing, what gets ignored, what g...
    ```
- `G1-17` (form `42`): user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    In a year when the wells ran low, a single jar of water was a small kingdom unto itself.

"A form is what's actually there on the pitcher's clay,"
Pyrite the crow, letting the count rise on its own, said, "after the conventions of writing and
reading have done their work. The runtime sees the cleane...
    ```
- `G4-01` (form `[]`): user_msg mentions 'REPL' 4 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    An old pitcher of glazed clay sat by the garden wall, half-empty and entirely useless to anyone too proud to think.

Caw arrived at the pitcher in the orchard before any stones had been gathered. The clay lip was bare, no pile laid out, no stones waiting.

She needed to show the REPL an empty stone-...
    ```
- `G4-01` (form `[]`): user_msg mentions 'REPL' 4 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    When Trill landed by the garden wall, she saw the water and saw the distance, and stood very still.

Caw arrived at the pitcher in the orchard before any stones had been gathered. The clay lip was bare, no pile laid out, no stones waiting.

She needed to show the REPL an empty stone-pile — a reserve...
    ```

#### NARRATIVE_NUMERAL_HARDCODE

- `G2-01` (form `(+ 1 2 3 4 5 6 7 8 9 10)`): parametric example has hard-coded English numeral 'Ten stones' in a story slot — the actual draws may differ from this fixed count
    ```
    along the road, where the orchard meets the well, an old clay pitcher had stood for as long as anyone could remember.

Korvus lined the stones along the pitcher's rim at the road, each numbered in order from one to ten. He wanted a single total for all ten before the sun moved.

He needed the accumu...
    ```
- `G2-01` (form `(+ 1 2 3 4 5 6 7 8 9 10)`): parametric example has hard-coded English numeral 'Ten stones' in a story slot — the actual draws may differ from this fixed count
    ```
    near the farm, where the heat shimmered above the stones, Mount began the slow business of solving thirst.

Korvus lined the stones along the pitcher's rim at the road, each numbered in order from one to ten. He wanted a single total for all ten before the sun moved.

He needed the accumulated sum o...
    ```
- `G2-01` (form `(+ 1 2 3 4 5 6 7 8 9 10)`): parametric example has hard-coded English numeral 'Ten stones' in a story slot — the actual draws may differ from this fixed count
    ```
    On the rim of a long-shadowed pitcher, a thirsty bird considered what it had and what it lacked.

Arc the crow, unhurried, form after form, arranged a small heap of smooth
stones by the village, careful with the count. The day was hot and the
water was low; the heap had to rise enough to drink, no f...
    ```
- `G2-18` (form `(count '(1 2 3))`): parametric example has hard-coded English numeral 'three integers' in a story slot — the actual draws may differ from this fixed count
    ```
    The drought had reached even by the market, and Tempest flew in slow circles searching for water.

"A chalk mark can be carried from stone to stone," Tempest the crow, calm and methodical, explained, "passed hand to hand, written again. The mark itself is
just a shape; the value it names is separate...
    ```
- `G2-18` (form `(count '(1 2 3))`): parametric example has hard-coded English numeral 'three integers' in a story slot — the actual draws may differ from this fixed count
    ```
    It had been a long, dry summer, and the rivers had pulled back from their banks in a slow and patient retreat.

"A chalk mark can be carried from stone to stone," Skreigh the crow, patient as the water rose, explained, "passed hand to hand, written again. The mark itself is
just a shape; the value i...
    ```

#### ANSWER_LEAK

- `G2-19` (form `(+ 99999999999 1)`): answer 100000000000 in narrative
    ```
    The orchard at the farm had grown quiet in the heat, and Cipher was the only sound at midday.

Gale the crow eyed the heap, with a self-satisfied beak-click, and called out a guess
about how many stones could be dropped before the water rose high
enough, without bothering to count. Cipher the crow s...
    ```
- `G3-04` (form `(let [a 2 b 3 c 4] (+ a b c))`): answer 9 in narrative
    ```
    On a long afternoon when even the bees had grown slow, a thirsty bird settled on the rim of a clay vessel.

"Watch the wing carefully," Drift the crow said near the market.
"While the form's stretch runs, the wing is closed and
the binding is safe." To bind a to 5, b to 9, c to 9, and add them, she
...
    ```
- `G3-04` (form `(let [a 2 b 3 c 4] (+ a b c))`): answer 9 in narrative
    ```
    A row of pebbles lay at the foot of the wall, sun-warmed, unremarkable, and just heavy enough.

Sage the crow, unhurried, form after form, patted the feathers of one wing.
"Whatever I tuck under a wing is in force only while the form runs,"
she said, "and only for the form that names the binding.
Th...
    ```
- `G3-09` (form `(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))`): answer 6 in narrative
    ```
    It was the kind of summer that turned every shaded stone into a small kindness.

Cunning the crow, trusting the process, stone after stone, held up a smooth stone and scratched
a step-by-step sequence into the pitcher's clay rim. "Drop-orders in
Clojure are like this," she said: "the smooth stones g...
    ```
- `G5-22` (form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n)`): answer 120 in narrative
    ```
    near the village, where the heat shimmered above the stones, Buffet began the slow business of solving thirst.

Caw stood at the pitcher's rim in the hilltop field, a circuit chalked beneath her feet: start with n=5 and accumulator=1. Each lap, multiply the accumulator by n, step n down by one — loo...
    ```

#### HIGH_LENGTH

- `G3-03` (form `(let [x 3] (+ x 1))`): user_msg 210 words
    ```
    Vane circled twice at the farm before settling on the rim of the old clay jar, eyes on the water below.

Korvus arrived at the tall clay pitcher in the orchard, three smooth stones from the morning's count in mind. Before dropping any, he tucked the count of three under his left wing, close and name...
    ```
- `G3-03` (form `(let [x 3] (+ x 1))`): user_msg 208 words
    ```
    The orchard had not seen a real rain in weeks, and even the lavender stood with its head bowed.

Korvus arrived at the tall clay pitcher in the orchard, three smooth stones from the morning's count in mind. Before dropping any, he tucked the count of three under his left wing, close and named: x, ho...
    ```
- `G8-07` (form `(do (defprotocol Pace (speed [this])) (defrecord Falcon [nam`): user_msg 201 words
    ```
    Witty circled twice near the hilltop before settling on the rim of the old clay jar, eyes on the water below.

Caw posted the Pace guild charter on the rim at the farm's edge, then wove a Falcon-shaped carrying-pouch with a name slot that signed the charter inline, pledging its own pace response. Sh...
    ```
- `G9-17` (form `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)`): user_msg 205 words
    ```
    The kitchen garden had been lovingly kept, but the sun that year had been merciless and constant.

Korvus chalked `1` on the pitcher's rim at the garden. Inside an alcove he re-chalked it to `99`, but when he stepped back out of the alcove the local chalk faded and the global mark of `1` reappeared ...
    ```
- `G10-03` (form `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-w`): user_msg 223 words
    ```
    Vane circled twice at the farm before settling on the rim of the old clay jar, eyes on the water below.

Caw scratched a master revision rule on the pitcher's rim at the village: `my-when` — whenever this pattern appeared in a form, the talon would rewrite it before the REPL ever saw the body. The r...
    ```

#### THE_FORM_OVERUSE

- `G3-03` (form `(let [n 10] (* n n))`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    by the farm, where the orchard meets the well, an old clay pitcher had stood for as long as anyone could remember.

Crosswind the crow, calm and methodical, patted the feathers of one wing.
"Whatever I tuck under a wing is in force only while the form runs,"
she said, "and only for the form that nam...
    ```
- `G3-03` (form `(let [a 5] a)`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    On a long afternoon when even the bees had grown slow, a thirsty bird settled on the rim of a clay vessel.

Quickwit the crow, steady in the stone-by-stone approach, patted the feathers of one wing.
"Whatever I tuck under a wing is in force only while the form runs,"
she said, "and only for the form...
    ```
- `G3-03` (form `(let [a 5] a)`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    The orchard at the edge of the hilltop had grown quiet in the heat, and Shout was the only sound at midday.

Shout the crow, steady in the stone-by-stone approach, patted the feathers of one wing.
"Whatever I tuck under a wing is in force only while the form runs,"
she said, "and only for the form t...
    ```
- `G3-04` (form `(let [a 2 b 3 c 4] (+ a b c))`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    A row of pebbles lay at the foot of the wall, sun-warmed, unremarkable, and just heavy enough.

Sage the crow, unhurried, form after form, patted the feathers of one wing.
"Whatever I tuck under a wing is in force only while the form runs,"
she said, "and only for the form that names the binding.
Th...
    ```
- `G3-06` (form `(let [a 3 b (+ a 1) c (* b 2)] c)`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    Sigil arrived near the hilltop with no plan but a sharp eye and a willingness to take small steps.

Sigil the crow, steady in the stone-by-stone approach, patted the feathers of one wing.
"Whatever I tuck under a wing is in force only while the form runs,"
she said, "and only for the form that names...
    ```

#### FORM_LEAK

- `G3-18` (form `(* 5 5 5)`): form '(* 5 5 5)' appears in user_msg of a goal-style subject
    ```
    When the cisterns ran shallow, even the cleverest creatures had to learn the patience of small additions.

Korvus dropped three literal stone-counts of five into the garden pitcher all at once — no wing tucked, no name carved — just three fives fed directly to the multiplication as plain inline valu...
    ```

#### NUMERAL_LIST_IN_GOAL

- `G4-13` (form `(count [1 2 3 4 5])`): goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    ```
    On the rim of a long-shadowed pitcher, a thirsty bird considered what it had and what it lacked.

Korvus laid five smooth stones in a row on the pitcher rim at the market — one through five, each touching the next. He needed a quick tally before moving on.

Without picking up each stone, he needed `...
    ```
- `G4-13` (form `(count [1 2 3 4 5])`): goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    ```
    Magnetite was no fool, and by the village the day demanded thinking rather than complaining.

"You can find what you want in a stone-pile several ways,"
Magnetite the crow said, calm and methodical, gesturing at the gathered
stones: "by the mark scratched on it, by its place in line, or by
simply as...
    ```
- `G4-13` (form `(count [1 2 3 4 5])`): goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    ```
    It was by the orchard, in the long heat of late summer, that a thirsty bird met a stubborn vessel.

Soar the crow began scattering the stone-pile, ruffling up with certainty, calling
out guesses about which stones were there without quite checking. "I know
exactly what's in the pile," she insisted. ...
    ```
- `G5-10` (form `(map #(* % %) [1 2 3 4])`): goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    ```
    An old pitcher of glazed clay sat by the garden wall, half-empty and entirely useless to anyone too proud to think.

Cinder the crow, letting the count rise on its own, perched at the pitcher's edge,
holding a decision-rule over the stones along the road. The pile was
heavy and the rim was high; the...
    ```
- `G5-10` (form `(map #(* % %) [1 2 3 4])`): goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    ```
    In a long-dry season, Bismuth found the pitcher by the market and began to consider it carefully.

Bismuth the crow, calm and methodical, held two decision-rules at the perch, one after the
other, each rule filtering the stones that the first had passed. "What lands at the
bottom," he said, "has bee...
    ```

#### ANSWER_LEAK_STRING

- `G5-03` (form `(when true :yes)`): answer string ':yes' appears in user_msg
    ```
    Vane circled twice at the farm before settling on the rim of the old clay jar, eyes on the water below.

Korvus examined the meadow pitcher's single-branch fork: one stone marked :yes sat poised above the opening. No second branch existed — only the one guarded by `when`.

He needed to know whether ...
    ```
- `G5-03` (form `(when true :yes)`): answer string ':yes' appears in user_msg
    ```
    The orchard had not seen a real rain in weeks, and even the lavender stood with its head bowed.

Korvus examined the meadow pitcher's single-branch fork: one stone marked :yes sat poised above the opening. No second branch existed — only the one guarded by `when`.

He needed to know whether the lone...
    ```
- `G5-07` (form `(or nil false :found)`): answer string ':found' appears in user_msg
    ```
    A row of pebbles lay at the foot of the wall, sun-warmed, unremarkable, and just heavy enough.

Caw examined the village pitcher's open-gate rail, the stones lined up: nil, false, then :found. The gate would release the first stone that proved truthy.

She needed to know which stone would be the fir...
    ```
- `G6-01` (form `(name 'foo.bar)`): answer string 'foo.bar' appears in user_msg
    ```
    In a year when the wells ran low, a single jar of water was a small kingdom unto itself.

Korvus perched at the pitcher's clay rim in the garden and studied the name carved into the side: a dotted path, two segments pressed into the clay. He wanted to read it as a plain string, not a symbol.

He nee...
    ```
- `G7-11` (form `(try (throw (ex-info "trouble" {})) (catch Exception e (.get`): answer string 'trouble' appears in user_msg
    ```
    A row of pebbles lay at the foot of the wall, sun-warmed, unremarkable, and just heavy enough.

Onyxwing the crow, steady in the stone-by-stone approach, spread a patch of soft moss beneath
the pitcher at the market — the day was hot, the throat was narrow, and any
pebble flung wrong without a cushi...
    ```

#### BAD_PLACE_PREP

- `G5-22` (form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n)`): 'in the hilltop' (wrong preposition)
    ```
    near the village, where the heat shimmered above the stones, Buffet began the slow business of solving thirst.

Caw stood at the pitcher's rim in the hilltop field, a circuit chalked beneath her feet: start with n=5 and accumulator=1. Each lap, multiply the accumulator by n, step n down by one — loo...
    ```
- `G5-22` (form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n)`): 'in the hilltop' (wrong preposition)
    ```
    On a long afternoon when even the bees had grown slow, a thirsty bird settled on the rim of a clay vessel.

Caw stood at the pitcher's rim in the hilltop field, a circuit chalked beneath her feet: start with n=5 and accumulator=1. Each lap, multiply the accumulator by n, step n down by one — loop wi...
    ```

#### STORY_RESOLUTION_NO_DRAWN

- `G6-05` (form `(clojure.string/reverse "abc")`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    ```
    The kitchen garden had been lovingly kept, but the sun that year had been merciless and constant.

Yowl the crow, with a triumphant rattle of feathers, glanced at the rim-carving in the meadow and
called out what she thought it said without stopping to
read carefully. The day was hot and the throat ...
    ```
- `G6-05` (form `(clojure.string/reverse "abc")`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    ```
    In a year when the wells ran low, a single jar of water was a small kingdom unto itself.

Insignia the crow, unbothered by the slow progress, pressed a talon-tip into the
pitcher's clay rim by the village, carving a name with care. The clay was
soft only briefly; once dry, the carving would last for...
    ```
- `G6-05` (form `(clojure.string/reverse "abc")`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    ```
    near the meadow, where the heat shimmered above the stones, Puzzle began the slow business of solving thirst.

"Naming is half the art," Puzzle the crow, calm and methodical, said, scoring a careful mark
into the pitcher's clay. "A clear carving tells every later crow what to
expect; a careless one ...
    ```
- `G6-11` (form `(clojure.string/split "src:test" #":")`): story-tagged example's resolution slot has no drawn-value reference (form has literals (':test', 'src:test'), resolution doesn't close the loop)
    ```
    Keen circled twice on the hilltop before settling on the rim of the old clay jar, eyes on the water below.

A small audience of meadow birds had perched on the rim of the tall
pitcher atop the hilltop to watch Symbol the crow attempt to outwit
Keen the crow at writing the right form. The challenge:
...
    ```
- `G6-11` (form `(clojure.string/split "src:test" #":")`): story-tagged example's resolution slot has no drawn-value reference (form has literals (':test', 'src:test'), resolution doesn't close the loop)
    ```
    In a long-dry season, Tempest found the pitcher at the village and began to consider it carefully.

A clay tag tied around the tall pitcher's neck by the village carried a
small puzzle. The challenge was simple: split a colon-separated classpath-like string into its individual entries. The day was
h...
    ```

#### HEDGING_NEAR_FORM

- `G6-11` (form `(count ["src" "test" "resources"])`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    Some problems cannot be hurried; they only respond to the slow addition of small things.

The wager was set by the garden: produce the value before the breeze had
turned the next leaf. The day was hot and the pitcher's water lay
low; a wrong guess wasted the breeze and the whole pebble both.
Enigma ...
    ```
- `G11-01` (form `(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScript; Pytho`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    The farmstead had stored what it could, but the heat was honest and the water was patient with no one.

The wager was set near the meadow: produce the value before the breeze had
turned the next leaf. The day was hot and the pitcher's water lay
low; a wrong guess wasted the breeze and the whole pebb...
    ```
- `G11-12` (form `(do "basilisp is a Clojure-like Lisp implemented on Python" `): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    at the edge of the meadow, where the orchard meets the well, an old clay pitcher had stood for as long as anyone could remember.

The wager was set at the edge of the meadow: produce the value before the breeze had
turned the next leaf. The day was hot and the pitcher's water lay
low; a wrong guess ...
    ```
- `G12-04` (form `(do "(chan), (go ...), (<! ...), (>! ...) form the core.asyn`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    When the cisterns ran shallow, even the cleverest creatures had to learn the patience of small additions.

The wager was set at the edge of the meadow: produce the value before the breeze had
turned the next leaf. The day was hot and the pitcher's water lay
low; a wrong guess wasted the breeze and t...
    ```
- `G12-06` (form `(do (require '[clojure.spec.alpha :as s]) (s/valid? string? `): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    Gale alighted on the rim of a jar near the farm and peered down at the small dark gleam below.

The wager was set on the farm: produce the value before the breeze had
turned the next leaf. The day was hot and the pitcher's water lay
low; a wrong guess wasted the breeze and the whole pebble both.
Sho...
    ```

#### DOUBLE_PREP

- `G9-07` (form `(do (def r (ref 0)) (dosync (alter r inc)) @r)`): verb+preposition followed by {place} which already carries its own preposition
    ```
    Witty circled twice near the hilltop before settling on the rim of the old clay jar, eyes on the water below.

Caw placed a zero-mark in a sealed safe-box beside the pitcher at the garden. To change the mark she had to open the safe-box in one atomic transaction, nudge the tally up by one, and seal ...
    ```
- `G9-18` (form `(do (def lock (Object.)) (locking lock 42))`): verb+preposition followed by {place} which already carries its own preposition
    ```
    Cluck was no fool, and at the edge of the garden the day demanded thinking rather than complaining.

Korvus planted a gate-stone at the pitcher's mouth on the road. He rolled it aside, placed a single stone tally inside the sealed section, then rolled the gate back — the tally was the body's only ex...
    ```
- `G9-18` (form `(do (def lock (Object.)) (locking lock 42))`): verb+preposition followed by {place} which already carries its own preposition
    ```
    Coal arrived at the farm with no plan but a sharp eye and a willingness to take small steps.

Korvus planted a gate-stone at the pitcher's mouth on the road. He rolled it aside, placed a single stone tally inside the sealed section, then rolled the gate back — the tally was the body's only expressio...
    ```

#### PROCEDURAL_OPENER

- `G11-08` (form `(do "type hints are metadata that guide compilation" :studie`): user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    ```
    The orchard had not seen a real rain in weeks, and even the lavender stood with its head bowed.

To understand that type hints guide compilation, she composed the purpose of type hints in Clojure and submitted the form. The REPL — calling into the earthenware vessel the human had fired — returned:

...
    ```
- `G11-14` (form `(do "host stack traces leak through interop; learn to read t`): user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    ```
    The orchard had not seen a real rain in weeks, and even the lavender stood with its head bowed.

To learn to read and debug host runtime errors, he composed debugging host-runtime errors and submitted the form. The REPL — calling into the earthenware vessel the human had fired — returned:

Question:...
    ```
- `G11-14` (form `(do "host stack traces leak through interop; learn to read t`): user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    ```
    The orchard had not seen a real rain in weeks, and even the lavender stood with its head bowed.

To learn to read and debug host runtime errors, she composed debugging host-runtime errors and submitted the form. The REPL — calling into the earthenware vessel the human had fired — returned:

What Clo...
    ```

#### METAPHOR_DISAPPEARS

- `G11-08` (form `(do "type hints are metadata that guide compilation" :studie`): user_msg has none of the fable's primary metaphor nouns (pitcher, water, pebble, stone...)
    ```
    The orchard had not seen a real rain in weeks, and even the lavender stood with its head bowed.

To understand that type hints guide compilation, she composed the purpose of type hints in Clojure and submitted the form. The REPL — calling into the earthenware vessel the human had fired — returned:

...
    ```
- `G11-14` (form `(do "host stack traces leak through interop; learn to read t`): user_msg has none of the fable's primary metaphor nouns (pitcher, water, pebble, stone...)
    ```
    The orchard had not seen a real rain in weeks, and even the lavender stood with its head bowed.

To learn to read and debug host runtime errors, he composed debugging host-runtime errors and submitted the form. The REPL — calling into the earthenware vessel the human had fired — returned:

Question:...
    ```
- `G11-14` (form `(do "host stack traces leak through interop; learn to read t`): user_msg has none of the fable's primary metaphor nouns (pitcher, water, pebble, stone...)
    ```
    The orchard had not seen a real rain in weeks, and even the lavender stood with its head bowed.

To learn to read and debug host runtime errors, she composed debugging host-runtime errors and submitted the form. The REPL — calling into the earthenware vessel the human had fired — returned:

What Clo...
    ```

#### META_FILLER_RESOLUTION

- `G11-11` (form `(do "(js/console.log x) calls a JS global; (.-foo o) reads a`): user_msg uses generic 'returned exactly' / 'settled with certainty' filler — describe what actually came back, not just that something did
    ```
    Drought has its own quiet way of teaching the difference between thirst and the right answer to thirst.

"There is no challenge here," Smoulder the crow said, ruffling up with certainty.
"Anyone could understand how ClojureScript calls JavaScript globals and reads fields without thinking." Umbra the...
    ```
- `G12-11` (form `(do "project.clj declares :dependencies, :main, :profiles fo`): user_msg uses generic 'returned exactly' / 'settled with certainty' filler — describe what actually came back, not just that something did
    ```
    Drought has its own quiet way of teaching the difference between thirst and the right answer to thirst.

"There is no challenge here," Smoulder the crow said, ruffling up with certainty.
"Anyone could study the project.clj file and how it declares dependencies, main entry points, and profiles for Le...
    ```
- `G12-15` (form `(do "Datomic and XTDB are immutable, time-aware datalog DBs"`): user_msg uses generic 'returned exactly' / 'settled with certainty' filler — describe what actually came back, not just that something did
    ```
    The orchard had not seen a real rain in weeks, and even the lavender stood with its head bowed.

"You always insist on writing it out," Foxy the crow complained,
ruffling up with certainty. "I can see the answer from here." Cawlick the crow
shook his head slowly. "To study Datomic and XTDB as immuta...
    ```

