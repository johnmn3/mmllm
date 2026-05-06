# Metaphor re-audit, round 2 — what's still semantically thin

**State as of commit `2bb63b5`.** Five high-leverage metaphor families
(pouch / recipe / basket / sieve / notebook) shipped. **62 subjects**
now carry the idiom in their narrative. **Re-reviewing the rest** to
find which subjects are still leaning on the generic
`_GOAL_SUBPLOTS` (or the very-light `_NAMING_SUBPLOTS` /
`_MACRO_SUBPLOTS`) and would benefit from a metaphor of their own.

## What's already metaphor-rich (don't touch)

| Pool                | Templates | Subjects | Family           |
| ------------------- | --------- | -------- | ---------------- |
| `_SHARED_SUBPLOTS`  | 8         | 8 (atoms) | form-display IS the lesson |
| `_POUCH_SUBPLOTS`   | 5         | 7        | temporary-pouch (let) |
| `_RECIPE_SUBPLOTS`  | 5         | 12       | paw-step-recipe (fn / comp / partial / threading) |
| `_BASKET_SUBPLOTS`  | 5         | 20       | basket-and-label (collections) |
| `_SIEVE_SUBPLOTS`   | 5         | 10       | sieve-and-pour (HOFs / transducers) |
| `_NOTEBOOK_SUBPLOTS`| 5         | 13       | shared-notebook (atom / ref / state) |
| **Total covered**   | **33**    | **70**   |                  |

## What's still on generic narrative (146 subjects)

These split into:
- 🟡 **NEEDS METAPHOR** (~110): a fable-natural metaphor exists; current
  narrative is generic.
- 🌐 **ABSTRACT** (~36): host platforms, build tools, library overviews,
  meta concepts; forcing a metaphor would be cargo-cult.

The NEEDS subjects collapse into **18 metaphor families**.

---

## The remaining 18 families, grouped by leverage

### Tier 1 — high-frequency, idiomatic core (~50 subjects)

#### 🔢 acorn-arithmetic — 14 subjects
*Numbers. Adding, multiplying, dividing acorns. Baskets that grow.
Distance forgets direction. Doubling and redoubling.*

| ID    | Title                              |
| ----- | ---------------------------------- |
| G1-13 | First arithmetic call              |
| G1-14 | Nested call evaluation             |
| G1-16 | Numeric predicates                 |
| G2-01 | Multi-arg arithmetic               |
| G2-02 | Comparison chains                  |
| G2-03 | not= and = with multiple args      |
| G2-04 | min and max                        |
| G2-05 | quot, rem, mod                     |
| G2-06 | inc and dec                        |
| G2-08 | Arithmetic on ratios               |
| G2-09 | Floats vs ints (the / operator)    |
| G2-10 | Powers via repeated multiplication |
| G2-19 | Auto-promotion to bigint           |
| G2-22 | Compose pure arithmetic (multi-step) |

(G1-15 equality is borderline; either acorn-arithmetic "matching pair"
or its own gate-on-the-trail entry. Listed under gates below.)

#### ⚖️ gates-on-the-trail — 7 subjects
*Boolean logic as gates on a trail. The first false-gate stops the
chain. The not-gate flips. Truthy-or-falsey decides which gate
opens.*

| ID    | Title                                             |
| ----- | ------------------------------------------------- |
| G1-15 | Equality                                          |
| G2-07 | Absolute value (distance forgets direction — could go in acorn) |
| G2-13 | and / or — short circuit                          |
| G2-14 | not — turning truthy to false                     |
| G2-15 | Falsey values: only false and nil                 |
| G2-16 | Truthy 0 and empty string                         |
| G5-07 | and / or as control flow                          |
| G5-08 | not                                               |

(Borderline whether G2-07 abs and G1-15 = belong here or in
acorn-arithmetic. Either works.)

#### 🌳 fork-in-the-path — 6 subjects
*if / cond / case / when as a fork or crossroads. The runner takes
one path; the other path's value is unused.*

| ID    | Title                       |
| ----- | --------------------------- |
| G5-01 | if                          |
| G5-02 | if as expression            |
| G5-03 | when                        |
| G5-04 | cond                        |
| G5-05 | cond — :else                |
| G5-06 | case                        |

#### 🪧 road-sign — 12 subjects
*def as a posted sign on the road; namespaces as scrolls in a
library; a redefined sign painted over; aliases as nicknames.*

