# Metaphor demo — tortoise-hare curriculum

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
for abstract subjects. Across 216 subjects the split is:

- 8 atoms (form-display IS the lesson)
- 172 metaphor-rich (22 families) — 22 of these have
  story-scaffold slots authored (Phase C demo); the rest
  render with the family-template only until their
  scenario/need/mapping/resolution are authored
- 36 abstract-by-nature (kept generic honestly)

---

## atom — G1-01: Eval as substitution

_pool_: `_SHARED_SUBPLOTS`

**The metaphor:** For atoms (literals), the form IS the answer. The user_msg deliberately shows the form (`{form_display}`); copy-from-prompt is the lesson — submit the literal as-is.

### Atom render

**form**: `42`  •  **expected**: `42`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened along the road.

A small audience of forest creatures had gathered along the road to watch
Whisker the hare attempt to outwit Slowpoke the tortoise at reading the REPL.
Slowpoke pointed to the value 42 and read out the form aloud:
`42`. The crowd waited to see who would correctly write
the form to submit.

Write a Clojure expression that computes the value of 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
````

---

## pouch — G3-03: let — local binding

_pool_: `_POUCH_SUBPLOTS`

**The metaphor:** A small leather pouch tied at the Tortoise's hip. Whatever is tucked inside is held just for one stretch of road; by the next milestone the pouch is empty again. Mirrors `let`-binding scope: the binding lives only inside the form.

### Story-scaffold render

**form**: `(let [x 3] (+ x 1))`  •  **expected**: `4`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. This was near the road.

Mossback the tortoise had been counting along a stretch of road. She set a single pebble — worth 3 acorns — into the small leather pouch tied at her hip and gave the pouch's contents the local name x.

Just past the next milestone she'd want the running total — what x plus one more acorn would come to. After the milestone, the pouch would empty and x would mean nothing again.

`let` binds a value into a pouch named locally for the stretch of one form. Inside `(+ x 1)`, x means 3; outside the form, x is empty and unknown again. The binding is in force only for the form's stretch.

To bind a value of 3 to a local name x for one stretch, then return that value plus one, He composed the local binding and addition with the binding tucked safely into the pouch and submitted the form. The REPL pulled from the pouch as the form directed:

the pouch yielded 3, the +1 added a fourth acorn, and the running total stood at 4 — exactly what the next milestone needed.

Question: write a Clojure expression for the running total after binding x to 3 and adding 1.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
````

### Family-template render _(seed 96386568)_

**form**: `(let [x 3] (+ x 1))`  •  **expected**: `4`

````text
It was well known among the animals that the Hare boasted of his speed at every chance.

Mossback the tortoise had been counting along a stretch of road. She set a single pebble — worth 3 acorns — into the small leather pouch tied at her hip and gave the pouch's contents the local name x.

Just past the next milestone she'd want the running total — what x plus one more acorn would come to. After the milestone, the pouch would empty and x would mean nothing again.

`let` binds a value into a pouch named locally for the stretch of one form. Inside `(+ x 1)`, x means 3; outside the form, x is empty and unknown again. The binding is in force only for the form's stretch.

To bind a value of 3 to a local name x for one stretch, then return that value plus one, She composed the local binding and addition with the binding tucked safely into the pouch and submitted the form. The REPL pulled from the pouch as the form directed:

the pouch yielded 3, the +1 added a fourth acorn, and the running total stood at 4 — exactly what the next milestone needed.

Write a form whose evaluation gives the running total after binding x to 3 and adding 1.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
````

---

## recipe — G3-09: defn — named function

_pool_: `_RECIPE_SUBPLOTS`

**The metaphor:** A recipe-card posted on the road, naming a paw-step routine that any animal can follow. Mirrors `defn`: a named, reusable procedure with parameters — the next runner along the road picks up the card and follows it.

### Story-scaffold render

**form**: `(do (defn dbl [x] (* x 2)) (dbl 5))`  •  **expected**: `10`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. This was near the road.

Twice as many animals had arrived for dinner as Mossback the tortoise had planned for, and every recipe now needed twice its salt.

Mossback wanted a doubling routine written once and posted under a name any cook could shout — tonight's first reach being 5 pinches of salt.

`defn` writes the routine on a recipe-card and posts the card under a name. The name (here `dbl`) is what the kitchen shouts to invoke the doubling; the parameter `x` is the quantity the cook brings.

To define a recipe named dbl that takes a quantity and serves twice that, then call dbl on 5 pinches, He wrote out the named recipe-card and its first call on a card and submitted the form. The REPL ran the recipe end to end:

the named recipe ran on 5 and handed back twice that — exactly what the doubled crowd would need.

Question: write a Clojure expression for the doubled count after defining a recipe named dbl and calling it on 5.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn dbl [x] (* x 2)) (dbl 5))"}}]}
````

### Family-template render _(seed 3890326)_

**form**: `(do (defn dbl [x] (* x 2)) (dbl 5))`  •  **expected**: `10`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

"Recipes can feed into one another," Mossback the tortoise said,
spreading several cards on the path. "What one recipe serves, the
next can take as its ingredient — together they make a longer
routine." To define a recipe named dbl that takes a quantity and serves twice that, then call dbl on 5 pinches, He composed
the named recipe-card and its first call, submitted the form, and the REPL — walking
through the recipe in order — handed back the value at the
end.

What Clojure form computes the doubled count after defining a recipe named dbl and calling it on 5? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn dbl [x] (* x 2)) (dbl 5))"}}]}
````

---

## basket — G4-08: assoc — pin a tag on the basket

_pool_: `_BASKET_SUBPLOTS`

**The metaphor:** A basket on the path: original sits untouched, you get a fresh one back. Mirrors immutable updates on collections — `assoc` doesn't mutate the original map; it returns a new one with the additional tag pinned on.

