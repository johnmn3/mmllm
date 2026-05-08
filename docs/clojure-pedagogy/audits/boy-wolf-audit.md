# boy-wolf curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

### G1-01: Eval as substitution

- examples: 8
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4}
    - [LOW_GROUNDING] form=`0` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(+ 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`nil` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`nil` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-02: Integer numbers

- examples: 6
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1, 'LOW_GROUNDING': 1, 'HONEST_JUDGE_REPEAT': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`-3` — tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    - [LOW_GROUNDING] form=`0` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HONEST_JUDGE_REPEAT] form=`100` — two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)

### G1-03: Ratios

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'FOREIGN_FABLE_IMAGERY': 1, 'HONEST_JUDGE_REPEAT': 1}
    - [LOW_GROUNDING] form=`1/2` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`1/2` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`1/2` — tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    - [LOW_GROUNDING] form=`1/2` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(* 2 1/2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(* 2 1/2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-05: Booleans

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 11, 'HONEST_JUDGE_REPEAT': 1}
    - [LOW_GROUNDING] form=`true` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`true` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`true` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`false` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`false` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-06: nil

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 14, 'FOREIGN_FABLE_IMAGERY': 4, 'HONEST_JUDGE_REPEAT': 2}
    - [LOW_GROUNDING] form=`nil` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`nil` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`nil` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(nil? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [FOREIGN_FABLE_IMAGERY] form=`(nil? nil)` — tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    - [LOW_GROUNDING] form=`(nil? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-07: Keywords

- examples: 5
- variety @ n=50: 1.00
- issues: {'HONEST_JUDGE_REPEAT': 1}
    - [HONEST_JUDGE_REPEAT] form=`(= :wolf :wolf)` — two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)

### G1-09: Symbols vs values

- examples: 4
- variety @ n=50: 0.99
- issues: {'BOOL_LEAK_RESOLUTION': 1, 'LOW_GROUNDING': 7}
    - [BOOL_LEAK_RESOLUTION] form=`(symbol? 'wolf)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(symbol? 'wolf)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`'wolf` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`'wolf` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`'wolf` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 'wolf 'wolf)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-13: First arithmetic call

- examples: 6
- variety @ n=50: 1.00
- issues: {'FORM_LEAK': 1}
    - [FORM_LEAK] form=`(+ 7 8)` — form '(+ 7 8)' appears in user_msg of a goal-style subject

### G1-15: Equality

