# goose-eggs curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

### G1-01: Eval as substitution

- examples: 8
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`42` — 'in the farm' (wrong preposition)

### G1-02: Integer numbers

- examples: 6
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`7` — 'in the farm' (wrong preposition)

### G1-03: Ratios

- examples: 5
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(+ 1/2 1/4)` — 'in the farm' (wrong preposition)

### G1-04: Strings

- examples: 5
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`"golden egg"` — 'in the farm' (wrong preposition)

### G1-05: Booleans

- examples: 6
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(> 3 5)` — 'in the farm' (wrong preposition)

### G1-06: nil

- examples: 5
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`nil` — 'in the farm' (wrong preposition)

### G1-07: Keywords

- examples: 5
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`:gold` — 'in the farm' (wrong preposition)

### G1-08: Characters

- examples: 4
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(char? \g)` — 'in the farm' (wrong preposition)

### G1-09: Symbols vs values

- examples: 4
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(symbol? 'goose)` — 'in the farm' (wrong preposition)

### G1-15: Equality

- examples: 6
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(= 1 1 1 1)` — 'in the farm' (wrong preposition)

### G1-18: Errors are safe in the REPL

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(* 7 6)` — 'in the farm' (wrong preposition)

## Grade 2

### G2-01: Multi-arg arithmetic

- examples: 6
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(+ 1 2 3 4)` — 'in the farm' (wrong preposition)

### G2-02: Comparison chains

- examples: 5
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(< 1 2 3)` — 'in the farm' (wrong preposition)

### G2-03: not= and = with multiple args

- examples: 5
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 2}
    - [BAD_PLACE_PREP] form=`(= 1 1 1)` — 'in the farm' (wrong preposition)
    - [BAD_PLACE_PREP] form=`(= 1 1 2)` — 'in the farm' (wrong preposition)

### G2-05: quot, rem, mod

- examples: 6
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(mod -7 3)` — 'in the farm' (wrong preposition)

### G2-06: inc and dec

- examples: 5
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(inc 5)` — 'in the farm' (wrong preposition)

### G2-07: Absolute value

- examples: 4
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 2}
    - [BAD_PLACE_PREP] form=`(abs 0)` — 'in the farm' (wrong preposition)
    - [BAD_PLACE_PREP] form=`(abs (- 3 8))` — 'in the farm' (wrong preposition)

### G2-09: Floats vs ints (the / operator)

- examples: 3
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(/ 10 2)` — 'in the farm' (wrong preposition)

### G2-11: String concatenation with str

- examples: 4
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(str "x" "y" "z")` — 'in the farm' (wrong preposition)

### G2-13: and / or — short circuit, return values

- examples: 6
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(or false true)` — 'in the farm' (wrong preposition)

### G2-16: Truthy 0 and empty string

- examples: 4
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(boolean nil)` — 'in the farm' (wrong preposition)

### G2-18: Quoting symbols

- examples: 3
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`'tortoise` — 'in the farm' (wrong preposition)

### G2-19: Auto-promotion to bigint

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(* 1000000 1000000)` — 'in the farm' (wrong preposition)

## Grade 3

### G3-01: def — top-level binding

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(do (def x 42) x)` — 'in the farm' (wrong preposition)

### G3-02: def — redefinition

- examples: 1
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(do (def x 1) (def x 99) x)` — 'in the farm' (wrong preposition)

### G3-03: let — local binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(let [a 5] a)` — 'in the farm' (wrong preposition)

### G3-06: let — binding can reference prior

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(let [a 5 b (* a 2)] b)` — 'in the farm' (wrong preposition)

### G3-09: defn — shorthand

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(do (defn dbl [x] (* x 2)) (dbl 5))` — 'in the farm' (wrong preposition)

### G3-18: When to name vs inline

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(* 5 5 5)` — 'in the farm' (wrong preposition)

## Grade 4

### G4-01: Vector literal

- examples: 3
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`[1 2 3]` — 'in the farm' (wrong preposition)

### G4-02: nth — vector access

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(nth [10 20 30] 0)` — 'in the farm' (wrong preposition)

### G4-04: List literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'UNCLOSED_DIALOGUE_QUOTE': 1}
    - [UNCLOSED_DIALOGUE_QUOTE] form=`'()` — user_msg has an odd number of dialogue quotes (subplot opened a `"` but did not close it)

