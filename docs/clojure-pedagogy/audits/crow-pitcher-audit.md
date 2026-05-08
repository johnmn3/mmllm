# crow-pitcher curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

### G1-15: Equality

- examples: 6
- variety @ n=50: 0.98
- issues: {'CONCEPT_AS_VERB': 5}
    - [CONCEPT_AS_VERB] form=`(= 1 1)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(= 1 1)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(= 1 2)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(= "a" "a")` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(= :hare :tortoise)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

## Grade 2

### G2-13: and / or — short circuit, return values

- examples: 6
- variety @ n=50: 0.99
- issues: {'CONCEPT_AS_VERB': 2}
    - [CONCEPT_AS_VERB] form=`(or false false)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(and 1 2 3)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G2-14: not — turning truthy to false

- examples: 5
- variety @ n=50: 0.99
- issues: {'CONCEPT_AS_VERB': 4}
    - [CONCEPT_AS_VERB] form=`(not true)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(not 0)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(not 0)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(not "")` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G2-15: Falsey values: only false and nil

- examples: 4
- variety @ n=50: 0.98
- issues: {'CONCEPT_AS_VERB': 4}
    - [CONCEPT_AS_VERB] form=`(if 0 1 0)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(if 0 1 0)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(if "" 1 0)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(if nil 1 0)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G2-16: Truthy 0 and empty string

- examples: 4
- variety @ n=50: 0.94
- issues: {'CONCEPT_AS_VERB': 3}
    - [CONCEPT_AS_VERB] form=`(boolean "")` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(boolean "")` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(boolean nil)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

## Grade 3

### G3-07: fn — anonymous function

- examples: 2
- variety @ n=50: 0.96
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`((fn [x] (+ x 1)) 4)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G3-09: defn — shorthand

- examples: 2
- variety @ n=50: 0.97
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

## Grade 4

### G4-16: into and conj on collections

- examples: 2
- variety @ n=50: 0.94

## Grade 5

### G5-07: and / or as control flow

- examples: 2
- variety @ n=50: 0.97
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`(and 1 2 3)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G5-08: not

- examples: 1
- variety @ n=50: 0.94

### G5-16: partial

- examples: 2
- variety @ n=50: 0.93
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`((partial + 10) 5)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G5-17: juxt

- examples: 1
- variety @ n=50: 0.96
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`((juxt inc dec) 5)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

## Grade 6

## Grade 7

## Grade 8

## Grade 9

## Grade 10

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 0.96
- issues: {'CONCEPT_AS_VERB': 3}
    - [CONCEPT_AS_VERB] form=`(-> 5 inc inc inc)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(macroexpand '(-> x f g))` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(macroexpand '(-> x f g))` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

## Grade 11

## Grade 12

---

## Summary

### Issue counts (across all examples × 3 records)

- **CONCEPT_AS_VERB**: 26

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 5 | — |
| 2 | 22 | 88 | 13 | G2-16(0.94) |
| 3 | 18 | 31 | 2 | — |
| 4 | 20 | 39 | 0 | G4-16(0.94) |
| 5 | 22 | 39 | 3 | G5-08(0.94); G5-16(0.93) |
| 6 | 16 | 33 | 0 | — |
| 7 | 18 | 36 | 0 | — |
| 8 | 16 | 31 | 0 | — |
| 9 | 18 | 34 | 0 | — |
| 10 | 16 | 36 | 3 | — |
| 11 | 14 | 29 | 0 | — |
| 12 | 18 | 37 | 0 | — |

### Sample issues by severity

#### CONCEPT_AS_VERB

- `G1-15` (form `(= 1 1)`): concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    ```
    It is said that wit, more than strength, is the friend of the thirsty Crow. This was in the meadow.

"You can't tell which way the gate will swing by guessing,"
Sable the crow said. "You bring the form to the gate, the runtime
checks it, and the gate gives the only answer that matters." To
test whet...
    ```
- `G1-15` (form `(= 1 1)`): concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    ```
    The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

"You can't tell which way the gate will swing by guessing,"
Korvus the crow said. "You bring the form to the gate, the runtime
checks it, and the gate gives the only answer that matters." To
test whether ...
    ```
- `G1-15` (form `(= 1 2)`): concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    ```
    The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened near the farm.

"You can't tell which way the gate will swing by guessing,"
Caw the crow said. "You bring the form to the gate, the runtime
checks it, and the gate gives the only answer that ma...
    ```
- `G1-15` (form `(= "a" "a")`): concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    ```
    It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place in the garden.

"You can't tell which way the gate will swing by guessing,"
Caw the crow said. "You bring the form to the gate, the runtime
checks it, and the gate gives the only answer that matters." To
...
    ```
- `G1-15` (form `(= :hare :tortoise)`): concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    ```
    It is said that wit, more than strength, is the friend of the thirsty Crow.

"You can't tell which way the gate will swing by guessing,"
Sable the crow said. "You bring the form to the gate, the runtime
checks it, and the gate gives the only answer that matters." To
test whether :hare equals :tortoi...
    ```

