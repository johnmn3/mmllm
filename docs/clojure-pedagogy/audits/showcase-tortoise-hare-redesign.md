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

Subjects are organized by **metaphor family** — five high-leverage
families now carry the Clojure idiom inside the narrative:

- 🟢 **atom** — `_SHARED_SUBPLOTS` (8 templates); the form IS
  the answer; copy-from-prompt is the lesson.
- 🔵 **goal** — `_GOAL_SUBPLOTS` (12 templates); generic
  Hare/Tortoise framing for subjects without a natural fable
  metaphor (host interop, errors, namespaces, polymorphism, etc.).
- 🟣 **pouch** — `_POUCH_SUBPLOTS` (5 templates); a small leather
  pouch tied at the Tortoise's hip. Whatever's tucked inside
  is held for one stretch of road; by the next milestone the
  pouch is empty again. Mirrors `let`-binding scope.
- 🟠 **recipe** — `_RECIPE_SUBPLOTS` (5 templates); a recipe-card
  posted on the road, naming a paw-step routine. Mirrors
  `fn` / `defn` / `comp` / `partial`.
- 🟤 **basket** — `_BASKET_SUBPLOTS` (5 templates); a basket on
  the path; whatever you do, the original basket sits untouched
  and a fresh one is what comes back. Mirrors
  vectors / lists / maps / sets and immutability.
- 🟡 **sieve** — `_SIEVE_SUBPLOTS` (5 templates); a sieve over an
  empty basket; the rule attached at its mouth decides which
  pebbles change, pass, or drop. Mirrors `map` / `filter` /
  `take` / `drop` / `into` / transducers.
- 🟢 **notebook** — `_NOTEBOOK_SUBPLOTS` (5 templates); a notebook
  open on a tree stump; any animal can read or atomically
  update. Mirrors `atom` / `ref` / `swap!` / `dosync` / `compare-and-set!`.

---

## G1-01 — Eval as substitution

_L1 atom — a literal evaluates to itself_  •  🟢 **atom** — form-display intentional

**form**: `42`  •  **expected**: `42`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. All this took place in the meadow.

Shelly the tortoise had been trying to teach Bramble the hare how the REPL
works. "Look here," she said, pointing to
the value 42. "You hand the form `42` to the runtime, and
the runtime hands you back what it evaluates to." Bramble, drowsy from the warm sun,
agreed to try.

Write a form whose evaluation gives the value of 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
````

---

## G1-07 — Keywords

_L1 atom — a keyword evaluates to itself_  •  🟢 **atom** — form-display intentional

**form**: `:hare`  •  **expected**: `':hare'`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. All this took place at the edge of the hilltop.

With a twig, Pip the hare marked out a wager near the hilltop: whoever
guessed the result of `:hare` first would win the right to
choose the next contest. Shelly the tortoise, with eyes always on the path, said it
was easier to ask the REPL about the keyword :hare than to argue.

Write a Clojure expression that computes the value of :hare.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":":hare"}}]}
````

---

## G1-09 — Symbols vs values

_first non-atom: predicate on quoted symbols_  •  🔵 **goal** — generic Hare/Tortoise narrative

**form**: `(symbol? 'hare)`  •  **expected**: `True`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. It happened at the edge of the garden.

Hopper the hare squinted at the goal — to ask whether a quoted name is a symbol, using the symbol? predicate — and blurted
out a confident guess, puffed up with pride, as though loudness were the
same as correctness. Shelly the tortoise did not argue.
She simply wrote the symbol-predicate on a quoted name on the path,
submitted it to the REPL, and held up the value the runtime
returned. The crowd compared the two, and the hare's guess was
found wanting against the form that had actually run.

Write a form whose evaluation gives whether a quoted name is a symbol.

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'hare)"}}]}
````

---

## G1-13 — First arithmetic call

_L2 application — first arithmetic call_  •  🔵 **goal** — generic Hare/Tortoise narrative

**form**: `(+ 1 2)`  •  **expected**: `3`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened near the road.

