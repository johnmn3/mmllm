# ant-grasshopper curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

### G1-01: Eval as substitution

- examples: 8
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 3}
    - [FOREIGN_FABLE_IMAGERY] form=`0` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`(* 4 5)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`(- 10 (+ 2 3))` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G1-02: Integer numbers

- examples: 6
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`-25` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`-25` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G1-04: Strings

- examples: 5
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`"slow and steady"` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`""` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G1-05: Booleans

- examples: 6
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(< 3 5)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G1-06: nil

- examples: 5
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(nil? 0)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G1-07: Keywords

- examples: 5
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 4}
    - [FOREIGN_FABLE_IMAGERY] form=`:ant` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`(keyword? :ant)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`(keyword? :ant)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`(= :ant :ant)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G1-09: Symbols vs values

- examples: 4
- variety @ n=50: 0.99
- issues: {'FOREIGN_FABLE_IMAGERY': 3}
    - [FOREIGN_FABLE_IMAGERY] form=`'ant` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`(= 'ant 'ant)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`(= 'ant 'ant)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G1-11: Whitespace doesn't matter

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`(+
  1
  2)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`(+
  1
  2)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G1-12: Parens group; they don't multiply

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(+ 2 3)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G1-13: First arithmetic call

- examples: 6
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 3}
    - [FOREIGN_FABLE_IMAGERY] form=`(* 4 5)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`(* 4 5)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`(/ 10 2)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G1-14: Nested call evaluation

- examples: 4
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(+ 1 (* 2 3))` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G1-15: Equality

- examples: 6
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`(= :ant :ant)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`(= 1 1 1 1)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

## Grade 2

### G2-03: not= and = with multiple args

- examples: 4
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(not= 1 1)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G2-04: min and max

- examples: 4
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(min 5 -2 0 9)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G2-07: abs (absolute value)

- examples: 3
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(Math/abs 9)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G2-08: Arithmetic on ratios

- examples: 3
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 3}
    - [FOREIGN_FABLE_IMAGERY] form=`(+ 1/2 1/4)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`(* 2/3 3/4)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`(- 1 1/3)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G2-13: and / or — short-circuit and value

- examples: 4
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`(or nil false)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`(or nil false)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G2-14: not — turning truthy to false

- examples: 4
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(not 0)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G2-15: Falsey values

- examples: 4
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(boolean "")` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G2-16: Coercion pitfalls in if

- examples: 3
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(if nil :a :b)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G2-17: Keyword as function

- examples: 4
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`(:missing {:a 1})` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`(:missing {:a 1} :default)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G2-21: rand and rand-int

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(let [r (rand-int 10)] (and (>= r 0) (< r 10)))` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

## Grade 3

### G3-03: let — local binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(let [n 10] (* n n))` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G3-08: fn — multi-arg

- examples: 1
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`((fn [a b c] (+ a b c)) 1 2 3)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

## Grade 4

### G4-03: conj — append to vector

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(conj [] :ant)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G4-08: assoc — map update

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(assoc {:a 1} :b 2)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G4-12: Set membership

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(contains? #{1 2 3} 4)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G4-13: count — universal

- examples: 4
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(count "grasshopper")` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G4-14: empty?

- examples: 3
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(empty? "")` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

## Grade 5

### G5-03: when

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(when false :yes)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G5-08: not

- examples: 1
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(not (> 1 2))` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G5-12: reduce

- examples: 3
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`(reduce * [1 2 3 4 5])` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`(reduce max [3 1 4 1 5 9 2 6])` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G5-21: distinct and sort

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(sort [3 1 2])` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

## Grade 6

### G6-03: require

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(clojure.string/lower-case "GRASSHOPPER")` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G6-08: Circular dependencies

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(clojure.string/upper-case "a")` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G6-12: Multiple files in one project

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(map name ['meadow.ant 'meadow.grasshopper])` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

## Grade 7

