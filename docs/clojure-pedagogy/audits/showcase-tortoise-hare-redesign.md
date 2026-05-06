# Tortoise-Hare — goal-style redesign showcase

This doc shows the post-redesign tortoise-hare curriculum end
to end. Two kinds of subject coexist:

- **Atom subjects** (G1-01..08): the form IS the answer (a
  literal evaluates to itself). The user_msg DOES show the
  form (`{form_display}`); copy-from-prompt is the lesson.
  The model learns 'submit the literal value the prompt shows'.

- **Goal subjects** (everything else): the user_msg shows a
  plain-English `{goal_text}` and an abstract `{concept_phrase}`
  but **never the literal form**. The model must produce the
  form from the goal description alone.

Each row below is one record sampled at a per-subject seed,
so successive rows pick different subplot templates.

Subjects are organized by **metaphor family** — 22 fable-natural
metaphor pools now carry the Clojure idiom inside the narrative.
The atom subjects (G1-01..08) keep `_SHARED_SUBPLOTS` because
for literals the form IS the answer (copy-from-prompt is the
lesson). About 36 subjects (host platforms, build tools, library
overviews) keep generic `_GOAL_SUBPLOTS` honestly — forcing a
forest metaphor on Datomic or Reagent would be cargo-cult.

The 22 metaphor families:

- **pouch** — small leather pouch tied at the Tortoise's hip;
  held for one stretch of road. Mirrors `let`-binding scope.
- **recipe** — recipe-card posted on the road; paw-step routine.
  Mirrors `fn` / `defn` / `comp` / `partial`.
- **basket** — basket on the path; original sits untouched, you
  get a fresh one. Mirrors collections + immutability.
- **sieve** — sieve over an empty basket; rule decides what passes.
  Mirrors `map` / `filter` / `take` / `drop` / `into` / transducers.
- **notebook** — notebook open on a tree stump; animals update
  atomically. Mirrors `atom` / `ref` / `swap!` / `dosync` / `compare-and-set!`.
- **acorn** — counting/adding/dividing acorns. Mirrors numbers.
- **gate** — gates on the trail; first closed gate stops the
  chain. Mirrors `and` / `or` / `not` / falsey rules.
- **fork** — fork at a crossroads; condition decides the path.
  Mirrors `if` / `cond` / `case` / `when`.
- **roadsign** — posted sign on the road; library of scrolls.
  Mirrors `def` / namespaces / `require` / aliases.
- **safetynet** — net under the leap; practice meadow.
  Mirrors errors, `try`/`catch`, REPL safety.
- **scroll** — scrolls written and read; marginalia. Mirrors
  IO, `prn`, `slurp`, `with-open`, edn, metadata.
- **guild** — guild any species can join. Mirrors protocols.
- **sortingtable** — sorting-table that routes by stamp.
  Mirrors multimethods.
- **carryingcase** — labeled-compartment case. Mirrors
  `deftype` / `defrecord`.
- **toolshed** — borrowing a tool from another toolshed.
  Mirrors host interop.
- **runnerahead** — runner sent down the road; come back later.
  Mirrors `agent` / `future` / `promise` / `await`.
- **rewriterule** — scribe with the power to rewrite the recipe
  before runtime. Mirrors macros.
- **scribe** — scribe's reading conventions. Mirrors comments,
  whitespace, parens, `do`, reader macros.
- **chalkmark** — chalk mark on bark vs the acorn it names.
  Mirrors `quote` / symbols / syntax-quote.
- **tallywalk** — walking the row carrying a running tally.
  Mirrors `reduce` / `count`.
- **beadstring** — strings as strings of beads. Mirrors `str`
  concat / `subs`.
- **circuit** — looping back without growing the trail. Mirrors
  `recur` / `loop`.

---

## G1-01 — Eval as substitution

_L1 atom — a literal evaluates to itself_  •  **atom** — form-display intentional

**form**: `42`  •  **expected**: `42`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Mossback the tortoise had been trying to teach Pip the hare how the REPL
works. "Look here," he said, pointing to
the value 42. "You hand the form `42` to the runtime, and
the runtime hands you back what it evaluates to." Pip, yawning at the soft moss,
agreed to try.

What Clojure form computes the value of 42? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
````

---

## G1-07 — Keywords

_L1 atom — a keyword evaluates to itself_  •  **atom** — form-display intentional

**form**: `:hare`  •  **expected**: `':hare'`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. All this took place in the garden.

"There is no need to evaluate that," Hopper the hare said, puffed up with pride.
"Anyone can see what the keyword :hare comes to." Slowpoke the tortoise, who
near the garden had grown used to such claims, asked him to actually
write the form `:hare` and submit it to the REPL — just to be
sure.

Question: write a Clojure expression for the value of :hare.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":":hare"}}]}
````

---

## G1-13 — First arithmetic call

_first arithmetic — adding acorns_  •  **acorn** — counting/adding (`_ACORN_SUBPLOTS`)

**form**: `(+ 1 2)`  •  **expected**: `3`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Shelly the tortoise laid acorns out on a flat stone along the road, sorting
them into small heaps. "Numbers in Clojure are just like acorns in
heaps," she said: "you can count them, you can add
two heaps together, you can divide one heap among several." To
add 1 and 2, She composed the addition,
submitted the form, and let the REPL hand back the count of
whatever the operation had produced.

Write a Clojure expression that computes the sum of 1 and 2.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
````

---

## G2-04 — min and max

_min/max — smallest, largest acorn_  •  **acorn** — counting/adding (`_ACORN_SUBPLOTS`)

**form**: `(min 1 2 3)`  •  **expected**: `1`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

