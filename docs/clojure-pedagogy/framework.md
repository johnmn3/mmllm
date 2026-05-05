# Framework: K-12 Clojure curriculum

Full specification of the layer hierarchy, grade-by-grade subject
lists, and the 4clojure-exercise model.

## The 5 elementary layers (grades 1-5)

### Layer 1 — atoms

The set of values that evaluate to themselves. Nothing else is needed
to start: a Clojure session reading `42` and printing `42` already
exhibits the entire layer.

Concepts in L1: `42`, `"hello"`, `true`/`false`, `nil`, `:keyword`,
`\c` (chars), `1/2` (ratios), comments, whitespace, parentheses-as-
syntax (not yet "operators").

### Layer 2 — application

Evaluating `(f x y)` means: evaluate `f`, evaluate `x`, evaluate `y`,
then apply `f` to the resulting values. This is the lambda-calculus
core; everything else in Clojure is layered on top.

Concepts in L2: function call, arity, operator-as-function (`+`, `*`,
`-`, `/`, `=`, `<`, `>`), single-form evaluation, prefix notation,
nested calls (the substitution rule).

### Layer 3 — naming

Three forms of naming, in order:
- `def`: top-level binding (the value is now reachable by name in the
  whole namespace).
- `let`: local binding inside an expression. The form `(let [x 3] ...)`
  is just sugar for `((fn [x] ...) 3)`.
- `fn` parameters: same shape — every function call introduces names
  for the duration of the body.

Once a learner can read `(let [x 3] (+ x 1))` and substitute `x` for
3 in their head, they have grasped naming.

### Layer 4 — collections

Four core collection types, each with its own literal syntax and
behavior.
- Vector `[1 2 3]` — indexed, ordered, fast `nth`/`conj-at-end`.
- List `'(1 2 3)` — sequential, ordered, fast `cons`/`first`.
- Map `{:a 1 :b 2}` — key-value, fast `get`/`assoc`.
- Set `#{1 2 3}` — unique unordered membership.

Operations split into "creation" (`vector`, `list`, `hash-map`,
`hash-set`), "access" (`nth`, `get`, `first`, `rest`, `last`,
`count`), and "modification" (`conj`, `assoc`, `dissoc`, `disj`).

### Layer 5 — control + higher-order

Two distinct things bundled together:
- **Control flow**: `if`, `when`, `cond`, `case`, `and`, `or`, `not`.
- **Higher-order**: `fn`, function-as-value, `map`, `filter`,
  `reduce`, `apply`, `comp`, `partial`, `juxt`, `iterate`.

Both are forms of *delaying* computation. `if` chooses which branch
to evaluate; `fn` packages a body for later evaluation; `map` defers
the per-element body until the sequence is realized.

## Dependency graph

A subject in any grade may only reference concepts from earlier
subjects. The strict ordering:

```
L1 < L2 < L3 < L4 < L5  (elementary)
< organization (G6)
< error handling (G7)
< polymorphism (G8)
< concurrency (G9)
< macros (G10)
< interop (G11)
< real-world (G12)
```

Within a grade, subjects also follow a dependency order — e.g., grade
1's "boolean values" precedes "boolean comparisons" which precedes
"boolean predicates."

The `prereqs:` field of each subject file makes the local dependencies
explicit and machine-readable.

## Grade 1 — atoms + first eval (Layer 1, hint of L2)

Theme: "Things, and what eval does to them."

A grade-1 student leaves with: I can type values into the REPL and
predict what comes back. I can read `(+ 1 2)` and know it's 3.

Subjects:
1. `01-eval-as-substitution` — what the REPL does, exemplar
2. `02-numbers-integer` — integers (positive, negative, zero)
3. `03-numbers-ratio` — `1/2` is a value, not a computation
4. `04-strings` — `"hello"` is a value
5. `05-booleans` — `true`, `false`
6. `06-nil` — `nil` is its own thing; not 0, not "", not false
7. `07-keywords` — `:foo` is a value-with-a-name
8. `08-characters` — `\c`, `\space`, `\newline`
9. `09-symbols-vs-values` — what makes `42` evaluate to 42 but `x`
   not? (intro to naming, formalized in grade 3)
