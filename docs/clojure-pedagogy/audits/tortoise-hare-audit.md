# tortoise-hare curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

## Grade 2

### G2-02: Comparison chains

- examples: 5
- variety @ n=50: 1.00
- issues: {'SAID_PARTICIPLE': 1}
    - [SAID_PARTICIPLE] form=`(<= 1 1 2)` — 'declared puffed' (missing comma after speech-verb)

### G2-03: not= and = with multiple args

- examples: 5
- variety @ n=50: 1.00
- issues: {'SAID_PARTICIPLE': 2}
    - [SAID_PARTICIPLE] form=`(not= 1 1)` — 'declared boasting' (missing comma after speech-verb)
    - [SAID_PARTICIPLE] form=`(not= 1 1 2)` — 'declared boasting' (missing comma after speech-verb)

### G2-04: min and max

- examples: 5
- variety @ n=50: 1.00
- issues: {'SAID_PARTICIPLE': 1}
    - [SAID_PARTICIPLE] form=`(max 1 2 3)` — 'declared swaggering' (missing comma after speech-verb)

### G2-05: quot, rem, mod

- examples: 6
- variety @ n=50: 1.00
- issues: {'SAID_PARTICIPLE': 1}
    - [SAID_PARTICIPLE] form=`(mod -7 3)` — 'declared with a smug grin' (missing comma after speech-verb)

### G2-06: inc and dec

- examples: 5
- variety @ n=50: 1.00
- issues: {'SAID_PARTICIPLE': 1}
    - [SAID_PARTICIPLE] form=`(inc 0)` — 'declared with a smug grin' (missing comma after speech-verb)

### G2-07: Absolute value

- examples: 4
- variety @ n=50: 1.00
- issues: {'SAID_PARTICIPLE': 1}
    - [SAID_PARTICIPLE] form=`(abs 5)` — 'declared boasting' (missing comma after speech-verb)

### G2-08: Arithmetic on ratios

- examples: 3
- variety @ n=50: 1.00
- issues: {'SAID_PARTICIPLE': 2}
    - [SAID_PARTICIPLE] form=`(* 2/3 3/4)` — 'declared boasting' (missing comma after speech-verb)
    - [SAID_PARTICIPLE] form=`(- 1 1/3)` — 'declared boasting' (missing comma after speech-verb)

### G2-09: Floats vs ints (the / operator)

- examples: 3
- variety @ n=50: 1.00
- issues: {'SAID_PARTICIPLE': 1}
    - [SAID_PARTICIPLE] form=`(/ 10 2)` — 'declared puffed' (missing comma after speech-verb)

### G2-11: String concatenation with str

- examples: 4
- variety @ n=50: 1.00
- issues: {'SAID_PARTICIPLE': 1}
    - [SAID_PARTICIPLE] form=`(str "tor" "toise")` — 'declared puffed' (missing comma after speech-verb)

### G2-13: and / or — short circuit, return values

- examples: 6
- variety @ n=50: 1.00
- issues: {'SAID_PARTICIPLE': 4}
    - [SAID_PARTICIPLE] form=`(and true false)` — 'declared boasting' (missing comma after speech-verb)
    - [SAID_PARTICIPLE] form=`(or false false)` — 'declared swaggering' (missing comma after speech-verb)
    - [SAID_PARTICIPLE] form=`(and 1 2 3)` — 'declared puffed' (missing comma after speech-verb)
    - [SAID_PARTICIPLE] form=`(and 1 2 3)` — 'declared boasting' (missing comma after speech-verb)

### G2-14: not — turning truthy to false

- examples: 5
- variety @ n=50: 1.00
- issues: {'SAID_PARTICIPLE': 1}
    - [SAID_PARTICIPLE] form=`(not false)` — 'declared puffed' (missing comma after speech-verb)

### G2-15: Falsey values: only false and nil

- examples: 4
- variety @ n=50: 1.00
- issues: {'SAID_PARTICIPLE': 1}
    - [SAID_PARTICIPLE] form=`(if false :truthy :falsey)` — 'declared boasting' (missing comma after speech-verb)

### G2-17: Keyword as function for map lookup

- examples: 3
- variety @ n=50: 1.00
- issues: {'SAID_PARTICIPLE': 1}
    - [SAID_PARTICIPLE] form=`(:tortoise {:hare 1 :tortoise 2})` — 'declared swaggering' (missing comma after speech-verb)

### G2-21: String length and substring

- examples: 3
- variety @ n=50: 1.00
- issues: {'SAID_PARTICIPLE': 1}
    - [SAID_PARTICIPLE] form=`(count "hare")` — 'declared puffed' (missing comma after speech-verb)

## Grade 3

