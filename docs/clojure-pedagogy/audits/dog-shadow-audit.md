# dog-shadow curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

## Grade 2

### G2-01: Multi-arg arithmetic

- examples: 6
- variety @ n=50: 0.98
- issues: {'ANSWER_LEAK': 2}
    - [ANSWER_LEAK] form=`(+ 1 2 3 4 5 6 7 8 9 10)` — answer 55 in narrative
    - [ANSWER_LEAK] form=`(* 1 2 3 4 5)` — answer 120 in narrative

### G2-05: quot, rem, mod

- examples: 6
- variety @ n=50: 0.99
- issues: {'UNFILLED_PLACEHOLDER': 1}
    - [UNFILLED_PLACEHOLDER] form=`(rem 17 5)` — user_msg has un-substituted placeholder

### G2-20: Counting

- examples: 3
- variety @ n=50: 0.95

## Grade 3

### G3-01: def — top-level binding

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (def y 7) y)` — user_msg 213 words

### G3-04: let — multi-binding

- examples: 3
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 2}
    - [HIGH_LENGTH] form=`(let [a 1 b 2] (+ a b))` — user_msg 205 words
    - [HIGH_LENGTH] form=`(let [a 2 b 3 c 4] (+ a b c))` — user_msg 207 words

### G3-05: let — shadowing outer def

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 2, 'UNFILLED_PLACEHOLDER': 1}
    - [HIGH_LENGTH] form=`(do (def x 10) (let [x 99] x))` — user_msg 255 words
    - [UNFILLED_PLACEHOLDER] form=`(do (def x 10) (let [x 99] x))` — user_msg has un-substituted placeholder
    - [HIGH_LENGTH] form=`(do (def x 10) (let [x 99] x) x)` — user_msg 248 words

### G3-07: fn — anonymous function

- examples: 2
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1, 'UNFILLED_PLACEHOLDER': 1}
    - [HIGH_LENGTH] form=`((fn [a b] (* a b)) 3 4)` — user_msg 225 words
    - [UNFILLED_PLACEHOLDER] form=`((fn [a b] (* a b)) 3 4)` — user_msg has un-substituted placeholder

### G3-08: fn — multi-arg

- examples: 1
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1, 'UNFILLED_PLACEHOLDER': 1}
    - [HIGH_LENGTH] form=`((fn [a b c] (+ a b c)) 1 2 3)` — user_msg 222 words
    - [UNFILLED_PLACEHOLDER] form=`((fn [a b c] (+ a b c)) 1 2 3)` — user_msg has un-substituted placeholder

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 2}
    - [HIGH_LENGTH] form=`(#(+ % 1) 5)` — user_msg 220 words
    - [HIGH_LENGTH] form=`(#(+ % 1) 5)` — user_msg 220 words

### G3-11: Substitution rule

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 2, 'UNFILLED_PLACEHOLDER': 2}
    - [HIGH_LENGTH] form=`(let [a 7] (+ a a))` — user_msg 213 words
    - [UNFILLED_PLACEHOLDER] form=`(let [a 7] (+ a a))` — user_msg has un-substituted placeholder
    - [HIGH_LENGTH] form=`(let [a 7] (+ a a))` — user_msg 201 words
    - [UNFILLED_PLACEHOLDER] form=`(let [a 7] (+ a a))` — user_msg has un-substituted placeholder

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
- issues: {'HIGH_LENGTH': 1, 'UNFILLED_PLACEHOLDER': 1}
    - [HIGH_LENGTH] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — user_msg 238 words
    - [UNFILLED_PLACEHOLDER] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — user_msg has un-substituted placeholder

### G5-05: cond — :else

