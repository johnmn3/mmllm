# milkmaid curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

### G1-01: Eval as substitution

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`0` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`nil` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation

### G1-02: Integer numbers

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`-3` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`0` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`0` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation

### G1-05: Booleans

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6}
    - [LOW_GROUNDING] form=`true` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`false` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`false` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`(= 1 1)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`(= 1 1)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`(= 1 1)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation

### G1-06: nil

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4}
    - [LOW_GROUNDING] form=`(nil? nil)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`(nil? nil)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`(nil? 0)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`(nil? false)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation

### G1-09: Symbols vs values

- examples: 4
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(symbol? 'hare)` — user_msg has a generic emotion-adverb dialogue tag (softly/quietly/gently/calmly) but no environment-anchored EMO phrase — tone named but not grounded
    - [LOW_GROUNDING] form=`(= 'hare 'hare)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`(= 'hare 'hare)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation

### G1-13: First arithmetic call

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOWERCASE_CONCEPT_AFTER_PERIOD': 2}
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(- 5 3)` — sentence-initial 'the X verb' (lowercase concept_phrase as subject) — produced when subplot template ends a sentence with a period before {concept_phrase}
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(- 20 7)` — sentence-initial 'the X verb' (lowercase concept_phrase as subject) — produced when subplot template ends a sentence with a period before {concept_phrase}

### G1-15: Equality

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6}
    - [LOW_GROUNDING] form=`(= 1 1)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`(= 1 1)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`(= 1 1)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`(= 1 1 1 1)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`(= 1 1 1 1)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`(= 1 1 1 1)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation

### G1-16: Numeric predicates

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOWERCASE_CONCEPT_AFTER_PERIOD': 1}
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(zero? 0)` — sentence-initial 'the X verb' (lowercase concept_phrase as subject) — produced when subplot template ends a sentence with a period before {concept_phrase}

## Grade 2

### G2-03: not= and = with multiple args

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOWERCASE_CONCEPT_AFTER_PERIOD': 1}
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(not= 1 1)` — sentence-initial 'the X verb' (lowercase concept_phrase as subject) — produced when subplot template ends a sentence with a period before {concept_phrase}

### G2-06: inc and dec

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOWERCASE_CONCEPT_AFTER_PERIOD': 1}
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(dec 0)` — sentence-initial 'the X verb' (lowercase concept_phrase as subject) — produced when subplot template ends a sentence with a period before {concept_phrase}

### G2-07: Absolute value

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOWERCASE_CONCEPT_AFTER_PERIOD': 1}
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(abs 5)` — sentence-initial 'the X verb' (lowercase concept_phrase as subject) — produced when subplot template ends a sentence with a period before {concept_phrase}

### G2-08: Arithmetic on ratios

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'LOWERCASE_CONCEPT_AFTER_PERIOD': 3}
    - [LOW_GROUNDING] form=`(+ 1/2 1/4)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(+ 1/2 1/4)` — sentence-initial 'the X verb' (lowercase concept_phrase as subject) — produced when subplot template ends a sentence with a period before {concept_phrase}
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(* 2/3 3/4)` — sentence-initial 'the X verb' (lowercase concept_phrase as subject) — produced when subplot template ends a sentence with a period before {concept_phrase}
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(* 2/3 3/4)` — sentence-initial 'the X verb' (lowercase concept_phrase as subject) — produced when subplot template ends a sentence with a period before {concept_phrase}

### G2-09: Floats vs ints (the / operator)

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOWERCASE_CONCEPT_AFTER_PERIOD': 1}
    - [LOWERCASE_CONCEPT_AFTER_PERIOD] form=`(/ 1.0 2)` — sentence-initial 'the X verb' (lowercase concept_phrase as subject) — produced when subplot template ends a sentence with a period before {concept_phrase}

### G2-10: Powers via repeated multiplication

- examples: 4
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1}
    - [ANSWER_LEAK] form=`(* 3 3 3 3)` — answer 81 in narrative

### G2-13: and / or — short circuit, return values

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 12}
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`(and true false)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`(and true false)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`(and true false)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation

### G2-14: not — turning truthy to false

- examples: 5
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 12}
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`(not false)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`(not false)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`(not false)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation

### G2-15: Falsey values: only false and nil

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(if nil 1 0)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`(if nil 1 0)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`(if false 1 0)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation

### G2-18: Quoting symbols

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg has a generic emotion-adverb dialogue tag (softly/quietly/gently/calmly) but no environment-anchored EMO phrase — tone named but not grounded
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg has a generic emotion-adverb dialogue tag (softly/quietly/gently/calmly) but no environment-anchored EMO phrase — tone named but not grounded

### G2-19: Auto-promotion to bigint

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(* 1000000 1000000)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`(* 1000000 1000000)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation

## Grade 3

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2}
    - [HIGH_LENGTH] form=`(#(+ % 1) 5)` — user_msg 221 words
    - [HIGH_LENGTH] form=`(#(* %1 %2) 3 4)` — user_msg 201 words

### G3-13: fn body returns last form

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`((fn [x] x x x 99) 1)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`((fn [x] x x x 99) 1)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`((fn [x] x x x 99) 1)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation

### G3-16: Name collision: namespace vs let

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(let [+ 99] +)` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation

## Grade 4

### G4-01: Vector literal

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'FORM_LEAK': 2}
    - [LOW_GROUNDING] form=`["a" "b"]` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [FORM_LEAK] form=`["a" "b"]` — form '["a" "b"]' appears in user_msg of a goal-style subject
    - [LOW_GROUNDING] form=`["a" "b"]` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [FORM_LEAK] form=`["a" "b"]` — form '["a" "b"]' appears in user_msg of a goal-style subject
    - [LOW_GROUNDING] form=`["a" "b"]` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation

### G4-11: Set literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(count #{1 1 1})` — user_msg 204 words

### G4-16: into and conj on collections

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'FORM_LEAK': 1}
    - [LOW_GROUNDING] form=`(into #{} [1 2 2 3])` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [LOW_GROUNDING] form=`(into #{} [1 2 2 3])` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation
    - [FORM_LEAK] form=`(into #{} [1 2 2 3])` — form '(into #{} [1 2 2 3])' appears in user_msg of a goal-style subject

### G4-19: range and seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(count (range 5))` — user_msg has a generic emotion-adverb dialogue tag (softly/quietly/gently/calmly) but no environment-anchored EMO phrase — tone named but not grounded

## Grade 5

### G5-08: not

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(not (> 1 2))` — user_msg lacks both a drawn-value reference (literal from form) AND any environment-anchored EMO phrase — no grounding for the operation

### G5-10: map

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(map #(* % %) [1 2 3 4])` — user_msg 201 words

### G5-22: recur — first taste

- examples: 1
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — user_msg 205 words

## Grade 6

### G6-02: ns form