### Story-scaffold render

**form**: `(assoc {:a 1} :b 2)`  •  **expected**: `{':a': 1, ':b': 2}`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. This was near the road.

Mossback the tortoise's foraging-basket had compartments stitched into its sides — an open area at the top, plus named pouches :a and :b. Pouch :a already held 1 acorn from the morning's gathering.

Pip the hare arrived from the orchard with 2 more acorns. Mossback decided they belonged in pouch :b — and pouch :a's acorn should stay exactly where it was.

`assoc` associates a value with a named compartment of the basket. The basket's shape stays the same — :a still holds its 1, and :b now holds the new 2 — exactly as the foraging called for.

To associate value 2 with the :b compartment of a basket already binding :a to 1, He composed the assoc operation for the basket and submitted the form. The REPL handed back the arrangement:

the basket carried both — 1 in :a, 2 in :b — ready for the rest of the day's gathering.

Question: write a Clojure expression for the basket after associating value 2 with the :b compartment.

---

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:a 1} :b 2)"}}]}
````

### Family-template render _(seed 8407194)_

**form**: `(assoc {:a 1} :b 2)`  •  **expected**: `{':a': 1, ':b': 2}`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. This was near the garden.

Shelly the tortoise pointed to a small basket on the path in the garden.
"Whatever I want to do with what's inside," she
said, "I read from the basket, work the change, and the basket
itself stays as it was — what I get back is a fresh arrangement."
To associate value 2 with the :b compartment of a basket already binding :a to 1, She composed the assoc operation,
submitted the form, and let the REPL handle the basket exactly
as the operation prescribed.

Write a form whose evaluation gives the basket after associating value 2 with the :b compartment.

---

I write the collection literal and let the REPL evaluate.

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:a 1} :b 2)"}}]}
````

---

## sieve — G5-10: map — pour through, transform each

_pool_: `_SIEVE_SUBPLOTS`

**The metaphor:** A sieve over an empty basket; the rule attached at its mouth decides what each pebble becomes. Mirrors `map`/`filter`/transducers — pour the basket through the sieve, and what lands below is the result.

### Story-scaffold render

**form**: `(map inc [1 2 3])`  •  **expected**: `[2, 3, 4]`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. This was near the road.

A row of three small acorns lay on a flat stone — the morning's first gathering, with counts of 1, 2, and 3.

Each acorn was missing a single bud at the cap. Mossback the tortoise wanted to add one bud to every acorn before sending the row to market — without pulling the row apart.

`map` is a sieve with a rule attached at its mouth. Pour the row through, and each acorn passes the rule — here, `inc`, adding one bud — coming out the other side budded by one. The shape stays a row; only the counts step up.

To pour the vector containing 1, 2, 3 through a sieve whose rule is inc, collecting each transformed element, He composed mapping increment over a vector as the sieve's rule, poured the input through, and submitted the form. The REPL caught what landed below:

what landed below the sieve was the same three acorns, each budded one more — counts of 2, 3, and 4.

Question: write a Clojure expression for the sequence produced by passing the vector containing 1, 2, and 3 through the inc-sieve.

---

{"tool_calls":[{"name":"eval","args":{"form":"(map inc [1 2 3])"}}]}
````

### Family-template render _(seed 20992547)_

**form**: `(map inc [1 2 3])`  •  **expected**: `[2, 3, 4]`

````text
It was well known among the animals that the Hare boasted of his speed at every chance.

Mossback the tortoise balanced a sieve over an empty basket. "The
pebbles go in at the top," he said, "and the
sieve does its work — applying the rule, choosing or changing —
and what lands in the basket below is the result." To
pour the vector containing 1, 2, 3 through a sieve whose rule is inc, collecting each transformed element, He composed mapping increment over a vector,
poured the input through, submitted the form, and the REPL
collected what fell into the receiving basket.

Write a Clojure expression that computes the sequence produced by passing the vector containing 1, 2, and 3 through the inc-sieve.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(map inc [1 2 3])"}}]}
````

---

## notebook — G9-03: atom — coordinated mutable state

_pool_: `_NOTEBOOK_SUBPLOTS`

**The metaphor:** A notebook open on a tree stump. Any animal can read; updates happen atomically; the bell on the corner rings on each change. Mirrors `atom`/`ref`/`swap!` — shared state with safe concurrent updates.

### Story-scaffold render

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. This was near the road.

The forest's berry-tally lived on a notebook open on the tree stump in the middle of the meadow. Anyone returning from foraging walked up, read the running total, and added their own count.

Today's tally page started at 0 — no one had foraged yet. Mossback the tortoise's first handful was a single berry, and she wanted the page to reflect it.

An `atom` is the notebook on the stump, named here `a`. `swap!` reads the current page, applies a function (here `inc`, adding one), and writes the new page back — all atomically. `@a` dereferences to read the page.

To set up a shared notebook starting at 0, atomically add one to its page, then read the page, He composed atom, swap, and deref for the notebook and submitted the form. The REPL applied the update on the stump:

Mossback dereferenced the page and read the new tally — one berry, exactly her contribution.

Question: write a Clojure expression for the running tally on the page after one foraging contribution.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
````

### Family-template render _(seed 92978719)_

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

"When I want to update the notebook," Slowpoke the tortoise said,
"I don't pick it up and walk away — I read the page, apply the
change, and write it back, all in a single motion. If two
animals arrive at once, the runtime makes sure only one of us
goes through at a time." To set up a shared notebook starting at 0, atomically add one to its page, then read the page, He
composed atom, swap, and deref for the notebook, submitted the form,
and the REPL applied the update atomically.

Write a form whose evaluation gives the running tally on the page after one foraging contribution.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
````

---

## acorn — G2-04: min and max

_pool_: `_ACORN_SUBPLOTS`

