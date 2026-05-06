# dog-shadow curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

## Grade 2

### G2-20: Counting

- examples: 3
- variety @ n=50: 0.95

## Grade 3

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 2}
    - [HIGH_LENGTH] form=`(#(+ % 1) 5)` — user_msg 220 words
    - [HIGH_LENGTH] form=`(#(+ % 1) 5)` — user_msg 220 words

### G3-11: Substitution rule

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 2}
    - [HIGH_LENGTH] form=`(let [a 7] (+ a a))` — user_msg 216 words
    - [HIGH_LENGTH] form=`(let [a 7] (+ a a))` — user_msg 204 words

### G3-14: do form

- examples: 2
- variety @ n=50: 0.97
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (+ 1 1) (+ 2 2) (+ 3 3))` — user_msg 203 words

### G3-17: Naming conventions (kebab-case)

- examples: 1
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(let [hare-speed 4 tortoise-speed 1] (- hare-speed` — user_msg 222 words

## Grade 4

## Grade 5

### G5-04: cond

- examples: 1
- variety @ n=50: 0.96
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — user_msg 233 words

### G5-05: cond — :else

- examples: 1
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(cond false :a false :b :else :c)` — user_msg 213 words

## Grade 6

## Grade 7

## Grade 8

### G8-05: Protocol extension

- examples: 2
- variety @ n=50: 0.97
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — user_msg 209 words

### G8-07: Record implementing protocol

- examples: 2
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defprotocol Pace (speed [this])) (defrecord T` — user_msg 204 words

### G8-13: this-style vs fn-style

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defprotocol Tagged (tag-of [this])) (defrecor` — user_msg 248 words

### G8-16: Abstract design with protocols

- examples: 2
- variety @ n=50: 0.96
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defprotocol Sound (cry [this])) (defrecord Ha` — user_msg 206 words

## Grade 9

### G9-01: Immutability as default — review

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(let [v [1 2 3]] (conj v 4) v)` — user_msg 233 words

### G9-04: Atom CAS semantics

- examples: 2
- variety @ n=50: 0.97
- issues: {'HIGH_LENGTH': 2}
    - [HIGH_LENGTH] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — user_msg 228 words
    - [HIGH_LENGTH] form=`(do (def a (atom 5)) (compare-and-set! a 0 99) @a)` — user_msg 219 words

### G9-05: Watch on atom

- examples: 1
- variety @ n=50: 0.94
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — user_msg 252 words

### G9-08: dosync and alter

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — user_msg 233 words

### G9-13: future introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`@(future (* 6 7))` — user_msg 204 words

### G9-14: deref @ shorthand

- examples: 2
- variety @ n=50: 0.97
- issues: {'HIGH_LENGTH': 2}
    - [HIGH_LENGTH] form=`(do (def a (atom 7)) (deref a))` — user_msg 229 words
    - [HIGH_LENGTH] form=`(do (def a (atom 7)) (deref a))` — user_msg 234 words

### G9-15: promise — deliver and deref

- examples: 2
- variety @ n=50: 0.97
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (def p (promise)) (deliver p 42) @p)` — user_msg 213 words

### G9-16: volatile — when STM is too heavy

- examples: 2
- variety @ n=50: 0.95
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (def v (volatile! 5)) (vreset! v 99) @v)` — user_msg 212 words

### G9-17: binding — thread-local

- examples: 2
- variety @ n=50: 0.97
- issues: {'HIGH_LENGTH': 2}
    - [HIGH_LENGTH] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — user_msg 236 words
    - [HIGH_LENGTH] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *` — user_msg 244 words

## Grade 10

## Grade 11

### G11-02: Method call syntax

- examples: 3
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(. "abc" toUpperCase)` — user_msg 220 words

### G11-08: Type hints

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(let [^String s "abc"] (.toUpperCase s))` — user_msg 220 words

### G11-14: Debugging host leaks

- examples: 2
- variety @ n=50: 0.97
- issues: {'HIGH_LENGTH': 2}
    - [HIGH_LENGTH] form=`(try (Math/sqrt 4) (catch Exception _ :err))` — user_msg 227 words
    - [HIGH_LENGTH] form=`(try (Math/sqrt 4) (catch Exception _ :err))` — user_msg 232 words

## Grade 12

---

## Summary

### Issue counts (across all examples × 3 records)

- **HIGH_LENGTH**: 28

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 0 | — |
| 2 | 22 | 88 | 0 | G2-20(0.95) |
| 3 | 18 | 31 | 6 | — |
| 4 | 20 | 39 | 0 | — |
| 5 | 22 | 39 | 2 | — |
| 6 | 16 | 33 | 0 | — |
| 7 | 18 | 36 | 0 | — |
| 8 | 16 | 31 | 4 | — |
| 9 | 18 | 34 | 12 | G9-05(0.94) |
| 10 | 16 | 36 | 0 | — |
| 11 | 14 | 29 | 4 | — |
| 12 | 18 | 37 | 0 | — |

### Sample issues by severity

#### HIGH_LENGTH

- `G3-10` (form `(#(+ % 1) 5)`): user_msg 220 words
    ```
    What the Dog thought he saw beneath the water turned out to be his own reflection.

Rex the hound caught a whiff of the bank near the meadow and traced a quick, terse sniffing-path — so brief it had almost no name at all. "Add one more bone to whatever you find," the marks said. He did not carve a m...
    ```
- `G3-10` (form `(#(+ % 1) 5)`): user_msg 220 words
    ```
    Greed has cost more than one creature what they already had. It happened near the road.

Rex the hound caught a whiff of the bank near the meadow and traced a quick, terse sniffing-path — so brief it had almost no name at all. "Add one more bone to whatever you find," the marks said. He did not carv...
    ```
- `G3-11` (form `(let [a 7] (+ a a))`): user_msg 216 words
    ```
    What the Dog thought he saw beneath the water turned out to be his own reflection. All this took place by the forest.

Patch the hound held a bone at the stream's edge between his jaws — a count of 7. "I will call this grip a," he said, "and I need to know what a plus a makes. The name a means 7, so...
    ```
- `G3-11` (form `(let [a 7] (+ a a))`): user_msg 204 words
    ```
    Greed has cost more than one creature what they already had.

Patch the hound held a bone at the stream's edge between his jaws — a count of 7. "I will call this grip a," he said, "and I need to know what a plus a makes. The name a means 7, so I will add 7 to 7."

The form referenced the same name t...
    ```
- `G3-14` (form `(do (+ 1 1) (+ 2 2) (+ 3 3))`): user_msg 203 words
    ```
    What the Dog thought he saw beneath the water turned out to be his own reflection. It happened on the road.

Rex the hound left three sets of paw-prints at the stream's edge, one trail after another. "I walk each trail in turn," he said, pressing the last print deep into the stone, "and whatever the...
    ```

