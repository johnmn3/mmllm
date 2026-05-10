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

### G1-03: Ratios

- examples: 5
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_FORM_PREFIX': 9}
    - [CONCEPT_PHRASE_FORM_PREFIX] form=`(+ 1/2 1/4)` — example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    - [CONCEPT_PHRASE_FORM_PREFIX] form=`(+ 1/2 1/4)` — example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    - [CONCEPT_PHRASE_FORM_PREFIX] form=`(+ 1/2 1/4)` — example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    - [CONCEPT_PHRASE_FORM_PREFIX] form=`(* 2 1/2)` — example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    - [CONCEPT_PHRASE_FORM_PREFIX] form=`(* 2 1/2)` — example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    - [CONCEPT_PHRASE_FORM_PREFIX] form=`(* 2 1/2)` — example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)

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

### G1-09: Symbols vs values

- examples: 4
- variety @ n=50: 1.00
- issues: {'ONLY_SHOOK_HEAD_TIC': 1}
    - [ONLY_SHOOK_HEAD_TIC] form=`(symbol? 'hare)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

### G1-10: Comments

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'TRAILING_PARTICIPLE_CLOSER': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(+ 1 2) ; sum of one and two` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [TRAILING_PARTICIPLE_CLOSER] form=`(+ 1 2) ; sum of one and two` — sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`42 ;; the answer` — sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead

### G1-11: Whitespace doesn't matter

- examples: 2
- variety @ n=50: 1.00
- issues: {'ONLY_SHOOK_HEAD_TIC': 1, 'EXPECTED_META_PHRASE': 1}
    - [ONLY_SHOOK_HEAD_TIC] form=`(+    1    2)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [EXPECTED_META_PHRASE] form=`(+    1    2)` — user_msg uses 'the expected X' meta-language — describes the answer in graders'-vocabulary instead of letting the runtime's return speak for itself

### G1-12: Parens group; they don't multiply

- examples: 2
- variety @ n=50: 1.00
- issues: {'ONLY_SHOOK_HEAD_TIC': 2}
    - [ONLY_SHOOK_HEAD_TIC] form=`(* (+ 1 2) 3)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [ONLY_SHOOK_HEAD_TIC] form=`(* (+ 1 2) 3)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

### G1-13: First arithmetic call

- examples: 6
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 3, 'PARAGRAPH_FRAGMENTATION': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(+ 7 8)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(+ 7 8)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(+ 7 8)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead
    - [PARAGRAPH_FRAGMENTATION] form=`(- 20 7)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [PARAGRAPH_FRAGMENTATION] form=`(- 20 7)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G1-14: Nested call evaluation

- examples: 4
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(+ (* 2 3) (* 4 5))` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(+ (* 2 3) (* 4 5))` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead

### G1-15: Equality

- examples: 6
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 5, 'LOW_GROUNDING': 1}
    - [CONCEPT_AS_VERB] form=`(= 1 1)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(= :hare :hare)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(= :hare :hare)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(= :hare :tortoise)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(= :hare :tortoise)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G1-16: Numeric predicates

- examples: 6
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 4}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(zero? 0)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(pos? -2)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(neg? -3)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(neg? 4)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead

### G1-17: Printing vs returning

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 3, 'ONLY_SHOOK_HEAD_TIC': 1}
    - [REPL_TRIPLE_VOICE] form=`42` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [ONLY_SHOOK_HEAD_TIC] form=`42` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [REPL_TRIPLE_VOICE] form=`42` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`42` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G1-18: Errors are safe in the REPL

- examples: 2
- variety @ n=50: 1.00
- issues: {'EXPECTED_META_PHRASE': 1}
    - [EXPECTED_META_PHRASE] form=`(+ 1 2)` — user_msg uses 'the expected X' meta-language — describes the answer in graders'-vocabulary instead of letting the runtime's return speak for itself

## Grade 2

### G2-01: Multi-arg arithmetic

- examples: 6
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 3}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(- 100 1 2 3)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(+ 1 2 3 4 5 6 7 8 9 10)` — sentence closes with a participial coda (', producing the full sum in a single evaluation.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(+ 1 2 3 4 5 6 7 8 9 10)` — sentence closes with a participial coda (', producing the full sum in a single evaluation.') — LLM-cadence; close on the verb instead

### G2-02: Comparison chains

- examples: 5
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(< 1 2 3)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(< 3 2 1)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead

### G2-03: not= and = with multiple args

- examples: 5
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2, 'TRAILING_PARTICIPLE_CLOSER': 4}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(not= 1 2)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(not= 1 2)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [TRAILING_PARTICIPLE_CLOSER] form=`(not= 1 1)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(= 1 1 1)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(= 1 1 2)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(not= 1 1 2)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead

### G2-04: min and max

- examples: 5
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 5, 'CLAUSE_STACK_OVERFLOW': 4}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(min 1 2 3)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(max 1 2 3)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead
    - [CLAUSE_STACK_OVERFLOW] form=`(min 7 3 9 1 5)` — sentence with 5 commas reads as AI-output cadence: 'Bluster the crow simply began\ncounting carefully — to find the minimum of 6, 4, '
    - [TRAILING_PARTICIPLE_CLOSER] form=`(min 7 3 9 1 5)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead
    - [CLAUSE_STACK_OVERFLOW] form=`(min 7 3 9 1 5)` — sentence with 5 commas reads as AI-output cadence: 'Dimsky the crow simply began\ncounting carefully — to find the minimum of 7, 6, 7'
    - [TRAILING_PARTICIPLE_CLOSER] form=`(min 7 3 9 1 5)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead

### G2-05: quot, rem, mod

- examples: 6
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'PARAGRAPH_FRAGMENTATION': 1, 'TRAILING_PARTICIPLE_CLOSER': 2, 'REPEATED_OPENER_FRAGMENT': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(rem 17 5)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [PARAGRAPH_FRAGMENTATION] form=`(rem 17 5)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [TRAILING_PARTICIPLE_CLOSER] form=`(mod 17 5)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead
    - [REPEATED_OPENER_FRAGMENT] form=`(mod 17 5)` — opener fragment 'at the edge of the hilltop' also appears later in user_msg
    - [TRAILING_PARTICIPLE_CLOSER] form=`(quot 100 7)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead

### G2-06: inc and dec

- examples: 5
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2, 'PARAGRAPH_FRAGMENTATION': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(inc 5)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead
    - [PARAGRAPH_FRAGMENTATION] form=`(inc 0)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [PARAGRAPH_FRAGMENTATION] form=`(inc -1)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [TRAILING_PARTICIPLE_CLOSER] form=`(inc -1)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead

### G2-07: Absolute value

- examples: 4
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'PARAGRAPH_FRAGMENTATION': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(abs -5)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [PARAGRAPH_FRAGMENTATION] form=`(abs -5)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [TRAILING_PARTICIPLE_CLOSER] form=`(abs -5)` — sentence closes with a participial coda (', yielding its positive mirror.') — LLM-cadence; close on the verb instead

