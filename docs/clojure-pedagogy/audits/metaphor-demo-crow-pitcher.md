# Metaphor demo — crow-pitcher curriculum

One canonical subject per metaphor family. For each, two
renders are shown:

- **Story-scaffold render** — the example's authored
  `scenario` / `need` / `mapping` / `resolution` slots
  composed into a 5-act grounded story by the
  `_story()` template (Phase C framework). The metaphor
  *drives* the action — concrete situation, specific need,
  explicit mapping, resolution that closes the loop.
- **Family-template render** — one of the family pool's
  generic templates, for contrast. Same example, no story
  slots used.

Coverage: 22 metaphor families + atoms + the goal-fallback
for abstract subjects. Across 216 subjects there are
509 examples; 423 carry story-scaffold slots.

---

## atom — G1-01: Eval as substitution

_pool_: `_SHARED_SUBPLOTS`

**The metaphor:** For atoms (literals), the form IS the answer. The user_msg deliberately shows the form (`{form_display}`); copy-from-prompt is the lesson — submit the literal as-is.

### Atom render

**form**: `42`  •  **expected**: `42`

````text
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. All this took place in the village.

Korvus the crow chalked a wager on a flat stone in the village: whoever
predicted the result of `42` would set the next race's
distance. Caw the crow, unbothered by the slow progress, said it would be simpler
to type the form into the REPL than to bicker about the value 42.

Write a Clojure expression that computes the value of 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
````

---

## pouch — G3-03: let — local binding

_pool_: `_POUCH_SUBPLOTS`

**The metaphor:** The clever crow tucks an intermediate value under one wing — held only for the stretch where the form needs it. After the drop, the wing opens again: the value existed only inside the form's reach. Mirrors `let`-binding scope.

### Story-scaffold render

**form**: `(let [x 3] (+ x 1))`  •  **expected**: `4`

````text
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened at the edge of the market.

Korvus arrived at the tall clay pitcher in the orchard, three smooth stones from the morning's count in mind. Before dropping any, he tucked the count of three under his left wing, close and named: x, holding three.

He needed to know how far the water would rise if he added one more stone to whatever was tucked under his wing.

`let` gives a name to a tucked value: x binds 3 for the span of the form. Inside that stretch, `(+ x 1)` reaches under the wing and adds one. When the form ends the wing opens; the binding dissolves.

To bind a value of 3 to a local name x for one stretch, then return that value plus one, They composed the local binding and addition with the binding tucked safely under a wing and submitted the form. The REPL reached under the wing as the form directed:

4 — the tucked count of three, plus the one stone added while the wing held it firm.

Question: write a Clojure expression for the running total after binding x to 3 and adding 1.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
````

### Family-template render _(seed 1021)_

**form**: `(let [x 3] (+ x 1))`  •  **expected**: `4`

````text
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

"Wherever the form names the binding," Sable the crow explained,
"the REPL reaches under the wing and pulls out what was tucked
there." They demonstrated by intending to
bind a value of 3 to a local name x for one stretch, then return that value plus one: each mention of the bound name, Sable said,
would be replaced by the value from under the wing the moment the
form ran. Sable the crow composed the local binding and addition, submitted
the form, and the REPL substituted as promised — the wing-cache's
value threaded into every place the binding had been named.

Write a Clojure expression that computes the running total after binding x to 3 and adding 1.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
````

---

## recipe — G3-07: fn — anonymous function

_pool_: `_RECIPE_SUBPLOTS`

**The metaphor:** The clever crow scratches a step-by-step drop-order into the pitcher's clay rim — a pattern any crow can follow. Same recipe, different stones each time. Mirrors `fn` / `defn`.

### Story-scaffold render

**form**: `((fn [x] (+ x 1)) 4)`  •  **expected**: `5`

````text
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Caw perched at the pitcher's rim in the garden and scratched a small drop-order into the clay with her talon: accept a count named x, then add one stone to it. No name carved — just the pattern, ready at the rim.

She wanted to apply the recipe at once, feeding it the count of four, and see how high the water rose.

`fn` scratches an anonymous recipe: it declares the argument x and specifies the body `(+ x 1)`. Wrapping the recipe with 4 applies it immediately — the argument fills x, the body runs.

To create an anonymous function that adds 1 to its argument and apply it to 4, She scratched out the anonymous function call on the rim and submitted the form. The REPL followed the drop-order end to end:

5 — the recipe added one stone to the count of four, the water clearing the fifth notch.

Question: write a Clojure expression for the result of applying an anonymous fn that adds 1 to its argument to the value 4.

---

I bind the inputs in a let, then compute.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] (+ x 1)) 4)"}}]}
````

### Family-template render _(seed 1050)_

**form**: `((fn [x] (+ x 1)) 4)`  •  **expected**: `5`

````text
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Caw the crow held up a smooth stone and scratched a step-by-step
sequence into the pitcher's clay rim. "Drop-orders in Clojure are
like this," she said: "the smooth stones go at the head,
the drops in order, and the last drop is what raises the water to
beak-reach." To create an anonymous function that adds 1 to its argument and apply it to 4, She scratched out
the anonymous function call on the rim, submitted the form, and the REPL
followed the drop-order and handed back the value the last drop
had raised.

Question: write a Clojure expression for the result of applying an anonymous fn that adds 1 to its argument to the value 4.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] (+ x 1)) 4)"}}]}
````

---

## basket — G2-17: Keyword as function for map lookup

_pool_: `_BASKET_SUBPLOTS`

