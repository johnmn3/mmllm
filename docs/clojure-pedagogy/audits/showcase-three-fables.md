# Curriculum showcase: three fables, K-12

Same Clojure subject, three fable lenses. Each row picks a
representative subject from the K-12 framework; columns show
the same subject taught through tortoise-hare, goose-eggs,
and ant-grasshopper. The model sees this kind of variation at
scale — for any one subject, ~222 narrative variants per
fable × 3 fables landed = ~666 distinct surface forms of the
same Clojure concept.

---

## G1-01 — Eval as substitution

_L1 atom: a value evaluates to itself_

### Tortoise and the Hare  _(lens: vanity vs. steadiness)_

**form**: `42`  •  **expected**: `42`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Slowpoke the tortoise had been trying to teach Hopper the hare how the REPL
works. "Look here," he said, pointing to
the value 42. "You hand the form `42` to the runtime, and
the runtime hands you back what it evaluates to." Hopper, with legs heavy from sprinting,
agreed to try.

Write a Clojure expression that computes the value of 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
````

### Goose and the Golden Eggs  _(lens: greed vs. patience)_

**form**: `42`  •  **expected**: `42`

````text
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A small audience of neighbors had gathered deep inside the cellar to watch
Emily attempt to outguess Bob at reading the
REPL. Bob pointed to the value 42 and read out the form
aloud: `42`. The crowd waited to see who would correctly
write the form to submit; Plume the goose watched too, untroubled by
the noise.

Question: write a Clojure expression for the value of 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
````

### Ant and the Grasshopper  _(lens: prudence vs. idleness)_

**form**: `42`  •  **expected**: `42`

````text
It is the way of the Ant to gather, and the way of the Grasshopper to play.

A small audience of meadow creatures had gathered at the edge of the garden to watch
Chirp the grasshopper attempt to outwit Toc the ant at reading the
REPL. Toc pointed to the value 42 and read the form aloud:
`42`. The crowd waited to see who would correctly write the
form to submit.

Write a Clojure expression that computes the value of 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
````

---

## G1-13 — First arithmetic call

_L2 application: (+ 1 2)_

### Tortoise and the Hare  _(lens: vanity vs. steadiness)_

**form**: `(+ 1 2)`  •  **expected**: `3`

````text
It was well known among the animals that the Hare boasted of his speed at every chance.

Slowpoke the tortoise had been keeping a small leather notebook of every
form he had successfully evaluated. Today near the road, the
next entry was the form (+ 1 2). Pip the hare peered over
his shoulder at the form `(+ 1 2)` and asked what
it would come out to.

Question: write a Clojure expression for the result of (+ 1 2).

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
````

### Goose and the Golden Eggs  _(lens: greed vs. patience)_

**form**: `(+ 1 2)`  •  **expected**: `3`

````text
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Diana offered a small basket of eggs as a wager in the cellar:
whoever guessed the result of `(+ 1 2)` first would keep them.
George, stepping deliberately, said it would be simpler to type the
form into the REPL than to bicker about the form (+ 1 2); the eggs,
after all, would still be there once Honk the goose laid the next
one.