- examples: 1
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(cond false :a false :b :else :c)` — user_msg 213 words

### G5-07: and / or as control flow

- examples: 2
- variety @ n=50: 0.97
- issues: {'HIGH_LENGTH': 1, 'UNFILLED_PLACEHOLDER': 1, 'ANSWER_LEAK_STRING': 1}
    - [HIGH_LENGTH] form=`(or nil false :found)` — user_msg 212 words
    - [UNFILLED_PLACEHOLDER] form=`(or nil false :found)` — user_msg has un-substituted placeholder
    - [ANSWER_LEAK_STRING] form=`(or nil false :found)` — answer string ':found' appears in user_msg

### G5-08: not

- examples: 1
- variety @ n=50: 1.00
- issues: {'UNFILLED_PLACEHOLDER': 1}
    - [UNFILLED_PLACEHOLDER] form=`(not (> 1 2))` — user_msg has un-substituted placeholder

### G5-10: map

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 2, 'UNFILLED_PLACEHOLDER': 2}
    - [HIGH_LENGTH] form=`(map inc [1 2 3])` — user_msg 258 words
    - [UNFILLED_PLACEHOLDER] form=`(map inc [1 2 3])` — user_msg has un-substituted placeholder
    - [HIGH_LENGTH] form=`(map inc [1 2 3])` — user_msg 258 words
    - [UNFILLED_PLACEHOLDER] form=`(map inc [1 2 3])` — user_msg has un-substituted placeholder

### G5-11: filter

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 2, 'UNFILLED_PLACEHOLDER': 2}
    - [HIGH_LENGTH] form=`(filter even? [1 2 3 4])` — user_msg 225 words
    - [UNFILLED_PLACEHOLDER] form=`(filter even? [1 2 3 4])` — user_msg has un-substituted placeholder
    - [HIGH_LENGTH] form=`(filter even? [1 2 3 4])` — user_msg 213 words
    - [UNFILLED_PLACEHOLDER] form=`(filter even? [1 2 3 4])` — user_msg has un-substituted placeholder

### G5-12: reduce

- examples: 3
- variety @ n=50: 0.97
- issues: {'HIGH_LENGTH': 2, 'UNFILLED_PLACEHOLDER': 1, 'ANSWER_LEAK': 1}
    - [HIGH_LENGTH] form=`(reduce * [1 2 3 4 5])` — user_msg 208 words
    - [UNFILLED_PLACEHOLDER] form=`(reduce * [1 2 3 4 5])` — user_msg has un-substituted placeholder
    - [ANSWER_LEAK] form=`(reduce * [1 2 3 4 5])` — answer 120 in narrative
    - [HIGH_LENGTH] form=`(reduce max [3 1 4 1 5 9 2 6])` — user_msg 225 words

### G5-14: apply

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 2, 'UNFILLED_PLACEHOLDER': 2}
    - [HIGH_LENGTH] form=`(apply max [3 1 4 1 5])` — user_msg 206 words
    - [UNFILLED_PLACEHOLDER] form=`(apply max [3 1 4 1 5])` — user_msg has un-substituted placeholder
    - [HIGH_LENGTH] form=`(apply max [3 1 4 1 5])` — user_msg 211 words
    - [UNFILLED_PLACEHOLDER] form=`(apply max [3 1 4 1 5])` — user_msg has un-substituted placeholder

### G5-15: comp

- examples: 2
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1, 'UNFILLED_PLACEHOLDER': 1}
    - [HIGH_LENGTH] form=`((comp str inc) 9)` — user_msg 204 words
    - [UNFILLED_PLACEHOLDER] form=`((comp str inc) 9)` — user_msg has un-substituted placeholder

### G5-16: partial

- examples: 2
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(map (partial * 3) [1 2 3])` — user_msg 224 words

### G5-17: juxt

- examples: 1
- variety @ n=50: 0.96
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`((juxt inc dec) 5)` — user_msg 212 words

### G5-19: every?

- examples: 2
- variety @ n=50: 0.97
- issues: {'UNFILLED_PLACEHOLDER': 1}
    - [UNFILLED_PLACEHOLDER] form=`(every? even? [1 2 3])` — user_msg has un-substituted placeholder

### G5-21: distinct and sort