**The metaphor:** The crow's gathered stone-pile sits beside the pitcher, each stone in place. Dropping a new stone doesn't move the ones already piled — the pile is the original arrangement. Mirrors persistent collections.

### Story-scaffold render

**form**: `(:hare {:hare 1 :tortoise 2})`  •  **expected**: `1`

````text
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was near the village.

Sable arranged two pebbles on the pitcher's rim near the hilltop: one marked :hare carrying the count 1, another marked :tortoise carrying 2. The pile sat in order, side by side.

She wanted only the count beneath the :hare stone without lifting or moving the :tortoise stone at all.

A map is a labelled stone-pile. Using :hare as a function reaches into the pile and pulls only the value under that label, leaving every other stone exactly in place.

To use the keyword :hare to look up a value in the map with keys :hare and :tortoise, She composed the keyword lookup for the stone-pile and submitted the form. The REPL handed back the arrangement:

1 — the :hare stone's count, lifted cleanly from the pile without disturbing its neighbour.

Question: write a Clojure expression for the result of using the keyword :hare as a function on the map {:hare 1 :tortoise 2}.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:hare {:hare 1 :tortoise 2})"}}]}
````

### Family-template render _(seed 1119)_

**form**: `(:hare {:hare 1 :tortoise 2})`  •  **expected**: `1`

````text
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. All this took place near the road.

"You can find what you want in a stone-pile several ways,"
Korvus the crow said, gesturing at the gathered stones:
"by the mark scratched on it, by its place in line, or by simply
asking whether it's there at all." To use the keyword :hare to look up a value in the map with keys :hare and :tortoise,
He wrote the keyword lookup for the stone-pile,
submitted the form, and the REPL applied the lookup or update
exactly as the form directed.

What Clojure form computes the result of using the keyword :hare as a function on the map {:hare 1 :tortoise 2}? Submit it via `eval`.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(:hare {:hare 1 :tortoise 2})"}}]}
````

---

## sieve — G4-16: into and conj on collections

_pool_: `_SIEVE_SUBPLOTS`

**The metaphor:** The crow holds each stone over the pitcher's mouth and decides: smooth round ones go in, jagged or flat ones are set aside. The rule filters the whole pile. Mirrors `filter` / `map` / transducers.

### Story-scaffold render

**form**: `(into [] '(1 2 3))`  •  **expected**: `[1, 2, 3]`

````text
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was near the village.

Caw had a three-stone chain queued at the market pitcher and an empty vector-pile waiting beside it. She needed to pour the chain's stones into the ordered pile.

She needed `into` to transfer each stone from the chain into the vector-pile, preserving order.

`into` pours one collection's stones into another. The chain is the source; the empty vector is the destination. Each stone lands in order, building the vector-pile from the chain.

To convert a list containing 1, 2, and 3 into a vector, She composed building a vector from a list as the sorting rule, held the stones over, and submitted the form. The REPL caught what landed below:

The REPL returned the filled vector-pile with all stones from the chain transferred in order.

Question: write a Clojure expression for the vector built from a list.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] '(1 2 3))"}}]}
````

### Family-template render _(seed 1112)_

**form**: `(into [] '(1 2 3))`  •  **expected**: `[1, 2, 3]`

````text
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Caw the crow perched at the pitcher's edge, holding a decision-rule
over the stones near the road. "Whatever rule I hold here,"
she said, "each stone passes under my eye one
at a time: some are changed, some kept, some set aside, depending
on the rule." To convert a list containing 1, 2, and 3 into a vector, She composed
building a vector from a list as the rule, sorted the pile through,
submitted the form, and the REPL returned what the rule had
let drop.

Write a Clojure expression that computes the vector built from a list.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] '(1 2 3))"}}]}
````

---

## notebook — G9-02: Why state at all

_pool_: `_NOTEBOOK_SUBPLOTS`

**The metaphor:** The crow scratches a tally mark into the pitcher's clay face each time the water level rises — the mark persists, updated stone by stone, visible to any crow who perches there later. Mirrors `atom` / `ref` / mutable state.

### Story-scaffold render

**form**: `(do (def counter (atom 0)) (swap! counter inc) @counter)`  •  **expected**: `1`

````text
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened at the edge of the market.

Korvus needed a mark that would survive across visits to the hilltop pitcher. He scratched a zero on the clay face as a counter, then nudged it up by one with a single talon stroke.

He needed to read the counter's current mark after the update to know how many visits were recorded.

`atom` creates the persistent tally on the clay face. `swap!` applies inc to the current value and writes the new mark. `@counter` reads the mark back from the clay.

To construct an atom holding 0 as counter, atomically swap it by applying inc, and dereference the result, They composed binding an atom to counter, atomically incrementing it, and dereferencing the result for the water-tally and submitted the form. The REPL scratched the mark on the pitcher:

The clay face showed the updated tally — one visit recorded, the counter holding its new mark.

Question: write a Clojure expression for the value after atomically swapping counter with inc and dereferencing.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def counter (atom 0)) (swap! counter inc) @counter)"}}]}
````

### Family-template render _(seed 1014)_

**form**: `(do (def counter (atom 0)) (swap! counter inc) @counter)`  •  **expected**: `1`

````text
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place at the edge of the hilltop.

"The tally stays put on the pitcher," Sable the crow said,
"so any crow who comes by can read what's marked right
now. The marks change only when someone scratches — and only as the
runtime allows." To construct an atom holding 0 as counter, atomically swap it by applying inc, and dereference the result, They composed
binding an atom to counter, atomically incrementing it, and dereferencing the result, submitted the form, and the REPL — reading
or scratching the tally as the form prescribed — handed back the
value the mark had carried.