10. `10-comments` — `;`, `;;`, and `#_form` reader-skip
11. `11-whitespace-doesnt-matter` — except inside strings
12. `12-parens-as-syntax` — they group, they don't multiply
13. `13-first-arithmetic-call` — `(+ 1 2)`, `(- 5 3)`, `(* 4 5)`
14. `14-nested-call-evaluation` — `(+ 1 (* 2 3))`
15. `15-equality` — `(= 1 1)`, `(= "a" "a")`
16. `16-numeric-predicates` — `zero?`, `pos?`, `neg?`
17. `17-printing-vs-returning` — REPL displays the return value
18. `18-error-doesnt-mean-broken` — making mistakes in the REPL is
    safe; how to read an arity error

## Grade 2 — operators + arithmetic mastery (Layer 1+2)

Theme: "Operators and their families."

Subjects:
1. `01-multi-arg-arithmetic` — `(+ 1 2 3 4)`, why this works
2. `02-comparison-chains` — `(< 1 2 3)` means strictly increasing
3. `03-not-equal` — `not=` and `=` with multiple args
4. `04-min-max` — `(min 1 2 3)`, `(max ...)`
5. `05-quot-rem-mod` — three division operators, when to use which
6. `06-inc-dec` — sugar for `+1` and `-1`
7. `07-abs` — absolute value via `(Math/abs ...)` interop or by hand
8. `08-arithmetic-on-ratios` — `1/2 + 1/4` stays exact
9. `09-floats-vs-ints` — when `/` returns a float vs an integer
10. `10-power-by-mult` — no built-in power for ints; multiply
11. `11-string-concat` — `(str "a" "b")`, mixing types
12. `12-print-and-println` — what they return, what they side-effect
13. `13-and-or-truthy` — `and`/`or` short-circuit and return values,
    not just booleans
14. `14-not` — turns truthy to false, falsy to true
15. `15-falsey-values` — only `false` and `nil` are falsey
16. `16-cond-coercion-pitfalls` — `(if 0 :a :b)` returns `:a`!
17. `17-keyword-as-function` — `(:foo m)` is `(get m :foo)`
18. `18-symbols-evaluate-to-bindings` — preview of grade 3
19. `19-quoting-intro` — `'foo` returns a symbol; `(quote foo)`
20. `20-numeric-tower` — auto-promotion to bigint, ratio, double
21. `21-rand-and-rand-int` — random, but a function call
22. `22-compose-pure-arithmetic` — multi-step calculations like
    BMI, distance, ratio-of-ratios, all in one expression

## Grade 3 — naming, scope, substitution (Layer 3)

Theme: "Names, scope, and substitution."

Subjects:
1. `01-def-introduction` — `(def x 42)` puts a value in the namespace
2. `02-def-redefinition` — what happens if you `def` again
3. `03-let-introduction` — `(let [x 3] (+ x 1))` is sugar for ((fn [x]...) 3)
4. `04-let-multi-binding` — `(let [a 1 b 2] (+ a b))` evaluates
   sequentially
5. `05-let-shadowing` — inner `let` shadows outer `def`
6. `06-let-binding-can-reference-prior` — `(let [a 1 b (+ a 1)] ...)`
7. `07-fn-introduction` — `(fn [x] (+ x 1))` is a value
8. `08-fn-multi-arity-arg-list` — single fn, takes multiple args
9. `09-defn-shorthand` — `(defn foo [x] (+ x 1))` is `def` + `fn`
10. `10-anonymous-shorthand` — `#(...)` and `%`, `%1`, `%2`
11. `11-substitution-rule` — what really happens during a function call
12. `12-scope-vs-namespace` — globals vs locals
13. `13-fn-returns-the-last-form` — body sequencing
14. `14-do-form` — `(do form1 form2 form3)`
15. `15-side-effects-in-body` — `(do (println "hi") result)`
16. `16-name-collision-namespace-vs-let` — what binds first
17. `17-naming-conventions` — kebab-case, no shadowing built-ins
18. `18-when-to-name-vs-inline` — code-clarity decisions

