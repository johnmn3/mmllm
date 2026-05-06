# Metaphor demo — tortoise-hare curriculum

One canonical subject per metaphor family, rendered **twice**
with different seeds so two templates from each family pool
are visible. Each entry includes a short annotation explaining
what the metaphor is mirroring in Clojure.

Coverage: 22 metaphor families + atoms + the goal-fallback
for abstract subjects. Across 216 subjects the split is:

- 8 atoms (form-display IS the lesson)
- 172 metaphor-rich (22 families)
- 36 abstract-by-nature (kept generic honestly)

---

## atom — G1-01: Eval as substitution

_pool_: `_SHARED_SUBPLOTS`

**The metaphor:** For atoms (literals), the form IS the answer. The user_msg deliberately shows the form (`{form_display}`); copy-from-prompt is the lesson — submit the literal as-is.

### Record A _(seed 4184714)_

**form**: `42`  •  **expected**: `42`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. All this took place along the road.

Halfway through the race, Bramble the hare stopped near the road and refused to
continue until someone could prove what the form `42`
evaluated to. Bramble called it impossible.
Slowpoke the tortoise, walking up at her usual pace, simply said: "Submit
the value 42 to the REPL. Whatever comes back is the answer."

Write a Clojure expression that computes the value of 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
````

### Record B _(seed 62937585)_

**form**: `42`  •  **expected**: `42`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened by the meadow.

Hopper the hare chalked a wager on a flat stone near the meadow: whoever
predicted the result of `42` would set the next race's
distance. Slowpoke the tortoise, stepping deliberately, said it would be simpler
to type the form into the REPL than to bicker about the value 42.

Question: write a Clojure expression for the value of 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
````

---

## pouch — G3-03: let — local binding

_pool_: `_POUCH_SUBPLOTS`

**The metaphor:** A small leather pouch tied at the Tortoise's hip. Whatever is tucked inside is held just for one stretch of road; by the next milestone the pouch is empty again. Mirrors `let`-binding scope: the binding lives only inside the form.

### Record A _(seed 78029526)_

**form**: `(let [x 3] (+ x 1))`  •  **expected**: `4`

````text
It was well known among the animals that the Hare boasted of his speed at every chance.

"There's a sign by the road that names one thing," Shelly the tortoise
said, patting the pouch at her hip, "but inside
this pouch I carry another. While I wear the pouch, the pouch
wins." Shelly described how to bind x to 3 and add 1 to it — the pouch's
binding overruling the road-sign's, but only for the pouch's
stretch of road. She composed the local binding and addition,
submitted it, and let the REPL show whose binding was in force
when the form ran.

Write a Clojure expression that computes adding 1 to x after binding x locally to 3 via let.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
````

### Record B _(seed 53335655)_

**form**: `(let [x 3] (+ x 1))`  •  **expected**: `4`

````text
It was well known among the animals that the Hare boasted of his speed at every chance. This was by the woods.

Whisker the hare brushed past the road-sign in the woods, as if the race were already won,
calling out guesses without bothering to peek into
Slowpoke the tortoise's pouch. But the pouch was where the answer
lived: He intended to bind x to 3 and add 1 to it, and the
value was tucked away for exactly that stretch. Slowpoke wrote
out the local binding and addition, submitted it, and the REPL — looking in
the pouch as the form told it to — handed back the value
Whisker had not even thought to check.

Write a Clojure expression that computes adding 1 to x after binding x locally to 3 via let.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
````

---

## recipe — G3-09: defn — named function

_pool_: `_RECIPE_SUBPLOTS`

**The metaphor:** A recipe-card posted on the road, naming a paw-step routine that any animal can follow. Mirrors `defn`: a named, reusable procedure with parameters — the next runner along the road picks up the card and follows it.

### Record A _(seed 4340300)_

**form**: `(do (defn dbl [x] (* x 2)) (dbl 5))`  •  **expected**: `10`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

"This is a recipe we want only once," Mossback the tortoise said,
declining to give the routine a card. To define a function dbl that doubles its argument, then call it with 5,
he composed the paw-steps inline — the procedure
unnamed, the ingredients listed in brackets at the head.
Mossback described the function definition and call as he wrote
it out, then submitted the form. The REPL followed the unnamed
recipe through to its last step and handed back the value, after
which the recipe was gone — exactly as Mossback had
intended.

Write a form whose evaluation gives the result of calling the function dbl, defined via defn to multiply its argument by 2, with 5.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn dbl [x] (* x 2)) (dbl 5))"}}]}
````

### Record B _(seed 19719980)_

**form**: `(do (defn dbl [x] (* x 2)) (dbl 5))`  •  **expected**: `10`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

"Here's a recipe with one ingredient already added,"
Slowpoke the tortoise said, holding up a card half-loaded. "When the
next animal calls it, they only have to bring the rest." To
define a function dbl that doubles its argument, then call it with 5, he composed the function definition and call that way
— some arguments fixed in advance, the others to be supplied at
the call site. Slowpoke the tortoise submitted the form, and the REPL
filled in what was missing and ran the recipe through to its
end.