Write a form whose evaluation gives the value after atomically swapping counter with inc and dereferencing.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def counter (atom 0)) (swap! counter inc) @counter)"}}]}
````

---

## acorn — G1-13: First arithmetic call

_pool_: `_ACORN_SUBPLOTS`

**The metaphor:** The clever crow counts smooth stones from the meadow floor, adding, dividing, or subtracting to calculate exactly how many more drops will raise the water. Mirrors arithmetic.

### Story-scaffold render

**form**: `(+ 1 2)`  •  **expected**: `3`

````text
It is said that wit, more than strength, is the friend of the thirsty Crow.

Korvus crouched at the tall clay pitcher's rim at the farm's yard, two handfuls of smooth stones — one stone in his left talon, two in his right.

He wanted to count the total stones in both talons to know how far the water would rise when both handfuls dropped together.

`+` is the stone-count call: it totals the numbers it receives, left to right. One stone plus two stones gives a total the runtime calculates and returns as the water-level.

To add 1 and 2, He composed the addition and submitted the form. The REPL counted out the answer:

The two handfuls combined, the water rising to the expected notch at beak-reach.

Question: write a Clojure expression for the sum of 1 and 2.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
````

### Family-template render _(seed 1091)_

**form**: `(+ 1 2)`  •  **expected**: `3`

````text
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened near the road.

"Whatever the heap looks like after the operation,"
Caw the crow said, "the runtime gives the exact count —
small or large, fraction or whole, the answer is precise." To
add 1 and 2, She composed the addition,
submitted the form, and the REPL handed back the value, exactly
as the operation had produced it.

Write a Clojure expression that computes the sum of 1 and 2.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
````

---

## gate — G1-15: Equality

_pool_: `_GATE_SUBPLOTS`

**The metaphor:** The crow can only drink if two gates clear in sequence — the pitcher must be deep enough AND the water must have risen past the threshold. One gate closed, no drink. Mirrors `and` / `or` / equality.

### Story-scaffold render

**form**: `(= 1 1)`  •  **expected**: `True`

````text
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was near the village.

Caw held two unmarked stones up at the pitcher's mouth in the village, one in each talon, both carrying the count 1. She set them side by side at the dual-gate check.

Only if both gate-arms confirmed the same count would the form return true and the beak dip to drink.

`=` checks whether all its arguments are equal. Both gate-arms read 1; both close together. With both gates cleared the runtime returns the confirmation: true.

To test whether 1 equals 1 with =, She composed the equality check and held it at the dual-gate check. The REPL opened or closed the gates as the logic demanded:

true — both gates closed in agreement, the counts identical, the confirmation dropping into the pitcher.

Question: write a Clojure expression for whether 1 equals 1.

---

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 1)"}}]}
````

### Family-template render _(seed 1105)_

**form**: `(= 1 1)`  •  **expected**: `True`

````text
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. All this took place near the road.

Caw the crow swooped toward the pitcher near the road, clicking the beak in self-satisfaction, certain
the gate would swing open. Korvus the crow watched: the only way to know
which way the gate swings is to bring the value to it. To test whether 1 equals 1 with =,
he composed the equality check, submitted the form, and the
REPL settled the matter — the gate had swung exactly as the rules said,
regardless of Caw's guess.

Write a Clojure expression that computes whether 1 equals 1.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 1)"}}]}
````

---

## fork — G5-01: if

_pool_: `_FORK_SUBPLOTS`

**The metaphor:** Perched above the pitcher's mouth, the crow decides: if the water already clears the mark, lower the beak; else drop another stone. The branch in the form is the branch on the perch. Mirrors `if` / `cond`.

### Story-scaffold render

**form**: `(if true :a :b)`  •  **expected**: `:a`

````text
Hunger and thirst had driven the Crow far from her usual perch.

Sable perched above the pitcher's mouth at the orchard's edge, the fork-path clear below: one branch drops a stone marked :a, the other drops one marked :b. She tested the condition first.

The condition was `true` — already settled. She needed to know which branch would release its stone into the pitcher.

`if` reads the condition first: if truthy, the then-branch releases; if falsy, the else-branch releases. `true` is unmistakably truthy — the :a branch releases, :b stays back.

To choose between :a and :b based on a true condition, She composed the conditional and submitted the form. The REPL took the right path:

:a — the then-branch released its stone, the :b stone resting where it was, the water rising one mark.

Question: write a Clojure expression for which of :a or :b is returned.

---

{"tool_calls":[{"name":"eval","args":{"form":"(if true :a :b)"}}]}
````

### Family-template render _(seed 1007)_

**form**: `(if true :a :b)`  •  **expected**: `:a`

````text
Hunger and thirst had driven the Crow far from her usual perch. All this took place on the road.

Korvus the crow perched above the pitcher's mouth near the road, head tilted
one way, then the other. "Branching forms in Clojure are like this
choice above the pitcher," he said. "The runtime checks
the condition, takes the matching path, and only that path's value comes
back." To choose between :a and :b based on a true condition, He composed the conditional,
submitted the form, and the REPL — having taken the right path —
handed back its value.

Write a form whose evaluation gives which of :a or :b is returned.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(if true :a :b)"}}]}
````

---

## roadsign — G3-01: def — top-level binding

_pool_: `_ROADSIGN_SUBPLOTS`