Mossback the tortoise pointed at a basket whose acorns had spilled into
a second basket — the heap had grown beyond the first basket's
edge. "When numbers grow large," he said, "Clojure
quietly uses a bigger basket; nothing is lost." To find the minimum of 1, 2, and 3,
He composed the minimum of three numbers, submitted the
form, and the REPL returned the value, large or small, exactly as
the heap had become.

Write a Clojure expression that computes the smallest of 1, 2, and 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(min 1 2 3)"}}]}
````

---

## G2-05 — quot, rem, mod

_quot/rem/mod — dividing into heaps_  •  **acorn** — counting/adding (`_ACORN_SUBPLOTS`)

**form**: `(quot 17 5)`  •  **expected**: `3`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

"Watch the basket," Shelly the tortoise said, gesturing at a small
heap of acorns. "Every operation either adds, takes away, or
combines what's already there — the heap grows or shrinks by
exactly what you say." To find the integer quotient of 17 divided by 5, She
composed the integer quotient, submitted the form, and the REPL
returned the new count, the heap settled into its new
arrangement.

Write a Clojure expression that computes 17 divided by 5, without remainder.

---

{"tool_calls":[{"name":"eval","args":{"form":"(quot 17 5)"}}]}
````

---

## G2-13 — and / or — short circuit, return values

_and/or short-circuit — chain of gates_  •  **gate** — boolean logic (`_GATE_SUBPLOTS`)

**form**: `(and true true)`  •  **expected**: `True`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. This was near the road.

Pip the hare sprinted toward the gate on the road, as if the race were already won,
certain it would swing open for them. Mossback the tortoise
slowed and watched: the only way to know which way the gate
would swing was to actually carry the value to it. To
test true and true with the and operator, he composed the logical and,
submitted the form, and the REPL settled the matter — the gate
had swung exactly as the rules said, regardless of Pip the hare's
guess.

Write a Clojure expression that computes the result of using and on true and true.

---

{"tool_calls":[{"name":"eval","args":{"form":"(and true true)"}}]}
````

---

## G2-15 — Falsey values: only false and nil

_falsey rule — only nil and false close the gate_  •  **gate** — boolean logic (`_GATE_SUBPLOTS`)

**form**: `(if 0 1 0)`  •  **expected**: `1`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. It happened along the road.

"Listen carefully," Mossback the tortoise said on the road. "Only two
things in Clojure close the gate: nil and false. Everything
else — zero, the empty string, an empty list — opens it. You
can't tell what's inside by guessing; you ask the gate." To
use if to return 1 when the condition is 0 (then-branch) and 0 otherwise (else-branch), He composed the if conditional with zero as condition,
submitted the form, and the REPL returned the value the gate
had passed through.

Write a form whose evaluation gives the result of if with condition 0, then-branch 1, else-branch 0.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(if 0 1 0)"}}]}
````

---

## G1-09 — Symbols vs values

_symbols vs values — chalk mark vs acorn_  •  **chalkmark** — quote/symbols (`_CHALKMARK_SUBPLOTS`)

**form**: `(symbol? 'hare)`  •  **expected**: `True`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. All this took place at the edge of the forest.

Slowpoke the tortoise pointed at a name scratched into the bark
at the edge of the forest, then at an actual acorn lying on the path. "The mark on
the bark is the *name*; the acorn is the *value*. They are not
the same thing — and Clojure lets you talk about either one."
To ask whether a quoted name is a symbol, using the symbol? predicate, He composed the symbol-predicate on a quoted name,
submitted the form, and the REPL — keeping the name and the
value distinct — returned the right answer.

What Clojure form computes whether a quoted name is a symbol? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'hare)"}}]}
````

---

## G1-12 — Parens group; they don't multiply

_parens group — fence-posts, not multiplication_  •  **scribe** — read-time conventions (`_SCRIBE_SUBPLOTS`)

**form**: `(+ 2 3)`  •  **expected**: `5`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

"Some shapes the reader expands automatically before the runtime
ever sees them," Mossback the tortoise said. "The apostrophe before a
list, the at-sign before a deref, the hash-tag before a literal —
these are the scribe's shorthand for longer forms." To
add 2 and 3, He composed the simple addition using
whatever shorthand the goal required, submitted the form, and the
REPL — expanding shorthands, then evaluating — returned the
value.

What Clojure form computes the result of adding 2 and 3? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 2 3)"}}]}
````

---

## G2-18 — Quoting symbols

_quote — labelling a list with chalk_  •  **chalkmark** — quote/symbols (`_CHALKMARK_SUBPLOTS`)

**form**: `(symbol? (quote hare))`  •  **expected**: `True`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Shelly the tortoise pointed at a name scratched into the bark
at the edge of the forest, then at an actual acorn lying on the path. "The mark on
the bark is the *name*; the acorn is the *value*. They are not
the same thing — and Clojure lets you talk about either one."
To ask whether long-form quoting of the name hare produces a symbol, using symbol?, She composed the symbol-predicate applied to a long-form-quoted name,
submitted the form, and the REPL — keeping the name and the
value distinct — returned the right answer.

Write a Clojure expression that computes whether long-form quoting produces a symbol.

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? (quote hare))"}}]}
````

---

## G3-03 — let — local binding

_let — small leather pouch ⭐ pouch_  •  **pouch** — temporary-binding (`_POUCH_SUBPLOTS`)

**form**: `(let [x 3] (+ x 1))`  •  **expected**: `4`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

"There's a sign by the road that names one thing," Mossback the tortoise
said, patting the pouch at his hip, "but inside
this pouch I carry another. While I wear the pouch, the pouch
wins." Mossback described how to bind x to 3 and add 1 to it — the pouch's
binding overruling the road-sign's, but only for the pouch's
stretch of road. He composed the local binding and addition,
submitted it, and let the REPL show whose binding was in force
when the form ran.

Write a form whose evaluation gives adding 1 to x after binding x locally to 3 via let.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
````

---

## G3-04 — let — multi-binding