Question: write a Clojure expression for the result of (+ 1 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
````

### Ant and the Grasshopper  _(lens: prudence vs. idleness)_

**form**: `(+ 1 2)`  •  **expected**: `3`

````text
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Beside a small stockpile at the edge of the orchard, Hum the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(+ 1 2)`
first would win the right to set the next day's count.
Bit the ant, without complaint, said it was simpler to type the form into
the REPL than to argue about the form (+ 1 2).

Question: write a Clojure expression for the result of (+ 1 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
````

---

## G2-13 — and/or short-circuit

_L1+L2: short-circuit logic returns values_

### Tortoise and the Hare  _(lens: vanity vs. steadiness)_

**form**: `(and true true)`  •  **expected**: `True`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place at the edge of the woods.

"There is no need to evaluate that," Hopper the hare said, boasting at every turn.
"Anyone can see what the form (and true true) comes to." Slowpoke the tortoise, who
by the woods had grown used to such claims, asked him to actually
write the form `(and true true)` and submit it to the REPL — just to be
sure.

Write a form whose evaluation gives the value of (and true true).

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(and true true)"}}]}
````

### Goose and the Golden Eggs  _(lens: greed vs. patience)_

**form**: `(and true true)`  •  **expected**: `True`

````text
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"Whatever `(and true true)` comes to," Beatrice declared,
boasting at every turn, on the farm, "I'll wager a basket of eggs I know it without
typing it." David, untroubled by what others thought, picked up a piece of chalk
and drew the form (and true true) on the side of the egg-crate. "Then write
the form," he said. "The REPL will have the last word, the
way Quill the goose has the last word on the morning's count."

Write a Clojure expression that computes the value of (and true true).

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(and true true)"}}]}
````

### Ant and the Grasshopper  _(lens: prudence vs. idleness)_

**form**: `(and 1 2 3)`  •  **expected**: `3`

````text
Two creatures of the meadow approached the coming winter very differently. It happened in the woods.

A wooden sign nailed to a stalk in the woods carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(and 1 2 3)`. Skip
laughed, puffed up with pride, and declared it too easy. Bit said patiently
that the only way to be sure of the form (and 1 2 3) was to put it in the
REPL.

Question: write a Clojure expression for the last truthy value of and.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(and 1 2 3)"}}]}
````

---

## G3-03 — let local binding

_L3 naming: scope and substitution_

### Tortoise and the Hare  _(lens: vanity vs. steadiness)_

**form**: `(let [x 3] (+ x 1))`  •  **expected**: `4`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Halfway through the race, Hopper the hare stopped in the orchard and refused to
continue until someone could prove what the form `(let [x 3] (+ x 1))`
evaluated to. Hopper called it impossible.
Mossback the tortoise, walking up at her usual pace, simply said: "Submit
the form (let [x 3] (+ x 1)) to the REPL. Whatever comes back is the answer."

Write a form whose evaluation gives the result of (let [x 3] (+ x 1)).

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
````

### Goose and the Golden Eggs  _(lens: greed vs. patience)_

**form**: `(let [x 3] (+ x 1))`  •  **expected**: `4`

````text
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

David kept a small leather ledger inside the kitchen where every
quantity that mattered got its own name, the same way each egg from
Plume the goose got its own tally mark in the column beside it.
He pointed to today's entry: the form (let [x 3] (+ x 1)). The
form `(let [x 3] (+ x 1))` would settle it once Frank agreed to
look at the binding rather than guess at the answer.

Question: write a Clojure expression for the result of (let [x 3] (+ x 1)).

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
````

### Ant and the Grasshopper  _(lens: prudence vs. idleness)_

**form**: `(let [x 3] (+ x 1))`  •  **expected**: `4`

````text
Two creatures of the meadow approached the coming winter very differently.

"You can call it whatever you like," Tic said by the orchard, "but the
form is what matters." He drew the binding for
Chirp the grasshopper: the form `(let [x 3] (+ x 1))` captured the form (let [x 3] (+ x 1)), and
the REPL would do the rest.

Write a form whose evaluation gives the result of (let [x 3] (+ x 1)).

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
````

---

## G4-08 — assoc — map update

_L4 collections: immutable map ops_

### Tortoise and the Hare  _(lens: vanity vs. steadiness)_

**form**: `(assoc {:a 1} :b 2)`  •  **expected**: `{':a': 1, ':b': 2}`

````text
It was well known among the animals that the Hare boasted of his speed at every chance.

Hopper the hare and Mossback the tortoise stopped at the edge of the garden where someone had
written the form (assoc {:a 1} :b 2) on a flat stone. Hopper, as if the race were already won, declared
that he could see the answer at a glance. Mossback,
without complaint, suggested they actually evaluate the form `(assoc {:a 1} :b 2)`
in the REPL and read off whatever it returned.

What Clojure form computes the map after assoc'ing :b 2? Submit it via `eval`.

---

I write the collection literal and let the REPL evaluate.

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:a 1} :b 2)"}}]}
````

### Goose and the Golden Eggs  _(lens: greed vs. patience)_

