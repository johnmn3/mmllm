# tortoise-hare curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

### G1-09: Symbols vs values

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4}
    - [LOW_GROUNDING] form=`(symbol? 'hare)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(= 'hare 'hare)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(= 'hare 'hare)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(= 'hare 'hare)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

## Grade 2

### G2-08: Arithmetic on ratios

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(+ 1/2 1/4)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(+ 1/2 1/4)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(* 2/3 3/4)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(* 2/3 3/4)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(* 2/3 3/4)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G2-13: and / or — short circuit, return values

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 9}
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(and true false)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(and true false)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(and true false)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(or false true)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G2-14: not — turning truthy to false

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(not false)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(not nil)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(not nil)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G2-16: Truthy 0 and empty string

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(boolean nil)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(boolean nil)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G2-18: Quoting symbols

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G2-19: Auto-promotion to bigint

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(* 1000000 1000000)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(* 1000000 1000000)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(* 1000000 1000000)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

## Grade 3

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(#(+ % 1) 5)` — user_msg 205 words

### G3-13: fn body returns last form

- examples: 1
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`((fn [x] x x x 99) 1)` — user_msg 201 words

### G3-16: Name collision: namespace vs let

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(let [+ 99] +)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

## Grade 4

### G4-16: into and conj on collections

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(into #{} [1 2 2 3])` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(into #{} [1 2 2 3])` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(into #{} [1 2 2 3])` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

## Grade 5

## Grade 6

### G6-01: Namespace as file

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 7, 'ANSWER_LEAK_STRING': 1}
    - [LOW_GROUNDING] form=`(name 'foo.bar)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(name 'foo.bar)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [ANSWER_LEAK_STRING] form=`(name 'foo.bar)` — answer string 'foo.bar' appears in user_msg
    - [LOW_GROUNDING] form=`(name 'clojure.string)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(name 'clojure.string)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(symbol? 'tortoise.race)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G6-02: ns form

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(name 'race.tortoise)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(name 'race.tortoise)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(name 'race.tortoise)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(= 'race.tortoise 'race.tortoise)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(= 'race.tortoise 'race.tortoise)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G6-05: Fully qualified names

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(name :owner/item)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(name :owner/item)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(name :owner/item)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G6-08: Circular dependencies

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(= 'a.b 'a.b)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G6-12: Multiple files in one project

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(count ['race.tortoise 'race.hare 'race.shared])` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(map name ['race.tortoise 'race.hare])` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(map name ['race.tortoise 'race.hare])` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G6-14: Import for host classes

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(symbol? 'java.util.List)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G6-15: Namespace meta

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(:doc (meta '\{:doc "steady wins"\} race))` — answer string 'steady wins' appears in user_msg

## Grade 7

### G7-01: throw

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(try (throw (Exception. "bad")) (catch Exception e` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(try (throw (Exception. "bad")) (catch Exception e` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G7-03: try / finally

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(try (try (/ 1 0) (finally (prn :ran))) (catch Exc` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(try (try (/ 1 0) (finally (prn :ran))) (catch Exc` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(try (try (/ 1 0) (finally (prn :ran))) (catch Exc` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G7-05: nil punning

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 7}
    - [LOW_GROUNDING] form=`(some? nil)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(some? nil)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(some? nil)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(first nil)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(count nil)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(count nil)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G7-09: tap>

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4}
    - [LOW_GROUNDING] form=`(tap> :hello)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(tap> :hello)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(tap> 42)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(tap> 42)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G7-11: Reading stack traces

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'ANSWER_LEAK_STRING': 1}
    - [LOW_GROUNDING] form=`(try (throw (Exception. "oops")) (catch Exception ` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [ANSWER_LEAK_STRING] form=`(try (throw (ex-info "trouble" {})) (catch Excepti` — answer string 'trouble' appears in user_msg
    - [LOW_GROUNDING] form=`(try (throw (ex-info "trouble" {})) (catch Excepti` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G7-12: slurp and spit

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(clojure.string/split "a\nb\nc" #"\n")` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(clojure.string/split "a\nb\nc" #"\n")` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(clojure.string/split "a\nb\nc" #"\n")` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G7-13: line-seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(first (clojure.string/split-lines "first\nsecond"` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(first (clojure.string/split-lines "first\nsecond"` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(first (clojure.string/split-lines "first\nsecond"` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G7-14: with-open

- examples: 1
- variety @ n=50: 0.98
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(with-out-str (println "hare"))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(with-out-str (println "hare"))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G7-15: *in* and *out*

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(with-out-str (println))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(with-out-str (println))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(with-out-str (println))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G7-16: edn read

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G7-17: JSON roundtrip

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

## Grade 8

### G8-02: deftype introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'HIGH_LENGTH': 1}
    - [LOW_GROUNDING] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(do (deftype Stone [weight]) (.-weight (Stone. 7))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(do (deftype Stone [weight]) (.-weight (Stone. 7))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [HIGH_LENGTH] form=`(do (deftype Stone [weight]) (.-weight (Stone. 7))` — user_msg 202 words

### G8-03: defrecord introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — user_msg 207 words

### G8-04: Protocol definition

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (some? Pace)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(do (defprotocol Greet (hail [this])) (some? Greet` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(do (defprotocol Greet (hail [this])) (some? Greet` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(do (defprotocol Greet (hail [this])) (some? Greet` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G8-05: Protocol extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G8-07: Record implementing protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (defrecord T` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G8-08: Multimethod defmulti

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defmulti pace :species) (defmethod pace :hare` — user_msg 209 words

### G8-10: Multimethod vs protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defprotocol Show (show [this])) (extend-proto` — user_msg 203 words

### G8-11: Protocol vs Java interface

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol IPace (run [this])) (extend-proto` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G8-12: extend-type on built-in types

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-type` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-type` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-type` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G8-14: Protocols don't inherit

- examples: 1
- variety @ n=50: 0.98
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg 220 words

### G8-15: derive and isa? — multimethod hierarchy

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(isa? java.lang.Long java.lang.Number)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(isa? java.lang.Long java.lang.Number)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(isa? java.lang.Long java.lang.Number)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(isa? java.lang.String java.lang.Number)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(isa? java.lang.String java.lang.Number)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G8-16: Abstract design with protocols

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'HIGH_LENGTH': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(do (defprotocol Move (step [this])) (defrecord Ha` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(do (defprotocol Sound (cry [this])) (defrecord Ha` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(do (defprotocol Sound (cry [this])) (defrecord Ha` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [HIGH_LENGTH] form=`(do (defprotocol Sound (cry [this])) (defrecord Ha` — user_msg 206 words

## Grade 9

### G9-02: Why state at all

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (def progress (atom :idle)) (reset! progress :` — user_msg 204 words

### G9-08: dosync and alter

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'LOW_GROUNDING': 1}
    - [HIGH_LENGTH] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — user_msg 209 words
    - [LOW_GROUNDING] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G9-15: promise — deliver and deref

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (def p (promise)) (deliver p :done) @p)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G9-16: volatile — when STM is too heavy

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (def v (volatile! 5)) (vreset! v 99) @v)` — user_msg 201 words

### G9-17: binding — thread-local

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — user_msg 208 words

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'HIGH_LENGTH': 2}
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock 42))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [HIGH_LENGTH] form=`(do (def lock (Object.)) (locking lock 42))` — user_msg 202 words
    - [HIGH_LENGTH] form=`(do (def lock (Object.)) (locking lock 42))` — user_msg 208 words

## Grade 10

### G10-01: quote, unquote, unquote-splice

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G10-02: syntax-quote

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(let [xs [1 2 3]] `(list ~@xs))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(let [xs [1 2 3]] `(list ~@xs))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G10-03: defmacro introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'LOW_GROUNDING': 3}
    - [HIGH_LENGTH] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg 207 words
    - [LOW_GROUNDING] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G10-04: Macro expansion rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4}
    - [LOW_GROUNDING] form=`(macroexpand-1 '(when true 1))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(macroexpand-1 '(when true 1))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(macroexpand-1 '(or a b))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(macroexpand-1 '(or a b))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G10-05: macroexpand

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4}
    - [LOW_GROUNDING] form=`(macroexpand '(when true 1))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(macroexpand '(when true 1))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(macroexpand '(-> 1 inc inc))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(macroexpand '(-> 1 inc inc))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G10-06: when and when-not as macros

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(when-not false :ok)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G10-09: Hygiene and gensym

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(symbol? (gensym))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G10-11: Reader macros overview

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6}
    - [LOW_GROUNDING] form=`(#(* % %) 6)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(#(* % %) 6)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(#(* % %) 6)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`[1 #_ 2 3]` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`[1 #_ 2 3]` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`[1 #_ 2 3]` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G10-12: Tagged literals

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 6}
    - [LOW_GROUNDING] form=`(inst? #inst "2024-01-01")` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(inst? #inst "2024-01-01")` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(inst? #inst "2024-01-01")` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(uuid? #uuid "00000000-0000-0000-0000-000000000000` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(uuid? #uuid "00000000-0000-0000-0000-000000000000` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(uuid? #uuid "00000000-0000-0000-0000-000000000000` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G10-13: Data readers and EDN extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G10-14: eval (the function)

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(eval '(+ 1 2 3))` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G10-16: Macro pattern library

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'HIGH_LENGTH': 1}
    - [LOW_GROUNDING] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [HIGH_LENGTH] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — user_msg 210 words

## Grade 11

### G11-06: new and dot-construct

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 6}
    - [LOW_GROUNDING] form=`(String. "go")` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(String. "go")` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(String. "go")` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(new String "jump")` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(new String "jump")` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    - [LOW_GROUNDING] form=`(new String "jump")` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

### G11-08: Type hints

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(let [^String s "abc"] (.toUpperCase s))` — user_msg 205 words

### G11-09: Checked vs unchecked math

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(+ 1 2)` — user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)

## Grade 12

### G12-01: Transducers introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(into [] (map inc) [1 2 3])` — user_msg 203 words

### G12-02: Transducer composition

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — user_msg 213 words

### G12-03: into with a transducer (xform)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(into #{} (map inc) [1 2 3])` — user_msg 203 words

---

## Summary

### Issue counts (across all examples × 3 records)

- **LOW_GROUNDING**: 165
- **HIGH_LENGTH**: 20
- **ANSWER_LEAK_STRING**: 3

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 4 | — |
| 2 | 22 | 88 | 25 | — |
| 3 | 18 | 31 | 3 | — |
| 4 | 20 | 39 | 3 | — |
| 5 | 22 | 39 | 0 | — |
| 6 | 16 | 33 | 22 | — |
| 7 | 18 | 36 | 37 | — |
| 8 | 16 | 31 | 35 | — |
| 9 | 18 | 34 | 10 | — |
| 10 | 16 | 36 | 38 | — |
| 11 | 14 | 29 | 8 | — |
| 12 | 18 | 37 | 3 | — |

### Sample issues by severity

#### LOW_GROUNDING

- `G1-09` (form `(symbol? 'hare)`): user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    ```
    By the time the dew had lifted, the meadow had gathered to watch the strangest race anyone could remember.

"There's a difference between *labeling* the form and
*evaluating* it," Wander the tortoise said. "Quote in any of its
shapes is the labeling — the runtime hands you back the form,
not its val...
    ```
- `G1-09` (form `(= 'hare 'hare)`): user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    ```
    It is one thing to have fast legs and another to know how to use them, as the meadow folk would soon be reminded.

"There's a difference between *labeling* the form and
*evaluating* it," Rhizome the tortoise said. "Quote in any of its
shapes is the labeling — the runtime hands you back the form,
not...
    ```
- `G1-09` (form `(= 'hare 'hare)`): user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    ```
    It happened at the edge of the forest, on a morning when the air was kind to swift feet and steady ones alike.

"There's a difference between *labeling* the form and
*evaluating* it," Grave the tortoise said. "Quote in any of its
shapes is the labeling — the runtime hands you back the form,
not its ...
    ```
- `G1-09` (form `(= 'hare 'hare)`): user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    ```
    Two creatures of very different gait once agreed that the ground between two stones would settle a long argument.

"There's a difference between *labeling* the form and
*evaluating* it," Grain the tortoise said. "Quote in any of its
shapes is the labeling — the runtime hands you back the form,
not i...
    ```
- `G2-08` (form `(+ 1/2 1/4)`): user_msg lacks both a drawn-value reference (any literal from the form) and any archetype-EMO phrase — emotional/concrete grounding is insufficient (Cat-J)
    ```
    Whiskling the hare liked to talk; Stoneheart the tortoise liked to listen, and the rivalry between them had grown into a small legend along the road.

"Whatever the heap looks like after the operation,"
Stoneheart the tortoise said, "the runtime gives the exact count —
small or large, fraction or wh...
    ```

#### HIGH_LENGTH

- `G3-10` (form `(#(+ % 1) 5)`): user_msg 205 words
    ```
    Among the small kingdoms of the meadow, swiftness was a kind of currency, and one creature spent it loudly.

Mossback was in a hurry at the roadside and had no time to write a full recipe card. She scratched a quick shorthand mark — `#(+ % 1)` — on a stone and put 5 acorns in front of it immediately...
    ```
- `G3-13` (form `((fn [x] x x x 99) 1)`): user_msg 201 words
    ```
    By the time the dew had lifted, the meadow had gathered to watch the strangest race anyone could remember.

Mossback's recipe card for this stretch listed several intermediate steps, but the cook only served the final dish — everything before it was preparation, not what got plated.

The kitchen nee...
    ```
- `G8-02` (form `(do (deftype Stone [weight]) (.-weight (Stone. 7)))`): user_msg 202 words
    ```
    It is one thing to have fast legs and another to know how to use them, as the meadow folk would soon be reminded.

Pip the hare found a smooth stone on the path and wanted to record its weight in a bare carrying-case. Mossback showed him that `deftype` could shape a case with a single weight slot — ...
    ```
- `G8-03` (form `(do (defrecord Runner [name pace]) (:pace (->Runner "Alice" `): user_msg 207 words
    ```
    Galop announced the race in a voice loud enough to wake the owls, and Fen accepted with a nod.

Mossback the tortoise was outfitting the meadow's runners with carrying-cases — small wooden cases with two named compartments inside, one labeled `name` and one labeled `pace`. The case-stamp on the outs...
    ```
- `G8-08` (form `(do (defmulti pace :species) (defmethod pace :hare [_] :swif`): user_msg 209 words
    ```
    Among the small kingdoms of the meadow, swiftness was a kind of currency, and one creature spent it loudly.

Mossback the tortoise set up a sorting-table at the edge of the meadow. Runners would walk up; the table would read each runner's :species stamp and route them to the matching arm.

Today's f...
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