### G7-03: try / finally

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(try (try (/ 1 0) (finally :ran)) (catch Exception` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G7-12: slurp and spit

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(count "grasshopper\nant\n")` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G7-18: Shell command

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(:cmd {:cmd "ls" :args ["-l"]})` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

## Grade 8

### G8-03: defrecord introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do (defrecord Runner [name pace]) (:name (->Runne` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G8-08: Multimethod defmulti

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do (defmulti pace :species) (defmethod pace :gras` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G8-12: extend-type on built-in types

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do (defprotocol Pace (speed [this])) (extend-type` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G8-15: derive and isa? — multimethod hierarchy

- examples: 3
- variety @ n=50: 1.00
- issues: {'PREDICATE_QUESTION_COLLISION': 1}
    - [PREDICATE_QUESTION_COLLISION] form=`(do (derive ::grasshopper ::runner) (isa? ::grassh` — predicate-suffix ``?`` collides with the question framing's trailing ``?`` or ``.``

## Grade 9

### G9-03: Atom introduction

- examples: 3
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do (def a (atom 10)) (swap! a + 5) @a)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G9-08: dosync and alter

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G9-17: binding — thread-local

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

## Grade 10

### G10-02: syntax-quote

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`(let [x 10] `(+ ~x ~x))` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`(let [x 10] `(+ ~x ~x))` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G10-03: defmacro introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G10-05: macroexpand

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(macroexpand '(-> 1 inc inc))` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G10-06: when and when-not as macros

- examples: 3
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(when false 1 2 3)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(-> 5 inc inc inc)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G10-10: Anaphoric macros are confusing

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`(if-let [x 7] (* x x) 0)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`(if-let [x 7] (* x x) 0)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G10-11: Reader macros overview

- examples: 3
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(#(* % %) 6)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G10-12: Tagged literals

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(uuid? #uuid "00000000-0000-0000-0000-000000000000` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G10-13: Data readers and EDN extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(clojure.edn/read-string "42")` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G10-15: When not to write a macro

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "prefer fn unless you must shape syntax" (map ` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

## Grade 11

### G11-02: Method call syntax

- examples: 3
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 3}
    - [FOREIGN_FABLE_IMAGERY] form=`(.toUpperCase "abc")` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`(.toUpperCase "abc")` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`(. "abc" toUpperCase)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G11-03: Static method call

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(Math/abs -7)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G11-05: Import form

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "import is a top-of-file ns clause" :studied)` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G11-06: new and dot-construct

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(new String "world")` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G11-07: Arrays

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(let [a (int-array [10 20 30])] (aget a 1))` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G11-10: ClojureScript overview

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "cljs runs in browsers and Node, with JS inter` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do "cljs runs in browsers and Node, with JS inter` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G11-11: cljs / JavaScript interop

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "js/<name> namespaces JS globals; .- prefix ma` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G11-13: Cross-platform .cljc and reader-conditionals

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "#?(:clj … :cljs …) selects a form per host at` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

## Grade 12

### G12-02: Transducer composition

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G12-03: into with a transducer (xform)

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(into #{} (map inc) [1 2 3])` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G12-05: Channels and pipelines

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "pipelines transform streams of values channel` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G12-06: clojure.spec

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G12-07: Spec generators

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "s/exercise produces sample inputs for a spec"` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G12-10: Property-based testing

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "test.check generates inputs and checks proper` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    - [FOREIGN_FABLE_IMAGERY] form=`(do "test.check generates inputs and checks proper` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G12-11: Leiningen project.clj

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "Leiningen reads project.clj at the project ro` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G12-13: Aliases and tools

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "`clj -M:test` runs the :test alias from deps.` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

### G12-15: Datomic / XTDB (datalog db brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "queries are written in datalog over EDN-shape` — tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose

---

## Summary

### Issue counts (across all examples × 3 records)

- **FOREIGN_FABLE_IMAGERY**: 97
- **PREDICATE_QUESTION_COLLISION**: 1

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 80 | 25 | — |
| 2 | 22 | 77 | 14 | — |
| 3 | 18 | 31 | 2 | — |
| 4 | 20 | 39 | 5 | — |
| 5 | 22 | 39 | 5 | — |
| 6 | 16 | 33 | 3 | — |
| 7 | 18 | 36 | 3 | — |
| 8 | 16 | 31 | 4 | — |
| 9 | 18 | 34 | 3 | — |
| 10 | 16 | 36 | 12 | — |
| 11 | 14 | 29 | 11 | — |
| 12 | 18 | 37 | 11 | — |

### Sample issues by severity

#### FOREIGN_FABLE_IMAGERY

- `G1-01` (form `0`): tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    ```
    Two creatures of the meadow approached the coming winter very differently.

Toc the ant had been keeping a small leather notebook of every form
she had successfully evaluated. Today by the garden, the next entry
was the value 0. Chirp the grasshopper peered over
her shoulder at the form `0` and aske...
    ```
- `G1-01` (form `(* 4 5)`): tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    ```
    Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Bit the ant had been keeping a small leather notebook of every form
they had successfully evaluated. Today at the edge of the orchard, the next entry
was the form (* 4 5). Skip the grasshop...
    ```
- `G1-01` (form `(- 10 (+ 2 3))`): tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    ```
    Two creatures of the meadow approached the coming winter very differently.

Tic the ant had been keeping a small leather notebook of every form
he had successfully evaluated. Today in the woods, the next entry
was the nested form (- 10 (+ 2 3)). Chirp the grasshopper peered over
his shoulder at the ...
    ```
- `G1-02` (form `-25`): tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    ```
    Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. This was in the garden.

Tic the ant had been keeping a small leather notebook of every form
he had successfully evaluated. Today by the garden, the next entry
was the integer -25. Skip the ...
    ```
- `G1-02` (form `-25`): tortoise-hare-specific imagery 'leather notebook' leaks into ant-grasshopper prose
    ```
    Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Toc the ant had been keeping a small leather notebook of every form
she had successfully evaluated. Today at the edge of the woods, the next entry
was the integer -25. Skip the grasshopper ...
    ```

#### PREDICATE_QUESTION_COLLISION

- `G8-15` (form `(do (derive ::grasshopper ::runner) (isa? ::grasshopper ::ru`): predicate-suffix ``?`` collides with the question framing's trailing ``?`` or ``.``
    ```
    Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. This was in the meadow.

Bit the ant had been trying to teach Skip the grasshopper how the REPL
works. "Look here," they said, pointing to deriving ::grasshopper from ::runner and asking isa...
    ```