Halfway through the race, Hopper the hare stopped near the road and refused
to continue until someone could add 1 and 2 with a Clojure form.
Hopper called the goal impossible. Mossback the tortoise, walking up at
his usual pace, simply said: "Compose the addition;
submit it. Whatever comes back is the answer."

What Clojure form computes the sum of 1 and 2? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
````

---

## G2-01 — Multi-arg arithmetic

_multi-arg arithmetic_  •  🔵 **goal** — generic Hare/Tortoise narrative

**form**: `(+ 1 2 3 4)`  •  **expected**: `10`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. This was on the road.

Slowpoke the tortoise kept a small leather notebook of every goal
he had translated into a Clojure form. Today on the road,
the next entry was a goal: add 1, 2, 3, and 4. Slowpoke sat with pen in
hand, ready to compose the multi-arg sum, then let the REPL
confirm the value.

What Clojure form computes the sum of 1, 2, 3, and 4? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2 3 4)"}}]}
````

---

## G2-13 — and / or — short circuit, return values

_and/or short-circuit, return values_  •  🔵 **goal** — generic Hare/Tortoise narrative

**form**: `(and true true)`  •  **expected**: `True`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. It happened by the meadow.

At a moss-covered milestone by the meadow, Pip the hare sketched a small
wager into the path: whoever could produce a form whose evaluation
would test true and true with the and operator ahead of the other would win the right to set
the next race. Slowpoke the tortoise, untroubled by what others thought, said it was
simpler to write the logical and carefully than to guess at the
answer.

What Clojure form computes the result of using and on true and true? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(and true true)"}}]}
````

---

## G3-03 — let — local binding

_let local binding ⭐ pouch_  •  🟣 **pouch** — temporary-binding metaphor (`_POUCH_SUBPLOTS`)

**form**: `(let [x 3] (+ x 1))`  •  **expected**: `4`

````text
It was well known among the animals that the Hare boasted of his speed at every chance.

Pip the hare brushed past the road-sign by the orchard, puffed up with pride,
calling out guesses without bothering to peek into
Slowpoke the tortoise's pouch. But the pouch was where the answer
lived: He intended to bind x to 3 and add 1 to it, and the
value was tucked away for exactly that stretch. Slowpoke wrote
out the local binding and addition, submitted it, and the REPL — looking in
the pouch as the form told it to — handed back the value
Pip had not even thought to check.

Write a Clojure expression that computes adding 1 to x after binding x locally to 3 via let.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
````

---

## G3-04 — let — multi-binding

_let multi-binding_  •  🟣 **pouch** — temporary-binding metaphor (`_POUCH_SUBPLOTS`)

**form**: `(let [a 1 b 2] (+ a b))`  •  **expected**: `3`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

"There's a sign by the road that names one thing," Shelly the tortoise
said, patting the pouch at her hip, "but inside
this pouch I carry another. While I wear the pouch, the pouch
wins." Shelly described how to bind a to 1 and b to 2, then add them — the pouch's
binding overruling the road-sign's, but only for the pouch's
stretch of road. She composed the multi-binding and addition,
submitted it, and let the REPL show whose binding was in force
when the form ran.

What Clojure form computes adding a and b after binding both via let to 1 and 2? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 1 b 2] (+ a b))"}}]}
````

---

## G3-16 — Name collision: namespace vs let

_name collision: let shadows operator_  •  🟣 **pouch** — temporary-binding metaphor (`_POUCH_SUBPLOTS`)

**form**: `(let [+ 99] +)`  •  **expected**: `99`

````text
It was well known among the animals that the Hare boasted of his speed at every chance. This was near the forest.

Mossback the tortoise reached for the small leather pouch tied at
his hip. "When I want to shadow the plus operator with a local binding and return the bound value," he
said, "I tuck the value into the pouch and carry it just for the
stretch of road where I need it. By the next milestone the pouch
is empty again." He composed the shadowed operator binding,
the binding tucked away inside, and submitted the form to the
REPL. Whisker the hare, puffed up with pride, had already forgotten what was
in the pouch — but the form, which still carried it, came back
with the answer.

