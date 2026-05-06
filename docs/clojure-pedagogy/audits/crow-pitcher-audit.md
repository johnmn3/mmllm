# crow-pitcher curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

## Grade 2

### G2-16: Truthy 0 and empty string

- examples: 4
- variety @ n=50: 0.94

## Grade 3

### G3-09: defn — shorthand

- examples: 2
- variety @ n=50: 0.97
- issues: {'HIGH_LENGTH': 2}
    - [HIGH_LENGTH] form=`(do (defn dbl [x] (* x 2)) (dbl 5))` — user_msg 203 words
    - [HIGH_LENGTH] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — user_msg 201 words

### G3-11: Substitution rule

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(let [a 7] (+ a a))` — user_msg 201 words

### G3-12: Scope vs namespace

- examples: 1
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 2}
    - [HIGH_LENGTH] form=`(do (def g 5) (let [g 99] (+ g 1)))` — user_msg 216 words
    - [HIGH_LENGTH] form=`(do (def g 5) (let [g 99] (+ g 1)))` — user_msg 215 words

### G3-13: fn body returns last form

- examples: 1
- variety @ n=50: 0.96
- issues: {'HIGH_LENGTH': 2}
    - [HIGH_LENGTH] form=`((fn [x] x x x 99) 1)` — user_msg 201 words
    - [HIGH_LENGTH] form=`((fn [x] x x x 99) 1)` — user_msg 206 words

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

## Grade 7

### G7-13: line-seq

- examples: 2
- variety @ n=50: 0.99
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(first (clojure.string/split-lines "first\nsecond"` — answer string 'first' appears in user_msg

## Grade 8

### G8-03: defrecord introduction

- examples: 2
- variety @ n=50: 0.95
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(do (defrecord Runner [name pace]) (:name (->Runne` — answer string 'Bob' appears in user_msg

### G8-13: this-style vs fn-style

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 2, 'ANSWER_LEAK_STRING': 2}
    - [HIGH_LENGTH] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg 205 words
    - [ANSWER_LEAK_STRING] form=`(do (defprotocol Named (name-of [this])) (defrecor` — answer string 'Zephyr' appears in user_msg
    - [HIGH_LENGTH] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg 210 words
    - [ANSWER_LEAK_STRING] form=`(do (defprotocol Named (name-of [this])) (defrecor` — answer string 'Zephyr' appears in user_msg

## Grade 9

## Grade 10

## Grade 11

## Grade 12

---

## Summary

### Issue counts (across all examples × 3 records)

- **HIGH_LENGTH**: 9
- **ANSWER_LEAK_STRING**: 4

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 0 | — |
| 2 | 22 | 88 | 0 | G2-16(0.94) |
| 3 | 18 | 31 | 7 | — |
| 4 | 20 | 39 | 0 | G4-16(0.94) |
| 5 | 22 | 39 | 0 | G5-08(0.94); G5-16(0.93) |
| 6 | 16 | 33 | 0 | — |
| 7 | 18 | 36 | 1 | — |
| 8 | 16 | 31 | 5 | — |
| 9 | 18 | 34 | 0 | — |
| 10 | 16 | 36 | 0 | — |
| 11 | 14 | 29 | 0 | — |
| 12 | 18 | 37 | 0 | — |

### Sample issues by severity

#### HIGH_LENGTH

- `G3-09` (form `(do (defn dbl [x] (* x 2)) (dbl 5))`): user_msg 203 words
    ```
    A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened at the edge of the village.

Caw carved the name dbl into the pitcher's rim at the market, then scratched the recipe beneath it: accept x, serve twice x. The name and the recipe were pressed togeth...
    ```
- `G3-09` (form `(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))`): user_msg 201 words
    ```
    A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Sable pressed the name add3 into the village pitcher's rim alongside a three-slot recipe: accept a, b, and c, then sum them. The carving was deep and permanent, ready to be called whenever three counts needed...
    ```
- `G3-11` (form `(let [a 7] (+ a a))`): user_msg 201 words
    ```
    Hunger and thirst had driven the Crow far from her usual perch. All this took place at the edge of the hilltop.

Sable tucked seven stones under one wing at the hilltop pitcher, naming the count a. Then, without adding more stones, Sable referenced a twice — as if the same tucked bundle could be dra...
    ```
- `G3-12` (form `(do (def g 5) (let [g 99] (+ g 1)))`): user_msg 216 words
    ```
    It is said that wit, more than strength, is the friend of the thirsty Crow. This was near the meadow.

Caw carved g into the orchard pitcher's rim and filled the groove with five. Then she tucked a very different count under her wing — ninety-nine — and also named it g, a shadow hiding the rim groov...
    ```
- `G3-12` (form `(do (def g 5) (let [g 99] (+ g 1)))`): user_msg 215 words
    ```
    Hunger and thirst had driven the Crow far from her usual perch. All this took place by the market.

Caw carved g into the orchard pitcher's rim and filled the groove with five. Then she tucked a very different count under her wing — ninety-nine — and also named it g, a shadow hiding the rim groove w...
    ```

#### ANSWER_LEAK_STRING

- `G7-13` (form `(first (clojure.string/split-lines "first\nsecond"))`): answer string 'first' appears in user_msg
    ```
    It is said that wit, more than strength, is the friend of the thirsty Crow. This was by the orchard.

Caw unrolled a two-row scroll at the meadow pitcher. She split it at the newline groove and reached for only the topmost row-pebble, ignoring the rest.

She needed only the first row lifted from the...
    ```
- `G8-03` (form `(do (defrecord Runner [name pace]) (:name (->Runner "Bob" :m`): answer string 'Bob' appears in user_msg
    ```
    It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place near the road.

Korvus stitched a Runner pouch on the pitcher's rim at the market with two slots: name and pace. He packed a new instance — name='Bob', pace=:moderate — and reached for the name slot.

He ...
    ```
- `G8-13` (form `(do (defprotocol Named (name-of [this])) (defrecord Hare [n]`): answer string 'Zephyr' appears in user_msg
    ```
    It is said that wit, more than strength, is the friend of the thirsty Crow.

Caw posted the Named guild charter on the pitcher's rim at the garden. She wove a Hare pouch with an 'n' slot that pledged the guild — its method reaching into the pouch via `this` to read the n slot. She packed 'Zephyr' an...
    ```
- `G8-13` (form `(do (defprotocol Named (name-of [this])) (defrecord Hare [n]`): answer string 'Zephyr' appears in user_msg
    ```
    It is said that wit, more than strength, is the friend of the thirsty Crow. It happened in the garden.

Caw posted the Named guild charter on the pitcher's rim at the garden. She wove a Hare pouch with an 'n' slot that pledged the guild — its method reaching into the pouch via `this` to read the n s...
    ```