## Grade 4

## Grade 5

## Grade 6

## Grade 7

## Grade 8

## Grade 9

## Grade 10

## Grade 11

## Grade 12

### G12-16: Reagent (cljs UI brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_FROM': 2}
    - [DOUBLE_FROM] form=`(do "Reagent wraps React with Hiccup-shaped Clojur` — EMO_TIRED tail duplicates an already-terminated prep phrase (e.g., 'from sprinting from a recent sprint', 'her legs heavy from sprinting of the lecture', 'weary from the morning's effort from a season of song')
    - [DOUBLE_FROM] form=`(do "components are functions returning Hiccup vec` — EMO_TIRED tail duplicates an already-terminated prep phrase (e.g., 'from sprinting from a recent sprint', 'her legs heavy from sprinting of the lecture', 'weary from the morning's effort from a season of song')

---

## Summary

### Issue counts (across all examples × 3 records)

- **SAID_PARTICIPLE**: 19
- **DOUBLE_FROM**: 2

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 80 | 0 | — |
| 2 | 22 | 88 | 19 | — |
| 3 | 18 | 31 | 0 | — |
| 4 | 20 | 39 | 0 | — |
| 5 | 22 | 39 | 0 | — |
| 6 | 16 | 33 | 0 | — |
| 7 | 18 | 36 | 0 | — |
| 8 | 16 | 31 | 0 | — |
| 9 | 18 | 34 | 0 | — |
| 10 | 16 | 36 | 0 | — |
| 11 | 14 | 29 | 0 | — |
| 12 | 18 | 37 | 2 | — |

### Sample issues by severity

#### SAID_PARTICIPLE

- `G2-02` (form `(<= 1 1 2)`): 'declared puffed' (missing comma after speech-verb)
    ```
    It was well known among the animals that the Hare boasted of his speed at every chance.

"Whatever `(<= 1 1 2)` comes to," Pip the hare declared puffed up with pride
on the road, "I'll wager I know it without typing it." Slowpoke the tortoise,
saying very little, picked up a stick and drew the chain...
    ```
- `G2-03` (form `(not= 1 1)`): 'declared boasting' (missing comma after speech-verb)
    ```
    It was well known among the animals that the Hare boasted of his speed at every chance.

"Whatever `(not= 1 1)` comes to," Hopper the hare declared boasting at every turn
at the edge of the hilltop, "I'll wager I know it without typing it." Shelly the tortoise,
her eyes always on the path, picked up...
    ```
- `G2-03` (form `(not= 1 1 2)`): 'declared boasting' (missing comma after speech-verb)
    ```
    The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

"Whatever `(not= 1 1 2)` comes to," Pip the hare declared boasting at every turn
in the forest, "I'll wager I know it without typing it." Shelly the tortoise,
her eyes always on the path, pick...
    ```
- `G2-04` (form `(max 1 2 3)`): 'declared swaggering' (missing comma after speech-verb)
    ```
    The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. This was in the forest.

"Whatever `(max 1 2 3)` comes to," Hopper the hare declared swaggering through the underbrush
at the edge of the forest, "I'll wager I know it without typing it." Mossb...
    ```
- `G2-05` (form `(mod -7 3)`): 'declared with a smug grin' (missing comma after speech-verb)
    ```
    It was well known among the animals that the Hare boasted of his speed at every chance. All this took place at the edge of the hilltop.

"Whatever `(mod -7 3)` comes to," Bramble the hare declared with a smug grin
at the edge of the hilltop, "I'll wager I know it without typing it." Slowpoke the tor...
    ```

#### DOUBLE_FROM

- `G12-16` (form `(do "Reagent wraps React with Hiccup-shaped Clojure data" :s`): EMO_TIRED tail duplicates an already-terminated prep phrase (e.g., 'from sprinting from a recent sprint', 'her legs heavy from sprinting of the lecture', 'weary from the morning's effort from a season of song')
    ```
    There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. This was along the road.

Whisker the hare, yawning at the soft moss from a season of races, was finally willing
to study patterns. Mossback the tortoise pointed on the road at
the Reagent wrapp...
    ```
- `G12-16` (form `(do "components are functions returning Hiccup vectors" :rea`): EMO_TIRED tail duplicates an already-terminated prep phrase (e.g., 'from sprinting from a recent sprint', 'her legs heavy from sprinting of the lecture', 'weary from the morning's effort from a season of song')
    ```
    It was well known among the animals that the Hare boasted of his speed at every chance.

Whisker the hare, her legs heavy from sprinting from a season of races, was finally willing
to study patterns. Slowpoke the tortoise pointed at the edge of the garden at
how Reagent components are written. The f...
    ```