Write a form whose evaluation gives the result of calling the function dbl, defined via defn to multiply its argument by 2, with 5.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn dbl [x] (* x 2)) (dbl 5))"}}]}
````

---

## basket — G4-08: assoc — pin a tag on the basket

_pool_: `_BASKET_SUBPLOTS`

**The metaphor:** A basket on the path: original sits untouched, you get a fresh one back. Mirrors immutable updates on collections — `assoc` doesn't mutate the original map; it returns a new one with the additional tag pinned on.

### Record A _(seed 97618792)_

**form**: `(assoc {:a 1} :b 2)`  •  **expected**: `{':a': 1, ':b': 2}`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

Mossback the tortoise pointed to a small basket on the path at the edge of the forest.
"Whatever I want to do with what's inside," he
said, "I read from the basket, work the change, and the basket
itself stays as it was — what I get back is a fresh arrangement."
To associate the key :b with value 2 onto a map binding :a to 1, He composed the assoc operation,
submitted the form, and let the REPL handle the basket exactly
as the operation prescribed.

Write a form whose evaluation gives the map after using assoc to add the key :b with value 2.

---

I use the appropriate access function on the collection.

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:a 1} :b 2)"}}]}
````

### Record B _(seed 65594300)_

**form**: `(assoc {:a 1} :b 2)`  •  **expected**: `{':a': 1, ':b': 2}`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. All this took place on the road.

"Watch carefully," Mossback the tortoise said, holding up the
original basket. "Whatever I do to it, this one sits unchanged
on the path — what I get back is a fresh basket with the change
made, leaving the first one exactly where it was." To
associate the key :b with value 2 onto a map binding :a to 1, He composed the assoc operation,
submitted the form, and the REPL returned a new arrangement
while the original waited, untouched. Hopper the hare, yawning at the soft moss,
was beginning to see why nothing could be lost by trying.

Write a Clojure expression that computes the map after using assoc to add the key :b with value 2.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:a 1} :b 2)"}}]}
````

---

## sieve — G5-10: map — pour through, transform each

_pool_: `_SIEVE_SUBPLOTS`

**The metaphor:** A sieve over an empty basket; the rule attached at its mouth decides what each pebble becomes. Mirrors `map`/`filter`/transducers — pour the basket through the sieve, and what lands below is the result.

### Record A _(seed 24825932)_

**form**: `(map inc [1 2 3])`  •  **expected**: `[2, 3, 4]`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Mossback the tortoise held up a sieve in the garden — a paw-step rule
attached at its mouth. "Whatever rule we hang on the sieve,"
he said, "the basket's pebbles pass through one
at a time: some are changed, some kept, some dropped, depending
on the rule." To apply inc to each element of the vector containing 1, 2, and 3, returning a sequence, He composed
mapping increment over a vector as the sieve's rule, poured the basket through,
submitted the form, and the REPL returned what the sieve had
let through.

What Clojure form computes the sequence produced by mapping inc over the vector containing 1, 2, and 3? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(map inc [1 2 3])"}}]}
````

### Record B _(seed 90194634)_

**form**: `(map inc [1 2 3])`  •  **expected**: `[2, 3, 4]`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

Mossback the tortoise balanced a sieve over an empty basket. "The
pebbles go in at the top," he said, "and the
sieve does its work — applying the rule, choosing or changing —
and what lands in the basket below is the result." To
apply inc to each element of the vector containing 1, 2, and 3, returning a sequence, He composed mapping increment over a vector,
poured the input through, submitted the form, and the REPL
collected what fell into the receiving basket.

Write a Clojure expression that computes the sequence produced by mapping inc over the vector containing 1, 2, and 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(map inc [1 2 3])"}}]}
````

---

## notebook — G9-03: atom — coordinated mutable state

_pool_: `_NOTEBOOK_SUBPLOTS`

**The metaphor:** A notebook open on a tree stump. Any animal can read; updates happen atomically; the bell on the corner rings on each change. Mirrors `atom`/`ref`/`swap!` — shared state with safe concurrent updates.

### Record A _(seed 97229946)_

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

````text
It was well known among the animals that the Hare boasted of his speed at every chance.

Mossback the tortoise gathered several notebooks together on the
stump — one for each runner in the race. "When I update them, I
want all the changes to land together, or none at all,"
he said. "That's a transaction." To construct an atom holding 0, atomically swap it by applying inc, and dereference the result,
He composed atom, swap, and deref inside a
coordinated block, submitted the form, and the REPL — committing
only when every notebook's change was ready — applied them as
one.

What Clojure form computes the value returned by dereferencing a after defining a as an atom holding 0 and swapping it via inc? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
````

### Record B _(seed 6886075)_

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