**The metaphor:** Acorns sorted into heaps, counted, divided, combined. The number is just the count of acorns; the operation is what the Tortoise does with the heap. Mirrors arithmetic, comparisons, multi-arg operators.

### Story-scaffold render

**form**: `(min 1 2 3)`  •  **expected**: `1`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. This was near the road.

Mossback the tortoise laid out three small acorn-counts on a flat stone — 1 from a dawn trip, 2 from a midday trip, 3 from an afternoon trip.

She wanted to know which trip had been the lightest, to plan tomorrow's routing.

`min` walks the heaps and returns the smallest count. The acorns themselves stay where they are; only the runtime's verdict — the smallest number — comes back.

To find the minimum of 1, 2, and 3, He composed the minimum of three numbers and submitted the form. The REPL counted out the answer:

the runtime named the lightest trip's count: 1, the dawn trip the smallest of the three.

Question: write a Clojure expression for the smallest of 1, 2, and 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(min 1 2 3)"}}]}
````

### Family-template render _(seed 51556413)_

**form**: `(min 1 2 3)`  •  **expected**: `1`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

"Whatever the heap looks like after the operation,"
Slowpoke the tortoise said, "the runtime gives the exact count —
small or large, fraction or whole, the answer is precise." To
find the minimum of 1, 2, and 3, He composed the minimum of three numbers,
submitted the form, and the REPL handed back the value, exactly
as the operation had produced it.

Write a Clojure expression that computes the smallest of 1, 2, and 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(min 1 2 3)"}}]}
````

---

## gate — G2-13: and / or — short-circuit

_pool_: `_GATE_SUBPLOTS`

**The metaphor:** Gates on the trail that pass or stop the value. The first closed gate stops the chain; the value at that gate is what comes back. Mirrors short-circuit boolean logic — `and` / `or` / `not` / falsey rules.

### Story-scaffold render

**form**: `(and true true)`  •  **expected**: `True`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. This was near the road.

Two small wooden gates stood at the start of the meadow trail. Each gate's verdict-stone was carved with the value the runner would carry to it — and today's two stones both read true.

Mossback the tortoise wanted to know whether both gates would let the runner through together, or whether the first one would close and stop the chain.

`and` walks the gates left to right: the first false closes the chain and that value comes back; otherwise the value at the last gate is what comes back. With both stones reading true, the chain holds and the last gate's true is the verdict.

To test whether two trues both pass through an and-chain of gates, He composed the logical and and submitted the form. The REPL let the gates decide:

both gates stood open, and the value at the last gate — true — passed back as the chain's verdict.

Question: write a Clojure expression for the result of passing true and true through the and-chain of gates.

---

{"tool_calls":[{"name":"eval","args":{"form":"(and true true)"}}]}
````

### Family-template render _(seed 33296541)_

**form**: `(and true true)`  •  **expected**: `True`

````text
It was well known among the animals that the Hare boasted of his speed at every chance. All this took place by the orchard.

Bramble the hare sprinted toward the gate near the orchard, swaggering through the underbrush,
certain it would swing open for her. Mossback the tortoise
slowed and watched: the only way to know which way the gate
would swing was to actually carry the value to it. To
test whether two trues both pass through an and-chain of gates, he composed the logical and,
submitted the form, and the REPL settled the matter — the gate
had swung exactly as the rules said, regardless of Bramble the hare's
guess.

Write a Clojure expression that computes the result of passing true and true through the and-chain of gates.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(and true true)"}}]}
````

---

## fork — G5-04: cond — multi-arm crossroads

_pool_: `_FORK_SUBPLOTS`

**The metaphor:** A fork at a crossroads. Each arm is marked by a condition-stone; the runner walks past each and takes the first arm whose stone says true. Mirrors `if`/`cond`/`case`/`when`.

### Story-scaffold render

**form**: `(cond (= 1 2) :a (= 1 1) :b :else :c)`  •  **expected**: `':b'`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. This was near the road.

The trail forked into three arms, each marked by a small condition-stone — the first carved `(= 1 2)`, the second `(= 1 1)`, the third `:else`.

Mossback the tortoise wanted the runtime to walk the stones in order and take the first arm whose stone read true.

`cond` walks each (condition, value) pair in order. The first stone is false (skip), the second is true (take that arm; return its value); the third is never reached.

To walk three condition-stones in order, taking the arm whose stone first reads true, He composed the multi-clause conditional and submitted the form. The REPL took the right arm:

the runtime took the second arm and returned :b, the value that arm carried.

Question: write a Clojure expression for the value of the first arm whose stone reads true.

---

{"tool_calls":[{"name":"eval","args":{"form":"(cond (= 1 2) :a (= 1 1) :b :else :c)"}}]}
````

### Family-template render _(seed 37603403)_

**form**: `(cond (= 1 2) :a (= 1 1) :b :else :c)`  •  **expected**: `':b'`

````text
It was well known among the animals that the Hare boasted of his speed at every chance. It happened by the meadow.

The trail in the meadow opened into a crossroads, each arm marked by a
small condition-stone. "Branching forms work like this,"
Mossback the tortoise said: "the runner walks past the stones in
order, takes the first arm whose stone says true, and the value
of that arm is what comes back." To walk three condition-stones in order, taking the arm whose stone first reads true,
He composed the multi-clause conditional, submitted the
form, and the REPL took the right arm and returned its
value.

What Clojure form computes the value of the first arm whose stone reads true? Submit it via `eval`.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(cond (= 1 2) :a (= 1 1) :b :else :c)"}}]}
````

---

## roadsign — G6-03: require — borrowing a scroll

_pool_: `_ROADSIGN_SUBPLOTS`

**The metaphor:** Posted signs on the road; library of scrolls. A `def` is a sign by the road; a namespace is a scroll; `require` borrows the scroll, fully-qualified names point library-section-title.

