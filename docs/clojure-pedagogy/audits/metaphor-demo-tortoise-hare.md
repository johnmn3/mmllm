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

### Record A _(seed 18292201)_

**form**: `42`  •  **expected**: `42`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

Hopper the hare chalked a wager on a flat stone in the forest: whoever
predicted the result of `42` would set the next race's
distance. Slowpoke the tortoise, without complaint, said it would be simpler
to type the form into the REPL than to bicker about the value 42.

What Clojure form computes the value of 42? Submit it via `eval`.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
````

### Record B _(seed 90036841)_

**form**: `42`  •  **expected**: `42`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Mossback the tortoise had been trying to teach Bramble the hare how the REPL
works. "Look here," he said, pointing to
the value 42. "You hand the form `42` to the runtime, and
the runtime hands you back what it evaluates to." Bramble, with legs heavy from sprinting,
agreed to try.

Write a Clojure expression that computes the value of 42.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
````

---

## pouch — G3-03: let — local binding

_pool_: `_POUCH_SUBPLOTS`

**The metaphor:** A small leather pouch tied at the Tortoise's hip. Whatever is tucked inside is held just for one stretch of road; by the next milestone the pouch is empty again. Mirrors `let`-binding scope: the binding lives only inside the form.

### Record A _(seed 888635)_

**form**: `(let [x 3] (+ x 1))`  •  **expected**: `4`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. It happened atop the hilltop.

"Watch the pouch carefully," Shelly the tortoise said near the hilltop.
"While the form's stretch of road runs, the pouch is full and
the binding is yours." To bind x to 3 and add 1 to it, She
composed the local binding and addition with the binding tucked safely inside,
then submitted the form. The REPL returned the value, and the
pouch — its work done — was empty again. Pip the hare, with legs heavy from sprinting,
finally admitted that the patient pouch-walk had carried the
day.

Write a form whose evaluation gives adding 1 to x after binding x locally to 3 via let.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
````

### Record B _(seed 65169382)_

**form**: `(let [x 3] (+ x 1))`  •  **expected**: `4`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Slowpoke the tortoise reached for the small leather pouch tied at
his hip. "When I want to bind x to 3 and add 1 to it," he
said, "I tuck the value into the pouch and carry it just for the
stretch of road where I need it. By the next milestone the pouch
is empty again." He composed the local binding and addition,
the binding tucked away inside, and submitted the form to the
REPL. Hopper the hare, as if the race were already won, had already forgotten what was
in the pouch — but the form, which still carried it, came back
with the answer.

What Clojure form computes adding 1 to x after binding x locally to 3 via let? Submit it via `eval`.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
````

---

## recipe — G3-09: defn — named function

_pool_: `_RECIPE_SUBPLOTS`

**The metaphor:** A recipe-card posted on the road, naming a paw-step routine that any animal can follow. Mirrors `defn`: a named, reusable procedure with parameters — the next runner along the road picks up the card and follows it.

### Record A _(seed 33179888)_

**form**: `(do (defn dbl [x] (* x 2)) (dbl 5))`  •  **expected**: `10`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

Pip the hare, as if the race were already won, insisted they could just
shout the answer rather than bother writing a recipe.
Slowpoke the tortoise only smiled and reached for a fresh card. To
define a function dbl that doubles its argument, then call it with 5, he composed the function definition and call,
submitted the form, and the REPL — running the recipe paw-step
by paw-step — handed back the value Pip had been guessing
at.

Write a Clojure expression that computes the result of calling the function dbl, defined via defn to multiply its argument by 2, with 5.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn dbl [x] (* x 2)) (dbl 5))"}}]}
````

### Record B _(seed 9994032)_

**form**: `(do (defn dbl [x] (* x 2)) (dbl 5))`  •  **expected**: `10`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

Mossback the tortoise kept a small stack of recipe-cards by the road,
each one a paw-step routine. "Recipes in Clojure are like these
cards," he said: "the ingredients go at the head,
the steps in order, and the last step is what gets served." To
define a function dbl that doubles its argument, then call it with 5, He wrote out the function definition and call on
a fresh card, submitted the form, and the REPL followed the
recipe and handed back the value the last step had produced.

What Clojure form computes the result of calling the function dbl, defined via defn to multiply its argument by 2, with 5? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn dbl [x] (* x 2)) (dbl 5))"}}]}
````

---

## basket — G4-08: assoc — pin a tag on the basket

_pool_: `_BASKET_SUBPLOTS`

**The metaphor:** A basket on the path: original sits untouched, you get a fresh one back. Mirrors immutable updates on collections — `assoc` doesn't mutate the original map; it returns a new one with the additional tag pinned on.

### Record A _(seed 52897455)_