**form**: `(assoc {:a 1} :b 2)`  •  **expected**: `{':a': 1, ':b': 2}`

````text
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Bob had been laying out a small collection in the market —
eggs from the morning, coins from the market, tallies from the barn,
whatever the day produced. Bob wrote `(assoc {:a 1} :b 2)` on a slate
and asked George to write the form into the REPL so they
could confirm it together, the way Plume the goose settled each
morning's count by laying one more egg.

Write a Clojure expression that computes the map after assoc'ing :b 2.

---

I use the appropriate access function on the collection.

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:a 1} :b 2)"}}]}
````

### Ant and the Grasshopper  _(lens: prudence vs. idleness)_

**form**: `(assoc {:a 1} :b 2)`  •  **expected**: `{':a': 1, ':b': 2}`

````text
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Toc the ant had been trying to teach Hum the grasshopper how the REPL
works. "Look here," she said, pointing to the form (assoc {:a 1} :b 2).
"You hand the form `(assoc {:a 1} :b 2)` to the runtime, and the runtime hands
you back what it evaluates to." Hum, drowsy from the warm sun, agreed to
try.

Question: write a Clojure expression for the map after assoc'ing :b 2.

---

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:a 1} :b 2)"}}]}
````

---

## G5-12 — reduce

_L5 higher-order: fold over a sequence_

### Tortoise and the Hare  _(lens: vanity vs. steadiness)_

**form**: `(reduce + [1 2 3 4])`  •  **expected**: `10`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place in the garden.

A small audience of forest creatures had gathered in the garden to watch
Whisker the hare attempt to outwit Mossback the tortoise at reading the REPL.
Mossback pointed to the form (reduce + [1 2 3 4]) and read out the form aloud:
`(reduce + [1 2 3 4])`. The crowd waited to see who would correctly write
the form to submit.

Write a Clojure expression that computes the sum.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + [1 2 3 4])"}}]}
````

### Goose and the Golden Eggs  _(lens: greed vs. patience)_

**form**: `(reduce + [1 2 3 4])`  •  **expected**: `10`

````text
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

"There is no need to evaluate that," Charlie said, boasting at every turn.
"Anyone with eyes can see what the form (reduce + [1 2 3 4]) comes to."
Casey, who inside the barn had grown used to such claims, asked
him to actually write the form `(reduce + [1 2 3 4])` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

What Clojure form computes the sum? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + [1 2 3 4])"}}]}
````

### Ant and the Grasshopper  _(lens: prudence vs. idleness)_

**form**: `(reduce + [1 2 3 4])`  •  **expected**: `10`

````text
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Hum the grasshopper chalked a wager on a flat slate at the edge of the orchard: whoever
predicted the result of `(reduce + [1 2 3 4])` first would set the next day's
ration. Tic the ant, with eyes always on the path, said it would be simpler to type
the form into the REPL than to bicker about the form (reduce + [1 2 3 4]).

Question: write a Clojure expression for the sum.

---

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + [1 2 3 4])"}}]}
````

---

## G6-03 — require

_namespace — pulling code in_

### Tortoise and the Hare  _(lens: vanity vs. steadiness)_

**form**: `(clojure.string/upper-case "hare")`  •  **expected**: `'HARE'`

````text
It was well known among the animals that the Hare boasted of his speed at every chance. All this took place by the meadow.

Mossback the tortoise had been keeping a small leather notebook of every
form he had successfully evaluated. Today in the meadow, the
next entry was the form using clojure.string/upper-case on "hare". Bramble the hare peered over
his shoulder at the form `(clojure.string/upper-case "hare")` and asked what
it would come out to.

Question: write a Clojure expression for the upper-cased string "HARE".

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"hare\")"}}]}
````

### Goose and the Golden Eggs  _(lens: greed vs. patience)_

**form**: `(clojure.string/upper-case "hare")`  •  **expected**: `'HARE'`

````text
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Jordan had been trying to teach Morgan how the REPL
works. "Here," they said, pointing to the form using clojure.string/upper-case on "hare".
"You hand the form `(clojure.string/upper-case "hare")` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Honk the goose gives one egg each morning, no more, no less."

