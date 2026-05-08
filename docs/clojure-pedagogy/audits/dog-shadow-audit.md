# dog-shadow curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

### G1-09: Symbols vs values

- examples: 4
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(= 'hare 'hare)` — user_msg 206 words

## Grade 2

### G2-10: Powers via repeated multiplication

- examples: 4
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 2}
    - [ANSWER_LEAK] form=`(* 3 3 3 3)` — answer 81 in narrative
    - [ANSWER_LEAK] form=`(* 3 3 3 3)` — answer 81 in narrative

### G2-18: Quoting symbols

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(= (quote tortoise) 'tortoise)` — user_msg 201 words

## Grade 3

### G3-03: let — local binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(let [a 5] a)` — user_msg 231 words

### G3-06: let — binding can reference prior

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(let [a 5 b (* a 2)] b)` — user_msg 242 words

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(#(* %1 %2) 3 4)` — user_msg 222 words

### G3-13: fn body returns last form

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`((fn [x] x x x 99) 1)` — user_msg 232 words

### G3-18: When to name vs inline

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(let [n 5] (* n n n))` — user_msg 228 words

## Grade 4

## Grade 5

### G5-10: map

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2}
    - [HIGH_LENGTH] form=`(map #(* % %) [1 2 3 4])` — user_msg 205 words
    - [HIGH_LENGTH] form=`(map #(* % %) [1 2 3 4])` — user_msg 204 words

### G5-15: comp

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'ANSWER_LEAK': 1}
    - [HIGH_LENGTH] form=`((comp inc inc) 5)` — user_msg 207 words
    - [ANSWER_LEAK] form=`((comp inc inc) 5)` — answer 7 in narrative

### G5-22: recur — first taste

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 3}
    - [HIGH_LENGTH] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — user_msg 227 words
    - [HIGH_LENGTH] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — user_msg 226 words
    - [HIGH_LENGTH] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — user_msg 226 words

## Grade 6

### G6-01: Namespace as file