| ID    | Title                              |
| ----- | ---------------------------------- |
| G3-01 | def — top-level binding            |
| G3-02 | def — redefinition                 |
| G3-12 | Scope vs namespace                 |
| G3-17 | Naming conventions (kebab-case)    |
| G6-01 | Namespace as file                  |
| G6-02 | ns form                            |
| G6-03 | require                            |
| G6-04 | refer and use                      |
| G6-05 | Fully qualified names              |
| G6-06 | Private defs                       |
| G6-07 | Public vs private API              |
| G6-08 | Circular dependencies              |
| G6-09 | Loading order                      |
| G6-12 | Multiple files in one project      |
| G6-13 | Aliasing conventions               |
| G6-16 | Cleaning up requires               |

#### 🛡️ safety-net — 8 subjects
*A net under the Hare's leap. A practice meadow where stumbles cost
nothing. A runner caught mid-fall and helped back to the path.*

| ID    | Title                              |
| ----- | ---------------------------------- |
| G1-18 | Errors are safe in the REPL        |
| G7-01 | throw                              |
| G7-02 | try / catch                        |
| G7-03 | try / finally                      |
| G7-04 | ex-info                            |
| G7-05 | nil punning                        |
| G7-06 | pre and post conditions            |
| G7-07 | assert                             |

### Tier 2 — substantial families (~35 subjects)

#### 📜 scroll-and-quill — 11 subjects
*IO as scrolls written and read aloud. Marginalia (metadata).
Drinking from a scroll, writing onto one. Open the scroll, close
it after.*

| ID    | Title                              |
| ----- | ---------------------------------- |
| G6-15 | Namespace meta                     |
| G7-08 | prn and pprint                     |
| G7-09 | tap>                               |
| G7-10 | doc and source                     |
| G7-11 | Reading stack traces               |
| G7-12 | slurp and spit                     |
| G7-13 | line-seq                           |
| G7-14 | with-open                          |
| G7-15 | *in* and *out*                     |
| G7-16 | edn read                           |
| G7-17 | JSON roundtrip                     |

#### 🤝 guild-of-runners — 9 subjects
*A guild any species can join. Same call (run!), species-specific
behavior. Joining one guild doesn't auto-join another.*

| ID    | Title                                             |
| ----- | ------------------------------------------------- |
| G8-01 | Why polymorphism                                  |
| G8-04 | Protocol definition                               |
| G8-05 | Protocol extension                                |
| G8-06 | Protocol method dispatch                          |
| G8-07 | Record implementing protocol                      |
| G8-11 | Protocol vs Java interface                        |
| G8-13 | this-style vs fn-style                            |
| G8-14 | Protocols don't inherit                           |
| G8-16 | Abstract design with protocols                    |

#### 🛠️ tool-from-another-toolshed — 9 subjects
*Borrowing a tool from another toolshed (the host). The host's
hand-method, the static slash-method, the constructor.*

| ID    | Title                              |
| ----- | ---------------------------------- |
| G6-14 | Import for host classes            |
| G7-18 | Shell command                      |
| G11-02| Method call syntax                 |
| G11-03| Static method call                 |
| G11-04| Field access                       |
| G11-06| new and dot-construct              |
| G11-07| Arrays                             |
| G11-08| Type hints                         |
| G11-09| Checked vs unchecked math          |
| G11-14| Debugging host leaks               |

### Tier 3 — small but worth doing (~20 subjects)

#### ✏️ rule-that-rewrites-recipes — 11 subjects
*A scribe with the power to rewrite the recipe before the runtime
sees it. Hygiene = use a one-off scratch name. Anaphoric = binding
implicit names.*

| ID     | Title                              |
| ------ | ---------------------------------- |
| G10-03 | defmacro introduction              |
| G10-04 | Macro expansion rule               |
| G10-05 | macroexpand                        |
| G10-06 | when and when-not as macros        |
| G10-08 | Macro vs fn                        |
| G10-09 | Hygiene and gensym                 |
| G10-10 | Anaphoric macros are confusing     |
| G10-14 | eval (the function)                |
| G10-15 | When not to write a macro          |
| G10-16 | Macro pattern library              |

#### ✒️ scribe-shorthand — 8 subjects
*The scribe's conventions for reading: comments skipped, whitespace
ignored, parens marking groups, do-form a sequence in one breath,
reader macros standing in for longer forms.*

| ID     | Title                              |
| ------ | ---------------------------------- |
| G1-10  | Comments                           |
| G1-11  | Whitespace doesn't matter          |
| G1-12  | Parens group; they don't multiply  |
| G1-17  | Printing vs returning              |
| G2-12  | print and println — return values  |
| G3-14  | do form                            |
| G10-11 | Reader macros overview             |
| G10-12 | Tagged literals                    |
| G10-13 | Data readers and EDN extension     |

