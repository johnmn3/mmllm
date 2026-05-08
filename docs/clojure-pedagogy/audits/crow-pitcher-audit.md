# crow-pitcher curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

### G1-13: First arithmetic call

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(+ 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G1-15: Equality

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'CONCEPT_AS_VERB': 1}
    - [LOW_GROUNDING] form=`(= 1 1 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(= 1 1 1 1)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G1-16: Numeric predicates

- examples: 6
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 4}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(zero? 0)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [SENTENCE_START_LOWER_PRONOUN] form=`(pos? 7)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [SENTENCE_START_LOWER_PRONOUN] form=`(pos? -2)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [SENTENCE_START_LOWER_PRONOUN] form=`(neg? -3)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation

## Grade 2

### G2-03: not= and = with multiple args

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'SENTENCE_START_LOWER_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(not= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [SENTENCE_START_LOWER_PRONOUN] form=`(not= 1 1)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [LOW_GROUNDING] form=`(= 1 1 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-06: inc and dec

- examples: 5
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 1}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(inc -1)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation

### G2-07: Absolute value

- examples: 4
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 1}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(abs -5)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation

### G2-08: Arithmetic on ratios

- examples: 3
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 2}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(- 1 1/3)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [SENTENCE_START_LOWER_PRONOUN] form=`(- 1 1/3)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation

### G2-09: Floats vs ints (the / operator)

- examples: 3
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 1}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(/ 1.0 2)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation

### G2-10: Powers via repeated multiplication

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'SENTENCE_START_LOWER_PRONOUN': 1}
    - [LOW_GROUNDING] form=`(* 2 2 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [SENTENCE_START_LOWER_PRONOUN] form=`(* 5 5)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation

### G2-13: and / or — short circuit, return values

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'CONCEPT_AS_VERB': 4, 'REPEATED_OPENER_FRAGMENT': 1}
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(and true false)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(or false true)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(or false false)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(or false false)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G2-14: not — turning truthy to false

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CONCEPT_AS_VERB': 3}
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(not true)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(not false)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(not false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(not nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(not 0)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G2-16: Truthy 0 and empty string

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'CONCEPT_AS_VERB': 1}
    - [LOW_GROUNDING] form=`(boolean 0)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(boolean false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CONCEPT_AS_VERB] form=`(boolean false)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G2-18: Quoting symbols

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5}
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= (quote tortoise) 'tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= (quote tortoise) 'tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 3

### G3-08: fn — multi-arg

- examples: 1
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`((fn [a b c] (+ a b c)) 1 2 3)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`(#(+ % 1) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G3-13: fn body returns last form

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`((fn [x] x x x 99) 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`((fn [x] x x x 99) 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

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
    - [LOW_GROUNDING] form=`["a" "b"]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-19: range and seq

- examples: 2
- variety @ n=50: 0.99
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(count (range 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count (range 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count (range 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 5

### G5-08: not

- examples: 1
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`(not (> 1 2))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G5-16: partial

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`((partial + 10) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G5-17: juxt

- examples: 1
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1}
    - [CONCEPT_AS_VERB] form=`((juxt inc dec) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

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
- issues: {'ANSWER_LEAK_STRING': 1, 'LOW_GROUNDING': 1}
    - [ANSWER_LEAK_STRING] form=`(name 'foo.bar)` — answer string 'foo.bar' appears in user_msg
    - [LOW_GROUNDING] form=`(name 'foo.bar)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-05: Fully qualified names

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(name :owner/item)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-07: Public vs private API

- examples: 2
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 1}
    - [BOOL_LEAK_RESOLUTION] form=`(boolean (:private (meta '^:private hidden)))` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead

### G6-09: Loading order

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-11: Classpath

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(count ["src" "test" "resources"])` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-14: Import for host classes

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(symbol? 'java.util.List)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name 'java.util.Map)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-16: Cleaning up requires

- examples: 2
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 1, 'LOW_GROUNDING': 1}
    - [BOOL_LEAK_RESOLUTION] form=`(contains? #{'clojure.string} 'clojure.set)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.set)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 7

### G7-03: try / finally

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(try 7 (finally (prn :cleanup)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-05: nil punning

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(first nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(first nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-06: pre and post conditions

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exce` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-07: assert

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPEATED_OPENER_FRAGMENT': 1}
    - [REPEATED_OPENER_FRAGMENT] form=`(do (assert (= 1 1)) 1)` — opener fragment 'the pitcher near the farm' also appears later in user_msg

### G7-09: tap>

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`(tap> 42)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(tap> 42)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(tap> 42)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-11: Reading stack traces

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(try (throw (ex-info "trouble" {})) (catch Excepti` — answer string 'trouble' appears in user_msg

### G7-13: line-seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4}
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(first (clojure.string/split-lines "alpha\nbeta"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-14: with-open

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(with-out-str (println "hare"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (println "hare"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-15: *in* and *out*

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(with-out-str (println))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(with-out-str (println))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-16: edn read

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "42")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "{:a 1}")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "{:a 1}")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "[:hare :tortoise]")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-17: JSON roundtrip

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

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
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-07: Record implementing protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (defrecord F` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-14: Protocols don't inherit

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-15: derive and isa? — multimethod hierarchy

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(isa? java.lang.Long java.lang.Number)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(isa? java.lang.String java.lang.Number)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-16: Abstract design with protocols

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol Sound (cry [this])) (defrecord Fa` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 9

### G9-03: Atom introduction

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-07: Ref introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_PREP': 1, 'LOW_GROUNDING': 1}
    - [DOUBLE_PREP] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — verb+preposition followed by {place} which already carries its own preposition
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-09: Ref vs atom

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-10: Agent introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-11: send and send-off

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send-off ag inc) (await ag` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-13: future introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3}
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'DOUBLE_PREP': 2}
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_PREP] form=`(do (def lock (Object.)) (locking lock 42))` — verb+preposition followed by {place} which already carries its own preposition
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock 42))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_PREP] form=`(do (def lock (Object.)) (locking lock 42))` — verb+preposition followed by {place} which already carries its own preposition

## Grade 10

### G10-01: quote, unquote, unquote-splice

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-03: defmacro introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg 221 words

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1, 'LOW_GROUNDING': 1}
    - [CONCEPT_AS_VERB] form=`(macroexpand '(-> x f g))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(macroexpand '(-> x f g))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-11: Reader macros overview

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`[1 #_ 2 3]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`[1 #_ 2 3]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-12: Tagged literals

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(inst? #inst "2024-01-01")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-13: Data readers and EDN extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(clojure.edn/read-string "[:a :b :c]")` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-14: eval (the function)

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2}
    - [LOW_GROUNDING] form=`(eval '(+ 1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(eval (list '+ 4 5))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G10-16: Macro pattern library

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1}
    - [LOW_GROUNDING] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 11

### G11-06: new and dot-construct

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1}
    - [ANSWER_LEAK_STRING] form=`(new String "jump")` — answer string 'jump' appears in user_msg

## Grade 12

### G12-03: into with a transducer (xform)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1}
    - [HIGH_LENGTH] form=`(into #{} (map inc) [1 2 3])` — user_msg 206 words

### G12-06: clojure.spec

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — tortoise-hare-specific imagery 'leather notebook' leaks into crow-pitcher prose

---

## Summary

### Issue counts (across all examples × 3 records)

- **LOW_GROUNDING**: 78
- **CONCEPT_AS_VERB**: 15
- **SENTENCE_START_LOWER_PRONOUN**: 11
- **ANSWER_LEAK_STRING**: 4
- **HIGH_LENGTH**: 3
- **DOUBLE_PREP**: 3
- **REPEATED_OPENER_FRAGMENT**: 2
- **ANSWER_LEAK**: 2
- **BAD_PLACE_PREP**: 2
- **BOOL_LEAK_RESOLUTION**: 2
- **FORM_LEAK**: 1
- **FOREIGN_FABLE_IMAGERY**: 1

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 7 | — |
| 2 | 22 | 88 | 31 | — |
| 3 | 18 | 31 | 6 | — |
| 4 | 20 | 39 | 4 | — |
| 5 | 22 | 39 | 7 | — |
| 6 | 16 | 33 | 10 | — |
| 7 | 18 | 36 | 22 | — |
| 8 | 16 | 31 | 7 | — |
| 9 | 18 | 34 | 16 | — |
| 10 | 16 | 36 | 11 | — |
| 11 | 14 | 29 | 1 | — |
| 12 | 18 | 37 | 2 | — |

### Sample issues by severity

#### LOW_GROUNDING

- `G1-13` (form `(+ 1 2)`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    The orchard had not seen a real rain in weeks, and even the lavender stood with its head bowed.

Caw crouched at the orchard pitcher's rim, seven stones in her left talon and eight in her right, both handfuls poised above the water.

She wanted the runtime to count both handfuls as one heap and retu...
    ```
- `G1-15` (form `(= 1 1 1 1)`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    in the orchard, a single pitcher held the last of the water, and Updraft the crow arrived too parched to be picky.

Sable lined up four single stones at the garden pitcher's dual-gate check, each carrying the count one, presenting all four to the gate at the same time.

Sable needed the gate to conf...
    ```
- `G2-03` (form `(not= 1 1)`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    on the farm, where the orchard meets the well, an old clay pitcher had stood for as long as anyone could remember.

Korvus placed two identical stones side by side on the pitcher's rim at the garden — both carrying the count one. He wondered if the pitcher would call them unequal.

He needed to veri...
    ```
- `G2-03` (form `(= 1 1 2)`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    in the village, a single pitcher held the last of the water, and Cipherwing the crow arrived too parched to be picky.

Sable lined up three stones at the orchard pitcher: two equal ones followed by a noticeably larger one. She needed the pitcher to check whether all three were truly the same.

She n...
    ```
- `G2-10` (form `(* 2 2 2)`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    The kitchen garden had been lovingly kept, but the sun that year had been merciless and constant.

Korvus scratched three tallies of two into the pitcher's rim at the farm, stacking each layer on the product of the last. He wanted the final compounded count from three doublings.

He needed the resul...
    ```

#### CONCEPT_AS_VERB

- `G1-15` (form `(= 1 1 1 1)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    Vellum circled twice by the orchard before settling on the rim of the old clay jar, eyes on the water below.

"You can't tell which way the gate will swing by guessing,"
Vellum the crow, calm and methodical, said. "You bring the form to the gate, the runtime
checks it, and the gate gives the only an...
    ```
- `G2-13` (form `(and true false)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    When Sly landed by the garden wall, he saw the water and saw the distance, and stood very still.

"You can't tell which way the gate will swing by guessing,"
Sly the crow, watching the level lift, drop by drop, said. "You bring the form to the gate, the runtime
checks it, and the gate gives the only...
    ```
- `G2-13` (form `(or false true)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    The kitchen garden had been lovingly kept, but the sun that year had been merciless and constant.

"You can't tell which way the gate will swing by guessing,"
Riddle the crow, patient as the water rose, said. "You bring the form to the gate, the runtime
checks it, and the gate gives the only answer ...
    ```
- `G2-13` (form `(or false false)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    near the hilltop, a single pitcher held the last of the water, and Swoop the crow arrived too parched to be picky.

"You can't tell which way the gate will swing by guessing,"
Swoop the crow, deliberate, unhurried by the rising sun, said. "You bring the form to the gate, the runtime
checks it, and t...
    ```
- `G2-13` (form `(or false false)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    The drought had reached even on the road, and Hieroglyph the crow flew in slow circles searching for water.

"You can't tell which way the gate will swing by guessing,"
Hieroglyph the crow, deliberate, unhurried by the rising sun, said. "You bring the form to the gate, the runtime
checks it, and the...
    ```

#### SENTENCE_START_LOWER_PRONOUN

- `G1-16` (form `(zero? 0)`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    Word had it that Glint had flown over three valleys before finding the pitcher on the road.

Coast the crow eyed the heap, with a confident tilt of the head, and called out a guess
about how many stones could be dropped before the water rose high
enough, without bothering to count. Glint the crow si...
    ```
- `G1-16` (form `(pos? 7)`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    In a year when the wells ran low, a single jar of water was a small kingdom unto itself.

Mystery the crow eyed the heap, with a triumphant rattle of feathers, and called out a guess
about how many stones could be dropped before the water rose high
enough, without bothering to count. Caw the crow si...
    ```
- `G1-16` (form `(pos? -2)`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    The orchard on the farm had grown quiet in the heat, and Coast the crow was the only sound at midday.

Lapis the crow eyed the heap, with a confident tilt of the head, and called out a guess
about how many stones could be dropped before the water rose high
enough, without bothering to count. Coast t...
    ```
- `G1-16` (form `(neg? -3)`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    On the rim of a long-shadowed pitcher, a thirsty bird considered what it had and what it lacked.

Bismuth the crow eyed the heap, with a triumphant rattle of feathers, and called out a guess
about how many stones could be dropped before the water rose high
enough, without bothering to count. Hum the...
    ```
- `G2-03` (form `(not= 1 1)`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    Malachite circled twice near the market before settling on the rim of the old clay jar, eyes on the water below.

Symbol the crow eyed the heap, preening at the thought of knowing, and called out a guess
about how many stones could be dropped before the water rose high
enough, without bothering to c...
    ```

#### REPEATED_OPENER_FRAGMENT

- `G2-13` (form `(or nil false 5)`): opener fragment 'the pitcher at the edge of the' also appears later in user_msg
    ```
    Word had it that Pirouette had flown over three valleys before finding the pitcher at the edge of the meadow.

Sharp the crow swooped toward the pitcher at the edge of the meadow, with a self-satisfied beak-click, certain
the gate would swing open. Pirouette the crow watched: the only way to know
wh...
    ```
- `G7-07` (form `(do (assert (= 1 1)) 1)`): opener fragment 'the pitcher near the farm' also appears later in user_msg
    ```
    Word had it that Thermal had flown over three valleys before finding the pitcher near the farm.

Thermal the crow, watching the level lift, drop by drop, spread a patch of soft moss beneath
the pitcher near the farm — the day was hot, the throat was narrow, and any
pebble flung wrong without a cushi...
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

Onyxwing the crow, steady in the stone-by-stone approach, spread a patch of soft moss beneath
the pitcher at the market — the day was hot, the throat was narrow, and any
pebble flung wrong without a cushi...
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

#### BOOL_LEAK_RESOLUTION

- `G6-07` (form `(boolean (:private (meta '^:private hidden)))`): resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    ```
    Witty circled twice near the hilltop before settling on the rim of the old clay jar, eyes on the water below.

Korvus carved a symbol onto the pitcher's rim in the orchard and pressed a small private mark into the margin beside it. He then tested whether the mark read as a firm yes when converted to...
    ```
- `G6-16` (form `(contains? #{'clojure.string} 'clojure.set)`): resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    ```
    It was the kind of summer that turned every shaded stone into a small kindness.

Sable examined the same set of required-namespace stones at the pitcher's rim in the garden and looked for a different shelf's stone — the set shelf, not the string shelf. They needed to know if it was there.

They need...
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

#### FOREIGN_FABLE_IMAGERY

- `G12-06` (form `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42)`): tortoise-hare-specific imagery 'leather notebook' leaks into crow-pitcher prose
    ```
    at the market, a single pitcher held the last of the water, and Sable the crow arrived too parched to be picky.

Sable the crow kept a small leather notebook of every goal
he had translated into a Clojure form. Today by the market,
the next entry was a goal: use spec to validate that 42 conforms to ...
    ```