### G2-08: Arithmetic on ratios

- examples: 3
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(- 1 1/3)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(- 1 1/3)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead

### G2-09: Floats vs ints (the / operator)

- examples: 3
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 3}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(/ 10 2)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(/ 10 3)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(/ 10 3)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead

### G2-10: Powers via repeated multiplication

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'TRAILING_PARTICIPLE_CLOSER': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [LOW_GROUNDING] form=`(* 2 2 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [TRAILING_PARTICIPLE_CLOSER] form=`(* 2 2 2)` — sentence closes with a participial coda (', giving the cube.') — LLM-cadence; close on the verb instead
    - [PARAGRAPH_FRAGMENTATION] form=`(* 3 3 3 3)` — user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

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
- issues: {'LOW_GROUNDING': 2, 'CONCEPT_AS_VERB': 6, 'CLAUSE_STACK_OVERFLOW': 2}
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(and true false)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(or false true)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(or false false)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(or false false)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G2-14: not — turning truthy to false

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CONCEPT_AS_VERB': 3}
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(not true)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(not false)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(not false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(not 0)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G2-15: Falsey values: only false and nil

- examples: 4
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 3, 'REPEATED_OPENER_FRAGMENT': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [CONCEPT_AS_VERB] form=`(if 0 1 0)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [REPEATED_OPENER_FRAGMENT] form=`(if "" 1 0)` — opener fragment 'the pitcher near the orchard' also appears later in user_msg
    - [TRAILING_PARTICIPLE_CLOSER] form=`(if nil 1 0)` — sentence closes with a participial coda (', returning the else-branch value.') — LLM-cadence; close on the verb instead
    - [CONCEPT_AS_VERB] form=`(if false 1 0)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(if false 1 0)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G2-16: Truthy 0 and empty string

- examples: 4
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 3, 'LOW_GROUNDING': 1}
    - [CONCEPT_AS_VERB] form=`(boolean 0)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(boolean "")` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(boolean false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(boolean false)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G2-17: Keyword as function for map lookup

- examples: 3
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 3}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(:hare {:hare 1 :tortoise 2})` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(:tortoise {:hare 1 :tortoise 2})` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(:missing {:hare 1})` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead

### G2-18: Quoting symbols

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= (quote tortoise) 'tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= (quote tortoise) 'tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count '(1 2 3))` — parametric example has hard-coded English numeral 'three integers' in a story slot — the actual draws may differ from this fixed count

### G2-19: Auto-promotion to bigint

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(+ 99999999999 1)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead

### G2-20: Counting

- examples: 3
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 4}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count [1 2 3])` — sentence closes with a participial coda (', carrying the\ntally — returned the final number.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count [1 2 3])` — sentence closes with a participial coda (',\nwalking the rim — returned the final value.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count "hello")` — sentence closes with a participial coda (', incrementing the tally with every bead.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count "hello")` — sentence closes with a participial coda (',\nwalking the rim — returned the final value.') — LLM-cadence; close on the verb instead

### G2-22: Compose pure arithmetic (multi-step calculation)

- examples: 3
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(- (* 5 4) 7)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead

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
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2, 'THE_FORM_OVERUSE': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [a 1 b 2] (+ a b))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [x 5 y 3] (- x y))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [THE_FORM_OVERUSE] form=`(let [a 2 b 3 c 4] (+ a b c))` — `the form` appears 5 times in user_msg (template tic — vary references)

### G3-06: let — binding can reference prior

- examples: 2
- variety @ n=50: 1.00
- issues: {'THE_FORM_OVERUSE': 1}
    - [THE_FORM_OVERUSE] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — `the form` appears 5 times in user_msg (template tic — vary references)

### G3-08: fn — multi-arg

- examples: 1
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`((fn [a b c] (+ a b c)) 1 2 3)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G3-09: defn — shorthand

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1, 'EXPECTED_META_PHRASE': 1, 'PARAGRAPH_FRAGMENTATION': 1}
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
- issues: {'TRAILING_PARTICIPLE_CLOSER': 3}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (def g 5) (let [g 99] (+ g 1)))` — sentence closes with a participial coda (', shadowing the top-level def.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (def g 5) (let [g 99] (+ g 1)))` — sentence closes with a participial coda (', shadowing the top-level def.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (def g 5) (let [g 99] (+ g 1)))` — sentence closes with a participial coda (', shadowing the top-level def.') — LLM-cadence; close on the verb instead

### G3-13: fn body returns last form

- examples: 1
- variety @ n=50: 1.00
- issues: {'PARAGRAPH_FRAGMENTATION': 2}
    - [PARAGRAPH_FRAGMENTATION] form=`((fn [x] x x x 99) 1)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [PARAGRAPH_FRAGMENTATION] form=`((fn [x] x x x 99) 1)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G3-15: Side-effects in body

- examples: 1
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 3}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (println "hi") 42)` — sentence closes with a participial coda (', ignoring the intermediate println side-effect.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (println "hi") 42)` — sentence closes with a participial coda (', ignoring the intermediate println side-effect.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (println "hi") 42)` — sentence closes with a participial coda (', ignoring the intermediate println side-effect.') — LLM-cadence; close on the verb instead

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
- issues: {'PARAGRAPH_FRAGMENTATION': 3, 'REPL_TRIPLE_VOICE': 4, 'TRAILING_PARTICIPLE_CLOSER': 3, 'LOW_GROUNDING': 1}
    - [PARAGRAPH_FRAGMENTATION] form=`[]` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [REPL_TRIPLE_VOICE] form=`[]` — user_msg mentions 'REPL' 4 times — the REPL personification should appear at most twice per record (submit + return)
    - [TRAILING_PARTICIPLE_CLOSER] form=`[]` — sentence closes with a participial coda (', confirming the reserved space held nothing at all.') — LLM-cadence; close on the verb instead
    - [PARAGRAPH_FRAGMENTATION] form=`[]` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [REPL_TRIPLE_VOICE] form=`[]` — user_msg mentions 'REPL' 4 times — the REPL personification should appear at most twice per record (submit + return)
    - [TRAILING_PARTICIPLE_CLOSER] form=`[]` — sentence closes with a participial coda (', confirming the reserved space held nothing at all.') — LLM-cadence; close on the verb instead

### G4-02: nth — vector access

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'TRAILING_PARTICIPLE_CLOSER': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(nth [10 20 30] 0)` — sentence with 5 commas reads as AI-output cadence: 'To get the element at index 0 of a vector containing 10, 20, and 30 properly,\nhe'
    - [TRAILING_PARTICIPLE_CLOSER] form=`(nth [10 20 30] 0)` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(nth [10 20 30] 2)` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead

### G4-03: conj — append to vector

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 2, 'TRAILING_PARTICIPLE_CLOSER': 3}
    - [REPL_TRIPLE_VOICE] form=`(conj [1 2] 3)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [TRAILING_PARTICIPLE_CLOSER] form=`(conj [1 2] 3)` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(conj [1 2] 3)` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(conj [] :hare)` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead
    - [REPL_TRIPLE_VOICE] form=`(conj [] :hare)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G4-04: List literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`'(1 2 3)` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`'()` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead

### G4-06: Map literal

- examples: 1
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`{:hare 1 :tortoise 2}` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead

### G4-07: get — map lookup

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 3, 'LOW_GROUNDING': 1, 'REPL_TRIPLE_VOICE': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(get {:a 1 :b 2} :a)` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(get {:a 1} :missing :default)` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead
    - [LOW_GROUNDING] form=`(get {:a 1} :missing :default)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [REPL_TRIPLE_VOICE] form=`(get {:a 1} :missing :default)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [TRAILING_PARTICIPLE_CLOSER] form=`(get {:a 1} :missing :default)` — sentence closes with a participial coda (', confirming the absent compartment triggered the soft.') — LLM-cadence; close on the verb instead

### G4-08: assoc — map update

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(assoc {:a 1} :a 99)` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(assoc {:a 1} :a 99)` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead

### G4-09: dissoc — map remove key

- examples: 1
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(dissoc {:a 1 :b 2} :a)` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(dissoc {:a 1 :b 2} :a)` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead

### G4-12: Set membership

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'REPL_TRIPLE_VOICE': 1, 'TRAILING_PARTICIPLE_CLOSER': 1, 'DOUBLED_INPUT_VALUE_PARENS': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(contains? #{1 2 3} 2)` — sentence with 5 commas reads as AI-output cadence: 'To check whether 2 is a member of a set containing 1, 2, and 3 properly,\nhe comp'
    - [REPL_TRIPLE_VOICE] form=`(contains? #{1 2 3} 4)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [TRAILING_PARTICIPLE_CLOSER] form=`(contains? #{1 2 3} 4)` — sentence closes with a participial coda (', telling the crow the stone has no slot.') — LLM-cadence; close on the verb instead
    - [DOUBLED_INPUT_VALUE_PARENS] form=`(contains? #{1 2 3} 4)` — user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it

### G4-13: count — universal

- examples: 4
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'TRAILING_PARTICIPLE_CLOSER': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(count #{:a :b :c})` — sentence with 5 commas reads as AI-output cadence: 'To count the elements in a set containing the keywords :a, :b, and :c properly,\n'
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count "tortoise")` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count "tortoise")` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead

### G4-14: empty?

- examples: 3
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 2, 'TRAILING_PARTICIPLE_CLOSER': 2}
    - [REPL_TRIPLE_VOICE] form=`(empty? [])` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [TRAILING_PARTICIPLE_CLOSER] form=`(empty? [])` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead
    - [REPL_TRIPLE_VOICE] form=`(empty? [1])` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [TRAILING_PARTICIPLE_CLOSER] form=`(empty? "")` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead

### G4-15: first, rest, last

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(count (rest [10 20 30]))` — sentence with 5 commas reads as AI-output cadence: 'To count the elements remaining after removing the first element from a vector w'

### G4-17: Immutability — assoc returns new

- examples: 1
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(let [m {:a 1}] (assoc m :a 99) m)` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead

### G4-19: range and seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(first (range 1 100))` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead

### G4-20: Collection vs sequence

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'REPL_TRIPLE_VOICE': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(count (seq [1 2 3]))` — sentence with 5 commas reads as AI-output cadence: 'To convert a vector containing 1, 2, and 3 to a sequence and count its elements '
    - [REPL_TRIPLE_VOICE] form=`(seq [])` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

## Grade 5

### G5-03: when

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(when true :yes)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(when true :yes)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G5-07: and / or as control flow

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [LOW_GROUNDING] form=`(or nil false :found)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [TRAILING_PARTICIPLE_CLOSER] form=`(or nil false :found)` — sentence closes with a participial coda (', returning the first truthy value it finds.') — LLM-cadence; close on the verb instead

### G5-10: map

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(map inc [1 2 3])` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(map inc [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'To pour the vector containing 1, 2, 3 through a sieve whose rule is inc, collect'
    - [TRAILING_PARTICIPLE_CLOSER] form=`(map inc [1 2 3])` — sentence closes with a participial coda (', collecting the full transformed sequence as the result.') — LLM-cadence; close on the verb instead
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(map inc [1 2 3])` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(map inc [1 2 3])` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count

### G5-12: reduce

- examples: 3
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 4}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(reduce + [1 2 3 4])` — sentence closes with a participial coda (', carrying the\ntally — returned the final number.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(reduce max [3 1 4 1 5 9 2 6])` — sentence closes with a participial coda (', carrying the\ntally — returned the final number.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(reduce max [3 1 4 1 5 9 2 6])` — sentence closes with a participial coda (',\nwalking the rim — returned the final value.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(reduce max [3 1 4 1 5 9 2 6])` — sentence closes with a participial coda (', carrying the\ntally — returned the final number.') — LLM-cadence; close on the verb instead

### G5-13: reduce with init

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 3}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(reduce + 100 [1 2 3])` — sentence closes with a participial coda (', counting the steps —\nreturned the count.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(reduce + 100 [1 2 3])` — sentence closes with a participial coda (', counting the steps —\nreturned the count.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(reduce + 0 [])` — sentence closes with a participial coda (', carrying the\ntally — returned the final number.') — LLM-cadence; close on the verb instead

### G5-14: apply

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 2}
    - [CONCEPT_AS_VERB] form=`(apply + [1 2 3 4])` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(apply max [3 1 4 1 5])` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G5-16: partial

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [CONCEPT_AS_VERB] form=`((partial + 10) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CLAUSE_STACK_OVERFLOW] form=`(map (partial * 3) [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To apply a partially applied multiplication to each element of the vector contai'

### G5-17: juxt

- examples: 1
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`((juxt inc dec) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G5-18: some

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'TRAILING_PARTICIPLE_CLOSER': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(some even? [1 3 5 8 7])` — sentence with 6 commas reads as AI-output cadence: '(with 6, 5, and 16 folded in)\n\nQuestion: write a Clojure expression for whether '
    - [TRAILING_PARTICIPLE_CLOSER] form=`(some even? [1 3 5 8 7])` — sentence closes with a participial coda (', returning the first truthy result it finds.') — LLM-cadence; close on the verb instead
    - [CLAUSE_STACK_OVERFLOW] form=`(some even? [1 3 5 8 7])` — sentence with 7 commas reads as AI-output cadence: '(with 15, 14, 14, and 17 folded in)\n\nWrite a form whose evaluation gives whether'
    - [TRAILING_PARTICIPLE_CLOSER] form=`(some even? [1 3 5 8 7])` — sentence closes with a participial coda (', returning the first truthy result it finds.') — LLM-cadence; close on the verb instead

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
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(take 3 [10 20 30 40 50])` — sentence closes with a participial coda (', leaving the rest on the rim.') — LLM-cadence; close on the verb instead

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
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(name 'foo.bar)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-05: Fully qualified names

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'STORY_SLOT_NOUN_REPEAT': 3}
    - [LOW_GROUNDING] form=`(namespace :owner/item)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_SLOT_NOUN_REPEAT] form=`(name :owner/item)` — the noun 'the local name' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(name :owner/item)` — the noun 'the local name' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(name :owner/item)` — the noun 'the local name' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats

### G6-11: Classpath

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HEDGING_NEAR_FORM] form=`(count ["src" "test" "resources"])` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(count ["src" "test" "resources"])` — sentence with 5 commas reads as AI-output cadence: 'Chatter the crow, unhurried with form after form, walked to the slate and began '

### G6-14: Import for host classes

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(symbol? 'java.util.List)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name 'java.util.Map)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-16: Cleaning up requires

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.set)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 7

### G7-05: nil punning

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(first nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(first nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-06: pre and post conditions

- examples: 2
- variety @ n=50: 1.00
- issues: {'ABSTRACT_RESULT_NARRATION': 3}
    - [ABSTRACT_RESULT_NARRATION] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns
    - [ABSTRACT_RESULT_NARRATION] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns
    - [ABSTRACT_RESULT_NARRATION] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns

### G7-07: assert

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPEATED_OPENER_FRAGMENT': 1, 'CLAUSE_STACK_OVERFLOW': 2}
    - [REPEATED_OPENER_FRAGMENT] form=`(do (assert (= 1 1)) 1)` — opener fragment 'the pitcher near the farm' also appears later in user_msg
    - [CLAUSE_STACK_OVERFLOW] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — sentence with 5 commas reads as AI-output cadence: 'To assert that 5 equals 0, catch the failure, and return a numeric code, he comp'
    - [CLAUSE_STACK_OVERFLOW] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — sentence with 5 commas reads as AI-output cadence: 'To assert that 5 equals 8, catch the failure, and return a numeric code, she com'

### G7-09: tap>

- examples: 2
- variety @ n=50: 1.00
- issues: {'PARAGRAPH_FRAGMENTATION': 1}
    - [PARAGRAPH_FRAGMENTATION] form=`(tap> 42)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G7-14: with-open

- examples: 1
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(with-out-str (println "hare"))` — sentence closes with a participial coda (', gathering the label and groove into a string at the rim.') — LLM-cadence; close on the verb instead

### G7-15: *in* and *out*

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(with-out-str (println))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

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
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — sentence closes with a participial coda (', filling its slots — returned the value\nthe pouch held.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (deftype Stone [weight]) (.-weight (Stone. 7))` — sentence closes with a participial coda (', filling its slots — returned the value\nthe pouch held.') — LLM-cadence; close on the verb instead

### G8-03: defrecord introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (defrecord Runner [name pace]) (:name (->Runne` — sentence closes with a participial coda (', filling its slots — returned the value\nthe pouch held.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (defrecord Runner [name pace]) (:name (->Runne` — sentence closes with a participial coda (', leaving the pace slot untouched.') — LLM-cadence; close on the verb instead

### G8-04: Protocol definition

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_SLOT_NOUN_REPEAT': 3}
    - [STORY_SLOT_NOUN_REPEAT] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — the noun 'the guild's' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — the noun 'the guild's' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — the noun 'the guild's' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats

### G8-05: Protocol extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol named Greet with one method hail, extend it to Long type wi'

### G8-06: Protocol method dispatch

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, extend it to both String and Long t'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, extend it to both String and Long t'
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence closes with a participial coda (', proving the guild dispatched correctly.') — LLM-cadence; close on the verb instead

### G8-07: Record implementing protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3, 'HIGH_LENGTH': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (defrecord F` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, define a record Falcon that impleme'
    - [HIGH_LENGTH] form=`(do (defprotocol Pace (speed [this])) (defrecord F` — user_msg 201 words
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (defprotocol Pace (speed [this])) (defrecord F` — sentence closes with a participial coda (', pledging its own pace response.') — LLM-cadence; close on the verb instead
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, define a record Heron that implemen'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, define a record Heron that implemen'

### G8-08: Multimethod defmulti

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence closes with a participial coda (', routing the stone — returned the chute-specific\nvalue.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (defmulti tag :kind) (defmethod tag :stone [_]` — sentence closes with a participial coda (', routing the stone — returned the chute-specific\nvalue.') — LLM-cadence; close on the verb instead
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
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (defmulti show identity) (defmethod show :rabb` — sentence closes with a participial coda (', routing the stone — returned the chute-specific\nvalue.') — LLM-cadence; close on the verb instead
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti show identity) (defmethod show :rabb` — sentence with 5 commas reads as AI-output cadence: 'To define a multimethod show that dispatches on identity with a method for one s'

### G8-11: Protocol vs Java interface

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol IPace (run [this])) (extend-proto` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol IPace with method run, extend it to String type, then call '

### G8-12: extend-type on built-in types

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-type` — sentence with 6 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, use extend-type to attach it to Lon'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-type` — sentence with 6 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, use extend-type to attach it to Lon'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-type` — sentence with 6 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, use extend-type to attach it to Str'
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (defprotocol Pace (speed [this])) (extend-type` — sentence closes with a participial coda (', routing the stone — returned the chute-specific\nvalue.') — LLM-cadence; close on the verb instead

### G8-15: derive and isa? — multimethod hierarchy

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'LOW_GROUNDING': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — sentence with 5 commas reads as AI-output cadence: 'To establish a type relationship where ::hare is a type of ::runner, then check '
    - [LOW_GROUNDING] form=`(isa? java.lang.Long java.lang.Number)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(isa? java.lang.String java.lang.Number)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-16: Abstract design with protocols

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (defprotocol Sound (cry [this])) (defrecord Fa` — sentence closes with a participial coda (', returning its registered response.') — LLM-cadence; close on the verb instead

## Grade 9

### G9-01: Immutability as default — review

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1, 'CLAUSE_STACK_OVERFLOW': 4}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(let [m {:a 1}] (assoc m :b 2) m)` — sentence closes with a participial coda (', leaving the first one exactly where it was.') — LLM-cadence; close on the verb instead
    - [CLAUSE_STACK_OVERFLOW] form=`(let [m {:a 1}] (assoc m :b 2) m)` — sentence with 7 commas reads as AI-output cadence: 'To bind a map m, call assoc to add :b 2 to a new map, then return the unchanged '
    - [CLAUSE_STACK_OVERFLOW] form=`(let [v [1 2 3]] (conj v 4) v)` — sentence with 5 commas reads as AI-output cadence: 'To bind a vector v, call conj to add 5 to a new vector, then return the unchange'
    - [CLAUSE_STACK_OVERFLOW] form=`(let [v [1 2 3]] (conj v 4) v)` — sentence with 5 commas reads as AI-output cadence: 'To bind a vector v, call conj to add 9 to a new vector, then return the unchange'
    - [CLAUSE_STACK_OVERFLOW] form=`(let [v [1 2 3]] (conj v 4) v)` — sentence with 5 commas reads as AI-output cadence: 'To bind a vector v, call conj to add 6 to a new vector, then return the unchange'

### G9-02: Why state at all

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — sentence with 7 commas reads as AI-output cadence: 'To construct an atom holding 0 as counter, atomically swap it by applying inc, a'

### G9-03: Atom introduction

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'CLAUSE_STACK_OVERFLOW': 2}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 10)) (swap! a + 5) @a)` — sentence with 5 commas reads as AI-output cadence: 'To construct an atom holding 10, atomically swap it by applying + to 5, and dere'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom :start)) (reset! a :done) @a)` — sentence with 5 commas reads as AI-output cadence: 'To construct an atom holding a start keyword, atomically reset it to a done keyw'

### G9-06: Validator on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — sentence with 5 commas reads as AI-output cadence: 'validator on it, atomically swap by applying inc, and dereference,\nhe composed a'

### G9-07: Ref introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3, 'STORY_SLOT_NOUN_REPEAT': 6, 'DOUBLE_PREP': 1, 'LOW_GROUNDING': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 5 commas reads as AI-output cadence: 'To construct a ref holding 0, perform a transactional alter by applying inc insi'
    - [STORY_SLOT_NOUN_REPEAT] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — the noun 'the safe-box' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — the noun 'the safe-box' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [DOUBLE_PREP] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — verb+preposition followed by {place} which already carries its own preposition
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_SLOT_NOUN_REPEAT] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — the noun 'the safe-box' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats

### G9-08: dosync and alter

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_SLOT_NOUN_REPEAT': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_SLOT_NOUN_REPEAT] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — the noun 'the safe-box' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — the noun 'the safe-box' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — sentence with 5 commas reads as AI-output cadence: 'To construct a ref holding 10, perform a transactional alter by applying + with '
    - [STORY_SLOT_NOUN_REPEAT] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — the noun 'the safe-box' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats

### G9-09: Ref vs atom

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'LOW_GROUNDING': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 5 commas reads as AI-output cadence: 'To construct an atom holding 0, atomically swap it by applying inc, and derefere'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 5 commas reads as AI-output cadence: 'To construct an atom holding 0, atomically swap it by applying inc, and derefere'
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-10: Agent introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'CLAUSE_STACK_OVERFLOW': 3}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 6 commas reads as AI-output cadence: 'To construct an agent holding 0, asynchronously send inc to it, await its comple'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 8 commas reads as AI-output cadence: 'To construct an agent holding 0, asynchronously send inc to it, await its comple'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 5)) (send ag + 10) (await ag) @` — sentence with 6 commas reads as AI-output cadence: 'To construct an agent holding 5, asynchronously send + with 10 to it, await its '

### G9-11: send and send-off

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 8 commas reads as AI-output cadence: 'To construct an agent holding 0, use send to asynchronously apply inc, await its'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send-off ag inc) (await ag` — sentence with 8 commas reads as AI-output cadence: 'To construct an agent holding 0, use send-off to asynchronously apply inc, await'

### G9-12: await — synchronizing on agents

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 8 commas reads as AI-output cadence: 'To construct an agent holding 0, asynchronously send inc twice, synchronize with'
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
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def p (promise)) (deliver p :done) @p)` — sentence with 5 commas reads as AI-output cadence: 'To construct a promise, deliver a completion keyword to it, and dereference to g'

### G9-17: binding — thread-local

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3, 'HIGH_LENGTH': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — sentence with 5 commas reads as AI-output cadence: 'To define a dynamic var *p* as 1, use binding to rebind it to 99, and read its v'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *` — sentence with 7 commas reads as AI-output cadence: 'To define a dynamic var *p* as 1, use binding to rebind it to 99 inside, and rea'
    - [HIGH_LENGTH] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *` — user_msg 205 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *` — sentence with 5 commas reads as AI-output cadence: 'To define a dynamic var *p* as 1, use binding to rebind it to 99 inside, and rea'

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'HIGH_LENGTH': 1, 'DOUBLE_PREP': 2, 'TRAILING_PARTICIPLE_CLOSER': 2}
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg 205 words
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_PREP] form=`(do (def lock (Object.)) (locking lock 42))` — verb+preposition followed by {place} which already carries its own preposition
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (def lock (Object.)) (locking lock 42))` — sentence closes with a participial coda (', freeing the path.') — LLM-cadence; close on the verb instead

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
- issues: {'HIGH_LENGTH': 1, 'REPL_TRIPLE_VOICE': 1}
    - [HIGH_LENGTH] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg 223 words
    - [REPL_TRIPLE_VOICE] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 2, 'CLAUSE_STACK_OVERFLOW': 3, 'HIGH_LENGTH': 2, 'DOUBLED_INPUT_VALUE_PARENS': 2, 'LOW_GROUNDING': 1}
    - [CONCEPT_AS_VERB] form=`(-> 5 inc inc inc)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CLAUSE_STACK_OVERFLOW] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — sentence with 7 commas reads as AI-output cadence: 'To thread a vector through filter, map, and reduce using thread-last, he compose'
    - [HIGH_LENGTH] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — user_msg 208 words
    - [CLAUSE_STACK_OVERFLOW] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — sentence with 5 commas reads as AI-output cadence: 'To thread a vector through filter, map, and reduce using thread-last, she scratc'
    - [DOUBLED_INPUT_VALUE_PARENS] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
    - [HIGH_LENGTH] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — user_msg 206 words

### G10-09: Hygiene and gensym

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_SLOT_NOUN_REPEAT': 3}
    - [STORY_SLOT_NOUN_REPEAT] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — the noun 'the same prefix' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — the noun 'the same prefix' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — the noun 'the same prefix' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats

### G10-10: Anaphoric macros are confusing

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_SLOT_NOUN_REPEAT': 3}
    - [STORY_SLOT_NOUN_REPEAT] form=`(if-let [x 7] (* x x) 0)` — the noun 'the then-branch' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(if-let [x 7] (* x x) 0)` — the noun 'the then-branch' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(if-let [x 7] (* x x) 0)` — the noun 'the then-branch' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats

### G10-13: Data readers and EDN extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2, 'ONLY_SHOOK_HEAD_TIC': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(clojure.edn/read-string "42")` — sentence closes with a participial coda (', producing the value those characters denote.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(clojure.edn/read-string "42")` — sentence closes with a participial coda (', producing the value those characters denote.') — LLM-cadence; close on the verb instead
    - [ONLY_SHOOK_HEAD_TIC] form=`(clojure.edn/read-string "[:a :b :c]")` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

### G10-14: eval (the function)

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1, 'DOUBLED_INPUT_VALUE_PARENS': 1}
    - [REPL_TRIPLE_VOICE] form=`(eval '(+ 1 2 3))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [DOUBLED_INPUT_VALUE_PARENS] form=`(eval '(+ 1 2 3))` — user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it

### G10-15: When not to write a macro

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLED_INPUT_VALUE_PARENS': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [DOUBLED_INPUT_VALUE_PARENS] form=`(do "a function suffices when no syntax shaping is` — user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do "prefer fn unless you must shape syntax" (map ` — sentence closes with a participial coda (', collecting the results.') — LLM-cadence; close on the verb instead

### G10-16: Macro pattern library

- examples: 2
- variety @ n=50: 1.00
- issues: {'PARAGRAPH_FRAGMENTATION': 1}
    - [PARAGRAPH_FRAGMENTATION] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

## Grade 11

### G11-01: JVM vs CLR vs JS vs Python (host overview)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HEDGING_NEAR_FORM] form=`(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScr` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScr` — sentence with 5 commas reads as AI-output cadence: 'Featherdark the crow, patient as the water rose, walked to the slate and began t'

### G11-08: Type hints

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'PROCEDURAL_OPENER': 1, 'METAPHOR_DISAPPEARS': 1}
    - [LOW_GROUNDING] form=`(do "type hints are metadata that guide compilatio` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PROCEDURAL_OPENER] form=`(do "type hints are metadata that guide compilatio` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    - [METAPHOR_DISAPPEARS] form=`(do "type hints are metadata that guide compilatio` — user_msg has none of the fable's primary metaphor nouns (pitcher, water, pebble, stone...)