**form**: `(assoc {:a 1} :b 2)`  •  **expected**: `{':a': 1, ':b': 2}`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Shelly the tortoise pointed to a small basket on the path atop the hilltop.
"Whatever I want to do with what's inside," she
said, "I read from the basket, work the change, and the basket
itself stays as it was — what I get back is a fresh arrangement."
To associate the key :b with value 2 onto a map binding :a to 1, She composed the assoc operation,
submitted the form, and let the REPL handle the basket exactly
as the operation prescribed.

Question: write a Clojure expression for the map after using assoc to add the key :b with value 2.

---

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:a 1} :b 2)"}}]}
````

### Record B _(seed 13755973)_

**form**: `(assoc {:a 1} :b 2)`  •  **expected**: `{':a': 1, ':b': 2}`

````text
It was well known among the animals that the Hare boasted of his speed at every chance.

A line of animals had formed near the road, each one taking the next
animal's tail in its paw — head at the front, the rest trailing
behind. "Many of our baskets are like this procession,"
Mossback the tortoise said. "You can grab the head, you can ask for
the tail, you can put a new animal at the front of the line."
To associate the key :b with value 2 onto a map binding :a to 1, he composed the assoc operation,
submitted the form, and the REPL marched the procession exactly
as the form described.

Question: write a Clojure expression for the map after using assoc to add the key :b with value 2.

---

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:a 1} :b 2)"}}]}
````

---

## sieve — G5-10: map — pour through, transform each

_pool_: `_SIEVE_SUBPLOTS`

**The metaphor:** A sieve over an empty basket; the rule attached at its mouth decides what each pebble becomes. Mirrors `map`/`filter`/transducers — pour the basket through the sieve, and what lands below is the result.

### Record A _(seed 86726173)_

**form**: `(map inc [1 2 3])`  •  **expected**: `[2, 3, 4]`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place by the woods.

Mossback the tortoise stacked two sieves one above the other, the
output of the first feeding into the second. "What lands at the
bottom," he said, "has been through both rules in
order — applied as a single combined sieve." To apply inc to each element of the vector containing 1, 2, and 3, returning a sequence,
He composed mapping increment over a vector as a stack of
sieves, poured the input through, submitted the form, and the
REPL caught what the stack let through.

Write a form whose evaluation gives the sequence produced by mapping inc over the vector containing 1, 2, and 3.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(map inc [1 2 3])"}}]}
````

### Record B _(seed 46202357)_

**form**: `(map inc [1 2 3])`  •  **expected**: `[2, 3, 4]`

````text
It was well known among the animals that the Hare boasted of his speed at every chance.

Whisker the hare eyed the basket, puffed up with pride, and called out a
guess about what would come out the other side of the sieve
without bothering to actually pour. Mossback the tortoise shook
his head and went on with the work: to
apply inc to each element of the vector containing 1, 2, and 3, returning a sequence, he composed mapping increment over a vector as
the sieve's rule, poured the input through carefully,
submitted the form, and the REPL returned the only answer
that would do — the one the sieve had actually produced.

Write a Clojure expression that computes the sequence produced by mapping inc over the vector containing 1, 2, and 3.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(map inc [1 2 3])"}}]}
````

---

## notebook — G9-03: atom — coordinated mutable state

_pool_: `_NOTEBOOK_SUBPLOTS`

**The metaphor:** A notebook open on a tree stump. Any animal can read; updates happen atomically; the bell on the corner rings on each change. Mirrors `atom`/`ref`/`swap!` — shared state with safe concurrent updates.

### Record A _(seed 13295164)_

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

A notebook lay open on a tree stump in the middle of the meadow.
Any animal could walk up, read the page, or — carefully — update
it. "Atoms are like this notebook," Slowpoke the tortoise said. "You
can deref to read; you can swap! to write atomically, no matter
who else is watching." To construct an atom holding 0, atomically swap it by applying inc, and dereference the result, he composed
atom, swap, and deref, submitted the form, and let the REPL work the
notebook exactly as the form prescribed.

Write a Clojure expression that computes the value returned by dereferencing a after defining a as an atom holding 0 and swapping it via inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
````

### Record B _(seed 41319561)_

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. All this took place in the orchard.

"The notebook stays put on the stump," Mossback the tortoise said,
"so any animal who comes by can read what's on the page right
now. The page changes only when someone writes — and only as the
runtime allows." To construct an atom holding 0, atomically swap it by applying inc, and dereference the result, He composed
atom, swap, and deref, submitted the form, and the REPL — reading
or writing the notebook as the form prescribed — handed back the
value the page had carried.

What Clojure form computes the value returned by dereferencing a after defining a as an atom holding 0 and swapping it via inc? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
````

---

## acorn — G2-04: min and max

_pool_: `_ACORN_SUBPLOTS`

**The metaphor:** Acorns sorted into heaps, counted, divided, combined. The number is just the count of acorns; the operation is what the Tortoise does with the heap. Mirrors arithmetic, comparisons, multi-arg operators.

### Record A _(seed 92632328)_