A notebook lay open on a tree stump in the middle of the meadow.
Any animal could walk up, read the page, or — carefully — update
it. "Atoms are like this notebook," Shelly the tortoise said. "You
can deref to read; you can swap! to write atomically, no matter
who else is watching." To construct an atom holding 0, atomically swap it by applying inc, and dereference the result, she composed
atom, swap, and deref, submitted the form, and let the REPL work the
notebook exactly as the form prescribed.

Write a Clojure expression that computes the value returned by dereferencing a after defining a as an atom holding 0 and swapping it via inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
````

---

## acorn — G2-04: min and max

_pool_: `_ACORN_SUBPLOTS`

**The metaphor:** Acorns sorted into heaps, counted, divided, combined. The number is just the count of acorns; the operation is what the Tortoise does with the heap. Mirrors arithmetic, comparisons, multi-arg operators.

### Record A _(seed 22438826)_

**form**: `(min 1 2 3)`  •  **expected**: `1`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

Shelly the tortoise divided a pile of acorns into smaller equal heaps
atop the hilltop, careful to count the leftovers. "Dividing in Clojure works
the same way," she said. "You can ask for the count
of full heaps, the leftover, or the heap-sized remainder." To
find the minimum of 1, 2, and 3, She composed the minimum of three numbers,
submitted the form, and the REPL handed back the right number from
the division.

Write a Clojure expression that computes the smallest of 1, 2, and 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(min 1 2 3)"}}]}
````

### Record B _(seed 61417980)_

**form**: `(min 1 2 3)`  •  **expected**: `1`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Mossback the tortoise laid acorns out on a flat stone in the meadow, sorting
them into small heaps. "Numbers in Clojure are just like acorns in
heaps," he said: "you can count them, you can add
two heaps together, you can divide one heap among several." To
find the minimum of 1, 2, and 3, He composed the minimum of three numbers,
submitted the form, and let the REPL hand back the count of
whatever the operation had produced.

Question: write a Clojure expression for the smallest of 1, 2, and 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(min 1 2 3)"}}]}
````

---

## gate — G2-13: and / or — short-circuit

_pool_: `_GATE_SUBPLOTS`

**The metaphor:** Gates on the trail that pass or stop the value. The first closed gate stops the chain; the value at that gate is what comes back. Mirrors short-circuit boolean logic — `and` / `or` / `not` / falsey rules.

### Record A _(seed 75743531)_

**form**: `(and true true)`  •  **expected**: `True`

````text
It was well known among the animals that the Hare boasted of his speed at every chance.

"Listen carefully," Shelly the tortoise said at the edge of the meadow. "Only two
things in Clojure close the gate: nil and false. Everything
else — zero, the empty string, an empty list — opens it. You
can't tell what's inside by guessing; you ask the gate." To
test true and true with the and operator, She composed the logical and,
submitted the form, and the REPL returned the value the gate
had passed through.

Question: write a Clojure expression for the result of using and on true and true.

---

{"tool_calls":[{"name":"eval","args":{"form":"(and true true)"}}]}
````

### Record B _(seed 99701652)_

**form**: `(and true true)`  •  **expected**: `True`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

A chain of small wooden gates stood across the trail near the meadow, each
swinging open or closed by the value the runner brought to it.
"Clojure's `and` is a chain of gates," Slowpoke the tortoise said.
"The first closed gate stops the chain; the value at that gate is
what comes back. If they're all open, the last value passes
through." To test true and true with the and operator, He composed
the logical and, submitted the form, and the REPL returned
whatever the gates had actually let through.

What Clojure form computes the result of using and on true and true? Submit it via `eval`.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(and true true)"}}]}
````

---

## fork — G5-04: cond — multi-arm crossroads

_pool_: `_FORK_SUBPLOTS`

**The metaphor:** A fork at a crossroads. Each arm is marked by a condition-stone; the runner walks past each and takes the first arm whose stone says true. Mirrors `if`/`cond`/`case`/`when`.

### Record A _(seed 42206130)_

**form**: `(cond (= 1 2) :a (= 1 1) :b :else :c)`  •  **expected**: `':b'`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. This was by the woods.

"Sometimes you only care about one arm," Shelly the tortoise said.
"When the condition is true, take the arm; when false, the runner
just stops where the fork was — no value, only nil." To
evaluate multiple conditions in sequence and return the value from the first true clause, She composed the multi-clause conditional,
submitted the form, and the REPL returned whatever the one-armed
fork had decided.

Question: write a Clojure expression for which clause of the cond fires.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(cond (= 1 2) :a (= 1 1) :b :else :c)"}}]}
````

### Record B _(seed 9436926)_

**form**: `(cond (= 1 2) :a (= 1 1) :b :else :c)`  •  **expected**: `':b'`

````text
It was well known among the animals that the Hare boasted of his speed at every chance.

A flat stone with several tokens carved into it lay by the woods.
"Case is a matching-stone," Shelly the tortoise said. "The runner
shows her token; the stone routes them to the
matching arm. No token, no match — unless a default is set."
To evaluate multiple conditions in sequence and return the value from the first true clause, She composed the multi-clause conditional,
submitted the form, and the REPL — matching by token — handed back
the right value.