### G11-09: Checked vs unchecked math

- examples: 2
- variety @ n=50: 0.99
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(+ 1 2)` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do "*unchecked-math* turns off overflow checking ` — sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead

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
- issues: {'LOW_GROUNDING': 2, 'PROCEDURAL_OPENER': 2, 'METAPHOR_DISAPPEARS': 2}
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
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] (map inc) [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To use the map-inc transducer with into to increment the vector containing 1, 2,'

### G12-02: Transducer composition

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — sentence with 6 commas reads as AI-output cadence: 'What Clojure form computes the sum accumulated via transduce using the composed '
    - [CLAUSE_STACK_OVERFLOW] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — sentence with 6 commas reads as AI-output cadence: 'What Clojure form computes the sum accumulated via transduce using the composed '

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
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "pipe, mult, mix, pipeline-async route values ` — sentence with 6 commas reads as AI-output cadence: 'Halfway through the race, Azure the crow, preening at the thought of knowing, st'

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
    - [CLAUSE_STACK_OVERFLOW] form=`(do "s/exercise produces sample inputs for a spec"` — sentence with 5 commas reads as AI-output cadence: 'Yawp the crow, deliberate and unhurried by the rising sun, walked to the slate a'

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

- **TRAILING_PARTICIPLE_CLOSER**: 109
- **CLAUSE_STACK_OVERFLOW**: 81
- **LOW_GROUNDING**: 48
- **CONCEPT_AS_VERB**: 29
- **STORY_SLOT_NOUN_REPEAT**: 21
- **REPL_TRIPLE_VOICE**: 18
- **FORM_DISPLAY_AND_FORM_NOUN**: 17
- **PARAGRAPH_FRAGMENTATION**: 15
- **ONLY_SHOOK_HEAD_TIC**: 14
- **HEDGING_NEAR_FORM**: 11
- **CONCEPT_PHRASE_FORM_PREFIX**: 9
- **NARRATIVE_NUMERAL_HARDCODE**: 9
- **HIGH_LENGTH**: 9
- **THE_FORM_OVERUSE**: 8
- **DOUBLED_INPUT_VALUE_PARENS**: 5
- **REPEATED_OPENER_FRAGMENT**: 4
- **EXPECTED_META_PHRASE**: 3
- **ABSTRACT_RESULT_NARRATION**: 3
- **DOUBLE_PREP**: 3
- **PROCEDURAL_OPENER**: 3
- **METAPHOR_DISAPPEARS**: 3
- **META_FILLER_RESOLUTION**: 3
- **ANSWER_LEAK**: 2
- **BAD_PLACE_PREP**: 2
- **FORM_LEAK**: 1

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 45 | — |
| 2 | 22 | 88 | 87 | — |
| 3 | 18 | 31 | 29 | — |
| 4 | 20 | 39 | 47 | — |
| 5 | 22 | 39 | 34 | — |
| 6 | 16 | 33 | 10 | — |
| 7 | 18 | 36 | 15 | — |
| 8 | 16 | 31 | 33 | — |
| 9 | 18 | 34 | 52 | — |
| 10 | 16 | 36 | 37 | — |
| 11 | 14 | 29 | 16 | — |
| 12 | 18 | 37 | 25 | — |

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

#### CONCEPT_PHRASE_FORM_PREFIX

- `G1-03` (form `(+ 1/2 1/4)`): example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    ```
    It was the kind of summer that turned every shaded stone into a small kindness.

At the foot of a tall pitcher at the village, Stoop the crow sketched a small
wager into the dry dust: whoever guessed the result of `(+ 1/2 1/4)`
first would claim the cool water lying low at the bottom. The throat
was...
    ```
- `G1-03` (form `(+ 1/2 1/4)`): example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    ```
    near the road, a single pitcher held the last of the water, and Bicker arrived too parched to be picky.

At the foot of a tall pitcher on the road, Antimony the crow sketched a small
wager into the dry dust: whoever guessed the result of `(+ 1/2 1/4)`
first would claim the cool water lying low at th...
    ```
- `G1-03` (form `(+ 1/2 1/4)`): example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    ```
    In a year when the wells ran low, a single jar of water was a small kingdom unto itself.

Loft the crow, watching the level lift, had been keeping a small leather
notebook of every form she had successfully evaluated —
each page like a pebble in the pitcher's growing pile, raising the
ledger's water...
    ```
- `G1-03` (form `(* 2 1/2)`): example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    ```
    The water sat at the bottom of the jar, deep enough to glimpse and far enough to tantalize.

Cowl the crow and Buzz the crow stopped by the garden where someone had
scratched the form (* 2 1/2) into the dust beside a tall pitcher. The day
was hot, the throat of the pitcher was narrow, and the water ...
    ```
- `G1-03` (form `(* 2 1/2)`): example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    ```
    When Vane landed by the garden wall, he saw the water and saw the distance, and stood very still.

Halfway to the pitcher, Cloudshroud the crow, with a triumphant rattle of feathers, stopped on the hilltop
and refused to take another step until someone could prove what the
form `(* 8 1/2)` evaluated...
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

Thermal the crow, watching the level lift, spread a patch of soft moss
beneath the pitcher near the farm — the day was hot, the throat was narrow, and any
pebble flung wrong without a cushion would chip ...
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

#### TRAILING_PARTICIPLE_CLOSER

- `G1-10` (form `(+ 1 2) ; sum of one and two`): sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    ```
    An old pitcher of glazed clay sat by the garden wall, half-empty and entirely useless to anyone too proud to think.

"There are conventions for how the runtime *reads* a form,"
Cinder the crow, dropping each stone with careful attention, said: "what counts as one token, what's just
spacing, what get...
    ```
- `G1-10` (form `42 ;; the answer`): sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    ```
    When the cisterns ran shallow, even the cleverest creatures had to learn the patience of small additions.

"A form is what the reader sees," Veer the crow, dropping each stone with careful attention, said,
"after the conventions have been applied. Some marks count, some
don't; some shapes are expand...
    ```
- `G1-13` (form `(+ 7 8)`): sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead
    ```
    It was near the hilltop, in the long heat of late summer, that a thirsty bird met a stubborn vessel.

Swoop the crow eyed the heap, preening at the thought of knowing, and called out a guess
about how many stones could be dropped before the water rose high
enough, without bothering to count. Malachi...
    ```
- `G1-13` (form `(+ 7 8)`): sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead
    ```
    In a long-dry season, Scholar found the pitcher on the road and began to consider it carefully.

Riddle the crow eyed the heap, ruffling up with certainty, and called out a guess
about how many stones could be dropped before the water rose high
enough, without bothering to count. Scholar the crow si...
    ```
- `G1-13` (form `(+ 7 8)`): sentence closes with a participial coda (', settling the matter the patient way.') — LLM-cadence; close on the verb instead
    ```
    On a long afternoon when even the bees had grown slow, a thirsty bird settled on the rim of a clay vessel.

Soothe the crow eyed the heap, with a self-satisfied beak-click, and called out a guess
about how many stones could be dropped before the water rose high
enough, without bothering to count. Ri...
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
Soot the crow, unhurried with form after form, said. "You bring the form to the gate, the runtime
checks it, and the gate gives the only answer...
    ```
- `G1-15` (form `(= :hare :tortoise)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    The kitchen garden had been lovingly kept, but the sun that year had been merciless and constant.

"You can't tell which way the gate will swing by guessing,"
Loft the crow, trusting the stone-by-stone process, said. "You bring the form to the gate, the runtime
checks it, and the gate gives the only...
    ```
- `G1-15` (form `(= :hare :tortoise)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    The water sat at the bottom of the jar, deep enough to glimpse and far enough to tantalize.

"You can't tell which way the gate will swing by guessing,"
Currents the crow, deliberate and unhurried by the rising sun, said. "You bring the form to the gate, the runtime
checks it, and the gate gives the...
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

#### CLAUSE_STACK_OVERFLOW

- `G2-04` (form `(min 7 3 9 1 5)`): sentence with 5 commas reads as AI-output cadence: 'Bluster the crow simply began\ncounting carefully — to find the minimum of 6, 4, '
    ```
    In a long-dry season, Bluster found the pitcher at the market and began to consider it carefully.

Tempestcaw the crow eyed the heap, with a self-satisfied beak-click, and called out a guess
about how many stones could be dropped before the water rose high
enough, without bothering to count. Bluster...
    ```
- `G2-04` (form `(min 7 3 9 1 5)`): sentence with 5 commas reads as AI-output cadence: 'Dimsky the crow simply began\ncounting carefully — to find the minimum of 7, 6, 7'
    ```
    Dimsky alighted on the rim of a jar atop the hilltop and peered down at the small dark gleam below.

Mystery the crow eyed the heap, ruffling up with certainty, and called out a guess
about how many stones could be dropped before the water rose high
enough, without bothering to count. Dimsky the cro...
    ```
- `G2-04` (form `(max 7 3 9 1 5)`): sentence with 5 commas reads as AI-output cadence: 'To find the maximum of 5, 0, 8, 5, and 3, she composed the maximum of the number'
    ```
    in the market, where the orchard meets the well, an old clay pitcher had stood for as long as anyone could remember.

Korvus laid five unsorted stones beside the market pitcher: the counts. He wanted the heaviest stone identified from the pile.

He needed the single heaviest stone named without sort...
    ```
- `G2-04` (form `(max 7 3 9 1 5)`): sentence with 5 commas reads as AI-output cadence: 'Sapphire the crow simply began\ncounting carefully — to find the maximum of 6, 7,'
    ```
    There was once a Crow who had flown a great distance and found nothing in any pond worth dipping a beak.

Cloudshroud the crow eyed the heap, head tilted confidently to one side, and called out a guess
about how many stones could be dropped before the water rose high
enough, without bothering to cou...
    ```
- `G2-13` (form `(or nil false 5)`): sentence with 6 commas reads as AI-output cadence: 'To apply or to nil, false, and 0,\nshe composed the logical or, submitted the for'
    ```
    Drought has its own quiet way of teaching the difference between thirst and the right answer to thirst.

Cowl the crow swooped toward the pitcher on the farm, ruffling up with certainty, certain
the gate would swing open. Shout the crow watched: the only way to know
which way the gate swings is to b...
    ```

#### NARRATIVE_NUMERAL_HARDCODE

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
- `G2-18` (form `(count '(1 2 3))`): parametric example has hard-coded English numeral 'three integers' in a story slot — the actual draws may differ from this fixed count
    ```
    When Nightfall landed by the garden wall, she saw the water and saw the distance, and stood very still.

"There's a difference between *marking* the form and
*evaluating* it," Nightfall the crow, trusting the stone-by-stone process, said. "Quote in any of its
shapes is the marking — the runtime hand...
    ```
- `G5-10` (form `(map inc [1 2 3])`): parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    ```
    The kitchen garden had been lovingly kept, but the sun that year had been merciless and constant.

Caw stood at the road pitcher's sorting-perch, three stones — 1, 2, 3 — queued above the inc-sieve. Each stone would pass through the sieve before dropping into the pitcher.

She needed every stone tra...
    ```
- `G5-10` (form `(map inc [1 2 3])`): parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    ```
    An old pitcher of glazed clay sat by the garden wall, half-empty and entirely useless to anyone too proud to think.

Cinder the crow, unbothered by the slow progress, perched at the pitcher's edge,
holding a decision-rule over the stones along the road. The pile was
heavy and the rim was high; the r...
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
- `G9-18` (form `(do (def lock (Object.)) (locking lock (+ 1 2)))`): user_msg 205 words
    ```
    It had been a long, dry summer, and the rivers had pulled back from their banks in a slow and patient retreat.

Caw placed a heavy stone at the pitcher's mouth at the market to serve as a gate. Only she could move it. She rolled the stone aside, added one and two inside the sealed section, then roll...
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

Sage the crow, unhurried with form after form, patted the feathers of one wing.
"Whatever I tuck under a wing is in force only while the form runs,"
she said, "and only for the form that names the binding...
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

#### DOUBLED_INPUT_VALUE_PARENS

- `G4-12` (form `(contains? #{1 2 3} 4)`): user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
    ```
    A row of pebbles lay at the foot of the wall, sun-warmed, unremarkable, and just heavy enough.

Sable held a stone marked four near the same three-stone sorting-pile at the farm pitcher. No groove was carved for four; she asked whether it belonged.

She needed a definitive answer before adding the s...
    ```
- `G10-07` (form `(->> [1 2 3 4] (filter even?) (map inc) (reduce +))`): user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
    ```
    Smoke had flown all morning on the farm without finding so much as a damp leaf to rest a beak against.

Caw lined up the stones at the farm pitcher and scratched a last-argument drop-order: sieve the evens, raise each by one, then tally the results. The `->>` rewrite-rule would compose the whole pip...
    ```
- `G10-07` (form `(->> [1 2 3 4] (filter even?) (map inc) (reduce +))`): user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
    ```
    Word had it that Drone had flown over three valleys before finding the pitcher along the road.

Caw lined up the stones at the farm pitcher and scratched a last-argument drop-order: sieve the evens, raise each by one, then tally the results. The `->>` rewrite-rule would compose the whole pipeline.

...
    ```
- `G10-14` (form `(eval '(+ 1 2 3))`): user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
    ```
    The orchard had not seen a real rain in weeks, and even the lavender stood with its head bowed.

Caw held a chalk-marked addition form as data on the meadow pitcher's rim — a quoted list, not yet run. She used `eval` to hand the chalk mark back to the REPL to run as code.

She needed the chalk-marke...
    ```
- `G10-15` (form `(do "a function suffices when no syntax shaping is needed" (`): user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
    ```
    The orchard had not seen a real rain in weeks, and even the lavender stood with its head bowed.

Korvus held a rewrite-rule stone in one talon and a plain drop-order stone in the other at the orchard pitcher. The task was simple addition — no syntax shaping needed. He set the rewrite-rule stone down...
    ```

#### ANSWER_LEAK

- `G5-22` (form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n)`): answer 120 in narrative
    ```
    near the village, where the heat shimmered above the stones, Buffet began the slow business of solving thirst.

Caw stood at the pitcher's rim in the hilltop field, a circuit chalked beneath her feet: start with n=5 and accumulator=1. Each lap, multiply the accumulator by n, step n down by one — loo...
    ```
- `G5-22` (form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n)`): answer 120 in narrative
    ```
    On a long afternoon when even the bees had grown slow, a thirsty bird settled on the rim of a clay vessel.

Caw stood at the pitcher's rim in the hilltop field, a circuit chalked beneath her feet: start with n=5 and accumulator=1. Each lap, multiply the accumulator by n, step n down by one — loop wi...
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

#### STORY_SLOT_NOUN_REPEAT

- `G6-05` (form `(name :owner/item)`): the noun 'the local name' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    ```
    The water sat at the bottom of the jar, deep enough to glimpse and far enough to tantalize.

