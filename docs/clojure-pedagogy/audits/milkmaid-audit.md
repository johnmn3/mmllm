# milkmaid curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

## Grade 2

### G2-10: Powers via repeated multiplication

- examples: 4
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 3}
    - [ANSWER_LEAK] form=`(* 5 5)` — answer 25 in narrative
    - [ANSWER_LEAK] form=`(* 3 3 3 3)` — answer 81 in narrative
    - [ANSWER_LEAK] form=`(* 3 3 3 3)` — answer 81 in narrative

## Grade 3

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2}
    - [HIGH_LENGTH] form=`(#(+ % 1) 5)` — user_msg 219 words
    - [HIGH_LENGTH] form=`(#(* %1 %2) 3 4)` — user_msg 201 words

## Grade 4

## Grade 5

### G5-22: recur — first taste

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — user_msg 205 words

## Grade 6

## Grade 7

### G7-10: doc and source

- examples: 1
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(:doc (meta '^{:doc "adds two"} plus))` — answer string 'adds two' appears in user_msg

## Grade 8

### G8-02: deftype introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2}
    - [HIGH_LENGTH] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — user_msg 204 words
    - [HIGH_LENGTH] form=`(do (deftype Stone [weight]) (.-weight (Stone. 7))` — user_msg 209 words

### G8-05: Protocol extension

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 2}
    - [HIGH_LENGTH] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — user_msg 214 words
    - [HIGH_LENGTH] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — user_msg 212 words

### G8-09: Multimethod defmethod

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defmulti pace :species) (defmethod pace :hare` — user_msg 229 words

### G8-10: Multimethod vs protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2}
    - [HIGH_LENGTH] form=`(do (defmulti show identity) (defmethod show :rabb` — user_msg 214 words
    - [HIGH_LENGTH] form=`(do (defprotocol Show (show [this])) (extend-proto` — user_msg 223 words

### G8-12: extend-type on built-in types

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defprotocol Pace (speed [this])) (extend-type` — user_msg 217 words

## Grade 9

### G9-02: Why state at all

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2}
    - [HIGH_LENGTH] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — user_msg 206 words
    - [HIGH_LENGTH] form=`(do (def progress (atom :idle)) (reset! progress :` — user_msg 211 words

### G9-10: Agent introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2}
    - [HIGH_LENGTH] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg 211 words
    - [HIGH_LENGTH] form=`(do (def ag (agent 5)) (send ag + 10) (await ag) @` — user_msg 204 words

### G9-12: await — synchronizing on agents

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — user_msg 201 words

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_PREP': 1}
    - [DOUBLE_PREP] form=`(do (def lock (Object.)) (locking lock 42))` — verb+preposition followed by {place} which already carries its own preposition

## Grade 10

### G10-02: syntax-quote

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 2}
    - [HIGH_LENGTH] form=`(let [x 10] `(+ ~x ~x))` — user_msg 205 words
    - [HIGH_LENGTH] form=`(let [xs [1 2 3]] `(list ~@xs))` — user_msg 206 words

### G10-10: Anaphoric macros are confusing

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — user_msg 207 words

### G10-16: Macro pattern library

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — user_msg 208 words

## Grade 11

### G11-02: Method call syntax

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'FORM_LEAK': 1}
    - [HIGH_LENGTH] form=`(.toUpperCase "abc")` — user_msg 208 words
    - [FORM_LEAK] form=`(. "abc" toUpperCase)` — form '(. "abc" toUpperCase)' appears in user_msg of a goal-style subject

### G11-14: Debugging host leaks

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(try (Math/sqrt 4) (catch Exception _ :err))` — user_msg 229 words

## Grade 12

### G12-02: Transducer composition

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — user_msg 207 words

---

## Summary

### Issue counts (across all examples × 3 records)

- **HIGH_LENGTH**: 23
- **ANSWER_LEAK**: 3
- **ANSWER_LEAK_STRING**: 1
- **DOUBLE_PREP**: 1
- **FORM_LEAK**: 1

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 0 | — |
| 2 | 22 | 88 | 3 | — |
| 3 | 18 | 31 | 2 | — |
| 4 | 20 | 39 | 0 | — |
| 5 | 22 | 39 | 1 | — |
| 6 | 16 | 33 | 0 | — |
| 7 | 18 | 36 | 1 | — |
| 8 | 16 | 31 | 8 | — |
| 9 | 18 | 34 | 6 | — |
| 10 | 16 | 36 | 4 | — |
| 11 | 14 | 29 | 3 | — |
| 12 | 18 | 37 | 1 | — |

### Sample issues by severity

#### ANSWER_LEAK

- `G2-10` (form `(* 5 5)`): answer 25 in narrative
    ```
    It was at the village, on a fair-weather morning, that Ninon began the long walk to market.

The farmer had a square garden plot: 5 paces wide and 5 paces long. She needed the total area in square paces to know how much seed to sow.

She needed to multiply 5 by itself to find the area of the square ...
    ```
- `G2-10` (form `(* 3 3 3 3)`): answer 81 in narrative
    ```
    Melina was not a careless girl by nature, but on the hilltop the morning was bright and the daydreams were brighter.

The farmer had a four-dimensional arrangement of coins (a thought experiment): 3 coins in each dimension. She wondered what the total count would be if she could stack all dimensions...
    ```
- `G2-10` (form `(* 3 3 3 3)`): answer 81 in narrative
    ```
    It is an old habit to count the worth of a thing before the thing has reached the buyer.

The farmer had a four-dimensional arrangement of coins (a thought experiment): 3 coins in each dimension. She wondered what the total count would be if she could stack all dimensions at once.

She needed to mul...
    ```

#### HIGH_LENGTH

- `G3-10` (form `(#(+ % 1) 5)`): user_msg 219 words
    ```
    It was the season of new chicks and first cheeses, and every small profit felt like the start of a larger one.

The milkmaid needed a nameless pail-steps card in a hurry and scrawled it in shorthand on a scrap of cheesecloth: a percent mark for whatever count came in, plus one. She passed the scrap ...
    ```
- `G3-10` (form `(#(* %1 %2) 3 4)`): user_msg 201 words
    ```
    It was at the village, on a fair-weather morning, that Ninon began the long walk to market.

The milkmaid had scrawled a two-slot nameless card in shorthand on a scrap of cheesecloth: first-count mark, second-count mark, and a step that multiplied them. She passed the scrap to the buyer at the dairy...
    ```
- `G5-22` (form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n)`): user_msg 205 words
    ```
    A walk to market, with a full pail and a full head, is one of the oldest tests of attention there is.

The milkmaid walked the daily milking circuit: five stations along the same path, starting with a tally of 1. At each station she multiplied the running tally by the station count, then moved one s...
    ```
- `G8-02` (form `(do (deftype Pebble [color]) (.-color (Pebble. "grey")))`): user_msg 204 words
    ```
    Long before the market opened its stalls, a young woman had already spent her milk three times in her head.

The farmer designed a custom pail called Pebble — a single-slot container meant to carry one attribute, color, to market. She then hammered a Pebble pail into shape and filled the color slot....
    ```
- `G8-02` (form `(do (deftype Stone [weight]) (.-weight (Stone. 7)))`): user_msg 209 words
    ```
    Milk does not forgive a tilted head, but a dreaming mind seldom remembers as much.

The farmer had designed a pail mold called Stone — a single-slot container shaped to carry one attribute, weight, to the dairy scale. She hammered a Stone pail into shape and dropped the weight into its labeled slot....
    ```

#### ANSWER_LEAK_STRING

- `G7-10` (form `(:doc (meta '^{:doc "adds two"} plus))`): answer string 'adds two' appears in user_msg
    ```
    It was the season of new chicks and first cheeses, and every small profit felt like the start of a larger one.

Clara found an old scroll marking the symbol 'plus' with notes written in the margins: 'adds two'.

She wanted to read the attached documentation note. What words were written in those mar...
    ```

#### DOUBLE_PREP

- `G9-18` (form `(do (def lock (Object.)) (locking lock 42))`): verb+preposition followed by {place} which already carries its own preposition
    ```
    The cows had given generously that dawn, and the pail was heavier than usual, and the imagination was heavier still.

The farmer showed the milkmaid the simplest possible padlocked section: just a plain value inside the lock. The padlock was real — it acquired the monitor — but the body needed no co...
    ```

#### FORM_LEAK

- `G11-02` (form `(. "abc" toUpperCase)`): form '(. "abc" toUpperCase)' appears in user_msg of a goal-style subject
    ```
    The pail sat steady on Lena's head as she started down the lane at the market.

The milkmaid had another string 'abc' and wished to borrow the same neighbor's tool — toUpperCase — but this time using the alternate dot form, which places the object before the method name.

She needed to learn that th...
    ```