What Clojure form computes which clause of the cond fires? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(cond (= 1 2) :a (= 1 1) :b :else :c)"}}]}
````

---

## roadsign — G6-03: require — borrowing a scroll

_pool_: `_ROADSIGN_SUBPLOTS`

**The metaphor:** Posted signs on the road; library of scrolls. A `def` is a sign by the road; a namespace is a scroll; `require` borrows the scroll, fully-qualified names point library-section-title.

### Record A _(seed 88017351)_

**form**: `(clojure.string/upper-case "hare")`  •  **expected**: `'HARE'`

````text
It was well known among the animals that the Hare boasted of his speed at every chance.

Mossback the tortoise drove a small wooden post at the edge of the woods and nailed a
fresh sign to it. "A def is a sign by the road," he
said. "Anyone passing reads the name, learns the value, and can
refer to it later by name alone." To call the uppercasing function from clojure.string on a test string,
He composed calling a fully-qualified string function, submitted the
form, and the REPL planted the sign — the name now bound to its
value for any later runner along the road.

Write a Clojure expression that computes the uppercase form of the string hare produced by clojure.string/upper-case.

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"hare\")"}}]}
````

### Record B _(seed 61484364)_

**form**: `(clojure.string/upper-case "hare")`  •  **expected**: `'HARE'`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. All this took place near the garden.

"You can paint over an old sign with new paint,"
Shelly the tortoise said, holding up a brush. "The post stays where
it is; the name is the same; only the value changes. The next
runner reads the new value and never sees the old." To
call the uppercasing function from clojure.string on a test string, She composed calling a fully-qualified string function,
submitted the form, and the REPL — having painted over the sign —
returned what the new paint now said.

What Clojure form computes the uppercase form of the string hare produced by clojure.string/upper-case? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"hare\")"}}]}
````

---

## safetynet — G7-02: try / catch

_pool_: `_SAFETYNET_SUBPLOTS`

**The metaphor:** A net stretched beneath a high jump. The runner can fall — the net catches them; the run continues, only the path bends. Mirrors error handling: `try`/`catch`, the practice-meadow REPL where stumbles cost nothing.

### Record A _(seed 15038521)_

**form**: `(try (/ 1 0) (catch Exception e -1))`  •  **expected**: `-1`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

Shelly the tortoise pointed at a small horn hung by the trailside.
"When something goes wrong, you blow the horn — and you can attach
a slip of paper to the horn-blast saying what went wrong, with
detail enough to inspect." To divide 1 by 0, catch the resulting ArithmeticException, return a numeric code, She
composed the handler for a division-by-zero error, submitted the form, and the REPL —
horn sounded, slip attached — handed back the value the alarm
chain had decided.

Write a Clojure expression that computes what the catch clause returns when ArithmeticException is caught.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 1 0) (catch Exception e -1))"}}]}
````

### Record B _(seed 85231292)_

**form**: `(try (/ 1 0) (catch Exception e -1))`  •  **expected**: `-1`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place at the edge of the garden.

"Before a real race," Slowpoke the tortoise said, "we check the
runner's fitness: are they ready to run? Are they carrying what
they should be? Pre and post conditions are exactly that — checks
that hold up the run if the runner isn't ready." To divide 1 by 0, catch the resulting ArithmeticException, return a numeric code,
He composed the handler for a division-by-zero error, submitted the
form, and the REPL — fitness checked — returned the value when the
checks held, or sounded the alarm when they didn't.

Question: write a Clojure expression for what the catch clause returns when ArithmeticException is caught.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 1 0) (catch Exception e -1))"}}]}
````

---

## scroll — G7-12: slurp / spit — IO

_pool_: `_SCROLL_SUBPLOTS`

**The metaphor:** Scrolls written and read. Marginalia (metadata) along the side. Drinking from / writing onto a scroll — `slurp`/`spit`. Reading line by line — `line-seq`. Open and roll up — `with-open`.

### Record A _(seed 29662188)_

**form**: `(count "hare\ntortoise\n")`  •  **expected**: `14`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Slowpoke the tortoise unrolled a long scroll by the orchard, dipping a quill
into ink at the edge. "The world outside the REPL is scrolls,"
he said: "you read what they say, you write what
you want to keep, and the runtime carries the words back and
forth." To count the characters in a multi-line string, He composed
the character count of a multi-line string, submitted the form, and the REPL handed back
what the scroll had said, or what the writing had committed.

Write a Clojure expression that computes how many characters are in the multi-line string.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"hare\\ntortoise\\n\")"}}]}
````

### Record B _(seed 94206278)_

**form**: `(count "hare\ntortoise\n")`  •  **expected**: `14`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. All this took place on the hilltop.

Down the side of the scroll, Shelly the tortoise pointed to small
notes in the margin. "Marginalia: notes about the scroll's
contents, not the contents themselves. Clojure metadata works the
same way — a small map of facts attached to a value, readable
when you ask for it." To count the characters in a multi-line string, She
composed the character count of a multi-line string, submitted the form, and the REPL —
peeking at the margins — handed back what the notes had said.