**The metaphor:** The crow carves a name into the pitcher's clay rim — a marker any crow who perches there can read to know which calculation is stored at this spot. Mirrors `def` / namespace bindings.

### Story-scaffold render

**form**: `(do (def x 42) x)`  •  **expected**: `42`

````text
Hunger and thirst had driven the Crow far from her usual perch.

Korvus pressed his talon to the pitcher's clay rim in the garden and carved the name x deep into the clay, then filled that groove with a count: 42, now permanently named.

Once the carving was set, he wanted to read the count back from the rim — to confirm x would answer when called.

`def` carves a name into the namespace rim and fills it with a value. The name persists as long as the rim stands. Evaluating x reads from the groove and returns what was carved.

To bind x to 42 and return it, She composed the top-level binding and lookup and submitted the form. The REPL read the rim-carvings and replied:

42 — the rim answered, the count intact in the groove where the talon had pressed it.

Question: write a Clojure expression for the value of x after using def to bind x to 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 42) x)"}}]}
````

### Family-template render _(seed 1007)_

**form**: `(do (def x 42) x)`  •  **expected**: `42`

````text
Hunger and thirst had driven the Crow far from her usual perch. All this took place on the road.

Korvus the crow pressed a talon-tip into the pitcher's clay rim near the road,
carving a name with care. "A def is a carving in the rim," he
said. "Anyone who perches here reads the name, learns the value, and can
call it by name alone from here on." To bind x to 42 and return it,
He composed the top-level binding and lookup, submitted the form, and
the REPL — carving the name — bound it to its value for any later
retrieval.

Write a form whose evaluation gives the value of x after using def to bind x to 42.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 42) x)"}}]}
````

---

## safetynet — G1-18: Errors are safe in the REPL

_pool_: `_SAFETYNET_SUBPLOTS`

**The metaphor:** The crow tests each stone over a soft patch of moss before committing — if the form fails, the moss catches the stone safely and the crow can try a different one without losing the water level. Mirrors `try` / `catch`.

### Story-scaffold render

**form**: `(+ 1 2)`  •  **expected**: `3`

````text
Hunger and thirst had driven the Crow far from her usual perch.

Sable spread a patch of soft moss on the ground beneath the garden pitcher before dropping any stone — a safety pad in place, ready to catch any mis-drop without harm.

Sable needed to confirm that a well-formed stone-drop would return the correct count even with the moss in place below.

The moss patch changes nothing when the drop succeeds: it only matters if something goes wrong. A correct addition returns its value as usual, the moss untouched and the pitcher undisturbed.

To add 1 and 2, He composed the addition and submitted the form. The REPL — moss in place — handled any slip and returned:

The expected sum returned cleanly, the moss never needed, the REPL untroubled by the safety pad beneath.

What Clojure form computes the result of adding 1 and 2? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
````

### Family-template render _(seed 1126)_

**form**: `(+ 1 2)`  •  **expected**: `3`

````text
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened at the edge of the hilltop.

Korvus the crow eyed the pitcher at the edge of the hilltop, head tilted confidently to one side, certain he
could drop the stone without the moss patch. Caw the crow spread the
moss carefully: a failed form without a catch leaves the pitcher in an
unknown state. To add 1 and 2, she composed the addition,
submitted the form, and the REPL — moss in place — caught anything that
fell and returned the answer the safety design had earned.

Write a form whose evaluation gives the result of adding 1 and 2.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
````

---

## scroll — G6-15: Namespace meta

_pool_: `_SCROLL_SUBPLOTS`

**The metaphor:** The crow scratches an inscription into a smooth flat stone with the tip of her talon — written once in the moment, readable whenever another crow alights on the same stone later. Mirrors lazy seqs / IO.

### Story-scaffold render

**form**: `(:doc (meta '\{:doc "steady wins"\} race))`  •  **expected**: `steady wins`

````text
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was near the village.

Sable pressed a talon-inscription into the margin beside the namespace symbol at the pitcher's flat stone in the meadow: a :doc note recording the shelf's purpose. They later read that margin to find the note.

They needed to recover the docstring scratched into the margin — a crow perching later would read it to understand the shelf's intent without examining every groove.

`meta` reads the marginal notes on a symbol as a map. `:doc` retrieves the documentation string from that map. The talon-inscription in the margin is the value; `meta` is the flat stone one reads it from.

To extract the :doc metadata value from a symbol with a docstring, She composed accessing the :doc metadata from a symbol and submitted the form. The REPL — talon pressed to stone — completed the inscription:

The pitcher returned the docstring from the margin — the talon-inscribed note retrieved intact.

Question: write a Clojure expression for the docstring value from a symbol's metadata.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '\\{:doc \"steady wins\"\\} race))"}}]}
````

### Family-template render _(seed 1105)_

**form**: `(:doc (meta '\{:doc "steady wins"\} race))`  •  **expected**: `steady wins`

````text
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. All this took place near the road.

Caw the crow, clicking the beak in self-satisfaction, claimed the flat stone said exactly what
she expected and didn't bother to actually read it. Korvus the crow
pressed the talon carefully and read each scratch. To extract the :doc metadata value from a symbol with a docstring required the
stone's actual content — he composed accessing the :doc metadata from a symbol, submitted
the form, and the REPL — reading the stone faithfully — returned the value the
inscription had held.

Write a Clojure expression that computes the docstring value from a symbol's metadata.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '\\{:doc \"steady wins\"\\} race))"}}]}
````

---

## guild — G8-01: Why polymorphism

_pool_: `_GUILD_SUBPLOTS`