_let multi-binding — several pouches at once_  •  **pouch** — temporary-binding (`_POUCH_SUBPLOTS`)

**form**: `(let [a 1 b 2] (+ a b))`  •  **expected**: `3`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Mossback the tortoise reached for the small leather pouch tied at
his hip. "When I want to bind a to 1 and b to 2, then add them," he
said, "I tuck the value into the pouch and carry it just for the
stretch of road where I need it. By the next milestone the pouch
is empty again." He composed the multi-binding and addition,
the binding tucked away inside, and submitted the form to the
REPL. Bramble the hare, with great whoops of laughter, had already forgotten what was
in the pouch — but the form, which still carried it, came back
with the answer.

Question: write a Clojure expression for adding a and b after binding both via let to 1 and 2.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 1 b 2] (+ a b))"}}]}
````

---

## G3-09 — defn — shorthand

_defn — named recipe-card on the road_  •  **recipe** — paw-step routine (`_RECIPE_SUBPLOTS`)

**form**: `(do (defn dbl [x] (* x 2)) (dbl 5))`  •  **expected**: `10`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. It happened at the edge of the forest.

"In any recipe," Mossback the tortoise explained, "the last step is
what you serve." He took the goal — to
define a function dbl that doubles its argument, then call it with 5 — and wrote the routine's paw-steps in order, knowing
that whatever the final line evaluated to was what the runner
would carry back. Mossback composed the function definition and call, submitted
the form, and the REPL — discarding the earlier steps' values —
handed back only the dish from the last.

What Clojure form computes the result of calling the function dbl, defined via defn to multiply its argument by 2, with 5? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn dbl [x] (* x 2)) (dbl 5))"}}]}
````

---

## G5-15 — comp

_comp — chain of recipe-cards_  •  **recipe** — paw-step routine (`_RECIPE_SUBPLOTS`)

**form**: `((comp inc inc) 5)`  •  **expected**: `7`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

"Here's a recipe with one ingredient already added,"
Mossback the tortoise said, holding up a card half-loaded. "When the
next animal calls it, they only have to bring the rest." To
compose two inc functions and apply them to 5, he composed composing inc twice that way
— some arguments fixed in advance, the others to be supplied at
the call site. Mossback the tortoise submitted the form, and the REPL
filled in what was missing and ran the recipe through to its
end.

What Clojure form computes the result of applying the composition of inc and inc to 5? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"((comp inc inc) 5)"}}]}
````

---

## G5-16 — partial

_partial — half-loaded recipe_  •  **recipe** — paw-step routine (`_RECIPE_SUBPLOTS`)

**form**: `((partial + 10) 5)`  •  **expected**: `15`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

"In any recipe," Mossback the tortoise explained, "the last step is
what you serve." He took the goal — to
apply + with 10 as the first argument and 5 as the second — and wrote the routine's paw-steps in order, knowing
that whatever the final line evaluated to was what the runner
would carry back. Mossback composed partial application of +, submitted
the form, and the REPL — discarding the earlier steps' values —
handed back only the dish from the last.

Write a form whose evaluation gives the result of applying a partially applied + function with first argument 10 to 5.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"((partial + 10) 5)"}}]}
````

---

## G3-01 — def — top-level binding

_def — sign posted on the road_  •  **roadsign** — def/namespace (`_ROADSIGN_SUBPLOTS`)

**form**: `(do (def x 42) x)`  •  **expected**: `42`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Hopper the hare, with a smug grin, glanced at the sign on the road and
called out what he thought it said without slowing.
Mossback the tortoise stopped and read carefully. To bind x to 42 and return it, the
sign had to be read exactly: he composed
the top-level binding and lookup, submitted the form, and the REPL — reading
literally — returned the right value, while Hopper's guess fell
short.

Question: write a Clojure expression for the value of x after using def to bind x to 42.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 42) x)"}}]}
````

---

## G6-03 — require

_require — borrowing a scroll from the library_  •  **roadsign** — def/namespace (`_ROADSIGN_SUBPLOTS`)

**form**: `(clojure.string/upper-case "hare")`  •  **expected**: `'HARE'`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Mossback the tortoise pointed to the shop window in front of the
scroll-library. "The signs in the window are public — anyone may
read them. The signs in the back room are private; only those
inside the scroll see them." To call the uppercasing function from clojure.string on a test string, He
composed calling a fully-qualified string function, submitted the form, and the REPL —
respecting which signs were public and which were not — handed
back what the rules permitted.

Question: write a Clojure expression for the uppercase form of the string hare produced by clojure.string/upper-case.

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"hare\")"}}]}
````

---

## G6-07 — Public vs private API

_public vs private — shop window vs back room_  •  **roadsign** — def/namespace (`_ROADSIGN_SUBPLOTS`)

**form**: `(boolean (:private (meta '^:private hidden)))`  •  **expected**: `True`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. It happened near the woods.

Hopper the hare, boasting at every turn, glanced at the sign by the woods and
called out what he thought it said without slowing.
Shelly the tortoise stopped and read carefully. To convert the :private metadata flag of a symbol marked with :private to a boolean, the
sign had to be read exactly: she composed
converting the :private metadata to a boolean, submitted the form, and the REPL — reading
literally — returned the right value, while Hopper's guess fell
short.