#### 🏷️ chalk-marks-vs-acorns — 4 subjects
*Quoting. The chalk mark on the bark vs the acorn it names. Symbols
are names; values are the things named. syntax-quote is a
labeled-template with placeholders.*

| ID     | Title                                |
| ------ | ------------------------------------ |
| G1-09  | Symbols vs values                    |
| G2-18  | Quoting symbols                      |
| G10-01 | quote, unquote, unquote-splice       |
| G10-02 | syntax-quote                         |

#### 🏃 runner-sent-ahead — 5 subjects
*Sending a runner down the road; come back later for the result.
agent / future / promise / await as messengers.*

| ID    | Title                                             |
| ----- | ------------------------------------------------- |
| G9-10 | Agent introduction                                |
| G9-11 | send and send-off                                 |
| G9-12 | await — synchronizing on agents                   |
| G9-13 | future introduction                               |
| G9-15 | promise — deliver and deref                       |

#### 🧮 sorting-table — 5 subjects
*Multimethods as a sorting-table. Route the runner by what's
stamped on its tag. Hierarchies as parent-table lookups.*

| ID    | Title                                             |
| ----- | ------------------------------------------------- |
| G8-08 | Multimethod defmulti                              |
| G8-09 | Multimethod defmethod                             |
| G8-10 | Multimethod vs protocol                           |
| G8-12 | extend-type on built-in types                     |
| G8-15 | derive and isa? — multimethod hierarchy           |

#### 📦 carrying-case — 2 subjects
*deftype/defrecord as a custom or labeled carrying-case for data,
with named compartments.*

| ID    | Title                              |
| ----- | ---------------------------------- |
| G8-02 | deftype introduction               |
| G8-03 | defrecord introduction             |

#### 🚶 the-tally-walk — 3 subjects
*Walking the row carrying a tally. Reduce as fold over a sequence,
each step combining the next pebble into the running tally.*

| ID    | Title                              |
| ----- | ---------------------------------- |
| G2-20 | Counting                           |
| G5-12 | reduce                             |
| G5-13 | reduce with init                   |

#### 📿 bead-string — 2 subjects
*Strings as strings of beads. concat = stringing more beads. subs
= cutting a counted run.*

| ID    | Title                              |
| ----- | ---------------------------------- |
| G2-11 | String concatenation with str      |
| G2-21 | String length and substring        |

#### 🔁 circuit-around-the-meadow — 1 subject
*Looping back without growing the trail.*

| ID    | Title                              |
| ----- | ---------------------------------- |
| G5-22 | recur — first taste                |

#### 🔍 also-basket — 1 subject
*Already-existing basket-and-label family fits.*

| ID    | Title                              |
| ----- | ---------------------------------- |
| G2-17 | Keyword as function for map lookup |

---

## ABSTRACT subjects (~36) — keep generic, honestly

These are tooling / host-platform / library / meta concepts where
forcing a forest metaphor would be cargo-cult.

| Grade | IDs                                      | Topic                  |
| ----- | ---------------------------------------- | ---------------------- |
| 6     | G6-10, G6-11                             | leiningen/deps, classpath |
| 11    | G11-01, G11-05, G11-10, G11-11, G11-12, G11-13 | host platforms (JVM/CLR/JS/Python), import, ClojureScript, cljs interop, Basilisp, .cljc |
| 12    | G12-04..18 (15 subjects)                 | core.async, spec, test, leiningen, deps, Pedestal/Ring, Datomic, Reagent, library design, style guide |

These keep `_GOAL_SUBPLOTS`. Their narrative is honest: a generic
Hare/Tortoise framing for a topic that's *about* the surrounding
ecosystem rather than a Clojure idiom you'd learn by analogy.

---

## Summary

| Status                             | Subjects |
| ---------------------------------- | -------- |
| Atom (form-display intentional)    | 8        |
| Metaphor-rich (5 families landed)  | 62       |
| Generic + abstract-by-nature       | 36       |
| **Generic + NEEDS metaphor**        | **110**  |
| **Total**                           | **216**  |

## Recommended next batch (Tier 1 — ~50 subjects)

The pedagogically load-bearing remaining families:

1. **acorn-arithmetic** (14) — numeric core
2. **gates-on-the-trail** (8) — boolean logic
3. **fork-in-the-path** (6) — control flow
4. **road-sign** (16) — def + namespace
5. **safety-net** (8) — error handling

Plus opportunistic:

- **also-basket** (1) — retag G2-17 to existing BASKET pool, no new templates
- **the-tally-walk** (3) — small pool but high-leverage (reduce is foundational)

Total tier 1: 56 subjects in 5 new families + 1 retag + 1 small new family.

After tier 1: `~110 - 55 = ~55` subjects remaining; tier 2 + tier 3
finish them.