Write a Clojure expression that computes the value locally bound to the + operator via let.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(let [+ 99] +)"}}]}
````

---

## G3-09 — defn — shorthand

_defn — named recipe_  •  🟠 **recipe** — paw-step-routine metaphor (`_RECIPE_SUBPLOTS`)

**form**: `(do (defn dbl [x] (* x 2)) (dbl 5))`  •  **expected**: `10`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

"In any recipe," Shelly the tortoise explained, "the last step is
what you serve." She took the goal — to
define a function dbl that doubles its argument, then call it with 5 — and wrote the routine's paw-steps in order, knowing
that whatever the final line evaluated to was what the runner
would carry back. Shelly composed the function definition and call, submitted
the form, and the REPL — discarding the earlier steps' values —
handed back only the dish from the last.

Write a Clojure expression that computes the result of calling the function dbl, defined via defn to multiply its argument by 2, with 5.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn dbl [x] (* x 2)) (dbl 5))"}}]}
````

---

## G3-10 — anonymous shorthand #()

_anonymous shorthand #()_  •  🟠 **recipe** — paw-step-routine metaphor (`_RECIPE_SUBPLOTS`)

**form**: `(#(+ % 1) 5)`  •  **expected**: `6`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened in the forest.

"In any recipe," Slowpoke the tortoise explained, "the last step is
what you serve." He took the goal — to
use the shorthand syntax to create a function that adds 1 to its argument and apply it to 5 — and wrote the routine's paw-steps in order, knowing
that whatever the final line evaluated to was what the runner
would carry back. Slowpoke composed the shorthand function syntax, submitted
the form, and the REPL — discarding the earlier steps' values —
handed back only the dish from the last.

What Clojure form computes the result of using the #() shorthand to create a function that adds 1 to its argument and applying it to 5? Submit it via `eval`.

---

I bind the inputs in a let, then compute.

{"tool_calls":[{"name":"eval","args":{"form":"(#(+ % 1) 5)"}}]}
````

---

## G5-15 — comp

_comp — chain of recipes_  •  🟠 **recipe** — paw-step-routine metaphor (`_RECIPE_SUBPLOTS`)

**form**: `((comp inc inc) 5)`  •  **expected**: `7`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. It happened by the woods.

"Here's a recipe with one ingredient already added,"
Slowpoke the tortoise said, holding up a card half-loaded. "When the
next animal calls it, they only have to bring the rest." To
compose two inc functions and apply them to 5, he composed composing inc twice that way
— some arguments fixed in advance, the others to be supplied at
the call site. Slowpoke the tortoise submitted the form, and the REPL
filled in what was missing and ran the recipe through to its
end.

Write a form whose evaluation gives the result of applying the composition of inc and inc to 5.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"((comp inc inc) 5)"}}]}
````

---

## G5-16 — partial

_partial — half-loaded recipe_  •  🟠 **recipe** — paw-step-routine metaphor (`_RECIPE_SUBPLOTS`)

**form**: `((partial + 10) 5)`  •  **expected**: `15`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

Mossback the tortoise kept a small stack of recipe-cards by the road,
each one a paw-step routine for some animal of the meadow to
follow. "Today we add another," he said: "to
apply + with 10 as the first argument and 5 as the second, the steps go like this." He
wrote out partial application of + on a fresh card, gave the recipe its
name, and submitted the form so the REPL could remember it.
Pip the hare, with great whoops of laughter, said they would never bother
with cards — but the next runner along the road would pick the
card up and follow it exactly.

Write a Clojure expression that computes the result of applying a partially applied + function with first argument 10 to 5.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"((partial + 10) 5)"}}]}
````

---

## G4-01 — Vector literal

_vector literal — a row of pebbles_  •  🟤 **basket** — collection metaphor (`_BASKET_SUBPLOTS`)