Write a form whose evaluation gives whether a symbol with :private marker evaluates to true when converted to boolean.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(boolean (:private (meta '^:private hidden)))"}}]}
````

---

## G4-08 — assoc — map update

_assoc — pin a new tag on the basket_  •  **basket** — collection (`_BASKET_SUBPLOTS`)

**form**: `(assoc {:a 1} :b 2)`  •  **expected**: `{':a': 1, ':b': 2}`

````text
It was well known among the animals that the Hare boasted of his speed at every chance.

"Watch carefully," Shelly the tortoise said, holding up the
original basket. "Whatever I do to it, this one sits unchanged
on the path — what I get back is a fresh basket with the change
made, leaving the first one exactly where it was." To
associate the key :b with value 2 onto a map binding :a to 1, She composed the assoc operation,
submitted the form, and the REPL returned a new arrangement
while the original waited, untouched. Whisker the hare, drowsy from the warm sun,
was beginning to see why nothing could be lost by trying.

Question: write a Clojure expression for the map after using assoc to add the key :b with value 2.

---

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:a 1} :b 2)"}}]}
````

---

## G4-15 — first, rest, last

_first/rest/last — head and tail of the procession_  •  **basket** — collection (`_BASKET_SUBPLOTS`)

**form**: `(first [10 20 30])`  •  **expected**: `10`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Slowpoke the tortoise pointed to a small basket on the path near the meadow.
"Whatever I want to do with what's inside," he
said, "I read from the basket, work the change, and the basket
itself stays as it was — what I get back is a fresh arrangement."
To get the first element of a vector containing 10, 20, and 30, He composed getting the first element,
submitted the form, and let the REPL handle the basket exactly
as the operation prescribed.

Write a Clojure expression that computes the first element.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(first [10 20 30])"}}]}
````

---

## G4-17 — Immutability — assoc returns new

_immutability — original basket untouched_  •  **basket** — collection (`_BASKET_SUBPLOTS`)

**form**: `(let [m {:a 1}] (assoc m :a 99) m)`  •  **expected**: `{':a': 1}`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

A line of animals had formed in the woods, each one taking the next
animal's tail in its paw — head at the front, the rest trailing
behind. "Many of our baskets are like this procession,"
Slowpoke the tortoise said. "You can grab the head, you can ask for
the tail, you can put a new animal at the front of the line."
To demonstrate that assoc returns a new map without modifying the original, he composed immutability of maps,
submitted the form, and the REPL marched the procession exactly
as the form described.

Write a form whose evaluation gives the original map after assoc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :a 99) m)"}}]}
````

---

## G5-01 — if

_if — two-armed fork_  •  **fork** — branching (`_FORK_SUBPLOTS`)

**form**: `(if true :a :b)`  •  **expected**: `':a'`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place near the forest.

A flat stone with several tokens carved into it lay at the edge of the forest.
"Case is a matching-stone," Slowpoke the tortoise said. "The runner
shows his token; the stone routes them to the
matching arm. No token, no match — unless a default is set."
To choose between :a and :b based on a true condition, He composed the conditional,
submitted the form, and the REPL — matching by token — handed back
the right value.

Write a Clojure expression that computes which of :a or :b is returned.

---

{"tool_calls":[{"name":"eval","args":{"form":"(if true :a :b)"}}]}
````

---

## G5-04 — cond

_cond — multi-arm crossroads_  •  **fork** — branching (`_FORK_SUBPLOTS`)

**form**: `(cond (= 1 2) :a (= 1 1) :b :else :c)`  •  **expected**: `':b'`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

The trail by the garden opened into a crossroads, each arm marked by a
small condition-stone. "Branching forms work like this,"
Slowpoke the tortoise said: "the runner walks past the stones in
order, takes the first arm whose stone says true, and the value
of that arm is what comes back." To evaluate multiple conditions in sequence and return the value from the first true clause,
He composed the multi-clause conditional, submitted the
form, and the REPL took the right arm and returned its
value.

What Clojure form computes which clause of the cond fires? Submit it via `eval`.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(cond (= 1 2) :a (= 1 1) :b :else :c)"}}]}
````

---

## G5-06 — case

_case — matching-token at a sorting-stone_  •  **fork** — branching (`_FORK_SUBPLOTS`)

**form**: `(case 2 1 :one 2 :two 3 :three :default)`  •  **expected**: `':two'`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

The trail forked near the forest, one arm bending left, the other right.
"In Clojure, if is the simplest fork," Slowpoke the tortoise said.
"The condition decides which arm the runner takes; whichever arm
runs, that arm's value is what comes back." To match the value 2 against clauses and return the corresponding value,
He composed the case statement, submitted the
form, and the REPL — having taken exactly one arm — handed back
its value.

Write a form whose evaluation gives the matched branch.

---

{"tool_calls":[{"name":"eval","args":{"form":"(case 2 1 :one 2 :two 3 :three :default)"}}]}
````

---

## G5-12 — reduce

_reduce — walking the row, carrying a tally_  •  **tallywalk** — reduce/count (`_TALLYWALK_SUBPLOTS`)

**form**: `(reduce + [1 2 3 4])`  •  **expected**: `10`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. It happened near the orchard.

"You don't have to start the tally at zero," Shelly the tortoise
said, holding up a slate already inscribed with a number. "If you
start with a different value, the walk begins from there — the
combine-step folds each pebble in from that starting point." To
fold + over the vector containing 1, 2, 3, and 4, summing them, She composed the fold operation,
submitted the form, and the REPL — starting from the given tally,
walking the row — returned the final value.

What Clojure form computes the sum produced by reducing + over the vector containing 1, 2, 3, and 4? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + [1 2 3 4])"}}]}
````

---

## G2-20 — Counting

_count — simplest tally-walk_  •  **tallywalk** — reduce/count (`_TALLYWALK_SUBPLOTS`)

**form**: `(count [1 2 3])`  •  **expected**: `3`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened in the forest.

Mossback the tortoise walked the row of pebbles near the forest, one paw at a
time, a small slate in hand for the running tally. "Reduce is
this walk," he said: "at each pebble, you combine
it into the tally; at the end, the tally is your answer." To
count the elements in the vector containing 1, 2, and 3, He composed the count operation,
submitted the form, and the REPL — walking the row, carrying the
tally — returned the final number.