### Story-scaffold render

**form**: `(clojure.string/upper-case "hare")`  •  **expected**: `'HARE'`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. This was near the road.

The library by the road kept a scroll on its shelves called `clojure.string`. Among its signs was a routine named `upper-case` — a routine that took a string and returned the same letters, capitalized.

Mossback the tortoise wanted the capitalized form of the four-letter word `hare`, for a road-sign she was painting.

When a routine lives on a scroll, you call it by both names together: scroll-name slash routine-name — `clojure.string/upper-case`. The runtime fetches the scroll and invokes the routine on the argument.

To call the upper-case routine on the clojure.string scroll, applied to the four-letter string hare, He composed calling a fully-qualified string function and submitted the form. The REPL read the signs and replied:

the routine returned the four letters in capitals, ready for the road-sign Mossback was painting.

Question: write a Clojure expression for the capitalized form returned by the upper-case routine on the scroll.

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"hare\")"}}]}
````

### Family-template render _(seed 53205677)_

**form**: `(clojure.string/upper-case "hare")`  •  **expected**: `'HARE'`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Mossback the tortoise drove a small wooden post near the road and nailed a
fresh sign to it. "A def is a sign by the road," he
said. "Anyone passing reads the name, learns the value, and can
refer to it later by name alone." To call the upper-case routine on the clojure.string scroll, applied to the four-letter string hare,
He composed calling a fully-qualified string function, submitted the
form, and the REPL planted the sign — the name now bound to its
value for any later runner along the road.

Question: write a Clojure expression for the capitalized form returned by the upper-case routine on the scroll.

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"hare\")"}}]}
````

---

## safetynet — G7-02: try / catch

_pool_: `_SAFETYNET_SUBPLOTS`

**The metaphor:** A net stretched beneath a high jump. The runner can fall — the net catches them; the run continues, only the path bends. Mirrors error handling: `try`/`catch`, the practice-meadow REPL where stumbles cost nothing.

### Story-scaffold render

**form**: `(try (/ 1 0) (catch Exception e -1))`  •  **expected**: `-1`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. This was near the road.

Mossback the tortoise was about to ask the runtime for the result of dividing 1 acorn into 0 piles — a division she knew would throw, because dividing by zero isn't a thing the runtime can do.

She didn't want the throw to end the run. She wanted the form to come back with -1 as a placeholder so the rest of the work could continue.

`try`/`catch` is a net beneath the leap. The throw still happens, but the catch-arm catches the Exception cleanly. Whatever the catch-arm returns is what the form yields — here, the placeholder -1.

To attempt to divide 1 by 0; when the runtime throws, catch the Exception and return -1 from the catch arm, He composed the handler for a division-by-zero error and submitted the form. The REPL — net in place — handed back the value:

the throw happened, the catch caught it, and the form yielded -1 — the placeholder Mossback had specified.

Question: write a Clojure expression for the value the catch arm returns when the divide-by-zero throw is caught.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 1 0) (catch Exception e -1))"}}]}
````

### Family-template render _(seed 33133535)_

**form**: `(try (/ 1 0) (catch Exception e -1))`  •  **expected**: `-1`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. This was in the woods.

"There's a discipline to running safely," Mossback the tortoise said,
"and it starts with checking — making sure the form does what it
claims, catching what could go wrong before it does." To
attempt to divide 1 by 0; when the runtime throws, catch the Exception and return -1 from the catch arm, He composed the handler for a division-by-zero error,
submitted the form, and the REPL — applying whatever check or
catch the form had asked for — returned the value the discipline
had earned.

Question: write a Clojure expression for the value the catch arm returns when the divide-by-zero throw is caught.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 1 0) (catch Exception e -1))"}}]}
````

---

## scroll — G7-12: slurp / spit — IO

_pool_: `_SCROLL_SUBPLOTS`

**The metaphor:** Scrolls written and read. Marginalia (metadata) along the side. Drinking from / writing onto a scroll — `slurp`/`spit`. Reading line by line — `line-seq`. Open and roll up — `with-open`.

### Story-scaffold render

**form**: `(count "hare
tortoise
")`  •  **expected**: `14`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. This was near the road.

Mossback the tortoise had a small two-line message on a scroll — the word `hare` on one line, `tortoise` on the next, each line ending with a newline-mark.

She wanted to know whether the message would fit in her message-pouch — and to know that, she needed the total character count, including the newline-marks.

`count` on a string walks each character — visible letters and the invisible newline-marks alike — returning the total. The scroll itself is unchanged.

To count every character in a two-line string ending each line with a newline-mark, including the marks, He composed the character count of a multi-line string and submitted the form. The REPL — quill in hand — completed the scroll-work:

the runtime tallied 14 characters: the four of `hare`, a newline, the eight of `tortoise`, and a final newline — the fit she had hoped for.

Question: write a Clojure expression for the total characters in a two-line string with newline-marks at each line's end.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count \"hare\ntortoise\n\")"}}]}
````

### Family-template render _(seed 17018218)_

**form**: `(count "hare
tortoise
")`  •  **expected**: `14`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

"There's the world inside the REPL," Mossback the tortoise said,
"and the world outside it. Scrolls are how the two meet — a value
crosses out and becomes letters on parchment, or letters on
parchment cross in and become a value again." To count every character in a two-line string ending each line with a newline-mark, including the marks,
He composed the character count of a multi-line string, submitted the
form, and the REPL — bridging the two worlds — handed back the
value the work had carried.

Write a Clojure expression that computes the total characters in a two-line string with newline-marks at each line's end.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"hare\ntortoise\n\")"}}]}
````

---

## guild — G8-04: Protocol definition

_pool_: `_GUILD_SUBPLOTS`