**form**: `[1 2 3]`  •  **expected**: `[1, 2, 3]`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place on the road.

"You can find what you want in a basket several ways,"
Slowpoke the tortoise said, gesturing at the woven shape:
"by the tag pinned to it, by its place in line, or by simply
asking whether it's there at all." To create a vector containing 1, 2, and 3,
He wrote a vector of three numbers for the basket,
submitted the form, and the REPL applied the lookup or update
exactly as the form directed.

Question: write a Clojure expression for the vector.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"[1 2 3]"}}]}
````

---

## G4-08 — assoc — map update

_assoc — pin a new tag on the basket_  •  🟤 **basket** — collection metaphor (`_BASKET_SUBPLOTS`)

**form**: `(assoc {:a 1} :b 2)`  •  **expected**: `{':a': 1, ':b': 2}`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

"Watch carefully," Shelly the tortoise said, holding up the
original basket. "Whatever I do to it, this one sits unchanged
on the path — what I get back is a fresh basket with the change
made, leaving the first one exactly where it was." To
associate the key :b with value 2 onto a map binding :a to 1, She composed the assoc operation,
submitted the form, and the REPL returned a new arrangement
while the original waited, untouched. Pip the hare, weary from the morning's effort,
was beginning to see why nothing could be lost by trying.

What Clojure form computes the map after using assoc to add the key :b with value 2? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:a 1} :b 2)"}}]}
````

---

## G4-15 — first, rest, last

_first/rest/last — head and tail of the procession_  •  🟤 **basket** — collection metaphor (`_BASKET_SUBPLOTS`)

**form**: `(first [10 20 30])`  •  **expected**: `10`

````text
It was well known among the animals that the Hare boasted of his speed at every chance. All this took place in the woods.

Pip the hare began rummaging in the basket, with great whoops of laughter, calling
out guesses about its contents without quite checking. "I know
exactly what's in there," they insisted. Slowpoke the tortoise
shook his head. To get the first element of a vector containing 10, 20, and 30 properly,
he wrote getting the first element carefully on a slate,
submitted the form, and the REPL — looking into the basket the
way the form told it to — handed back the answer
Pip had been guessing at.

Write a form whose evaluation gives the first element.

---

{"tool_calls":[{"name":"eval","args":{"form":"(first [10 20 30])"}}]}
````

---

## G4-17 — Immutability — assoc returns new

_immutability — original basket untouched_  •  🟤 **basket** — collection metaphor (`_BASKET_SUBPLOTS`)

**form**: `(let [m {:a 1}] (assoc m :a 99) m)`  •  **expected**: `{':a': 1}`

````text
It was well known among the animals that the Hare boasted of his speed at every chance.

"Watch carefully," Mossback the tortoise said, holding up the
original basket. "Whatever I do to it, this one sits unchanged
on the path — what I get back is a fresh basket with the change
made, leaving the first one exactly where it was." To
demonstrate that assoc returns a new map without modifying the original, He composed immutability of maps,
submitted the form, and the REPL returned a new arrangement
while the original waited, untouched. Whisker the hare, yawning at the soft moss,
was beginning to see why nothing could be lost by trying.

Write a form whose evaluation gives the original map after assoc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :a 99) m)"}}]}
````

---

## G5-10 — map

_map — pour through, transform each_  •  🟡 **sieve** — pour-through metaphor (`_SIEVE_SUBPLOTS`)

**form**: `(map inc [1 2 3])`  •  **expected**: `[2, 3, 4]`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

Pip the hare eyed the basket, puffed up with pride, and called out a
guess about what would come out the other side of the sieve
without bothering to actually pour. Slowpoke the tortoise shook
his head and went on with the work: to
apply inc to each element of the vector containing 1, 2, and 3, returning a sequence, he composed mapping increment over a vector as
the sieve's rule, poured the input through carefully,
submitted the form, and the REPL returned the only answer
that would do — the one the sieve had actually produced.

Write a Clojure expression that computes the sequence produced by mapping inc over the vector containing 1, 2, and 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(map inc [1 2 3])"}}]}
````

