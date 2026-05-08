# dog-shadow curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

## Grade 2

### G2-20: Counting

- examples: 3
- variety @ n=50: 0.95

## Grade 3

### G3-07: fn — anonymous function

- examples: 2
- variety @ n=50: 0.98
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`((fn [x] (+ x 1)) 4)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G3-09: defn — shorthand

- examples: 2
- variety @ n=50: 0.97
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 0.99
- issues: {'CONCEPT_AS_VERB': 2}
    - [CONCEPT_AS_VERB] form=`(#(+ % 1) 5)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(#(* %1 %2) 3 4)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G3-15: Side-effects in body

- examples: 1
- variety @ n=50: 0.96
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`(do (println "hi") 42)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

## Grade 4

## Grade 5

### G5-15: comp

- examples: 2
- variety @ n=50: 0.98
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`((comp inc inc) 5)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G5-16: partial

- examples: 2
- variety @ n=50: 0.98
- issues: {'CONCEPT_AS_VERB': 2}
    - [CONCEPT_AS_VERB] form=`((partial + 10) 5)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(map (partial * 3) [1 2 3])` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

### G5-17: juxt

- examples: 1
- variety @ n=50: 0.96
- issues: {'CONCEPT_AS_VERB': 2}
    - [CONCEPT_AS_VERB] form=`((juxt inc dec) 5)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`((juxt inc dec) 5)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

## Grade 6

## Grade 7

## Grade 8

## Grade 9

### G9-05: Watch on atom

- examples: 1
- variety @ n=50: 0.94

## Grade 10

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 0.97
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`(-> 5 inc inc inc)` — concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')

## Grade 11

## Grade 12

---

## Summary

### Issue counts (across all examples × 3 records)

- **CONCEPT_AS_VERB**: 11

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 0 | — |
| 2 | 22 | 88 | 0 | G2-20(0.95) |
| 3 | 18 | 31 | 5 | — |
| 4 | 20 | 39 | 0 | — |
| 5 | 22 | 39 | 5 | — |
| 6 | 16 | 33 | 0 | — |
| 7 | 18 | 36 | 0 | — |
| 8 | 16 | 31 | 0 | — |
| 9 | 18 | 34 | 0 | G9-05(0.94) |
| 10 | 16 | 36 | 1 | — |
| 11 | 14 | 29 | 0 | — |
| 12 | 18 | 37 | 0 | — |

### Sample issues by severity

#### CONCEPT_AS_VERB

- `G3-07` (form `((fn [x] (+ x 1)) 4)`): concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    ```
    What the Dog thought he saw beneath the water turned out to be his own reflection.

"A nose-trail is only useful when it gets walked," Rex the dog
said, head low. "You set out the sniffs, you bring the
ingredients, the runtime does the rest." To create an anonymous function that adds 1 to its argume...
    ```
- `G3-09` (form `(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))`): concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    ```
    A Dog was crossing a stream with a fine bone in his mouth, and was very pleased with himself.

"A nose-trail is only useful when it gets walked," Rex the dog
said, head low. "You set out the sniffs, you bring the
ingredients, the runtime does the rest." To define a function add3 that adds three argu...
    ```
- `G3-10` (form `(#(+ % 1) 5)`): concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    ```
    It is said that the foolish Dog will trade what is real for what is only an image.

"A nose-trail is only useful when it gets walked," Rex the dog
said, head low. "You set out the sniffs, you bring the
ingredients, the runtime does the rest." To use the shorthand syntax to create a function that add...
    ```
- `G3-10` (form `(#(* %1 %2) 3 4)`): concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    ```
    Greed has cost more than one creature what they already had. This was on the village.

"A nose-trail is only useful when it gets walked," Bell the dog
said, head low. "You set out the sniffs, you bring the
ingredients, the runtime does the rest." To use the shorthand syntax to create a function that...
    ```
- `G3-15` (form `(do (println "hi") 42)`): concept_phrase substituted into a slot that needs a finite verb (e.g., 'must calling X', 'I applying Y')
    ```
    A Dog was crossing a stream with a fine bone in his mouth, and was very pleased with himself.

"A nose-trail is only useful when it gets walked," Patch the dog
said, head low. "You set out the sniffs, you bring the
ingredients, the runtime does the rest." To execute a print statement for side-effect...
    ```