- examples: 3
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(name 'foo.bar)` — answer string 'foo.bar' appears in user_msg

### G6-15: Namespace meta

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(:doc (meta '\{:doc "steady wins"\} race))` — user_msg 207 words

## Grade 7

## Grade 8

### G8-02: deftype introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (deftype Stone [weight]) (.-weight (Stone. 7))` — user_msg 207 words

### G8-03: defrecord introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'ANSWER_LEAK_STRING': 1}
    - [HIGH_LENGTH] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — user_msg 206 words
    - [ANSWER_LEAK_STRING] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — answer string ':slow' appears in user_msg

### G8-08: Multimethod defmulti

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defmulti pace :species) (defmethod pace :hare` — user_msg 202 words

### G8-09: Multimethod defmethod

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defmulti pace :species) (defmethod pace :hare` — user_msg 207 words

### G8-14: Protocols don't inherit

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg 216 words

## Grade 9

### G9-02: Why state at all

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (def progress (atom :idle)) (reset! progress :` — user_msg 227 words

### G9-03: Atom introduction

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg 217 words

### G9-07: Ref introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` — user_msg 205 words

### G9-08: dosync and alter

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — user_msg 213 words

### G9-09: Ref vs atom

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg 212 words

### G9-10: Agent introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (def ag (agent 5)) (send ag + 10) (await ag) @` — user_msg 223 words

### G9-13: future introduction

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`@(future (+ 1 2))` — user_msg 212 words

### G9-15: promise — deliver and deref

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(do (def p (promise)) (deliver p :done) @p)` — answer string ':done' appears in user_msg

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 4}
    - [HIGH_LENGTH] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg 233 words
    - [HIGH_LENGTH] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg 233 words
    - [HIGH_LENGTH] form=`(do (def lock (Object.)) (locking lock 42))` — user_msg 225 words
    - [HIGH_LENGTH] form=`(do (def lock (Object.)) (locking lock 42))` — user_msg 221 words

## Grade 10

### G10-02: syntax-quote

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(let [xs [1 2 3]] `(list ~@xs))` — user_msg 219 words

### G10-03: defmacro introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg 234 words

### G10-06: when and when-not as macros

- examples: 3
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 2}
    - [ANSWER_LEAK_STRING] form=`(when-not false :ok)` — answer string ':ok' appears in user_msg
    - [ANSWER_LEAK_STRING] form=`(when-not false :ok)` — answer string ':ok' appears in user_msg

### G10-08: Macro vs fn

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'ANSWER_LEAK': 1}
    - [HIGH_LENGTH] form=`(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3` — user_msg 207 words
    - [ANSWER_LEAK] form=`(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3` — answer 7 in narrative

### G10-09: Hygiene and gensym

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — user_msg 211 words

### G10-10: Anaphoric macros are confusing

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'ANSWER_LEAK': 1}
    - [HIGH_LENGTH] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — user_msg 206 words
    - [HIGH_LENGTH] form=`(if-let [x 7] (* x x) 0)` — user_msg 218 words
    - [ANSWER_LEAK] form=`(if-let [x 7] (* x x) 0)` — answer 49 in narrative

### G10-14: eval (the function)

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1}
    - [ANSWER_LEAK] form=`(eval '(+ 1 2 3))` — answer 6 in narrative

## Grade 11

### G11-02: Method call syntax

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(.startsWith "hare-tortoise" "hare")` — user_msg 215 words

### G11-03: Static method call

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(Math/abs -7)` — user_msg 221 words

### G11-06: new and dot-construct

- examples: 2
- variety @ n=50: 0.99
- issues: {'ANSWER_LEAK_STRING': 2}
    - [ANSWER_LEAK_STRING] form=`(new String "jump")` — answer string 'jump' appears in user_msg
    - [ANSWER_LEAK_STRING] form=`(new String "jump")` — answer string 'jump' appears in user_msg

## Grade 12

### G12-01: Transducers introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(into [] (map inc) [1 2 3])` — user_msg 238 words

### G12-03: into with a transducer (xform)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(into #{} (map inc) [1 2 3])` — user_msg 244 words

---

## Summary

### Issue counts (across all examples × 3 records)

- **HIGH_LENGTH**: 40
- **ANSWER_LEAK_STRING**: 7
- **ANSWER_LEAK**: 6

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 1 | — |
| 2 | 22 | 88 | 3 | — |
| 3 | 18 | 31 | 5 | — |
| 4 | 20 | 39 | 0 | — |
| 5 | 22 | 39 | 7 | — |
| 6 | 16 | 33 | 2 | — |
| 7 | 18 | 36 | 0 | — |
| 8 | 16 | 31 | 6 | — |
| 9 | 18 | 34 | 12 | — |
| 10 | 16 | 36 | 11 | — |
| 11 | 14 | 29 | 4 | — |
| 12 | 18 | 37 | 2 | — |

### Sample issues by severity

#### HIGH_LENGTH

- `G1-09` (form `(= 'hare 'hare)`): user_msg 206 words
    ```
    It happened on the village, on the very bridge Bagel the dog crossed every day, that he stopped longer than he should have.

Rex the hound laid two scratch-marks side by side on bark near the forest. Both marks said the same thing: hare, hare. "Are these two scratches the same name?" Rex asked. "Bot...
    ```
- `G2-18` (form `(= (quote tortoise) 'tortoise)`): user_msg 201 words
    ```
    It was at the edge of the pond, on the wooden bridge above the slow brook, that Henry the dog looked down at the water.

Bell the hound found two bones at the stream's edge scratched with the same mark. One bore the long scratch of the full word tortoise, the other a quick mark that meant the same t...
    ```
- `G3-03` (form `(let [a 5] a)`): user_msg 231 words
    ```
    near the beach, where the boards of the bridge meet the stones of the path, Snoopy the dog caught sight of himself in the stream.

Bell the hound found a bone near the meadow, five joints long, and cradled it between her teeth. "For this one stretch of the path, I will know this bone by the name a,"...
    ```
- `G3-06` (form `(let [a 5 b (* a 2)] b)`): user_msg 242 words
    ```
    It was an afternoon of quiet sky and steady current, and the world below the surface seemed almost solid.

Rex the hound gathered five bones and clamped them in his jaws as the name a. Before stepping forward, he computed in his mind what twice that grip would weigh — and held both the first grip an...
    ```
- `G3-10` (form `(#(* %1 %2) 3 4)`): user_msg 222 words
    ```
    Snuffler the dog was halfway home by the village when the water played its old trick on a young dog.

Bell the hound drew a bare-minimum sniffing-path at the stream's edge — so short and terse it had almost no form at all. "%1 and %2, then multiply," the marks said in one quick sequence. The trail w...
    ```

#### ANSWER_LEAK

- `G2-10` (form `(* 3 3 3 3)`): answer 81 in narrative
    ```
    A dog with a bone in his jaws is a happy creature; a dog who looks too hard at the water may not be.

Bell the hound gathered four pebbles at the stream's edge, each marked with 3. She wanted to multiply them all together to find the fourth power.

She needed the result of three multiplied four time...
    ```
- `G2-10` (form `(* 3 3 3 3)`): answer 81 in narrative
    ```
    It is one of the oldest tricks of light to make one bone seem like two and to make a fool of the unwary.

Bell the hound gathered four pebbles at the stream's edge, each marked with 3. She wanted to multiply them all together to find the fourth power.

She needed the result of three multiplied four ...
    ```
- `G5-15` (form `((comp inc inc) 5)`): answer 7 in narrative
    ```
    It was an afternoon of quiet sky and steady current, and the world below the surface seemed almost solid.

Patch the hound laid down two nose-trails end to end by the river bank. The first trail was inc, the second trail was inc again. She would chain them together, so what the first trail turned up...
    ```
- `G10-08` (form `(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))`): answer 7 in narrative
    ```
    Down by the stream where the bank dipped low, the world above was answered politely by the world below.

Rex the hound set a rewrite-rule named add-mac. Unlike the function, the macro would rewrite the call first — before any evaluation. It would receive the unevaluated marks 3 and 4, then build a n...
    ```
- `G10-10` (form `(if-let [x 7] (* x x) 0)`): answer 49 in narrative
    ```
    Snuffler the dog was halfway home by the village when the water played its old trick on a young dog.

Rex the hound found the if-let rule carved on the bank. It would bind x to a value — 7 in this case — and test whether the binding succeeded. If it did, the then-branch would run with x in scope.

W...
    ```

#### ANSWER_LEAK_STRING

- `G6-01` (form `(name 'foo.bar)`): answer string 'foo.bar' appears in user_msg
    ```
    There is a kind of greed that does not see what it already has, and another kind that mistakes a reflection for a meal.

Patch the hound examined a marker stone at the stream's edge with a strange dotted path scratched into it — foo.bar. {hound_he_she} wanted to read what the scratch said without us...
    ```
- `G8-03` (form `(do (defrecord Runner [name pace]) (:pace (->Runner "Alice" `): answer string ':slow' appears in user_msg
    ```
    Diesel had crossed this bridge a hundred times on the beach, but never with so fine a bone clamped in his jaws.

Bell the hound crafted a labeled kennel-bag for tracking runners. The bag had two named compartments — one for a runner's name, one for the runner's pace-style. She slipped "Alice" and :s...
    ```
- `G9-15` (form `(do (def p (promise)) (deliver p :done) @p)`): answer string ':done' appears in user_msg
    ```
    It was an afternoon of quiet sky and steady current, and the world below the surface seemed almost solid.

Bell sent a scout-dog with a task. She created a promise — an empty satchel for the scout's answer.

The scout would race ahead, do the work, then deliver the answer to the promise. Bell would ...
    ```
- `G10-06` (form `(when-not false :ok)`): answer string ':ok' appears in user_msg
    ```
    A dog with a bone in his jaws is a happy creature; a dog who looks too hard at the water may not be.

Bell the hound wanted the opposite check: run the expression only if the condition was false. She scratched when-not false and the keyword :ok. "If danger is NOT present, say all is well."

When-not...
    ```
- `G10-06` (form `(when-not false :ok)`): answer string ':ok' appears in user_msg
    ```
    Diesel the dog was crossing the stream on the river bank when she caught a glimpse of his own reflection.

Bell the hound wanted the opposite check: run the expression only if the condition was false. She scratched when-not false and the keyword :ok. "If danger is NOT present, say all is well."

Whe...
    ```