Write a Clojure expression that computes how many characters are in the multi-line string.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count \"hare\\ntortoise\\n\")"}}]}
````

---

## guild — G8-04: Protocol definition

_pool_: `_GUILD_SUBPLOTS`

**The metaphor:** A guild any species can join. The guild lists what its members must be able to do — the methods. Any animal that signs the ledger may claim membership. Mirrors `defprotocol` / `extend-protocol`.

### Record A _(seed 9789111)_

**form**: `(do (defprotocol Pace (speed [this])) (some? Pace))`  •  **expected**: `True`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Slowpoke the tortoise carved a small wooden sign at the edge of the garden: "Runners'
Guild — any species may join." "A protocol is a guild,"
he said. "It lists what every member must be able
to do — the methods. Any animal that can sign the book may claim
membership." To define a protocol named Pace with one method speed that takes a single argument this, He composed
a protocol definition, submitted the form, and the REPL — guild
founded — handed back the guild's record.

Write a Clojure expression that computes whether the protocol var Pace is truthy after defining a protocol named Pace with one method speed taking a single argument this.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (some? Pace))"}}]}
````

### Record B _(seed 15487904)_

**form**: `(do (defprotocol Pace (speed [this])) (some? Pace))`  •  **expected**: `True`

````text
It was well known among the animals that the Hare boasted of his speed at every chance.

"Today another animal signs the book," Shelly the tortoise said,
holding the guild ledger. "By signing, the species swears that any
of its members can perform the guild's methods — the same call,
species-specific behavior." To define a protocol named Pace with one method speed that takes a single argument this, She
composed a protocol definition, submitted the form, and the REPL —
finding the new signature in the book — dispatched correctly to
the new species' implementation.

Write a Clojure expression that computes whether the protocol var Pace is truthy after defining a protocol named Pace with one method speed taking a single argument this.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (some? Pace))"}}]}
````

---

## sortingtable — G8-08: defmulti — multimethod dispatch

_pool_: `_SORTINGTABLE_SUBPLOTS`

**The metaphor:** A sorting-table with arms branching off the sides. Runners walk up; the table reads what's stamped on each runner; the matching arm runs. Mirrors `defmulti`/`defmethod` — open-dispatch by any criterion.

### Record A _(seed 53082622)_

**form**: `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))`  •  **expected**: `':swift'`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. This was at the edge of the hilltop.

Pip the hare, puffed up with pride, leaped onto the sorting-table without
showing their stamp. Mossback the tortoise pointed at the
edge of the table: every runner must show the stamp the table
sorts by. To define a multimethod pace that dispatches on the :species key, add a method for :hare, then call pace with a map, he composed
calling a multimethod with a specific dispatch value, submitted the form, and the REPL — reading the
stamp first, dispatching second — returned the value from the
correct branch.

Write a Clojure expression that computes the value returned after defining multimethod pace that dispatches on :species, adding a method for :hare, then calling pace with a map.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))"}}]}
````

### Record B _(seed 78308397)_

**form**: `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))`  •  **expected**: `':swift'`

````text
It was well known among the animals that the Hare boasted of his speed at every chance.

"There's the sorting-table, and there's the runners' guild,"
Mossback the tortoise said. "Both route by what the runner is, but
the sorting-table is open to any criterion you like, while the
guild is open to any species that signs the book." To
define a multimethod pace that dispatches on the :species key, add a method for :hare, then call pace with a map, He composed calling a multimethod with a specific dispatch value,
submitted the form, and the REPL — using whichever was right
for the goal — returned the value cleanly.

Write a form whose evaluation gives the value returned after defining multimethod pace that dispatches on :species, adding a method for :hare, then calling pace with a map.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))"}}]}
````

---

## carryingcase — G8-03: defrecord — labeled compartments

_pool_: `_CARRYINGCASE_SUBPLOTS`

**The metaphor:** A small wooden case with named compartments. The stamp on the outside says what kind of case; the labels on the inside say what each compartment holds. Mirrors `deftype` / `defrecord`.

### Record A _(seed 46150031)_

**form**: `(do (defrecord Runner [name pace]) (:pace (->Runner "Alice" :slow)))`  •  **expected**: `':slow'`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Shelly the tortoise held up a small wooden case on the hilltop, its inside
divided into labeled compartments. "Defrecord makes a case like
this," she said: "named compartments holding
specific things; a stamp on the outside saying what kind of case
it is." To define a record type named Runner with two fields, then retrieve one field from an instance, She composed
reading the pace field from a Runner record, submitted the form, and the REPL — constructing
the case, filling its compartments — returned the value the case
held or carried.

What Clojure form computes the pace field value after defining a record Runner with two fields name and pace, then creating an instance and reading the pace field? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defrecord Runner [name pace]) (:pace (->Runner \"Alice\" :slow)))"}}]}
````

### Record B _(seed 68570251)_