**form**: `(min 1 2 3)`  •  **expected**: `1`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

Mossback the tortoise laid acorns out on a flat stone at the edge of the orchard, sorting
them into small heaps. "Numbers in Clojure are just like acorns in
heaps," he said: "you can count them, you can add
two heaps together, you can divide one heap among several." To
find the minimum of 1, 2, and 3, He composed the minimum of three numbers,
submitted the form, and let the REPL hand back the count of
whatever the operation had produced.

What Clojure form computes the smallest of 1, 2, and 3? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(min 1 2 3)"}}]}
````

### Record B _(seed 49927199)_

**form**: `(min 1 2 3)`  •  **expected**: `1`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Shelly the tortoise arranged a small heap of acorns by the woods,
careful with the count. "Numbers in Clojure don't fudge,"
she said. "Whatever you do — adding, subtracting,
dividing into heaps with leftovers, comparing two piles — the
runtime gets it exactly right, every time." To find the minimum of 1, 2, and 3,
She composed the minimum of three numbers, submitted the
form, and the REPL handed back the precise number the operation
called for.

What Clojure form computes the smallest of 1, 2, and 3? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(min 1 2 3)"}}]}
````

---

## gate — G2-13: and / or — short-circuit

_pool_: `_GATE_SUBPLOTS`

**The metaphor:** Gates on the trail that pass or stop the value. The first closed gate stops the chain; the value at that gate is what comes back. Mirrors short-circuit boolean logic — `and` / `or` / `not` / falsey rules.

### Record A _(seed 90155415)_

**form**: `(and true true)`  •  **expected**: `True`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

"Only two things in Clojure close the gate," Mossback the tortoise
said: "nil and false. Everything else — zero, the empty string,
an empty list — opens it. The gate's verdict follows that rule
exactly." To test true and true with the and operator, He composed
the logical and, submitted the form, and the REPL returned the
value the gate had passed, true or false.

Write a form whose evaluation gives the result of using and on true and true.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(and true true)"}}]}
````

### Record B _(seed 96739842)_

**form**: `(and true true)`  •  **expected**: `True`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

"You can't tell which way the gate will swing by guessing,"
Slowpoke the tortoise said. "You bring the value to the gate, the
runtime checks it, and the gate gives the only answer that
matters." To test true and true with the and operator, He composed
the logical and, submitted the form, and the REPL settled the
matter — the gate had swung exactly as the rule said.

What Clojure form computes the result of using and on true and true? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(and true true)"}}]}
````

---

## fork — G5-04: cond — multi-arm crossroads

_pool_: `_FORK_SUBPLOTS`

**The metaphor:** A fork at a crossroads. Each arm is marked by a condition-stone; the runner walks past each and takes the first arm whose stone says true. Mirrors `if`/`cond`/`case`/`when`.

### Record A _(seed 79194221)_

**form**: `(cond (= 1 2) :a (= 1 1) :b :else :c)`  •  **expected**: `':b'`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

"What's important about a fork," Shelly the tortoise said, "is
that the arm not taken doesn't run at all. The runtime checks
the condition, walks the right arm, and the unrun arm is just
left behind." To evaluate multiple conditions in sequence and return the value from the first true clause, She composed
the multi-clause conditional, submitted the form, and the REPL — running
only what was needed — handed back the value of the chosen
arm.

Question: write a Clojure expression for which clause of the cond fires.

---

{"tool_calls":[{"name":"eval","args":{"form":"(cond (= 1 2) :a (= 1 1) :b :else :c)"}}]}
````

### Record B _(seed 57466888)_

**form**: `(cond (= 1 2) :a (= 1 1) :b :else :c)`  •  **expected**: `':b'`

````text
It was well known among the animals that the Hare boasted of his speed at every chance.

"It isn't the runner who picks the arm," Slowpoke the tortoise said,
"it's the condition. Whatever the condition evaluates to, that
decides." To evaluate multiple conditions in sequence and return the value from the first true clause, He composed
the multi-clause conditional, submitted the form, and the REPL — letting the
condition decide — handed back the value of the arm the
condition had pointed at.

What Clojure form computes which clause of the cond fires? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(cond (= 1 2) :a (= 1 1) :b :else :c)"}}]}
````

---

## roadsign — G6-03: require — borrowing a scroll

_pool_: `_ROADSIGN_SUBPLOTS`

**The metaphor:** Posted signs on the road; library of scrolls. A `def` is a sign by the road; a namespace is a scroll; `require` borrows the scroll, fully-qualified names point library-section-title.

### Record A _(seed 12367368)_

**form**: `(clojure.string/upper-case "hare")`  •  **expected**: `'HARE'`

````text
It was well known among the animals that the Hare boasted of his speed at every chance. It happened in the meadow.