Question: write a Clojure expression for the upper-cased string "HARE".

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"hare\")"}}]}
````

### Ant and the Grasshopper  _(lens: prudence vs. idleness)_

**form**: `(clojure.string/upper-case "grasshopper")`  •  **expected**: `'GRASSHOPPER'`

````text
Two creatures of the meadow approached the coming winter very differently.

Chirp the grasshopper chalked a wager on a flat slate atop the hilltop: whoever
predicted the result of `(clojure.string/upper-case "grasshopper")` first would set the next day's
ration. Toc the ant, saying very little, said it would be simpler to type
the form into the REPL than to bicker about the form using clojure.string/upper-case on "grasshopper".

What Clojure form computes the upper-cased string "GRASSHOPPER"? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"grasshopper\")"}}]}
````

---

## G7-02 — try / catch

_errors — catching what the runtime throws_

### Tortoise and the Hare  _(lens: vanity vs. steadiness)_

**form**: `(try (/ 1 0) (catch Exception e :caught))`  •  **expected**: `':caught'`

````text
It was well known among the animals that the Hare boasted of his speed at every chance. All this took place near the orchard.

"There is no need to evaluate that," Whisker the hare said, boasting at every turn.
"Anyone can see what a division by zero wrapped in try/catch comes to." Mossback the tortoise, who
at the edge of the orchard had grown used to such claims, asked him to actually
write the form `(try (/ 1 0) (catch Exception e :caught))` and submit it to the REPL — just to be
sure.

What Clojure form computes the keyword :caught returned by the catch branch? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 1 0) (catch Exception e :caught))"}}]}
````

### Goose and the Golden Eggs  _(lens: greed vs. patience)_

**form**: `(try (/ 1 0) (catch Exception e :caught))`  •  **expected**: `':caught'`

````text
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was at the edge of the village.

Robin had been trying to teach Morgan how the REPL
works. "Here," they said, pointing to a division by zero wrapped in try/catch.
"You hand the form `(try (/ 1 0) (catch Exception e :caught))` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Quill the goose gives one egg each morning, no more, no less."

Write a form whose evaluation gives the keyword :caught returned by the catch branch.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 1 0) (catch Exception e :caught))"}}]}
````

### Ant and the Grasshopper  _(lens: prudence vs. idleness)_

**form**: `(try (/ 1 0) (catch Exception e :caught))`  •  **expected**: `':caught'`

````text
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Tic the ant had been keeping a small leather notebook of every form
he had successfully evaluated. Today in the meadow, the next entry
was a division by zero wrapped in try/catch. Chirp the grasshopper peered over
his shoulder at the form `(try (/ 1 0) (catch Exception e :caught))` and asked what it
would come out to.

Question: write a Clojure expression for the keyword :caught returned by the catch branch.

---

I use ex-info to attach data to the error.

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 1 0) (catch Exception e :caught))"}}]}
````

---

## G8-04 — Protocol definition

_polymorphism — defining behavior across types_

### Tortoise and the Hare  _(lens: vanity vs. steadiness)_

**form**: `(do (defprotocol Pace (speed [this])) (some? Pace))`  •  **expected**: `True`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. This was at the edge of the hilltop.

A scrap of parchment, pinned to a tree at the edge of the hilltop, set out a rule that all
creatures of the woodland would have to abide by. Bramble, boasting at every turn,
read it aloud: it was a defprotocol Pace with a single method speed. Shelly the tortoise said only the
REPL could confirm what `(do (defprotocol Pace (speed [this])) (some? Pace))` actually decided.

What Clojure form computes whether the Pace protocol was defined (a non-nil truthy value)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (some? Pace))"}}]}
````

### Goose and the Golden Eggs  _(lens: greed vs. patience)_

**form**: `(do (defprotocol Pace (speed [this])) (some? Pace))`  •  **expected**: `True`

````text
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A small wooden notice nailed to a post deep inside a cottage carried a puzzle for
the village. The riddle asked the reader to evaluate `(do (defprotocol Pace (speed [this])) (some? Pace))`.
Jordan laughed, with a smug grin, and declared it too easy.
Emily said, untroubled by what others thought, that the only honest way to know
a defprotocol Pace with a single method speed was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a Clojure expression that computes whether the Pace protocol was defined (a non-nil truthy value).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (some? Pace))"}}]}
````