**The metaphor:** Any crow at the pitcher — Korvus, Caw, Sable — answers the same stone-drop call. Each raises the water the same amount per stone, each in their own rhythm. Mirrors protocols / polymorphism.

### Story-scaffold render

**form**: `(defn speak [k] (cond (= k :hare) "swift" (= k :tortoise) "steady" :else "silent"))`  •  **expected**: `None`

````text
Hunger and thirst had driven the Crow far from her usual perch.

Sable talon-scratched a routing rule on the pitcher's rim at the hilltop: a stone marked :hare gets one word, :tortoise gets another, everything else gets 'silent'. The rule was scratched — not yet called.

She needed to record the routing rule so any stone could be handed to it later without re-scratching.

`defn` scratches the rule permanently onto the rim. The `cond` branches encode each stone's tag and its matching word. No stone is dropped yet — the rule is simply registered.

To define a function speak that returns different strings depending on whether its argument is :hare or :tortoise, She composed conditional dispatch on a tag and submitted the form. The REPL — checking the guild ledger — dispatched cleanly:

The pitcher acknowledged the rule was scratched and the var was registered.

Question: write a Clojure expression for the function definition.

---

{"tool_calls":[{"name":"eval","args":{"form":"(defn speak [k] (cond (= k :hare) \"swift\" (= k :tortoise) \"steady\" :else \"silent\"))"}}]}
````

### Family-template render _(seed 1007)_

**form**: `(defn speak [k] (cond (= k :hare) "swift" (= k :tortoise) "steady" :else "silent"))`  •  **expected**: `None`

````text
Hunger and thirst had driven the Crow far from her usual perch. All this took place on the road.

Korvus the crow scratched a small sign into the pitcher's rim near the road:
"Stone-Drop Guild — any crow may join." "A protocol is a guild,"
he said. "It lists what every member must be able to do —
the methods. Any crow who can fulfil the stone-drop call may claim
membership." To define a function speak that returns different strings depending on whether its argument is :hare or :tortoise, He composed
conditional dispatch on a tag, submitted the form, and the REPL — guild scratched —
handed back the guild's record.

Write a form whose evaluation gives the function definition.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(defn speak [k] (cond (= k :hare) \"swift\" (= k :tortoise) \"steady\" :else \"silent\"))"}}]}
````

---

## sortingtable — G8-08: Multimethod defmulti

_pool_: `_SORTINGTABLE_SUBPLOTS`

**The metaphor:** The pitcher's mouth has a sorting lip: stones marked with one groove go straight in; stones with two grooves are deflected. The mark on the stone decides the path. Mirrors multimethods / dispatch.

### Story-scaffold render

**form**: `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))`  •  **expected**: `:swift`

````text
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Korvus set the sorting-lip on the pitcher's mouth at the farm's edge: stones bearing a :species mark would be routed by the matching chute. He registered a chute for the :hare stamp.

He wanted to drop a stone stamped {:species :hare} and watch the lip route it automatically.

`defmulti` installs the reading-rule — here it reads :species. `defmethod` registers what happens per reading. The dispatch is automatic at call time.

To declare a sorting-table named pace that reads each runner's :species stamp; add an arm for the :hare stamp returning the swift-pace keyword; then route a runner stamped :hare through the table, They composed the multimethod and its first arm and set it at the shape-sorting rim. The REPL read the mark and routed as directed:

the lip read :hare, opened the matching chute, and the registered value dropped into the pitcher.

What Clojure form computes the pace returned for a runner stamped :hare after the table routes to its arm? Submit it via `eval`.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))"}}]}
````

### Family-template render _(seed 1056)_

**form**: `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))`  •  **expected**: `:swift`

````text
Hunger and thirst had driven the Crow far from her usual perch. All this took place in the market.

"What the rim sorts by is up to you," Korvus the crow said. "You decide
what to look at on each stone — a scratch, a shape, a color, anything.
The runtime reads it, finds the matching chute, and runs that one." To
declare a sorting-table named pace that reads each runner's :species stamp; add an arm for the :hare stamp returning the swift-pace keyword; then route a runner stamped :hare through the table, He composed the multimethod and its first arm, submitted the
form, and the REPL — reading the mark the dispatch function produced —
returned the value the right chute had given.

Write a Clojure expression that computes the pace returned for a runner stamped :hare after the table routes to its arm.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))"}}]}
````

---

## carryingcase — G8-02: deftype introduction

_pool_: `_CARRYINGCASE_SUBPLOTS`

**The metaphor:** The clever crow weaves a carrying-pouch from bark strips and vine — a bespoke case with named slots for each kind of stone. The case's shape defines what fits inside. Mirrors `defrecord` / `deftype`.

### Story-scaffold render

**form**: `(do (deftype Pebble [color]) (.-color (Pebble. "grey")))`  •  **expected**: `grey`

````text
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened at the edge of the market.

Caw wove a bark-and-vine pouch at the orchard with a single slot called color. She packed one pebble in, marking the color slot with a talon-scratch, then held the pouch to the light.

She needed to reach into the color slot and lift the marked value back out without unpacking everything.

`deftype` weaves the pouch's shape — one named slot. Constructing `Pebble.` packs the value in. The `.-color` accessor reaches directly into the slot and lifts the value.

To define a type Pebble with a color field and then read the color field from an instance, They stitched reading the color field of a Pebble instance into the stone-pouch and submitted the form. The REPL pulled from the slots as the form prescribed:

The color slot answered with the value packed inside.

