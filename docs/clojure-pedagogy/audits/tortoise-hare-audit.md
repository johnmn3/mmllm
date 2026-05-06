# tortoise-hare curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

## Grade 2

### G2-18: Quoting symbols

- examples: 3
- variety @ n=50: 0.95

## Grade 3

### G3-13: fn body returns last form

- examples: 1
- variety @ n=50: 0.94

## Grade 4

## Grade 5

### G5-09: fn as value

- examples: 1
- variety @ n=50: 0.94

## Grade 6

### G6-13: Aliasing conventions

- examples: 1
- variety @ n=50: 0.94

## Grade 7

## Grade 8

### G8-02: deftype introduction

- examples: 2
- variety @ n=50: 0.92

### G8-07: Record implementing protocol

- examples: 2
- variety @ n=50: 0.97
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — user_msg 213 words

### G8-08: Multimethod defmulti

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defmulti tag :kind) (defmethod tag :stone [_]` — user_msg 204 words

### G8-11: Protocol vs Java interface

- examples: 1
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 2}
    - [HIGH_LENGTH] form=`(do (defprotocol IPace (run [this])) (extend-proto` — user_msg 222 words
    - [HIGH_LENGTH] form=`(do (defprotocol IPace (run [this])) (extend-proto` — user_msg 215 words

### G8-13: this-style vs fn-style

- examples: 2
- variety @ n=50: 0.94
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defprotocol Tagged (tag-of [this])) (defrecor` — user_msg 217 words

### G8-14: Protocols don't inherit

- examples: 1
- variety @ n=50: 0.92

### G8-16: Abstract design with protocols

- examples: 2
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — user_msg 214 words

## Grade 9

## Grade 10

## Grade 11

## Grade 12

---

## Summary

### Issue counts (across all examples × 3 records)

- **HIGH_LENGTH**: 6

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 0 | — |
| 2 | 22 | 88 | 0 | G2-18(0.95) |
| 3 | 18 | 31 | 0 | G3-13(0.94) |
| 4 | 20 | 39 | 0 | — |
| 5 | 22 | 39 | 0 | G5-09(0.94) |
| 6 | 16 | 33 | 0 | G6-13(0.94) |
| 7 | 18 | 36 | 0 | — |
| 8 | 16 | 31 | 6 | G8-02(0.92); G8-13(0.94); G8-14(0.92) |
| 9 | 18 | 34 | 0 | — |
| 10 | 16 | 36 | 0 | — |
| 11 | 14 | 29 | 0 | — |
| 12 | 18 | 37 | 0 | — |

### Sample issues by severity

#### HIGH_LENGTH

- `G8-07` (form `(do (defprotocol Pace (speed [this])) (defrecord Hare [name]`): user_msg 213 words
    ```
    The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the faster. All this took place by the orchard.

Mossback the tortoise decided to build a labeled carrying-case for a hare runner — a `Hare` record with a `name` compartment — and have that case sign the Pa...
    ```
- `G8-08` (form `(do (defmulti tag :kind) (defmethod tag :stone [_] :hard) (t`): user_msg 204 words
    ```
    It was well known among the animals that the Hare boasted of his speed at every chance. It happened near the woods.

Pip the hare found a smooth stone on the trail and carried it to Mossback's sorting-table. The table read each item's `:kind` stamp; an arm existed only for the `:stone` stamp so far....
    ```
- `G8-11` (form `(do (defprotocol IPace (run [this])) (extend-protocol IPace `): user_msg 222 words
    ```
    The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the faster. All this took place by the forest.

Mossback the tortoise explained to Pip that the meadow had its own guild system — written entirely in Clojure — that worked like the host world's signed ledge...
    ```
- `G8-11` (form `(do (defprotocol IPace (run [this])) (extend-protocol IPace `): user_msg 215 words
    ```
    There was once a Hare whose pride matched her feet in speed, and a Tortoise who said nothing about either.

Mossback the tortoise explained to Pip that the meadow had its own guild system — written entirely in Clojure — that worked like the host world's signed ledger but without needing to enter the...
    ```
- `G8-13` (form `(do (defprotocol Tagged (tag-of [this])) (defrecord Stone [t`): user_msg 217 words
    ```
    The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the faster.

Pip the hare found a pebble and placed it in a Stone carrying-case with a single field `t` for its tag. The Tagged guild required a `tag-of` routine that read back that stored tag through `this...
    ```