Korvus inspected the same two-part keyword stone at the market: shelf's name before the slash, local name after. This time he needed the local name — what the thing was called inside the shelf.

He needed th...
    ```
- `G6-05` (form `(name :owner/item)`): the noun 'the local name' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    ```
    In a year when the wells ran low, a single jar of water was a small kingdom unto itself.

Murk the crow, patient as the water rose, pressed a talon-tip into the
pitcher's clay rim near the orchard, carving a name with care. The clay was
soft only briefly; once dry, the carving would last for every l...
    ```
- `G6-05` (form `(name :owner/item)`): the noun 'the local name' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    ```
    Some problems cannot be hurried; they only respond to the slow addition of small things.

"Naming is half the art," Tarwing the crow, steady in the stone-by-stone approach, said, scoring a careful mark
into the pitcher's clay. "A clear carving tells every later crow what to
expect; a careless one tr...
    ```
- `G8-04` (form `(do (defprotocol Pace (speed [this])) (some? Pace))`): the noun 'the guild's' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    ```
    An old pitcher of glazed clay sat by the garden wall, half-empty and entirely useless to anyone too proud to think.

"Each guild has its own boundaries," Soothe the crow, unbothered by the slow progress, said. "Belonging to
the stone-drop guild doesn't mean belonging to the inscription guild —
the r...
    ```
- `G8-04` (form `(do (defprotocol Pace (speed [this])) (some? Pace))`): the noun 'the guild's' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    ```
    at the edge of the garden, where the orchard meets the well, an old clay pitcher had stood for as long as anyone could remember.

Tailwind the crow, dropping each stone with careful attention, held up the guild ledger in the garden.
The day's pitcher was narrow and the drop-orders many; the ledger
w...
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

#### ABSTRACT_RESULT_NARRATION

- `G7-06` (form `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)`): meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns
    ```
    On a long afternoon when even the bees had grown slow, a thirsty bird settled on the rim of a clay vessel.

Galena the crow, watching the level lift, spread a patch of soft moss
beneath the pitcher on the hilltop — the day was hot, the throat was narrow, and any
pebble flung wrong without a cushion ...
    ```
- `G7-06` (form `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)`): meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns
    ```
    at the market, a single pitcher held the last of the water, and Sable arrived too parched to be picky.

"What matters when a stone goes wrong," Sable the crow, calm and methodical, said, "is that
the drop can continue — the runtime catches the slip, takes the recovery
path, and the water level comes...
    ```
- `G7-06` (form `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)`): meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns
    ```
    On a long afternoon when even the bees had grown slow, a thirsty bird settled on the rim of a clay vessel.

"This patch of moss is the practice area," Tower the crow, deliberate and unhurried by the rising sun, said in the village.
"A stumble here costs nothing. Drop the form, see what comes back, f...
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