**The metaphor:** A guild any species can join. The guild lists what its members must be able to do — the methods. Any animal that signs the ledger may claim membership. Mirrors `defprotocol` / `extend-protocol`.

### Story-scaffold render

**form**: `(do (defprotocol Pace (speed [this])) (some? Pace))`  •  **expected**: `True`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. This was near the road.

Mossback wanted to found a Runners' guild named `Pace`. Members would have to perform `speed`, taking the runner as its argument.

Before any species could sign, the guild had to be founded — and Mossback wanted to confirm the name was now real to the runtime.

`defprotocol Pace (speed [this])` founds the guild. `(some? Pace)` then asks whether the name is non-nil.

To found a Runners' guild named Pace whose only requirement is a method speed taking the runner as its single argument; then check whether the guild's name is now a real thing in the runtime, He composed a protocol definition and submitted the form. The REPL — checking the guild book — dispatched cleanly:

the runtime confirmed the guild was real — `some?` returned true.

Question: write a Clojure expression for whether the Runners' guild named Pace is real after the founding.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (some? Pace))"}}]}
````

### Family-template render _(seed 35529658)_

**form**: `(do (defprotocol Pace (speed [this])) (some? Pace))`  •  **expected**: `True`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. All this took place near the woods.

"What makes a guild useful," Slowpoke the tortoise said, "is that
the call is the same for every member, but each species answers
in its own way. The runtime looks up which species the runner
is, then runs that species' answer." To found a Runners' guild named Pace whose only requirement is a method speed taking the runner as its single argument; then check whether the guild's name is now a real thing in the runtime,
He composed a protocol definition, submitted the
form, and the REPL — dispatching to the right species — returned
the species-specific value.

Write a form whose evaluation gives whether the Runners' guild named Pace is real after the founding.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (some? Pace))"}}]}
````

---

## sortingtable — G8-08: defmulti — multimethod dispatch

_pool_: `_SORTINGTABLE_SUBPLOTS`

**The metaphor:** A sorting-table with arms branching off the sides. Runners walk up; the table reads what's stamped on each runner; the matching arm runs. Mirrors `defmulti`/`defmethod` — open-dispatch by any criterion.

### Story-scaffold render

**form**: `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))`  •  **expected**: `':swift'`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. This was near the road.

Mossback the tortoise set up a sorting-table at the edge of the meadow. Runners would walk up; the table would read each runner's :species stamp and route them to the matching arm.

Today's first arm she added was for hares: any runner stamped :hare should be routed to an arm that returns the swift-pace keyword. Today's first runner arrived stamped :hare.

`defmulti` declares the table and what it sorts by (`:species`). `defmethod` adds an arm for a specific stamp (`:hare`). Calling `pace` on a runner reads the stamp and routes to the matching arm.

To declare a sorting-table named pace that reads each runner's :species stamp; add an arm for the :hare stamp returning the swift-pace keyword; then route a runner stamped :hare through the table, He composed the multimethod and its first arm and submitted the form. The REPL routed through the table:

the table read the :hare stamp, took the matching arm, and returned the swift-pace keyword — exactly the right pace for the species.

Question: write a Clojure expression for the pace returned for a runner stamped :hare after the table routes to its arm.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))"}}]}
````

### Family-template render _(seed 52002123)_

**form**: `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))`  •  **expected**: `':swift'`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened at the edge of the meadow.

Whisker the hare, with a smug grin, leaped onto the sorting-table without
showing his stamp. Mossback the tortoise pointed at the
edge of the table: every runner must show the stamp the table
sorts by. To declare a sorting-table named pace that reads each runner's :species stamp; add an arm for the :hare stamp returning the swift-pace keyword; then route a runner stamped :hare through the table, he composed
the multimethod and its first arm, submitted the form, and the REPL — reading the
stamp first, dispatching second — returned the value from the
correct branch.

Question: write a Clojure expression for the pace returned for a runner stamped :hare after the table routes to its arm.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))"}}]}
````

---

## carryingcase — G8-03: defrecord — labeled compartments

_pool_: `_CARRYINGCASE_SUBPLOTS`

**The metaphor:** A small wooden case with named compartments. The stamp on the outside says what kind of case; the labels on the inside say what each compartment holds. Mirrors `deftype` / `defrecord`.

### Story-scaffold render

**form**: `(do (defrecord Runner [name pace]) (:pace (->Runner "Alice" :slow)))`  •  **expected**: `':slow'`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. This was near the road.

Mossback the tortoise was outfitting the meadow's runners with carrying-cases — small wooden cases with two named compartments inside, one labeled `name` and one labeled `pace`. The case-stamp on the outside would read `Runner`.

She wanted to define the Runner case-shape, then build one such case for a tortoise named Alice carrying a deliberate-pace keyword, and finally read what was in the pace compartment.

`defrecord` declares the case-shape: stamp `Runner`, compartments [name pace]. `(->Runner "Alice" :slow)` constructs a case filling the compartments in order. `(:pace …)` reads the named compartment by its keyword.

To define a Runner case with two named compartments, name and pace; build a Runner case for Alice with a deliberate-pace keyword; then read the pace compartment, He composed reading the pace compartment of a Runner case and submitted the form. The REPL constructed the case:

the case held the runner's name and the pace keyword in their compartments; reading the pace compartment returned exactly what the case had been built with.

Question: write a Clojure expression for the value in the pace compartment of a freshly-built Runner case for Alice.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defrecord Runner [name pace]) (:pace (->Runner \"Alice\" :slow)))"}}]}
````

### Family-template render _(seed 58982356)_

