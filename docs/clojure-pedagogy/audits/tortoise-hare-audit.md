# tortoise-hare curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

### G1-15: Equality

- examples: 6
- variety @ n=50: 0.98
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`(= 1 2)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

## Grade 2

### G2-13: and / or — short circuit, return values

- examples: 6
- variety @ n=50: 0.98
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`(and true true)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G2-14: not — turning truthy to false

- examples: 5
- variety @ n=50: 0.98
- issues: {'CONCEPT_AS_VERB': 2}
    - [CONCEPT_AS_VERB] form=`(not false)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(not 0)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G2-15: Falsey values: only false and nil

- examples: 4
- variety @ n=50: 0.98
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`(if "" 1 0)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G2-16: Truthy 0 and empty string

- examples: 4
- variety @ n=50: 0.97
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`(boolean "")` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G2-18: Quoting symbols

- examples: 3
- variety @ n=50: 0.95

## Grade 3

### G3-07: fn — anonymous function

- examples: 2
- variety @ n=50: 0.96
- issues: {'CONCEPT_AS_VERB': 3}
    - [CONCEPT_AS_VERB] form=`((fn [a b] (* a b)) 3 4)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`((fn [a b] (* a b)) 3 4)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`((fn [a b] (* a b)) 3 4)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G3-09: defn — shorthand

- examples: 2
- variety @ n=50: 0.96
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 0.98
- issues: {'CONCEPT_AS_VERB': 2}
    - [CONCEPT_AS_VERB] form=`(#(+ % 1) 5)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(#(+ % 1) 5)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G3-13: fn body returns last form

- examples: 1
- variety @ n=50: 0.94

### G3-15: Side-effects in body

- examples: 1
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 2}
    - [CONCEPT_AS_VERB] form=`(do (println "hi") 42)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(do (println "hi") 42)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

## Grade 4

## Grade 5

### G5-07: and / or as control flow

- examples: 2
- variety @ n=50: 0.98
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`(and 1 2 3)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G5-09: fn as value

- examples: 1
- variety @ n=50: 0.94

### G5-15: comp

- examples: 2
- variety @ n=50: 0.98
- issues: {'CONCEPT_AS_VERB': 3}
    - [CONCEPT_AS_VERB] form=`((comp inc inc) 5)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`((comp inc inc) 5)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`((comp str inc) 9)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G5-16: partial

- examples: 2
- variety @ n=50: 0.99
- issues: {'CONCEPT_AS_VERB': 4}
    - [CONCEPT_AS_VERB] form=`((partial + 10) 5)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`((partial + 10) 5)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(map (partial * 3) [1 2 3])` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(map (partial * 3) [1 2 3])` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G5-17: juxt

- examples: 1
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`((juxt inc dec) 5)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

## Grade 6

### G6-13: Aliasing conventions

- examples: 1
- variety @ n=50: 0.94

## Grade 7

## Grade 8

### G8-02: deftype introduction

- examples: 2
- variety @ n=50: 0.92

### G8-13: this-style vs fn-style

- examples: 2
- variety @ n=50: 0.94

### G8-14: Protocols don't inherit

- examples: 1
- variety @ n=50: 0.92

## Grade 9

## Grade 10

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 0.97
- issues: {'CONCEPT_AS_VERB': 5}
    - [CONCEPT_AS_VERB] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(macroexpand '(-> x f g))` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(macroexpand '(-> x f g))` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

## Grade 11

## Grade 12

---

## Summary

### Issue counts (across all examples × 3 records)

- **CONCEPT_AS_VERB**: 28

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 1 | — |
| 2 | 22 | 88 | 5 | G2-18(0.95) |
| 3 | 18 | 31 | 8 | G3-13(0.94) |
| 4 | 20 | 39 | 0 | — |
| 5 | 22 | 39 | 9 | G5-09(0.94) |
| 6 | 16 | 33 | 0 | G6-13(0.94) |
| 7 | 18 | 36 | 0 | — |
| 8 | 16 | 31 | 0 | G8-02(0.92); G8-13(0.94); G8-14(0.92) |
| 9 | 18 | 34 | 0 | — |
| 10 | 16 | 36 | 5 | — |
| 11 | 14 | 29 | 0 | — |
| 12 | 18 | 37 | 0 | — |

### Sample issues by severity

#### CONCEPT_AS_VERB

- `G1-15` (form `(= 1 2)`): concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    ```
    The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the faster. This was at the edge of the forest.

"You can't tell which way the gate will swing by guessing,"
Mossback the tortoise said. "You bring the value to the gate, the
runtime checks it, and the gate...
    ```
- `G2-13` (form `(and true true)`): concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    ```
    The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the faster.

"You can't tell which way the gate will swing by guessing,"
Mossback the tortoise said. "You bring the value to the gate, the
runtime checks it, and the gate gives the only answer that
matters....
    ```
- `G2-14` (form `(not false)`): concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    ```
    The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the faster.

"You can't tell which way the gate will swing by guessing,"
Slowpoke the tortoise said. "You bring the value to the gate, the
runtime checks it, and the gate gives the only answer that
matters....
    ```
- `G2-14` (form `(not 0)`): concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    ```
    There was once a Hare whose pride matched her feet in speed, and a Tortoise who said nothing about either.

"You can't tell which way the gate will swing by guessing,"
Mossback the tortoise said. "You bring the value to the gate, the
runtime checks it, and the gate gives the only answer that
matters...
    ```
- `G2-15` (form `(if "" 1 0)`): concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    ```
    The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the faster. This was at the edge of the forest.

"You can't tell which way the gate will swing by guessing,"
Mossback the tortoise said. "You bring the value to the gate, the
runtime checks it, and the gate...
    ```

