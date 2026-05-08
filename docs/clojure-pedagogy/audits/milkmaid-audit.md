# milkmaid curriculum audit

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
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 3}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`-3` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`-3` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`-25` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-03: Ratios

- examples: 5
- variety @ n=50: 1.00
- issues: {'CONCEPT_PHRASE_FORM_PREFIX': 9, 'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [CONCEPT_PHRASE_FORM_PREFIX] form=`(+ 1/2 1/4)` — example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(+ 1/2 1/4)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [CONCEPT_PHRASE_FORM_PREFIX] form=`(+ 1/2 1/4)` — example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(+ 1/2 1/4)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [CONCEPT_PHRASE_FORM_PREFIX] form=`(+ 1/2 1/4)` — example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    - [CONCEPT_PHRASE_FORM_PREFIX] form=`(* 2 1/2)` — example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)

### G1-05: Booleans

- examples: 6
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 4}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`false` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(= 1 1)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(= 1 2)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(= 1 2)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-06: nil

- examples: 5
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 3}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(nil? nil)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(nil? nil)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
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
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(char? \h)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-09: Symbols vs values

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(= 'hare 'hare)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-10: Comments

- examples: 2
- variety @ n=50: 1.00
- issues: {'THE_FORM_OVERUSE': 1, 'TRAILING_PARTICIPLE_CLOSER': 4, 'REPL_TRIPLE_VOICE': 1}
    - [THE_FORM_OVERUSE] form=`(+ 1 2) ; sum of one and two` — `the form` appears 6 times in user_msg (template tic — vary references)
    - [TRAILING_PARTICIPLE_CLOSER] form=`(+ 1 2) ; sum of one and two` — sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(+ 1 2) ; sum of one and two` — sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    - [REPL_TRIPLE_VOICE] form=`(+ 1 2) ; sum of one and two` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [TRAILING_PARTICIPLE_CLOSER] form=`(+ 1 2) ; sum of one and two` — sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`42 ;; the answer` — sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead

### G1-11: Whitespace doesn't matter

- examples: 2
- variety @ n=50: 1.00
- issues: {'THE_FORM_OVERUSE': 2}
    - [THE_FORM_OVERUSE] form=`(+    1    2)` — `the form` appears 6 times in user_msg (template tic — vary references)
    - [THE_FORM_OVERUSE] form=`(+
  1
  2)` — `the form` appears 6 times in user_msg (template tic — vary references)

### G1-12: Parens group; they don't multiply

- examples: 2
- variety @ n=50: 1.00
- issues: {'THE_FORM_OVERUSE': 3}
    - [THE_FORM_OVERUSE] form=`(+ 2 3)` — `the form` appears 6 times in user_msg (template tic — vary references)
    - [THE_FORM_OVERUSE] form=`(* (+ 1 2) 3)` — `the form` appears 6 times in user_msg (template tic — vary references)
    - [THE_FORM_OVERUSE] form=`(* (+ 1 2) 3)` — `the form` appears 6 times in user_msg (template tic — vary references)

### G1-13: First arithmetic call

- examples: 6
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1, 'REPL_TRIPLE_VOICE': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(* 4 5)` — sentence closes with a participial coda (', wearing his pride like a bright cloak.') — LLM-cadence; close on the verb instead
    - [REPL_TRIPLE_VOICE] form=`(/ 10 2)` — user_msg mentions 'REPL' 5 times — the REPL personification should appear at most twice per record (submit + return)

### G1-14: Nested call evaluation

- examples: 4
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1}
    - [REPL_TRIPLE_VOICE] form=`(- 100 (* 5 5))` — user_msg mentions 'REPL' 4 times — the REPL personification should appear at most twice per record (submit + return)

### G1-15: Equality

- examples: 6
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(= 1 1)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(= 1 2)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-16: Numeric predicates

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(pos? 7)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-17: Printing vs returning

- examples: 2
- variety @ n=50: 1.00
- issues: {'PROCEDURAL_OPENER': 2}
    - [PROCEDURAL_OPENER] form=`(+ 1 2)` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    - [PROCEDURAL_OPENER] form=`(+ 1 2)` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence

### G1-18: Errors are safe in the REPL

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOWERCASE_CONCEPT_AFTER_PERIOD': 2, 'REPL_TRIPLE_VOICE': 1}
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(+ 1 2)` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(* 7 6)` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    - [REPL_TRIPLE_VOICE] form=`(* 7 6)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

## Grade 2

### G2-01: Multi-arg arithmetic

- examples: 6
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(* 2 3 4)` — sentence with 6 commas reads as AI-output cadence: '"To multiply 9, 7, and 9, we must count — truly count, and the multi-arg product'
    - [TRAILING_PARTICIPLE_CLOSER] form=`(- 100 1 2 3)` — sentence closes with a participial coda (', needing the true total after all losses.') — LLM-cadence; close on the verb instead

### G2-02: Comparison chains

- examples: 5
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(> 5 4 3 2 1)` — user_msg 201 words

### G2-03: not= and = with multiple args

- examples: 5
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(= 1 1 1)` — sentence with 6 commas reads as AI-output cadence: '"To test whether 1, 1, and 1 are all equal, we must count — truly count, and the'
    - [CLAUSE_STACK_OVERFLOW] form=`(= 1 1 1)` — sentence with 6 commas reads as AI-output cadence: '"To test whether 1, 1, and 1 are all equal, we must count — truly count, and the'

### G2-04: min and max

- examples: 5
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1, 'CLAUSE_STACK_OVERFLOW': 3}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(max 1 2 3)` — sentence closes with a participial coda (', tossing his head as a proud horse tosses its mane.') — LLM-cadence; close on the verb instead
    - [CLAUSE_STACK_OVERFLOW] form=`(max 1 2 3)` — sentence with 6 commas reads as AI-output cadence: '"To find the maximum of 1, 5, and 3, we must count — truly count, and the msever'
    - [CLAUSE_STACK_OVERFLOW] form=`(min -3 -1 -5)` — sentence with 6 commas reads as AI-output cadence: '"To find the minimum of -84, -75, and -27, we must count — truly count, and thes'
    - [CLAUSE_STACK_OVERFLOW] form=`(min -3 -1 -5)` — sentence with 6 commas reads as AI-output cadence: '"To find the minimum of -11, -17, and -31, we must count — truly count, and thes'

### G2-05: quot, rem, mod

- examples: 6
- variety @ n=50: 1.00
- issues: {'PROCEDURAL_OPENER': 1, 'ANSWER_LEAK': 1}
    - [PROCEDURAL_OPENER] form=`(quot 17 5)` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    - [ANSWER_LEAK] form=`(mod -7 3)` — answer 7 in narrative

### G2-06: inc and dec

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(inc 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-10: Powers via repeated multiplication

- examples: 4
- variety @ n=50: 1.00
- issues: {'PARAGRAPH_FRAGMENTATION': 4}
    - [PARAGRAPH_FRAGMENTATION] form=`(* 5 5)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [PARAGRAPH_FRAGMENTATION] form=`(* 3 3 3 3)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [PARAGRAPH_FRAGMENTATION] form=`(* 10 10)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [PARAGRAPH_FRAGMENTATION] form=`(* 10 10)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G2-11: String concatenation with str

- examples: 4
- variety @ n=50: 1.00
- issues: {'PARAGRAPH_FRAGMENTATION': 1, 'LOW_GROUNDING': 1}
    - [PARAGRAPH_FRAGMENTATION] form=`(str "p" "q" "r")` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [LOW_GROUNDING] form=`(str 1 "+" 2 "=" 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-13: and / or — short circuit, return values

- examples: 6
- variety @ n=50: 1.00
- issues: {'REPEATED_OPENER_FRAGMENT': 1, 'LOW_GROUNDING': 1, 'PARAGRAPH_FRAGMENTATION': 2}
    - [REPEATED_OPENER_FRAGMENT] form=`(or false true)` — opener fragment 'pail balanced carefully on her head' also appears later in user_msg
    - [LOW_GROUNDING] form=`(or false false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PARAGRAPH_FRAGMENTATION] form=`(or false false)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [PARAGRAPH_FRAGMENTATION] form=`(or nil false 5)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G2-14: not — turning truthy to false

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'PARAGRAPH_FRAGMENTATION': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [LOW_GROUNDING] form=`(not false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PARAGRAPH_FRAGMENTATION] form=`(not nil)` — user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [TRAILING_PARTICIPLE_CLOSER] form=`(not nil)` — sentence closes with a participial coda (', flipping the falsey value to its truthy opposite.') — LLM-cadence; close on the verb instead

### G2-15: Falsey values: only false and nil

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(if nil 1 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-16: Truthy 0 and empty string

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_SLOT_NOUN_REPEAT': 3}
    - [STORY_SLOT_NOUN_REPEAT] form=`(boolean "")` — the noun 'the empty string' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(boolean "")` — the noun 'the empty string' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(boolean "")` — the noun 'the empty string' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats

### G2-17: Keyword as function for map lookup

- examples: 3
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 3, 'LOW_GROUNDING': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(:hare {:hare 1 :tortoise 2})` — sentence closes with a participial coda (', moving the cream to\nthe left and the curds to the right.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(:tortoise {:hare 1 :tortoise 2})` — sentence closes with a participial coda (', moving the cream to\nthe left and the curds to the right.') — LLM-cadence; close on the verb instead
    - [LOW_GROUNDING] form=`(:tortoise {:hare 1 :tortoise 2})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [TRAILING_PARTICIPLE_CLOSER] form=`(:missing {:hare 1})` — sentence closes with a participial coda (', moving the cream to\nthe left and the curds to the right.') — LLM-cadence; close on the verb instead

### G2-18: Quoting symbols

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(= (quote tortoise) 'tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-19: Auto-promotion to bigint

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 2}
    - [REPL_TRIPLE_VOICE] form=`(* 1000000 1000000)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`(* 1000000 1000000)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G2-20: Counting

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOWERCASE_CONCEPT_AFTER_PERIOD': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLED_PLACE': 1}
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(count [1 2 3])` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'The REPL walked the collection carrying the tally:\n\n20, 16, 20, and 12 returned:'
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(count "hello")` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(count [])` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    - [DOUBLED_PLACE] form=`(count [])` — location stutter: 'farm by the farm...'

### G2-21: String length and substring

- examples: 3
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [ANSWER_LEAK] form=`(count "tortoise")` — answer 6 in narrative
    - [PARAGRAPH_FRAGMENTATION] form=`(count "hare")` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G2-22: Compose pure arithmetic (multi-step calculation)

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(- (* 5 4) 7)` — sentence with 5 commas reads as AI-output cadence: '"To compute 7 times 8, then subtract 0, we must count — truly count, and the nes'

## Grade 3

### G3-02: def — redefinition

- examples: 1
- variety @ n=50: 1.00
- issues: {'ONLY_SHOOK_HEAD_TIC': 1}
    - [ONLY_SHOOK_HEAD_TIC] form=`(do (def x 1) (def x 99) x)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

### G3-03: let — local binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3, 'TRAILING_PARTICIPLE_CLOSER': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(let [x 3] (+ x 1))` — sentence with 6 commas reads as AI-output cadence: 'She arrived with\na form, saying, "To bind a value of 5 to a local name x for one'
    - [TRAILING_PARTICIPLE_CLOSER] form=`(let [x 3] (+ x 1))` — sentence closes with a participial coda (',\npatting her side.') — LLM-cadence; close on the verb instead
    - [CLAUSE_STACK_OVERFLOW] form=`(let [n 10] (* n n))` — sentence with 5 commas reads as AI-output cadence: 'She arrived with\na form, saying, "To bind n to 9 and compute n squared, first tu'
    - [TRAILING_PARTICIPLE_CLOSER] form=`(let [n 10] (* n n))` — sentence closes with a participial coda (',\npatting her side.') — LLM-cadence; close on the verb instead
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a 5] a)` — sentence with 5 commas reads as AI-output cadence: 'He arrived with\na form, saying, "To bind a to 1 and return it, first tuck the va'
    - [TRAILING_PARTICIPLE_CLOSER] form=`(let [a 5] a)` — sentence closes with a participial coda (',\npatting her side.') — LLM-cadence; close on the verb instead

### G3-04: let — multi-binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'ONLY_SHOOK_HEAD_TIC': 1}
    - [ONLY_SHOOK_HEAD_TIC] form=`(let [a 1 b 2] (+ a b))` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

### G3-05: let — shadowing outer def

- examples: 2
- variety @ n=50: 1.00
- issues: {'PARAGRAPH_FRAGMENTATION': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'STORY_SLOT_NOUN_REPEAT': 3, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [PARAGRAPH_FRAGMENTATION] form=`(do (def x 10) (let [x 99] x))` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def x 10) (let [x 99] x) x)` — sentence with 7 commas reads as AI-output cadence: 'He arrived with\na form, saying, "To define x, shadow it in a let, then look up x'
    - [STORY_SLOT_NOUN_REPEAT] form=`(do (def x 10) (let [x 99] x) x)` — the noun 'the market-board' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (def x 10) (let [x 99] x) x)` — sentence closes with a participial coda (',\npatting her side.') — LLM-cadence; close on the verb instead
    - [STORY_SLOT_NOUN_REPEAT] form=`(do (def x 10) (let [x 99] x) x)` — the noun 'the market-board' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(do (def x 10) (let [x 99] x) x)` — the noun 'the market-board' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats

### G3-06: let — binding can reference prior

- examples: 2
- variety @ n=50: 1.00
- issues: {'ONLY_SHOOK_HEAD_TIC': 2, 'HIGH_LENGTH': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [ONLY_SHOOK_HEAD_TIC] form=`(let [a 5 b (* a 2)] b)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [HIGH_LENGTH] form=`(let [a 5 b (* a 2)] b)` — user_msg 215 words
    - [ONLY_SHOOK_HEAD_TIC] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [PARAGRAPH_FRAGMENTATION] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G3-09: defn — shorthand

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — user_msg 223 words

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2}
    - [HIGH_LENGTH] form=`(#(+ % 1) 5)` — user_msg 223 words
    - [HIGH_LENGTH] form=`(#(* %1 %2) 3 4)` — user_msg 203 words

### G3-11: Substitution rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'ONLY_SHOOK_HEAD_TIC': 2, 'CLAUSE_STACK_OVERFLOW': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [ONLY_SHOOK_HEAD_TIC] form=`(let [a 7] (+ a a))` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [ONLY_SHOOK_HEAD_TIC] form=`((fn [x] (* x x)) 6)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [CLAUSE_STACK_OVERFLOW] form=`((fn [x] (* x x)) 6)` — sentence with 5 commas reads as AI-output cadence: 'He arrived with\na form, saying, "To apply a function that squares its argument t'
    - [TRAILING_PARTICIPLE_CLOSER] form=`((fn [x] (* x x)) 6)` — sentence closes with a participial coda (',\npatting her side.') — LLM-cadence; close on the verb instead

### G3-12: Scope vs namespace

- examples: 1
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2, 'HIGH_LENGTH': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (def g 5) (let [g 99] (+ g 1)))` — sentence closes with a participial coda (', shadowing the top-level def.') — LLM-cadence; close on the verb instead
    - [HIGH_LENGTH] form=`(do (def g 5) (let [g 99] (+ g 1)))` — user_msg 217 words
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (def g 5) (let [g 99] (+ g 1)))` — sentence closes with a participial coda (', shadowing the top-level def.') — LLM-cadence; close on the verb instead

### G3-14: do form

- examples: 2
- variety @ n=50: 1.00
- issues: {'THE_FORM_OVERUSE': 3}
    - [THE_FORM_OVERUSE] form=`(do 1 2 3)` — `the form` appears 6 times in user_msg (template tic — vary references)
    - [THE_FORM_OVERUSE] form=`(do (+ 1 1) (+ 2 2) (+ 3 3))` — `the form` appears 6 times in user_msg (template tic — vary references)
    - [THE_FORM_OVERUSE] form=`(do (+ 1 1) (+ 2 2) (+ 3 3))` — `the form` appears 6 times in user_msg (template tic — vary references)

### G3-15: Side-effects in body

- examples: 1
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2, 'HIGH_LENGTH': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (println "hi") 42)` — sentence closes with a participial coda (', ignoring the intermediate println side-effect.') — LLM-cadence; close on the verb instead
    - [HIGH_LENGTH] form=`(do (println "hi") 42)` — user_msg 207 words
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (println "hi") 42)` — sentence closes with a participial coda (', ignoring the intermediate println side-effect.') — LLM-cadence; close on the verb instead

### G3-18: When to name vs inline

- examples: 2
- variety @ n=50: 1.00
- issues: {'ONLY_SHOOK_HEAD_TIC': 2}
    - [ONLY_SHOOK_HEAD_TIC] form=`(let [n 5] (* n n n))` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [ONLY_SHOOK_HEAD_TIC] form=`(let [n 5] (* n n n))` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

## Grade 4

### G4-01: Vector literal

