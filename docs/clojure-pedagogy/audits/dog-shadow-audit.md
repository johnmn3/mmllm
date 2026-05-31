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
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 5, 'CONCEPT_PHRASE_FORM_PREFIX': 9}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`1/2` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`3/4` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(+ 1/2 1/4)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [CONCEPT_PHRASE_FORM_PREFIX] form=`(+ 1/2 1/4)` — example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    - [CONCEPT_PHRASE_FORM_PREFIX] form=`(+ 1/2 1/4)` — example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(+ 1/2 1/4)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-04: Strings

- examples: 5
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 4}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`"race"` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`"slow and steady"` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`""` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`"42"` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-05: Booleans

- examples: 6
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 5}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`true` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`true` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(= 1 1)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(< 3 5)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(> 3 5)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-06: nil

- examples: 5
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(nil? 0)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(nil? false)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-07: Keywords

- examples: 5
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`:hare` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-08: Characters

- examples: 4
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(char? \h)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(char? \h)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-09: Symbols vs values

- examples: 4
- variety @ n=50: 1.00
- issues: {'ONLY_SHOOK_HEAD_TIC': 1, 'TRAILING_PARTICIPLE_CLOSER': 1, 'BOOL_LEAK_RESOLUTION': 2}
    - [ONLY_SHOOK_HEAD_TIC] form=`(symbol? 'hare)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [TRAILING_PARTICIPLE_CLOSER] form=`(symbol? 42)` — sentence closes with a participial coda (', tapping the bark.') — LLM-cadence; close on the verb instead
    - [BOOL_LEAK_RESOLUTION] form=`(symbol? "tortoise")` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [BOOL_LEAK_RESOLUTION] form=`(= 'hare 'hare)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead

### G1-10: Comments

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 6}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(+ 1 2) ;; sum of one and two` — sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(+ 1 2) ;; sum of one and two` — sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(+ 1 2) ;; sum of one and two` — sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`42 ;; the answer` — sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`42 ;; the answer` — sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`42 ;; the answer` — sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead

### G1-13: First arithmetic call

- examples: 6
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 2, 'FABLE_FOREIGN_NUMERAL_QUANTIFIER': 1, 'SENTENCE_START_LOWER_PRONOUN': 1}
    - [REPL_TRIPLE_VOICE] form=`(/ 10 2)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [FABLE_FOREIGN_NUMERAL_QUANTIFIER] form=`(/ 10 2)` — parametric example has hardcoded digit quantifier 'a heap of 12 bones' in narrative — the form is parametric so the actual count drifts from the prose
    - [SENTENCE_START_LOWER_PRONOUN] form=`(+ 7 8)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [REPL_TRIPLE_VOICE] form=`(+ 7 8)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G1-15: Equality

- examples: 6
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 5}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(= 1 2)` — sentence closes with a participial coda (', weighing the crossing.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(= "a" "a")` — sentence closes with a participial coda (', weighing the crossing.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(= :hare :tortoise)` — sentence closes with a participial coda (', weighing the crossing.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(= :hare :tortoise)` — sentence closes with a participial coda (', weighing the crossing.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(= 1 1 1 1)` — sentence closes with a participial coda (', weighing the crossing.') — LLM-cadence; close on the verb instead

### G1-16: Numeric predicates

- examples: 6
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1}
    - [REPL_TRIPLE_VOICE] form=`(neg? -3)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G1-17: Printing vs returning

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 3}
    - [REPL_TRIPLE_VOICE] form=`42` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`42` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`42` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G1-18: Errors are safe in the REPL

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1}
    - [REPL_TRIPLE_VOICE] form=`(* 7 6)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

## Grade 2

### G2-01: Multi-arg arithmetic

- examples: 6
- variety @ n=50: 1.00
- issues: {'META_FILLER_RESOLUTION': 2}
    - [META_FILLER_RESOLUTION] form=`(- 100 1 2 3)` — user_msg uses generic 'returned exactly' / 'settled with certainty' filler — describe what actually came back, not just that something did
    - [META_FILLER_RESOLUTION] form=`(- 100 1 2 3)` — user_msg uses generic 'returned exactly' / 'settled with certainty' filler — describe what actually came back, not just that something did

### G2-02: Comparison chains

- examples: 5
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 1, 'GENERIC_RESOLUTION_TAIL': 3}
    - [BOOL_LEAK_RESOLUTION] form=`(< 1 2 3)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [GENERIC_RESOLUTION_TAIL] form=`(> 5 4 3 2 1)` — resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    - [GENERIC_RESOLUTION_TAIL] form=`(> 5 4 3 2 1)` — resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop
    - [GENERIC_RESOLUTION_TAIL] form=`(> 5 4 3 2 1)` — resolution ends with generic 'the answer was returned' / 'returned cleanly' / 'settled the matter' — name the operand or close the metaphor's loop

### G2-03: not= and = with multiple args

- examples: 5
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 2}
    - [BOOL_LEAK_RESOLUTION] form=`(not= 1 1)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [BOOL_LEAK_RESOLUTION] form=`(= 1 1 1)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead

### G2-05: quot, rem, mod

- examples: 6
- variety @ n=50: 1.00
- issues: {'SMALL_INT_LEAK': 1}
    - [SMALL_INT_LEAK] form=`(mod -7 3)` — small-int answer 2 leaks via resolution-slot phrasing

### G2-07: Absolute value

- examples: 4
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(abs -5)` — sentence closes with a participial coda (', ignoring the negative sign entirely.') — LLM-cadence; close on the verb instead

### G2-13: and / or — short circuit, return values

- examples: 6
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 3, 'TRAILING_PARTICIPLE_CLOSER': 4, 'CLAUSE_STACK_OVERFLOW': 2}
    - [BOOL_LEAK_RESOLUTION] form=`(and true true)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(and true true)` — sentence closes with a participial coda (', weighing the crossing.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(and true true)` — sentence closes with a participial coda (', weighing the crossing.') — LLM-cadence; close on the verb instead
    - [BOOL_LEAK_RESOLUTION] form=`(and true false)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [BOOL_LEAK_RESOLUTION] form=`(or false true)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(or false false)` — sentence closes with a participial coda (', weighing the crossing.') — LLM-cadence; close on the verb instead

### G2-14: not — turning truthy to false

- examples: 5
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 3}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(not true)` — sentence closes with a participial coda (', weighing the crossing.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(not false)` — sentence closes with a participial coda (', weighing the crossing.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(not nil)` — sentence closes with a participial coda (', weighing the crossing.') — LLM-cadence; close on the verb instead

### G2-15: Falsey values: only false and nil

- examples: 4
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(if false 1 0)` — sentence closes with a participial coda (', weighing the crossing.') — LLM-cadence; close on the verb instead

### G2-16: Truthy 0 and empty string

- examples: 4
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(boolean 0)` — sentence closes with a participial coda (', weighing the crossing.') — LLM-cadence; close on the verb instead

### G2-17: Keyword as function for map lookup

- examples: 3
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(:hare {:hare 1 :tortoise 2})` — sentence closes with a participial coda (',\nleaving the first one untouched.') — LLM-cadence; close on the verb instead

### G2-18: Quoting symbols

- examples: 3
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 2, 'CLAUSE_STACK_OVERFLOW': 1, 'ONLY_SHOOK_HEAD_TIC': 1}
    - [BOOL_LEAK_RESOLUTION] form=`(symbol? (quote hare))` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [BOOL_LEAK_RESOLUTION] form=`(symbol? (quote hare))` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [CLAUSE_STACK_OVERFLOW] form=`(count '(1 2 3))` — sentence with 5 commas reads as AI-output cadence: 'To\ncount the elements in a quoted list of the integers 1, 2, and 3, he composed '
    - [ONLY_SHOOK_HEAD_TIC] form=`(count '(1 2 3))` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

### G2-19: Auto-promotion to bigint

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1, 'RESOLUTION_REPL_DOUBLED': 3}
    - [REPL_TRIPLE_VOICE] form=`(* 1000000 1000000)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [RESOLUTION_REPL_DOUBLED] form=`(* 1000000 1000000)` — story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat
    - [RESOLUTION_REPL_DOUBLED] form=`(* 1000000 1000000)` — story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat
    - [RESOLUTION_REPL_DOUBLED] form=`(* 1000000 1000000)` — story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat

### G2-20: Counting

- examples: 3
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 6, 'HIGH_LENGTH': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count [1 2 3])` — sentence closes with a participial coda (', counting the steps — returned the count.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count [1 2 3])` — sentence closes with a participial coda (', counting the steps — returned the count.') — LLM-cadence; close on the verb instead
    - [HIGH_LENGTH] form=`(count [1 2 3])` — user_msg 201 words
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count "hello")` — sentence closes with a participial coda (', counting the steps — returned the count.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count "hello")` — sentence closes with a participial coda (', carrying the tally — returned the final number.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count [])` — sentence closes with a participial coda (', counting the steps — returned the count.') — LLM-cadence; close on the verb instead

## Grade 3

### G3-03: let — local binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 3}
    - [HIGH_LENGTH] form=`(let [x 3] (+ x 1))` — user_msg 217 words
    - [HIGH_LENGTH] form=`(let [n 10] (* n n))` — user_msg 215 words
    - [HIGH_LENGTH] form=`(let [a 5] a)` — user_msg 212 words

### G3-04: let — multi-binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a 2 b 3 c 4] (+ a b c))` — sentence with 7 commas reads as AI-output cadence: 'Tracker the dog, with even breath and steady step,\nheld his grip steady and did '

### G3-05: let — shadowing outer def

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def x 10) (let [x 99] x))` — sentence with 5 commas reads as AI-output cadence: 'Howler the dog, untroubled by what others thought,\nheld his grip steady and did '

### G3-06: let — binding can reference prior

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 4}
    - [HIGH_LENGTH] form=`(let [a 5 b (* a 2)] b)` — user_msg 232 words
    - [HIGH_LENGTH] form=`(let [a 5 b (* a 2)] b)` — user_msg 234 words
    - [HIGH_LENGTH] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — user_msg 236 words
    - [HIGH_LENGTH] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — user_msg 240 words

### G3-07: fn — anonymous function

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`((fn [a b] (* a b)) 3 4)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G3-08: fn — multi-arg

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`((fn [a b c] (+ a b c)) 1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'To create an anonymous function with three parameters that adds them and apply i'

### G3-09: defn — shorthand

- examples: 2
- variety @ n=50: 1.00
- issues: {'RESOLUTION_REPL_DOUBLED': 3, 'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [RESOLUTION_REPL_DOUBLED] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat
    - [HIGH_LENGTH] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — user_msg 242 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — sentence with 6 commas reads as AI-output cadence: 'To define a function add3 that adds three arguments, then call it with 9, 8, and'
    - [RESOLUTION_REPL_DOUBLED] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat
    - [RESOLUTION_REPL_DOUBLED] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 3}
    - [CONCEPT_AS_VERB] form=`(#(+ % 1) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(#(+ % 1) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(#(* %1 %2) 3 4)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

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
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`((fn [x] x x x 99) 1)` — user_msg 247 words

### G3-15: Side-effects in body

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'SENTENCE_START_LOWER_PRONOUN': 1, 'TRAILING_PARTICIPLE_CLOSER': 2}
    - [HIGH_LENGTH] form=`(do (println "hi") 42)` — user_msg 216 words
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do (println "hi") 42)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (println "hi") 42)` — sentence closes with a participial coda (', ignoring the intermediate println side-effect.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (println "hi") 42)` — sentence closes with a participial coda (', ignoring the intermediate println side-effect.') — LLM-cadence; close on the verb instead

