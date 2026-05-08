# boy-wolf curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

## Grade 2

### G2-13: and / or — short circuit, return values

- examples: 6
- variety @ n=50: 0.98
- issues: {'CONCEPT_AS_VERB': 4}
    - [CONCEPT_AS_VERB] form=`(and true true)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(and true true)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(or false false)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(or nil false 5)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G2-14: not — turning truthy to false

- examples: 5
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 3}
    - [CONCEPT_AS_VERB] form=`(not true)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(not 0)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(not "")` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G2-16: Truthy 0 and empty string

- examples: 4
- variety @ n=50: 0.99
- issues: {'CONCEPT_AS_VERB': 2}
    - [CONCEPT_AS_VERB] form=`(boolean 0)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(boolean false)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G2-20: Counting

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOWERCASE_PRONOUN_AFTER_PERIOD': 1}
    - [LOWERCASE_PRONOUN_AFTER_PERIOD] form=`(count "hello")` — sentence-initial pronoun (she/he/they) appears lowercase after a period (pronoun-substitution did not capitalize at sentence start)

## Grade 3

### G3-03: let — local binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOWERCASE_PRONOUN_AFTER_PERIOD': 1}
    - [LOWERCASE_PRONOUN_AFTER_PERIOD] form=`(let [n 10] (* n n))` — sentence-initial pronoun (she/he/they) appears lowercase after a period (pronoun-substitution did not capitalize at sentence start)

### G3-04: let — multi-binding

- examples: 3
- variety @ n=50: 0.99
- issues: {'LOWERCASE_PRONOUN_AFTER_PERIOD': 1}
    - [LOWERCASE_PRONOUN_AFTER_PERIOD] form=`(let [x 5 y 3] (- x y))` — sentence-initial pronoun (she/he/they) appears lowercase after a period (pronoun-substitution did not capitalize at sentence start)

### G3-05: let — shadowing outer def

- examples: 2
- variety @ n=50: 0.98
- issues: {'LOWERCASE_PRONOUN_AFTER_PERIOD': 1}
    - [LOWERCASE_PRONOUN_AFTER_PERIOD] form=`(do (def x 10) (let [x 99] x))` — sentence-initial pronoun (she/he/they) appears lowercase after a period (pronoun-substitution did not capitalize at sentence start)

### G3-07: fn — anonymous function

- examples: 2
- variety @ n=50: 0.99
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`((fn [x] (+ x 1)) 4)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G3-09: defn — shorthand

- examples: 2
- variety @ n=50: 0.98
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G3-15: Side-effects in body

- examples: 1
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`(do (println "hi") 42)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G3-16: Name collision: namespace vs let

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOWERCASE_PRONOUN_AFTER_PERIOD': 1}
    - [LOWERCASE_PRONOUN_AFTER_PERIOD] form=`(let [+ 99] +)` — sentence-initial pronoun (she/he/they) appears lowercase after a period (pronoun-substitution did not capitalize at sentence start)

### G3-18: When to name vs inline

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOWERCASE_PRONOUN_AFTER_PERIOD': 1}
    - [LOWERCASE_PRONOUN_AFTER_PERIOD] form=`(let [n 5] (* n n n))` — sentence-initial pronoun (she/he/they) appears lowercase after a period (pronoun-substitution did not capitalize at sentence start)

## Grade 4

### G4-10: keys and vals

- examples: 1
- variety @ n=50: 0.94

## Grade 5

### G5-07: and / or as control flow

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`(and 1 2 3)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G5-12: reduce

- examples: 3
- variety @ n=50: 0.99
- issues: {'LOWERCASE_PRONOUN_AFTER_PERIOD': 2}
    - [LOWERCASE_PRONOUN_AFTER_PERIOD] form=`(reduce + [1 2 3 4])` — sentence-initial pronoun (she/he/they) appears lowercase after a period (pronoun-substitution did not capitalize at sentence start)
    - [LOWERCASE_PRONOUN_AFTER_PERIOD] form=`(reduce max [3 1 4 1 5 9 2 6])` — sentence-initial pronoun (she/he/they) appears lowercase after a period (pronoun-substitution did not capitalize at sentence start)

### G5-13: reduce with init

- examples: 2
- variety @ n=50: 0.98
- issues: {'LOWERCASE_PRONOUN_AFTER_PERIOD': 1}
    - [LOWERCASE_PRONOUN_AFTER_PERIOD] form=`(reduce + 100 [1 2 3])` — sentence-initial pronoun (she/he/they) appears lowercase after a period (pronoun-substitution did not capitalize at sentence start)

### G5-15: comp

- examples: 2
- variety @ n=50: 0.98
- issues: {'CONCEPT_AS_VERB': 3}
    - [CONCEPT_AS_VERB] form=`((comp inc inc) 5)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`((comp str inc) 9)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`((comp str inc) 9)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G5-16: partial

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 3}
    - [CONCEPT_AS_VERB] form=`((partial + 10) 5)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(map (partial * 3) [1 2 3])` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(map (partial * 3) [1 2 3])` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G5-17: juxt

- examples: 1
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`((juxt inc dec) 5)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