A small wooden library stood at the edge of the meadow, its shelves stocked with
scrolls — each scroll holding the signs for one stretch of road.
"Names live on scrolls," Slowpoke the tortoise said: "to use a sign
from a scroll, you make sure the scroll is on the shelf where the
runtime can find it." To call the uppercasing function from clojure.string on a test string, He
composed calling a fully-qualified string function, submitted the form, and the REPL —
finding the right sign on the right scroll — returned the value
the form had asked for.

Question: write a Clojure expression for the uppercase form of the string hare produced by clojure.string/upper-case.

---

I require the namespace and call the function.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"hare\")"}}]}
````

### Record B _(seed 32838944)_

**form**: `(clojure.string/upper-case "hare")`  •  **expected**: `'HARE'`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. All this took place at the edge of the meadow.

Hopper the hare, with great whoops of laughter, glanced at the sign by the meadow and
called out what he thought it said without slowing.
Mossback the tortoise stopped and read carefully. To call the uppercasing function from clojure.string on a test string, the
sign had to be read exactly: he composed
calling a fully-qualified string function, submitted the form, and the REPL — reading
literally — returned the right value, while Hopper's guess fell
short.

Write a form whose evaluation gives the uppercase form of the string hare produced by clojure.string/upper-case.

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"hare\")"}}]}
````

---

## safetynet — G7-02: try / catch

_pool_: `_SAFETYNET_SUBPLOTS`

**The metaphor:** A net stretched beneath a high jump. The runner can fall — the net catches them; the run continues, only the path bends. Mirrors error handling: `try`/`catch`, the practice-meadow REPL where stumbles cost nothing.

### Record A _(seed 18435215)_

**form**: `(try (/ 1 0) (catch Exception e -1))`  •  **expected**: `-1`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. All this took place by the garden.

Shelly the tortoise stretched a small net beneath a high jump
by the garden. "If the runner falls, the net catches them; the run
doesn't end, only the path bends." To divide 1 by 0, catch the resulting ArithmeticException, return a numeric code,
She composed the handler for a division-by-zero error, submitted the
form, and the REPL — net in place — caught the trouble and
returned the value the catch-arm had specified, the run continuing
the patient way.

Write a form whose evaluation gives what the catch clause returns when ArithmeticException is caught.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 1 0) (catch Exception e -1))"}}]}
````

### Record B _(seed 78087795)_

**form**: `(try (/ 1 0) (catch Exception e -1))`  •  **expected**: `-1`

````text
It was well known among the animals that the Hare boasted of his speed at every chance.

Mossback the tortoise stretched a small net beneath a high jump
near the orchard. "If the runner falls, the net catches them; the run
doesn't end, only the path bends." To divide 1 by 0, catch the resulting ArithmeticException, return a numeric code,
He composed the handler for a division-by-zero error, submitted the
form, and the REPL — net in place — caught the trouble and
returned the value the catch-arm had specified, the run continuing
the patient way.

Question: write a Clojure expression for what the catch clause returns when ArithmeticException is caught.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 1 0) (catch Exception e -1))"}}]}
````

---

## scroll — G7-12: slurp / spit — IO

_pool_: `_SCROLL_SUBPLOTS`

**The metaphor:** Scrolls written and read. Marginalia (metadata) along the side. Drinking from / writing onto a scroll — `slurp`/`spit`. Reading line by line — `line-seq`. Open and roll up — `with-open`.

### Record A _(seed 92757339)_

**form**: `(count "hare\ntortoise\n")`  •  **expected**: `14`

````text
It was well known among the animals that the Hare boasted of his speed at every chance. All this took place near the hilltop.

Whisker the hare, with a smug grin, claimed the scroll said exactly what
he expected and didn't bother to actually read.
Mossback the tortoise unrolled it carefully. To count the characters in a multi-line string required
the scroll's actual contents — he composed
the character count of a multi-line string, submitted the form, and the REPL — reading the
scroll faithfully — returned the value the parchment had
held.

Write a form whose evaluation gives how many characters are in the multi-line string.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"hare\\ntortoise\\n\")"}}]}
````

### Record B _(seed 21075757)_

**form**: `(count "hare\ntortoise\n")`  •  **expected**: `14`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

"Reading and writing scrolls is just like reading and writing
forms," Slowpoke the tortoise said. "You ask the runtime for what's
on the parchment, you write what you want recorded, and the work
goes both ways through one quill." To count the characters in a multi-line string,
He composed the character count of a multi-line string, submitted the
form, and the REPL handed back what the scroll had said — or
what the writing had committed.

Question: write a Clojure expression for how many characters are in the multi-line string.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count \"hare\\ntortoise\\n\")"}}]}
````

---

## guild — G8-04: Protocol definition

_pool_: `_GUILD_SUBPLOTS`

**The metaphor:** A guild any species can join. The guild lists what its members must be able to do — the methods. Any animal that signs the ledger may claim membership. Mirrors `defprotocol` / `extend-protocol`.

### Record A _(seed 63577878)_