**form**: `(do (defrecord Runner [name pace]) (:pace (->Runner "Alice" :slow)))`  •  **expected**: `':slow'`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Shelly the tortoise held up a small wooden case near the garden, its inside
divided into labeled compartments. "Defrecord makes a case like
this," she said: "named compartments holding
specific things; a stamp on the outside saying what kind of case
it is." To define a Runner case with two named compartments, name and pace; build a Runner case for Alice with a deliberate-pace keyword; then read the pace compartment, She composed
reading the pace compartment of a Runner case, submitted the form, and the REPL — constructing
the case, filling its compartments — returned the value the case
held or carried.

What Clojure form computes the value in the pace compartment of a freshly-built Runner case for Alice? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defrecord Runner [name pace]) (:pace (->Runner \"Alice\" :slow)))"}}]}
````

---

## toolshed — G11-02: Method call — borrowing a host tool

_pool_: `_TOOLSHED_SUBPLOTS`

**The metaphor:** A different toolshed of foreign tools, none carved by the Tortoise. Each tool has a label; calling it uses dot-prefix for instance, slash for static. Mirrors host interop — `.method`, `Class/static`, `(new …)`, type hints.

### Story-scaffold render

**form**: `(.toUpperCase "abc")`  •  **expected**: `'ABC'`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. This was near the road.

Mossback the tortoise was using a small string of three letters from the foreign toolshed — `abc` — and she wanted the host's own routine for capitalizing strings, kept under the name `toUpperCase`.

She didn't want to write a Clojure routine for capitalization; she wanted to call the host's own routine directly.

Host instance methods are called with dot-prefix on the instance: `(.toUpperCase "abc")` invokes the host's routine on the string. The runtime crosses the boundary to the host, calls the method, and brings the result back.

To call the host's toUpperCase routine on the three-letter string abc using the dot-prefix calling convention, He composed the host method toUpperCase and submitted the form. The REPL — calling into the foreign toolshed — returned:

the host returned the three letters in capitals, and the runtime brought the value back as a Clojure string.

Question: write a Clojure expression for the capitalized result the host's toUpperCase returns on the three-letter string abc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
````

### Family-template render _(seed 74392710)_

**form**: `(.toUpperCase "abc")`  •  **expected**: `'ABC'`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

Bramble the hare, boasting at every turn, grabbed at the foreign toolshed
without checking which tool was which. The wrong tool, of course,
made an awful sound. Slowpoke the tortoise sighed and walked over: to
call the host's toUpperCase routine on the three-letter string abc using the dot-prefix calling convention required reading the toolshed's labels carefully.
He composed the host method toUpperCase, submitted the
form, and the REPL — calling the right host method by name —
returned the value cleanly while Bramble watched, chastened.

Question: write a Clojure expression for the capitalized result the host's toUpperCase returns on the three-letter string abc.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
````

---

## runnerahead — G9-13: future — runner sent ahead

_pool_: `_RUNNERAHEAD_SUBPLOTS`

**The metaphor:** A messenger sent down the road while the Tortoise carries on. Later, the Tortoise asks the runner to hand back the result. Mirrors `future` / `agent` / `promise` / `await`.

### Story-scaffold render

**form**: `@(future (+ 1 2))`  •  **expected**: `3`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. It happened by the woods.

Mossback the tortoise dispatched a young messenger down the long road
by the woods, work in paw. "The runner goes ahead while we keep on
with our own business," he said, "and when we
need the result we ask the runner to hand it back." To
dispatch a runner to compute the sum of 1 and 2; later, ask the runner for the answer, He composed future, add, deref,
submitted the form, and the REPL — sending the runner, fetching
the result later — returned the value when it was ready.

Write a form whose evaluation gives the value the messenger returns from adding 1 and 2.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"@(future (+ 1 2))"}}]}
````

### Family-template render _(seed 88118324)_

**form**: `@(future (+ 1 2))`  •  **expected**: `3`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

"The hard part isn't sending the runner," Shelly the tortoise said.
"The hard part is being patient enough to wait for the answer
when it comes — not snatching too early, not giving up too soon.
The runtime makes that easier than it sounds." To dispatch a runner to compute the sum of 1 and 2; later, ask the runner for the answer,
She composed future, add, deref, submitted the
form, and the REPL — coordinating the wait properly — returned
the runner's answer when the runner had it ready.

Write a form whose evaluation gives the value the messenger returns from adding 1 and 2.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"@(future (+ 1 2))"}}]}
````

---

## rewriterule — G10-03: defmacro — rule that rewrites the recipe

_pool_: `_REWRITERULE_SUBPLOTS`

**The metaphor:** A scribe with the power to rewrite the recipe before the runtime ever cooks it. The rule pays off when many recipes need the same rewriting. Mirrors `defmacro` / `macroexpand` / `eval`.

### Story-scaffold render

**form**: `` (do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3)) ``  •  **expected**: `3`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. This was near the road.

Mossback the tortoise was tired of writing `if`/`do` by hand for every form where she wanted several steps to run only if a condition held.

She wanted a rule called `my-when` that rewrote the shorter form `(my-when t body...)` into the longer `(if t (do body...))` — once written, applicable to any test and body.

`defmacro` defines a rewrite-rule. The rule's body uses syntax-quote and unquote-splicing to build the rewritten form. The runtime applies the rule first, then evaluates the rewritten form normally.

To define a rule named my-when that rewrites (my-when t body...) into (if t (do body...)); then invoke it with the test true and a three-expression body, He composed defining a conditional macro and invoking it and submitted the form. The REPL — applying the rewrite, then evaluating the rewritten form — returned:

the rewritten form ran the body, kept only the last-step value, and returned it — the rule had saved Mossback the longer writing.

Question: write a Clojure expression for the value the rewritten if-do form returns when the test is true and the body has three expressions.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

### Family-template render _(seed 43771232)_

**form**: `` (do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3)) ``  •  **expected**: `3`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