## Grade 4 — collections (Layer 4)

Theme: "Collections — vector, list, map, set."

Subjects:
1. `01-vector-literal` — `[1 2 3]`, the workhorse
2. `02-vector-access-nth` — `(nth v 0)`, 0-indexed
3. `03-vector-conj-end` — `(conj [1 2] 3) ;=> [1 2 3]`
4. `04-list-literal` — `'(1 2 3)`, when to use lists
5. `05-list-cons-front` — `(cons 0 '(1 2 3))`
6. `06-map-literal` — `{:a 1 :b 2}`, key-value
7. `07-map-get` — `(get m :a)`, `(:a m)`, `(m :a)` — three ways
8. `08-map-assoc` — `(assoc m :a 99)` returns a new map
9. `09-map-dissoc` — `(dissoc m :a)`
10. `10-map-keys-vals` — `(keys m)`, `(vals m)`
11. `11-set-literal` — `#{1 2 3}`, no duplicates
12. `12-set-membership` — `(contains? s 1)` or `(s 1)`
13. `13-count-on-anything` — `(count [1 2 3])`, `(count {:a 1})`
14. `14-empty-checks` — `(empty? [])`, `(seq coll)` for nil-or-seq
15. `15-first-rest-last` — universal seq access
16. `16-into-and-conj-coll-of-coll` — building from existing
17. `17-immutability` — `assoc` returns new, doesn't mutate
18. `18-equality-of-colls` — `[1 2 3]` equals `'(1 2 3)`?
19. `19-range-and-seq` — `(range 5)`, lazy intro
20. `20-collection-vs-sequence` — what `seq` does

## Grade 5 — control flow + higher-order intro (Layer 5)

Theme: "Choosing and repeating."

Subjects:
1. `01-if` — `(if test then else)`
2. `02-if-as-expression` — returns a value, not just branches
3. `03-when` — `if` with implicit `do` and no else
4. `04-cond` — multiple test/result pairs
5. `05-cond-else` — `:else` clause
6. `06-case` — value-based dispatch
7. `07-and-or-as-control` — short-circuit
8. `08-not` — turning truthy to false
9. `09-fn-as-value` — pass functions to other functions
10. `10-map-introduction` — `(map inc [1 2 3])`
11. `11-filter-introduction` — `(filter even? [1 2 3 4])`
12. `12-reduce-introduction` — `(reduce + [1 2 3 4])`
13. `13-reduce-with-init` — `(reduce + 0 [...])`
14. `14-apply` — `(apply + [1 2 3])`
15. `15-comp` — `(comp inc inc)` as `(fn [x] (inc (inc x)))`
16. `16-partial` — `(partial + 10)` is `(fn [x] (+ 10 x))`
17. `17-juxt` — parallel application
18. `18-some` — find first truthy
19. `19-every?` — universal quantifier
20. `20-take-and-drop` — slicing seqs
21. `21-distinct-and-sort` — set-like ops on seqs
22. `22-recur-tail-position` — first-pass on recursion

## Grade 6 — namespaces and modular code

Theme: "Where code lives."

Subjects:
1. `01-namespace-as-file` — `src/foo/bar.clj` matches `foo.bar`
2. `02-ns-form` — `(ns foo.bar)` at top of file
3. `03-require` — `(:require [clojure.string :as s])`
4. `04-refer-and-use` — bringing names into scope
5. `05-fully-qualified-names` — `clojure.string/upper-case`
6. `06-private-defs` — `defn-`, `^:private`
7. `07-public-vs-private-api` — design decision
8. `08-circular-dependencies` — what they are, how to avoid
9. `09-loading-order` — REPL vs file-system
10. `10-leiningen-and-deps-edn` — project setup briefly
11. `11-classpath` — where Clojure looks for code
12. `12-multiple-files-one-project` — splitting code by concern
13. `13-aliasing-conventions` — `s` for clojure.string, etc.
14. `14-import-for-java-classes` — `(:import (java.util Date))`
15. `15-namespace-meta` — docstrings, doc display
16. `16-cleaning-up-requires` — only what you use