**form**: `(do (defprotocol Pace (speed [this])) (some? Pace))`  •  **expected**: `True`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Slowpoke the tortoise carved a small wooden sign near the meadow: "Runners'
Guild — any species may join." "A protocol is a guild,"
he said. "It lists what every member must be able
to do — the methods. Any animal that can sign the book may claim
membership." To define a protocol named Pace with one method speed that takes a single argument this, He composed
a protocol definition, submitted the form, and the REPL — guild
founded — handed back the guild's record.

Write a Clojure expression that computes whether the protocol var Pace is truthy after defining a protocol named Pace with one method speed taking a single argument this.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (some? Pace))"}}]}
````

### Record B _(seed 34109032)_

**form**: `(do (defprotocol Pace (speed [this])) (some? Pace))`  •  **expected**: `True`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. All this took place near the woods.

Hopper the hare, with great whoops of laughter, declared that he could of
course do whatever the guild's call demanded — even though the
species had never signed the book. Mossback the tortoise only smiled
and asked for the actual implementation. To define a protocol named Pace with one method speed that takes a single argument this,
he composed a protocol definition, submitted the form,
and the REPL — checking the book first — returned the right answer
based on who had actually signed.

Write a Clojure expression that computes whether the protocol var Pace is truthy after defining a protocol named Pace with one method speed taking a single argument this.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (some? Pace))"}}]}
````

---

## sortingtable — G8-08: defmulti — multimethod dispatch

_pool_: `_SORTINGTABLE_SUBPLOTS`

**The metaphor:** A sorting-table with arms branching off the sides. Runners walk up; the table reads what's stamped on each runner; the matching arm runs. Mirrors `defmulti`/`defmethod` — open-dispatch by any criterion.

### Record A _(seed 17895662)_

**form**: `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))`  •  **expected**: `':swift'`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. This was at the edge of the meadow.

"What the table sorts by is up to you," Shelly the tortoise said.
"You decide what to look at on each runner — a tag, a kind, a
field, anything. The runtime reads it, finds the matching arm,
and runs that one." To define a multimethod pace that dispatches on the :species key, add a method for :hare, then call pace with a map, She
composed calling a multimethod with a specific dispatch value, submitted the form, and the REPL —
reading the stamp the dispatch function produced — returned the
value the right arm had given.

Question: write a Clojure expression for the value returned after defining multimethod pace that dispatches on :species, adding a method for :hare, then calling pace with a map.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))"}}]}
````

### Record B _(seed 87266701)_

**form**: `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))`  •  **expected**: `':swift'`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. All this took place on the hilltop.

"To add a branch to the sorting-table," Mossback the tortoise said,
"you say what stamp the branch handles and what behavior runs
when a runner with that stamp arrives." To define a multimethod pace that dispatches on the :species key, add a method for :hare, then call pace with a map,
He composed calling a multimethod with a specific dispatch value for the right
branch, submitted the form, and the REPL — adding the branch,
dispatching the runner — returned the branch-specific value.

Write a form whose evaluation gives the value returned after defining multimethod pace that dispatches on :species, adding a method for :hare, then calling pace with a map.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))"}}]}
````

---

## carryingcase — G8-03: defrecord — labeled compartments

_pool_: `_CARRYINGCASE_SUBPLOTS`

**The metaphor:** A small wooden case with named compartments. The stamp on the outside says what kind of case; the labels on the inside say what each compartment holds. Mirrors `deftype` / `defrecord`.

### Record A _(seed 69794072)_

**form**: `(do (defrecord Runner [name pace]) (:pace (->Runner "Alice" :slow)))`  •  **expected**: `':slow'`

````text
It was well known among the animals that the Hare boasted of his speed at every chance.

Mossback the tortoise held up a small wooden case at the edge of the forest, its inside
divided into labeled compartments. "Defrecord makes a case like
this," he said: "named compartments holding
specific things; a stamp on the outside saying what kind of case
it is." To define a record type named Runner with two fields, then retrieve one field from an instance, He composed
reading the pace field from a Runner record, submitted the form, and the REPL — constructing
the case, filling its compartments — returned the value the case
held or carried.

What Clojure form computes the pace field value after defining a record Runner with two fields name and pace, then creating an instance and reading the pace field? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defrecord Runner [name pace]) (:pace (->Runner \"Alice\" :slow)))"}}]}
````

### Record B _(seed 34110903)_

**form**: `(do (defrecord Runner [name pace]) (:pace (->Runner "Alice" :slow)))`  •  **expected**: `':slow'`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. It happened in the meadow.

"To reach into a labeled compartment," Mossback the tortoise said,
"you ask for it by name. The case knows where each compartment
is; the runtime fetches it cleanly." To define a record type named Runner with two fields, then retrieve one field from an instance,
He composed reading the pace field from a Runner record, submitted the
form, and the REPL — opening the right compartment — returned
exactly what was inside.