- examples: 3
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 4, 'LOW_GROUNDING': 2, 'PARAGRAPH_FRAGMENTATION': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`[1 2 3]` — sentence closes with a participial coda (', moving the cream to\nthe left and the curds to the right.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`[1 2 3]` — sentence closes with a participial coda (', moving the cream to\nthe left and the curds to the right.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`[]` — sentence closes with a participial coda (', moving the cream to\nthe left and the curds to the right.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`["a" "b"]` — sentence closes with a participial coda (', moving the cream to\nthe left and the curds to the right.') — LLM-cadence; close on the verb instead
    - [LOW_GROUNDING] form=`["a" "b"]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PARAGRAPH_FRAGMENTATION] form=`["a" "b"]` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G4-03: conj — append to vector

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'STORY_SLOT_NOUN_REPEAT': 3}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(conj [1 2] 3)` — sentence closes with a participial coda (', moving the cream to\nthe left and the curds to the right.') — LLM-cadence; close on the verb instead
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(conj [1 2] 3)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [STORY_SLOT_NOUN_REPEAT] form=`(conj [] :hare)` — the noun 'the keyword' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(conj [] :hare)` — the noun 'the keyword' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(conj [] :hare)` — the noun 'the keyword' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats

### G4-04: List literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`'()` — sentence closes with a participial coda (', moving the cream to\nthe left and the curds to the right.') — LLM-cadence; close on the verb instead

### G4-05: cons — prepend to seq

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2}
    - [HIGH_LENGTH] form=`(cons 0 '(1 2 3))` — user_msg 207 words
    - [HIGH_LENGTH] form=`(cons 0 '(1 2 3))` — user_msg 205 words

### G4-07: get — map lookup

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1, 'LOW_GROUNDING': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(get {:a 1 :b 2} :a)` — sentence closes with a participial coda (', moving the cream to\nthe left and the curds to the right.') — LLM-cadence; close on the verb instead
    - [LOW_GROUNDING] form=`(get {:a 1} :missing :default)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-08: assoc — map update

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 3, 'HIGH_LENGTH': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(assoc {:a 1} :b 2)` — sentence closes with a participial coda (', moving the cream to\nthe left and the curds to the right.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(assoc {:a 1} :a 99)` — sentence closes with a participial coda (', moving the cream to\nthe left and the curds to the right.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(assoc {:a 1} :a 99)` — sentence closes with a participial coda (', moving the cream to\nthe left and the curds to the right.') — LLM-cadence; close on the verb instead
    - [HIGH_LENGTH] form=`(assoc {:a 1} :a 99)` — user_msg 201 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(assoc {:a 1} :a 99)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G4-09: dissoc — map remove key

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [HIGH_LENGTH] form=`(dissoc {:a 1 :b 2} :a)` — user_msg 210 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(dissoc {:a 1 :b 2} :a)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [TRAILING_PARTICIPLE_CLOSER] form=`(dissoc {:a 1 :b 2} :a)` — sentence closes with a participial coda (', moving the cream to\nthe left and the curds to the right.') — LLM-cadence; close on the verb instead

### G4-11: Set literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'LOW_GROUNDING': 1}
    - [HIGH_LENGTH] form=`(count #{1 2 3})` — user_msg 201 words
    - [HIGH_LENGTH] form=`(count #{1 1 1})` — user_msg 204 words
    - [LOW_GROUNDING] form=`(count #{1 1 1})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-12: Set membership

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2, 'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(contains? #{1 2 3} 2)` — sentence closes with a participial coda (', moving the cream to\nthe left and the curds to the right.') — LLM-cadence; close on the verb instead
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(contains? #{1 2 3} 4)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [TRAILING_PARTICIPLE_CLOSER] form=`(contains? #{1 2 3} 4)` — sentence closes with a participial coda (', moving the cream to\nthe left and the curds to the right.') — LLM-cadence; close on the verb instead
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(contains? #{1 2 3} 4)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G4-13: count — universal

- examples: 4
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count {:a 1 :b 2})` — sentence closes with a participial coda (', moving the cream to\nthe left and the curds to the right.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count {:a 1 :b 2})` — sentence closes with a participial coda (', moving the cream to\nthe left and the curds to the right.') — LLM-cadence; close on the verb instead

### G4-14: empty?

- examples: 3
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2, 'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(empty? [])` — sentence closes with a participial coda (', moving the cream to\nthe left and the curds to the right.') — LLM-cadence; close on the verb instead
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(empty? [])` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(empty? [1])` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [TRAILING_PARTICIPLE_CLOSER] form=`(empty? "")` — sentence closes with a participial coda (', moving the cream to\nthe left and the curds to the right.') — LLM-cadence; close on the verb instead

### G4-15: first, rest, last

- examples: 3
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 4}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(first [10 20 30])` — sentence closes with a participial coda (', moving the cream to\nthe left and the curds to the right.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(last [10 20 30])` — sentence closes with a participial coda (', moving the cream to\nthe left and the curds to the right.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(last [10 20 30])` — sentence closes with a participial coda (', getting the last element does not alter the first basket.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(last [10 20 30])` — sentence closes with a participial coda (', getting the last element does not alter the first basket.') — LLM-cadence; close on the verb instead

### G4-16: into and conj on collections

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(into #{} [1 2 2 3])` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G4-17: Immutability — assoc returns new

- examples: 1
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(let [m {:a 1}] (assoc m :a 99) m)` — sentence closes with a participial coda (', moving the cream to\nthe left and the curds to the right.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(let [m {:a 1}] (assoc m :a 99) m)` — sentence closes with a participial coda (', moving the cream to\nthe left and the curds to the right.') — LLM-cadence; close on the verb instead

### G4-19: range and seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'LOW_GROUNDING': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(count (range 5))` — sentence with 5 commas reads as AI-output cadence: 'The milkmaid walked the market road, counting off each milestone: 0, 1, 2, 3, 4'
    - [LOW_GROUNDING] form=`(count (range 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(count (range 5))` — sentence with 5 commas reads as AI-output cadence: 'The milkmaid walked the market road, counting off each milestone: 0, 1, 2, 3, 4'
    - [TRAILING_PARTICIPLE_CLOSER] form=`(first (range 1 100))` — sentence closes with a participial coda (', moving the cream to\nthe left and the curds to the right.') — LLM-cadence; close on the verb instead

### G4-20: Collection vs sequence

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(seq [])` — sentence closes with a participial coda (', moving the cream to\nthe left and the curds to the right.') — LLM-cadence; close on the verb instead

## Grade 5

### G5-01: if

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOWERCASE_CONCEPT_AFTER_PERIOD': 2, 'LOW_GROUNDING': 1}
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(if true :a :b)` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    - [LOW_GROUNDING] form=`(if false :a :b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
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
- issues: {'LOW_GROUNDING': 1, 'LOWERCASE_CONCEPT_AFTER_PERIOD': 1}
    - [LOW_GROUNDING] form=`(when true :yes)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(when false :yes)` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)

### G5-06: case

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOWERCASE_CONCEPT_AFTER_PERIOD': 3}
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(case 2 1 :one 2 :two 3 :three :default)` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
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

### G5-10: map

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(map #(* % %) [1 2 3 4])` — user_msg 201 words

### G5-11: filter

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(filter even? [1 2 3 4])` — parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(filter even? [1 2 3 4])` — parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(filter even? [1 2 3 4])` — parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(filter pos? [-2 -1 0 1 2])` — parametric example has hard-coded English numeral 'Five counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(filter pos? [-2 -1 0 1 2])` — parametric example has hard-coded English numeral 'Five counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(filter pos? [-2 -1 0 1 2])` — parametric example has hard-coded English numeral 'Five counts' in a story slot — the actual draws may differ from this fixed count

### G5-12: reduce

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 3, 'LOWERCASE_CONCEPT_AFTER_PERIOD': 2, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [HIGH_LENGTH] form=`(reduce + [1 2 3 4])` — user_msg 212 words
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(reduce * [1 2 3 4 5])` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(reduce * [1 2 3 4 5])` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    - [TRAILING_PARTICIPLE_CLOSER] form=`(reduce * [1 2 3 4 5])` — sentence closes with a participial coda (', computing their product becomes.') — LLM-cadence; close on the verb instead
    - [HIGH_LENGTH] form=`(reduce max [3 1 4 1 5 9 2 6])` — user_msg 207 words
    - [HIGH_LENGTH] form=`(reduce max [3 1 4 1 5 9 2 6])` — user_msg 208 words

### G5-13: reduce with init

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(reduce + 100 [1 2 3])` — user_msg 206 words

### G5-14: apply

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'HIGH_LENGTH': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply + [1 2 3 4])` — parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply + [1 2 3 4])` — parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    - [HIGH_LENGTH] form=`(apply + [1 2 3 4])` — user_msg 202 words
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply + [1 2 3 4])` — parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply max [3 1 4 1 5])` — parametric example has hard-coded English numeral 'five counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply max [3 1 4 1 5])` — parametric example has hard-coded English numeral 'five counts' in a story slot — the actual draws may differ from this fixed count

### G5-16: partial

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(map (partial * 3) [1 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G5-18: some

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(some even? [1 3 5 8 7])` — parametric example has hard-coded English numeral 'five counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(some even? [1 3 5 8 7])` — parametric example has hard-coded English numeral 'five counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(some even? [1 3 5 8 7])` — parametric example has hard-coded English numeral 'five counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(some neg? [1 2 3])` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(some neg? [1 2 3])` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(some neg? [1 2 3])` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count

### G5-19: every?

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'CLAUSE_STACK_OVERFLOW': 2, 'HIGH_LENGTH': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(every? pos? [1 2 3])` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(every? pos? [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To check if all elements in the vector containing 1, 2, and 3 are positive, he c'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(every? pos? [1 2 3])` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(every? pos? [1 2 3])` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(every? even? [1 2 3])` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(every? even? [1 2 3])` — parametric example has hard-coded English numeral 'three counts' in a story slot — the actual draws may differ from this fixed count

### G5-20: take and drop

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(take 3 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'five counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(take 3 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'five counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(take 3 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'five counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(drop 2 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'five counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(drop 2 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'five counts' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(drop 2 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'five counts' in a story slot — the actual draws may differ from this fixed count

### G5-22: recur — first taste

- examples: 1
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — user_msg 207 words
    - [CLAUSE_STACK_OVERFLOW] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — sentence with 5 commas reads as AI-output cadence: 'Every morning, Katarzyna, his own praise his favourite song walked the same path'

## Grade 6

### G6-01: Namespace as file

- examples: 3
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 1, 'CONCEPT_AS_VERB': 1, 'ONLY_SHOOK_HEAD_TIC': 1}
    - [LOW_GROUNDING] form=`(name 'foo.bar)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(name 'clojure.string)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [ONLY_SHOOK_HEAD_TIC] form=`(name 'clojure.string)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

### G6-02: ns form

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(name 'race.tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-03: require

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1, 'ONLY_SHOOK_HEAD_TIC': 1}
    - [CONCEPT_AS_VERB] form=`(clojure.string/upper-case "hare")` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [ONLY_SHOOK_HEAD_TIC] form=`(clojure.string/upper-case "hare")` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

### G6-04: refer and use

- examples: 1
- variety @ n=50: 1.00
- issues: {'DOUBLED_INPUT_VALUE_PARENS': 1}
    - [DOUBLED_INPUT_VALUE_PARENS] form=`(= (clojure.string/upper-case "x") (clojure.string` — user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it

### G6-05: Fully qualified names

- examples: 4
- variety @ n=50: 0.99
- issues: {'CONCEPT_AS_VERB': 2, 'ONLY_SHOOK_HEAD_TIC': 2, 'LOW_GROUNDING': 2, 'TRAILING_PARTICIPLE_CLOSER': 2}
    - [CONCEPT_AS_VERB] form=`(clojure.string/reverse "abc")` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [ONLY_SHOOK_HEAD_TIC] form=`(clojure.string/reverse "abc")` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [LOW_GROUNDING] form=`(namespace :owner/item)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [TRAILING_PARTICIPLE_CLOSER] form=`(namespace :owner/item)` — sentence closes with a participial coda (', ignoring the entry name after the slash.') — LLM-cadence; close on the verb instead
    - [LOW_GROUNDING] form=`(namespace :owner/item)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [TRAILING_PARTICIPLE_CLOSER] form=`(namespace :owner/item)` — sentence closes with a participial coda (', ignoring the entry name after the slash.') — LLM-cadence; close on the verb instead

### G6-06: Private defs

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_SLOT_NOUN_REPEAT': 3, 'CONCEPT_AS_VERB': 2, 'ONLY_SHOOK_HEAD_TIC': 2}
    - [STORY_SLOT_NOUN_REPEAT] form=`(:private (meta '^:private x))` — the noun 'the board entry' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(:private (meta '^:private x))` — the noun 'the board entry' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(:private (meta '^:private x))` — the noun 'the board entry' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [CONCEPT_AS_VERB] form=`(:private (meta 'x))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [ONLY_SHOOK_HEAD_TIC] form=`(:private (meta 'x))` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [CONCEPT_AS_VERB] form=`(:private (meta 'x))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

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
- issues: {'ONLY_SHOOK_HEAD_TIC': 1, 'HIGH_LENGTH': 1, 'LOW_GROUNDING': 1}
    - [ONLY_SHOOK_HEAD_TIC] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [HIGH_LENGTH] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg 210 words
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-10: Leiningen and deps.edn

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1}
    - [HEDGING_NEAR_FORM] form=`(:deps {:deps {:a 1 :b 2}})` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value

### G6-11: Classpath

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1}
    - [HEDGING_NEAR_FORM] form=`(clojure.string/split "src:test" #":")` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value

### G6-12: Multiple files in one project

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(count ['race.tortoise 'race.hare 'race.shared])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

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
- issues: {'REPL_TRIPLE_VOICE': 1}
    - [REPL_TRIPLE_VOICE] form=`(try (throw (Exception. "bad")) (catch Exception e` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G7-02: try / catch

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(try 42 (catch Exception e :caught))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-03: try / finally

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 3}
    - [REPL_TRIPLE_VOICE] form=`(try 7 (finally (prn :cleanup)))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`(try (try (/ 1 0) (finally (prn :ran))) (catch Exc` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`(try (try (/ 1 0) (finally (prn :ran))) (catch Exc` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G7-04: ex-info

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'REPL_TRIPLE_VOICE': 2}
    - [LOW_GROUNDING] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [REPL_TRIPLE_VOICE] form=`(try (throw (ex-info "x" {:k :v})) (catch Exceptio` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`(try (throw (ex-info "x" {:k :v})) (catch Exceptio` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G7-05: nil punning

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'REPL_TRIPLE_VOICE': 2, 'LOWERCASE_CONCEPT_AFTER_PERIOD': 1}
    - [LOW_GROUNDING] form=`(some? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(some? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(some? 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [REPL_TRIPLE_VOICE] form=`(some? 0)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(first nil)` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    - [LOW_GROUNDING] form=`(first nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-06: pre and post conditions

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'ABSTRACT_RESULT_NARRATION': 3, 'LOWERCASE_CONCEPT_AFTER_PERIOD': 2}
    - [LOW_GROUNDING] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [ABSTRACT_RESULT_NARRATION] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns
    - [ABSTRACT_RESULT_NARRATION] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns
    - [LOW_GROUNDING] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [ABSTRACT_RESULT_NARRATION] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exce` — sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)

### G7-07: assert

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 3, 'DOUBLED_PLACE': 1}
    - [REPL_TRIPLE_VOICE] form=`(do (assert (= 1 1)) 1)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`(do (assert (= 1 1)) 1)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`(do (assert (= 1 1)) 1)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [DOUBLED_PLACE] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — location stutter: 'farm on the farm...'

### G7-10: doc and source

- examples: 1
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(:doc (meta '^{:doc "adds two"} plus))` — sentence closes with a participial coda (', proving the notes were there all along.') — LLM-cadence; close on the verb instead

### G7-11: Reading stack traces

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 2, 'LOW_GROUNDING': 1}
    - [REPL_TRIPLE_VOICE] form=`(try (throw (Exception. "oops")) (catch Exception ` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`(try (throw (Exception. "oops")) (catch Exception ` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [LOW_GROUNDING] form=`(try (throw (Exception. "oops")) (catch Exception ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-18: Shell command

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [LOW_GROUNDING] form=`(count (:args {:cmd "echo" :args ["hello" "world"]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count (:args {:cmd "echo" :args ["hello" "world"]` — sentence closes with a participial coda (', proving the tool came with two clear instructions.') — LLM-cadence; close on the verb instead

## Grade 8

### G8-01: Why polymorphism

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(let [speak (fn [k] (cond (= k :hare) "swift" (= k` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [speak (fn [k] (cond (= k :hare) "swift" (= k` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-02: deftype introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — user_msg 210 words

### G8-03: defrecord introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — sentence with 5 commas reads as AI-output cadence: 'So she, with even breath and steady step, said, "To define a Runner case with tw'

### G8-04: Protocol definition

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 4, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — sentence closes with a participial coda (', nailing its charter to the guild-hall door.') — LLM-cadence; close on the verb instead
    - [LOW_GROUNDING] form=`(do (defprotocol Greet (hail [this])) (some? Greet` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Greet (hail [this])) (some? Greet` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Greet (hail [this])) (some? Greet` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-05: Protocol extension

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 2, 'CONCEPT_AS_VERB': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — user_msg 202 words
    - [HIGH_LENGTH] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — user_msg 201 words
    - [CONCEPT_AS_VERB] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'Cassius, untroubled by what others thought,\nexplained to Czeslawa: "To define a '
    - [CONCEPT_AS_VERB] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G8-06: Protocol method dispatch

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-07: Record implementing protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'CONCEPT_AS_VERB': 2}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (defrecord M` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (defrecord M` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (defrecord M` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(do (defprotocol Pace (speed [this])) (defrecord F` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(do (defprotocol Pace (speed [this])) (defrecord F` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (defrecord F` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-09: Multimethod defmethod

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defmulti pace :species) (defmethod pace :hare` — user_msg 205 words

### G8-10: Multimethod vs protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 3, 'STORY_SLOT_NOUN_REPEAT': 3}
    - [HIGH_LENGTH] form=`(do (defmulti show identity) (defmethod show :rabb` — user_msg 216 words
    - [HIGH_LENGTH] form=`(do (defprotocol Show (show [this])) (extend-proto` — user_msg 204 words
    - [STORY_SLOT_NOUN_REPEAT] form=`(do (defprotocol Show (show [this])) (extend-proto` — the noun 'the pail's' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(do (defprotocol Show (show [this])) (extend-proto` — the noun 'the pail's' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [HIGH_LENGTH] form=`(do (defprotocol Show (show [this])) (extend-proto` — user_msg 229 words
    - [STORY_SLOT_NOUN_REPEAT] form=`(do (defprotocol Show (show [this])) (extend-proto` — the noun 'the pail's' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats

### G8-11: Protocol vs Java interface

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'CONCEPT_AS_VERB': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol IPace (run [this])) (extend-proto` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol IPace (run [this])) (extend-proto` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(do (defprotocol IPace (run [this])) (extend-proto` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G8-12: extend-type on built-in types

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_SLOT_NOUN_REPEAT': 3}
    - [HIGH_LENGTH] form=`(do (defprotocol Pace (speed [this])) (extend-type` — user_msg 223 words
    - [STORY_SLOT_NOUN_REPEAT] form=`(do (defprotocol Pace (speed [this])) (extend-type` — the noun 'the string variety' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(do (defprotocol Pace (speed [this])) (extend-type` — the noun 'the string variety' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(do (defprotocol Pace (speed [this])) (extend-type` — the noun 'the string variety' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats

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
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'LOW_GROUNDING': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — sentence with 6 commas reads as AI-output cadence: 'Theodoric, untroubled by what others thought,\nexplained to Pernille: "To define '
    - [LOW_GROUNDING] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-15: derive and isa? — multimethod hierarchy

- examples: 3
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(isa? java.lang.String java.lang.Number)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(isa? java.lang.String java.lang.Number)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-16: Abstract design with protocols

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'CONCEPT_AS_VERB': 4}
    - [LOW_GROUNDING] form=`(do (defprotocol Move (step [this])) (defrecord Mi` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Move (step [this])) (defrecord Mi` — sentence with 5 commas reads as AI-output cadence: 'Ulvilda, with the slow grace of a creature unhurried,\nexplained to Genevieve: "T'
    - [CONCEPT_AS_VERB] form=`(do (defprotocol Move (step [this])) (defrecord Mi` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(do (defprotocol Sound (cry [this])) (defrecord Mi` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(do (defprotocol Sound (cry [this])) (defrecord Mi` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(do (defprotocol Sound (cry [this])) (defrecord Mi` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

## Grade 9

### G9-01: Immutability as default — review

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(let [m {:a 1}] (assoc m :b 2) m)` — sentence closes with a participial coda (', moving the cream to\nthe left and the curds to the right.') — LLM-cadence; close on the verb instead

### G9-02: Why state at all

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4, 'HIGH_LENGTH': 1, 'LOW_GROUNDING': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — sentence with 6 commas reads as AI-output cadence: "She said untroubled by what others thought, the chalk's edge cool against her\nfi"
    - [HIGH_LENGTH] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — user_msg 207 words
    - [LOW_GROUNDING] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — sentence with 5 commas reads as AI-output cadence: 'To construct an atom holding 0 as counter, atomically swap it by applying inc, a'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def progress (atom :idle)) (reset! progress :` — sentence with 6 commas reads as AI-output cadence: "She said with a hen's long stillness on the nest, the chalk's edge cool against "
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def progress (atom :idle)) (reset! progress :` — sentence with 5 commas reads as AI-output cadence: '"Each farmer submits a form for binding an atom to progress, atomically resettin'

### G9-04: Atom CAS semantics

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'LOW_GROUNDING': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — sentence with 6 commas reads as AI-output cadence: "She said with the steady turn of a millwheel, the chalk's edge cool against her\n"
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-05: Watch on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — sentence with 5 commas reads as AI-output cadence: 'To construct an atom a, construct a log atom, add a watch to a that conjoins new'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — sentence with 5 commas reads as AI-output cadence: 'To construct an atom a, construct a log atom, add a watch to a that conjoins new'

### G9-07: Ref introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` — sentence with 6 commas reads as AI-output cadence: "He said neither restless nor weary but steady, the chalk's edge cool against his"

### G9-09: Ref vs atom

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 6 commas reads as AI-output cadence: "She said with the steady measure of a long walker, the chalk's edge cool against"

### G9-10: Agent introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'LOW_GROUNDING': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [HIGH_LENGTH] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg 224 words
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 5 commas reads as AI-output cadence: '"To construct an agent holding 0, asynchronously send inc to it, await its compl'
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (def ag (agent 5)) (send ag + 10) (await ag) @` — sentence closes with a participial coda (', preparing the cart.') — LLM-cadence; close on the verb instead
    - [HIGH_LENGTH] form=`(do (def ag (agent 5)) (send ag + 10) (await ag) @` — user_msg 209 words

### G9-11: send and send-off

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 5 commas reads as AI-output cadence: '"To construct an agent holding 0, use send to asynchronously apply inc, await it'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 5 commas reads as AI-output cadence: '"To construct an agent holding 0, use send to asynchronously apply inc, await it'
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (def ag (agent 0)) (send-off ag inc) (await ag` — sentence closes with a participial coda (', preparing the cart.') — LLM-cadence; close on the verb instead

### G9-12: await — synchronizing on agents

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'LOW_GROUNDING': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — user_msg 210 words
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 5 commas reads as AI-output cadence: '"To construct an agent holding 0, asynchronously send inc twice, synchronize wit'

### G9-13: future introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`@(future (+ 1 2))` — sentence closes with a participial coda (', preparing the cart.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`@(future (* 6 7))` — sentence closes with a participial coda (', preparing the cart.') — LLM-cadence; close on the verb instead

### G9-15: promise — deliver and deref

- examples: 2
- variety @ n=50: 0.99
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (def p (promise)) (deliver p :done) @p)` — sentence closes with a participial coda (', preparing the cart.') — LLM-cadence; close on the verb instead

### G9-16: volatile — when STM is too heavy

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def v (volatile! 5)) (vreset! v 99) @v)` — sentence with 6 commas reads as AI-output cadence: "He said neither hastening nor hanging back, the chalk's edge cool against his\nfi"
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def v (volatile! 5)) (vreset! v 99) @v)` — sentence with 6 commas reads as AI-output cadence: "She said with a hen's long stillness on the nest, the chalk's edge cool against "
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def v (volatile! 5)) (vreset! v 99) @v)` — sentence with 6 commas reads as AI-output cadence: "She said with the slow certainty of the sun, the chalk's edge cool against her\nf"

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 0.99
- issues: {'GENERIC_RESOLUTION_TAIL': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'HIGH_LENGTH': 1, 'DOUBLE_PREP': 1}
    - [GENERIC_RESOLUTION_TAIL] form=`(do (def lock (Object.)) (locking lock 42))` — resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def lock (Object.)) (locking lock 42))` — sentence with 6 commas reads as AI-output cadence: "He said with the steady turn of a millwheel, the chalk's edge cool against his\nf"
    - [HIGH_LENGTH] form=`(do (def lock (Object.)) (locking lock 42))` — user_msg 207 words
    - [DOUBLE_PREP] form=`(do (def lock (Object.)) (locking lock 42))` — verb+preposition followed by {place} which already carries its own preposition
    - [GENERIC_RESOLUTION_TAIL] form=`(do (def lock (Object.)) (locking lock 42))` — resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    - [GENERIC_RESOLUTION_TAIL] form=`(do (def lock (Object.)) (locking lock 42))` — resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop

## Grade 10

### G10-01: quote, unquote, unquote-splice

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_SLOT_NOUN_REPEAT': 3, 'HIGH_LENGTH': 3, 'LOW_GROUNDING': 1}
    - [STORY_SLOT_NOUN_REPEAT] form=`(quote (+ 1 2))` — the noun 'the chalk mark' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(quote (+ 1 2))` — the noun 'the chalk mark' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [HIGH_LENGTH] form=`(quote (+ 1 2))` — user_msg 205 words
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_SLOT_NOUN_REPEAT] form=`(quote (+ 1 2))` — the noun 'the chalk mark' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [HIGH_LENGTH] form=`'(1 2 3)` — user_msg 206 words

### G10-02: syntax-quote

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(let [x 10] `(+ ~x ~x))` — user_msg 207 words

### G10-04: Macro expansion rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'MULTIPLE_SAID_TAGS': 1, 'PARAGRAPH_FRAGMENTATION': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [MULTIPLE_SAID_TAGS] form=`(macroexpand-1 '(when true 1))` — user_msg has 3 dialogue-attribution tags — over-announcing the speakers
    - [PARAGRAPH_FRAGMENTATION] form=`(macroexpand-1 '(when true 1))` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [TRAILING_PARTICIPLE_CLOSER] form=`(macroexpand-1 '(when true 1))` — sentence closes with a participial coda (', showing the expanded intermediate form.') — LLM-cadence; close on the verb instead

### G10-05: macroexpand

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(macroexpand '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(macroexpand '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-06: when and when-not as macros

- examples: 3
- variety @ n=50: 1.00
- issues: {'MULTIPLE_SAID_TAGS': 1, 'HIGH_LENGTH': 2, 'LOW_GROUNDING': 2, 'REPL_TRIPLE_VOICE': 1, 'SUBMITTED_THE_FORM_DOUBLED': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [MULTIPLE_SAID_TAGS] form=`(when true 1 2 3)` — user_msg has 3 dialogue-attribution tags — over-announcing the speakers
    - [HIGH_LENGTH] form=`(when true 1 2 3)` — user_msg 211 words
    - [LOW_GROUNDING] form=`(when true 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(when true 1 2 3)` — user_msg 209 words
    - [LOW_GROUNDING] form=`(when false 1 2 3)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [REPL_TRIPLE_VOICE] form=`(when false 1 2 3)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'DOUBLED_PLACE': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'LOW_GROUNDING': 1}
    - [HIGH_LENGTH] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — user_msg 214 words
    - [DOUBLED_PLACE] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — location stutter: 'farm on the farm...'
    - [CLAUSE_STACK_OVERFLOW] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — sentence with 5 commas reads as AI-output cadence: 'To thread a vector through filter, map, and reduce using thread-last, he wrote o'
    - [LOW_GROUNDING] form=`(macroexpand '(-> x f g))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-08: Macro vs fn

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 3, 'MULTIPLE_SAID_TAGS': 3}
    - [CONCEPT_AS_VERB] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [MULTIPLE_SAID_TAGS] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — user_msg has 3 dialogue-attribution tags — over-announcing the speakers
    - [CONCEPT_AS_VERB] form=`(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [MULTIPLE_SAID_TAGS] form=`(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3` — user_msg has 3 dialogue-attribution tags — over-announcing the speakers
    - [CONCEPT_AS_VERB] form=`(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [MULTIPLE_SAID_TAGS] form=`(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3` — user_msg has 3 dialogue-attribution tags — over-announcing the speakers

### G10-09: Hygiene and gensym

- examples: 2
- variety @ n=50: 1.00
- issues: {'GENERIC_RESOLUTION_TAIL': 3, 'MULTIPLE_SAID_TAGS': 1}
    - [GENERIC_RESOLUTION_TAIL] form=`(symbol? (gensym))` — resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    - [GENERIC_RESOLUTION_TAIL] form=`(symbol? (gensym))` — resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    - [GENERIC_RESOLUTION_TAIL] form=`(symbol? (gensym))` — resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    - [MULTIPLE_SAID_TAGS] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — user_msg has 3 dialogue-attribution tags — over-announcing the speakers

### G10-10: Anaphoric macros are confusing

- examples: 2
- variety @ n=50: 1.00
- issues: {'MULTIPLE_SAID_TAGS': 1, 'HIGH_LENGTH': 1, 'TRAILING_PARTICIPLE_CLOSER': 1, 'STORY_SLOT_NOUN_REPEAT': 3}
    - [MULTIPLE_SAID_TAGS] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — user_msg has 3 dialogue-attribution tags — over-announcing the speakers
    - [HIGH_LENGTH] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — user_msg 215 words
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — sentence closes with a participial coda (', keeping the name visible and safe.') — LLM-cadence; close on the verb instead
    - [STORY_SLOT_NOUN_REPEAT] form=`(if-let [x 7] (* x x) 0)` — the noun 'the then-branch' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(if-let [x 7] (* x x) 0)` — the noun 'the then-branch' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(if-let [x 7] (* x x) 0)` — the noun 'the then-branch' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats

### G10-11: Reader macros overview

- examples: 3
- variety @ n=50: 1.00
- issues: {'THE_FORM_OVERUSE': 2, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'HIGH_LENGTH': 1}
    - [THE_FORM_OVERUSE] form=`'(1 2 3)` — `the form` appears 7 times in user_msg (template tic — vary references)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`'(1 2 3)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [THE_FORM_OVERUSE] form=`(#(* % %) 6)` — `the form` appears 6 times in user_msg (template tic — vary references)
    - [HIGH_LENGTH] form=`[1 #_ 2 3]` — user_msg 202 words

### G10-12: Tagged literals

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(inst? #inst "2024-01-01")` — user_msg 206 words

### G10-14: eval (the function)

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 2, 'MULTIPLE_SAID_TAGS': 2}
    - [CONCEPT_AS_VERB] form=`(eval '(+ 1 2 3))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [MULTIPLE_SAID_TAGS] form=`(eval '(+ 1 2 3))` — user_msg has 3 dialogue-attribution tags — over-announcing the speakers
    - [CONCEPT_AS_VERB] form=`(eval (list '+ 4 5))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [MULTIPLE_SAID_TAGS] form=`(eval (list '+ 4 5))` — user_msg has 3 dialogue-attribution tags — over-announcing the speakers

### G10-15: When not to write a macro

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 3, 'MULTIPLE_SAID_TAGS': 3, 'HIGH_LENGTH': 1, 'DOUBLED_INPUT_VALUE_PARENS': 1}
    - [CONCEPT_AS_VERB] form=`(do "a function suffices when no syntax shaping is` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [MULTIPLE_SAID_TAGS] form=`(do "a function suffices when no syntax shaping is` — user_msg has 3 dialogue-attribution tags — over-announcing the speakers
    - [HIGH_LENGTH] form=`(do "a function suffices when no syntax shaping is` — user_msg 207 words
    - [DOUBLED_INPUT_VALUE_PARENS] form=`(do "a function suffices when no syntax shaping is` — user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
    - [CONCEPT_AS_VERB] form=`(do "prefer fn unless you must shape syntax" (map ` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [MULTIPLE_SAID_TAGS] form=`(do "prefer fn unless you must shape syntax" (map ` — user_msg has 3 dialogue-attribution tags — over-announcing the speakers

### G10-16: Macro pattern library

- examples: 2
- variety @ n=50: 1.00
- issues: {'MULTIPLE_SAID_TAGS': 3, 'STORY_SLOT_NOUN_REPEAT': 3}
    - [MULTIPLE_SAID_TAGS] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — user_msg has 3 dialogue-attribution tags — over-announcing the speakers
    - [STORY_SLOT_NOUN_REPEAT] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — the noun 'the market-board' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [MULTIPLE_SAID_TAGS] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — user_msg has 3 dialogue-attribution tags — over-announcing the speakers
    - [STORY_SLOT_NOUN_REPEAT] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — the noun 'the market-board' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [MULTIPLE_SAID_TAGS] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — user_msg has 3 dialogue-attribution tags — over-announcing the speakers
    - [STORY_SLOT_NOUN_REPEAT] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — the noun 'the market-board' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats

## Grade 11

### G11-02: Method call syntax

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_SLOT_NOUN_REPEAT': 3, 'HIGH_LENGTH': 1}
    - [STORY_SLOT_NOUN_REPEAT] form=`(.toUpperCase "abc")` — the noun 'the neighbor's' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [HIGH_LENGTH] form=`(.toUpperCase "abc")` — user_msg 210 words
    - [STORY_SLOT_NOUN_REPEAT] form=`(.toUpperCase "abc")` — the noun 'the neighbor's' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(.toUpperCase "abc")` — the noun 'the neighbor's' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats

### G11-05: Import form

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1}
    - [HEDGING_NEAR_FORM] form=`(do "import is a top-of-file ns clause" :studied)` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value

### G11-06: new and dot-construct

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 4}
    - [CONCEPT_AS_VERB] form=`(String. "go")` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(new String "leap")` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(new String "leap")` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(new String "leap")` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G11-07: Arrays

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 2}
    - [CONCEPT_AS_VERB] form=`(let [a (int-array [1 2 3])] (alength a))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(let [a (int-array [1 2 3])] (alength a))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G11-08: Type hints

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 3}
    - [CONCEPT_AS_VERB] form=`(let [^String s "abc"] (.toUpperCase s))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(let [^String s "abc"] (.toUpperCase s))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(let [^String s "abc"] (.toUpperCase s))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G11-09: Checked vs unchecked math

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_SLOT_NOUN_REPEAT': 3, 'HIGH_LENGTH': 1}
    - [STORY_SLOT_NOUN_REPEAT] form=`(+ 1 2)` — the noun 'the default checked' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(+ 1 2)` — the noun 'the default checked' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [STORY_SLOT_NOUN_REPEAT] form=`(+ 1 2)` — the noun 'the default checked' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    - [HIGH_LENGTH] form=`(do "*unchecked-math* turns off overflow checking ` — user_msg 202 words

### G11-11: cljs / JavaScript interop

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 2}
    - [HEDGING_NEAR_FORM] form=`(do "(js/console.log x) calls a JS global; (.-foo ` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [HEDGING_NEAR_FORM] form=`(do "(js/console.log x) calls a JS global; (.-foo ` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value

### G11-13: Cross-platform .cljc and reader-conditionals

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1}
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
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLED_INPUT_VALUE_PARENS': 1}
    - [HIGH_LENGTH] form=`(into [] (map inc) [1 2 3])` — user_msg 206 words
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] (map inc) [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To use the map-inc transducer with into to increment the vector containing 1, 2,'
    - [DOUBLED_INPUT_VALUE_PARENS] form=`(into [] (map inc) [1 2 3])` — user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it

### G12-02: Transducer composition

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'DOUBLED_INPUT_VALUE_PARENS': 1}
    - [HIGH_LENGTH] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — user_msg 217 words
    - [DOUBLED_INPUT_VALUE_PARENS] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it

### G12-03: into with a transducer (xform)

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(into [] (take 3) (range 100))` — sentence closes with a participial coda (', hearing her own name in an old kindness.') — LLM-cadence; close on the verb instead

### G12-05: Channels and pipelines

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'HEDGING_NEAR_FORM': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do "pipe, mult, mix, pipeline-async route values ` — sentence with 5 commas reads as AI-output cadence: 'Maeve squinted at the goal — to study how pipe, mult, mix, and pipeline-async ro'
    - [CLAUSE_STACK_OVERFLOW] form=`(do "pipe, mult, mix, pipeline-async route values ` — sentence with 5 commas reads as AI-output cadence: 'Halfway through the race, Cora, his name first in every story he told stopped by'
    - [HEDGING_NEAR_FORM] form=`(do "pipelines transform streams of values channel` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value

### G12-07: Spec generators

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 2}
    - [HEDGING_NEAR_FORM] form=`(do "s/exercise produces sample inputs for a spec"` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [HEDGING_NEAR_FORM] form=`(do "spec generators turn specs into property-base` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value

### G12-08: clojure.test

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 3}
    - [HEDGING_NEAR_FORM] form=`(= (+ 1 2) 3)` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [HEDGING_NEAR_FORM] form=`(= (+ 1 2) 3)` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [HEDGING_NEAR_FORM] form=`(do "(deftest …), (is …), (testing …) are the core` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value

### G12-10: Property-based testing

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1}
    - [HEDGING_NEAR_FORM] form=`(do "test.check generates inputs and checks proper` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value

### G12-11: Leiningen project.clj

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 2}
    - [HEDGING_NEAR_FORM] form=`(do "project.clj declares :dependencies, :main, :p` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [HEDGING_NEAR_FORM] form=`(do "project.clj declares :dependencies, :main, :p` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value

### G12-13: Aliases and tools

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1}
    - [HEDGING_NEAR_FORM] form=`(do "`clj -M:test` runs the :test alias from deps.` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value

### G12-17: Library design patterns

- examples: 3
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do "small public API surface, plain data inputs, ` — sentence closes with a participial coda (',\ntossing his head as a proud horse tosses its mane.') — LLM-cadence; close on the verb instead

---

## Summary

### Issue counts (across all examples × 3 records)

- **LOW_GROUNDING**: 69
- **TRAILING_PARTICIPLE_CLOSER**: 61
- **HIGH_LENGTH**: 51
- **CLAUSE_STACK_OVERFLOW**: 44
- **CONCEPT_AS_VERB**: 39
- **STORY_SLOT_NOUN_REPEAT**: 33
- **NARRATIVE_NUMERAL_HARDCODE**: 30
- **FORM_DISPLAY_AND_FORM_NOUN**: 28
- **ONLY_SHOOK_HEAD_TIC**: 21
- **REPL_TRIPLE_VOICE**: 20
- **LOWERCASE_CONCEPT_AFTER_PERIOD**: 19
- **HEDGING_NEAR_FORM**: 16
- **MULTIPLE_SAID_TAGS**: 15
- **PARAGRAPH_FRAGMENTATION**: 14
- **THE_FORM_OVERUSE**: 11
- **CONCEPT_PHRASE_FORM_PREFIX**: 9
- **GENERIC_RESOLUTION_TAIL**: 6
- **DOUBLED_PLACE**: 4
- **DOUBLED_INPUT_VALUE_PARENS**: 4
- **PROCEDURAL_OPENER**: 3
- **ABSTRACT_RESULT_NARRATION**: 3
- **ANSWER_LEAK**: 2
- **REPEATED_OPENER_FRAGMENT**: 1
- **DOUBLE_PREP**: 1
- **SUBMITTED_THE_FORM_DOUBLED**: 1

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 48 | — |
| 2 | 22 | 88 | 45 | — |
| 3 | 18 | 31 | 36 | — |
| 4 | 20 | 39 | 51 | — |
| 5 | 22 | 39 | 60 | — |
| 6 | 16 | 33 | 41 | — |
| 7 | 18 | 36 | 32 | — |
| 8 | 16 | 31 | 51 | — |
| 9 | 18 | 34 | 36 | — |
| 10 | 16 | 36 | 64 | — |
| 11 | 14 | 29 | 22 | — |
| 12 | 18 | 37 | 19 | — |

### Sample issues by severity

#### FORM_DISPLAY_AND_FORM_NOUN

- `G1-01` (form `nil`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

A handful of market-goers had gathered around the dairy cart
at the farm to watch Marzena, his deeds magnified in his own retelling attempt to outwit
Konstantin at reading the REPL. Konstantin poin...
    ```
- `G1-02` (form `-3`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    It was the season of new chicks and first cheeses, and every small profit felt like the start of a larger one.

A handful of market-goers had gathered around the dairy cart
by the village to watch Greta, his voice carrying over the whole tavern attempt to outwit
Anselmo at reading the REPL. Anselmo ...
    ```
- `G1-02` (form `-3`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    near the market, the dairy stood between the lane and the meadow, and the day's milk waited to be carried to town.

A handful of market-goers had gathered around the dairy cart
near the market to watch Paola, in the manner of had taken to his own legend attempt to outwit
Bartholomew at reading the R...
    ```
- `G1-02` (form `-25`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    Ingrid hummed quietly near the road as she walked, the pail steady and the future already half-spent.

A handful of market-goers had gathered around the dairy cart
on the road to watch Ingrid, taking credit for the morning sun attempt to outwit
Alaric at reading the REPL. Alaric pointed to
the integ...
    ```
- `G1-03` (form `(+ 1/2 1/4)`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    Between the dairy and the marketplace stretched a road, a hill, and an entire life imagined into being.

A handful of market-goers had gathered around the dairy cart
by the market to watch Klara, with wide pride — spares no detail attempt to outwit
Kasimir at reading the REPL. Kasimir pointed to
the...
    ```

#### CONCEPT_PHRASE_FORM_PREFIX

- `G1-03` (form `(+ 1/2 1/4)`): example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    ```
    The road from the farm to the town was long, and a daydream could fit comfortably along its length.

Ferdinand had been trying to teach Gretchen how the REPL
works. "Look here," He said, pointing to
the form (+ 1/2 1/4). "You hand the form `(+ 1/2 1/4)` to the runtime, and
the runtime hands you back...
    ```
- `G1-03` (form `(+ 1/2 1/4)`): example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    ```
    Between the dairy and the marketplace stretched a road, a hill, and an entire life imagined into being.

A handful of market-goers had gathered around the dairy cart
by the market to watch Klara, with wide pride — spares no detail attempt to outwit
Kasimir at reading the REPL. Kasimir pointed to
the...
    ```
- `G1-03` (form `(+ 1/2 1/4)`): example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    ```
    near the orchard, the road from the farmstead curved gently downhill, and Wiebke walked it with her head held high.

A handful of market-goers had gathered around the dairy cart
near the orchard to watch Wiebke, with a flourish at every mention of his name attempt to outwit
Eulalia at reading the RE...
    ```
- `G1-03` (form `(* 2 1/2)`): example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    ```
    Isabella was not a careless girl by nature, but near the hilltop the morning was bright and the daydreams were brighter.

Imelda had been keeping a careful chalk-tally on the dairy
slate of every form she had successfully evaluated —
each entry one more notch toward a steady reckoning. Today at the ...
    ```
- `G1-03` (form `(* 2 1/2)`): example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    ```
    The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

With a twig, Ottilia marked out a wager at the edge of the hilltop: whoever
guessed the result of `(* 5 1/2)` first would win the right to
choose the next contest. Wenceslas, untroubled by what others th...
    ```

#### LOW_GROUNDING

- `G1-09` (form `(= 'hare 'hare)`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    Long before the market opened its stalls, a young woman had already spent her milk three times in her head.

Two chalk marks were written on the dairy wall: 'hare' and 'hare'. The milkmaid nodded, guessing they were the same. The farmer asked: but are those symbols truly equal? Let us read them thro...
    ```
- `G1-16` (form `(pos? 7)`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    on the road, where the lane bends past the old hedge, Karin began to add up coins she had not yet earned.

The farmer held a pile of seven gold coins on the sunny side of the table. The coins caught the light. She chalked a form to ask: is this pile on the plus side — positive?

She needed a predica...
    ```
- `G2-06` (form `(inc 0)`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    by the orchard, where the lane bends past the old hedge, Mihaela began to add up coins she had not yet earned.

The farmer's pail was empty at the start of the day. The first buyer brought one pail of milk. She needed to know the new count without guessing.

She needed to add one to 2 in a single st...
    ```
- `G2-11` (form `(str 1 "+" 2 "=" 3)`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    atop the hilltop, the road from the farmstead curved gently downhill, and Eudora walked it with her head held high.

The milkmaid held a teaching cloth for children with five separate pieces: numbers and operator symbols meant to form a lesson. She needed to weave them all together.

She needed to b...
    ```
- `G2-13` (form `(or false false)`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    by the meadow, the dairy stood between the lane and the meadow, and the day's milk waited to be carried to town.

The farmer had two gates: both were blocked (both false). She wondered if the or-chain would have any way through.

She needed to test if at least one gate opened using the or operator.
...
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
crossed out, some added. "The form looks like a mess!" She, with quiet steps taking the long way, cried...
    ```
- `G1-11` (form `(+
  1
  2)`): `the form` appears 6 times in user_msg (template tic — vary references)
    ```
    A pail of milk is a small fortune to a careful walker and a lost fortune to a careless one.

Dorothea peered at Augusta's dairy wall and saw lines of chalk marks above the form. Some marks were
crossed out, some added. "The form looks like a mess!" She, carrying his head as one carrying the certaint...
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
crossed out, some added. "The form looks like a mess!" She, sure of the win with hea...
    ```

#### TRAILING_PARTICIPLE_CLOSER

- `G1-10` (form `(+ 1 2) ; sum of one and two`): sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    ```
    A pail of milk is a small fortune to a careful walker and a lost fortune to a careless one.

Ula peered at Xaverius's dairy wall and saw lines of chalk marks above the form. Some marks were
crossed out, some added. "The form looks like a mess!" She, as a victor walks before a victory is named, cried...
    ```
- `G1-10` (form `(+ 1 2) ; sum of one and two`): sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    ```
    Yelena carried more than milk that morning on the farm; she carried a whole imagined fortune.

Walther handed Yelena a piece of chalk. "Write a mark above the churn," he, stepping deliberately one foot before the next, said,
"that says what we are about to do." Yelena wrote: "Cooling the cream." The...
    ```
- `G1-10` (form `(+ 1 2) ; sum of one and two`): sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

Beside the dairy tally, the milkmaid had chalked a note: '; sum of one and two.' The note was for her own reference — the dairy buyer at market would never see the chalk wall.

She needed a way to ...
    ```
- `G1-10` (form `42 ;; the answer`): sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    ```
    Milk does not forgive a tilted head, but a dreaming mind seldom remembers as much.

Ulysses handed Margarethe a piece of chalk. "Write a mark above the churn," he, settled in for a long wait, said,
"that says what we are about to do." Margarethe wrote: "Cooling the cream." Then he showed the
form. "...
    ```
- `G1-13` (form `(* 4 5)`): sentence closes with a participial coda (', wearing his pride like a bright cloak.') — LLM-cadence; close on the verb instead
    ```
    Roisin was not a careless girl by nature, but at the edge of the orchard the morning was bright and the daydreams were brighter.

Roisin arrived at the market with a handful of copper coins, jingling in
her pocket — the pail was heavy on her arm and the road had been
long. "I know how much I have wi...
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

One afternoon, Giulia, his deeds painted larger than his deeds had been hurried down the path and tripped. The pail crashed, and the milk was lost.
She wept. But he gathered the pieces of the...
    ```
- `G2-19` (form `(* 1000000 1000000)`): user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    Marina had walked this road near the farm a hundred times before, but never quite so dreamily.

The farmer had a million coins stacked on one side of the counting table and a million coins stacked on the other side. She wondered what the total would be if she multiplied them together — a vast number...
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

Sorcha, carrying his head as one carrying the certainty of victory, claimed, "I can add 7 and 7 while running and juggling!" But he
knew better. "In the real meadow, a stumble spills the pail. But in the practice mea...
    ```
- `G1-18` (form `(* 7 6)`): sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    ```
    on the hilltop, the road from the farmstead curved gently downhill, and Ingrid walked it with her head held high.

Ingrid, as one struts who has never yet been bested, claimed, "I can multiply 7 by 2 while running and juggling!" But she
knew better. "In the real meadow, a stumble spills the pail. Bu...
    ```
- `G2-20` (form `(count [1 2 3])`): sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    ```
    The cows had given generously that dawn, and the pail was heavier than usual, and the imagination was heavier still.

Friederike arrived at the market breathless. "How many coins do I have?" He, with the steady turn of a millwheel, asked.
She counted on her fingers, looking back at each milestone. "...
    ```
- `G2-20` (form `(count "hello")`): sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    ```
    It was the kind of morning that tempts a careful person into carelessness through the back door of a happy thought.

Rosalia arrived at the market breathless. "How many coins do I have?" He, with the steady walk of a tortoise, asked.
She counted on her fingers, looking back at each milestone. "I pic...
    ```
- `G2-20` (form `(count [])`): sentence-initial 'the X verb' (lowercase concept_phrase as subject after a period)
    ```
    A pail of milk is a small fortune to a careful walker and a lost fortune to a careless one.

Slavena arrived at the market breathless. "How many coins do I have?" She, with a calm that nothing seemed to ruffle, asked.
She counted on her fingers, looking back at each milestone. "I picked up bags at
f...
    ```

#### CLAUSE_STACK_OVERFLOW

- `G2-01` (form `(* 2 3 4)`): sentence with 6 commas reads as AI-output cadence: '"To multiply 9, 7, and 9, we must count — truly count, and the multi-arg product'
    ```
    She had not yet sold the milk and yet had already chosen the ribbons she would wear at the dance.

One afternoon, she found a cache of coins hidden in the dairy and tried to guess
the fortune, boasting at every turn, the dairy cool and the imagined market still far away. "Surely I can
see the total ...
    ```
- `G2-03` (form `(= 1 1 1)`): sentence with 6 commas reads as AI-output cadence: '"To test whether 1, 1, and 1 are all equal, we must count — truly count, and the'
    ```
    Every step of the road carried the soft sound of liquid against tin and the louder sound of a daydream gathering speed.

One afternoon, she found a cache of coins hidden in the dairy and tried to guess
the fortune, as a young captain walks before his first battle, the dairy cool and the imagined mar...
    ```
- `G2-03` (form `(= 1 1 1)`): sentence with 6 commas reads as AI-output cadence: '"To test whether 1, 1, and 1 are all equal, we must count — truly count, and the'
    ```
    The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

One afternoon, she found a cache of coins hidden in the dairy and tried to guess
the fortune, with a pride that filled him from ear-tip to heel, the dairy cool and the imagined market still far away. "Su...
    ```
- `G2-04` (form `(max 1 2 3)`): sentence with 6 commas reads as AI-output cadence: '"To find the maximum of 1, 5, and 3, we must count — truly count, and the msever'
    ```
    Some plans grow gently from the ground up; others are built from the rooftop down, and topple just as fast.

One afternoon, she found a cache of coins hidden in the dairy and tried to guess
the fortune, wearing his pride like a bright cloak, the dairy cool and the imagined market still far away. "Su...
    ```
- `G2-04` (form `(min -3 -1 -5)`): sentence with 6 commas reads as AI-output cadence: '"To find the minimum of -84, -75, and -27, we must count — truly count, and thes'
    ```
    Despina balanced the pail with the ease of long practice, and near the meadow the road stretched out invitingly.

One afternoon, she found a cache of coins hidden in the dairy and tried to guess
the fortune, wearing his pride like a bright cloak, the dairy cool and the imagined market still far away...
    ```

#### HIGH_LENGTH

- `G2-02` (form `(> 5 4 3 2 1)`): user_msg 201 words
    ```
    It was the season of new chicks and first cheeses, and every small profit felt like the start of a larger one.

The farmer had counted five bags of coins from richest to poorest: the first bag held 1 coins, the next held 3, then 1, then 7, then 8. She wondered if the bags truly decreased in size all...
    ```
- `G3-06` (form `(let [a 5 b (* a 2)] b)`): user_msg 215 words
    ```
    The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

The milkmaid had sewn two compartments into her apron-pocket at the start of the morning round: she tucked a count into the first compartment, then reached in to read it while sewing the second compartme...
    ```
- `G3-09` (form `(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))`): user_msg 223 words
    ```
    Every step of the road carried the soft sound of liquid against tin and the louder sound of a daydream gathering speed.

The milkmaid had nailed a three-slot pail-steps card to the market-board under the name add3: three input slots for the morning, midday, and afternoon counts, and a step that summ...
    ```
- `G3-10` (form `(#(+ % 1) 5)`): user_msg 223 words
    ```
    It was the season of new chicks and first cheeses, and every small profit felt like the start of a larger one.

The milkmaid needed a nameless pail-steps card in a hurry and scrawled it in shorthand on a scrap of cheesecloth: a percent mark for whatever count came in, plus one. She passed the scrap ...
    ```
- `G3-10` (form `(#(* %1 %2) 3 4)`): user_msg 203 words
    ```
    Maja hummed quietly by the meadow as she walked, the pail steady and the future already half-spent.

The milkmaid had scrawled a two-slot nameless card in shorthand on a scrap of cheesecloth: first-count mark, second-count mark, and a step that multiplied them. She passed the scrap to the buyer at t...
    ```

#### ANSWER_LEAK

- `G2-05` (form `(mod -7 3)`): answer 7 in narrative
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

Slavena arrived at the market with a handful of copper coins, jingling in
her pocket — the pail was heavy on her arm and the road had been
long. "I know how much I have without counting," she boast...
    ```
- `G2-21` (form `(count "tortoise")`): answer 6 in narrative
    ```
    A pail of milk is a small fortune to a careful walker and a lost fortune to a careless one.

Boglarka, his eyes bright with the joy of being first, asked, "Can I take a piece of the braided cloth?" He showed Boglarka the braid and
said, "Yes. If the braid says 'morning-walk-to-dairy,' and you want o...
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

Elsa, tossing back his ears as if to taunt the wind, hurried down the long farm path toward the village, the
heavy pail balanced carefully on her head. But the path was blocked by a chain of gates — one
after ...
    ```

#### STORY_SLOT_NOUN_REPEAT

- `G2-16` (form `(boolean "")`): the noun 'the empty string' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    ```
    It was in the meadow, on a fair-weather morning, that Delphine began the long walk to market.

Delphine, his chest thrown out before him, claimed, "I know whether the gates will open without checking them!" But
she led Delphine to the first gate. "Read the rule the boolean conversion. Now write a
fo...
    ```
- `G2-16` (form `(boolean "")`): the noun 'the empty string' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    ```
    On market mornings, the dairy yard smelled of damp grass and warm tin, and the future seemed safely arrangeable.

Polina, tossing back his ears as if to taunt the wind, hurried down the long farm path toward the village, the
heavy pail balanced carefully on her head. But the path was blocked by a ch...
    ```
- `G2-16` (form `(boolean "")`): the noun 'the empty string' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    ```
    near the farm, the road from the farmstead curved gently downhill, and Despina walked it with her head held high.

Despina, with quiet steps taking the long way, gazed at a farmyard gate blocking the path and said,
"Surely this gate will swing open!" Diogenes, only pointed at the latch.
"The gate ru...
    ```
- `G3-05` (form `(do (def x 10) (let [x 99] x) x)`): the noun 'the market-board' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    ```
    There was once a milkmaid who walked to market with a pail of fresh milk balanced upon her head.

Jutta strutted down the market road, milk pail in hand. "define x, shadow it in a let, then look up x again in the outer scope?
Why, I've already tucked the answer into my apron-pocket," she, with the w...
    ```
- `G3-05` (form `(do (def x 10) (let [x 99] x) x)`): the noun 'the market-board' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    ```
    Every step of the road carried the soft sound of liquid against tin and the louder sound of a daydream gathering speed.

Winifred arrived at the village convinced she could define x, shadow it in a let, then look up x again in the outer scope
wherever she stood. Maximilian did not argue. Instead, he...
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

The milkmaid stood at a farmyard gate with three latch-checks in sequence. The first latch returned nothing; the second returned the verdict. The third bore a keyword mark.

She needed the gate to stop at the firs...
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

#### ONLY_SHOOK_HEAD_TIC

- `G3-02` (form `(do (def x 1) (def x 99) x)`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    The cows had given generously that dawn, and the pail was heavier than usual, and the imagination was heavier still.

Katarzyna, his chest thrown out before him, declared, "I will invent new names for the prices each time I visit the market!"
But he only shook his head. "No, Katarzyna. To bind x to ...
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

#### NARRATIVE_NUMERAL_HARDCODE

- `G5-11` (form `(filter even? [1 2 3 4])`): parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    ```
    The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

One morning, she poured milk through a strainer with no rule written. The strainer
did nothing — every drop fell away, the fresh pail was empty, and the milk pooled cold and useless
on the dairy floor. "...
    ```
- `G5-11` (form `(filter even? [1 2 3 4])`): parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    ```
    Milk does not forgive a tilted head, but a dreaming mind seldom remembers as much.

Despina stood with a pail of milk and cried, "I can guess which cream belongs in the market
basket!" But he set a milk-strainer between them. "No guessing," he, with the steady turn of a millwheel, said. "To
keep the...
    ```
- `G5-11` (form `(filter even? [1 2 3 4])`): parametric example has hard-coded English numeral 'four counts' in a story slot — the actual draws may differ from this fixed count
    ```
    Dagmar carried more than milk that morning near the road; she carried a whole imagined fortune.

The milkmaid set her milk-strainer over the pail and poured four counts through: the counts. The strainer's mesh was set to let only even counts pass to the collection below.

She needed the strainer to ...
    ```
- `G5-11` (form `(filter pos? [-2 -1 0 1 2])`): parametric example has hard-coded English numeral 'Five counts' in a story slot — the actual draws may differ from this fixed count
    ```
    It happened near the road, on the morning Iwona took the milk to market and her thoughts ran ahead of her feet.

Iwona, as a young captain walks before his first battle, claimed, "I know which drops should remain without writing down the rule." He
asked, "Then produce the form with the rule written ...
    ```
- `G5-11` (form `(filter pos? [-2 -1 0 1 2])`): parametric example has hard-coded English numeral 'Five counts' in a story slot — the actual draws may differ from this fixed count
    ```
    Milk does not forgive a tilted head, but a dreaming mind seldom remembers as much.

Halina stood with a pail of milk and cried, "I can guess which cream belongs in the market
basket!" But he set a milk-strainer between them. "No guessing," he, neither hastening nor hanging back, said. "To
keep the p...
    ```

#### CONCEPT_AS_VERB

- `G6-01` (form `(name 'clojure.string)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    It was the season of new chicks and first cheeses, and every small profit felt like the start of a larger one.

Katarzyna, his eyes bright with the joy of being first, declared, "I will invent new names for the prices each time I visit the market!"
But he only shook his head. "No, Katarzyna. To extr...
    ```
- `G6-03` (form `(clojure.string/upper-case "hare")`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    by the farm, before the cocks had finished crowing, Trudi had set out with the milk and a head full of plans.

Trudi, as a young captain walks before his first battle, declared, "I will invent new names for the prices each time I visit the market!"
But she only shook her head. "No, Trudi. To call th...
    ```
- `G6-05` (form `(clojure.string/reverse "abc")`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    Every step of the road carried the soft sound of liquid against tin and the louder sound of a daydream gathering speed.

Wanda, as a victor walks before a victory is named, declared, "I will invent new names for the prices each time I visit the market!"
But he only shook his head. "No, Wanda. To cal...
    ```
- `G6-05` (form `(name :owner/item)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    The cows had given generously that dawn, and the pail was heavier than usual, and the imagination was heavier still.

Mira, with the clear ringing pride of the favoured, declared, "I will invent new names for the prices each time I visit the market!"
But he only shook his head. "No, Mira. To extract...
    ```
- `G6-06` (form `(:private (meta 'x))`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    Some plans grow gently from the ground up; others are built from the rooftop down, and topple just as fast.

Slavena, stepping high as proud creatures step, declared, "I will invent new names for the prices each time I visit the market!"
But she only shook her head. "No, Slavena. To check whether th...
    ```

#### DOUBLED_INPUT_VALUE_PARENS

- `G6-04` (form `(= (clojure.string/upper-case "x") (clojure.string/upper-cas`): user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
    ```
    Long before the market opened its stalls, a young woman had already spent her milk three times in her head.

The farmer had posted the clojure.string section on the market-board and the milkmaid called the same board-listed routine twice in a row on the same letter, once from each side of the stall....
    ```
- `G10-15` (form `(do "a function suffices when no syntax shaping is needed" (`): user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

The farmer looked at the milkmaid's plan and said there was no need for a rewrite rule here — a plain nameless pail-steps card would do. No syntax needed shaping; the arguments were already evaluat...
    ```
- `G12-01` (form `(into [] (map inc) [1 2 3])`): user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
    ```
    Long before the market opened its stalls, a young woman had already spent her milk three times in her head.

Margery held a milk-strainer over the fresh pail. The rule inside the mesh whispered: 'Each drop shall thicken by one.' She poured the stream of raw milk through. One by one, the drops passed...
    ```
- `G12-02` (form `(into [] (comp (map inc) (filter even?)) [1 2 3 4])`): user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
    ```
    Long before the market opened its stalls, a young woman had already spent her milk three times in her head.

Clara stood at the dairy with two strainers nested one behind the other. The first strainer whispered 'thicken'; the second whispered 'keep only the even-thickness drops.' She held both over ...
    ```

#### HEDGING_NEAR_FORM

- `G6-10` (form `(:deps {:deps {:a 1 :b 2}})`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    By the time Grainne had reached the second milestone in the orchard, the milk had become eggs, and the eggs a flock.

The wager was set by the orchard: produce the value before the breeze had
turned the next leaf. Grainne, with wide pride — spares no detail bolted into a flurry of
guesses, calling o...
    ```
- `G6-11` (form `(clojure.string/split "src:test" #":")`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

The wager was set in the orchard: produce the value before the breeze had
turned the next leaf. Lydia, with a long story of his own merit bolted into a flurry of
guesses, calling out numbers and second-g...
    ```
- `G11-05` (form `(do "import is a top-of-file ns clause" :studied)`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    Every step of the road carried the soft sound of liquid against tin and the louder sound of a daydream gathering speed.

The wager was set at the edge of the meadow: produce the value before the breeze had
turned the next leaf. Winifred, taking credit for the morning sun bolted into a flurry of
gues...
    ```
- `G11-11` (form `(do "(js/console.log x) calls a JS global; (.-foo o) reads a`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

The wager was set by the orchard: produce the value before the breeze had
turned the next leaf. Lydia, his modesty long since worn through bolted into a flurry of
guesses, calling out numbers and second-...
    ```
- `G11-11` (form `(do "(js/console.log x) calls a JS global; (.-foo o) reads a`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    The road from the farm to the town was long, and a daydream could fit comfortably along its length.

The wager was set in the market: produce the value before the breeze had
turned the next leaf. Niamh, with the broad voice of a bragging man bolted into a flurry of
guesses, calling out numbers and s...
    ```

#### ABSTRACT_RESULT_NARRATION

- `G7-06` (form `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)`): meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns
    ```
    Milk does not forgive a tilted head, but a dreaming mind seldom remembers as much.

Solveig was determined to call a function with a positive precondition on a positive number, doubling it quickly, without pausing. But he
stopped her at the gate. "To call a function with a positive precondition on a...
    ```
- `G7-06` (form `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)`): meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns
    ```
    The cows had given generously that dawn, and the pail was heavier than usual, and the imagination was heavier still.

Yara arrived at the dairy after a long walk, pail intact and milk brimming. He
smiled and asked, "How did you keep the pail so steady?" She, with the warm pride that goes before a fa...
    ```
- `G7-06` (form `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)`): meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns
    ```
    It is an old habit to count the worth of a thing before the thing has reached the buyer.

Irmgard was determined to call a function with a positive precondition on a positive number, doubling it quickly, without pausing. But he
stopped her at the gate. "To call a function with a positive preconditio...
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

Pernille stood at the dairy door, staring at the tally-slate. "I want to change the count,
but I do not know how," she admitted. Octavia, settled in for a long wait, smiled and placed a form in
her han...
    ```
- `G10-09` (form `(symbol? (gensym))`): resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

Walburga, swaggering through the underbrush, asked, "Why does my form not do what I wrote?" He smiled and pulled out
two slips. "This one is what you wrote — your daydream." He showed the first. "T...
    ```
- `G10-09` (form `(symbol? (gensym))`): resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    ```
    Halina set out from the farm near the road with the pail balanced carefully on her head.

Halina, his nose lifted toward the bright sky, daydreamed aloud: "I will test that gensym returns a symbol by doing step one,
then step two, then step three." Iustinian, listened carefully and wrote it
all down...
    ```

#### DOUBLE_PREP

- `G9-18` (form `(do (def lock (Object.)) (locking lock 42))`): verb+preposition followed by {place} which already carries its own preposition
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

The farmer showed the milkmaid the simplest possible padlocked section: just a plain value inside the lock. The padlock was real — it acquired the monitor — but the body needed no computation.

She...
    ```

#### MULTIPLE_SAID_TAGS

- `G10-04` (form `(macroexpand-1 '(when true 1))`): user_msg has 3 dialogue-attribution tags — over-announcing the speakers
    ```
    Sigrid was not a careless girl by nature, but in the market the morning was bright and the daydreams were brighter.

Sigrid wrote a plan on a slip of paper, tossing back his ears as if to taunt the wind: "First add milk, then add cream, then mix."
She read it, the slip thin between her fingers, and ...
    ```
- `G10-06` (form `(when true 1 2 3)`): user_msg has 3 dialogue-attribution tags — over-announcing the speakers
    ```
    Milk does not forgive a tilted head, but a dreaming mind seldom remembers as much.

Solveig wrote a plan on a slip of paper, as if the race were already won: "First add milk, then add cream, then mix."
He read it, the slip thin between his fingers, and said,
"Good plan. But now watch — the recipe is...
    ```
- `G10-08` (form `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))`): user_msg has 3 dialogue-attribution tags — over-announcing the speakers
    ```
    The cows had given generously that dawn, and the pail was heavier than usual, and the imagination was heavier still.

Nora wrote a plan on a slip of paper, as a victor walks before a victory is named: "First add milk, then add cream, then mix."
She read it, the slip thin between her fingers, and sai...
    ```
- `G10-08` (form `(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))`): user_msg has 3 dialogue-attribution tags — over-announcing the speakers
    ```
    The cows had given generously that dawn, and the pail was heavier than usual, and the imagination was heavier still.

Nora wrote a plan on a slip of paper, tossing his head as a proud horse tosses its mane: "First add milk, then add cream, then mix."
She read it, the slip thin between her fingers, a...
    ```
- `G10-08` (form `(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))`): user_msg has 3 dialogue-attribution tags — over-announcing the speakers
    ```
    near the meadow, the road from the farmstead curved gently downhill, and Yvette walked it with her head held high.

Yvette wrote a plan on a slip of paper, as if the prize already sat in his paw: "First add milk, then add cream, then mix."
She read it, the slip thin between her fingers, and said,
"G...
    ```

#### SUBMITTED_THE_FORM_DOUBLED

- `G10-06` (form `(when false 1 2 3)`): 'submitted the form' appears 2× in user_msg — connective_prose + subplot double the same beat
    ```
    She had not yet sold the milk and yet had already chosen the ribbons she would wear at the dance.

The farmer's rewrite rule for `when` included a guard: if the test was false, the body was never stamped into the expanded form at all. The milkmaid submitted the form with a false test and watched.

S...
    ```