### Ant and the Grasshopper  _(lens: prudence vs. idleness)_

**form**: `(do (defprotocol Pace (speed [this])) (some? Pace))`  •  **expected**: `True`

````text
All summer long, the Ant worked while the Grasshopper sang. It happened in the garden.

Hum the grasshopper chalked a wager on a flat slate in the garden: whoever
predicted the result of `(do (defprotocol Pace (speed [this])) (some? Pace))` first would set the next day's
ration. Tic the ant, untroubled by what others thought, said it would be simpler to type
the form into the REPL than to bicker about a defprotocol Pace with a single method speed.

Write a form whose evaluation gives whether the Pace protocol was defined (a non-nil truthy value).

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (some? Pace))"}}]}
````

---

## G9-03 — Atom introduction

_concurrency — coordinated mutable state_

### Tortoise and the Hare  _(lens: vanity vs. steadiness)_

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

Hopper the hare and Slowpoke the tortoise stopped in the garden where someone had
written an atom starting at 0, incremented once via swap! on a flat stone. Hopper, with a smug grin, declared
that he could see the answer at a glance. Slowpoke,
with steady, careful steps, suggested they actually evaluate the form `(do (def a (atom 0)) (swap! a inc) @a)`
in the REPL and read off whatever it returned.

Write a Clojure expression that computes the value of the atom after one swap! inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
````

### Goose and the Golden Eggs  _(lens: greed vs. patience)_

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

````text
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened by the meadow.

A row of three coins sat on a wooden table at the edge of the meadow, set out as a
wager between Fiona and Alice. The bet was
simple: predict what `(do (def a (atom 0)) (swap! a inc) @a)` would return. Fiona,
imagining all that might be gained, was certain about the answer. Alice asked
her, saying very little, to actually write the form into the
REPL — an atom starting at 0, incremented once via swap! would be settled the moment the runtime
answered, not before.

Write a form whose evaluation gives the value of the atom after one swap! inc.

---

I bind the state, perform the update, then dereference.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
````

### Ant and the Grasshopper  _(lens: prudence vs. idleness)_

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

````text
All summer long, the Ant worked while the Grasshopper sang.