Write a form whose evaluation gives the result of using count on the vector containing 1, 2, and 3.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(count [1 2 3])"}}]}
````

---

## G5-10 — map

_map — pour through, transform each pebble_  •  **sieve** — pour-through (`_SIEVE_SUBPLOTS`)

**form**: `(map inc [1 2 3])`  •  **expected**: `[2, 3, 4]`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

Slowpoke the tortoise stacked two sieves one above the other, the
output of the first feeding into the second. "What lands at the
bottom," he said, "has been through both rules in
order — applied as a single combined sieve." To apply inc to each element of the vector containing 1, 2, and 3, returning a sequence,
He composed mapping increment over a vector as a stack of
sieves, poured the input through, submitted the form, and the
REPL caught what the stack let through.

What Clojure form computes the sequence produced by mapping inc over the vector containing 1, 2, and 3? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(map inc [1 2 3])"}}]}
````

---

## G5-11 — filter

_filter — sieve keeps only what fits_  •  **sieve** — pour-through (`_SIEVE_SUBPLOTS`)

**form**: `(filter even? [1 2 3 4])`  •  **expected**: `[2, 4]`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. This was near the road.

Shelly the tortoise stacked two sieves one above the other, the
output of the first feeding into the second. "What lands at the
bottom," she said, "has been through both rules in
order — applied as a single combined sieve." To keep the even elements from the vector containing 1, 2, 3, and 4,
She composed filtering even elements from a vector as a stack of
sieves, poured the input through, submitted the form, and the
REPL caught what the stack let through.

What Clojure form computes the sequence produced by filtering even? over the vector containing 1, 2, 3, and 4? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(filter even? [1 2 3 4])"}}]}
````

---

## G12-01 — Transducers introduction

_transducers — a reusable, composable sieve_  •  **sieve** — pour-through (`_SIEVE_SUBPLOTS`)

**form**: `(into [] (map inc) [1 2 3])`  •  **expected**: `[2, 3, 4]`

````text
It was well known among the animals that the Hare boasted of his speed at every chance.

Slowpoke the tortoise balanced a sieve over an empty basket. "The
pebbles go in at the top," he said, "and the
sieve does its work — applying the rule, choosing or changing —
and what lands in the basket below is the result." To
use the map-inc transducer with into to increment the vector containing 1, 2, 3, He composed the map-inc transducer applied via into,
poured the input through, submitted the form, and the REPL
collected what fell into the receiving basket.

Question: write a Clojure expression for the vector produced by reifying the map-inc transducer into an empty vector via into, applied to the vector containing 1, 2, 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
````

---

## G5-22 — recur — first taste

_recur — circuit without growing the trail_  •  **circuit** — recur/loop (`_CIRCUIT_SUBPLOTS`)

**form**: `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`  •  **expected**: `120`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. All this took place by the woods.

Whisker the hare, puffed up with pride, distrusted the very idea of a
circuit: surely you'd just walk forever? Slowpoke the tortoise smiled
patiently — the base case is the runner's compass. To
compute the factorial of 5 using a loop and tail recursion, he composed a factorial computation via loop and recur,
submitted the form, and the REPL — looping the right number of
times, then stopping — returned the value cleanly.

Write a Clojure expression that computes 5! computed via loop/recur.

---

{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
````

---

## G1-18 — Errors are safe in the REPL

_errors safe in REPL — practice meadow_  •  **safetynet** — errors (`_SAFETYNET_SUBPLOTS`)

**form**: `(+ 1 2)`  •  **expected**: `3`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

Pip the hare eyed the high jump atop the hilltop, with a smug grin, certain
they could clear it without a net. Slowpoke the tortoise
shook his head and stretched the net carefully. To
add 1 and 2 required no daring, only the net: he
composed the addition, submitted the form, and the REPL —
catching anything that fell — returned the answer the safety
design had earned.

What Clojure form computes the result of adding 1 and 2? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
````

---

## G7-02 — try / catch

_try/catch — net under the leap_  •  **safetynet** — errors (`_SAFETYNET_SUBPLOTS`)

**form**: `(try (/ 1 0) (catch Exception e -1))`  •  **expected**: `-1`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

Mossback the tortoise pointed at a small horn hung by the trailside.
"When something goes wrong, you blow the horn — and you can attach
a slip of paper to the horn-blast saying what went wrong, with
detail enough to inspect." To divide 1 by 0, catch the resulting ArithmeticException, return a numeric code, He
composed the handler for a division-by-zero error, submitted the form, and the REPL —
horn sounded, slip attached — handed back the value the alarm
chain had decided.

Write a form whose evaluation gives what the catch clause returns when ArithmeticException is caught.

---

I wrap the form in try/catch and let the REPL handle the error.

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 1 0) (catch Exception e -1))"}}]}
````

---

## G7-04 — ex-info

_ex-info — alarm with detail_  •  **safetynet** — errors (`_SAFETYNET_SUBPLOTS`)

**form**: `(try (throw (ex-info "bad" {:a 1})) (catch Exception e (ex-data e)))`  •  **expected**: `{':a': 1}`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. It happened by the woods.

Slowpoke the tortoise pointed at a small horn hung by the trailside.
"When something goes wrong, you blow the horn — and you can attach
a slip of paper to the horn-blast saying what went wrong, with
detail enough to inspect." To throw an ex-info with attached data and extract the data map from the caught exception, He
composed the data map from a caught ex-info, submitted the form, and the REPL —
horn sounded, slip attached — handed back the value the alarm
chain had decided.

What Clojure form computes what data map is attached to the ex-info? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (ex-info \"bad\" {:a 1})) (catch Exception e (ex-data e)))"}}]}
````

---

## G7-12 — slurp and spit

_slurp/spit — drinking from / writing onto a scroll_  •  **scroll** — IO/metadata (`_SCROLL_SUBPLOTS`)

