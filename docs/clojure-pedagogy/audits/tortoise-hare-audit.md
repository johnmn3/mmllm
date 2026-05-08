# tortoise-hare curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

## Grade 2

## Grade 3

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(#(+ % 1) 5)` — user_msg 203 words

## Grade 4

## Grade 5

## Grade 6

### G6-01: Namespace as file

- examples: 3
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(name 'foo.bar)` — answer string 'foo.bar' appears in user_msg

### G6-15: Namespace meta

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(:doc (meta '\{:doc "steady wins"\} race))` — answer string 'steady wins' appears in user_msg

## Grade 7

### G7-11: Reading stack traces

- examples: 2
- variety @ n=50: 0.99
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(try (throw (ex-info "trouble" {})) (catch Excepti` — answer string 'trouble' appears in user_msg

## Grade 8

### G8-03: defrecord introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — user_msg 204 words

### G8-08: Multimethod defmulti

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defmulti pace :species) (defmethod pace :hare` — user_msg 207 words

### G8-14: Protocols don't inherit

- examples: 1
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg 218 words

## Grade 9

### G9-02: Why state at all

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (def progress (atom :idle)) (reset! progress :` — user_msg 201 words

### G9-08: dosync and alter

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — user_msg 207 words

### G9-17: binding — thread-local

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — user_msg 206 words

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (def lock (Object.)) (locking lock 42))` — user_msg 204 words

## Grade 10

### G10-03: defmacro introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg 204 words

### G10-16: Macro pattern library

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — user_msg 204 words

## Grade 11

### G11-08: Type hints

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(let [^String s "abc"] (.toUpperCase s))` — user_msg 203 words

## Grade 12

### G12-02: Transducer composition

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — user_msg 210 words

---

## Summary

### Issue counts (across all examples × 3 records)

- **HIGH_LENGTH**: 12
- **ANSWER_LEAK_STRING**: 3

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 0 | — |
| 2 | 22 | 88 | 0 | — |
| 3 | 18 | 31 | 1 | — |
| 4 | 20 | 39 | 0 | — |
| 5 | 22 | 39 | 0 | — |
| 6 | 16 | 33 | 2 | — |
| 7 | 18 | 36 | 1 | — |
| 8 | 16 | 31 | 3 | — |
| 9 | 18 | 34 | 4 | — |
| 10 | 16 | 36 | 2 | — |
| 11 | 14 | 29 | 1 | — |
| 12 | 18 | 37 | 1 | — |

### Sample issues by severity

#### HIGH_LENGTH

- `G3-10` (form `(#(+ % 1) 5)`): user_msg 203 words
    ```
    Among the small kingdoms of the meadow, swiftness was a kind of currency, and one creature spent it loudly.

Mossback was in a hurry at the roadside and had no time to write a full recipe card. She scratched a quick shorthand mark — `#(+ % 1)` — on a stone and put 5 acorns in front of it immediately...
    ```
- `G8-03` (form `(do (defrecord Runner [name pace]) (:pace (->Runner "Alice" `): user_msg 204 words
    ```
    Galop announced the race in a voice loud enough to wake the owls, and Fen accepted with a nod.

Mossback the tortoise was outfitting the meadow's runners with carrying-cases — small wooden cases with two named compartments inside, one labeled `name` and one labeled `pace`. The case-stamp on the outs...
    ```
- `G8-08` (form `(do (defmulti pace :species) (defmethod pace :hare [_] :swif`): user_msg 207 words
    ```
    Among the small kingdoms of the meadow, swiftness was a kind of currency, and one creature spent it loudly.

Mossback the tortoise set up a sorting-table at the edge of the meadow. Runners would walk up; the table would read each runner's :species stamp and route them to the matching arm.

Today's f...
    ```
- `G8-14` (form `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this`): user_msg 218 words
    ```
    In that part of the woods, no one ever expected the slow to outpace the swift, yet the question was always quietly asked.

Mossback the tortoise founded two separate guilds — A and B — each with its own routine. She signed the String type into both guilds independently, giving each its own implement...
    ```
- `G9-02` (form `(do (def progress (atom :idle)) (reset! progress :running) @`): user_msg 201 words
    ```
    It is one thing to have fast legs and another to know how to use them, as the meadow folk would soon be reminded.

Mossback kept a small notebook on the stump to track the race's status. Before the starting horn, the page read the idle word. The horn sounded and the race began.

The status needed to...
    ```

#### ANSWER_LEAK_STRING

- `G6-01` (form `(name 'foo.bar)`): answer string 'foo.bar' appears in user_msg
    ```
    Some say it began with a yawn and a laugh; others say it began with a quiet refusal to be laughed at.

On the long road, there lay a library shelf holding scrolls. Each scroll had a name — foo.bar, tortoise.race — inscribed on its spine in the style of the land.

Mossback the tortoise needed to know...
    ```
- `G6-15` (form `(:doc (meta '\{:doc "steady wins"\} race))`): answer string 'steady wins' appears in user_msg
    ```
    Two creatures of very different gait once agreed that the ground between two stones would settle a long argument.

On a scroll lay a symbol race, marked with marginalia in the margin: ^{:doc "steady wins"}. The margin held a note — a docstring — explaining what the symbol was about.

Mossback wanted...
    ```
- `G7-11` (form `(try (throw (ex-info "trouble" {})) (catch Exception e (.get`): answer string 'trouble' appears in user_msg
    ```
    Among the small kingdoms of the meadow, swiftness was a kind of currency, and one creature spent it loudly.

Lichen the tortoise stretched a small net beneath a high jump
at the edge of the woods. "If the runner falls, the net catches them; the run
doesn't end, only the path bends." To throw an ex-i...
    ```