**form**: `(do (defrecord Runner [name pace]) (:pace (->Runner "Alice" :slow)))`  •  **expected**: `':slow'`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

Mossback the tortoise held up a small wooden case in the forest, its inside
divided into labeled compartments. "Defrecord makes a case like
this," he said: "named compartments holding
specific things; a stamp on the outside saying what kind of case
it is." To define a record type named Runner with two fields, then retrieve one field from an instance, He composed
reading the pace field from a Runner record, submitted the form, and the REPL — constructing
the case, filling its compartments — returned the value the case
held or carried.

Write a form whose evaluation gives the pace field value after defining a record Runner with two fields name and pace, then creating an instance and reading the pace field.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defrecord Runner [name pace]) (:pace (->Runner \"Alice\" :slow)))"}}]}
````

---

## toolshed — G11-02: Method call — borrowing a host tool

_pool_: `_TOOLSHED_SUBPLOTS`

**The metaphor:** A different toolshed of foreign tools, none carved by the Tortoise. Each tool has a label; calling it uses dot-prefix for instance, slash for static. Mirrors host interop — `.method`, `Class/static`, `(new …)`, type hints.

### Record A _(seed 27444416)_

**form**: `(.toUpperCase "abc")`  •  **expected**: `'ABC'`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened by the orchard.

"Sometimes the toolshed needs to know what kind of tool you mean,"
Mossback the tortoise said, marking a small tag onto the form.
"Type-hints save the runtime from having to guess; the host can
go straight to the right method." To call the host method toUpperCase on the string abc,
He composed the host method toUpperCase with the right
hint, submitted the form, and the REPL — taking the host's
fast path — returned the value cleanly.

What Clojure form computes the uppercase form of the string abc produced by the host method toUpperCase via dot-prefix syntax? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
````

### Record B _(seed 63890653)_

**form**: `(.toUpperCase "abc")`  •  **expected**: `'ABC'`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. It happened by the meadow.

"Sometimes the toolshed needs to know what kind of tool you mean,"
Mossback the tortoise said, marking a small tag onto the form.
"Type-hints save the runtime from having to guess; the host can
go straight to the right method." To call the host method toUpperCase on the string abc,
He composed the host method toUpperCase with the right
hint, submitted the form, and the REPL — taking the host's
fast path — returned the value cleanly.

What Clojure form computes the uppercase form of the string abc produced by the host method toUpperCase via dot-prefix syntax? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
````

---

## runnerahead — G9-13: future — runner sent ahead

_pool_: `_RUNNERAHEAD_SUBPLOTS`

**The metaphor:** A messenger sent down the road while the Tortoise carries on. Later, the Tortoise asks the runner to hand back the result. Mirrors `future` / `agent` / `promise` / `await`.

### Record A _(seed 32022335)_

**form**: `@(future (+ 1 2))`  •  **expected**: `3`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. All this took place at the edge of the orchard.

"You can send a message ahead to the runner," Shelly the tortoise
said, "and the runner applies it to whatever they're carrying.
The message reaches them; their carry is updated." To
construct a future that adds 1 and 2, and dereference it, She composed future, add, deref,
submitted the form, and the REPL — delivering the message,
updating the runner's carry — returned what the runner now
held.

Write a Clojure expression that computes the value returned by dereferencing a future that adds 1 and 2.

---

{"tool_calls":[{"name":"eval","args":{"form":"@(future (+ 1 2))"}}]}
````

### Record B _(seed 20107900)_

**form**: `@(future (+ 1 2))`  •  **expected**: `3`

````text
It was well known among the animals that the Hare boasted of his speed at every chance.

"You can send a message ahead to the runner," Mossback the tortoise
said, "and the runner applies it to whatever they're carrying.
The message reaches them; their carry is updated." To
construct a future that adds 1 and 2, and dereference it, He composed future, add, deref,
submitted the form, and the REPL — delivering the message,
updating the runner's carry — returned what the runner now
held.

What Clojure form computes the value returned by dereferencing a future that adds 1 and 2? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"@(future (+ 1 2))"}}]}
````

---

## rewriterule — G10-03: defmacro — rule that rewrites the recipe

_pool_: `_REWRITERULE_SUBPLOTS`

**The metaphor:** A scribe with the power to rewrite the recipe before the runtime ever cooks it. The rule pays off when many recipes need the same rewriting. Mirrors `defmacro` / `macroexpand` / `eval`.

### Record A _(seed 37377577)_

**form**: `` (do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3)) ``  •  **expected**: `3`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

"Most of the time, you don't need a rule that rewrites,"
Shelly the tortoise said. "A function suffices: it takes its
arguments, runs its body, returns its value. Macros are for when
you need to shape the *form* itself — not the value." To
define a macro named my-when that takes a test and body expressions, then invoke it, She composed defining a conditional macro and invoking it —
choosing macro or function as the goal demanded — submitted the
form, and the REPL returned the value either way.

What Clojure form computes the value returned when my-when expands to an if-do block that runs the body with test true? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

### Record B _(seed 3075222)_