"Here's the difference between a rule and a recipe,"
Mossback the tortoise said. "A recipe takes ingredients and makes a
dish. A rule takes a *form* and makes a different *form* — only
then does the runtime get to evaluate it." To define a rule named my-when that rewrites (my-when t body...) into (if t (do body...)); then invoke it with the test true and a three-expression body,
He composed defining a conditional macro and invoking it, submitted the
form, and the REPL — applying the rule to the form first, then
evaluating — handed back the value the rewritten form had
produced.

Write a Clojure expression that computes the value the rewritten if-do form returns when the test is true and the body has three expressions.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

---

## scribe — G1-12: Parens group — fence-posts

_pool_: `_SCRIBE_SUBPLOTS`

**The metaphor:** The scribe's reading conventions. Comments are marginalia skipped by the eye. Whitespace is the breath between words. Parens are fence-posts marking which things go together. `do` is a sequence in one breath. Reader macros are shorthand.

### Story-scaffold render

**form**: `(+ 2 3)`  •  **expected**: `5`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. This was near the road.

Mossback the tortoise chalked a small expression on the path: the plus-mark, then 2, then 3, all wrapped in a single set of parens. Pip the hare paused — was the answer 6 (parens means multiply, surely?), or maybe 23?

Mossback wanted to show that the parens are fence-posts, not multiplication: they mark which tokens belong together as one form, nothing more.

Parens in Clojure group: the first token inside is the operator (`+`), the rest are arguments (2, 3). The runtime applies + to 2 and 3 — the parens themselves do no math.

To add 2 and 3, He composed the simple addition and submitted the form. The REPL read by the conventions and returned:

the runtime applied + to 2 and 3 and returned 5 — not 6, not 23, just the sum the form had asked for.

Question: write a Clojure expression for the result of adding 2 and 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 2 3)"}}]}
````

### Family-template render _(seed 7082350)_

**form**: `(+ 2 3)`  •  **expected**: `5`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. This was along the road.

"A form is what the reader sees," Slowpoke the tortoise said,
"after the conventions have been applied. Some marks count, some
don't; some shapes are expanded before the runtime even gets a
look. The form you write and the form the runtime evaluates
aren't always character-for-character the same." To
add 2 and 3, He composed the simple addition,
submitted the form, and the REPL — reading carefully — returned
the value of what the conventions had produced.

What Clojure form computes the result of adding 2 and 3? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 2 3)"}}]}
````

---

## chalkmark — G1-09: Symbols vs values

_pool_: `_CHALKMARK_SUBPLOTS`

**The metaphor:** The chalk mark scratched onto the bark vs the actual acorn it names. The mark is the *name*; the acorn is the *value*. `quote` labels a form so the runtime hands it back as-is instead of cooking it. Mirrors `'` / syntax-quote.

### Story-scaffold render

**form**: `(symbol? 'hare)`  •  **expected**: `True`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. This was near the road.

Mossback the tortoise scratched a chalk mark across a piece of bark — the name 'hare — and pointed first at the chalk mark, then at the actual bounding hare itself.

She wanted to show that the chalk mark and the bounding hare are different kinds of thing — and to ask the runtime which kind the chalk mark itself was.

Quoting (with the leading apostrophe) labels a name as a name — a symbol — rather than evaluating it. `symbol?` then asks the runtime: is this thing a chalk-mark-of-a-name?

To ask whether a quoted name is a symbol, using the symbol? predicate, He composed the symbol-predicate on a quoted name and submitted the form. The REPL — distinguishing label from value — returned:

the runtime confirmed: 'hare is indeed a symbol, a name and not the bounding thing the name might refer to. true came back.

Question: write a Clojure expression for whether a quoted name is a symbol.

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'hare)"}}]}
````

### Family-template render _(seed 56262718)_

**form**: `(symbol? 'hare)`  •  **expected**: `True`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. All this took place near the hilltop.

Mossback the tortoise scratched a chalk mark across a piece of bark — the name 'hare — and pointed first at the chalk mark, then at the actual bounding hare itself.

She wanted to show that the chalk mark and the bounding hare are different kinds of thing — and to ask the runtime which kind the chalk mark itself was.

Quoting (with the leading apostrophe) labels a name as a name — a symbol — rather than evaluating it. `symbol?` then asks the runtime: is this thing a chalk-mark-of-a-name?

To ask whether a quoted name is a symbol, using the symbol? predicate, She composed the symbol-predicate on a quoted name and submitted the form. The REPL — distinguishing label from value — returned:

the runtime confirmed: 'hare is indeed a symbol, a name and not the bounding thing the name might refer to. true came back.

Write a form whose evaluation gives whether a quoted name is a symbol.

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'hare)"}}]}
````

---

## tallywalk — G5-12: reduce — fold over a sequence

_pool_: `_TALLYWALK_SUBPLOTS`

**The metaphor:** Walking the row of pebbles one paw at a time, a slate in hand for the running tally. At each pebble, combine it into the tally; at the end, the tally is the answer. Mirrors `reduce` / `count` / fold.

### Story-scaffold render

**form**: `(reduce + [1 2 3 4])`  •  **expected**: `10`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. This was near the road.

A row of four small pebbles lay along the path — counts of 1, 2, 3, and 4 from four foraging trips.

Mossback the tortoise wanted the grand total of the four trips. Walking the row and carrying a running tally was the patient way.

`reduce` walks the collection from left to right carrying a tally. At each pebble, the combine function (here `+`) is applied to (tally, pebble), producing the new tally. The final tally is what comes back.

To walk the row of pebbles 1, 2, 3, 4 carrying a tally that combines each with + into the running total, He composed the fold operation and submitted the form. The REPL walked the row carrying the tally:

the walk produced a tally that grew across the four pebbles, ending at the grand total of all four trips.

Question: write a Clojure expression for the running tally after walking 1, 2, 3, 4 with + as the combine step.