## Grade 7 — error handling, debugging, IO

Theme: "When things go wrong, and the world outside the REPL."

Subjects:
1. `01-throw` — `(throw (Exception. "msg"))`
2. `02-try-catch` — basic exception handling
3. `03-try-finally` — cleanup
4. `04-ex-info` — `(ex-info "msg" {:data ...})` for structured errors
5. `05-nil-puning` — `nil` returns through threads silently
6. `06-pre-post-conditions` — `{:pre [...] :post [...]}`
7. `07-assert-form` — `(assert ...)` for invariants
8. `08-printing-for-debugging` — `prn`, `pprint`
9. `09-tap` — `(tap> x)` for non-invasive inspection
10. `10-doc-source` — REPL helpers `doc`, `source`
11. `11-reading-stack-traces` — what to look for
12. `12-slurp-and-spit` — read/write files
13. `13-line-seq` — read line-by-line
14. `14-with-open` — resource cleanup
15. `15-stdin-stdout` — `*in*`, `*out*`, `*err*`
16. `16-edn-read-string` — safe data reading
17. `17-json-roundtrip` — via cheshire or `clojure.data.json`
18. `18-shell-command` — `(clojure.java.shell/sh "ls")`

## Grade 8 — protocols, multimethods, abstraction

Theme: "Defining behavior across types."

Subjects:
1. `01-why-polymorphism` — the problem it solves
2. `02-deftype-introduction` — minimal record-like type
3. `03-defrecord-introduction` — type with map-like access
4. `04-protocol-definition` — `(defprotocol Foo ...)`
5. `05-protocol-extension` — `(extend-protocol Foo ...)`
6. `06-protocol-method-dispatch` — by argument-class
7. `07-record-implementing-protocol` — combined
8. `08-multimethod-defmulti` — dispatch fn intro
9. `09-multimethod-defmethod` — adding implementations
10. `10-multimethod-vs-protocol` — when to choose which
11. `11-protocol-vs-interface` — Java analogue
12. `12-extending-existing-types` — `extend-type` on built-in types
13. `13-this-style-vs-fn-style` — protocol fn first arg
14. `14-protocol-inheritance` — there isn't any, by design
15. `15-derive-and-isa` — multimethod hierarchy
16. `16-abstract-design-with-protocols` — small example

## Grade 9 — state and concurrency primitives

Theme: "When time matters."

Subjects:
1. `01-immutability-as-default` — review
2. `02-why-state-at-all` — places that need it
3. `03-atom-introduction` — `(atom 0)`, `swap!`, `reset!`
4. `04-atom-cas-semantics` — `swap!` retries
5. `05-watch-on-atom` — change notification
6. `06-validator-on-atom` — preventing bad values
7. `07-ref-introduction` — coordinated change
8. `08-dosync-and-alter` — STM transactions
9. `09-ref-vs-atom` — when to choose which
10. `10-agent-introduction` — async changes
11. `11-send-and-send-off` — agent thread-pool variants
12. `12-await` — synchronizing on agents
13. `13-future-introduction` — `(future ...)`
14. `14-deref` — `@x` shorthand
15. `15-promise` — `(promise)`, `(deliver p v)`
16. `16-volatile` — when STM is too heavy
17. `17-thread-local-binding` — `binding` form
18. `18-locking` — last resort

## Grade 10 — macros, code as data

Theme: "Programs that write programs."

Subjects:
1. `01-quote-and-unquote` — `'`, `~`, `~@`
2. `02-syntax-quote` — `` ` `` and namespace resolution
3. `03-defmacro-introduction` — first macro
4. `04-macro-expansion-rule` — input forms in, output forms out
5. `05-macroexpand` — debugging tool
6. `06-when-and-unless-macros` — built-ins as exemplars
7. `07-threading-macros-revisited` — `->`, `->>`
8. `08-macro-vs-fn` — when each is right
9. `09-hygiene-and-gensym` — `(gensym)`, `#`-suffix
10. `10-anaphoric-macros-bad-idea` — why `it` binds confuse
11. `11-reader-macros-overview` — what reader does before eval
12. `12-tagged-literals` — `#inst`, `#uuid`
13. `13-data-readers-edn-extension` — defining your own
14. `14-eval` — yes the function
15. `15-when-not-to-write-a-macro` — most of the time
16. `16-macro-pattern-library` — `with-X`, `def-X-thing`