Beside a small stockpile at the farm, Chirp the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(do (def a (atom 0)) (swap! a inc) @a)`
first would win the right to set the next day's count.
Bit the ant, without complaint, said it was simpler to type the form into
the REPL than to argue about an atom starting at 0, incremented once via swap!.

Write a Clojure expression that computes the value of the atom after one swap! inc.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
````

---

## G10-03 — defmacro introduction

_macros — code that writes code_

### Tortoise and the Hare  _(lens: vanity vs. steadiness)_

**form**: `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`  •  **expected**: `3`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. This was at the edge of the meadow.

Mossback the tortoise had spent the morning at the edge of the meadow sketching a tiny
language of his own — a notebook of macros that wrote
other forms. The next entry was a tiny when-style macro and a call to it, and the form
`(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))` was what Mossback wanted Hopper the hare to submit so
the REPL could show what code it produced or what value it returned.

Write a form whose evaluation gives what (my-when true 1 2 3) returns.

---

I write the macro form and let the runtime evaluate or expand it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

### Goose and the Golden Eggs  _(lens: greed vs. patience)_

**form**: `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`  •  **expected**: `3`

````text
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A small audience of neighbors had gathered inside the barn to watch
Alice attempt to outguess Diana at reading the
REPL. Diana pointed to a tiny when-style macro and a call to it and read out the form
aloud: `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`. The crowd waited to see who would correctly
write the form to submit; Quill the goose watched too, untroubled by
the noise.

Write a Clojure expression that computes what (my-when true 1 2 3) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

### Ant and the Grasshopper  _(lens: prudence vs. idleness)_

**form**: `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`  •  **expected**: `3`

````text
All summer long, the Ant worked while the Grasshopper sang. This was by the woods.

Bit the ant and Chirp the grasshopper stopped near the woods where someone had
written a tiny when-style macro and a call to it on a flat stone. Chirp, boasting at every turn,
declared that he could see the answer at a glance.
Bit, untroubled by what others thought, suggested they actually evaluate the form
`(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))` in the REPL and read off whatever it returned.

Question: write a Clojure expression for what (my-when true 1 2 3) returns.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

---

## G11-02 — Method call syntax

_interop — calling host methods_

### Tortoise and the Hare  _(lens: vanity vs. steadiness)_

**form**: `(.toUpperCase "abc")`  •  **expected**: `'ABC'`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. This was near the garden.

"This is not your meadow," Mossback the tortoise said in the garden, with eyes always on the path.
"Here, the methods belong to objects, and the dot has a particular
meaning." Hopper the hare, with great whoops of laughter, said he could read
the foreign form anyway. Mossback sketched `(.toUpperCase "abc")` on the
ground; let the runtime, he insisted, declare what
the method call (.toUpperCase "abc") returned.

Write a form whose evaluation gives the uppercased string returned by the method.

---

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
````

### Goose and the Golden Eggs  _(lens: greed vs. patience)_

**form**: `(.toUpperCase "abc")`  •  **expected**: `'ABC'`

````text
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place in the cellar.

At a small stall inside the cellar, someone had chalked a wager: whoever
predicted the result of `(.toUpperCase "abc")` first would set the asking
price for the morning's eggs. Grace, stepping deliberately, said it
was easier to type the form into the REPL than to argue about
the method call (.toUpperCase "abc") — Quill the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a form whose evaluation gives the uppercased string returned by the method.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
````

### Ant and the Grasshopper  _(lens: prudence vs. idleness)_

**form**: `(.toUpperCase "abc")`  •  **expected**: `'ABC'`

````text
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Halfway through the morning's work, Chirp the grasshopper blocked
Tic the ant's path at the farm and refused to step aside until someone
could prove what the form `(.toUpperCase "abc")` evaluated to. Chirp
called it impossible. Tic the ant, walking up at his usual
pace, simply said: "Submit the method call (.toUpperCase "abc") to the REPL. Whatever comes
back is the answer."

Question: write a Clojure expression for the uppercased string returned by the method.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
````

---

## G12-01 — Transducers introduction

_real-world — composable transformations_

### Tortoise and the Hare  _(lens: vanity vs. steadiness)_

**form**: `(into [] (map inc) [1 2 3])`  •  **expected**: `[2, 3, 4]`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

"This isn't a sprint trick," Slowpoke said by the forest, saying very little.
"It's a tool." Pip the hare looked at the transducer (map inc) used via into and admitted
they would not have known what to write. Slowpoke sketched
`(into [] (map inc) [1 2 3])` on a slate so the runtime could speak for itself.

Write a form whose evaluation gives [1 2 3] each incremented through a transducer.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
````

### Goose and the Golden Eggs  _(lens: greed vs. patience)_

**form**: `(into [] (map inc) [1 2 3])`  •  **expected**: `[2, 3, 4]`

````text
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

At a small stall at the edge of the orchard, someone had chalked a wager: whoever
predicted the result of `(into [] (map inc) [1 2 3])` first would set the asking
price for the morning's eggs. Edward, with eyes always on the path, said it
was easier to type the form into the REPL than to argue about
the transducer (map inc) used via into — Honk the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a form whose evaluation gives [1 2 3] each incremented through a transducer.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
````

### Ant and the Grasshopper  _(lens: prudence vs. idleness)_

**form**: `(into [] (map inc) [1 2 3])`  •  **expected**: `[2, 3, 4]`

````text
All summer long, the Ant worked while the Grasshopper sang.

With a twig, Hum the grasshopper marked out a wager in the forest: whoever
guessed the result of `(into [] (map inc) [1 2 3])` first would win the right to
choose the next song. Tic the ant, with steady, careful steps, said it was easier
to ask the REPL about the transducer (map inc) used via into than to argue.

Write a Clojure expression that computes [1 2 3] each incremented through a transducer.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
````

---

