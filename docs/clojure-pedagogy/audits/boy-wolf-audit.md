# boy-wolf curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

### G1-13: First arithmetic call

- examples: 6
- variety @ n=50: 1.00
- issues: {'FORM_LEAK': 1}
    - [FORM_LEAK] form=`(+ 7 8)` — form '(+ 7 8)' appears in user_msg of a goal-style subject

## Grade 2

### G2-10: Powers via repeated multiplication

- examples: 4
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 2}
    - [ANSWER_LEAK] form=`(* 2 2 2)` — answer 8 in narrative
    - [ANSWER_LEAK] form=`(* 2 2 2)` — answer 8 in narrative

## Grade 3

### G3-03: let — local binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'ANSWER_LEAK': 2}
    - [HIGH_LENGTH] form=`(let [x 3] (+ x 1))` — user_msg 229 words
    - [ANSWER_LEAK] form=`(let [n 10] (* n n))` — answer 100 in narrative
    - [ANSWER_LEAK] form=`(let [n 10] (* n n))` — answer 100 in narrative

### G3-06: let — binding can reference prior

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1}
    - [ANSWER_LEAK] form=`(let [a 5 b (* a 2)] b)` — answer 10 in narrative

### G3-07: fn — anonymous function

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`((fn [x] (+ x 1)) 4)` — user_msg 223 words

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1}
    - [ANSWER_LEAK] form=`(#(+ % 1) 5)` — answer 6 in narrative

### G3-13: fn body returns last form

- examples: 1
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`((fn [x] x x x 99) 1)` — user_msg 201 words

## Grade 4

## Grade 5

## Grade 6

### G6-01: Namespace as file