**form**: `` (do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3)) ``  •  **expected**: `3`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

"When the rule introduces a name of its own," Slowpoke the tortoise
said, "you don't want it to collide with names the runner is
using. So we use a one-off scratch-name — gensym — guaranteed
unique." To define a macro named my-when that takes a test and body expressions, then invoke it, He composed
defining a conditional macro and invoking it with the scratch-name woven in, submitted the
form, and the REPL — running the hygienic rewrite — returned the
value cleanly.

What Clojure form computes the value returned when my-when expands to an if-do block that runs the body with test true? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

---

## scribe — G1-12: Parens group — fence-posts

_pool_: `_SCRIBE_SUBPLOTS`

**The metaphor:** The scribe's reading conventions. Comments are marginalia skipped by the eye. Whitespace is the breath between words. Parens are fence-posts marking which things go together. `do` is a sequence in one breath. Reader macros are shorthand.

### Record A _(seed 20555794)_

**form**: `(+ 2 3)`  •  **expected**: `5`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. All this took place at the edge of the garden.

Shelly the tortoise pointed at a small note jotted along the side of
the scroll. "When the reader reaches a comment, the eye moves
past it — the runtime never sees it at all." To add 2 and 3,
She composed the simple addition with the
side-notes ignored exactly as the runtime ignores them, submitted
the form, and the REPL returned the value the form alone
produced.

What Clojure form computes the result of adding 2 and 3? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 2 3)"}}]}
````

### Record B _(seed 77491960)_

**form**: `(+ 2 3)`  •  **expected**: `5`

````text
It was well known among the animals that the Hare boasted of his speed at every chance.

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

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 2 3)"}}]}
````

---

## chalkmark — G1-09: Symbols vs values

_pool_: `_CHALKMARK_SUBPLOTS`

**The metaphor:** The chalk mark scratched onto the bark vs the actual acorn it names. The mark is the *name*; the acorn is the *value*. `quote` labels a form so the runtime hands it back as-is instead of cooking it. Mirrors `'` / syntax-quote.

### Record A _(seed 63668447)_

**form**: `(symbol? 'hare)`  •  **expected**: `True`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. All this took place near the hilltop.

Bramble the hare, puffed up with pride, mistook the name on the bark for the
acorn it pointed to. "It says hare, so the value must be the
hare!" Slowpoke the tortoise only shook his head: the
mark and the acorn are never the same thing. To ask whether a quoted name is a symbol, using the symbol? predicate,
he composed the symbol-predicate on a quoted name, submitted the form,
and the REPL — keeping mark and acorn distinct — returned the
right answer for the goal.

Write a Clojure expression that computes whether a quoted name is a symbol.

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'hare)"}}]}
````

### Record B _(seed 84639566)_

**form**: `(symbol? 'hare)`  •  **expected**: `True`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

"To talk about the form itself rather than evaluating it,"
Mossback the tortoise said, "you label the form with a chalk mark
in front. Quoting tells the runtime: don't cook this, just hand
it back as the shape it is." To ask whether a quoted name is a symbol, using the symbol? predicate, He
composed the symbol-predicate on a quoted name, submitted the form, and the REPL —
respecting the chalk mark — returned the form unevaluated.

Write a form whose evaluation gives whether a quoted name is a symbol.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'hare)"}}]}
````

---

## tallywalk — G5-12: reduce — fold over a sequence

_pool_: `_TALLYWALK_SUBPLOTS`

**The metaphor:** Walking the row of pebbles one paw at a time, a slate in hand for the running tally. At each pebble, combine it into the tally; at the end, the tally is the answer. Mirrors `reduce` / `count` / fold.

### Record A _(seed 4220380)_

**form**: `(reduce + [1 2 3 4])`  •  **expected**: `10`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. It happened at the edge of the forest.

"You don't have to start the tally at zero," Shelly the tortoise
said, holding up a slate already inscribed with a number. "If you
start with a different value, the walk begins from there — the
combine-step folds each pebble in from that starting point." To
fold + over the vector containing 1, 2, 3, and 4, summing them, She composed the fold operation,
submitted the form, and the REPL — starting from the given tally,
walking the row — returned the final value.

Write a form whose evaluation gives the sum produced by reducing + over the vector containing 1, 2, 3, and 4.

---

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + [1 2 3 4])"}}]}
````

### Record B _(seed 86270535)_

**form**: `(reduce + [1 2 3 4])`  •  **expected**: `10`

````text
It was well known among the animals that the Hare boasted of his speed at every chance. This was near the garden.

"The simplest tally-walk is just counting,"
Shelly the tortoise said: "step along the row, add one at every
pebble, no other operation. The runtime does this for any
collection — vector, list, map, string." To fold + over the vector containing 1, 2, 3, and 4, summing them,
She composed the fold operation, submitted the
form, and the REPL — walking the row, counting the steps —
returned the count.

What Clojure form computes the sum produced by reducing + over the vector containing 1, 2, 3, and 4? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + [1 2 3 4])"}}]}
````