---

## G5-11 — filter

_filter — keep only what fits the rule_  •  🟡 **sieve** — pour-through metaphor (`_SIEVE_SUBPLOTS`)

**form**: `(filter even? [1 2 3 4])`  •  **expected**: `[2, 4]`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

Slowpoke the tortoise stacked two sieves one above the other, the
output of the first feeding into the second. "What lands at the
bottom," he said, "has been through both rules in
order — applied as a single combined sieve." To keep the even elements from the vector containing 1, 2, 3, and 4,
He composed filtering even elements from a vector as a stack of
sieves, poured the input through, submitted the form, and the
REPL caught what the stack let through.

Write a form whose evaluation gives the sequence produced by filtering even? over the vector containing 1, 2, 3, and 4.

---

{"tool_calls":[{"name":"eval","args":{"form":"(filter even? [1 2 3 4])"}}]}
````

---

## G12-01 — Transducers introduction

_transducers — a reusable, composable sieve_  •  🟡 **sieve** — pour-through metaphor (`_SIEVE_SUBPLOTS`)

**form**: `(into [] (map inc) [1 2 3])`  •  **expected**: `[2, 3, 4]`

````text
It was well known among the animals that the Hare boasted of his speed at every chance.

Mossback the tortoise stacked two sieves one above the other, the
output of the first feeding into the second. "What lands at the
bottom," he said, "has been through both rules in
order — applied as a single combined sieve." To use the map-inc transducer with into to increment the vector containing 1, 2, 3,
He composed the map-inc transducer applied via into as a stack of
sieves, poured the input through, submitted the form, and the
REPL caught what the stack let through.

Write a form whose evaluation gives the vector produced by reifying the map-inc transducer into an empty vector via into, applied to the vector containing 1, 2, 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
````

---

## G9-03 — Atom introduction

_atom — a notebook on a tree stump ⭐ notebook_  •  🟢 **notebook** — shared-state metaphor (`_NOTEBOOK_SUBPLOTS`)

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. It happened near the road.

Shelly the tortoise pinned a small bell to the corner of the
notebook. "Now," she said, "anyone who updates the
page rings the bell, and a listener can keep a record of every
change." To construct an atom holding 0, atomically swap it by applying inc, and dereference the result, She composed
atom, swap, and deref — listener and all — submitted the form, and
the REPL kept a record of each update, the bell ringing each
time the page turned.

What Clojure form computes the value returned by dereferencing a after defining a as an atom holding 0 and swapping it via inc? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
````

---

## G9-04 — Atom CAS semantics

_CAS — only-if-still-says_  •  🟢 **notebook** — shared-state metaphor (`_NOTEBOOK_SUBPLOTS`)

**form**: `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)`  •  **expected**: `1`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. All this took place on the road.

"Sometimes I want to update the notebook only if it still says
what I last saw," Slowpoke the tortoise explained. "If another animal
got there first, I'd rather not overwrite their work." To
construct an atom holding 0, perform a compare-and-set checking for 0 and setting to 1, and dereference, He composed atom, CAS, deref that
way — the update conditional on the old value — submitted the
form, and the REPL applied the change only if the conditions
held.

What Clojure form computes the value returned by dereferencing a after defining a as an atom holding 0 and performing a successful compare-and-set to 1? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (compare-and-set! a 0 1) @a)"}}]}
````

---

## G9-08 — dosync and alter

_dosync/alter — coordinated update of several notebooks_  •  🟢 **notebook** — shared-state metaphor (`_NOTEBOOK_SUBPLOTS`)

**form**: `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])`  •  **expected**: `[2, 3]`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place at the edge of the woods.

Shelly the tortoise pinned a small bell to the corner of the
notebook. "Now," she said, "anyone who updates the
page rings the bell, and a listener can keep a record of every
change." To construct refs a and b, perform a coordinated transaction that alters both by applying inc, and dereference both, She composed
two refs, coordinated alter — listener and all — submitted the form, and
the REPL kept a record of each update, the bell ringing each
time the page turned.