---

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + [1 2 3 4])"}}]}
````

### Family-template render _(seed 28017048)_

**form**: `(reduce + [1 2 3 4])`  •  **expected**: `10`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

A row of four small pebbles lay along the path — counts of 1, 2, 3, and 4 from four foraging trips.

Mossback the tortoise wanted the grand total of the four trips. Walking the row and carrying a running tally was the patient way.

`reduce` walks the collection from left to right carrying a tally. At each pebble, the combine function (here `+`) is applied to (tally, pebble), producing the new tally. The final tally is what comes back.

To walk the row of pebbles 1, 2, 3, 4 carrying a tally that combines each with + into the running total, He composed the fold operation and submitted the form. The REPL walked the row carrying the tally:

the walk produced a tally that grew across the four pebbles, ending at the grand total of all four trips.

Write a Clojure expression that computes the running tally after walking 1, 2, 3, 4 with + as the combine step.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + [1 2 3 4])"}}]}
````

---

## beadstring — G2-11: str — string concatenation

_pool_: `_BEADSTRING_SUBPLOTS`

**The metaphor:** Strings as strings of beads, threaded in order. Concatenating splices threads together; substring cuts a counted run; counting beads gives the length. Mirrors `str` / `subs` / string operations.

### Story-scaffold render

**form**: `(str "ab" "cd")`  •  **expected**: `'abcd'`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. This was near the road.

Mossback the tortoise held two short threads of beads — one with the two letters "ab" wound on, the other with the two letters "cd". Two threads, four beads in all.

She wanted them spliced end to end into one longer thread, so the four-bead string could carry as a single name in her foraging-ledger.

`str` splices its arguments into one bead-string: each argument's beads thread one after another. With two short threads "ab" and "cd", the splice yields a single four-bead thread.

To use str to splice the two-letter strings "ab" and "cd" into a single thread, He composed the string concatenation and submitted the form. The REPL spliced or counted as the form said:

the spliced thread came back as a single four-letter string in order — ready to wear in the ledger.

Question: write a Clojure expression for the result of using str to splice "ab" and "cd".

---

{"tool_calls":[{"name":"eval","args":{"form":"(str \"ab\" \"cd\")"}}]}
````

### Family-template render _(seed 15807505)_

**form**: `(str "ab" "cd")`  •  **expected**: `'abcd'`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

Bramble the hare, with a smug grin, yanked at the bead-thread on the road
without bothering to count. Shelly the tortoise stopped her:
strings are precise — every bead in its place, every position
counted. To use str to splice the two-letter strings "ab" and "cd" into a single thread, she composed
the string concatenation, submitted the form, and the REPL — handling the
thread carefully — returned the right answer.

What Clojure form computes the result of using str to splice "ab" and "cd"? Submit it via `eval`.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(str \"ab\" \"cd\")"}}]}
````

---

## circuit — G5-22: recur — circuit without growing the trail

_pool_: `_CIRCUIT_SUBPLOTS`

**The metaphor:** Walking a circle around the meadow: each lap returns to the same starting point with a slightly different tally. No extra trail laid behind. Mirrors `recur` / `loop` — tail-call iteration.

### Story-scaffold render

**form**: `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`  •  **expected**: `120`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. This was near the road.

Mossback the tortoise wanted to compute 5! — the product 5 × 4 × 3 × 2 × 1 — without writing five separate multiplications.

She'd walk a small circuit around a stone, each lap multiplying her tally by the current step, until the step counter reached zero — then return the tally.

`loop`/`recur` is the circuit. `loop [n 5 acc 1]` starts the bindings; `recur` jumps back to the top with new bindings — `(dec n)` and `(* acc n)` — without growing the call-stack. The base case `(zero? n)` returns `acc`.

To walk a small circuit five times, multiplying a running tally by the current step each lap, until the step counter reaches zero, He composed a factorial computation via loop and recur and submitted the form. The REPL looped without growing the trail:

five laps later the step counter reached zero and the tally — 5! — came back.

Question: write a Clojure expression for the factorial of 5 computed by walking a circuit.

---

{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
````

### Family-template render _(seed 30121832)_

**form**: `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`  •  **expected**: `120`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

Shelly the tortoise walked a small circle around the meadow in the forest,
each lap returning to the same starting point with a slightly
different tally in hand. "Recur is this circuit," she
said: "back to the top with new bindings, no extra trail laid
down behind us." To walk a small circuit five times, multiplying a running tally by the current step each lap, until the step counter reaches zero, She composed
a factorial computation via loop and recur, submitted the form, and the REPL — looping
without growing the call-stack — returned the final value.

Write a Clojure expression that computes the factorial of 5 computed by walking a circuit.

---

{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
````

---

## goal — G12-08: clojure.test (tooling)

_pool_: `_GOAL_SUBPLOTS`

**The metaphor:** Tooling subjects (host platforms, build tools, library overviews, test framework, style guide) keep generic Hare/Tortoise narrative. Forcing a forest metaphor on `clojure.test` would be cargo-cult — the topic is *about* the ecosystem rather than a Clojure idiom.

### Generic render

**form**: `(= (+ 1 2) 3)`  •  **expected**: `True`

````text
It was well known among the animals that the Hare boasted of his speed at every chance. This was near the road.

Bramble the hare and Shelly the tortoise stopped along the road to settle a small
puzzle. Bramble wanted to test whether the sum of 1 and 2 equals 3 using equality. Bramble, as if the race were already won, declared
that she could write the form for it without thinking.
Shelly, untroubled by what others thought, suggested she actually write
the equality assertion at the heart of test checking carefully — and then let the REPL confirm what
the value really was.

Write a form whose evaluation gives the truth value showing the assertion passes.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(= (+ 1 2) 3)"}}]}
````

---