### G3-18: When to name vs inline

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'TRAILING_PARTICIPLE_CLOSER': 1, 'THE_FORM_OVERUSE': 1}
    - [HIGH_LENGTH] form=`(let [n 5] (* n n n))` — user_msg 210 words
    - [TRAILING_PARTICIPLE_CLOSER] form=`(let [n 5] (* n n n))` — sentence closes with a participial coda (', holding the grip tight.') — LLM-cadence; close on the verb instead
    - [THE_FORM_OVERUSE] form=`(* 5 5 5)` — `the form` appears 5 times in user_msg (template tic — vary references)

## Grade 4

### G4-01: Vector literal

- examples: 3
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`[1 2 3]` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`[1 2 3]` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`[1 2 3]` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [TRAILING_PARTICIPLE_CLOSER] form=`["a" "b"]` — sentence closes with a participial coda (',\nleaving the first one untouched.') — LLM-cadence; close on the verb instead

### G4-02: nth — vector access

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'FABLE_FOREIGN_NUMERAL_QUANTIFIER': 2, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 0)` — parametric example has hard-coded English numeral 'three bone' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 0)` — parametric example has hard-coded English numeral 'three bone' in a story slot — the actual draws may differ from this fixed count
    - [FABLE_FOREIGN_NUMERAL_QUANTIFIER] form=`(nth [10 20 30] 0)` — parametric example has hardcoded digit quantifier 'a pile of 10 bones' in narrative — the form is parametric so the actual count drifts from the prose
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 0)` — parametric example has hard-coded English numeral 'three bone' in a story slot — the actual draws may differ from this fixed count
    - [FABLE_FOREIGN_NUMERAL_QUANTIFIER] form=`(nth [10 20 30] 0)` — parametric example has hardcoded digit quantifier 'a pile of 10 bones' in narrative — the form is parametric so the actual count drifts from the prose
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(nth [10 20 30] 2)` — parametric example has hard-coded English numeral 'three piles' in a story slot — the actual draws may differ from this fixed count

### G4-03: conj — append to vector

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(conj [1 2] 3)` — sentence closes with a participial coda (', sealing the cache so it now held the counts in order.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(conj [1 2] 3)` — sentence closes with a participial coda (', sealing the cache so it now held the counts in order.') — LLM-cadence; close on the verb instead

### G4-04: List literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'TRAILING_PARTICIPLE_CLOSER': 1, 'HANGING_FORM_THAT': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [TRAILING_PARTICIPLE_CLOSER] form=`'(1 2 3)` — sentence closes with a participial coda (',\nleaving the first one untouched.') — LLM-cadence; close on the verb instead
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [HANGING_FORM_THAT] form=`'()` — 'form that <noun>' rendered without a verb — template should be 'form for {concept_phrase}'

### G4-05: cons — prepend to seq

- examples: 1
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(cons 0 '(1 2 3))` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(cons 0 '(1 2 3))` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(cons 0 '(1 2 3))` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count

### G4-07: get — map lookup

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(get {:a 1 :b 2} :a)` — sentence closes with a participial coda (',\nleaving the first one untouched.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(get {:a 1} :missing :default)` — sentence closes with a participial coda (',\nleaving the first one untouched.') — LLM-cadence; close on the verb instead

### G4-08: assoc — map update

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(assoc {:a 1} :a 99)` — sentence closes with a participial coda (',\nleaving the first one untouched.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(assoc {:a 1} :a 99)` — sentence closes with a participial coda (',\nleaving the first one untouched.') — LLM-cadence; close on the verb instead

### G4-12: Set membership

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'TRAILING_PARTICIPLE_CLOSER': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(contains? #{1 2 3} 2)` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(contains? #{1 2 3} 2)` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(contains? #{1 2 3} 2)` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(contains? #{1 2 3} 4)` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [TRAILING_PARTICIPLE_CLOSER] form=`(contains? #{1 2 3} 4)` — sentence closes with a participial coda (',\nleaving the first one untouched.') — LLM-cadence; close on the verb instead
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(contains? #{1 2 3} 4)` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count

### G4-13: count — universal

- examples: 4
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'NUMERAL_LIST_IN_GOAL': 3, 'TRAILING_PARTICIPLE_CLOSER': 2}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count [1 2 3 4 5])` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [NUMERAL_LIST_IN_GOAL] form=`(count [1 2 3 4 5])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count [1 2 3 4 5])` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [NUMERAL_LIST_IN_GOAL] form=`(count [1 2 3 4 5])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count [1 2 3 4 5])` — sentence closes with a participial coda (',\nleaving the first one untouched.') — LLM-cadence; close on the verb instead
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count [1 2 3 4 5])` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count

### G4-14: empty?

- examples: 3
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 3, 'TRAILING_PARTICIPLE_CLOSER': 3, 'REPL_TRIPLE_VOICE': 2}
    - [BOOL_LEAK_RESOLUTION] form=`(empty? [])` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(empty? [])` — sentence closes with a participial coda (',\nleaving the first one untouched.') — LLM-cadence; close on the verb instead
    - [BOOL_LEAK_RESOLUTION] form=`(empty? [1])` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [REPL_TRIPLE_VOICE] form=`(empty? [1])` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [BOOL_LEAK_RESOLUTION] form=`(empty? [1])` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [REPL_TRIPLE_VOICE] form=`(empty? [1])` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G4-15: first, rest, last

- examples: 3
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 9, 'TRAILING_PARTICIPLE_CLOSER': 2}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(first [10 20 30])` — parametric example has hard-coded English numeral 'three bone' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(first [10 20 30])` — parametric example has hard-coded English numeral 'three bone' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(first [10 20 30])` — parametric example has hard-coded English numeral 'three bone' in a story slot — the actual draws may differ from this fixed count
    - [TRAILING_PARTICIPLE_CLOSER] form=`(first [10 20 30])` — sentence closes with a participial coda (',\nleaving the first one untouched.') — LLM-cadence; close on the verb instead
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(last [10 20 30])` — parametric example has hard-coded English numeral 'three heaps' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(last [10 20 30])` — parametric example has hard-coded English numeral 'three heaps' in a story slot — the actual draws may differ from this fixed count