### G4-06: Map literal

- examples: 1
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`{:hare 1 :tortoise 2}` — 'in the farm' (wrong preposition)

### G4-09: dissoc — map remove key

- examples: 1
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(dissoc {:a 1 :b 2} :a)` — 'in the farm' (wrong preposition)

### G4-11: Set literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'ASIDE_PAREN': 3}
    - [ASIDE_PAREN] form=`(count #{1 1 1})` — concept_phrase has pedagogical-aside parenthetical
    - [ASIDE_PAREN] form=`(count #{1 1 1})` — concept_phrase has pedagogical-aside parenthetical
    - [ASIDE_PAREN] form=`(count #{1 1 1})` — concept_phrase has pedagogical-aside parenthetical

### G4-13: count — universal

- examples: 4
- variety @ n=50: 1.00
- issues: {'UNCLOSED_DIALOGUE_QUOTE': 1, 'BAD_PLACE_PREP': 1}
    - [UNCLOSED_DIALOGUE_QUOTE] form=`(count {:a 1 :b 2})` — user_msg has an odd number of dialogue quotes (subplot opened a `"` but did not close it)
    - [BAD_PLACE_PREP] form=`(count #{:a :b :c})` — 'in the farm' (wrong preposition)

### G4-14: empty?

- examples: 3
- variety @ n=50: 1.00
- issues: {'UNCLOSED_DIALOGUE_QUOTE': 1}
    - [UNCLOSED_DIALOGUE_QUOTE] form=`(empty? "")` — user_msg has an odd number of dialogue quotes (subplot opened a `"` but did not close it)

### G4-15: first, rest, last

- examples: 3
- variety @ n=50: 1.00
- issues: {'ASIDE_PAREN': 3}
    - [ASIDE_PAREN] form=`(count (rest [10 20 30]))` — concept_phrase has pedagogical-aside parenthetical
    - [ASIDE_PAREN] form=`(count (rest [10 20 30]))` — concept_phrase has pedagogical-aside parenthetical
    - [ASIDE_PAREN] form=`(count (rest [10 20 30]))` — concept_phrase has pedagogical-aside parenthetical

### G4-19: range and seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1, 'UNCLOSED_DIALOGUE_QUOTE': 1}
    - [BAD_PLACE_PREP] form=`(count (range 5))` — 'in the farm' (wrong preposition)
    - [UNCLOSED_DIALOGUE_QUOTE] form=`(first (range 1 100))` — user_msg has an odd number of dialogue quotes (subplot opened a `"` but did not close it)

## Grade 5

### G5-01: if

- examples: 3
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(if true :a :b)` — 'in the farm' (wrong preposition)

### G5-02: if as expression

- examples: 1
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(+ 1 (if true 10 20))` — 'in the farm' (wrong preposition)

### G5-06: case

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(case 2 1 :one 2 :two 3 :three :default)` — 'in the farm' (wrong preposition)

### G5-09: fn as value

- examples: 1
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`((fn [f x] (f (f x))) inc 5)` — 'in the farm' (wrong preposition)

### G5-18: some

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(some neg? [1 2 3])` — 'in the farm' (wrong preposition)

### G5-19: every?

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(every? pos? [1 2 3])` — 'in the farm' (wrong preposition)

## Grade 6

### G6-01: Namespace as file

- examples: 3
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(name 'foo.bar)` — 'in the farm' (wrong preposition)

### G6-02: ns form

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(name 'race.tortoise)` — 'in the farm' (wrong preposition)

### G6-06: Private defs

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1, 'ASIDE_PAREN': 3, 'WHICH_IS_LEAK': 3}
    - [BAD_PLACE_PREP] form=`(:private (meta '^:private x))` — 'in the farm' (wrong preposition)
    - [ASIDE_PAREN] form=`(:private (meta 'x))` — concept_phrase has pedagogical-aside parenthetical
    - [WHICH_IS_LEAK] form=`(:private (meta 'x))` — question_what '..., which is X' leaks the answer in narrative
    - [ASIDE_PAREN] form=`(:private (meta 'x))` — concept_phrase has pedagogical-aside parenthetical
    - [WHICH_IS_LEAK] form=`(:private (meta 'x))` — question_what '..., which is X' leaks the answer in narrative
    - [ASIDE_PAREN] form=`(:private (meta 'x))` — concept_phrase has pedagogical-aside parenthetical

### G6-09: Loading order

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — 'in the farm' (wrong preposition)

## Grade 7

### G7-01: throw

- examples: 1
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(try (throw (Exception. "bad")) (catch Exception e` — 'in the farm' (wrong preposition)

### G7-02: try / catch

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(try (/ 1 0) (catch Exception e :caught))` — 'in the farm' (wrong preposition)

### G7-03: try / finally

- examples: 2
- variety @ n=50: 1.00
- issues: {'ASIDE_PAREN': 3}
    - [ASIDE_PAREN] form=`(try 7 (finally :cleanup))` — question_what has pedagogical-aside parenthetical
    - [ASIDE_PAREN] form=`(try 7 (finally :cleanup))` — question_what has pedagogical-aside parenthetical
    - [ASIDE_PAREN] form=`(try 7 (finally :cleanup))` — question_what has pedagogical-aside parenthetical

### G7-05: nil punning

- examples: 4
- variety @ n=50: 1.00
- issues: {'EMDASH_COMMENTARY': 3, 'WHICH_IS_LEAK': 6, 'LOWERCASE_AFTER_PERIOD': 2}
    - [EMDASH_COMMENTARY] form=`(some? 0)` — concept_phrase or question_what has em-dash commentary
    - [EMDASH_COMMENTARY] form=`(some? 0)` — concept_phrase or question_what has em-dash commentary
    - [EMDASH_COMMENTARY] form=`(some? 0)` — concept_phrase or question_what has em-dash commentary
    - [WHICH_IS_LEAK] form=`(first nil)` — question_what '..., which is X' leaks the answer in narrative
    - [WHICH_IS_LEAK] form=`(first nil)` — question_what '..., which is X' leaks the answer in narrative
    - [LOWERCASE_AFTER_PERIOD] form=`(first nil)` — subplot template starts a sentence with a lowercase {place} phrase (period followed by 'in the X' / 'on the Y' / etc.)

### G7-06: pre and post conditions

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — 'in the farm' (wrong preposition)

### G7-09: tap>

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1, 'ASIDE_PAREN': 3, 'LOWERCASE_AFTER_PERIOD': 1}
    - [BAD_PLACE_PREP] form=`(tap> :hello)` — 'in the farm' (wrong preposition)
    - [ASIDE_PAREN] form=`(tap> 42)` — question_what has pedagogical-aside parenthetical
    - [ASIDE_PAREN] form=`(tap> 42)` — question_what has pedagogical-aside parenthetical
    - [ASIDE_PAREN] form=`(tap> 42)` — question_what has pedagogical-aside parenthetical
    - [LOWERCASE_AFTER_PERIOD] form=`(tap> 42)` — subplot template starts a sentence with a lowercase {place} phrase (period followed by 'in the X' / 'on the Y' / etc.)

### G7-10: doc and source

- examples: 1
- variety @ n=50: 1.00
- issues: {'EMDASH_COMMENTARY': 3, 'LOWERCASE_AFTER_PERIOD': 1}
    - [EMDASH_COMMENTARY] form=`(:doc (meta '^{:doc "adds two"} plus))` — concept_phrase or question_what has em-dash commentary
    - [EMDASH_COMMENTARY] form=`(:doc (meta '^{:doc "adds two"} plus))` — concept_phrase or question_what has em-dash commentary
    - [LOWERCASE_AFTER_PERIOD] form=`(:doc (meta '^{:doc "adds two"} plus))` — subplot template starts a sentence with a lowercase {place} phrase (period followed by 'in the X' / 'on the Y' / etc.)
    - [EMDASH_COMMENTARY] form=`(:doc (meta '^{:doc "adds two"} plus))` — concept_phrase or question_what has em-dash commentary

### G7-12: slurp and spit

- examples: 2
- variety @ n=50: 1.00
- issues: {'ASIDE_PAREN': 3}
    - [ASIDE_PAREN] form=`(count "hare\ntortoise\n")` — concept_phrase has pedagogical-aside parenthetical
    - [ASIDE_PAREN] form=`(count "hare\ntortoise\n")` — concept_phrase has pedagogical-aside parenthetical
    - [ASIDE_PAREN] form=`(count "hare\ntortoise\n")` — concept_phrase has pedagogical-aside parenthetical

### G7-13: line-seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOWERCASE_AFTER_PERIOD': 2}
    - [LOWERCASE_AFTER_PERIOD] form=`(count (clojure.string/split-lines "a\nb\nc"))` — subplot template starts a sentence with a lowercase {place} phrase (period followed by 'in the X' / 'on the Y' / etc.)
    - [LOWERCASE_AFTER_PERIOD] form=`(count (clojure.string/split-lines "a\nb\nc"))` — subplot template starts a sentence with a lowercase {place} phrase (period followed by 'in the X' / 'on the Y' / etc.)

### G7-15: *in* and *out*

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOWERCASE_AFTER_PERIOD': 1}
    - [LOWERCASE_AFTER_PERIOD] form=`(with-out-str (println))` — subplot template starts a sentence with a lowercase {place} phrase (period followed by 'in the X' / 'on the Y' / etc.)

### G7-16: edn read

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOWERCASE_AFTER_PERIOD': 1, 'BAD_PLACE_PREP': 1}
    - [LOWERCASE_AFTER_PERIOD] form=`(clojure.edn/read-string "[:hare :tortoise]")` — subplot template starts a sentence with a lowercase {place} phrase (period followed by 'in the X' / 'on the Y' / etc.)
    - [BAD_PLACE_PREP] form=`(clojure.edn/read-string "[:hare :tortoise]")` — 'in the farm' (wrong preposition)

### G7-17: JSON roundtrip

- examples: 2
- variety @ n=50: 1.00
- issues: {'ASIDE_PAREN': 3}
    - [ASIDE_PAREN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — concept_phrase has pedagogical-aside parenthetical
    - [ASIDE_PAREN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — concept_phrase has pedagogical-aside parenthetical
    - [ASIDE_PAREN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — concept_phrase has pedagogical-aside parenthetical

### G7-18: Shell command

- examples: 2
- variety @ n=50: 1.00
- issues: {'WHICH_IS_LEAK': 3, 'BAD_PLACE_PREP': 1}
    - [WHICH_IS_LEAK] form=`(count (:args {:cmd "echo" :args ["hello" "world"]` — question_what '..., which is X' leaks the answer in narrative
    - [BAD_PLACE_PREP] form=`(count (:args {:cmd "echo" :args ["hello" "world"]` — 'in the farm' (wrong preposition)
    - [WHICH_IS_LEAK] form=`(count (:args {:cmd "echo" :args ["hello" "world"]` — question_what '..., which is X' leaks the answer in narrative
    - [WHICH_IS_LEAK] form=`(count (:args {:cmd "echo" :args ["hello" "world"]` — question_what '..., which is X' leaks the answer in narrative

## Grade 8

### G8-01: Why polymorphism

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — 'in the farm' (wrong preposition)

### G8-02: deftype introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — 'in the farm' (wrong preposition)

### G8-06: Protocol method dispatch

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — 'in the farm' (wrong preposition)

## Grade 9

### G9-01: Immutability as default — review

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(let [m {:a 1}] (assoc m :b 2) m)` — 'in the farm' (wrong preposition)

### G9-02: Why state at all

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — 'in the farm' (wrong preposition)

### G9-03: Atom introduction

- examples: 3
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(do (def a (atom :start)) (reset! a :done) @a)` — 'in the farm' (wrong preposition)

### G9-04: Atom CAS semantics

- examples: 2
- variety @ n=50: 1.00
- issues: {'ASIDE_PAREN': 3}
    - [ASIDE_PAREN] form=`(do (def a (atom 5)) (compare-and-set! a 0 99) @a)` — concept_phrase has pedagogical-aside parenthetical
    - [ASIDE_PAREN] form=`(do (def a (atom 5)) (compare-and-set! a 0 99) @a)` — concept_phrase has pedagogical-aside parenthetical
    - [ASIDE_PAREN] form=`(do (def a (atom 5)) (compare-and-set! a 0 99) @a)` — concept_phrase has pedagogical-aside parenthetical

### G9-06: Validator on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — 'in the farm' (wrong preposition)

### G9-09: Ref vs atom

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(do (def a (atom 0)) (swap! a inc) @a)` — 'in the farm' (wrong preposition)

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(do (def lock (Object.)) (locking lock 42))` — 'in the farm' (wrong preposition)

## Grade 10

### G10-01: quote, unquote, unquote-splice

- examples: 3
- variety @ n=50: 1.00
- issues: {'EMDASH_COMMENTARY': 3, 'BAD_PLACE_PREP': 1}
    - [EMDASH_COMMENTARY] form=`(quote (+ 1 2))` — concept_phrase or question_what has em-dash commentary
    - [EMDASH_COMMENTARY] form=`(quote (+ 1 2))` — concept_phrase or question_what has em-dash commentary
    - [EMDASH_COMMENTARY] form=`(quote (+ 1 2))` — concept_phrase or question_what has em-dash commentary
    - [BAD_PLACE_PREP] form=`(quote (+ 1 2))` — 'in the farm' (wrong preposition)

### G10-02: syntax-quote

- examples: 2
- variety @ n=50: 1.00
- issues: {'UNCLOSED_DIALOGUE_QUOTE': 1, 'BAD_PLACE_PREP': 1}
    - [UNCLOSED_DIALOGUE_QUOTE] form=`(let [x 10] `(+ ~x ~x))` — user_msg has an odd number of dialogue quotes (subplot opened a `"` but did not close it)
    - [BAD_PLACE_PREP] form=`(let [x 10] `(+ ~x ~x))` — 'in the farm' (wrong preposition)

### G10-06: when and when-not as macros

- examples: 3
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(when true 1 2 3)` — 'in the farm' (wrong preposition)

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(macroexpand '(-> x f g))` — 'in the farm' (wrong preposition)

### G10-09: Hygiene and gensym

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(symbol? (gensym))` — 'in the farm' (wrong preposition)

### G10-11: Reader macros overview

- examples: 3
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`[1 #_ 2 3]` — 'in the farm' (wrong preposition)

## Grade 11

### G11-01: JVM vs CLR vs JS vs Python (host overview)

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(do "Clojure runs on multiple hosts: JVM, CLR, JS,` — 'in the farm' (wrong preposition)

### G11-02: Method call syntax

- examples: 3
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(.toUpperCase "abc")` — 'in the farm' (wrong preposition)

### G11-04: Field access

- examples: 2
- variety @ n=50: 1.00
- issues: {'EMDASH_COMMENTARY': 3}
    - [EMDASH_COMMENTARY] form=`(count "tortoise")` — concept_phrase or question_what has em-dash commentary
    - [EMDASH_COMMENTARY] form=`(count "tortoise")` — concept_phrase or question_what has em-dash commentary
    - [EMDASH_COMMENTARY] form=`(count "tortoise")` — concept_phrase or question_what has em-dash commentary

### G11-06: new and dot-construct

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(String. "hello")` — 'in the farm' (wrong preposition)

### G11-09: Checked vs unchecked math

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(+ 1 2)` — 'in the farm' (wrong preposition)

## Grade 12

### G12-01: Transducers introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(into [] (map inc) [1 2 3])` — 'in the farm' (wrong preposition)

### G12-02: Transducer composition

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1}
    - [BAD_PLACE_PREP] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — 'in the farm' (wrong preposition)

### G12-03: into with a transducer (xform)

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOWERCASE_AFTER_PERIOD': 1}
    - [LOWERCASE_AFTER_PERIOD] form=`(into #{} (map inc) [1 2 3])` — subplot template starts a sentence with a lowercase {place} phrase (period followed by 'in the X' / 'on the Y' / etc.)

### G12-06: clojure.spec

- examples: 2
- variety @ n=50: 1.00
- issues: {'EMDASH_COMMENTARY': 6, 'BAD_PLACE_PREP': 1}
    - [EMDASH_COMMENTARY] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — concept_phrase or question_what has em-dash commentary
    - [BAD_PLACE_PREP] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — 'in the farm' (wrong preposition)
    - [EMDASH_COMMENTARY] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — concept_phrase or question_what has em-dash commentary
    - [EMDASH_COMMENTARY] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — concept_phrase or question_what has em-dash commentary
    - [EMDASH_COMMENTARY] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — concept_phrase or question_what has em-dash commentary
    - [EMDASH_COMMENTARY] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — concept_phrase or question_what has em-dash commentary

### G12-09: Test fixtures

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1, 'LOWERCASE_AFTER_PERIOD': 1}
    - [BAD_PLACE_PREP] form=`(do "(use-fixtures :each f) wraps every deftest in` — 'in the farm' (wrong preposition)
    - [LOWERCASE_AFTER_PERIOD] form=`(do "(use-fixtures :each f) wraps every deftest in` — subplot template starts a sentence with a lowercase {place} phrase (period followed by 'in the X' / 'on the Y' / etc.)

### G12-11: Leiningen project.clj

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOWERCASE_AFTER_PERIOD': 1}
    - [LOWERCASE_AFTER_PERIOD] form=`(do "Leiningen reads project.clj at the project ro` — subplot template starts a sentence with a lowercase {place} phrase (period followed by 'in the X' / 'on the Y' / etc.)

### G12-12: deps.edn projects

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOWERCASE_AFTER_PERIOD': 1}
    - [LOWERCASE_AFTER_PERIOD] form=`(do "deps.edn declares :deps and :aliases for the ` — subplot template starts a sentence with a lowercase {place} phrase (period followed by 'in the X' / 'on the Y' / etc.)

### G12-18: Clojure style guide

- examples: 2
- variety @ n=50: 1.00
- issues: {'BAD_PLACE_PREP': 1, 'LOWERCASE_AFTER_PERIOD': 1}
    - [BAD_PLACE_PREP] form=`(do "prefer pure functions, name predicates with ?` — 'in the farm' (wrong preposition)
    - [LOWERCASE_AFTER_PERIOD] form=`(do "prefer pure functions, name predicates with ?` — subplot template starts a sentence with a lowercase {place} phrase (period followed by 'in the X' / 'on the Y' / etc.)

---

## Summary

### Issue counts (across all examples × 3 records)

- **BAD_PLACE_PREP**: 77
- **ASIDE_PAREN**: 24
- **EMDASH_COMMENTARY**: 18
- **LOWERCASE_AFTER_PERIOD**: 13
- **WHICH_IS_LEAK**: 12
- **UNCLOSED_DIALOGUE_QUOTE**: 5

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 80 | 11 | — |
| 2 | 22 | 88 | 14 | — |
| 3 | 18 | 31 | 6 | — |
| 4 | 20 | 39 | 16 | — |
| 5 | 22 | 39 | 6 | — |
| 6 | 16 | 33 | 10 | — |
| 7 | 18 | 36 | 41 | — |
| 8 | 16 | 31 | 3 | — |
| 9 | 18 | 34 | 9 | — |
| 10 | 16 | 36 | 10 | — |
| 11 | 14 | 29 | 7 | — |
| 12 | 18 | 37 | 16 | — |

### Sample issues by severity

#### BAD_PLACE_PREP

- `G1-01` (form `42`): 'in the farm' (wrong preposition)
    ```
    The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place by the farm.

Grace and Casey stood in the farm where someone had
scratched the value 42 into a smooth slate by the egg-basket.
Casey, swaggering through the...
    ```
- `G1-02` (form `7`): 'in the farm' (wrong preposition)
    ```
    Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened in the farm.

Halfway through the morning errand, Alex stopped in the farm
with a basket of eggs and refused to move on until someone could
prove what the form `7` evaluated to. ...
    ```
- `G1-03` (form `(+ 1/2 1/4)`): 'in the farm' (wrong preposition)
    ```
    There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

At a small stall in the farm, someone had chalked a wager: whoever
predicted the result of `(+ 1/2 1/4)` first would set the asking
price for the morning's eggs. Casey, untroubled by what others thought, s...
    ```
- `G1-04` (form `"golden egg"`): 'in the farm' (wrong preposition)
    ```
    A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. This was in the farm.

A small wooden notice nailed to a post at the edge of the farm carried a puzzle for
the village. The riddle asked the reader to evaluate `"golden egg"`.
Carol laughed, puffed...
    ```
- `G1-05` (form `(> 3 5)`): 'in the farm' (wrong preposition)
    ```
    Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Carol and Casey stood in the farm where someone had
scratched the comparison (> 3 5) into a smooth slate by the egg-basket.
Casey, boasting at every turn, declared the answer was obvious — ...
    ```

#### UNCLOSED_DIALOGUE_QUOTE

- `G4-04` (form `'()`): user_msg has an odd number of dialogue quotes (subplot opened a `"` but did not close it)
    ```
    There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Henry, puffed up with pride, declared the collection plain — a row
of eggs, a stack of coins, nothing worth a second look. Frank
wrote `'()` on a slate in the cellar, calmly. "It's not about
plain or fancy...
    ```
- `G4-13` (form `(count {:a 1 :b 2})`): user_msg has an odd number of dialogue quotes (subplot opened a `"` but did not close it)
    ```
    There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place deep inside the kitchen.

Edward, boasting at every turn, declared the collection plain — a row
of eggs, a stack of coins, nothing worth a second look. David
wrote `(count {:a 1 :b 2})` ...
    ```
- `G4-14` (form `(empty? "")`): user_msg has an odd number of dialogue quotes (subplot opened a `"` but did not close it)
    ```
    A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Henry, with great whoops of laughter, declared the collection plain — a row
of eggs, a stack of coins, nothing worth a second look. Fiona
wrote `(empty? "")` on a slate deep inside the cellar, cal...
    ```
- `G4-19` (form `(first (range 1 100))`): user_msg has an odd number of dialogue quotes (subplot opened a `"` but did not close it)
    ```
    There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Morgan, as if the race were already won, declared the collection plain — a row
of eggs, a stack of coins, nothing worth a second look. Jordan
wrote `(first (range 1 100))` on a slate deep inside the barn, ...
    ```
- `G10-02` (form `(let [x 10] `(+ ~x ~x))`): user_msg has an odd number of dialogue quotes (subplot opened a `"` but did not close it)
    ```
    The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Henry had been trying to teach Bob how the REPL
works. "Here," he said, pointing to a syntax-quoted addition with x unquoted twice.
"You hand the form `(let [x 10] `(+ ~x ~x))`...
    ```

#### ASIDE_PAREN

- `G4-11` (form `(count #{1 1 1})`): concept_phrase has pedagogical-aside parenthetical
    ```
    There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened in the market.

A row of three coins sat on the kitchen table in the market, set out as a
wager between Sam and Henry. The bet was
simple: predict what `(count #{1 1 1})` would return. Sam,
with...
    ```
- `G4-11` (form `(count #{1 1 1})`): concept_phrase has pedagogical-aside parenthetical
    ```
    The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A wooden tally board hung on the barn wall at the edge of the market, half-filled with
the morning's marks. Casey wanted to add one more entry: the
result of `(count #{1 1 1})`...
    ```
- `G4-11` (form `(count #{1 1 1})`): concept_phrase has pedagogical-aside parenthetical
    ```
    A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A small wooden notice nailed to a post deep inside the kitchen carried a puzzle for
the village. The riddle asked the reader to evaluate `(count #{1 1 1})`.
Edward laughed, swaggering through the ...
    ```
- `G4-15` (form `(count (rest [10 20 30]))`): concept_phrase has pedagogical-aside parenthetical
    ```
    There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Edward had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Honk the goose were tallied in another column. Today inside a cottage, the
next entry ...
    ```
- `G4-15` (form `(count (rest [10 20 30]))`): concept_phrase has pedagogical-aside parenthetical
    ```
    Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened inside the kitchen.

Alice offered a small basket of eggs as a wager in the kitchen:
whoever guessed the result of `(count (rest [10 20 30]))` first would keep them.
Robin, untro...
    ```

#### WHICH_IS_LEAK

- `G6-06` (form `(:private (meta 'x))`): question_what '..., which is X' leaks the answer in narrative
    ```
    There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened inside the barn.

Bob had been trying to teach Henry how the REPL
works. "Here," he said, pointing to the :private flag on plain metadata of 'x (none set).
"You hand the form `(:private (meta 'x...
    ```
- `G6-06` (form `(:private (meta 'x))`): question_what '..., which is X' leaks the answer in narrative
    ```
    Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. This was at the edge of the market.

Emily and Frank stood in the market where someone had
scratched the :private flag on plain metadata of 'x (none set) into a smooth slate by the egg-baske...
    ```
- `G6-06` (form `(:private (meta 'x))`): question_what '..., which is X' leaks the answer in narrative
    ```
    A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened at the edge of the orchard.

George had been trying to teach Edward how the REPL
works. "Here," he said, pointing to the :private flag on plain metadata of 'x (none set).
"You hand the ...
    ```
- `G7-05` (form `(first nil)`): question_what '..., which is X' leaks the answer in narrative
    ```
    Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Sam and Grace stood deep inside a cottage where someone had
scratched calling first on nil into a smooth slate by the egg-basket.
Grace, with great whoops of laughter, declared the answer w...
    ```
- `G7-05` (form `(first nil)`): question_what '..., which is X' leaks the answer in narrative
    ```
    Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Emily had learned not to trust the morning basket on first
glance. by the village, she typed `(first nil)` carefully, ready
to catch whatever the REPL might throw back, the way one sets a q...
    ```

#### EMDASH_COMMENTARY

- `G7-05` (form `(some? 0)`): concept_phrase or question_what has em-dash commentary
    ```
    A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. This was inside the kitchen.

A row of three coins sat on the kitchen table inside the kitchen, set out as a
wager between Bob and Diana. The bet was
simple: predict what `(some? 0)` would return. ...
    ```
- `G7-05` (form `(some? 0)`): concept_phrase or question_what has em-dash commentary
    ```
    Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A row of three coins sat on the kitchen table in the cellar, set out as a
wager between George and Emily. The bet was
simple: predict what `(some? 0)` would return. George,
tempted by the t...
    ```
- `G7-05` (form `(some? 0)`): concept_phrase or question_what has em-dash commentary
    ```
    There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

"There is no need to evaluate that," Edward said, boasting at every turn.
"Anyone with eyes can see what the predicate (some? 0) — 0 is not nil comes to."
Charlie, who by the orchard had grown used to such...
    ```
- `G7-10` (form `(:doc (meta '^{:doc "adds two"} plus))`): concept_phrase or question_what has em-dash commentary
    ```
    Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. All this took place deep inside the kitchen.

Edward had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Plume the goose were tall...
    ```
- `G7-10` (form `(:doc (meta '^{:doc "adds two"} plus))`): concept_phrase or question_what has em-dash commentary
    ```
    There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Carol had learned not to trust the morning basket on first
glance. near the meadow, she typed `(:doc (meta '^{:doc "adds two"} plus))` carefully, ready
to catch whatever the REPL might throw back, the way ...
    ```

#### LOWERCASE_AFTER_PERIOD

- `G7-05` (form `(first nil)`): subplot template starts a sentence with a lowercase {place} phrase (period followed by 'in the X' / 'on the Y' / etc.)
    ```
    Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Emily had learned not to trust the morning basket on first
glance. by the village, she typed `(first nil)` carefully, ready
to catch whatever the REPL might throw back, the way one sets a q...
    ```
- `G7-05` (form `(count nil)`): subplot template starts a sentence with a lowercase {place} phrase (period followed by 'in the X' / 'on the Y' / etc.)
    ```
    A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened deep inside the barn.

Emily had learned not to trust the morning basket on first
glance. inside the barn, she typed `(count nil)` carefully, ready
to catch whatever the REPL might thro...
    ```
- `G7-09` (form `(tap> 42)`): subplot template starts a sentence with a lowercase {place} phrase (period followed by 'in the X' / 'on the Y' / etc.)
    ```
    The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Charlie had learned not to trust the morning basket on first
glance. near the market, he typed `(tap> 42)` carefully, ready
to catch whatever the REPL might throw back, the way...
    ```
- `G7-10` (form `(:doc (meta '^{:doc "adds two"} plus))`): subplot template starts a sentence with a lowercase {place} phrase (period followed by 'in the X' / 'on the Y' / etc.)
    ```
    There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Carol had learned not to trust the morning basket on first
glance. near the meadow, she typed `(:doc (meta '^{:doc "adds two"} plus))` carefully, ready
to catch whatever the REPL might throw back, the way ...
    ```
- `G7-13` (form `(count (clojure.string/split-lines "a\nb\nc"))`): subplot template starts a sentence with a lowercase {place} phrase (period followed by 'in the X' / 'on the Y' / etc.)
    ```
    Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

David had learned not to trust the morning basket on first
glance. by the market, he typed `(count (clojure.string/split-lines "a\nb\nc"))` carefully, ready
to catch whatever the REPL might...
    ```