Question: write a Clojure expression for the color field value after defining a type Pebble with one field color, then constructing an instance and reading the field.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (deftype Pebble [color]) (.-color (Pebble. \"grey\")))"}}]}
````

### Family-template render _(seed 1014)_

**form**: `(do (deftype Pebble [color]) (.-color (Pebble. "grey")))`  •  **expected**: `grey`

````text
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place at the edge of the hilltop.

"A deftype is a barer pouch," Sable the crow said. "Slots, a knot — no
map-like behavior unless you ask for it. Lighter, more focused." To
define a type Pebble with a color field and then read the color field from an instance, They composed reading the color field of a Pebble instance, submitted the
form, and the REPL — stitching the bare pouch as specified — returned the
value inside.

Write a form whose evaluation gives the color field value after defining a type Pebble with one field color, then constructing an instance and reading the field.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (deftype Pebble [color]) (.-color (Pebble. \"grey\")))"}}]}
````

---

## toolshed — G6-14: Import for host classes

_pool_: `_TOOLSHED_SUBPLOTS`

**The metaphor:** The crow borrows an earthenware pitcher made by a human potter — a different maker's vessel, but the stone-drop sequence works the same. Mirrors Java interop.

### Story-scaffold render

**form**: `(symbol? 'java.util.List)`  •  **expected**: `True`

````text
It is said that wit, more than strength, is the friend of the thirsty Crow. This was at the edge of the market.

Korvus discovered a borrowed earthenware vessel at the pitcher's base in the market: a human-fired container with a dotted three-part label, the potter's full class name pressed into the clay. He needed to confirm its kind.

He needed to know whether the dotted human-potter label was a symbol — the import machinery would only register it if it arrived as a proper symbol, not raw text.

`symbol?` tests the kind-mark of any value. A quoted dotted label — even one naming a human potter's class — is a symbol; the test reads the kind-mark and returns the answer.

To test whether a Java class name written as a quoted symbol is a symbol, She composed testing whether a value is a symbol and submitted the form. The REPL — calling into the earthenware vessel the human had fired — returned:

The pitcher confirmed the human-potter label was a symbol — the kind-mark matched, the import path valid.

What Clojure form computes whether a dotted Java class name is a symbol? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'java.util.List)"}}]}
````

### Family-template render _(seed 1098)_

**form**: `(symbol? 'java.util.List)`  •  **expected**: `True`

````text
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened on the road.

"Each vessel from the human potters has its own label," Korvus the crow
said, "and the right way to call it depends on which kind of vessel it is
— some held by a crow, some standard-issue from the potter's hand." To
test whether a Java class name written as a quoted symbol is a symbol, He composed testing whether a value is a symbol using the
right calling convention, submitted the form, and the REPL — invoking
the host vessel's method by its label — returned the value the human had
crafted.

Write a form whose evaluation gives whether a dotted Java class name is a symbol.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'java.util.List)"}}]}
````

---

## runnerahead — G9-10: Agent introduction

_pool_: `_RUNNERAHEAD_SUBPLOTS`

**The metaphor:** The clever crow sends a second crow ahead to count the stones at the far orchard — come back with the tally when done; meanwhile, keep dropping here. Mirrors agents / futures / promises.

### Story-scaffold render

**form**: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`  •  **expected**: `1`

````text
Hunger and thirst had driven the Crow far from her usual perch.

Sable set a scout-crow carrying a tally of zero on the road to the far orchard. She sent the scout ahead with one instruction: increment the tally by one. Then she waited at the pitcher for the scout's return.

Once the scout had done its work she wanted to read the tally the scout carried back and see how the water stood.

`agent` creates the scout carrying a value. `send` dispatches the function asynchronously. `await` blocks until the scout returns. `@` dereferences the final tally from the agent.

To construct an agent holding 0, asynchronously send inc to it, await its completion, and dereference, She composed agent, send, await, deref and submitted the form. The REPL sent the scout ahead and coordinated the return:

1 — the scout returned with the incremented count, the tally settling into the pitcher's depth.

Write a Clojure expression that computes the value returned by dereferencing ag after defining an agent holding 0, sending inc asynchronously, awaiting, and dereferencing.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
````

### Family-template render _(seed 1071)_

**form**: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`  •  **expected**: `1`

````text
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Sable the crow, with a triumphant rattle of feathers, reached for the scout's count before the
scout had even returned. Korvus the crow held them back: a
scout sent ahead must be allowed to finish. To construct an agent holding 0, asynchronously send inc to it, await its completion, and dereference,
he composed agent, send, await, deref, submitted the form, and the
REPL — waiting for the scout the patient way — returned the value when
the scout had actually delivered it.

What Clojure form computes the value returned by dereferencing ag after defining an agent holding 0, sending inc asynchronously, awaiting, and dereferencing? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
````

---

## rewriterule — G10-03: defmacro introduction

_pool_: `_REWRITERULE_SUBPLOTS`

**The metaphor:** The crow's talon rewrites the drop-order scratched on the rim before a single stone falls — a master revision that changes what the form will do before the REPL sees it. Mirrors `defmacro`.

### Story-scaffold render

**form**: `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`  •  **expected**: `3`

````text
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened at the edge of the market.

Caw scratched a master revision rule on the pitcher's rim at the village: `my-when` — whenever this pattern appeared in a form, the talon would rewrite it before the REPL ever saw the body. The rule expanded it to an `if`.

She wanted to call `(my-when true 1 2 3)` and see the rewritten form evaluated — the `if` expansion running and returning the last body expression.

