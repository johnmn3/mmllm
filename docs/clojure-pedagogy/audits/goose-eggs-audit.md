# goose-eggs curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

## Grade 2

## Grade 3

## Grade 4

## Grade 5

## Grade 6

## Grade 7

## Grade 8

### G8-07: Record implementing protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 6}
    - [WRONG_FABLE_LITERAL] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — tortoise-hare ghost name 'Pip' appears in goose-eggs user_msg
    - [WRONG_FABLE_LITERAL] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — tortoise-hare ghost name 'Pip' appears in goose-eggs user_msg
    - [WRONG_FABLE_LITERAL] form=`(do (defprotocol Pace (speed [this])) (defrecord H` — tortoise-hare ghost name 'Pip' appears in goose-eggs user_msg
    - [WRONG_FABLE_LITERAL] form=`(do (defprotocol Pace (speed [this])) (defrecord T` — tortoise-hare ghost name 'Shelly' appears in goose-eggs user_msg
    - [WRONG_FABLE_LITERAL] form=`(do (defprotocol Pace (speed [this])) (defrecord T` — tortoise-hare ghost name 'Shelly' appears in goose-eggs user_msg
    - [WRONG_FABLE_LITERAL] form=`(do (defprotocol Pace (speed [this])) (defrecord T` — tortoise-hare ghost name 'Shelly' appears in goose-eggs user_msg

### G8-13: this-style vs fn-style

- examples: 2
- variety @ n=50: 1.00
- issues: {'WRONG_FABLE_LITERAL': 3}
    - [WRONG_FABLE_LITERAL] form=`(do (defprotocol Named (name-of [this])) (defrecor` — tortoise-hare ghost name 'Pip' appears in goose-eggs user_msg
    - [WRONG_FABLE_LITERAL] form=`(do (defprotocol Named (name-of [this])) (defrecor` — tortoise-hare ghost name 'Pip' appears in goose-eggs user_msg
    - [WRONG_FABLE_LITERAL] form=`(do (defprotocol Named (name-of [this])) (defrecor` — tortoise-hare ghost name 'Pip' appears in goose-eggs user_msg

### G8-15: derive and isa? — multimethod hierarchy

- examples: 3
- variety @ n=50: 1.00
- issues: {'PREDICATE_QUESTION_COLLISION': 2}
    - [PREDICATE_QUESTION_COLLISION] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — predicate-suffix ``?`` collides with the question framing's trailing ``?`` or ``.``
    - [PREDICATE_QUESTION_COLLISION] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — predicate-suffix ``?`` collides with the question framing's trailing ``?`` or ``.``

## Grade 9

## Grade 10

## Grade 11

## Grade 12

---

## Summary

### Issue counts (across all examples × 3 records)

- **WRONG_FABLE_LITERAL**: 9
- **PREDICATE_QUESTION_COLLISION**: 2

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 80 | 0 | — |
| 2 | 22 | 88 | 0 | — |
| 3 | 18 | 31 | 0 | — |
| 4 | 20 | 39 | 0 | — |
| 5 | 22 | 39 | 0 | — |
| 6 | 16 | 33 | 0 | — |
| 7 | 18 | 36 | 0 | — |
| 8 | 16 | 31 | 11 | — |
| 9 | 18 | 34 | 0 | — |
| 10 | 16 | 36 | 0 | — |
| 11 | 14 | 29 | 0 | — |
| 12 | 18 | 37 | 0 | — |

### Sample issues by severity

#### WRONG_FABLE_LITERAL

- `G8-07` (form `(do (defprotocol Pace (speed [this])) (defrecord Hare [name]`): tortoise-hare ghost name 'Pip' appears in goose-eggs user_msg
    ```
    There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Halfway through the morning errand, Emily stopped in the orchard
with a basket of eggs and refused to move on until someone could
prove what the form `(do (defprotocol Pace (speed [this])) (defrecord Hare ...
    ```
- `G8-07` (form `(do (defprotocol Pace (speed [this])) (defrecord Hare [name]`): tortoise-hare ghost name 'Pip' appears in goose-eggs user_msg
    ```
    Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Alice offered a small basket of eggs as a wager near the village:
whoever guessed the result of `(do (defprotocol Pace (speed [this])) (defrecord Hare [name] Pace (speed [_] :swift)) (speed...
    ```
- `G8-07` (form `(do (defprotocol Pace (speed [this])) (defrecord Hare [name]`): tortoise-hare ghost name 'Pip' appears in goose-eggs user_msg
    ```
    The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A row of three coins sat on a wooden table near the market, set out as a
wager between Sam and Oliver. The bet was
simple: predict what `(do (defprotocol Pace (speed [this])) (...
    ```
- `G8-07` (form `(do (defprotocol Pace (speed [this])) (defrecord Tortoise [n`): tortoise-hare ghost name 'Shelly' appears in goose-eggs user_msg
    ```
    A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Bob had been trying to teach Alice how the REPL
works. "Here," he said, pointing to a Tortoise record implementing Pace with speed -> :steady.
"You hand the form `(do (defprotocol Pace (speed [thi...
    ```
- `G8-07` (form `(do (defprotocol Pace (speed [this])) (defrecord Tortoise [n`): tortoise-hare ghost name 'Shelly' appears in goose-eggs user_msg
    ```
    A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A scrap of parchment, pinned to the barn door deep inside the barn, set out a rule
that all egg-owners in the village would have to abide by. Casey,
with a hungry gleam in the eye, read it aloud: ...
    ```

#### PREDICATE_QUESTION_COLLISION

- `G8-15` (form `(do (derive ::hare ::runner) (isa? ::hare ::runner))`): predicate-suffix ``?`` collides with the question framing's trailing ``?`` or ``.``
    ```
    Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. This was inside the cellar.

Helen had been trying to teach Bob how the REPL
works. "Here," she said, pointing to deriving ::hare from ::runner and asking isa?.
"You hand the form `(do (deri...
    ```
- `G8-15` (form `(do (derive ::hare ::runner) (isa? ::hare ::runner))`): predicate-suffix ``?`` collides with the question framing's trailing ``?`` or ``.``
    ```
    Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A scrap of parchment, pinned to the barn door in the barn, set out a rule
that all egg-owners in the village would have to abide by. Casey,
eyeing the next morning's gift, read it aloud: it...
    ```