## Grade 11 — interop

Theme: "Crossing into other runtimes."

Subjects:
1. `01-jvm-vs-clr-vs-js-vs-python` — Clojure's hosted nature
2. `02-method-call-syntax` — `(.method obj args)`
3. `03-static-method-call` — `(Math/sqrt 2.0)`
4. `04-field-access` — `(.-x p)` and `(.x p)`
5. `05-import-form` — `(:import (java.util Date))`
6. `06-new-form-and-dot-construct` — `(Date.)` and `(new Date)`
7. `07-arrays` — `(int-array ...)`, `(aget ...)`
8. `08-typed-args-and-^` — type hints
9. `09-checked-vs-unchecked-math` — `*unchecked-math*`
10. `10-clojurescript-overview` — JS host
11. `11-cljs-js-interop` — `js/console.log`, `(.-foo ...)`
12. `12-basilisp-overview` — Python host (this is the project!)
13. `13-cross-platform-cljc` — `.cljc` files and reader-conditionals
14. `14-debugging-host-leaks` — when interop bites

## Grade 12 — real-world Clojure

Theme: "Putting it all together."

Subjects:
1. `01-transducers-introduction` — `(map inc)` without seq context
2. `02-transducers-composition` — `(comp (map inc) (filter even?))`
3. `03-into-with-transducer` — `(into [] xform xs)`
4. `04-core-async-introduction` — `chan`, `go`, `<!`, `>!`
5. `05-channels-and-pipelines` — pipe, mult, mix
6. `06-spec-clojure-spec` — `s/def`, `s/keys`, `s/conform`
7. `07-spec-generators` — `s/exercise`
8. `08-test-clojure-test` — `deftest`, `is`, `testing`
9. `09-test-fixtures` — `use-fixtures`
10. `10-test-property-based` — generative testing
11. `11-leiningen-projects` — `project.clj` shape
12. `12-deps-edn-projects` — modern alternative
13. `13-aliases-and-tools` — `clj -M:test`
14. `14-pedestal-or-ring-overview` — web stack briefly
15. `15-datomic-or-xtdb-overview` — datalog db briefly
16. `16-reagent-overview` — cljs UI briefly
17. `17-library-design-patterns` — public API surface
18. `18-clojure-style-guide` — community conventions

## 4clojure-style exercise model

Every subject ends with 5-10 exercises in the form:

```
{:problem-id "G1-01-eval-1"
 :prompt    "What does the REPL print for this form?"
 :form      "42"
 :expected  42}

{:problem-id "G1-01-eval-2"
 :prompt    "Evaluate."
 :form      "(+ 1 2)"
 :expected  3}
```

Each exercise has:
- A problem id (`G<grade>-<subject>-<n>`)
- A natural-language prompt
- A Clojure form OR a fill-in-the-blank shape
- An expected value (or, for code-completion, a test predicate)

Exercises are runnable in basilisp / mmllm's eval tool — the same
runtime the model is being trained against. This is the bridge
between the pedagogical framework and the model: the **same
exercises** are training data + evaluation set.

## How this connects to mmllm

The model we're training (mmllm) submits answers via `eval(form)`.
The pedagogy framework's exercises are training-shaped: each one is
a (sys-prompt declaring `eval` tool, user prompt with the question,
expected eval result). The graded curriculum gives a ladder:

- Grade 1 problems: model can write `(+ 1 2)` and have it eval to 3.
- Grade 5 problems: model can write a `(let [...] (reduce ...))` to
  solve a small puzzle.
- Grade 10 problems: model can write a macro.

By tying mastery to specific grades, we have a graded benchmark for
the model's Clojure capability that's more interpretable than a
single bpc number.