`defmacro` installs the rewrite-rule. When the REPL encounters `my-when`, it runs the macro first and produces the expansion. The expansion is what evaluates — the macro's return is code, not a value.

To define a rule named my-when that rewrites (my-when t body...) into (if t (do body...)); then invoke it with the test true and a three-expression body, They composed defining a conditional macro and invoking it and scratched it on the rim for rewriting. The REPL — applying the rewrite-rule, then evaluating the rewritten form — returned:

3 — the rewrite ran, the `if` expanded, the last body form evaluated and dropped into the pitcher.

Question: write a Clojure expression for the value the rewritten if-do form returns when the test is true and the body has three expressions.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

### Family-template render _(seed 1021)_

**form**: `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`  •  **expected**: `3`

````text
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Korvus the crow, ruffling up with certainty, insisted that no rule was needed —
he could write the form directly. Sable the crow allowed
that sometimes that's true, but the rule shines when many forms need the
same rewriting. To define a rule named my-when that rewrites (my-when t body...) into (if t (do body...)); then invoke it with the test true and a three-expression body, they composed defining a conditional macro and invoking it,
submitted the form, and the REPL — handling the rule's rewrite the rule's
way — returned the value the form had produced.

Write a Clojure expression that computes the value the rewritten if-do form returns when the test is true and the body has three expressions.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

---

## scribe — G1-10: Comments

_pool_: `_SCRIBE_SUBPLOTS`

**The metaphor:** The talon-scratched notes on the clay: spacing between tally marks, parenthetical asides in the margin, shorthand that tells the REPL how to read the form before it evaluates. Mirrors reader conventions / comments.

### Story-scaffold render

**form**: `(+ 1 2) ; sum of one and two`  •  **expected**: `3`

````text
Hunger and thirst had driven the Crow far from her usual perch.

Korvus scratched a stone-drop form onto the pitcher's rim in the garden: `(+ 1 2)`. Beside it he pressed the finest tip of his talon to the clay and added a marginal note: `; sum of one and two` — a reader-note, not part of the drop.

He wanted the form to evaluate as usual, the marginal note silent, the REPL reading only the form to the semicolon's left.

The semicolon marks everything to its right as a scribe-note: the reader ignores it completely. Only the form before the semicolon enters the pitcher and drops as a stone.

To add 1 and 2, with a single-semicolon trailing comment, She composed the addition with a trailing comment and submitted the form. The REPL read by the pitcher-notation conventions and returned:

The sum arrived unchanged, the marginal note never entering the water, exactly as the scribe intended.

Write a Clojure expression that computes the result, ignoring the comment.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2) ; sum of one and two"}}]}
````

### Family-template render _(seed 1071)_

**form**: `(+ 1 2) ; sum of one and two`  •  **expected**: `3`

````text
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

"A form is what's actually there on the pitcher's clay,"
Korvus the crow said, "after the conventions of writing and
reading have done their work. The runtime sees the cleaned-up form,
evaluates it, and gives back what it computes." To add 1 and 2, with a single-semicolon trailing comment,
He composed the addition with a trailing comment, submitted the
form, and the REPL — taking the form exactly as it was — handed
back the value.

What Clojure form computes the result, ignoring the comment? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2) ; sum of one and two"}}]}
````

---

## chalkmark — G1-09: Symbols vs values

_pool_: `_CHALKMARK_SUBPLOTS`

**The metaphor:** The chalk mark scratched on a smooth stone names the stone — it is not the stone itself. The mark can be carried, quoted, passed around; only when the form runs does the mark become the stone's weight. Mirrors `quote` / symbols.

### Story-scaffold render

**form**: `(symbol? 'hare)`  •  **expected**: `True`

````text
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened at the edge of the village.

Caw held up a chalk-scratched mark — the name 'hare — and pointed first at the chalk on her talon, then at an actual hare bounding across the meadow. She set the chalk mark beside the pitcher's rim.

She wanted to know whether the runtime would confirm the chalk mark as a name-thing — a symbol — not the bounding hare.

Quoting (the leading apostrophe) wraps the name as a chalk mark, preventing evaluation. `symbol?` asks the runtime: is this a name-mark? A quoted name is a symbol — chalk, not hare.

To ask whether a quoted name is a symbol, using the symbol? predicate, She composed the symbol-predicate on a quoted name and submitted the form. The REPL — distinguishing chalk-mark from stone — returned:

true — the runtime confirmed: 'hare is a chalk mark, a symbol, not the bounding creature the name might refer to.

Write a Clojure expression that computes whether a quoted name is a symbol.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'hare)"}}]}
````

### Family-template render _(seed 1063)_

**form**: `(symbol? 'hare)`  •  **expected**: `True`

````text
Hunger and thirst had driven the Crow far from her usual perch.

"There's a difference between *marking* the form and
*evaluating* it," Korvus the crow said. "Quote in any of its
shapes is the marking — the runtime hands you back the form,
not its value, unless you say otherwise." To ask whether a quoted name is a symbol, using the symbol? predicate,
He composed the symbol-predicate on a quoted name, submitted the
form, and the REPL — marking exactly what the form asked for —
returned the form-as-data, exactly as the chalk had directed.

Write a form whose evaluation gives whether a quoted name is a symbol.

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'hare)"}}]}
````

---

## tallywalk — G2-20: Counting

_pool_: `_TALLYWALK_SUBPLOTS`

**The metaphor:** The crow walks the rim of the pitcher, dropping each stone in turn, carrying the running count in one talon — the tally grows with every drop until the last stone goes in. Mirrors `reduce` / `count`.