---

## beadstring — G2-11: str — string concatenation

_pool_: `_BEADSTRING_SUBPLOTS`

**The metaphor:** Strings as strings of beads, threaded in order. Concatenating splices threads together; substring cuts a counted run; counting beads gives the length. Mirrors `str` / `subs` / string operations.

### Record A _(seed 85032438)_

**form**: `(str "ab" "cd")`  •  **expected**: `'abcd'`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened by the garden.

Hopper the hare, as if the race were already won, yanked at the bead-thread near the garden
without bothering to count. Mossback the tortoise stopped him:
strings are precise — every bead in its place, every position
counted. To use str to join the two-letter strings "ab" and "cd", he composed
the string concatenation, submitted the form, and the REPL — handling the
thread carefully — returned the right answer.

Write a Clojure expression that computes the result of using str to join "ab" and "cd".

---

{"tool_calls":[{"name":"eval","args":{"form":"(str \"ab\" \"cd\")"}}]}
````

### Record B _(seed 28023612)_

**form**: `(str "ab" "cd")`  •  **expected**: `'abcd'`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. All this took place near the orchard.

"To count the beads, walk the thread,"
Mossback the tortoise said. "Want a section of beads? Cut from one
position to another and you get a smaller thread, the original
untouched." To use str to join the two-letter strings "ab" and "cd", He composed
the string concatenation, submitted the form, and the REPL — counting or
cutting — returned the answer the bead-thread had given up.

Question: write a Clojure expression for the result of using str to join "ab" and "cd".

---

{"tool_calls":[{"name":"eval","args":{"form":"(str \"ab\" \"cd\")"}}]}
````

---

## circuit — G5-22: recur — circuit without growing the trail

_pool_: `_CIRCUIT_SUBPLOTS`

**The metaphor:** Walking a circle around the meadow: each lap returns to the same starting point with a slightly different tally. No extra trail laid behind. Mirrors `recur` / `loop` — tail-call iteration.

### Record A _(seed 63639708)_

**form**: `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`  •  **expected**: `120`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Mossback the tortoise walked a small circle around the meadow at the edge of the hilltop,
each lap returning to the same starting point with a slightly
different tally in hand. "Recur is this circuit," he
said: "back to the top with new bindings, no extra trail laid
down behind us." To compute the factorial of 5 using a loop and tail recursion, He composed
a factorial computation via loop and recur, submitted the form, and the REPL — looping
without growing the call-stack — returned the final value.

Write a form whose evaluation gives 5! computed via loop/recur.

---

{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
````

### Record B _(seed 37596392)_

**form**: `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`  •  **expected**: `120`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Mossback the tortoise walked a small circle around the meadow near the hilltop,
each lap returning to the same starting point with a slightly
different tally in hand. "Recur is this circuit," he
said: "back to the top with new bindings, no extra trail laid
down behind us." To compute the factorial of 5 using a loop and tail recursion, He composed
a factorial computation via loop and recur, submitted the form, and the REPL — looping
without growing the call-stack — returned the final value.

Write a form whose evaluation gives 5! computed via loop/recur.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
````

---

## goal — G12-08: clojure.test (tooling)

_pool_: `_GOAL_SUBPLOTS`

**The metaphor:** Tooling subjects (host platforms, build tools, library overviews, test framework, style guide) keep generic Hare/Tortoise narrative. Forcing a forest metaphor on `clojure.test` would be cargo-cult — the topic is *about* the ecosystem rather than a Clojure idiom.

### Record A _(seed 63819760)_

**form**: `(= (+ 1 2) 3)`  •  **expected**: `True`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

The wager was set on the hilltop: produce the value before the breeze had
turned the next leaf. Whisker the hare bolted into a flurry of
guesses, calling out numbers and second-guessing himself
about whether the goal was to test whether the sum of 1 and 2 equals 3 using equality or something close to it.
Mossback the tortoise, who had simply walked to the slate and begun to
write the equality assertion at the heart of test checking, finished the form, submitted it, and read
the value off the REPL while Whisker was still arguing with the
breeze. The race, like every other, went to the steady hand.

Write a Clojure expression that computes the truth value showing the assertion passes.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(= (+ 1 2) 3)"}}]}
````

### Record B _(seed 10102326)_

**form**: `(= (+ 1 2) 3)`  •  **expected**: `True`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

The wager was set near the hilltop: produce the value before the breeze had
turned the next leaf. Hopper the hare bolted into a flurry of
guesses, calling out numbers and second-guessing himself
about whether the goal was to test whether the sum of 1 and 2 equals 3 using equality or something close to it.
Mossback the tortoise, who had simply walked to the slate and begun to
write the equality assertion at the heart of test checking, finished the form, submitted it, and read
the value off the REPL while Hopper was still arguing with the
breeze. The race, like every other, went to the steady hand.

What Clojure form computes the truth value showing the assertion passes? Submit it via `eval`.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(= (+ 1 2) 3)"}}]}
````

---