Question: write a Clojure expression for the pace field value after defining a record Runner with two fields name and pace, then creating an instance and reading the pace field.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defrecord Runner [name pace]) (:pace (->Runner \"Alice\" :slow)))"}}]}
````

---

## toolshed — G11-02: Method call — borrowing a host tool

_pool_: `_TOOLSHED_SUBPLOTS`

**The metaphor:** A different toolshed of foreign tools, none carved by the Tortoise. Each tool has a label; calling it uses dot-prefix for instance, slash for static. Mirrors host interop — `.method`, `Class/static`, `(new …)`, type hints.

### Record A _(seed 92276244)_

**form**: `(.toUpperCase "abc")`  •  **expected**: `'ABC'`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. All this took place on the road.

"There's the meadow's own toolshed," Shelly the tortoise said,
"and there's the foreign one. The runtime moves a value across
the boundary, calls the foreign tool, and brings the result back
into the meadow." To call the host method toUpperCase on the string abc, She composed
the host method toUpperCase, submitted the form, and the REPL — bridging
the two toolsheds — returned the value cleanly.

Question: write a Clojure expression for the uppercase form of the string abc produced by the host method toUpperCase via dot-prefix syntax.

---

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
````

### Record B _(seed 12457461)_

**form**: `(.toUpperCase "abc")`  •  **expected**: `'ABC'`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

"Foreign tools work, but they need careful handling,"
Slowpoke the tortoise said. "Their labels are different, their
calling conventions are different, and the runtime has to bridge
between Clojure and the host every time." To call the host method toUpperCase on the string abc,
He composed the host method toUpperCase, submitted the
form, and the REPL — making the bridge cleanly — handed back the
value the foreign tool had produced.

What Clojure form computes the uppercase form of the string abc produced by the host method toUpperCase via dot-prefix syntax? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
````

---

## runnerahead — G9-13: future — runner sent ahead

_pool_: `_RUNNERAHEAD_SUBPLOTS`

**The metaphor:** A messenger sent down the road while the Tortoise carries on. Later, the Tortoise asks the runner to hand back the result. Mirrors `future` / `agent` / `promise` / `await`.

### Record A _(seed 38920704)_

**form**: `@(future (+ 1 2))`  •  **expected**: `3`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. This was in the garden.

"The hard part isn't sending the runner," Slowpoke the tortoise said.
"The hard part is being patient enough to wait for the answer
when it comes — not snatching too early, not giving up too soon.
The runtime makes that easier than it sounds." To construct a future that adds 1 and 2, and dereference it,
He composed future, add, deref, submitted the
form, and the REPL — coordinating the wait properly — returned
the runner's answer when the runner had it ready.

What Clojure form computes the value returned by dereferencing a future that adds 1 and 2? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"@(future (+ 1 2))"}}]}
````

### Record B _(seed 74060815)_

**form**: `@(future (+ 1 2))`  •  **expected**: `3`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

Mossback the tortoise arranged a small relay near the road, runners and
messengers each in their place. "The runtime keeps track of who
sent what and when each one finishes," he said,
"so the values come back in the right order, no matter how long
each runner takes." To construct a future that adds 1 and 2, and dereference it, He
composed future, add, deref, submitted the form, and the REPL —
coordinating the relay — returned the right value at the right
time.

Question: write a Clojure expression for the value returned by dereferencing a future that adds 1 and 2.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"@(future (+ 1 2))"}}]}
````

---

## rewriterule — G10-03: defmacro — rule that rewrites the recipe

_pool_: `_REWRITERULE_SUBPLOTS`

**The metaphor:** A scribe with the power to rewrite the recipe before the runtime ever cooks it. The rule pays off when many recipes need the same rewriting. Mirrors `defmacro` / `macroexpand` / `eval`.

### Record A _(seed 44775824)_

**form**: `` (do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3)) ``  •  **expected**: `3`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

"Here's the difference between a rule and a recipe,"
Mossback the tortoise said. "A recipe takes ingredients and makes a
dish. A rule takes a *form* and makes a different *form* — only
then does the runtime get to evaluate it." To define a macro named my-when that takes a test and body expressions, then invoke it,
He composed defining a conditional macro and invoking it, submitted the
form, and the REPL — applying the rule to the form first, then
evaluating — handed back the value the rewritten form had
produced.

Write a Clojure expression that computes the value returned when my-when expands to an if-do block that runs the body with test true.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

### Record B _(seed 60533359)_

**form**: `` (do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3)) ``  •  **expected**: `3`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. It happened at the edge of the orchard.

Bramble the hare, with great whoops of laughter, insisted that the rule was unnecessary
— she could write the rewritten recipe directly.
Slowpoke the tortoise only smiled: a hand-rewritten recipe is fine
once, but the rule pays off when many recipes need rewriting the
same way. To define a macro named my-when that takes a test and body expressions, then invoke it, he composed
defining a conditional macro and invoking it, submitted the form, and the REPL — running the
rule the rule's way — returned the value the rewritten recipe
yielded.