### G4-16: into and conj on collections

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(into [] '(1 2 3))` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(into [] '(1 2 3))` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(into [] '(1 2 3))` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count

### G4-17: Immutability — assoc returns new

- examples: 1
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(let [m {:a 1}] (assoc m :a 99) m)` — sentence closes with a participial coda (',\nleaving the first one untouched.') — LLM-cadence; close on the verb instead

### G4-19: range and seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'TRAILING_PARTICIPLE_CLOSER': 3, 'REPL_TRIPLE_VOICE': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(count (range 5))` — sentence with 6 commas reads as AI-output cadence: 'The range is a promise of 9 bones (0, 1, 2, 3, 4), and count consumes that promi'
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count (range 5))` — sentence closes with a participial coda (', tallying the whole.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count (range 5))` — sentence closes with a participial coda (',\nleaving the first one untouched.') — LLM-cadence; close on the verb instead
    - [CLAUSE_STACK_OVERFLOW] form=`(count (range 5))` — sentence with 6 commas reads as AI-output cadence: 'The range is a promise of 9 bones (0, 1, 2, 3, 4), and count consumes that promi'
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count (range 5))` — sentence closes with a participial coda (', tallying the whole.') — LLM-cadence; close on the verb instead
    - [REPL_TRIPLE_VOICE] form=`(first (range 1 100))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G4-20: Collection vs sequence

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count (seq [1 2 3]))` — sentence closes with a participial coda (',\nleaving the first one untouched.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(seq [])` — sentence closes with a participial coda (',\nleaving the first one untouched.') — LLM-cadence; close on the verb instead

## Grade 5

### G5-02: if as expression

- examples: 1
- variety @ n=50: 1.00
- issues: {'RESOLUTION_REPL_DOUBLED': 3, 'HIGH_LENGTH': 1}
    - [RESOLUTION_REPL_DOUBLED] form=`(+ 1 (if true 10 20))` — story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat
    - [HIGH_LENGTH] form=`(+ 1 (if true 10 20))` — user_msg 220 words
    - [RESOLUTION_REPL_DOUBLED] form=`(+ 1 (if true 10 20))` — story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat
    - [RESOLUTION_REPL_DOUBLED] form=`(+ 1 (if true 10 20))` — story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat

### G5-03: when

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'DOUBLED_INPUT_VALUE_PARENS': 1}
    - [HIGH_LENGTH] form=`(when true :yes)` — user_msg 204 words
    - [DOUBLED_INPUT_VALUE_PARENS] form=`(when true :yes)` — user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it

### G5-07: and / or as control flow

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLED_INPUT_VALUE_PARENS': 1}
    - [HIGH_LENGTH] form=`(or nil false :found)` — user_msg 204 words
    - [CLAUSE_STACK_OVERFLOW] form=`(or nil false :found)` — sentence with 6 commas reads as AI-output cadence: 'The runtime let the crossing-conditions decide: The REPL walked the first gate, '
    - [DOUBLED_INPUT_VALUE_PARENS] form=`(or nil false :found)` — user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it

### G5-10: map

