# crow-pitcher curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

### G1-15: Equality

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(= 1 1 1 1)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

## Grade 2

### G2-03: not= and = with multiple args

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(not= 1 1)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G2-13: and / or — short circuit, return values

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4}
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(or false false)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G2-14: not — turning truthy to false

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4}
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(not false)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(not nil)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G2-16: Truthy 0 and empty string

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(boolean 0)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(boolean false)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(boolean false)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G2-18: Quoting symbols

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(= (quote tortoise) 'tortoise)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(= (quote tortoise) 'tortoise)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

## Grade 3

### G3-13: fn body returns last form

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`((fn [x] x x x 99) 1)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`((fn [x] x x x 99) 1)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G3-18: When to name vs inline

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'FORM_LEAK': 1}
    - [HIGH_LENGTH] form=`(let [n 5] (* n n n))` — user_msg 205 words
    - [FORM_LEAK] form=`(* 5 5 5)` — form '(* 5 5 5)' appears in user_msg of a goal-style subject

## Grade 4

### G4-01: Vector literal

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`["a" "b"]` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G4-19: range and seq

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(count (range 5))` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(count (range 5))` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(count (range 5))` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

## Grade 5

### G5-01: if

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(if true :a :b)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G5-22: recur — first taste

- examples: 1
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 2, 'BAD_PLACE_PREP': 2}
    - [ANSWER_LEAK] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — answer 120 in narrative
    - [BAD_PLACE_PREP] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — 'in the hilltop' (wrong preposition)
    - [ANSWER_LEAK] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — answer 120 in narrative
    - [BAD_PLACE_PREP] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — 'in the hilltop' (wrong preposition)

## Grade 6

### G6-01: Namespace as file

- examples: 3
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1, 'LOW_GROUNDING': 2}
    - [ANSWER_LEAK_STRING] form=`(name 'foo.bar)` — answer string 'foo.bar' appears in user_msg
    - [LOW_GROUNDING] form=`(name 'foo.bar)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(symbol? 'tortoise.race)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G6-02: ns form

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(name 'race.tortoise)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G6-05: Fully qualified names

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(name :owner/item)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G6-08: Circular dependencies

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(= 'a.b 'a.b)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G6-09: Loading order

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G6-11: Classpath

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(clojure.string/split "src:test" #":")` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(count ["src" "test" "resources"])` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G6-12: Multiple files in one project

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(count ['race.tortoise 'race.hare 'race.shared])` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(count ['race.tortoise 'race.hare 'race.shared])` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(map name ['race.tortoise 'race.hare])` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G6-14: Import for host classes

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(symbol? 'java.util.List)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(symbol? 'java.util.List)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(name 'java.util.Map)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G6-16: Cleaning up requires

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.set)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

## Grade 7

### G7-01: throw

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(try (throw (Exception. "bad")) (catch Exception e` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G7-04: ex-info

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(try (throw (ex-info "x" {:k :v})) (catch Exceptio` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G7-05: nil punning

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(some? 0)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(first nil)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(first nil)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(count nil)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(count nil)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G7-06: pre and post conditions

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exce` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G7-07: assert

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (assert (= 1 1)) 1)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G7-09: tap>

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(tap> 42)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(tap> 42)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(tap> 42)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G7-11: Reading stack traces

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(try (throw (ex-info "trouble" {})) (catch Excepti` — answer string 'trouble' appears in user_msg

### G7-13: line-seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4}
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(first (clojure.string/split-lines "alpha\nbeta"))` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G7-14: with-open

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(with-out-str (println "hare"))` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(with-out-str (println "hare"))` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G7-15: *in* and *out*

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(with-out-str (println))` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(with-out-str (println))` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G7-16: edn read

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "{:a 1}")` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "{:a 1}")` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "[:hare :tortoise]")` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G7-17: JSON roundtrip

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

## Grade 8

### G8-03: defrecord introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — answer string ':slow' appears in user_msg

### G8-06: Protocol method dispatch

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G8-13: this-style vs fn-style

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(do (defprotocol Named (name-of [this])) (defrecor` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G8-14: Protocols don't inherit

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G8-15: derive and isa? — multimethod hierarchy

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(isa? java.lang.Long java.lang.Number)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(isa? java.lang.String java.lang.Number)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G8-16: Abstract design with protocols

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol Sound (cry [this])) (defrecord Ha` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

## Grade 9

### G9-03: Atom introduction

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G9-07: Ref introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_PREP': 1, 'LOW_GROUNDING': 1}
    - [DOUBLE_PREP] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — verb+preposition followed by {place} which already carries its own preposition
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G9-09: Ref vs atom

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G9-10: Agent introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G9-11: send and send-off

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send-off ag inc) (await ag` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'DOUBLE_PREP': 2}
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [DOUBLE_PREP] form=`(do (def lock (Object.)) (locking lock 42))` — verb+preposition followed by {place} which already carries its own preposition
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock 42))` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [DOUBLE_PREP] form=`(do (def lock (Object.)) (locking lock 42))` — verb+preposition followed by {place} which already carries its own preposition

## Grade 10

### G10-01: quote, unquote, unquote-splice

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G10-03: defmacro introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg 221 words

### G10-04: Macro expansion rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(macroexpand-1 '(or a b))` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(macroexpand '(-> x f g))` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G10-09: Hygiene and gensym

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G10-11: Reader macros overview

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`[1 #_ 2 3]` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`[1 #_ 2 3]` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G10-12: Tagged literals

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(inst? #inst "2024-01-01")` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G10-13: Data readers and EDN extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "[:a :b :c]")` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G10-14: eval (the function)

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(eval '(+ 1 2 3))` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(eval '(+ 1 2 3))` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(eval (list '+ 4 5))` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

### G10-16: Macro pattern library

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [LOW_GROUNDING] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding

## Grade 11

### G11-06: new and dot-construct

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'ANSWER_LEAK_STRING': 1}
    - [LOW_GROUNDING] form=`(String. "go")` — user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    - [ANSWER_LEAK_STRING] form=`(new String "jump")` — answer string 'jump' appears in user_msg

## Grade 12

### G12-03: into with a transducer (xform)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(into #{} (map inc) [1 2 3])` — user_msg 206 words

---

## Summary

### Issue counts (across all examples × 3 records)

- **LOW_GROUNDING**: 100
- **ANSWER_LEAK_STRING**: 4
- **HIGH_LENGTH**: 3
- **DOUBLE_PREP**: 3
- **ANSWER_LEAK**: 2
- **BAD_PLACE_PREP**: 2
- **FORM_LEAK**: 1

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 1 | — |
| 2 | 22 | 88 | 17 | — |
| 3 | 18 | 31 | 4 | — |
| 4 | 20 | 39 | 4 | — |
| 5 | 22 | 39 | 5 | — |
| 6 | 16 | 33 | 17 | — |
| 7 | 18 | 36 | 27 | — |
| 8 | 16 | 31 | 8 | — |
| 9 | 18 | 34 | 13 | — |
| 10 | 16 | 36 | 16 | — |
| 11 | 14 | 29 | 2 | — |
| 12 | 18 | 37 | 1 | — |

### Sample issues by severity

#### LOW_GROUNDING

- `G1-15` (form `(= 1 1 1 1)`): user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    ```
    in the orchard, a single pitcher held the last of the water, and Updraft the crow arrived too parched to be picky.

Sable lined up four single stones at the garden pitcher's dual-gate check, each carrying the count one, presenting all four to the gate at the same time.

Sable needed the gate to conf...
    ```
- `G2-03` (form `(not= 1 1)`): user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    ```
    on the farm, where the orchard meets the well, an old clay pitcher had stood for as long as anyone could remember.

Korvus placed two identical stones side by side on the pitcher's rim at the garden — both carrying the count one. He wondered if the pitcher would call them unequal.

He needed to veri...
    ```
- `G2-13` (form `(and true true)`): user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    ```
    On the rim of a long-shadowed pitcher, a thirsty bird considered what it had and what it lacked.

Korvus stood at the pitcher's mouth on the road, two gate-arms stretched across it. Both arms were raised open. He needed to know whether the path through both gates was clear.

He needed the final verd...
    ```
- `G2-13` (form `(and true true)`): user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    ```
    In a year when the wells ran low, a single jar of water was a small kingdom unto itself.

Korvus stood at the pitcher's mouth on the road, two gate-arms stretched across it. Both arms were raised open. He needed to know whether the path through both gates was clear.

He needed the final verdict only...
    ```
- `G2-13` (form `(and true true)`): user_msg lacks both drawn-value reference and EMO-pool phrasing — flat narrative grounding
    ```
    A row of pebbles lay at the foot of the wall, sun-warmed, unremarkable, and just heavy enough.

Windrider the crow paused at the pitcher's rim by the garden, talon raised.
"Boolean forms in Clojure are like a dual-gate check at the pitcher's
mouth," she said. "The runtime checks the value and the
ga...
    ```

#### HIGH_LENGTH

- `G3-18` (form `(let [n 5] (* n n n))`): user_msg 205 words
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

Onyxwing the crow spread a patch of soft moss beneath the pitcher at the market.
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