Question: write a Clojure expression for the value returned when my-when expands to an if-do block that runs the body with test true.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

---

## scribe — G1-12: Parens group — fence-posts

_pool_: `_SCRIBE_SUBPLOTS`

**The metaphor:** The scribe's reading conventions. Comments are marginalia skipped by the eye. Whitespace is the breath between words. Parens are fence-posts marking which things go together. `do` is a sequence in one breath. Reader macros are shorthand.

### Record A _(seed 94701405)_

**form**: `(+ 2 3)`  •  **expected**: `5`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Bramble the hare, boasting at every turn, glanced at the form and called out
what she thought it would do without paying attention to
the conventions of how it was written. Mossback the tortoise only
shook his head — the runtime reads the form
exactly. To add 2 and 3, he composed
the simple addition, submitted the form, and the REPL — reading
literally — returned the right value, while Bramble's guess fell
short.

Write a Clojure expression that computes the result of adding 2 and 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 2 3)"}}]}
````

### Record B _(seed 70839667)_

**form**: `(+ 2 3)`  •  **expected**: `5`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. It happened in the forest.

"A form is what's actually there on the page," Mossback the tortoise
said, "after the conventions of writing and reading have done
their work. The runtime sees the cleaned-up form, evaluates it,
and gives back what it computes." To add 2 and 3,
He composed the simple addition, submitted the
form, and the REPL — taking the form exactly as it was — handed
back the value.

Write a form whose evaluation gives the result of adding 2 and 3.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 2 3)"}}]}
````

---

## chalkmark — G1-09: Symbols vs values

_pool_: `_CHALKMARK_SUBPLOTS`

**The metaphor:** The chalk mark scratched onto the bark vs the actual acorn it names. The mark is the *name*; the acorn is the *value*. `quote` labels a form so the runtime hands it back as-is instead of cooking it. Mirrors `'` / syntax-quote.

### Record A _(seed 95498852)_

**form**: `(symbol? 'hare)`  •  **expected**: `True`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Whisker the hare, boasting at every turn, mistook the name on the bark for the
acorn it pointed to. "It says hare, so the value must be the
hare!" Shelly the tortoise only shook her head: the
mark and the acorn are never the same thing. To ask whether a quoted name is a symbol, using the symbol? predicate,
she composed the symbol-predicate on a quoted name, submitted the form,
and the REPL — keeping mark and acorn distinct — returned the
right answer for the goal.

Write a form whose evaluation gives whether a quoted name is a symbol.

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'hare)"}}]}
````

### Record B _(seed 25591429)_

**form**: `(symbol? 'hare)`  •  **expected**: `True`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

"To talk about the form itself rather than evaluating it,"
Shelly the tortoise said, "you label the form with a chalk mark
in front. Quoting tells the runtime: don't cook this, just hand
it back as the shape it is." To ask whether a quoted name is a symbol, using the symbol? predicate, She
composed the symbol-predicate on a quoted name, submitted the form, and the REPL —
respecting the chalk mark — returned the form unevaluated.

Write a Clojure expression that computes whether a quoted name is a symbol.

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'hare)"}}]}
````

---

## tallywalk — G5-12: reduce — fold over a sequence

_pool_: `_TALLYWALK_SUBPLOTS`

**The metaphor:** Walking the row of pebbles one paw at a time, a slate in hand for the running tally. At each pebble, combine it into the tally; at the end, the tally is the answer. Mirrors `reduce` / `count` / fold.

### Record A _(seed 84939804)_

**form**: `(reduce + [1 2 3 4])`  •  **expected**: `10`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

"The simplest tally-walk is just counting,"
Shelly the tortoise said: "step along the row, add one at every
pebble, no other operation. The runtime does this for any
collection — vector, list, map, string." To fold + over the vector containing 1, 2, 3, and 4, summing them,
She composed the fold operation, submitted the
form, and the REPL — walking the row, counting the steps —
returned the count.

Write a Clojure expression that computes the sum produced by reducing + over the vector containing 1, 2, 3, and 4.

---

I write the higher-order form so the REPL can compute.

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + [1 2 3 4])"}}]}
````

### Record B _(seed 95841351)_

**form**: `(reduce + [1 2 3 4])`  •  **expected**: `10`

````text
It was well known among the animals that the Hare boasted of his speed at every chance. All this took place near the forest.

Shelly the tortoise walked the row of pebbles at the edge of the forest, one paw at a
time, a small slate in hand for the running tally. "Reduce is
this walk," she said: "at each pebble, you combine
it into the tally; at the end, the tally is your answer." To
fold + over the vector containing 1, 2, 3, and 4, summing them, She composed the fold operation,
submitted the form, and the REPL — walking the row, carrying the
tally — returned the final number.