### Story-scaffold render

**form**: `(count [1 2 3])`  •  **expected**: `3`

````text
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Sable walked the pitcher's rim in the village, three smooth stones set in a row along the clay ledge: 1, 2, 3. She carried her running tally in one talon, marking each stone as she passed.

She needed the total count of the row — how many pebbles sat along the rim before she dropped them.

`count` walks the collection talon-mark by talon-mark, incrementing the running tally at each element. When the last stone is passed, the final tally is the return value.

To count the elements in the vector containing 1, 2, and 3, They composed the count operation and submitted the form. The REPL walked the rim carrying the tally:

3 — three passes made, three stones counted, the tally settling as the answer.

What Clojure form computes the result of using count on the vector containing 1, 2, and 3? Submit it via `eval`.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(count [1 2 3])"}}]}
````

### Family-template render _(seed 1140)_

**form**: `(count [1 2 3])`  •  **expected**: `3`

````text
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Caw the crow walked the rim of the pitcher along the road, one claw at a
time, a small smooth stone held in the other talon for the running tally.
"Reduce is this walk," she said: "at each drop-point, you
combine the stone into the tally; at the end, the tally is your answer."
To count the elements in the vector containing 1, 2, and 3, She composed the count operation,
submitted the form, and the REPL — walking the rim, carrying the
tally — returned the final number.

Write a Clojure expression that computes the result of using count on the vector containing 1, 2, and 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count [1 2 3])"}}]}
````

---

## beadstring — G2-11: String concatenation with str

_pool_: `_BEADSTRING_SUBPLOTS`

**The metaphor:** The crow threads smooth pebbles on a vine in a row — each pebble a character in the sequence, the whole vine a pebble-string. Joining two vines end-to-end extends the string. Mirrors strings / sequences.

### Story-scaffold render

**form**: `(str "ab" "cd")`  •  **expected**: `abcd`

````text
Hunger and thirst had driven the Crow far from her usual perch. All this took place at the edge of the hilltop.

Korvus had two short pebble-strings woven on separate vines in the garden: one threaded a-b, the other c-d. He needed a single vine stringing all four pebbles in sequence.

He wanted to join the two vines end-to-end into one continuous pebble-string, the second starting exactly where the first left off.

`str` joins any number of string values into one, concatenating left to right. Each vine is appended to the previous; the result is one pebble-string in order.

To use str to splice the two-letter strings "ab" and "cd" into a single thread, She composed the string concatenation and submitted the form. The REPL spliced or counted as the form said:

a single vine carrying all four pebbles in sequence, the join seamless, the pebble-string complete at beak-reach.

Write a Clojure expression that computes the result of using str to splice "ab" and "cd".

---

{"tool_calls":[{"name":"eval","args":{"form":"(str \"ab\" \"cd\")"}}]}
````

### Family-template render _(seed 1077)_

**form**: `(str "ab" "cd")`  •  **expected**: `abcd`

````text
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was atop the hilltop.

Korvus the crow, clicking the beak in self-satisfaction, yanked at the pebble-vine atop the hilltop
without bothering to count the pebbles first. Sable the crow
stopped him: strings are precise — every pebble in
its place, every position counted. To use str to splice the two-letter strings "ab" and "cd" into a single thread,
they composed the string concatenation, submitted the form,
and the REPL — handling the vine carefully — returned the right
answer.

What Clojure form computes the result of using str to splice "ab" and "cd"? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(str \"ab\" \"cd\")"}}]}
````

---

## circuit — G5-22: recur — first taste

_pool_: `_CIRCUIT_SUBPLOTS`

**The metaphor:** The crow loops back to the stone-pile after each drop without lifting off the rim — stone after stone in a tight circuit, each iteration calling back to the start without growing the flight path. Mirrors `loop` / `recur`.

### Story-scaffold render

**form**: `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`  •  **expected**: `120`

````text
Hunger and thirst had driven the Crow far from her usual perch. This was near the hilltop.

Caw stood at the pitcher's rim in the hilltop field, a circuit chalked beneath her feet: start with n=5 and accumulator=1. Each lap, multiply the accumulator by n, step n down by one — loop without lifting from the rim.

She needed to run the circuit until n hit zero, then read the final accumulated count as the answer.

`loop` opens the circuit with initial bindings. `recur` loops back to the top without growing the call stack — no new flight, just another lap. When the zero-check passes `acc` is returned as the result.

To walk a small circuit five times, multiplying a running tally by the current step each lap, until the step counter reaches zero, They composed a factorial computation via loop and recur and submitted the form. The REPL looped without growing the trail:

120 — five laps, the accumulator multiplied each pass, the final product surfacing when n hit zero.

Question: write a Clojure expression for the factorial of 5 computed by walking a circuit.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
````

### Family-template render _(seed 1154)_

**form**: `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`  •  **expected**: `120`

````text
It is said that wit, more than strength, is the friend of the thirsty Crow.

Korvus the crow, preening at the thought of knowing, distrusted the very idea of a
circuit: surely you'd just walk forever? Sable the crow
smiled patiently — the base case is the runner's compass.
To walk a small circuit five times, multiplying a running tally by the current step each lap, until the step counter reaches zero, they composed a factorial computation via loop and recur,
submitted the form, and the REPL — looping the right number
of times, then stopping — returned the value cleanly.

Write a Clojure expression that computes the factorial of 5 computed by walking a circuit.

---

I write the higher-order form so the REPL can compute.

{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
````

---
