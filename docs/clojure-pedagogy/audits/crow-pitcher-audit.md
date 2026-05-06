# crow-pitcher curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

## Grade 2

### G2-16: Truthy 0 and empty string

- examples: 4
- variety @ n=50: 0.94

## Grade 3

### G3-05: let — shadowing outer def

- examples: 2
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (def x 10) (let [x 99] x) x)` — user_msg 205 words

### G3-12: Scope vs namespace

- examples: 1
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 2}
    - [HIGH_LENGTH] form=`(do (def g 5) (let [g 99] (+ g 1)))` — user_msg 206 words
    - [HIGH_LENGTH] form=`(do (def g 5) (let [g 99] (+ g 1)))` — user_msg 205 words

## Grade 4

### G4-16: into and conj on collections

- examples: 2
- variety @ n=50: 0.94

## Grade 5

### G5-08: not

- examples: 1
- variety @ n=50: 0.94

### G5-16: partial

- examples: 2
- variety @ n=50: 0.93

## Grade 6

### G6-05: Fully qualified names

- examples: 4
- variety @ n=50: 0.98
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(name :owner/item)` — answer string 'item' appears in user_msg

## Grade 7

### G7-11: Reading stack traces

- examples: 2
- variety @ n=50: 0.97
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(try (throw (ex-info "trouble" {})) (catch Excepti` — answer string 'trouble' appears in user_msg

### G7-12: slurp and spit

- examples: 2
- variety @ n=50: 0.98
- issues: {'ANSWER_LEAK': 2}
    - [ANSWER_LEAK] form=`(count "hare
tortoise
")` — answer 14 in narrative
    - [ANSWER_LEAK] form=`(count "hare
tortoise
")` — answer 14 in narrative

## Grade 8

### G8-03: defrecord introduction

- examples: 2
- variety @ n=50: 0.95
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defrecord Runner [name pace]) (:name (->Runne` — user_msg 202 words

### G8-08: Multimethod defmulti

- examples: 2
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 2}
    - [HIGH_LENGTH] form=`(do (defmulti pace :species) (defmethod pace :hare` — user_msg 208 words
    - [HIGH_LENGTH] form=`(do (defmulti pace :species) (defmethod pace :hare` — user_msg 202 words

### G8-14: Protocols don't inherit

- examples: 1
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg 220 words

## Grade 9

### G9-08: dosync and alter

- examples: 2
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 2}
    - [HIGH_LENGTH] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — user_msg 208 words
    - [HIGH_LENGTH] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — user_msg 202 words

### G9-17: binding — thread-local

- examples: 2
- variety @ n=50: 0.96
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — user_msg 209 words

## Grade 10

### G10-16: Macro pattern library

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — user_msg 204 words

## Grade 11

### G11-08: Type hints

- examples: 2
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(let [^String s "abc"] (.toUpperCase s))` — user_msg 204 words

## Grade 12

### G12-02: Transducer composition

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — user_msg 201 words

---

## Summary

### Issue counts (across all examples × 3 records)

- **HIGH_LENGTH**: 13
- **ANSWER_LEAK_STRING**: 2
- **ANSWER_LEAK**: 2

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 0 | — |
| 2 | 22 | 88 | 0 | G2-16(0.94) |
| 3 | 18 | 31 | 3 | — |
| 4 | 20 | 39 | 0 | G4-16(0.94) |
| 5 | 22 | 39 | 0 | G5-08(0.94); G5-16(0.93) |
| 6 | 16 | 33 | 1 | — |
| 7 | 18 | 36 | 3 | — |
| 8 | 16 | 31 | 4 | — |
| 9 | 18 | 34 | 3 | — |
| 10 | 16 | 36 | 1 | — |
| 11 | 14 | 29 | 1 | — |
| 12 | 18 | 37 | 1 | — |

### Sample issues by severity

#### HIGH_LENGTH

- `G3-05` (form `(do (def x 10) (let [x 99] x) x)`): user_msg 205 words
    ```
    A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened by the market.

Mossback posted x at 10 on the road sign, then walked a detour where her hip-pouch shadowed x with 99. When she returned to the main road, the pouch was empty; only the road sign st...
    ```
- `G3-12` (form `(do (def g 5) (let [g 99] (+ g 1)))`): user_msg 206 words
    ```
    It is said that wit, more than strength, is the friend of the thirsty Crow. This was near the meadow.

The road sign at the trailhead read g = 5. Mossback slipped onto a side-path and tied a fresh pouch at her hip labeled g, loaded with 99 acorns. She needed g plus one more while on the side-path.

...
    ```
- `G3-12` (form `(do (def g 5) (let [g 99] (+ g 1)))`): user_msg 205 words
    ```
    Hunger and thirst had driven the Crow far from her usual perch. All this took place by the market.

The road sign at the trailhead read g = 5. Mossback slipped onto a side-path and tied a fresh pouch at her hip labeled g, loaded with 99 acorns. She needed g plus one more while on the side-path.

On ...
    ```
- `G8-03` (form `(do (defrecord Runner [name pace]) (:name (->Runner "Bob" :m`): user_msg 202 words
    ```
    It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place near the road.

Mossback the tortoise built a second Runner carrying-case, this time filling the name compartment for a hare and the pace compartment with a moderate-pace keyword. She wanted to prove that...
    ```
- `G8-08` (form `(do (defmulti pace :species) (defmethod pace :hare [_] :swif`): user_msg 208 words
    ```
    The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Mossback the tortoise set up a sorting-table at the edge of the meadow. Runners would walk up; the table would read each runner's :species stamp and route them to the matching arm.

Today's first arm she ...
    ```

#### ANSWER_LEAK_STRING

- `G6-05` (form `(name :owner/item)`): answer string 'item' appears in user_msg
    ```
    A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened near the village.

From the same qualified label :owner/item, Mossback now wanted the second part — the local name that lived *within* the namespace.

She needed to know what the routine was called...
    ```
- `G7-11` (form `(try (throw (ex-info "trouble" {})) (catch Exception e (.get`): answer string 'trouble' appears in user_msg
    ```
    It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place near the road.

This time the alarm was an `ex-info` horn — the kind that could carry both a label and a data-map slip. Mossback wanted only the label text; the data-map was empty for this alarm.

She nee...
    ```

#### ANSWER_LEAK

- `G7-12` (form `(count "hare
tortoise
")`): answer 14 in narrative
    ```
    It is said that wit, more than strength, is the friend of the thirsty Crow. This was near the meadow.

Mossback the tortoise had a small two-line message on a scroll — the word `hare` on one line, `tortoise` on the next, each line ending with a newline-mark.

She wanted to know whether the message w...
    ```
- `G7-12` (form `(count "hare
tortoise
")`): answer 14 in narrative
    ```
    Hunger and thirst had driven the Crow far from her usual perch. All this took place by the market.

Mossback the tortoise had a small two-line message on a scroll — the word `hare` on one line, `tortoise` on the next, each line ending with a newline-mark.

She wanted to know whether the message woul...
    ```