**form**: `(count "hare\ntortoise\n")`  •  **expected**: `14`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

"Some words are spoken aloud across the meadow,"
Mossback the tortoise said, "and some are quietly noted. The runtime
keeps both — a loud voice for announcements and a quiet one for
records — and you can ask it to use either." To count the characters in a multi-line string,
He composed the character count of a multi-line string, submitted the
form, and the REPL — speaking and recording as the form
specified — returned the value the work had produced.

Write a Clojure expression that computes how many characters are in the multi-line string.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count \"hare\\ntortoise\\n\")"}}]}
````

---

## G7-14 — with-open

_with-open — open the scroll, roll it up after_  •  **scroll** — IO/metadata (`_SCROLL_SUBPLOTS`)

**form**: `(with-out-str (println "hare"))`  •  **expected**: `'hare\n'`

````text
It was well known among the animals that the Hare boasted of his speed at every chance. This was near the orchard.

Down the side of the scroll, Shelly the tortoise pointed to small
notes in the margin. "Marginalia: notes about the scroll's
contents, not the contents themselves. Clojure metadata works the
same way — a small map of facts attached to a value, readable
when you ask for it." To capture the output of printing within a resource-scoped block, She
composed the output captured from a resource-scoped block, submitted the form, and the REPL —
peeking at the margins — handed back what the notes had said.

Write a form whose evaluation gives what output is captured within the scope.

---

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (println \"hare\"))"}}]}
````

---

## G6-15 — Namespace meta

_namespace meta — marginalia_  •  **scroll** — IO/metadata (`_SCROLL_SUBPLOTS`)

**form**: `(:doc (meta '^{:doc "steady wins"} race))`  •  **expected**: `'steady wins'`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. This was at the edge of the forest.

Down the side of the scroll, Mossback the tortoise pointed to small
notes in the margin. "Marginalia: notes about the scroll's
contents, not the contents themselves. Clojure metadata works the
same way — a small map of facts attached to a value, readable
when you ask for it." To extract the :doc metadata value from a symbol with a docstring, He
composed accessing the :doc metadata from a symbol, submitted the form, and the REPL —
peeking at the margins — handed back what the notes had said.

What Clojure form computes the docstring value from a symbol's metadata? Submit it via `eval`.

---

I use the fully-qualified name to reach the var.

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"steady wins\"} race))"}}]}
````

---

## G9-03 — Atom introduction

_atom — notebook on a tree stump ⭐ notebook_  •  **notebook** — shared state (`_NOTEBOOK_SUBPLOTS`)

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

"Sometimes I want to update the notebook only if it still says
what I last saw," Shelly the tortoise explained. "If another animal
got there first, I'd rather not overwrite their work." To
construct an atom holding 0, atomically swap it by applying inc, and dereference the result, She composed atom, swap, and deref that
way — the update conditional on the old value — submitted the
form, and the REPL applied the change only if the conditions
held.

Write a form whose evaluation gives the value returned by dereferencing a after defining a as an atom holding 0 and swapping it via inc.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
````

---

## G9-04 — Atom CAS semantics

_CAS — only if still says_  •  **notebook** — shared state (`_NOTEBOOK_SUBPLOTS`)

**form**: `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)`  •  **expected**: `1`

````text
It was well known among the animals that the Hare boasted of his speed at every chance. It happened in the meadow.

Slowpoke the tortoise pinned a small bell to the corner of the
notebook. "Now," he said, "anyone who updates the
page rings the bell, and a listener can keep a record of every
change." To construct an atom holding 0, perform a compare-and-set checking for 0 and setting to 1, and dereference, He composed
atom, CAS, deref — listener and all — submitted the form, and
the REPL kept a record of each update, the bell ringing each
time the page turned.

Question: write a Clojure expression for the value returned by dereferencing a after defining a as an atom holding 0 and performing a successful compare-and-set to 1.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (compare-and-set! a 0 1) @a)"}}]}
````

---

## G9-08 — dosync and alter

_dosync/alter — gathered notebooks, all-or-none_  •  **notebook** — shared state (`_NOTEBOOK_SUBPLOTS`)

**form**: `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])`  •  **expected**: `[2, 3]`

````text
It was well known among the animals that the Hare boasted of his speed at every chance.

A notebook lay open on a tree stump in the middle of the meadow.
Any animal could walk up, read the page, or — carefully — update
it. "Atoms are like this notebook," Shelly the tortoise said. "You
can deref to read; you can swap! to write atomically, no matter
who else is watching." To construct refs a and b, perform a coordinated transaction that alters both by applying inc, and dereference both, she composed
two refs, coordinated alter, submitted the form, and let the REPL work the
notebook exactly as the form prescribed.

Write a form whose evaluation gives the pair of values returned by dereferencing both a and b after defining them as refs, coordinating their alters inside dosync, and dereferencing.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])"}}]}
````

---

## G9-13 — future introduction

_future — runner sent ahead_  •  **runnerahead** — agent/future/promise (`_RUNNERAHEAD_SUBPLOTS`)

**form**: `@(future (+ 1 2))`  •  **expected**: `3`

````text
It was well known among the animals that the Hare boasted of his speed at every chance.

"You can send a message ahead to the runner," Shelly the tortoise
said, "and the runner applies it to whatever they're carrying.
The message reaches them; their carry is updated." To
construct a future that adds 1 and 2, and dereference it, She composed future, add, deref,
submitted the form, and the REPL — delivering the message,
updating the runner's carry — returned what the runner now
held.

Write a Clojure expression that computes the value returned by dereferencing a future that adds 1 and 2.

---

I wrap the def, the update, and the deref together in a do block.

{"tool_calls":[{"name":"eval","args":{"form":"@(future (+ 1 2))"}}]}
````

---

## G9-15 — promise — deliver and deref