What Clojure form computes the sum produced by reducing + over the vector containing 1, 2, 3, and 4? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + [1 2 3 4])"}}]}
````

---

## beadstring — G2-11: str — string concatenation

_pool_: `_BEADSTRING_SUBPLOTS`

**The metaphor:** Strings as strings of beads, threaded in order. Concatenating splices threads together; substring cuts a counted run; counting beads gives the length. Mirrors `str` / `subs` / string operations.

### Record A _(seed 54587182)_

**form**: `(str "ab" "cd")`  •  **expected**: `'abcd'`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. This was in the garden.

Shelly the tortoise held up a string of small wooden beads near the garden.
"Strings in Clojure are like this," she said: "a
threaded line of characters, in order. Concat strings together,
and the threads are spliced; cut a substring out, and you get a
shorter thread." To use str to join the two-letter strings "ab" and "cd", She composed
the string concatenation, submitted the form, and the REPL — splicing or
cutting as the form said — returned the new bead-string.

Write a Clojure expression that computes the result of using str to join "ab" and "cd".

---

{"tool_calls":[{"name":"eval","args":{"form":"(str \"ab\" \"cd\")"}}]}
````

### Record B _(seed 58176305)_

**form**: `(str "ab" "cd")`  •  **expected**: `'abcd'`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

Hopper the hare, boasting at every turn, yanked at the bead-thread near the garden
without bothering to count. Shelly the tortoise stopped him:
strings are precise — every bead in its place, every position
counted. To use str to join the two-letter strings "ab" and "cd", she composed
the string concatenation, submitted the form, and the REPL — handling the
thread carefully — returned the right answer.

Write a Clojure expression that computes the result of using str to join "ab" and "cd".

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(str \"ab\" \"cd\")"}}]}
````

---

## circuit — G5-22: recur — circuit without growing the trail

_pool_: `_CIRCUIT_SUBPLOTS`

**The metaphor:** Walking a circle around the meadow: each lap returns to the same starting point with a slightly different tally. No extra trail laid behind. Mirrors `recur` / `loop` — tail-call iteration.

### Record A _(seed 49643070)_

**form**: `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`  •  **expected**: `120`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. It happened at the edge of the orchard.

Shelly the tortoise walked a small circle around the meadow near the orchard,
each lap returning to the same starting point with a slightly
different tally in hand. "Recur is this circuit," she
said: "back to the top with new bindings, no extra trail laid
down behind us." To compute the factorial of 5 using a loop and tail recursion, She composed
a factorial computation via loop and recur, submitted the form, and the REPL — looping
without growing the call-stack — returned the final value.

What Clojure form computes 5! computed via loop/recur? Submit it via `eval`.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
````

### Record B _(seed 95484508)_

**form**: `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`  •  **expected**: `120`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

"Every circuit has a stopping condition," Shelly the tortoise
said. "Without one, the runner walks forever. With one, the
runner knows when the laps are done and the tally is the
answer." To compute the factorial of 5 using a loop and tail recursion, She composed
a factorial computation via loop and recur, submitted the form, and the REPL — looping
until the base case — returned the value the final lap
produced.

Question: write a Clojure expression for 5! computed via loop/recur.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
````

---

## goal — G12-08: clojure.test (tooling)

_pool_: `_GOAL_SUBPLOTS`

**The metaphor:** Tooling subjects (host platforms, build tools, library overviews, test framework, style guide) keep generic Hare/Tortoise narrative. Forcing a forest metaphor on `clojure.test` would be cargo-cult — the topic is *about* the ecosystem rather than a Clojure idiom.

### Record A _(seed 51897388)_

**form**: `(= (+ 1 2) 3)`  •  **expected**: `True`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

A wooden sign nailed to a tree at the edge of the orchard carried a small puzzle. The
challenge was simple: test whether the sum of 1 and 2 equals 3 using equality. Hopper laughed, swaggering through the underbrush, and
declared it too easy. Slowpoke said patiently that the only way
to be sure of the equality assertion at the heart of test checking was to write the form and put it
in the REPL — not to guess at the value from the goal alone.

What Clojure form computes the truth value showing the assertion passes? Submit it via `eval`.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(= (+ 1 2) 3)"}}]}
````

### Record B _(seed 49666726)_

**form**: `(= (+ 1 2) 3)`  •  **expected**: `True`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. It happened in the forest.

Whisker the hare and Shelly the tortoise stopped by the forest to settle a small
puzzle. Whisker wanted to test whether the sum of 1 and 2 equals 3 using equality. Whisker, boasting at every turn, declared
that he could write the form for it without thinking.
Shelly, saying very little, suggested he actually write
the equality assertion at the heart of test checking carefully — and then let the REPL confirm what
the value really was.

What Clojure form computes the truth value showing the assertion passes? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(= (+ 1 2) 3)"}}]}
````

---