## Grade 6

## Grade 7

## Grade 8

### G8-03: defrecord introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOWERCASE_PRONOUN_AFTER_PERIOD': 1}
    - [LOWERCASE_PRONOUN_AFTER_PERIOD] form=`(do (defrecord Watcher [name post]) (:name (->Watc` — sentence-initial pronoun (she/he/they) appears lowercase after a period (pronoun-substitution did not capitalize at sentence start)

## Grade 9

## Grade 10

### G10-05: macroexpand

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOWERCASE_PRONOUN_AFTER_PERIOD': 1}
    - [LOWERCASE_PRONOUN_AFTER_PERIOD] form=`(macroexpand '(when true 1))` — sentence-initial pronoun (she/he/they) appears lowercase after a period (pronoun-substitution did not capitalize at sentence start)

### G10-06: when and when-not as macros

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOWERCASE_PRONOUN_AFTER_PERIOD': 1}
    - [LOWERCASE_PRONOUN_AFTER_PERIOD] form=`(when false 1 2 3)` — sentence-initial pronoun (she/he/they) appears lowercase after a period (pronoun-substitution did not capitalize at sentence start)

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 0.98
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`(-> 5 inc inc inc)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G10-08: Macro vs fn

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOWERCASE_PRONOUN_AFTER_PERIOD': 1}
    - [LOWERCASE_PRONOUN_AFTER_PERIOD] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — sentence-initial pronoun (she/he/they) appears lowercase after a period (pronoun-substitution did not capitalize at sentence start)

### G10-10: Anaphoric macros are confusing

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOWERCASE_PRONOUN_AFTER_PERIOD': 3}
    - [LOWERCASE_PRONOUN_AFTER_PERIOD] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — sentence-initial pronoun (she/he/they) appears lowercase after a period (pronoun-substitution did not capitalize at sentence start)
    - [LOWERCASE_PRONOUN_AFTER_PERIOD] form=`(if-let [x 7] (* x x) 0)` — sentence-initial pronoun (she/he/they) appears lowercase after a period (pronoun-substitution did not capitalize at sentence start)
    - [LOWERCASE_PRONOUN_AFTER_PERIOD] form=`(if-let [x 7] (* x x) 0)` — sentence-initial pronoun (she/he/they) appears lowercase after a period (pronoun-substitution did not capitalize at sentence start)

### G10-14: eval (the function)

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOWERCASE_PRONOUN_AFTER_PERIOD': 1}
    - [LOWERCASE_PRONOUN_AFTER_PERIOD] form=`(eval '(+ 1 2 3))` — sentence-initial pronoun (she/he/they) appears lowercase after a period (pronoun-substitution did not capitalize at sentence start)

### G10-16: Macro pattern library

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOWERCASE_PRONOUN_AFTER_PERIOD': 2}
    - [LOWERCASE_PRONOUN_AFTER_PERIOD] form=`(do (defmacro with-careful-watch [& body] `(let [p` — sentence-initial pronoun (she/he/they) appears lowercase after a period (pronoun-substitution did not capitalize at sentence start)
    - [LOWERCASE_PRONOUN_AFTER_PERIOD] form=`(do (defmacro def-watch [name v] `(def ~name ~v)) ` — sentence-initial pronoun (she/he/they) appears lowercase after a period (pronoun-substitution did not capitalize at sentence start)

## Grade 11

## Grade 12

---

## Summary

### Issue counts (across all examples × 3 records)

- **CONCEPT_AS_VERB**: 21
- **LOWERCASE_PRONOUN_AFTER_PERIOD**: 19

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 80 | 0 | — |
| 2 | 22 | 88 | 10 | — |
| 3 | 18 | 31 | 8 | — |
| 4 | 20 | 39 | 0 | G4-10(0.94) |
| 5 | 22 | 39 | 11 | — |
| 6 | 16 | 33 | 0 | — |
| 7 | 18 | 36 | 0 | — |
| 8 | 16 | 31 | 1 | — |
| 9 | 18 | 34 | 0 | — |
| 10 | 16 | 36 | 10 | — |
| 11 | 14 | 58 | 0 | — |
| 12 | 18 | 37 | 0 | — |

### Sample issues by severity

#### CONCEPT_AS_VERB

- `G2-13` (form `(and true true)`): concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    ```
    A young shepherd had been left alone with the flock far too often, and boredom had taken root.

"You can't tell which way the fold-gates will swing by guessing," Robin
said. "You bring the value to the first gate, the runtime checks it, and if
that gate closes, the chain stops — the rest of the gate...
    ```
- `G2-13` (form `(and true true)`): concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    ```
    Every shepherd in the valley knew the danger of crying wolf for sport.

"You can't tell which way the fold-gates will swing by guessing," Sam
said. "You bring the value to the first gate, the runtime checks it, and if
that gate closes, the chain stops — the rest of the gates never even see the
value...
    ```
- `G2-13` (form `(or false false)`): concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    ```
    A young shepherd had been left alone with the flock far too often, and boredom had taken root.

"You can't tell which way the fold-gates will swing by guessing," Alice
said. "You bring the value to the first gate, the runtime checks it, and if
that gate closes, the chain stops — the rest of the gate...
    ```
- `G2-13` (form `(or nil false 5)`): concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    ```
    It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened at the farm.

"You can't tell which way the fold-gates will swing by guessing," Alex
said. "You bring the value to the first gate, the runtime checks it, and if
that gate closes, th...
    ```
- `G2-14` (form `(not true)`): concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    ```
    A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place at the edge of the orchard.

"You can't tell which way the fold-gates will swing by guessing," Grace
said. "You bring the value to the first gate, the runtime checks it, and if
that gat...
    ```

#### LOWERCASE_PRONOUN_AFTER_PERIOD

- `G2-20` (form `(count "hello")`): sentence-initial pronoun (she/he/they) appears lowercase after a period (pronoun-substitution did not capitalize at sentence start)
    ```
    The boy on the hill thought the trick clever the first time he played it. It happened in the forest.

Jess, in a panic, was beginning to understand: the
tally-stick walk was not magic, only patient. Morgan took the
goal — to count the characters in the string hello — and composed the count operation...
    ```
- `G3-03` (form `(let [n 10] (* n n))`): sentence-initial pronoun (she/he/they) appears lowercase after a period (pronoun-substitution did not capitalize at sentence start)
    ```
    The boy on the hill thought the trick clever the first time he played it.

Lou, wide-eyed with fear, was beginning to understand:
the belt-pouch was not magic, only careful. Alex took the
goal — to bind n to 10 and compute n squared — and composed the local binding and multiplication, the value
tuck...
    ```
- `G3-04` (form `(let [x 5 y 3] (- x y))`): sentence-initial pronoun (she/he/they) appears lowercase after a period (pronoun-substitution did not capitalize at sentence start)
    ```
    A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Tom, calling out without confidence anyone would come, was beginning to understand:
the belt-pouch was not magic, only careful. Grace took the
goal — to bind x to 5 and y to 3, then subtract y from x — an...
    ```
- `G3-05` (form `(do (def x 10) (let [x 99] x))`): sentence-initial pronoun (she/he/they) appears lowercase after a period (pronoun-substitution did not capitalize at sentence start)
    ```
    The boy on the hill thought the trick clever the first time he played it.

Lou, calling out without confidence anyone would come, was beginning to understand:
the belt-pouch was not magic, only careful. Frank took the
goal — to define x at the top level, then shadow it locally and return the inner v...
    ```
- `G3-16` (form `(let [+ 99] +)`): sentence-initial pronoun (she/he/they) appears lowercase after a period (pronoun-substitution did not capitalize at sentence start)
    ```
    It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Jess, in a panic, was beginning to understand:
the belt-pouch was not magic, only careful. Morgan took the
goal — to shadow the plus operator with a local binding and return the bound value — ...
    ```