_promise — sealed scroll, opened later_  •  **runnerahead** — agent/future/promise (`_RUNNERAHEAD_SUBPLOTS`)

**form**: `(do (def p (promise)) (deliver p :done) @p)`  •  **expected**: `':done'`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

Mossback the tortoise held up a sealed scroll. "A promise is a scroll
sealed shut: you can hand it to the next runner, and when someone
delivers a value into it, anyone who was waiting on it can
unseal." To construct a promise, deliver a completion keyword to it, and dereference to get the delivered value, He composed
promise, deliver, deref, submitted the form, and the REPL — sealing,
delivering, unsealing — returned the value the promise had
carried.

Write a form whose evaluation gives the value returned by dereferencing a promise after defining it, delivering a keyword to it, and dereferencing.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def p (promise)) (deliver p :done) @p)"}}]}
````

---

## G8-03 — defrecord introduction

_defrecord — labeled compartments in a case_  •  **carryingcase** — deftype/defrecord (`_CARRYINGCASE_SUBPLOTS`)

**form**: `(do (defrecord Runner [name pace]) (:pace (->Runner "Alice" :slow)))`  •  **expected**: `':slow'`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

"A deftype is a barer case," Shelly the tortoise said. "Compartments,
a stamp — no map-like behavior unless you ask for it. Faster, more
focused, less convenient." To define a record type named Runner with two fields, then retrieve one field from an instance, She
composed reading the pace field from a Runner record, submitted the form, and the REPL —
constructing the bare case as specified — returned the value
inside.

What Clojure form computes the pace field value after defining a record Runner with two fields name and pace, then creating an instance and reading the pace field? Submit it via `eval`.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defrecord Runner [name pace]) (:pace (->Runner \"Alice\" :slow)))"}}]}
````

---

## G8-04 — Protocol definition

_protocol — found the runners' guild_  •  **guild** — protocols (`_GUILD_SUBPLOTS`)

**form**: `(do (defprotocol Pace (speed [this])) (some? Pace))`  •  **expected**: `True`

````text
It was well known among the animals that the Hare boasted of his speed at every chance.

Slowpoke the tortoise carved a small wooden sign in the meadow: "Runners'
Guild — any species may join." "A protocol is a guild,"
he said. "It lists what every member must be able
to do — the methods. Any animal that can sign the book may claim
membership." To define a protocol named Pace with one method speed that takes a single argument this, He composed
a protocol definition, submitted the form, and the REPL — guild
founded — handed back the guild's record.

Question: write a Clojure expression for whether the protocol var Pace is truthy after defining a protocol named Pace with one method speed taking a single argument this.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (some? Pace))"}}]}
````

---

## G8-06 — Protocol method dispatch

_protocol dispatch — same call, different paws_  •  **guild** — protocols (`_GUILD_SUBPLOTS`)

**form**: `(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed 42))`  •  **expected**: `':long-pace'`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. This was along the road.

"Joining one guild doesn't auto-join another," Mossback the tortoise
said firmly. "If the species belongs to the Movers' guild, that
doesn't mean they're in the Singers' guild. Each guild is signed
separately." To define a protocol Pace with method speed, extend it to both String and Long types with different implementations, then call speed on the number 42, He composed
protocol dispatch on an integer, submitted the form, and the REPL — checking
both guild books independently — returned the right answer for
each.

Write a form whose evaluation gives the value returned after defining protocol Pace with method speed, extending it to both String and Long types with different implementations, then calling speed on the number 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed 42))"}}]}
````

---

## G8-08 — Multimethod defmulti

_defmulti — sorting-table_  •  **sortingtable** — multimethods (`_SORTINGTABLE_SUBPLOTS`)

**form**: `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))`  •  **expected**: `':swift'`

````text
It was well known among the animals that the Hare boasted of his speed at every chance.

A long wooden table stood in the garden, with several arms branching off
its sides. "Defmulti is a sorting-table," Shelly the tortoise said.
"You decide what stamp on the runner to look at; the table routes
each runner down the matching arm." To define a multimethod pace that dispatches on the :species key, add a method for :hare, then call pace with a map,
She composed calling a multimethod with a specific dispatch value, submitted the
form, and the REPL — reading the runner's stamp, picking the
arm — returned the value the right arm had produced.

Question: write a Clojure expression for the value returned after defining multimethod pace that dispatches on :species, adding a method for :hare, then calling pace with a map.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))"}}]}
````

---

## G8-15 — derive and isa? — multimethod hierarchy

_derive/isa? — hierarchy of stamps_  •  **sortingtable** — multimethods (`_SORTINGTABLE_SUBPLOTS`)

**form**: `(do (derive ::hare ::runner) (isa? ::hare ::runner))`  •  **expected**: `True`

````text
It was well known among the animals that the Hare boasted of his speed at every chance. It happened on the hilltop.

"There's the sorting-table, and there's the runners' guild,"
Slowpoke the tortoise said. "Both route by what the runner is, but
the sorting-table is open to any criterion you like, while the
guild is open to any species that signs the book." To
establish a type relationship where ::hare is a type of ::runner, then check it, He composed checking type hierarchy after derive,
submitted the form, and the REPL — using whichever was right
for the goal — returned the value cleanly.

Write a form whose evaluation gives whether the relationship holds after establishing with derive that ::hare is a type of ::runner, then checking with isa?.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (derive ::hare ::runner) (isa? ::hare ::runner))"}}]}
````

---

## G10-03 — defmacro introduction

_defmacro — rule that rewrites the recipe_  •  **rewriterule** — macros (`_REWRITERULE_SUBPLOTS`)

**form**: `` (do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3)) ``  •  **expected**: `3`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