- examples: 6
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 2, 'LOW_GROUNDING': 6}
    - [CONCEPT_AS_VERB] form=`(= 1 1)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(= 1 1 1 1)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(= 1 1 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-16: Numeric predicates

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'BOOL_LEAK_RESOLUTION': 5}
    - [LOW_GROUNDING] form=`(zero? 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(zero? 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(zero? 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [BOOL_LEAK_RESOLUTION] form=`(zero? 5)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [BOOL_LEAK_RESOLUTION] form=`(pos? 7)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [BOOL_LEAK_RESOLUTION] form=`(pos? -2)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead

### G1-18: Errors are safe in the REPL

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(+ 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 2

### G2-02: Comparison chains

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(<= 1 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-03: not= and = with multiple args

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 8, 'BOOL_LEAK_RESOLUTION': 2}
    - [LOW_GROUNDING] form=`(not= 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [BOOL_LEAK_RESOLUTION] form=`(not= 1 1)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(not= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [BOOL_LEAK_RESOLUTION] form=`(= 1 1 1)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead

### G2-06: inc and dec

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6}
    - [LOW_GROUNDING] form=`(inc 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(inc 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(inc 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(dec 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(dec 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(inc -1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-07: Absolute value

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(abs -5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(abs -5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(abs 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(abs 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(abs 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-08: Arithmetic on ratios

- examples: 3
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(* 2/3 3/4)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(* 2/3 3/4)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-09: Floats vs ints (the / operator)

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(/ 1.0 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(/ 1.0 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-10: Powers via repeated multiplication

- examples: 4
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 2, 'LOW_GROUNDING': 3}
    - [ANSWER_LEAK] form=`(* 2 2 2)` — answer 8 in narrative
    - [LOW_GROUNDING] form=`(* 2 2 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [ANSWER_LEAK] form=`(* 2 2 2)` — answer 8 in narrative
    - [LOW_GROUNDING] form=`(* 2 2 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(* 2 2 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-13: and / or — short circuit, return values

- examples: 6
- variety @ n=50: 0.99
- issues: {'BOOL_LEAK_RESOLUTION': 2, 'LOW_GROUNDING': 8, 'CONCEPT_AS_VERB': 2}
    - [BOOL_LEAK_RESOLUTION] form=`(and true true)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(and true true)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(and true false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(and true false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-14: not — turning truthy to false

- examples: 5
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 1, 'LOW_GROUNDING': 7}
    - [BOOL_LEAK_RESOLUTION] form=`(not true)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-16: Truthy 0 and empty string

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 7, 'CONCEPT_AS_VERB': 1}
    - [LOW_GROUNDING] form=`(boolean 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(boolean 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(boolean nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(boolean nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(boolean false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(boolean false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-18: Quoting symbols

- examples: 3
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(quote wolf)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(quote wolf)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(quote wolf)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`'flock` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`'flock` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-19: Auto-promotion to bigint

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(* 1000000 1000000)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(* 1000000 1000000)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(* 1000000 1000000)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 3

### G3-03: let — local binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'SMALL_INT_LEAK': 1, 'ANSWER_LEAK': 2}
    - [HIGH_LENGTH] form=`(let [x 3] (+ x 1))` — user_msg 229 words
    - [SMALL_INT_LEAK] form=`(let [x 3] (+ x 1))` — small-int answer 4 leaks via resolution-slot phrasing
    - [ANSWER_LEAK] form=`(let [n 10] (* n n))` — answer 100 in narrative
    - [ANSWER_LEAK] form=`(let [n 10] (* n n))` — answer 100 in narrative

### G3-04: let — multi-binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 1}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(let [x 5 y 3] (- x y))` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation

### G3-06: let — binding can reference prior

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1}
    - [ANSWER_LEAK] form=`(let [a 5 b (* a 2)] b)` — answer 10 in narrative

### G3-07: fn — anonymous function

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'SMALL_INT_LEAK': 1}
    - [HIGH_LENGTH] form=`((fn [x] (+ x 1)) 4)` — user_msg 223 words
    - [SMALL_INT_LEAK] form=`((fn [x] (+ x 1)) 4)` — small-int answer 5 leaks via resolution-slot phrasing

### G3-08: fn — multi-arg

- examples: 1
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`((fn [a b c] (+ a b c)) 1 2 3)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1, 'CONCEPT_AS_VERB': 2}
    - [ANSWER_LEAK] form=`(#(+ % 1) 5)` — answer 6 in narrative
    - [CONCEPT_AS_VERB] form=`(#(+ % 1) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(#(* %1 %2) 3 4)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G3-11: Substitution rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 2}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(let [a 7] (+ a a))` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [SENTENCE_START_LOWER_PRONOUN] form=`((fn [x] (* x x)) 6)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation

### G3-13: fn body returns last form

- examples: 1
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1, 'LOW_GROUNDING': 1}
    - [HIGH_LENGTH] form=`((fn [x] x x x 99) 1)` — user_msg 201 words
    - [LOW_GROUNDING] form=`((fn [x] x x x 99) 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G3-17: Naming conventions (kebab-case)

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(let [flock-size 8 stray-count 2] (- flock-size st` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G3-18: When to name vs inline

- examples: 2
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 1}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(let [n 5] (* n n n))` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation

## Grade 4

### G4-01: Vector literal

- examples: 3
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`["a" "b"]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-11: Set literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(count #{1 1 1})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count #{1 1 1})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-16: into and conj on collections

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(into #{} [1 2 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(into #{} [1 2 2 3])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-19: range and seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(count (range 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count (range 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count (range 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 5

### G5-15: comp

- examples: 2
- variety @ n=50: 0.99
- issues: {'CONCEPT_AS_VERB': 3}
    - [CONCEPT_AS_VERB] form=`((comp inc inc) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`((comp inc inc) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`((comp str inc) 9)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G5-16: partial

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`((partial + 10) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G5-17: juxt

- examples: 1
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`((juxt inc dec) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

## Grade 6

### G6-01: Namespace as file

- examples: 3
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 8, 'ANSWER_LEAK_STRING': 1, 'BOOL_LEAK_RESOLUTION': 2}
    - [LOW_GROUNDING] form=`(name 'foo.bar)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name 'foo.bar)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [ANSWER_LEAK_STRING] form=`(name 'foo.bar)` — answer string 'foo.bar' appears in user_msg
    - [LOW_GROUNDING] form=`(name 'foo.bar)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name 'clojure.string)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name 'clojure.string)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-02: ns form

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(name 'village.shepherd)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name 'village.shepherd)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 'village.shepherd 'village.shepherd)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 'village.shepherd 'village.shepherd)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 'village.shepherd 'village.shepherd)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-07: Public vs private API

- examples: 2
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 1, 'VILLAGE_NOUN_OVERUSE': 1}
    - [BOOL_LEAK_RESOLUTION] form=`(boolean (:private (meta '^:private hidden)))` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [VILLAGE_NOUN_OVERUSE] form=`(boolean (:private (meta '^:private hidden)))` — `the village` appears 4 times (noun-saturation tic — vary or drop)

### G6-08: Circular dependencies

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(= 'a.b 'a.b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 'a.b 'a.b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= 'a.b 'a.b)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-09: Loading order

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6}
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [a 1 b (+ a 1)] (+ a b))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [a 1 b (+ a 1)] (+ a b))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [a 1 b (+ a 1)] (+ a b))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-10: Leiningen and deps.edn

- examples: 2
- variety @ n=50: 1.00
- issues: {'VILLAGE_NOUN_OVERUSE': 1}
    - [VILLAGE_NOUN_OVERUSE] form=`(get-in {:paths ["src"]} [:paths 0])` — `the village` appears 4 times (noun-saturation tic — vary or drop)

### G6-11: Classpath

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(clojure.string/split "src:test" #":")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.string/split "src:test" #":")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-12: Multiple files in one project

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(count ['village.shepherd 'village.elder 'village.` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count ['village.shepherd 'village.elder 'village.` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(map name ['village.shepherd 'village.elder])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-14: Import for host classes

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4}
    - [LOW_GROUNDING] form=`(symbol? 'java.util.Date)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(symbol? 'java.util.Date)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name 'java.util.Date)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name 'java.util.Date)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-16: Cleaning up requires

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'BOOL_LEAK_RESOLUTION': 1}
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.string)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.set)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.set)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [BOOL_LEAK_RESOLUTION] form=`(contains? #{'clojure.string} 'clojure.set)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.set)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 7

### G7-04: ex-info

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-05: nil punning

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 9}
    - [LOW_GROUNDING] form=`(some? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(some? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(some? nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(some? 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(some? 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(first nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-06: pre and post conditions

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-09: tap>

- examples: 2
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 1, 'LOW_GROUNDING': 3}
    - [BOOL_LEAK_RESOLUTION] form=`(tap> :hello)` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(tap> :hello)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(tap> 42)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(tap> 42)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-10: doc and source

- examples: 1
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(:doc (meta '^{:doc "adds two"} plus))` — answer string 'adds two' appears in user_msg

### G7-11: Reading stack traces

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(try (throw (Exception. "oops")) (catch Exception ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try (throw (Exception. "oops")) (catch Exception ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try (throw (Exception. "oops")) (catch Exception ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try (throw (ex-info "trouble" {})) (catch Excepti` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try (throw (ex-info "trouble" {})) (catch Excepti` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-12: slurp and spit

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(clojure.string/split "a\nb\nc" #"\n")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-13: line-seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'SMALL_INT_LEAK': 1, 'LOW_GROUNDING': 5}
    - [SMALL_INT_LEAK] form=`(count (clojure.string/split-lines "a\nb\nc"))` — small-int answer 3 leaks via resolution-slot phrasing
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(first (clojure.string/split-lines "alpha\nbeta"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(first (clojure.string/split-lines "alpha\nbeta"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(first (clojure.string/split-lines "alpha\nbeta"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-15: *in* and *out*

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(with-out-str (print "x"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (print "x"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (print "x"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (println))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (println))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-16: edn read

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-17: JSON roundtrip

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 8

### G8-01: Why polymorphism

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(defn speak [k] (cond (= k :wolf) "howl" (= k :flo` — user_msg 208 words

### G8-02: deftype introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 1, 'LOW_GROUNDING': 2}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do (deftype Lantern [color]) (.-color (Lantern. "` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [LOW_GROUNDING] form=`(do (deftype Lantern [color]) (.-color (Lantern. "` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (deftype Lantern [color]) (.-color (Lantern. "` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-03: defrecord introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 1}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do (defrecord Watcher [name post]) (:post (->Watc` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation

### G8-04: Protocol definition

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(do (defprotocol Alarm (sound [this])) (some? Alar` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Alarm (sound [this])) (some? Alar` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Alarm (sound [this])) (some? Alar` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Greet (hail [this])) (some? Greet` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Greet (hail [this])) (some? Greet` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-05: Protocol extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1, 'HONEST_JUDGE_REPEAT': 1, 'LOW_GROUNDING': 2}
    - [ANSWER_LEAK_STRING] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — answer string ':number' appears in user_msg
    - [HONEST_JUDGE_REPEAT] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    - [LOW_GROUNDING] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-06: Protocol method dispatch

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(do (defprotocol Alarm (sound [this])) (extend-pro` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Alarm (sound [this])) (extend-pro` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Alarm (sound [this])) (extend-pro` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-07: Record implementing protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'HONEST_JUDGE_REPEAT': 1}
    - [HONEST_JUDGE_REPEAT] form=`(do (defprotocol Alarm (sound [this])) (defrecord ` — two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)

### G8-13: this-style vs fn-style

- examples: 2
- variety @ n=50: 0.99
- issues: {'WRONG_FABLE_LITERAL': 1, 'LOW_GROUNDING': 2}
    - [WRONG_FABLE_LITERAL] form=`(do (defprotocol Named (name-of [this])) (defrecor` — tortoise-hare ghost name 'Pip' appears in boy-wolf user_msg
    - [LOW_GROUNDING] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-14: Protocols don't inherit

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-15: derive and isa? — multimethod hierarchy

- examples: 3
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 6, 'BOOL_LEAK_RESOLUTION': 1}
    - [LOW_GROUNDING] form=`(isa? java.lang.Long java.lang.Number)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(isa? java.lang.Long java.lang.Number)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(isa? java.lang.Long java.lang.Number)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(isa? java.lang.String java.lang.Number)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [BOOL_LEAK_RESOLUTION] form=`(isa? java.lang.String java.lang.Number)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(isa? java.lang.String java.lang.Number)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-16: Abstract design with protocols

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'HONEST_JUDGE_REPEAT': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol Watch (look [this])) (defrecord S` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Sound (cry [this])) (defrecord Sh` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Sound (cry [this])) (defrecord Sh` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HONEST_JUDGE_REPEAT] form=`(do (defprotocol Sound (cry [this])) (defrecord Sh` — two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)

## Grade 9

### G9-02: Why state at all

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4}
    - [LOW_GROUNDING] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def progress (atom :idle)) (reset! progress :` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def progress (atom :idle)) (reset! progress :` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def progress (atom :idle)) (reset! progress :` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-03: Atom introduction

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom :start)) (reset! a :done) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom :start)) (reset! a :done) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-04: Atom CAS semantics

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-05: Watch on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-06: Validator on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-07: Ref introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'HIGH_LENGTH': 1}
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg 218 words
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-08: dosync and alter

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-09: Ref vs atom

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-10: Agent introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'LOW_GROUNDING': 2}
    - [HIGH_LENGTH] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg 212 words
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-11: send and send-off

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send-off ag inc) (await ag` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send-off ag inc) (await ag` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-12: await — synchronizing on agents

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-13: future introduction

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-15: promise — deliver and deref

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(do (def p (promise)) (deliver p :done) @p)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def p (promise)) (deliver p :done) @p)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-16: volatile — when STM is too heavy

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock 42))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock 42))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 10

### G10-01: quote, unquote, unquote-splice

- examples: 3
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-02: syntax-quote

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(let [xs [1 2 3]] `(list ~@xs))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [xs [1 2 3]] `(list ~@xs))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-03: defmacro introduction

- examples: 2
- variety @ n=50: 0.99
- issues: {'SENTENCE_START_LOWER_PRONOUN': 1, 'LOW_GROUNDING': 4}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [LOW_GROUNDING] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-04: Macro expansion rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4, 'SENTENCE_START_LOWER_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(macroexpand-1 '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(macroexpand-1 '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(macroexpand-1 '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(macroexpand-1 '(or a b))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [SENTENCE_START_LOWER_PRONOUN] form=`(macroexpand-1 '(or a b))` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation

### G10-05: macroexpand

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(macroexpand '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(macroexpand '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(macroexpand '(when true 1))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(macroexpand '(-> 1 inc inc))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(macroexpand '(-> 1 inc inc))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-06: when and when-not as macros

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(when-not false :ok)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(when-not false :ok)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(when-not false :ok)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1, 'LOW_GROUNDING': 3}
    - [CONCEPT_AS_VERB] form=`(macroexpand '(-> x f g))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(macroexpand '(-> x f g))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(macroexpand '(-> x f g))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(macroexpand '(-> x f g))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-09: Hygiene and gensym

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(symbol? (gensym))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-10: Anaphoric macros are confusing

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'ANSWER_LEAK': 1, 'SENTENCE_START_LOWER_PRONOUN': 1}
    - [HIGH_LENGTH] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — user_msg 206 words
    - [ANSWER_LEAK] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — answer 10 in narrative
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation

### G10-11: Reader macros overview

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6}
    - [LOW_GROUNDING] form=`(#(* % %) 6)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(#(* % %) 6)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(#(* % %) 6)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`[1 #_ 2 3]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`[1 #_ 2 3]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`[1 #_ 2 3]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-12: Tagged literals

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(inst? #inst "2024-01-01")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(inst? #inst "2024-01-01")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(uuid? #uuid "00000000-0000-0000-0000-000000000000` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(uuid? #uuid "00000000-0000-0000-0000-000000000000` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(uuid? #uuid "00000000-0000-0000-0000-000000000000` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-13: Data readers and EDN extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "[:a :b :c]")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "[:a :b :c]")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "[:a :b :c]")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-14: eval (the function)

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'SENTENCE_START_LOWER_PRONOUN': 2}
    - [LOW_GROUNDING] form=`(eval '(+ 1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [SENTENCE_START_LOWER_PRONOUN] form=`(eval '(+ 1 2 3))` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [SENTENCE_START_LOWER_PRONOUN] form=`(eval (list '+ 4 5))` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [LOW_GROUNDING] form=`(eval (list '+ 4 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(eval (list '+ 4 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-16: Macro pattern library

- examples: 2
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 1, 'LOW_GROUNDING': 2}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do (defmacro with-careful-watch [& body] `(let [p` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [LOW_GROUNDING] form=`(do (defmacro with-careful-watch [& body] `(let [p` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (defmacro with-careful-watch [& body] `(let [p` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 11

### G11-02: Method call syntax

- examples: 8
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 8, 'HIGH_LENGTH': 2, 'ANSWER_LEAK_STRING': 2}
    - [LOW_GROUNDING] form=`(.startsWith "shepherd-elder" "shepherd")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(.startsWith "shepherd-elder" "shepherd")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [HIGH_LENGTH] form=`(. "abc" toUpperCase)` — user_msg 201 words
    - [ANSWER_LEAK_STRING] form=`(. "abc" toUpperCase)` — answer string 'ABC' appears in user_msg
    - [LOW_GROUNDING] form=`(.startsWith "shepherd-elder" "shepherd")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(.startsWith "shepherd-elder" "shepherd")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-07: Arrays

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(let [a (int-array [5 10 15])] (aget a 0))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [a (int-array [5 10 15])] (aget a 0))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [a (int-array [5 10 15])] (aget a 0))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [a (int-array [7 8 9])] (alength a))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [a (int-array [7 8 9])] (alength a))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-08: Type hints

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6, 'VILLAGE_NOUN_OVERUSE': 1}
    - [LOW_GROUNDING] form=`(let [^String s "def"] (.length s))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [^String s "def"] (.length s))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [^long n 42] (+ n 8))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(let [^long n 42] (+ n 8))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [VILLAGE_NOUN_OVERUSE] form=`(let [^long n 42] (+ n 8))` — `the village` appears 4 times (noun-saturation tic — vary or drop)
    - [LOW_GROUNDING] form=`(let [^long n 42] (+ n 8))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-14: Debugging host leaks

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6}
    - [LOW_GROUNDING] form=`(try (Math/abs -42) (catch Exception _ :err))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try (Math/abs -42) (catch Exception _ :err))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try (.length "test") (catch Exception _ :err))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try (.length "test") (catch Exception _ :err))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try (do (Math/sqrt 4) :success) (catch Exception ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(try (do (Math/sqrt 4) :success) (catch Exception ` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 12

### G12-01: Transducers introduction

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(into [] (map inc) [1 2 3])` — user_msg 218 words

### G12-03: into with a transducer (xform)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'COLLECTION_LEAK': 1}
    - [HIGH_LENGTH] form=`(into #{} (map inc) [1 2 3])` — user_msg 213 words
    - [COLLECTION_LEAK] form=`(into #{} (map inc) [1 2 3])` — elements of expected {2, 3, 4} appear comma-separated in user_msg (collection answer leak)

### G12-06: clojure.spec

- examples: 2
- variety @ n=50: 1.00
- issues: {'VILLAGE_NOUN_OVERUSE': 2}
    - [VILLAGE_NOUN_OVERUSE] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — `the village` appears 4 times (noun-saturation tic — vary or drop)
    - [VILLAGE_NOUN_OVERUSE] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — `the village` appears 4 times (noun-saturation tic — vary or drop)

### G12-17: Library design patterns

- examples: 3
- variety @ n=50: 1.00
- issues: {'VILLAGE_NOUN_OVERUSE': 3}
    - [VILLAGE_NOUN_OVERUSE] form=`(= [1 2 3] (vec '(1 2 3)))` — `the village` appears 4 times (noun-saturation tic — vary or drop)
    - [VILLAGE_NOUN_OVERUSE] form=`(= [1 2 3] (vec '(1 2 3)))` — `the village` appears 4 times (noun-saturation tic — vary or drop)
    - [VILLAGE_NOUN_OVERUSE] form=`(= [1 2 3] (vec '(1 2 3)))` — `the village` appears 4 times (noun-saturation tic — vary or drop)

---

## Summary

### Issue counts (across all examples × 3 records)

- **LOW_GROUNDING**: 336
- **BOOL_LEAK_RESOLUTION**: 17
- **CONCEPT_AS_VERB**: 14
- **SENTENCE_START_LOWER_PRONOUN**: 12
- **HIGH_LENGTH**: 11
- **HONEST_JUDGE_REPEAT**: 9
- **VILLAGE_NOUN_OVERUSE**: 8
- **ANSWER_LEAK**: 7
- **FOREIGN_FABLE_IMAGERY**: 6
- **ANSWER_LEAK_STRING**: 5
- **SMALL_INT_LEAK**: 3
- **FORM_LEAK**: 1
- **WRONG_FABLE_LITERAL**: 1
- **COLLECTION_LEAK**: 1

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 80 | 73 | — |
| 2 | 22 | 88 | 67 | — |
| 3 | 18 | 31 | 18 | — |
| 4 | 20 | 39 | 8 | — |
| 5 | 22 | 39 | 5 | — |
| 6 | 16 | 33 | 42 | — |
| 7 | 18 | 36 | 41 | — |
| 8 | 16 | 31 | 34 | — |
| 9 | 18 | 34 | 48 | — |
| 10 | 16 | 36 | 57 | — |
| 11 | 14 | 58 | 30 | — |
| 12 | 18 | 37 | 8 | — |

### Sample issues by severity

#### LOW_GROUNDING

- `G1-01` (form `0`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    The villagers had agreed that any cry of wolf would bring them running with their sticks and lanterns.

A small crowd of villagers had gathered in the forest to watch
Giulia attempt to predict, off the cuff, what the REPL would
return. Konstantin pointed to the value 0 and read out the
form aloud: `...
    ```
- `G1-01` (form `(+ 1 2)`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    When Solveig climbed up to the lookout that morning, she did not yet know that the day would teach a lasting lesson.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `...
    ```
- `G1-01` (form `nil`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    A boy with too little to do and too loud a voice is a small danger to himself and a larger one to his village.

Halfway through the morning watch, Cesare called out
at the edge of the hilltop, demanding a verdict on the form `nil` and refusing
to come back to the flock until somebody confirmed it. C...
    ```
- `G1-01` (form `nil`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    Voica had cried wolf once already, in the forest, and the villagers had laughed but not entirely.

A small slate sat on a flat stone near the forest; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `nil`, and the ...
    ```
- `G1-02` (form `0`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    On those slopes, trust was a thing the village extended freely, and a thing it could not afford to lose.

Ingrid had been trying to teach Damien how the REPL
works. "Look here," she said, pointing to the integer 0.
"You hand the form `0` to the runtime, and the runtime hands
you back what it evaluat...
    ```

#### FOREIGN_FABLE_IMAGERY

- `G1-02` (form `-3`): tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    ```
    The wolves of those hills were rare but not absent, and the shepherds knew it was safer to be vigilant than clever.

Cassius kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today in the village the next entry was
the integer -3. Rutger peered over his ...
    ```
- `G1-03` (form `1/2`): tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    ```
    The sheep had grazed peacefully all morning, and there was nothing at all the matter, which was exactly the problem.

Gildas kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the hilltop the next entry was
the ratio 1/2. Karin peered over his ...
    ```
- `G1-06` (form `(nil? nil)`): tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    ```
    It was atop the hilltop, where the ridge looks down on the houses, that Wilma first cried wolf.

Gunhilda kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today on the hilltop the next entry was
the predicate (nil? nil). Wilma peered over her shoulder
a...
    ```
- `G1-06` (form `(nil? 0)`): tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    ```
    Long days alone with a flock can teach patience, or they can teach mischief, depending on the boy.

Remigius kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the farm the next entry was
the predicate (nil? 0). Bedwyr peered over his shoulder
...
    ```
- `G1-06` (form `(nil? 0)`): tortoise-hare-specific imagery 'leather notebook' leaks into boy-wolf prose
    ```
    When Bridget climbed up to the lookout that morning, she did not yet know that the day would teach a lasting lesson.

Oswald kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the orchard the next entry was
the predicate (nil? 0). Bridget peere...
    ```

#### HONEST_JUDGE_REPEAT

- `G1-02` (form `100`): two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    ```
    The villagers had agreed that any cry of wolf would bring them running with their sticks and lanterns.

The elder of the village kept a small slate near the farm, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the integer 100. Maxi...
    ```
- `G1-03` (form `(- 1 1/3)`): two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    ```
    An empty hour can sometimes be filled with mischief, and mischief once started has a way of escalating.

The elder of the village kept a small slate in the forest, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the form (- 1 1/3). ...
    ```
- `G1-05` (form `(= 1 1)`): two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    ```
    On a hill above the village, a boy watched sheep, and the sheep watched the grass, and the day moved slowly.

The elder of the village kept a small slate near the farm, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the equality (=...
    ```
- `G1-06` (form `(nil? 0)`): two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    ```
    There was once a shepherd boy whose afternoons were long and whose imagination was longer.

The elder of the village kept a small slate near the orchard, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the predicate (nil? 0). Nikode...
    ```
- `G1-06` (form `(= nil nil)`): two or more 'honest' uses in one boy-wolf user_msg (judge-bombast tic — drop one)
    ```
    It happened in a quiet season, when the lambs were strong and the days were long enough to grow tired of.

The elder of the village kept a small slate in the village, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the equality (= n...
    ```

#### BOOL_LEAK_RESOLUTION

- `G1-09` (form `(symbol? 'wolf)`): resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    ```
    There is a difference between a real alarm and a bored one, and the village knew the difference well.

Tom had chalked a label on the slate for a flock pen. Carol stood with a carved tag from the live sheep itself.

The village's notes must not mix chalk marks with the things they name. Tom had to t...
    ```
- `G1-16` (form `(zero? 5)`): resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    ```
    at the farm, in the long grass above the village road, Idun settled in for another slow afternoon.

Carol pointed to a tally of 5 sheep. Tom wondered if the predicate `zero?` would mistake the count for nothing. Carol wrote the test.

Tom had to trust that `zero?` would correctly reject any count th...
    ```
- `G1-16` (form `(pos? 7)`): resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    ```
    in the woods, on a slope above the village, Paolo watched his flock and his shadow grow longer.

Carol had tracked the flock's change from morning to afternoon: +7 sheep had returned. Tom asked if the predicate could confirm that the change was positive.

The village's ledger recorded gains and loss...
    ```
- `G1-16` (form `(pos? -2)`): resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    ```
    The sheep had grazed peacefully all morning, and there was nothing at all the matter, which was exactly the problem.

Tom had counted 2 fewer sheep at the afternoon fold than at morning. Carol wanted the predicate to confirm that -2 was not a positive change.

The village had to track losses as loss...
    ```
- `G1-16` (form `(neg? -3)`): resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    ```
    The lambs were milling in the lower meadow when the boy first thought of the joke he should not have made.

Carol had a record: -3 fleeces sold this week (a shortage). Tom wondered if `neg?` would confirm the negative change.

The wool-ledger had to mark shortages clearly. `neg?` had to confirm that...
    ```

#### FORM_LEAK

- `G1-13` (form `(+ 7 8)`): form '(+ 7 8)' appears in user_msg of a goal-style subject
    ```
    Paola had been told the rules plainly: cry only when the wolf is real, and never when she is bored.

At dawn, Tom had brought lambs back from the south pasture and Carol had brought lambs from the north. They stood at the fold counting together, the village's morning record waiting on them.

The com...
    ```

#### CONCEPT_AS_VERB

- `G1-15` (form `(= 1 1)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    Aristos had been told the rules plainly: cry only when the wolf is real, and never when he is bored.

"You can't tell which way the fold-gates will swing by guessing," Bonifacius
said. "You bring the value to the first gate, the runtime checks it, and if
that gate closes, the chain stops — the rest ...
    ```
- `G1-15` (form `(= 1 1 1 1)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    in the village, on a slope above the village, Winifred watched his flock and his shadow grow longer.

"You can't tell which way the fold-gates will swing by guessing," Jeremias
said. "You bring the value to the first gate, the runtime checks it, and if
that gate closes, the chain stops — the rest of...
    ```
- `G2-13` (form `(and true true)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    Long days alone with a flock can teach patience, or they can teach mischief, depending on the boy.

"You can't tell which way the fold-gates will swing by guessing," Apollonia
said. "You bring the value to the first gate, the runtime checks it, and if
that gate closes, the chain stops — the rest of ...
    ```
- `G2-13` (form `(or false true)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    A boy with too little to do and too loud a voice is a small danger to himself and a larger one to his village.

"You can't tell which way the fold-gates will swing by guessing," Bonifacius
said. "You bring the value to the first gate, the runtime checks it, and if
that gate closes, the chain stops —...
    ```
- `G2-16` (form `(boolean false)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    The hilltop offered a fine view of both the flock and the road below, where help would have to come from.

"You can't tell which way the fold-gates will swing by guessing," Cordelia
said. "You bring the value to the first gate, the runtime checks it, and if
that gate closes, the chain stops — the re...
    ```

#### ANSWER_LEAK

- `G2-10` (form `(* 2 2 2)`): answer 8 in narrative
    ```
    The hilltop offered a fine view of both the flock and the road below, where help would have to come from.

Carol stacked boxes in a cube pattern: 2 boxes deep, 2 boxes wide, 2 boxes tall. She wanted to know the total volume.

The cube volume required multiplying 2 three times. Tom estimated; Carol d...
    ```
- `G2-10` (form `(* 2 2 2)`): answer 8 in narrative
    ```
    Maarten had been told the rules plainly: cry only when the wolf is real, and never when he is bored.

Carol stacked boxes in a cube pattern: 2 boxes deep, 2 boxes wide, 2 boxes tall. She wanted to know the total volume.

The cube volume required multiplying 2 three times. Tom estimated; Carol drew t...
    ```
- `G3-03` (form `(let [n 10] (* n n))`): answer 100 in narrative
    ```
    Grainne was a clever boy, and by the meadow cleverness had begun to look very much like trouble.

Tom had just counted 10 stones for a marker wall, and he wanted to know how many stones would fill a perfect square patch. He reached for a tally-token and turned to Carol.

The square count was needed ...
    ```
- `G3-03` (form `(let [n 10] (* n n))`): answer 100 in narrative
    ```
    On those slopes, trust was a thing the village extended freely, and a thing it could not afford to lose.

Tom had just counted 10 stones for a marker wall, and he wanted to know how many stones would fill a perfect square patch. He reached for a tally-token and turned to Carol.

The square count was...
    ```
- `G3-06` (form `(let [a 5 b (* a 2)] b)`): answer 10 in narrative
    ```
    An empty hour can sometimes be filled with mischief, and mischief once started has a way of escalating.

Carol had counted 5 morning lambs in the upper pasture. Tom asked: what if we double that count for the afternoon fold calculations?

Tom needed the doubled count for one specific task, but that ...
    ```

#### HIGH_LENGTH

- `G3-03` (form `(let [x 3] (+ x 1))`): user_msg 229 words
    ```
    The hilltop offered a fine view of both the flock and the road below, where help would have to come from.

Carol the elder had been counting along a stretch of fence-line at dawn. She slipped a tally-token worth 3 lambs into the small leather belt-pouch at her hip and gave the pouch's contents the l...
    ```
- `G3-07` (form `((fn [x] (+ x 1)) 4)`): user_msg 223 words
    ```
    It happened at the edge of the orchard, on a hill where shouting carries far and trust carries further, until it doesn't.

On the watchhouse wall, Carol the elder had pinned a small drill-card with no name at the top — just the steps for what to do once an unnamed quantity arrived. Tom waited beside...
    ```
- `G3-13` (form `((fn [x] x x x 99) 1)`): user_msg 201 words
    ```
    On those slopes, trust was a thing the village extended freely, and a thing it could not afford to lose.

Carol had written a drill-card with three steps: read x, read x again, read x a third time. But then she realized the final step should return 99 instead.

Tom asked: if the drill-card lists man...
    ```
- `G8-01` (form `(defn speak [k] (cond (= k :wolf) "howl" (= k :flock) "bleat`): user_msg 208 words
    ```
    On a hill above the village, a boy watched sheep, and the sheep watched the grass, and the day moved slowly.

Carol had called a meeting of the shepherds' fellowship on the village green — sheep-shepherd, goat-shepherd, geese-keeper, all gathered. Each kind of keeper had their own way of raising an ...
    ```
- `G9-07` (form `(do (def r (ref 0)) (dosync (alter r inc)) @r)`): user_msg 218 words
    ```
    It happened at the edge of the orchard, on a hill where shouting carries far and trust carries further, until it doesn't.

Carol led Tom into the watchhouse vault, where the ledger lay under lock. 'This record is precious,' she said. 'You cannot touch it alone. We enter together, I read the page, yo...
    ```

#### SMALL_INT_LEAK

- `G3-03` (form `(let [x 3] (+ x 1))`): small-int answer 4 leaks via resolution-slot phrasing
    ```
    The hilltop offered a fine view of both the flock and the road below, where help would have to come from.

Carol the elder had been counting along a stretch of fence-line at dawn. She slipped a tally-token worth 3 lambs into the small leather belt-pouch at her hip and gave the pouch's contents the l...
    ```
- `G3-07` (form `((fn [x] (+ x 1)) 4)`): small-int answer 5 leaks via resolution-slot phrasing
    ```
    It happened at the edge of the orchard, on a hill where shouting carries far and trust carries further, until it doesn't.

On the watchhouse wall, Carol the elder had pinned a small drill-card with no name at the top — just the steps for what to do once an unnamed quantity arrived. Tom waited beside...
    ```
- `G7-13` (form `(count (clojure.string/split-lines "a\nb\nc"))`): small-int answer 3 leaks via resolution-slot phrasing
    ```
    On those slopes, trust was a thing the village extended freely, and a thing it could not afford to lose.

The village log-book had been split into lines. Carol asked Tom to count how many lines the scroll held.

Before processing the log, the village needs to know its size. Tom had to count the line...
    ```

#### SENTENCE_START_LOWER_PRONOUN

- `G3-04` (form `(let [x 5 y 3] (- x y))`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    It happened at the edge of the meadow, on a hill where shouting carries far and trust carries further, until it doesn't.

Barak, calling out without confidence anyone would come, was beginning to understand:
the belt-pouch was not magic, only careful. Ulysses took the
goal — to bind x to 5 and y to ...
    ```
- `G3-11` (form `(let [a 7] (+ a a))`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    at the edge of the meadow, on a slope above the village, Calista watched his flock and his shadow grow longer.

Calista, wide-eyed with fear, was beginning to understand:
the belt-pouch was not magic, only careful. Anselmo took the
goal — to bind a to 7 and add a to itself — and composed the binding...
    ```
- `G3-11` (form `((fn [x] (* x x)) 6)`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    The pasture lay below a rocky lookout, and the sheep were easier to count than the hours.

Rosa, voice still hoarse from yesterday's false alarm, was beginning to understand:
the belt-pouch was not magic, only careful. Salomea took the
goal — to apply a function that squares its argument to 6 — and ...
    ```
- `G3-18` (form `(let [n 5] (* n n n))`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    at the edge of the meadow, on a slope above the village, Olav watched his flock and his shadow grow longer.

Olav, in a panic, was beginning to understand:
the belt-pouch was not magic, only careful. Perpetua took the
goal — to bind n to 5 and compute n cubed — and composed the named binding used mu...
    ```
- `G8-02` (form `(do (deftype Lantern [color]) (.-color (Lantern. "amber")))`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    An empty hour can sometimes be filled with mischief, and mischief once started has a way of escalating.

Dylan, in a panic, was beginning to see: the
tally-box was not magic, only careful naming. Leopold took
the goal — to  — and composed a deftype Lantern with a color field, then read color of an i...
    ```

#### ANSWER_LEAK_STRING

- `G6-01` (form `(name 'foo.bar)`): answer string 'foo.bar' appears in user_msg
    ```
    On a hill above the village, a boy watched sheep, and the sheep watched the grass, and the day moved slowly.

Tom stood at the village notice-post, where scrolls hung labeled with dotted names. Carol showed him the scroll marked `foo.bar`—a namespace written as a symbol.

Tom wanted to know what the...
    ```
- `G7-10` (form `(:doc (meta '^{:doc "adds two"} plus))`): answer string 'adds two' appears in user_msg
    ```
    The hilltop offered a fine view of both the flock and the road below, where help would have to come from.

Carol carved a drill-card on the watchhouse wall. Above the recipe's steps, she chalked a small note: "adds two". Tom asked what the note was for. Carol opened the metadata.

Every drill-card n...
    ```
- `G8-05` (form `(do (defprotocol Greet (hail [this])) (extend-protocol Greet`): answer string ':number' appears in user_msg
    ```
    The wolves of those hills were rare but not absent, and the shepherds knew it was safer to be vigilant than clever.

Carol had posted a Greet protocol at the fold-gate. A number-keeper — a tender of the tally-sticks — offered their pledge: any number greeting would return the keyword `:number`.

The...
    ```
- `G11-02` (form `(. "abc" toUpperCase)`): answer string 'ABC' appears in user_msg
    ```
    The pasture lay below a rocky lookout, and the sheep were easier to count than the hours.

Tom noticed a second way to write the same kind of tool-call, using the same dot but with the syntax stretched out: `(. object method)`. Carol explained this was the more explicit form.

Tom wanted to understa...
    ```
- `G11-02` (form `(. "abc" toUpperCase)`): answer string 'ABC' appears in user_msg
    ```
    The pasture lay below a rocky lookout, and the sheep were easier to count than the hours.

Tom noticed a second way to write the same kind of tool-call, using the same dot but with the syntax stretched out: `(. object method)`. Carol explained this was the more explicit form.

Tom wanted to understa...
    ```

#### VILLAGE_NOUN_OVERUSE

- `G6-07` (form `(boolean (:private (meta '^:private hidden)))`): `the village` appears 4 times (noun-saturation tic — vary or drop)
    ```
    It happened at the edge of the orchard, on a hill where shouting carries far and trust carries further, until it doesn't.

Carol showed Tom two entries in the village log-book. One symbol, `hidden`, carried a private marker in its margin. Carol asked Tom to convert the raw answer to a simple true or...
    ```
- `G6-10` (form `(get-in {:paths ["src"]} [:paths 0])`): `the village` appears 4 times (noun-saturation tic — vary or drop)
    ```
    Melina had cried wolf once already, near the road, and the villagers had laughed but not entirely.

At the village notice-stone on the road, the question of the day was
posted: how to extract the first entry from the :paths vector in a deps-style map. Melina, with the swagger of an unrepentant fibbe...
    ```
- `G11-08` (form `(let [^long n 42] (+ n 8))`): `the village` appears 4 times (noun-saturation tic — vary or drop)
    ```
    Petar was supposed to keep the sheep safe; instead, in the village, he kept inventing reasons for the village to run.

"There's the village's own toolshed," Diogenes said, "and
there's the foreign one. The runtime moves a value across the
boundary, calls the foreign tool, and brings the result back ...
    ```
- `G12-06` (form `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42)`): `the village` appears 4 times (noun-saturation tic — vary or drop)
    ```
    The wolves of those hills were rare but not absent, and the shepherds knew it was safer to be vigilant than clever.

At the village notice-stone in the village, the question of the day was
posted: how to use spec to validate that 42 conforms to the int? predicate. Veronika, sounding sure of every wo...
    ```
- `G12-06` (form `(do (require '[clojure.spec.alpha :as s]) (s/valid? string? `): `the village` appears 4 times (noun-saturation tic — vary or drop)
    ```
    The hilltop offered a fine view of both the flock and the road below, where help would have to come from.

At the village notice-stone in the village, the question of the day was
posted: how to use spec to validate that 42 conforms to the string? predicate. Stavros, with the swagger of an unrepentan...
    ```

#### WRONG_FABLE_LITERAL

- `G8-13` (form `(do (defprotocol Named (name-of [this])) (defrecord Shepherd`): tortoise-hare ghost name 'Pip' appears in boy-wolf user_msg
    ```
    On those slopes, trust was a thing the village extended freely, and a thing it could not afford to lose.

Carol had a Shepherd tally-box with a name slot. When she asked the box to tell her its name via the `name-of` method, the box could refer to itself as `this` and pull its own name out.

A proto...
    ```

#### COLLECTION_LEAK

- `G12-03` (form `(into #{} (map inc) [1 2 3])`): elements of expected {2, 3, 4} appear comma-separated in user_msg (collection answer leak)
    ```
    The lambs were milling in the lower meadow when the boy first thought of the joke he should not have made.

Carol had an empty unique-only basket — one that would not hold duplicates. The fleece-comb with its increment rule waited. Three numbers sat ready to be poured through.

The numbers needed to...
    ```

