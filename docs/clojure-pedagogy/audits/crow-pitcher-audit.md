# crow-pitcher curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

## Grade 2

## Grade 3

### G3-18: When to name vs inline

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'FORM_LEAK': 1}
    - [HIGH_LENGTH] form=`(let [n 5] (* n n n))` — user_msg 203 words
    - [FORM_LEAK] form=`(* 5 5 5)` — form '(* 5 5 5)' appears in user_msg of a goal-style subject

## Grade 4

## Grade 5

### G5-22: recur — first taste

- examples: 1
- variety @ n=50: 0.98
- issues: {'ANSWER_LEAK': 2, 'BAD_PLACE_PREP': 2}
    - [ANSWER_LEAK] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — answer 120 in narrative
    - [BAD_PLACE_PREP] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — 'in the hilltop' (wrong preposition)
    - [ANSWER_LEAK] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — answer 120 in narrative
    - [BAD_PLACE_PREP] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — 'in the hilltop' (wrong preposition)

## Grade 6

### G6-01: Namespace as file

- examples: 3
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(name 'foo.bar)` — answer string 'foo.bar' appears in user_msg

## Grade 7

### G7-11: Reading stack traces

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(try (throw (ex-info "trouble" {})) (catch Excepti` — answer string 'trouble' appears in user_msg

## Grade 8

### G8-03: defrecord introduction

- examples: 2
- variety @ n=50: 0.99
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — answer string ':slow' appears in user_msg

## Grade 9

### G9-07: Ref introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_PREP': 1}
    - [DOUBLE_PREP] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — verb+preposition followed by {place} which already carries its own preposition

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_PREP': 2}
    - [DOUBLE_PREP] form=`(do (def lock (Object.)) (locking lock 42))` — verb+preposition followed by {place} which already carries its own preposition
    - [DOUBLE_PREP] form=`(do (def lock (Object.)) (locking lock 42))` — verb+preposition followed by {place} which already carries its own preposition

## Grade 10

### G10-03: defmacro introduction

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg 221 words

## Grade 11

### G11-06: new and dot-construct

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(new String "jump")` — answer string 'jump' appears in user_msg

## Grade 12

### G12-03: into with a transducer (xform)

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(into #{} (map inc) [1 2 3])` — user_msg 206 words

---

## Summary

### Issue counts (across all examples × 3 records)

- **ANSWER_LEAK_STRING**: 4
- **HIGH_LENGTH**: 3
- **DOUBLE_PREP**: 3
- **ANSWER_LEAK**: 2
- **BAD_PLACE_PREP**: 2
- **FORM_LEAK**: 1

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 0 | — |
| 2 | 22 | 88 | 0 | — |
| 3 | 18 | 31 | 2 | — |
| 4 | 20 | 39 | 0 | — |
| 5 | 22 | 39 | 4 | — |
| 6 | 16 | 33 | 1 | — |
| 7 | 18 | 36 | 1 | — |
| 8 | 16 | 31 | 1 | — |
| 9 | 18 | 34 | 3 | — |
| 10 | 16 | 36 | 1 | — |
| 11 | 14 | 29 | 1 | — |
| 12 | 18 | 37 | 1 | — |

### Sample issues by severity

#### HIGH_LENGTH

- `G3-18` (form `(let [n 5] (* n n n))`): user_msg 203 words
    ```
    Mantle the crow alighted on the rim of a jar at the edge of the orchard and peered down at the small dark gleam below.

Sable tucked five stones under one wing at the village pitcher, naming the count n, then used that one tucked count three times in the body — multiplying n by itself twice over wit...
    ```
- `G10-03` (form `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-w`): user_msg 221 words
    ```
    Vane circled twice at the farm before settling on the rim of the old clay jar, eyes on the water below.

Caw scratched a master revision rule on the pitcher's rim at the village: `my-when` — whenever this pattern appeared in a form, the talon would rewrite it before the REPL ever saw the body. The r...
    ```
- `G12-03` (form `(into #{} (map inc) [1 2 3])`): user_msg 206 words
    ```
    Vane circled twice at the farm before settling on the rim of the old clay jar, eyes on the water below.

Caw stood at the village sorting-perch with the increment groove, but this time the receiving pile below was a set — a heap that keeps only unique stones. Three stones waited in line to pass thro...
    ```

#### FORM_LEAK

- `G3-18` (form `(* 5 5 5)`): form '(* 5 5 5)' appears in user_msg of a goal-style subject
    ```
    near the village, where the orchard meets the well, an old clay pitcher had stood for as long as anyone could remember.

Korvus dropped three literal stone-counts of five into the garden pitcher all at once — no wing tucked, no name carved — just three fives fed directly to the multiplication as pla...
    ```

#### ANSWER_LEAK

- `G5-22` (form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n)`): answer 120 in narrative
    ```
    near the village, where the heat shimmered above the stones, Buffet the crow began the slow business of solving thirst.

Caw stood at the pitcher's rim in the hilltop field, a circuit chalked beneath her feet: start with n=5 and accumulator=1. Each lap, multiply the accumulator by n, step n down by ...
    ```
- `G5-22` (form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n)`): answer 120 in narrative
    ```
    On a long afternoon when even the bees had grown slow, a thirsty bird settled on the rim of a clay vessel.

Caw stood at the pitcher's rim in the hilltop field, a circuit chalked beneath her feet: start with n=5 and accumulator=1. Each lap, multiply the accumulator by n, step n down by one — loop wi...
    ```

#### BAD_PLACE_PREP

- `G5-22` (form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n)`): 'in the hilltop' (wrong preposition)
    ```
    near the village, where the heat shimmered above the stones, Buffet the crow began the slow business of solving thirst.

Caw stood at the pitcher's rim in the hilltop field, a circuit chalked beneath her feet: start with n=5 and accumulator=1. Each lap, multiply the accumulator by n, step n down by ...
    ```
- `G5-22` (form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n)`): 'in the hilltop' (wrong preposition)
    ```
    On a long afternoon when even the bees had grown slow, a thirsty bird settled on the rim of a clay vessel.

Caw stood at the pitcher's rim in the hilltop field, a circuit chalked beneath her feet: start with n=5 and accumulator=1. Each lap, multiply the accumulator by n, step n down by one — loop wi...
    ```

#### ANSWER_LEAK_STRING

- `G6-01` (form `(name 'foo.bar)`): answer string 'foo.bar' appears in user_msg
    ```
    In a year when the wells ran low, a single jar of water was a small kingdom unto itself.

Korvus perched at the pitcher's clay rim in the garden and studied the name carved into the side: a dotted path, two segments pressed into the clay. He wanted to read it as a plain string, not a symbol.

He nee...
    ```
- `G7-11` (form `(try (throw (ex-info "trouble" {})) (catch Exception e (.get`): answer string 'trouble' appears in user_msg
    ```
    A row of pebbles lay at the foot of the wall, sun-warmed, unremarkable, and just heavy enough.

Onyxwing the crow spread a patch of soft moss beneath the pitcher on the market.
"If a stone goes wrong — if the form fails — the moss catches it safely,"
he said. "The pitcher's water level doesn't drop;...
    ```
- `G8-03` (form `(do (defrecord Runner [name pace]) (:pace (->Runner "Alice" `): answer string ':slow' appears in user_msg
    ```
    Vane circled twice at the farm before settling on the rim of the old clay jar, eyes on the water below.

Caw wove a bark-and-vine carrying-pouch with two named slots: one for a name-stone, one for a pace-stone. She stitched the shape onto the rim once, then packed an instance: name='Alice', pace=:sl...
    ```
- `G11-06` (form `(new String "jump")`): answer string 'jump' appears in user_msg
    ```
    The kitchen garden had been lovingly kept, but the sun that year had been merciless and constant.

Korvus tried the same potter's mold at the meadow but wrote the inscription differently — using the `new` keyword before the class name, pressing 'jump' into the wet clay.

He wanted to confirm `new` w...
    ```

#### DOUBLE_PREP

- `G9-07` (form `(do (def r (ref 0)) (dosync (alter r inc)) @r)`): verb+preposition followed by {place} which already carries its own preposition
    ```
    Witty circled twice near the hilltop before settling on the rim of the old clay jar, eyes on the water below.

Caw placed a zero-mark in a sealed safe-box beside the pitcher at the garden. To change the mark she had to open the safe-box in one atomic transaction, nudge the tally up by one, and seal ...
    ```
- `G9-18` (form `(do (def lock (Object.)) (locking lock 42))`): verb+preposition followed by {place} which already carries its own preposition
    ```
    Cluck the crow was no fool, and at the edge of the garden the day demanded thinking rather than complaining.

Korvus planted a gate-stone at the pitcher's mouth on the road. He rolled it aside, placed a single stone tally inside the sealed section, then rolled the gate back — the tally was the body'...
    ```
- `G9-18` (form `(do (def lock (Object.)) (locking lock 42))`): verb+preposition followed by {place} which already carries its own preposition
    ```
    Coal the crow arrived at the farm with no plan but a sharp eye and a willingness to take small steps.

Korvus planted a gate-stone at the pitcher's mouth on the road. He rolled it aside, placed a single stone tally inside the sealed section, then rolled the gate back — the tally was the body's only ...
    ```