- examples: 2
- variety @ n=50: 1.00
- issues: {'COLLECTION_LEAK': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'NUMERAL_LIST_IN_GOAL': 3}
    - [COLLECTION_LEAK] form=`(map inc [1 2 3])` — elements of expected [2, 3, 4] appear comma-separated in user_msg (collection answer leak)
    - [CLAUSE_STACK_OVERFLOW] form=`(map inc [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'Zoomer the dog shook\nhis head and went on with the work: to pour the vector cont'
    - [NUMERAL_LIST_IN_GOAL] form=`(map #(* % %) [1 2 3 4])` — goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(map #(* % %) [1 2 3 4])` — goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(map #(* % %) [1 2 3 4])` — goal_text contains 4 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(map #(* % %) [1 2 3 4])` — sentence with 6 commas reads as AI-output cadence: 'Leaper the dog shook\nhis head and went on with the work: to apply a squaring ope'

### G5-11: filter

- examples: 2
- variety @ n=50: 1.00
- issues: {'NUMERAL_LIST_IN_GOAL': 6, 'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [NUMERAL_LIST_IN_GOAL] form=`(filter even? [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(filter even? [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(filter even? [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(filter pos? [-2 -1 0 1 2])` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count
    - [NUMERAL_LIST_IN_GOAL] form=`(filter pos? [-2 -1 0 1 2])` — goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(filter pos? [-2 -1 0 1 2])` — parametric example has hard-coded English numeral 'five bones' in a story slot — the actual draws may differ from this fixed count

### G5-12: reduce

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'NUMERAL_LIST_IN_GOAL': 9, 'TRAILING_PARTICIPLE_CLOSER': 5, 'CLAUSE_STACK_OVERFLOW': 3}
    - [HIGH_LENGTH] form=`(reduce + [1 2 3 4])` — user_msg 215 words
    - [NUMERAL_LIST_IN_GOAL] form=`(reduce + [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [HIGH_LENGTH] form=`(reduce + [1 2 3 4])` — user_msg 209 words
    - [NUMERAL_LIST_IN_GOAL] form=`(reduce + [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(reduce + [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [TRAILING_PARTICIPLE_CLOSER] form=`(reduce + [1 2 3 4])` — sentence closes with a participial coda (', counting the steps — returned the count.') — LLM-cadence; close on the verb instead

### G5-13: reduce with init

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 4, 'HIGH_LENGTH': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(reduce + 100 [1 2 3])` — sentence closes with a participial coda (', counting the steps — returned the count.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(reduce + 100 [1 2 3])` — sentence closes with a participial coda (', counting the steps — returned the count.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(reduce + 0 [])` — sentence closes with a participial coda (', walking the row — returned the final value.') — LLM-cadence; close on the verb instead
    - [HIGH_LENGTH] form=`(reduce + 0 [])` — user_msg 203 words
    - [TRAILING_PARTICIPLE_CLOSER] form=`(reduce + 0 [])` — sentence closes with a participial coda (', carrying the tally — returned the final number.') — LLM-cadence; close on the verb instead

### G5-14: apply

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 3, 'NARRATIVE_NUMERAL_HARDCODE': 6, 'NUMERAL_LIST_IN_GOAL': 6, 'CLAUSE_STACK_OVERFLOW': 3}
    - [HIGH_LENGTH] form=`(apply + [1 2 3 4])` — user_msg 231 words
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply + [1 2 3 4])` — parametric example has hard-coded English numeral 'four bones' in a story slot — the actual draws may differ from this fixed count
    - [NUMERAL_LIST_IN_GOAL] form=`(apply + [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(apply + [1 2 3 4])` — sentence with 6 commas reads as AI-output cadence: 'To apply + to the elements of the vector containing 1, 2, 3, and 4, he, with the'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply + [1 2 3 4])` — parametric example has hard-coded English numeral 'four bones' in a story slot — the actual draws may differ from this fixed count
    - [NUMERAL_LIST_IN_GOAL] form=`(apply + [1 2 3 4])` — goal_text contains 4 numerals across 3 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing

### G5-15: comp

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'ANSWER_LEAK': 1, 'CONCEPT_AS_VERB': 1}
    - [HIGH_LENGTH] form=`((comp inc inc) 5)` — user_msg 212 words
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
    - [HIGH_LENGTH] form=`(some neg? [1 2 3])` — user_msg 204 words

### G5-19: every?

- examples: 2
- variety @ n=50: 1.00
- issues: {'PREDICATE_QUESTION_COLLISION': 1, 'BOOL_LEAK_RESOLUTION': 1}
    - [PREDICATE_QUESTION_COLLISION] form=`(every? pos? [1 2 3])` — predicate-suffix ``?`` collides with the question framing's trailing ``?`` or ``.``
    - [BOOL_LEAK_RESOLUTION] form=`(every? pos? [1 2 3])` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead

### G5-20: take and drop

- examples: 2
- variety @ n=50: 1.00
- issues: {'NUMERAL_LIST_IN_GOAL': 6, 'CLAUSE_STACK_OVERFLOW': 3, 'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [NUMERAL_LIST_IN_GOAL] form=`(take 3 [10 20 30 40 50])` — goal_text contains 6 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(take 3 [10 20 30 40 50])` — sentence with 6 commas reads as AI-output cadence: 'Zoomer the dog shook\nhis head and went on with the work: to take the first 3 ele'
    - [NUMERAL_LIST_IN_GOAL] form=`(take 3 [10 20 30 40 50])` — goal_text contains 6 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(take 3 [10 20 30 40 50])` — sentence with 6 commas reads as AI-output cadence: 'Slate the dog shook\nhis head and went on with the work: to take the first 3 elem'
    - [NUMERAL_LIST_IN_GOAL] form=`(take 3 [10 20 30 40 50])` — goal_text contains 6 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(drop 2 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count

### G5-21: distinct and sort

- examples: 2
- variety @ n=50: 1.00
- issues: {'NUMERAL_LIST_IN_GOAL': 3, 'CLAUSE_STACK_OVERFLOW': 2}
    - [NUMERAL_LIST_IN_GOAL] form=`(distinct [1 1 2 3 3 4])` — goal_text contains 6 numerals across 5 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [NUMERAL_LIST_IN_GOAL] form=`(distinct [1 1 2 3 3 4])` — goal_text contains 6 numerals across 5 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(distinct [1 1 2 3 3 4])` — sentence with 7 commas reads as AI-output cadence: 'Marley the dog shook\nhis head and went on with the work: to remove duplicate ele'
    - [NUMERAL_LIST_IN_GOAL] form=`(distinct [1 1 2 3 3 4])` — goal_text contains 6 numerals across 5 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    - [CLAUSE_STACK_OVERFLOW] form=`(distinct [1 1 2 3 3 4])` — sentence with 5 commas reads as AI-output cadence: 'What Clojure form computes the sequence produced by passing 1, 1, 2, 3, 3, 4 thr'

### G5-22: recur — first taste

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 3}
    - [HIGH_LENGTH] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — user_msg 215 words
    - [HIGH_LENGTH] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — user_msg 214 words
    - [HIGH_LENGTH] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — user_msg 212 words

## Grade 6

### G6-10: Leiningen and deps.edn

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HEDGING_NEAR_FORM] form=`(:deps {:deps {:a 1 :b 2}})` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(:deps {:deps {:a 1 :b 2}})` — sentence with 5 commas reads as AI-output cadence: 'Pewter the dog, with eyes always on the path, who had simply walked to a flat st'

### G6-13: Aliasing conventions

- examples: 1
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 2}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(let [s clojure.string/upper-case] (s "hare"))` — sentence closes with a participial coda (', returning the uppercase result.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(let [s clojure.string/upper-case] (s "hare"))` — sentence closes with a participial coda (', returning the uppercase result.') — LLM-cadence; close on the verb instead

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
- issues: {'REPL_TRIPLE_VOICE': 2, 'HIGH_LENGTH': 1}
    - [REPL_TRIPLE_VOICE] form=`(:doc (meta '\{:doc "steady wins"\} race))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [HIGH_LENGTH] form=`(:doc (meta '\{:doc "steady wins"\} race))` — user_msg 220 words
    - [REPL_TRIPLE_VOICE] form=`(:author (meta '\{:author "Aesop"\} race))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G6-16: Cleaning up requires

- examples: 2
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 1}
    - [BOOL_LEAK_RESOLUTION] form=`(contains? #{'clojure.string} 'clojure.set)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead

## Grade 7

### G7-01: throw

- examples: 1
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(try (throw (Exception. "bad")) (catch Exception e` — sentence closes with a participial coda (', testing its hold paw by paw before trusting full weight.') — LLM-cadence; close on the verb instead

### G7-02: try / catch

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(try (/ 1 0) (catch Exception e -1))` — sentence closes with a participial coda (', testing its hold paw by paw before trusting full weight.') — LLM-cadence; close on the verb instead

### G7-03: try / finally

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(try 7 (finally (prn :cleanup)))` — sentence closes with a participial coda (', crossing the shallow ford.') — LLM-cadence; close on the verb instead

### G7-04: ex-info

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(try (throw (ex-info "x" {:k :v})) (catch Exceptio` — sentence closes with a participial coda (', testing its hold paw by paw before trusting full weight.') — LLM-cadence; close on the verb instead

### G7-05: nil punning

- examples: 4
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 3, 'REPL_TRIPLE_VOICE': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(some? 0)` — sentence closes with a participial coda (', testing its hold paw by paw before trusting full weight.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(some? 0)` — sentence closes with a participial coda (', testing its hold paw by paw before trusting full weight.') — LLM-cadence; close on the verb instead
    - [REPL_TRIPLE_VOICE] form=`(first nil)` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [TRAILING_PARTICIPLE_CLOSER] form=`(first nil)` — sentence closes with a participial coda (', testing its hold paw by paw before trusting full weight.') — LLM-cadence; close on the verb instead

### G7-06: pre and post conditions

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 3, 'ABSTRACT_RESULT_NARRATION': 3}
    - [TRAILING_PARTICIPLE_CLOSER] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — sentence closes with a participial coda (', testing its hold paw by paw before trusting full weight.') — LLM-cadence; close on the verb instead
    - [ABSTRACT_RESULT_NARRATION] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns
    - [ABSTRACT_RESULT_NARRATION] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns
    - [ABSTRACT_RESULT_NARRATION] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns
    - [TRAILING_PARTICIPLE_CLOSER] form=`(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exce` — sentence closes with a participial coda (', testing its hold paw by paw before trusting full weight.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exce` — sentence closes with a participial coda (', testing its hold paw by paw before trusting full weight.') — LLM-cadence; close on the verb instead

### G7-07: assert

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — sentence with 5 commas reads as AI-output cadence: 'To\nassert that 7 equals 9, catch the failure, and return a numeric code required'

### G7-08: prn and pprint

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1}
    - [REPL_TRIPLE_VOICE] form=`(with-out-str (prn 42))` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

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
- issues: {'TRAILING_PARTICIPLE_CLOSER': 1}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(try (throw (ex-info "trouble" {})) (catch Excepti` — sentence closes with a participial coda (', testing its hold paw by paw before trusting full weight.') — LLM-cadence; close on the verb instead

### G7-12: slurp and spit

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'TRAILING_PARTICIPLE_CLOSER': 1, 'REPL_TRIPLE_VOICE': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(count "hare
tortoise
")` — sentence with 5 commas reads as AI-output cadence: 'To count every character in a two-line string ending each line with a newline-ma'
    - [TRAILING_PARTICIPLE_CLOSER] form=`(count "hare
tortoise
")` — sentence closes with a participial coda (', including the newlines.') — LLM-cadence; close on the verb instead
    - [REPL_TRIPLE_VOICE] form=`(count "hare
tortoise
")` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    - [REPL_TRIPLE_VOICE] form=`(clojure.string/split "a\nb\nc" #"\n")` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G7-13: line-seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 1}
    - [REPL_TRIPLE_VOICE] form=`(first (clojure.string/split-lines "first\nsecond"` — user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)

### G7-14: with-open

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(with-out-str (println "hare"))` — user_msg 201 words

### G7-15: *in* and *out*

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPL_TRIPLE_VOICE': 2}
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
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — user_msg 213 words

## Grade 8

### G8-05: Protocol extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol named Greet with one method hail, extend it to Long type wi'

### G8-06: Protocol method dispatch

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, extend it to both String and Long t'

### G8-07: Record implementing protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, define a record Hare that implement'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, define a record Hare that implement'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (defrecord T` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, define a record Tortoise that imple'

### G8-08: Multimethod defmulti

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti tag :kind) (defmethod tag :stone [_]` — sentence with 6 commas reads as AI-output cadence: 'To define a multimethod tag that dispatches on the :kind key, add a method for :'
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (defmulti tag :kind) (defmethod tag :stone [_]` — sentence closes with a participial coda (', dispatching\nthe bone — returned the pile-specific value.') — LLM-cadence; close on the verb instead

### G8-09: Multimethod defmethod

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 5 commas reads as AI-output cadence: 'To define a multimethod pace that dispatches on :species with methods for both :'

### G8-10: Multimethod vs protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'TRAILING_PARTICIPLE_CLOSER': 3}
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (defmulti show identity) (defmethod show :rabb` — sentence closes with a participial coda (', dispatching\nthe bone — returned the pile-specific value.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (defmulti show identity) (defmethod show :rabb` — sentence closes with a participial coda (', dispatching\nthe bone — returned the pile-specific value.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(do (defprotocol Show (show [this])) (extend-proto` — sentence closes with a participial coda (', dispatching\nthe bone — returned the pile-specific value.') — LLM-cadence; close on the verb instead

### G8-11: Protocol vs Java interface

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol IPace (run [this])) (extend-proto` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol IPace with method run, extend it to String type, then call '

### G8-12: extend-type on built-in types

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-type` — sentence with 6 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, use extend-type to attach it to Lon'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-type` — sentence with 6 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, use extend-type to attach it to Lon'

### G8-14: Protocols don't inherit

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — sentence with 6 commas reads as AI-output cadence: 'To define two protocols A and B, each with a method, extend both to String type '

### G8-15: derive and isa? — multimethod hierarchy

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'TRAILING_PARTICIPLE_CLOSER': 2, 'BOOL_LEAK_RESOLUTION': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — sentence with 5 commas reads as AI-output cadence: 'To establish a type relationship where ::hare is a type of ::runner, then check '
    - [TRAILING_PARTICIPLE_CLOSER] form=`(isa? java.lang.Long java.lang.Number)` — sentence closes with a participial coda (', dispatching\nthe bone — returned the pile-specific value.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(isa? java.lang.String java.lang.Number)` — sentence closes with a participial coda (', dispatching\nthe bone — returned the pile-specific value.') — LLM-cadence; close on the verb instead
    - [BOOL_LEAK_RESOLUTION] form=`(isa? java.lang.String java.lang.Number)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead

## Grade 9

### G9-01: Immutability as default — review

- examples: 2
- variety @ n=50: 1.00
- issues: {'RESOLUTION_REPL_DOUBLED': 3, 'TRAILING_PARTICIPLE_CLOSER': 3}
    - [RESOLUTION_REPL_DOUBLED] form=`(let [m {:a 1}] (assoc m :b 2) m)` — story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat
    - [RESOLUTION_REPL_DOUBLED] form=`(let [m {:a 1}] (assoc m :b 2) m)` — story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat
    - [TRAILING_PARTICIPLE_CLOSER] form=`(let [m {:a 1}] (assoc m :b 2) m)` — sentence closes with a participial coda (',\nleaving the first one untouched.') — LLM-cadence; close on the verb instead
    - [RESOLUTION_REPL_DOUBLED] form=`(let [m {:a 1}] (assoc m :b 2) m)` — story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat
    - [TRAILING_PARTICIPLE_CLOSER] form=`(let [v [1 2 3]] (conj v 4) v)` — sentence closes with a participial coda (',\nleaving the first one untouched.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`(let [v [1 2 3]] (conj v 4) v)` — sentence closes with a participial coda (',\nleaving the first one untouched.') — LLM-cadence; close on the verb instead

### G9-02: Why state at all

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(do (def progress (atom :idle)) (reset! progress :` — user_msg 214 words
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def progress (atom :idle)) (reset! progress :` — sentence with 5 commas reads as AI-output cadence: 'To construct an atom holding an idle value as progress, atomically reset it to r'

### G9-03: Atom introduction

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg 205 words

### G9-06: Validator on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — sentence with 5 commas reads as AI-output cadence: 'validator on it, atomically swap by applying inc, and dereference, he composed a'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — sentence with 5 commas reads as AI-output cadence: 'validator on it, atomically swap by applying inc, and dereference, he\ncomposed a'

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2}
    - [HIGH_LENGTH] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg 223 words
    - [HIGH_LENGTH] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg 225 words

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
- issues: {'THE_FORM_OVERUSE': 2, 'ONLY_SHOOK_HEAD_TIC': 1}
    - [THE_FORM_OVERUSE] form=`(let [x 10] `(+ ~x ~x))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [THE_FORM_OVERUSE] form=`(let [xs [1 2 3]] `(list ~@xs))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [ONLY_SHOOK_HEAD_TIC] form=`(let [xs [1 2 3]] `(list ~@xs))` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

### G10-03: defmacro introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'DOUBLED_INPUT_VALUE_PARENS': 1}
    - [HIGH_LENGTH] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg 211 words
    - [DOUBLED_INPUT_VALUE_PARENS] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 3, 'ANSWER_LEAK': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'CONCEPT_AS_VERB': 1}
    - [HIGH_LENGTH] form=`(-> 5 inc inc inc)` — user_msg 227 words
    - [ANSWER_LEAK] form=`(-> 5 inc inc inc)` — answer 7 in narrative
    - [HIGH_LENGTH] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — user_msg 217 words
    - [CLAUSE_STACK_OVERFLOW] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — sentence with 7 commas reads as AI-output cadence: 'To thread a vector through filter, map, and reduce using thread-last, she, with '
    - [CONCEPT_AS_VERB] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [HIGH_LENGTH] form=`(macroexpand '(-> x f g))` — user_msg 202 words

### G10-11: Reader macros overview

- examples: 3
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1, 'TRAILING_PARTICIPLE_CLOSER': 2}
    - [ANSWER_LEAK] form=`(#(* % %) 6)` — answer 36 in narrative
    - [TRAILING_PARTICIPLE_CLOSER] form=`(#(* % %) 6)` — sentence closes with a participial coda (', yielding the product.') — LLM-cadence; close on the verb instead
    - [TRAILING_PARTICIPLE_CLOSER] form=`[1 #_ 2 3]` — sentence closes with a participial coda (', leaving the others in the vector.') — LLM-cadence; close on the verb instead

### G10-12: Tagged literals

- examples: 2
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 1}
    - [BOOL_LEAK_RESOLUTION] form=`(uuid? #uuid "00000000-0000-0000-0000-000000000000` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead

### G10-14: eval (the function)

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1}
    - [ANSWER_LEAK] form=`(eval '(+ 1 2 3))` — answer 6 in narrative

### G10-16: Macro pattern library

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLED_INPUT_VALUE_PARENS': 1}
    - [DOUBLED_INPUT_VALUE_PARENS] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it

## Grade 11

### G11-03: Static method call

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'TRAILING_PARTICIPLE_CLOSER': 1}
    - [HIGH_LENGTH] form=`(Math/abs -7)` — user_msg 212 words
    - [TRAILING_PARTICIPLE_CLOSER] form=`(Math/abs -7)` — sentence closes with a participial coda (', removing the sign and leaving only the magnitude.') — LLM-cadence; close on the verb instead

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

## Grade 12

### G12-01: Transducers introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'COLLECTION_LEAK': 1}
    - [HIGH_LENGTH] form=`(into [] (map inc) [1 2 3])` — user_msg 226 words
    - [COLLECTION_LEAK] form=`(into [] (map inc) [1 2 3])` — elements of expected [2, 3, 4] appear comma-separated in user_msg (collection answer leak)

### G12-02: Transducer composition

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — sentence with 6 commas reads as AI-output cadence: 'What Clojure form computes the sum accumulated via transduce using the composed '

### G12-03: into with a transducer (xform)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'COLLECTION_LEAK': 1}
    - [HIGH_LENGTH] form=`(into #{} (map inc) [1 2 3])` — user_msg 227 words
    - [COLLECTION_LEAK] form=`(into #{} (map inc) [1 2 3])` — elements of expected {2, 3, 4} appear comma-separated in user_msg (collection answer leak)

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

### G12-15: Datomic / XTDB (datalog db brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HEDGING_NEAR_FORM] form=`(do "Datomic and XTDB are immutable, time-aware da` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "Datomic and XTDB are immutable, time-aware da` — sentence with 6 commas reads as AI-output cadence: 'Setter the dog, her quiet hands at her quiet sides, who had simply walked to a f'

---

## Summary

### Issue counts (across all examples × 3 records)

- **TRAILING_PARTICIPLE_CLOSER**: 95
- **CLAUSE_STACK_OVERFLOW**: 55
- **NARRATIVE_NUMERAL_HARDCODE**: 51
- **HIGH_LENGTH**: 41
- **NUMERAL_LIST_IN_GOAL**: 39
- **REPL_TRIPLE_VOICE**: 26
- **FORM_DISPLAY_AND_FORM_NOUN**: 25
- **BOOL_LEAK_RESOLUTION**: 17
- **RESOLUTION_REPL_DOUBLED**: 12
- **HEDGING_NEAR_FORM**: 11
- **CONCEPT_PHRASE_FORM_PREFIX**: 9
- **CONCEPT_AS_VERB**: 7
- **THE_FORM_OVERUSE**: 5
- **ONLY_SHOOK_HEAD_TIC**: 4
- **DOUBLED_INPUT_VALUE_PARENS**: 4
- **ANSWER_LEAK**: 4
- **FABLE_FOREIGN_NUMERAL_QUANTIFIER**: 3
- **GENERIC_RESOLUTION_TAIL**: 3
- **COLLECTION_LEAK**: 3
- **PREDICATE_QUESTION_COLLISION**: 3
- **STORY_SLOT_NOUN_REPEAT**: 3
- **ABSTRACT_RESULT_NARRATION**: 3
- **SENTENCE_START_LOWER_PRONOUN**: 2
- **META_FILLER_RESOLUTION**: 2
- **SMALL_INT_LEAK**: 1
- **HANGING_FORM_THAT**: 1

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 58 | — |
| 2 | 22 | 88 | 40 | — |
| 3 | 18 | 31 | 30 | — |
| 4 | 20 | 39 | 75 | — |
| 5 | 22 | 39 | 99 | — |
| 6 | 16 | 33 | 11 | — |
| 7 | 18 | 36 | 34 | — |
| 8 | 16 | 31 | 19 | — |
| 9 | 18 | 34 | 13 | — |
| 10 | 16 | 36 | 23 | — |
| 11 | 14 | 29 | 6 | — |
| 12 | 18 | 37 | 21 | — |

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
    Sniff was halfway home at the edge of the forest when the water played its old trick on a young dog.

Sniff had been showing Bailey the dog how the REPL works,
the stream cool against their paws and the bridge's shadow long.
"Look here," he said, pointing to the integer -60.
"You hand the form `-60`...
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

#### CONCEPT_PHRASE_FORM_PREFIX

- `G1-03` (form `(+ 1/2 1/4)`): example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    ```
    Tippet had found the bone by the meadow and was carrying it home with no small amount of pride.

A few stream-side creatures had gathered on the bank by the meadow to
watch Rover attempt to outwit Tippet the dog at reading
the REPL. The water moved on, the bridge held its shadow, and
Tippet, with th...
    ```
- `G1-03` (form `(+ 1/2 1/4)`): example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    ```
    It was on the beach, on the wooden bridge above the slow brook, that Pumpernickel looked down at the water.

Loki chalked a wager on a flat stone by the beach: whoever
predicted the result of `(+ 1/2 1/4)` would set who crossed the
bridge first. Pumpernickel the dog, with the slow grace of a creatur...
    ```
- `G1-03` (form `(+ 1/2 1/4)`): example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    ```
    A dog with a bone in his jaws is a happy creature; a dog who looks too hard at the water may not be.

Bagel had been showing Cloud the dog how the REPL works,
the stream cool against their paws and the bridge's shadow long.
"Look here," he said, pointing to the form (+ 1/2 1/4).
"You hand the form `...
    ```
- `G1-03` (form `(* 2 1/2)`): example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    ```
    It is one of the oldest tricks of light to make one bone seem like two and to make a fool of the unwary.

With a twig, Bear marked a wager into the wet sand on the road:
whoever guessed the result of `(* 6 1/2)` first would choose
which bone to carry. Marley the dog, untroubled by what others though...
    ```
- `G1-03` (form `(* 2 1/2)`): example.concept_phrase begins with 'the form (' — vary the noun phrase (use 'the expression', 'the call', or drop the prefix entirely)
    ```
    on the beach, on a still afternoon by the brook, Collie learned what a reflection costs the careless.

With a twig, Houndsman marked a wager into the wet sand near the beach:
whoever guessed the result of `(* 5 1/2)` first would choose
which bone to carry. Collie the dog, stepping deliberately one f...
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
    Pebble was crossing the stream by the beach when he caught a glimpse of his own reflection.

Pickles, as a crow turns a coin against the sun, mistook the name on the bark for the
bone it pointed to. "It says bone, so the value must be the
bone!" Pebble the dog only shook his head: the mark
and the b...
    ```

#### TRAILING_PARTICIPLE_CLOSER

- `G1-09` (form `(symbol? 42)`): sentence closes with a participial coda (', tapping the bark.') — LLM-cadence; close on the verb instead
    ```
    Silver had crossed this bridge a hundred times by the village, but never with so fine a bone clamped in his jaws.

Patch the hound stood at the stream's edge, holding two objects side by side: a scratch-mark on bark and a smooth stone bearing the number 68. "This one is the symbol," Patch said, tapp...
    ```
- `G1-10` (form `(+ 1 2) ;; sum of one and two`): sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    ```
    The bone was good, the day was warm, and the path was clear, and yet the trouble was already shaped in the water.

Bell the hound wrote a form on a clean strip of bark near the pond, then added a double-semicolon mark followed by a note in plain words. "The note is only for other dogs to read," she ...
    ```
- `G1-10` (form `(+ 1 2) ;; sum of one and two`): sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    ```
    Louie was nearly home at the village when the water below showed him a second bone that did not exist.

Louie, stepping deliberately one foot before the next smoothed a fresh strip of bark near the village and
scratched slowly, paying attention to every mark. "The form has
to be written so the reade...
    ```
- `G1-10` (form `(+ 1 2) ;; sum of one and two`): sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    ```
    A dog with a bone in his jaws is a happy creature; a dog who looks too hard at the water may not be.

"A form is what's actually there on the bark," Cocoa, stepping deliberately one foot before the next
said, "after the conventions of writing and reading have done
their work. The runtime sees the cl...
    ```
- `G1-10` (form `42 ;; the answer`): sentence closes with a participial coda (', ignoring the comment.') — LLM-cadence; close on the verb instead
    ```
    The bone was good, the day was warm, and the path was clear, and yet the trouble was already shaped in the water.

Pathfinder, with only one measure: more, glanced at the form and called out
what he thought it would do without paying attention
to the conventions of how it was scratched. Ginger the d...
    ```

#### BOOL_LEAK_RESOLUTION

- `G1-09` (form `(symbol? "tortoise")`): resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    ```
    The bone was good, the day was warm, and the path was clear, and yet the trouble was already shaped in the water.

Patch the hound held a message scratched on bark — not a name to pass around, but a strand of letters. "The reader will treat this as text, not as a symbol the dogs can quote," Patch sa...
    ```
- `G1-09` (form `(= 'hare 'hare)`): resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    ```
    in the meadow, where the boards of the bridge meet the stones of the path, Jack caught sight of himself in the stream.

Rex the hound laid two scratch-marks side by side on bark near the forest. Both marks said the same thing: hare, hare. "Are these two scratches the same name?" Rex asked. "Both poi...
    ```
- `G2-02` (form `(< 1 2 3)`): resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    ```
    Some lessons are taught by mirrors, and some are taught by rivers; this one was taught by both at once.

Bell the hound laid three smooth pebbles near the pond, each one marked with a number: 6, then 6, then 9. The sizes of the pebbles did not matter — only their marks. She needed to know if the mar...
    ```
- `G2-03` (form `(not= 1 1)`): resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    ```
    When Cloud reached the bridge in the forest, he paused to admire the bone he had been so lucky to find.

Patch the hound held two bones carved with the same mark — 1 and 1. They wanted to test if the marks were different from each other. They needed to know if the two marks were distinct. The inequa...
    ```
- `G2-03` (form `(= 1 1 1)`): resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    ```
    On a path that ran beside the stream, a dog was carrying his supper home and looking pleased with himself.

Bell the hound gathered the bones near the pond, each carved with the same mark: 9. She wanted to test if all three matched each other. She needed to know if all three marks were identical. Th...
    ```

#### REPL_TRIPLE_VOICE

- `G1-13` (form `(/ 10 2)`): user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    The path home wound past a slow brook, and on bright days the brook was full of borrowed shapes.

Patch the hound looked at a heap of 12 bones and measured them into two equal piles. "How many bones in each pile?" asked a younger dog. "The runtime can tell us exactly by dividing." Patch wanted the R...
    ```
- `G1-13` (form `(+ 7 8)`): user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    Honey had crossed this bridge a hundred times along the river bank, but never with so fine a bone clamped in his jaws.

Rex the hound gathered 3 bones from one bank and eight from another. "Should I count them all?" he asked. "Let the runtime add them together. It will give the exact total." He want...
    ```
- `G1-16` (form `(neg? -3)`): user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    On a path that ran beside the stream, a dog was carrying his supper home and looking pleased with himself.

Bell the hound marked a negative number on flat bark at the pond and asked: "Is this count moving backward from the starting point?" "The runtime can check," her packmate said. She wanted the ...
    ```
- `G1-17` (form `42`): user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    Pathfinder was halfway home by the meadow when the water played its old trick on a young dog.

Kobe, with greed like a small worm at the heart, glanced at the form and called out
what he thought it would do without paying attention
to the conventions of how it was scratched. Pathfinder the dog only
...
    ```
- `G1-17` (form `42`): user_msg mentions 'REPL' 3 times — the REPL personification should appear at most twice per record (submit + return)
    ```
    On a path that ran beside the stream, a dog was carrying his supper home and looking pleased with himself.

"A form is what the reader sees," Skippy, with no need to hurry the work said, "after
the conventions have been applied. Some marks count, some
don't; some shapes are expanded before the runti...
    ```

#### FABLE_FOREIGN_NUMERAL_QUANTIFIER

- `G1-13` (form `(/ 10 2)`): parametric example has hardcoded digit quantifier 'a heap of 12 bones' in narrative — the form is parametric so the actual count drifts from the prose
    ```
    The path home wound past a slow brook, and on bright days the brook was full of borrowed shapes.

Patch the hound looked at a heap of 12 bones and measured them into two equal piles. "How many bones in each pile?" asked a younger dog. "The runtime can tell us exactly by dividing." Patch wanted the R...
    ```
- `G4-02` (form `(nth [10 20 30] 0)`): parametric example has hardcoded digit quantifier 'a pile of 10 bones' in narrative — the form is parametric so the actual count drifts from the prose
    ```
    A dog with a bone in his jaws is a happy creature; a dog who looks too hard at the water may not be.

Bell the hound counted three bone-heaps in the hollow log cache: a pile of 10 bones first, then 20, then 30. She wanted the very first heap to be pulled out and held up. She asked the REPL for the b...
    ```
- `G4-02` (form `(nth [10 20 30] 0)`): parametric example has hardcoded digit quantifier 'a pile of 10 bones' in narrative — the form is parametric so the actual count drifts from the prose
    ```
    The bridge had stood there as long as anyone remembered, and so had the temptation it offered to anyone crossing with full jaws.

Bell the hound counted three bone-heaps in the hollow log cache: a pile of 10 bones first, then 20, then 30. She wanted the very first heap to be pulled out and held up. ...
    ```

#### SENTENCE_START_LOWER_PRONOUN

- `G1-13` (form `(+ 7 8)`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    Honey had crossed this bridge a hundred times along the river bank, but never with so fine a bone clamped in his jaws.

Rex the hound gathered 3 bones from one bank and eight from another. "Should I count them all?" he asked. "Let the runtime add them together. It will give the exact total." He want...
    ```
- `G3-15` (form `(do (println "hi") 42)`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    When Bruno reached the bridge in the village, he paused to admire the bone he had been so lucky to find.

Bell the hound barked a signal across the bank near the forest — "Hi!" she called out, watching it echo into the canyon. "That bark had its moment," she said. "But what I carry back is not the s...
    ```

#### META_FILLER_RESOLUTION

- `G2-01` (form `(- 100 1 2 3)`): user_msg uses generic 'returned exactly' / 'settled with certainty' filler — describe what actually came back, not just that something did
    ```
    at the edge of the forest, the path bends down to meet the water, and Buddy stopped at exactly the wrong moment.

Bell the hound held a great pile of 639 bones by the river bank. Then came three separate losses — first 5, then 7, then 1 bones taken away in turn. She wanted to know how many remained ...
    ```
- `G2-01` (form `(- 100 1 2 3)`): user_msg uses generic 'returned exactly' / 'settled with certainty' filler — describe what actually came back, not just that something did
    ```
    by the beach, on a still afternoon by the brook, Saffron learned what a reflection costs the careless.

Bell the hound held a great pile of 422 bones by the river bank. Then came three separate losses — first 1, then 3, then 1 bones taken away in turn. She wanted to know how many remained after each...
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

#### SMALL_INT_LEAK

- `G2-05` (form `(mod -7 3)`): small-int answer 2 leaks via resolution-slot phrasing
    ```
    It is one of the oldest tricks of light to make one bone seem like two and to make a fool of the unwary.

Bell the hound stood by the river bank holding a negative value — negative seven — and wanted to find its modulo against three. Negative numbers in modulo work in their own way. She needed to kn...
    ```

#### CLAUSE_STACK_OVERFLOW

- `G2-13` (form `(and 1 2 3)`): sentence with 6 commas reads as AI-output cadence: 'To apply and to 6, 9, and 2,\nshe composed the logical and, submitted the form,\na'
    ```
    It was near the road, on the wooden bridge above the slow brook, that Pearl looked down at the water.

Stalker sprinted toward the stream near the road, with the sharp hunger that no meal mends,
certain the way would be open for him. Pearl the dog
slowed and watched: the only way to know whether the...
    ```
- `G2-13` (form `(or nil false 5)`): sentence with 6 commas reads as AI-output cadence: 'To apply or to nil, false, and 1,\nshe composed the logical or, submitted the for'
    ```
    The stream ran clear that afternoon, and the bridge cast a long trembling shadow across the water.

Rusty sprinted toward the stream near the beach, his mouth watering at the thought of more,
certain the way would be open for him. Rocky the dog
slowed and watched: the only way to know whether the cr...
    ```
- `G2-18` (form `(count '(1 2 3))`): sentence with 5 commas reads as AI-output cadence: 'To\ncount the elements in a quoted list of the integers 1, 2, and 3, he composed '
    ```
    A dog with a bone in his jaws is a happy creature; a dog who looks too hard at the water may not be.

Latte, weighing his neighbour's loaf in his eye, mistook the name on the bark for the
bone it pointed to. "It says bone, so the value must be the
bone!" Cooper the dog only shook his head: the mark
...
    ```
- `G3-04` (form `(let [a 2 b 3 c 4] (+ a b c))`): sentence with 7 commas reads as AI-output cadence: 'Tracker the dog, with even breath and steady step,\nheld his grip steady and did '
    ```
    It happened on a day so ordinary that it seemed impossible anything could have been lost.

Onyx, his thoughts running on doubling and tripling, eyed the bone in her jaws
and the brighter one shimmering on the water below — sure the
shadow was the better catch. She snapped at it, and
the real bone fe...
    ```
- `G3-05` (form `(do (def x 10) (let [x 99] x))`): sentence with 5 commas reads as AI-output cadence: 'Howler the dog, untroubled by what others thought,\nheld his grip steady and did '
    ```
    It was in the forest, on the wooden bridge above the slow brook, that Howler looked down at the water.

Gus, his mind already on the larger share, eyed the bone in her jaws
and the brighter one shimmering on the water below — sure the
shadow was the better catch. She snapped at it, and
the real bone...
    ```

#### RESOLUTION_REPL_DOUBLED

- `G2-19` (form `(* 1000000 1000000)`): story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat
    ```
    Peach was crossing the stream near the village when she caught a glimpse of his own reflection.

Rex the hound stood by the river bank with two enormous piles of bones. Each pile held one million bones. He wanted to know the result if he multiplied them together. He needed the exact product of one m...
    ```
- `G2-19` (form `(* 1000000 1000000)`): story-tagged resolution mentions 'REPL' 2 times — name the mechanic once, use pronoun/it/runtime/it for the second beat
    ```
    It was near the meadow, on the wooden bridge above the slow brook, that Inky looked down at the water.

Bayer eyed the pile, his mouth watering at the thought of more, and called out a guess
about how many bones were there without bothering to count.
Inky the dog simply began counting — to multiply ...
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

Patch the hound laid out a three-step sniffing-trail at the stream's edge and scratched its name — add3 — into a marker stone beside the path. "This trail takes 1 counts and gives back their sum," Patch...
    ```

#### HIGH_LENGTH

- `G2-20` (form `(count [1 2 3])`): user_msg 201 words
    ```
    A reflection is a strange kind of promise: present and unreachable, and very hard to argue with.

Bell the hound paced down a small row of cached bones near the pond — three of them lying end to end on a flat stone — adding one to her running tally at each bone, no other operation needed. She wanted...
    ```
- `G3-03` (form `(let [x 3] (+ x 1))`): user_msg 217 words
    ```
    Diesel had crossed this bridge a hundred times on the beach, but never with so fine a bone clamped in his jaws.

Bell the hound had picked up a small bone near the pond and held it firmly between her jaws. Just for the next stretch of crossing she would need to know the bone's tally — 7 — by a short...
    ```
- `G3-03` (form `(let [n 10] (* n n))`): user_msg 215 words
    ```
    When Cloud reached the bridge in the forest, he paused to admire the bone he had been so lucky to find.

Rex the hound found ten smooth stones near the forest and gathered them into a tight mouthful. "I hold this count only for one stretch — while I carry these stones from bank to bank," he said, hi...
    ```
- `G3-03` (form `(let [a 5] a)`): user_msg 212 words
    ```
    On a path that ran beside the stream, a dog was carrying his supper home and looking pleased with himself.

Bell the hound found a bone near the meadow, five joints long, and cradled it between her teeth. "For this one stretch of the path, I will know this bone by the name a," she said through the g...
    ```
- `G3-06` (form `(let [a 5 b (* a 2)] b)`): user_msg 232 words
    ```
    Some lessons are taught by mirrors, and some are taught by rivers; this one was taught by both at once.

Rex the hound gathered 5 bones and clamped them in his jaws as the name a. Before stepping forward, he computed in his mind what twice that grip would weigh — and held both the first grip and the...
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
    in the meadow, where the boards of the bridge meet the stones of the path, Bingo caught sight of himself in the stream.

"A nose-trail is only useful when it gets walked," Bingo, with the soft patience of running water
said, head low. "You set out the sniffs, you bring the
ingredients, the runtime d...
    ```
- `G5-15` (form `((comp str inc) 9)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    It is one of the oldest tricks of light to make one bone seem like two and to make a fool of the unwary.

"A nose-trail is only useful when it gets walked," Peach, with the soft patience of running water
said, head low. "You set out the sniffs, you bring the
ingredients, the runtime does the rest." ...
    ```

#### THE_FORM_OVERUSE

- `G3-18` (form `(* 5 5 5)`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    It was at the village, on the wooden bridge above the slow brook, that Muffin looked down at the water.

Patch the hound arrived at the crossing and saw the stones arranged in a pile. "I don't need to name these," he said, "because I will use them just once and the form is so short that the values a...
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
    On a path that ran beside the stream, a dog was carrying his supper home and looking pleased with himself.

"There's a difference between *labeling* the form and
*evaluating* it," Runner, with the soft patience of running water said. "Quote in any of its
shapes is the labeling — the runtime hands yo...
    ```
- `G10-02` (form `(let [xs [1 2 3]] `(list ~@xs))`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    It happened on a day so ordinary that it seemed impossible anything could have been lost.

Rex the hound had cached three bones — marked 1, 2, 3 — in a vector. He scratched a new form with the word "list" and then a tilde-at sign — meaning: unwrap the vector and splice all the bones into this spot. ...
    ```

#### NARRATIVE_NUMERAL_HARDCODE

- `G4-01` (form `[1 2 3]`): parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    ```
    Bayer had crossed this bridge a hundred times in the meadow, but never with so fine a bone clamped in his jaws.

A row of bones lay tucked end-to-end inside the log in the meadow, head
at the front, the rest trailing behind. The river ran past, and
the bones stayed in their order, each one waiting t...
    ```
- `G4-01` (form `[1 2 3]`): parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    ```
    Sooty had crossed this bridge a hundred times near the river bank, but never with so fine a bone clamped in his jaws.

Sooty, with a hen's long stillness on the nest, pointed to a hollow log on the river bank,
its inside lined with bones tucked into named slots — the wood
cool, the slots solid. "Wha...
    ```
- `G4-01` (form `[1 2 3]`): parametric example has hard-coded English numeral 'three bones' in a story slot — the actual draws may differ from this fixed count
    ```
    It is one of the oldest tricks of light to make one bone seem like two and to make a fool of the unwary.

Woofer, untroubled by what others thought, pointed to a hollow log along the river bank,
its inside lined with bones tucked into named slots — the wood
cool, the slots solid. "Whatever I want to...
    ```
- `G4-02` (form `(nth [10 20 30] 0)`): parametric example has hard-coded English numeral 'three bone' in a story slot — the actual draws may differ from this fixed count
    ```
    The water beneath the bridge was unhurried that day, and any creature looking down would see a perfect copy of itself.

"You can find what you want in a bone-cache several ways,"
Teddy said, without raising her voice at the troubles of the road, gesturing at the hollow log:
"by the scratch above the...
    ```
- `G4-02` (form `(nth [10 20 30] 0)`): parametric example has hard-coded English numeral 'three bone' in a story slot — the actual draws may differ from this fixed count
    ```
    A dog with a bone in his jaws is a happy creature; a dog who looks too hard at the water may not be.

Bell the hound counted three bone-heaps in the hollow log cache: a pile of 10 bones first, then 20, then 30. She wanted the very first heap to be pulled out and held up. She asked the REPL for the b...
    ```

#### HANGING_FORM_THAT

- `G4-04` (form `'()`): 'form that <noun>' rendered without a verb — template should be 'form for {concept_phrase}'
    ```
    On a path that ran beside the stream, a dog was carrying his supper home and looking pleased with himself.

Patch the hound picked up an empty chain by the bank, a mere collar with no bones attached, and held it up. Patch wanted the empty chain itself to be a recognizable form that the REPL would ho...
    ```

#### NUMERAL_LIST_IN_GOAL

- `G4-13` (form `(count [1 2 3 4 5])`): goal_text contains 5 numerals across 4 commas — comma-list of numerals blows the sentence's clause budget; use a range or 'these numbers' framing
    ```
    It happened on a day so ordinary that it seemed impossible anything could have been lost.

Rex the hound laid out five bones in a hollow log arranged in a neat row: 1, 2, 3, 4, 5. He wanted the precise count of all bones in the cache. He asked the REPL to tally the bones in the vector and return tha...
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

#### DOUBLED_INPUT_VALUE_PARENS

- `G5-03` (form `(when true :yes)`): user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
    ```
    Diesel had crossed this bridge a hundred times on the beach, but never with so fine a bone clamped in his jaws.

Bell stood at the stream crossing near the pond. A single marker-stone bore a clear verdict: true. The form when was different from if — it had no else arm. If the stone read true, she wo...
    ```
- `G5-07` (form `(or nil false :found)`): user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
    ```
    On a path that ran beside the stream, a dog was carrying his supper home and looking pleased with himself.

Rex stood at a fork by the stream facing gates. Three gates in sequence: the first held nil (closed), the second held false (closed), the third held a keyword (open). The or-form would test ea...
    ```
- `G10-03` (form `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-w`): user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
    ```
    Diesel had crossed this bridge a hundred times on the beach, but never with so fine a bone clamped in his jaws.

Bell the hound crouched at a fresh patch of bark near the pond, paw poised. She would set a rule that any later mark of a certain shape would be rewritten — before the runtime ever follow...
    ```
- `G10-16` (form `(do (defmacro def-pace [name v] `(def ~name ~v)) (def-pace r`): user_msg contains two or more 'as the input value' parentheticals — auto-closer fired twice or authored prose duplicated it
    ```
    The bridge had stood there as long as anyone remembered, and so had the temptation it offered to anyone crossing with full jaws.

Patch the hound carved another macro-pattern that would define named values. The macro would rewrite calls into def-forms. When called with a name and value, the macro wo...
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
    by the pond, where the path crosses the stream, Ace trotted home with a fine bone in his teeth.

Bell the hound found a shorthand reading-mark on bark: #(* % %). This was the scribe's way of saying "make a quick function where %  is the argument." The function would take 6 and square it. No need for...
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
    It was on the river bank, on the wooden bridge above the slow brook, that Gizmo looked down at the water.

Bell the hound held a pile of bones marked 1, 2, 3 by the river bank. A gap-sieve before her had a different rule: only negative-marked bones can pass. She wanted to know: does any bone fit thr...
    ```
- `G5-19` (form `(every? pos? [1 2 3])`): predicate-suffix ``?`` collides with the question framing's trailing ``?`` or ``.``
    ```
    Peach was crossing the stream near the village when she caught a glimpse of his own reflection.

Patch the hound held a pile of bones marked 1, 2, 3 at the stream near the forest. A gap-sieve had a rule: only positive-marked bones can pass. She wanted to know: will every bone in this pile fit throug...
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
    at the edge of the meadow, where the path crosses the stream, Topsy trotted home with a fine bone in his teeth.

A wager was set at the edge of the meadow: produce the value before the next ripple
crossed the pond. Trailblazer bolted into a flurry of guesses,
calling out numbers and second-guessing ...
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

#### STORY_SLOT_NOUN_REPEAT

- `G6-14` (form `(name 'java.util.Map)`): the noun 'the kennel-master' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    ```
    near the river bank, where the path crosses the stream, Shadow trotted home with a fine bone in his teeth.

"Each tool in the kennel-master's shed has its own label,"
Shadow, with steady road-tested feet said, "and the right way to call it depends on
which kind of tool it is — some held by a single ...
    ```
- `G6-14` (form `(name 'java.util.Map)`): the noun 'the kennel-master' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    ```
    Down by the stream where the bank dipped low, the world above was answered politely by the world below.

Barker, with the slow grace of a creature unhurried padded over to the kennel-master's shed near the road
and pulled down a tool the dogs hadn't carved themselves — a
leash, a bowl, a collar. "Th...
    ```
- `G6-14` (form `(name 'java.util.Map)`): the noun 'the kennel-master' appears in all 4 story slots (scenario/need/mapping/resolution) — vary the imagery between beats
    ```
    Cashew had found the bone near the beach and was carrying it home with no small amount of pride.

Patch returned to the kennel-master's shed where another tool hung on a peg — this one labeled with a long, dotted Java class name. She wanted to extract the plain text of that host-side label and read ...
    ```

#### ABSTRACT_RESULT_NARRATION

- `G7-06` (form `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)`): meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns
    ```
    On a path that ran beside the stream, a dog was carrying his supper home and looking pleased with himself.

Acorn, with the slow grace of a creature unhurried stepped onto a fallen log spanning the stream
in the forest, testing its hold paw by paw before trusting full weight.
"If the log gives, I re...
    ```
- `G7-06` (form `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)`): meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns
    ```
    Cooper had carried his prize all the way from the village, and near the road the bridge offered him an unwelcome second look.

Pathfinder eyed the log-bridge along the road, with the grasping look of the never-satisfied, certain
she could bound across without testing. Cooper the dog
shook his head a...
    ```
- `G7-06` (form `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)`): meta-narrative 'the result of a function call' uses layered abstract nouns instead of naming the concrete thing the form returns
    ```
    On a path that ran beside the stream, a dog was carrying his supper home and looking pleased with himself.

"This is the practice bank," Inky, without complaint or hurry said on the beach,
gesturing wide. "A stumble here costs nothing. Try a form, see
what comes back, fix it, try again. The REPL is ...
    ```