- examples: 3
- variety @ n=50: 0.99
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(name 'foo.bar)` — answer string 'foo.bar' appears in user_msg

## Grade 7

### G7-10: doc and source

- examples: 1
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(:doc (meta '^{:doc "adds two"} plus))` — answer string 'adds two' appears in user_msg

## Grade 8

### G8-01: Why polymorphism

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(defn speak [k] (cond (= k :wolf) "howl" (= k :flo` — user_msg 208 words

### G8-05: Protocol extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — answer string ':number' appears in user_msg

## Grade 9

### G9-07: Ref introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg 218 words

### G9-10: Agent introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg 212 words

## Grade 10

### G10-10: Anaphoric macros are confusing

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'ANSWER_LEAK': 1}
    - [HIGH_LENGTH] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — user_msg 206 words
    - [ANSWER_LEAK] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — answer 10 in narrative

## Grade 11

### G11-02: Method call syntax

- examples: 8
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'ANSWER_LEAK_STRING': 2}
    - [HIGH_LENGTH] form=`(. "abc" toUpperCase)` — user_msg 201 words
    - [ANSWER_LEAK_STRING] form=`(. "abc" toUpperCase)` — answer string 'ABC' appears in user_msg
    - [HIGH_LENGTH] form=`(. "abc" toUpperCase)` — user_msg 201 words
    - [ANSWER_LEAK_STRING] form=`(. "abc" toUpperCase)` — answer string 'ABC' appears in user_msg

## Grade 12

### G12-01: Transducers introduction

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(into [] (map inc) [1 2 3])` — user_msg 218 words

### G12-03: into with a transducer (xform)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(into #{} (map inc) [1 2 3])` — user_msg 213 words

---

## Summary

### Issue counts (across all examples × 3 records)

- **HIGH_LENGTH**: 11
- **ANSWER_LEAK**: 7
- **ANSWER_LEAK_STRING**: 5
- **FORM_LEAK**: 1

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 80 | 1 | — |
| 2 | 22 | 88 | 2 | — |
| 3 | 18 | 31 | 7 | — |
| 4 | 20 | 39 | 0 | — |
| 5 | 22 | 39 | 0 | — |
| 6 | 16 | 33 | 1 | — |
| 7 | 18 | 36 | 1 | — |
| 8 | 16 | 31 | 2 | — |
| 9 | 18 | 34 | 2 | — |
| 10 | 16 | 36 | 2 | — |
| 11 | 14 | 58 | 4 | — |
| 12 | 18 | 37 | 2 | — |

### Sample issues by severity

#### FORM_LEAK

- `G1-13` (form `(+ 7 8)`): form '(+ 7 8)' appears in user_msg of a goal-style subject
    ```
    Paola had been told the rules plainly: cry only when the wolf is real, and never when she is bored.

At dawn, Tom had brought lambs back from the south pasture and Carol had brought lambs from the north. They stood at the fold counting together, the village's morning record waiting on them.

The com...
    ```

#### ANSWER_LEAK

- `G2-10` (form `(* 2 2 2)`): answer 8 in narrative
    ```
    The hilltop offered a fine view of both the flock and the road below, where help would have to come from.

Carol stacked boxes in a cube pattern: 2 boxes deep, 2 boxes wide, 2 boxes tall. She wanted to know the total volume.

The cube volume required multiplying 2 three times. Tom estimated; Carol d...
    ```
- `G2-10` (form `(* 2 2 2)`): answer 8 in narrative
    ```
    Maarten had been told the rules plainly: cry only when the wolf is real, and never when he is bored.

Carol stacked boxes in a cube pattern: 2 boxes deep, 2 boxes wide, 2 boxes tall. She wanted to know the total volume.

The cube volume required multiplying 2 three times. Tom estimated; Carol drew t...
    ```
- `G3-03` (form `(let [n 10] (* n n))`): answer 100 in narrative
    ```
    Grainne was a clever boy, and by the meadow cleverness had begun to look very much like trouble.

Tom had just counted 10 stones for a marker wall, and he wanted to know how many stones would fill a perfect square patch. He reached for a tally-token and turned to Carol.

The square count was needed ...
    ```
- `G3-03` (form `(let [n 10] (* n n))`): answer 100 in narrative
    ```
    On those slopes, trust was a thing the village extended freely, and a thing it could not afford to lose.

Tom had just counted 10 stones for a marker wall, and he wanted to know how many stones would fill a perfect square patch. He reached for a tally-token and turned to Carol.

The square count was...
    ```
- `G3-06` (form `(let [a 5 b (* a 2)] b)`): answer 10 in narrative
    ```
    An empty hour can sometimes be filled with mischief, and mischief once started has a way of escalating.

Carol had counted 5 morning lambs in the upper pasture. Tom asked: what if we double that count for the afternoon fold calculations?

Tom needed the doubled count for one specific task, but that ...
    ```

#### HIGH_LENGTH

- `G3-03` (form `(let [x 3] (+ x 1))`): user_msg 229 words
    ```
    The hilltop offered a fine view of both the flock and the road below, where help would have to come from.

Carol the elder had been counting along a stretch of fence-line at dawn. She slipped a tally-token worth 3 lambs into the small leather belt-pouch at her hip and gave the pouch's contents the l...
    ```
- `G3-07` (form `((fn [x] (+ x 1)) 4)`): user_msg 223 words
    ```
    It happened at the edge of the orchard, on a hill where shouting carries far and trust carries further, until it doesn't.

On the watchhouse wall, Carol the elder had pinned a small drill-card with no name at the top — just the steps for what to do once an unnamed quantity arrived. Tom waited beside...
    ```
- `G3-13` (form `((fn [x] x x x 99) 1)`): user_msg 201 words
    ```
    On those slopes, trust was a thing the village extended freely, and a thing it could not afford to lose.

Carol had written a drill-card with three steps: read x, read x again, read x a third time. But then she realized the final step should return 99 instead.

Tom asked: if the drill-card lists man...
    ```
- `G8-01` (form `(defn speak [k] (cond (= k :wolf) "howl" (= k :flock) "bleat`): user_msg 208 words
    ```
    On a hill above the village, a boy watched sheep, and the sheep watched the grass, and the day moved slowly.

Carol had called a meeting of the shepherds' fellowship on the village green — sheep-shepherd, goat-shepherd, geese-keeper, all gathered. Each kind of keeper had their own way of raising an ...
    ```
- `G9-07` (form `(do (def r (ref 0)) (dosync (alter r inc)) @r)`): user_msg 218 words
    ```
    It happened at the edge of the orchard, on a hill where shouting carries far and trust carries further, until it doesn't.

Carol led Tom into the watchhouse vault, where the ledger lay under lock. 'This record is precious,' she said. 'You cannot touch it alone. We enter together, I read the page, yo...
    ```

#### ANSWER_LEAK_STRING

- `G6-01` (form `(name 'foo.bar)`): answer string 'foo.bar' appears in user_msg
    ```
    On a hill above the village, a boy watched sheep, and the sheep watched the grass, and the day moved slowly.

Tom stood at the village notice-post, where scrolls hung labeled with dotted names. Carol showed him the scroll marked `foo.bar`—a namespace written as a symbol.

Tom wanted to know what the...
    ```
- `G7-10` (form `(:doc (meta '^{:doc "adds two"} plus))`): answer string 'adds two' appears in user_msg
    ```
    The hilltop offered a fine view of both the flock and the road below, where help would have to come from.

Carol carved a drill-card on the watchhouse wall. Above the recipe's steps, she chalked a small note: "adds two". Tom asked what the note was for. Carol opened the metadata.

Every drill-card n...
    ```
- `G8-05` (form `(do (defprotocol Greet (hail [this])) (extend-protocol Greet`): answer string ':number' appears in user_msg
    ```
    The wolves of those hills were rare but not absent, and the shepherds knew it was safer to be vigilant than clever.

Carol had posted a Greet protocol at the fold-gate. A number-keeper — a tender of the tally-sticks — offered their pledge: any number greeting would return the keyword `:number`.

The...
    ```
- `G11-02` (form `(. "abc" toUpperCase)`): answer string 'ABC' appears in user_msg
    ```
    The pasture lay below a rocky lookout, and the sheep were easier to count than the hours.

Tom noticed a second way to write the same kind of tool-call, using the same dot but with the syntax stretched out: `(. object method)`. Carol explained this was the more explicit form.

Tom wanted to understa...
    ```
- `G11-02` (form `(. "abc" toUpperCase)`): answer string 'ABC' appears in user_msg
    ```
    The pasture lay below a rocky lookout, and the sheep were easier to count than the hours.

Tom noticed a second way to write the same kind of tool-call, using the same dot but with the syntax stretched out: `(. object method)`. Carol explained this was the more explicit form.

Tom wanted to understa...
    ```