Write a Clojure expression that computes the pair of values returned by dereferencing both a and b after defining them as refs, coordinating their alters inside dosync, and dereferencing.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])"}}]}
````

---

## G6-03 — require

_require — pulling code in_  •  🔵 **goal** — generic Hare/Tortoise narrative

**form**: `(clojure.string/upper-case "hare")`  •  **expected**: `'HARE'`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

A small audience of forest creatures had gathered near the garden to watch
Bramble the hare attempt to outwit Slowpoke the tortoise at writing the
right form. The challenge: call the uppercasing function from clojure.string on a test string. Slowpoke reminded the
crowd that what mattered was writing calling a fully-qualified string function carefully,
then submitting it to the REPL — not guessing aloud at the
answer.

What Clojure form computes the uppercase form of the string hare produced by clojure.string/upper-case? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"hare\")"}}]}
````

---

## G7-02 — try / catch

_try / catch_  •  🔵 **goal** — generic Hare/Tortoise narrative

**form**: `(try (/ 1 0) (catch Exception e -1))`  •  **expected**: `-1`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Whisker the hare and Slowpoke the tortoise stopped by the woods to settle a small
puzzle. Whisker wanted to divide 1 by 0, catch the resulting ArithmeticException, return a numeric code. Whisker, with great whoops of laughter, declared
that he could write the form for it without thinking.
Slowpoke, stepping deliberately, suggested he actually write
the handler for a division-by-zero error carefully — and then let the REPL confirm what
the value really was.

What Clojure form computes what the catch clause returns when ArithmeticException is caught? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 1 0) (catch Exception e -1))"}}]}
````

---

## G8-04 — Protocol definition

_Protocol definition_  •  🔵 **goal** — generic Hare/Tortoise narrative

**form**: `(do (defprotocol Pace (speed [this])) (some? Pace))`  •  **expected**: `True`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. This was near the hilltop.

Slowpoke the tortoise had been teaching Whisker the hare how to translate a
goal into a Clojure form. "If you want to define a protocol named Pace with one method speed that takes a single argument this," he
said, "you write a protocol definition; submit that to the REPL, and it
hands you back the value." Whisker, with legs heavy from sprinting, agreed to try
writing it.

Question: write a Clojure expression for whether the protocol var Pace is truthy after defining a protocol named Pace with one method speed taking a single argument this.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (some? Pace))"}}]}
````

---

## G10-03 — defmacro introduction

_defmacro introduction_  •  🔵 **goal** — generic Hare/Tortoise narrative

**form**: `` (do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3)) ``  •  **expected**: `3`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. This was by the forest.

"You always insist on writing it out," Hopper the hare complained,
as if the race were already won. "I can see the answer from here." Slowpoke the tortoise
shook his head slowly. "To define a macro named my-when that takes a test and body expressions, then invoke it, the eye is
no help — only the form is. Watch." He wrote
defining a conditional macro and invoking it in careful strokes, submitted it to the REPL,
and let the returned value speak for itself. Hopper, yawning at the soft moss,
admitted that this time, again, the patient way had carried the
day.

Write a Clojure expression that computes the value returned when my-when expands to an if-do block that runs the body with test true.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

---

## G11-02 — Method call syntax

_Method call syntax_  •  🔵 **goal** — generic Hare/Tortoise narrative

**form**: `(.toUpperCase "abc")`  •  **expected**: `'ABC'`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. All this took place near the garden.

Pip the hare and Mossback the tortoise stopped by the garden to settle a small
puzzle. Pip wanted to call the host method toUpperCase on the string abc. Pip, as if the race were already won, declared
that they could write the form for it without thinking.
Mossback, with steady, careful steps, suggested they actually write
the host method toUpperCase carefully — and then let the REPL confirm what
the value really was.

What Clojure form computes the uppercase form of the string abc produced by the host method toUpperCase via dot-prefix syntax? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
````

---