- examples: 2
- variety @ n=50: 0.96
- issues: {'UNFILLED_PLACEHOLDER': 1}
    - [UNFILLED_PLACEHOLDER] form=`(sort [3 1 2])` — user_msg has un-substituted placeholder

## Grade 6

### G6-01: Namespace as file

- examples: 3
- variety @ n=50: 0.98
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(name 'clojure.string)` — answer string 'clojure.string' appears in user_msg

### G6-14: Import for host classes

- examples: 2
- variety @ n=50: 0.97
- issues: {'ANSWER_LEAK_STRING': 2}
    - [ANSWER_LEAK_STRING] form=`(name 'java.util.Map)` — answer string 'java.util.Map' appears in user_msg
    - [ANSWER_LEAK_STRING] form=`(name 'java.util.Map)` — answer string 'java.util.Map' appears in user_msg

## Grade 7

### G7-05: nil punning

- examples: 4
- variety @ n=50: 0.99
- issues: {'UNFILLED_PLACEHOLDER': 1}
    - [UNFILLED_PLACEHOLDER] form=`(some? nil)` — user_msg has un-substituted placeholder

### G7-10: doc and source

- examples: 1
- variety @ n=50: 1.00
- issues: {'UNFILLED_PLACEHOLDER': 2, 'ANSWER_LEAK_STRING': 2}
    - [UNFILLED_PLACEHOLDER] form=`(:doc (meta '^{:doc "adds two"} plus))` — user_msg has un-substituted placeholder
    - [ANSWER_LEAK_STRING] form=`(:doc (meta '^{:doc "adds two"} plus))` — answer string 'adds two' appears in user_msg
    - [UNFILLED_PLACEHOLDER] form=`(:doc (meta '^{:doc "adds two"} plus))` — user_msg has un-substituted placeholder
    - [ANSWER_LEAK_STRING] form=`(:doc (meta '^{:doc "adds two"} plus))` — answer string 'adds two' appears in user_msg

### G7-11: Reading stack traces

- examples: 2
- variety @ n=50: 0.99
- issues: {'ANSWER_LEAK_STRING': 2}
    - [ANSWER_LEAK_STRING] form=`(try (throw (Exception. "oops")) (catch Exception ` — answer string 'oops' appears in user_msg
    - [ANSWER_LEAK_STRING] form=`(try (throw (Exception. "oops")) (catch Exception ` — answer string 'oops' appears in user_msg

### G7-12: slurp and spit

- examples: 2
- variety @ n=50: 1.00
- issues: {'UNFILLED_PLACEHOLDER': 1}
    - [UNFILLED_PLACEHOLDER] form=`(clojure.string/split "a\nb\nc" #"\n")` — user_msg has un-substituted placeholder

### G7-13: line-seq

- examples: 2
- variety @ n=50: 0.99
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(first (clojure.string/split-lines "first\nsecond"` — answer string 'first' appears in user_msg

### G7-15: *in* and *out*

- examples: 2
- variety @ n=50: 1.00
- issues: {'UNFILLED_PLACEHOLDER': 1}
    - [UNFILLED_PLACEHOLDER] form=`(with-out-str (println))` — user_msg has un-substituted placeholder

### G7-16: edn read

- examples: 3
- variety @ n=50: 0.97
- issues: {'UNFILLED_PLACEHOLDER': 1}
    - [UNFILLED_PLACEHOLDER] form=`(clojure.edn/read-string "{:a 1}")` — user_msg has un-substituted placeholder

### G7-17: JSON roundtrip

- examples: 2
- variety @ n=50: 0.99
- issues: {'UNFILLED_PLACEHOLDER': 1}
    - [UNFILLED_PLACEHOLDER] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — user_msg has un-substituted placeholder

## Grade 8

### G8-04: Protocol definition

- examples: 2
- variety @ n=50: 0.97
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — user_msg 214 words

### G8-05: Protocol extension

- examples: 2
- variety @ n=50: 0.97
- issues: {'ANSWER_LEAK_STRING': 1, 'HIGH_LENGTH': 1}
    - [ANSWER_LEAK_STRING] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — answer string 'swift' appears in user_msg
    - [HIGH_LENGTH] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — user_msg 209 words

### G8-07: Record implementing protocol

- examples: 2
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defprotocol Pace (speed [this])) (defrecord T` — user_msg 204 words

### G8-10: Multimethod vs protocol

- examples: 2
- variety @ n=50: 0.99
- issues: {'ANSWER_LEAK_STRING': 2}
    - [ANSWER_LEAK_STRING] form=`(do (defmulti show identity) (defmethod show :rabb` — answer string 'quick' appears in user_msg
    - [ANSWER_LEAK_STRING] form=`(do (defmulti show identity) (defmethod show :rabb` — answer string 'quick' appears in user_msg

### G8-13: this-style vs fn-style

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 1, 'ANSWER_LEAK_STRING': 1}
    - [HIGH_LENGTH] form=`(do (defprotocol Tagged (tag-of [this])) (defrecor` — user_msg 245 words
    - [ANSWER_LEAK_STRING] form=`(do (defprotocol Tagged (tag-of [this])) (defrecor` — answer string ':grey' appears in user_msg

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

### G10-05: macroexpand

- examples: 2
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(macroexpand '(-> 1 inc inc))` — user_msg 217 words

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 0.97
- issues: {'HIGH_LENGTH': 1, 'ANSWER_LEAK': 1}
    - [HIGH_LENGTH] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — user_msg 211 words
    - [ANSWER_LEAK] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — answer 8 in narrative

### G10-08: Macro vs fn

- examples: 2
- variety @ n=50: 0.99
- issues: {'ANSWER_LEAK': 1}
    - [ANSWER_LEAK] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — answer 7 in narrative

### G10-10: Anaphoric macros are confusing

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'ANSWER_LEAK': 2}
    - [HIGH_LENGTH] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — user_msg 221 words
    - [ANSWER_LEAK] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — answer 10 in narrative
    - [HIGH_LENGTH] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — user_msg 221 words
    - [ANSWER_LEAK] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — answer 10 in narrative

### G10-11: Reader macros overview

- examples: 3
- variety @ n=50: 0.99
- issues: {'HIGH_LENGTH': 2}
    - [HIGH_LENGTH] form=`'(1 2 3)` — user_msg 211 words
    - [HIGH_LENGTH] form=`[1 #_ 2 3]` — user_msg 212 words

### G10-14: eval (the function)

- examples: 2
- variety @ n=50: 0.98
- issues: {'ANSWER_LEAK': 2}
    - [ANSWER_LEAK] form=`(eval (list '+ 4 5))` — answer 9 in narrative
    - [ANSWER_LEAK] form=`(eval (list '+ 4 5))` — answer 9 in narrative

### G10-15: When not to write a macro

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do "prefer fn unless you must shape syntax" (map ` — user_msg 204 words

### G10-16: Macro pattern library

- examples: 2
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1, 'ANSWER_LEAK_STRING': 1}
    - [HIGH_LENGTH] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — user_msg 226 words
    - [ANSWER_LEAK_STRING] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — answer string ':slow' appears in user_msg

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

- **HIGH_LENGTH**: 56
- **UNFILLED_PLACEHOLDER**: 26
- **ANSWER_LEAK_STRING**: 14
- **ANSWER_LEAK**: 9

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 0 | — |
| 2 | 22 | 88 | 3 | G2-20(0.95) |
| 3 | 18 | 31 | 18 | — |
| 4 | 20 | 39 | 0 | — |
| 5 | 22 | 39 | 29 | — |
| 6 | 16 | 33 | 3 | — |
| 7 | 18 | 36 | 12 | — |
| 8 | 16 | 31 | 9 | — |
| 9 | 18 | 34 | 12 | G9-05(0.94) |
| 10 | 16 | 36 | 15 | — |
| 11 | 14 | 29 | 4 | — |
| 12 | 18 | 37 | 0 | — |

### Sample issues by severity

#### ANSWER_LEAK

- `G2-01` (form `(+ 1 2 3 4 5 6 7 8 9 10)`): answer 55 in narrative
    ```
    A Dog was crossing a stream with a fine bone in his mouth, and was very pleased with himself. All this took place by the meadow.

Rex the hound arranged ten marked stones in a line at the stream's edge, each one numbered from 1 to 10. He wanted the grand tally of all of them stacked together.

He ne...
    ```
- `G2-01` (form `(* 1 2 3 4 5)`): answer 120 in narrative
    ```
    It is said that the foolish Dog will trade what is real for what is only an image.

Patch the hound laid five bones in a row near the forest, each one carved with the numbers 1, 2, 3, 4, and 5. They wanted to multiply them all together to see what the chain would yield.

They needed the product when...
    ```
- `G5-12` (form `(reduce * [1 2 3 4 5])`): answer 120 in narrative
    ```
    A Dog was crossing a stream with a fine bone in his mouth, and was very pleased with himself.

Bell the hound stood at a different stretch of the bank {place}, facing a row of pebbles marked 1, 2, 3, 4, 5. She would walk the row, carrying a product-tally, multiplying each pebble into the tally as sh...
    ```
- `G10-07` (form `(->> [1 2 3 4] (filter even?) (map inc) (reduce +))`): answer 8 in narrative
    ```
    It is said that the foolish Dog will trade what is real for what is only an image.

Rex the hound had a vector of four bones and a multi-step sniffing-trail. Thread-last would pass the bones as the final argument to each step — first filtering for even counts, then incrementing each, then summing th...
    ```
- `G10-08` (form `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))`): answer 7 in narrative
    ```
    Greed has cost more than one creature what they already had.

Bell the hound set a sniffing-trail rule named add-fn. When a dog followed the trail with bones 3 and 4, the trail would evaluate the bones first, then add them. The function takes pre-computed values.

When add-fn is called with 3 and 4,...
    ```

#### UNFILLED_PLACEHOLDER

- `G2-05` (form `(rem 17 5)`): user_msg has un-substituted placeholder
    ```
    A Dog was crossing a stream with a fine bone in his mouth, and was very pleased with himself.

Patch the hound held seventeen bones and wanted to share them into groups of five {place}. Some bones would be left over — strays that did not fill a complete group.

They wanted to know how many bones rem...
    ```
- `G3-05` (form `(do (def x 10) (let [x 99] x))`): user_msg has un-substituted placeholder
    ```
    What the Dog thought he saw beneath the water turned out to be his own reflection.

Bell the hound had long marked a stone {place} with the name x, recording a weight of 10 beside it for all to read. But one day, she picked up a much larger bone and held it in her jaws for a single crossing. "For ju...
    ```
- `G3-07` (form `((fn [a b] (* a b)) 3 4)`): user_msg has un-substituted placeholder
    ```
    It is said that the foolish Dog will trade what is real for what is only an image.

Patch the hound laid out a quick nose-trail {place} — a path of sniffs that said: take whatever comes in, take what comes next, and hand back their product. "This trail is nameless," Patch said, breathing along the s...
    ```
- `G3-08` (form `((fn [a b c] (+ a b c)) 1 2 3)`): user_msg has un-substituted placeholder
    ```
    Greed has cost more than one creature what they already had.

Rex the hound drew out three sniffing-steps {place}, a path that asked for three separate counts. "Take the first, then the second, then the third," he said, tracing the marks, "and carry back their sum. This trail has no name — I design ...
    ```
- `G3-11` (form `(let [a 7] (+ a a))`): user_msg has un-substituted placeholder
    ```
    What the Dog thought he saw beneath the water turned out to be his own reflection. All this took place by the forest.

Patch the hound held a bone {place} between his jaws — a count of 7. "I will call this grip a," he said, "and I need to know what a plus a makes. The name a means 7, so I will add 7...
    ```

#### HIGH_LENGTH

- `G3-01` (form `(do (def y 7) y)`): user_msg 213 words
    ```
    What the Dog thought he saw beneath the water turned out to be his own reflection. All this took place by the forest.

Rex the hound discovered a worn stone at the stream's edge and began carving a fresh name into its face — y. "When I cut a name deep into the marker," he said, pressing the stone's ...
    ```
- `G3-04` (form `(let [a 1 b 2] (+ a b))`): user_msg 205 words
    ```
    Greed has cost more than one creature what they already had. It happened along the road.

Patch the hound arrived at the crossing with two bones — one small, one larger. "I will know these two by separate names for the span of this form," Patch said, holding both between the jaws. "The names a and b...
    ```
- `G3-04` (form `(let [a 2 b 3 c 4] (+ a b c))`): user_msg 207 words
    ```
    Greed has cost more than one creature what they already had.

Rex the hound gathered three bones at the stream's edge and clenched them all between his jaws — a light grip, a medium one, and a heavy one. "I will hold these as a, b, and c for one stretch," he said, naming each as his teeth settled. "...
    ```
- `G3-05` (form `(do (def x 10) (let [x 99] x))`): user_msg 255 words
    ```
    What the Dog thought he saw beneath the water turned out to be his own reflection.

Bell the hound had long marked a stone {place} with the name x, recording a weight of 10 beside it for all to read. But one day, she picked up a much larger bone and held it in her jaws for a single crossing. "For ju...
    ```
- `G3-05` (form `(do (def x 10) (let [x 99] x) x)`): user_msg 248 words
    ```
    A Dog was crossing a stream with a fine bone in his mouth, and was very pleased with himself.

Patch the hound had carved a marker stone by the forest, scratching the name x deep into it and pressing a weight of 10 beside it. One crossing later, Patch picked up a larger bone and held it in the jaws ...
    ```

#### ANSWER_LEAK_STRING

- `G5-07` (form `(or nil false :found)`): answer string ':found' appears in user_msg
    ```
    It is said that the foolish Dog will trade what is real for what is only an image.

Rex stood at a different fork {place}, facing a row of gates. Three gates in sequence: the first held nil (a closed gate), the second held false (also closed), the third held :found (an open gate). The or-form would ...
    ```
- `G6-01` (form `(name 'clojure.string)`): answer string 'clojure.string' appears in user_msg
    ```
    What the Dog thought he saw beneath the water turned out to be his own reflection. All this took place by the forest.

Further upstream, Patch found another stone marker with a longer path scratched in — clojure.string — a well-known location where other dogs had cached their scrolls.

She wanted to...
    ```
- `G6-14` (form `(name 'java.util.Map)`): answer string 'java.util.Map' appears in user_msg
    ```
    It is said that the foolish Dog will trade what is real for what is only an image.

Patch returned to the kennel-master's shed where another tool hung on a peg — this one labeled with a long Java class name: java.util.Map. She wanted to extract the plain text of that host-side label and read it alou...
    ```
- `G6-14` (form `(name 'java.util.Map)`): answer string 'java.util.Map' appears in user_msg
    ```
    What the Dog thought he saw beneath the water turned out to be his own reflection. It happened on the road.

Patch returned to the kennel-master's shed where another tool hung on a peg — this one labeled with a long Java class name: java.util.Map. She wanted to extract the plain text of that host-si...
    ```
- `G7-10` (form `(:doc (meta '^{:doc "adds two"} plus))`): answer string 'adds two' appears in user_msg
    ```
    What the Dog thought he saw beneath the water turned out to be his own reflection.

Patch found a message-bone marked "plus" at the stone {place}. The bone carried metadata—extra scratch-marks that said what the symbol meant: "adds two". She wanted to read that documentation.

She needed to extract ...
    ```