"Want to see what the rule rewrites the recipe into?"
Shelly the tortoise asked, holding up a slate split in half.
"Macroexpand shows you the before and the after — the original
form on one side, the rewritten form on the other." To
define a macro named my-when that takes a test and body expressions, then invoke it, She composed defining a conditional macro and invoking it,
submitted the form, and the REPL handed back the rewriting itself
or the value, depending on what was asked.

Question: write a Clojure expression for the value returned when my-when expands to an if-do block that runs the body with test true.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

---

## G10-09 — Hygiene and gensym

_gensym — scratch-name for hygiene_  •  **rewriterule** — macros (`_REWRITERULE_SUBPLOTS`)

**form**: `(symbol? (gensym))`  •  **expected**: `True`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

Slowpoke the tortoise sat at a small writing desk in the meadow, quill in
paw. "A macro," he said, "is a rule that rewrites
the recipe before the runtime ever cooks it. You write the rule
once, and any recipe that uses it gets rewritten on the way to
the kitchen." To test that gensym returns a symbol, He composed
testing whether gensym produces a symbol, submitted the form, and the REPL — first
rewriting, then evaluating — returned the value the rewritten
recipe yielded.

Question: write a Clojure expression for whether a generated symbol is of type symbol.

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? (gensym))"}}]}
````

---

## G11-02 — Method call syntax

_method call — borrowing a foreign tool_  •  **toolshed** — host interop (`_TOOLSHED_SUBPLOTS`)

**form**: `(.toUpperCase "abc")`  •  **expected**: `'ABC'`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. This was atop the hilltop.

"Sometimes the toolshed needs to know what kind of tool you mean,"
Slowpoke the tortoise said, marking a small tag onto the form.
"Type-hints save the runtime from having to guess; the host can
go straight to the right method." To call the host method toUpperCase on the string abc,
He composed the host method toUpperCase with the right
hint, submitted the form, and the REPL — taking the host's
fast path — returned the value cleanly.

Question: write a Clojure expression for the uppercase form of the string abc produced by the host method toUpperCase via dot-prefix syntax.

---

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
````

---

## G11-06 — new and dot-construct

_new — constructing a host object_  •  **toolshed** — host interop (`_TOOLSHED_SUBPLOTS`)

**form**: `(String. "go")`  •  **expected**: `'go'`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

"Sometimes the toolshed needs to know what kind of tool you mean,"
Slowpoke the tortoise said, marking a small tag onto the form.
"Type-hints save the runtime from having to guess; the host can
go straight to the right method." To construct a host String object with the dot-construct syntax,
He composed constructing a String via the dot-construct form with the right
hint, submitted the form, and the REPL — taking the host's
fast path — returned the value cleanly.

Write a Clojure expression that computes the newly constructed String object created from a text argument via the dot-construct syntax.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(String. \"go\")"}}]}
````

---

## G2-11 — String concatenation with str

_str concat — threading more beads_  •  **beadstring** — string ops (`_BEADSTRING_SUBPLOTS`)

**form**: `(str "ab" "cd")`  •  **expected**: `'abcd'`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Slowpoke the tortoise held up a string of small wooden beads near the woods.
"Strings in Clojure are like this," he said: "a
threaded line of characters, in order. Concat strings together,
and the threads are spliced; cut a substring out, and you get a
shorter thread." To use str to join the two-letter strings "ab" and "cd", He composed
the string concatenation, submitted the form, and the REPL — splicing or
cutting as the form said — returned the new bead-string.

Question: write a Clojure expression for the result of using str to join "ab" and "cd".

---

{"tool_calls":[{"name":"eval","args":{"form":"(str \"ab\" \"cd\")"}}]}
````

---

## G2-21 — String length and substring

_string length — counting beads_  •  **beadstring** — string ops (`_BEADSTRING_SUBPLOTS`)

**form**: `(count "tortoise")`  •  **expected**: `8`

````text
It was well known among the animals that the Hare boasted of his speed at every chance. It happened on the hilltop.

"To count the beads, walk the thread,"
Mossback the tortoise said. "Want a section of beads? Cut from one
position to another and you get a smaller thread, the original
untouched." To count the characters in the string tortoise, He composed
the count of characters in a string, submitted the form, and the REPL — counting or
cutting — returned the answer the bead-thread had given up.

Question: write a Clojure expression for the result of using count on the string tortoise.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count \"tortoise\")"}}]}
````

---

## G6-10 — Leiningen and deps.edn

_Leiningen / deps.edn (tooling)_  •  **goal** — generic narrative (abstract subject)

**form**: `(:deps {:deps {:a 1 :b 2}})`  •  **expected**: `{':a': 1, ':b': 2}`

````text
It was well known among the animals that the Hare boasted of his speed at every chance.

At a moss-covered milestone by the woods, Hopper the hare sketched a small
wager into the path: whoever could produce a form whose evaluation
would extract the value at the :deps key from a nested map ahead of the other would win the right to set
the next race. Mossback the tortoise, saying very little, said it was
simpler to write accessing a key from a nested map structure carefully than to guess at the
answer.

What Clojure form computes the value at the :deps key in a deps-style map? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:deps {:deps {:a 1 :b 2}})"}}]}
````

---

## G12-08 — clojure.test

_clojure.test (tooling)_  •  **goal** — generic narrative (abstract subject)

**form**: `(= (+ 1 2) 3)`  •  **expected**: `True`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. It happened atop the hilltop.

Mossback the tortoise had been teaching Pip the hare how to translate a
goal into a Clojure form. "If you want to test whether the sum of 1 and 2 equals 3 using equality," he
said, "you write the equality assertion at the heart of test checking; submit that to the REPL, and it
hands you back the value." Pip, weary from the morning's effort, agreed to try
writing it.

Write a Clojure expression that computes the truth value showing the assertion passes.

---

{"tool_calls":[{"name":"eval","args":{"form":"(= (+ 1 2) 3)"}}]}
````

---

