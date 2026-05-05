# crow-pitcher grade 9 — deep spot-check

5 records per subject for hand-audit.

---

## G9-01: Immutability as default — review

### G9-01 record 1  •  form `(let [m {:a 1}] (assoc m :b 2) m)`  •  expected `{':a': 1}`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened in the meadow.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust in the meadow: whoever guessed the result of `(let [m {:a 1}] (assoc m :b 2) m)`
first would win the right to claim the next clear water they found.
Sable the crow, untroubled by what others thought, said it was easier to ask the REPL
about binding m, calling (assoc m :b 2), then returning m unchanged than to argue.

Write a Clojure expression that computes the original map after a non-mutating assoc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :b 2) m)"}}]}
```

### G9-01 record 2  •  form `(let [v [1 2 3]] (conj v 4) v)`  •  expected `[1, 2, 3]`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place near the road.

A wooden sign nailed to a tree near the road carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(let [v [1 2 3]] (conj v 4) v)`. Sable laughed, with a smug grin, and declared it
too easy. Caw said patiently that the only way to be sure of
binding v, calling (conj v 4), then returning v unchanged was to drop it into the REPL.

What Clojure form computes the original vector after conj? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [v [1 2 3]] (conj v 4) v)"}}]}
```

### G9-01 record 3  •  form `(let [m {:a 1}] (assoc m :b 2) m)`  •  expected `{':a': 1}`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Halfway through a long thirsty afternoon, Korvus the crow alighted
in the market and refused to fly on until someone could prove what the form
`(let [m {:a 1}] (assoc m :b 2) m)` evaluated to. Korvus called it impossible.
Caw the crow, gliding down at an unhurried pace, simply said: "Drop
binding m, calling (assoc m :b 2), then returning m unchanged into the REPL. Whatever rises is the answer."

What Clojure form computes the original map after a non-mutating assoc? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :b 2) m)"}}]}
```

### G9-01 record 4  •  form `(let [v [1 2 3]] (conj v 4) v)`  •  expected `[1, 2, 3]`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. All this took place near the market.

Sable the crow etched a wager along the rim of a chipped pitcher
at the edge of the market: whoever predicted the result of `(let [v [1 2 3]] (conj v 4) v)` first would set
the next day's foraging route. Caw the crow, untroubled by what others thought, said it
would be simpler to drop the form into the REPL than to bicker about
binding v, calling (conj v 4), then returning v unchanged.

What Clojure form computes the original vector after conj? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [v [1 2 3]] (conj v 4) v)"}}]}
```

### G9-01 record 5  •  form `(let [m {:a 1}] (assoc m :b 2) m)`  •  expected `{':a': 1}`

```
Hunger and thirst had driven the Crow far from her usual perch.

Caw the crow and Sable the crow alighted by the farm on the rim of an old
pitcher where someone had scratched binding m, calling (assoc m :b 2), then returning m unchanged. Caw,
shouting until her voice cracked, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(let [m {:a 1}] (assoc m :b 2) m)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

What Clojure form computes the original map after a non-mutating assoc? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :b 2) m)"}}]}
```

## G9-02: Why state at all

### G9-02 record 1  •  form `(do (def counter (atom 0)) (swap! counter inc) @counter)`  •  expected `1`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust at the edge of the orchard: whoever guessed the result of `(do (def counter (atom 0)) (swap! counter inc) @counter)`
first would win the right to claim the next clear water they found.
Caw the crow, without complaint, said it was easier to ask the REPL
about an atom counter, incremented once, then read than to argue.

Write a Clojure expression that computes the value of counter after one swap! inc.

---

I let each form raise the surface a little closer to the answer.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def counter (atom 0)) (swap! counter inc) @counter)"}}]}
```

### G9-02 record 2  •  form `(do (def progress (atom :idle)) (reset! progress :running) @progress)`  •  expected `':running'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened by the market.

"Why bother with all this?" Korvus the crow demanded in the market.
"He could just splash the new value in!"
Caw the crow, with steady, careful steps, sketched out a progress atom reset to :running
instead and showed the form `(do (def progress (atom :idle)) (reset! progress :running) @progress)`: the proper way for the
runtime to manage change. They agreed to submit it to the REPL.

Question: write a Clojure expression for the value of progress after reset!.

---

I let each form raise the surface a little closer to the answer.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def progress (atom :idle)) (reset! progress :running) @progress)"}}]}
```

### G9-02 record 3  •  form `(do (def counter (atom 0)) (swap! counter inc) @counter)`  •  expected `1`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place in the orchard.

"There is no need to evaluate that," Sable the crow said, puffed up with pride.
"Anyone with a sharp eye can see what an atom counter, incremented once, then read comes to."
Caw the crow, who at the edge of the orchard had grown used to such claims, asked
them to actually write the form `(do (def counter (atom 0)) (swap! counter inc) @counter)` and drop it
into the REPL — just to be sure.

What Clojure form computes the value of counter after one swap! inc? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def counter (atom 0)) (swap! counter inc) @counter)"}}]}
```

### G9-02 record 4  •  form `(do (def progress (atom :idle)) (reset! progress :running) @progress)`  •  expected `':running'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened at the edge of the farm.

At a moss-flecked pitcher in the farm, Caw the crow sketched a small
wager: whoever guessed the result of `(do (def progress (atom :idle)) (reset! progress :running) @progress)` first would drink
first when the water rose. Sable the crow, stepping deliberately, said it was
simpler to type the form into the REPL than to argue about
a progress atom reset to :running.

Question: write a Clojure expression for the value of progress after reset!.

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def progress (atom :idle)) (reset! progress :running) @progress)"}}]}
```

### G9-02 record 5  •  form `(do (def counter (atom 0)) (swap! counter inc) @counter)`  •  expected `1`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was near the garden.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust in the garden: whoever guessed the result of `(do (def counter (atom 0)) (swap! counter inc) @counter)`
first would win the right to claim the next clear water they found.
Korvus the crow, untroubled by what others thought, said it was easier to ask the REPL
about an atom counter, incremented once, then read than to argue.

Write a form whose evaluation gives the value of counter after one swap! inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def counter (atom 0)) (swap! counter inc) @counter)"}}]}
```

## G9-03: Atom introduction

### G9-03 record 1  •  form `(do (def a (atom 0)) (swap! a inc) @a)`  •  expected `1`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Halfway through a long thirsty afternoon, Sable the crow alighted
by the orchard and refused to fly on until someone could prove what the form
`(do (def a (atom 0)) (swap! a inc) @a)` evaluated to. Sable called it impossible.
Caw the crow, gliding down at an unhurried pace, simply said: "Drop
an atom starting at 0, incremented once via swap! into the REPL. Whatever rises is the answer."

Write a form whose evaluation gives the value of the atom after one swap! inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
```

### G9-03 record 2  •  form `(do (def a (atom 10)) (swap! a + 5) @a)`  •  expected `15`

```
Hunger and thirst had driven the Crow far from her usual perch. This was in the farm.

"There is no need to evaluate that," Sable the crow said, with a smug grin.
"Anyone with a sharp eye can see what an atom starting at 10, with (swap! a + 5) comes to."
Korvus the crow, who near the farm had grown used to such claims, asked
them to actually write the form `(do (def a (atom 10)) (swap! a + 5) @a)` and drop it
into the REPL — just to be sure.

What Clojure form computes the value of the atom after swap! + 5? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 10)) (swap! a + 5) @a)"}}]}
```

### G9-03 record 3  •  form `(do (def a (atom :start)) (reset! a :done) @a)`  •  expected `':done'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Sable the crow had been trying to teach Caw the crow how the REPL
works. "Look here," they said, pointing to an atom reset! from :start to :done.
"You hand the form `(do (def a (atom :start)) (reset! a :done) @a)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Caw, with a thirst that hurt to bear, agreed to try.

Write a Clojure expression that computes the value of the atom after reset!.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom :start)) (reset! a :done) @a)"}}]}
```

### G9-03 record 4  •  form `(do (def a (atom 0)) (swap! a inc) @a)`  •  expected `1`

```
Hunger and thirst had driven the Crow far from her usual perch.

Sable the crow had been keeping a small leather notebook of every form
they had successfully dropped into the REPL — one entry per
stone, one rise per form. Today at the edge of the orchard, the next entry was
an atom starting at 0, incremented once via swap!. Caw the crow peered over their shoulder
at the form `(do (def a (atom 0)) (swap! a inc) @a)` and asked what it would come out to.

Write a form whose evaluation gives the value of the atom after one swap! inc.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
```

### G9-03 record 5  •  form `(do (def a (atom 10)) (swap! a + 5) @a)`  •  expected `15`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place in the farm.

"Why bother with all this?" Sable the crow demanded in the farm.
"They could just splash the new value in!"
Korvus the crow, saying very little, sketched out an atom starting at 10, with (swap! a + 5)
instead and showed the form `(do (def a (atom 10)) (swap! a + 5) @a)`: the proper way for the
runtime to manage change. They agreed to submit it to the REPL.

Write a Clojure expression that computes the value of the atom after swap! + 5.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 10)) (swap! a + 5) @a)"}}]}
```

## G9-04: Atom CAS semantics

### G9-04 record 1  •  form `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)`  •  expected `1`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was at the edge of the hilltop.

Caw the crow and Korvus the crow alighted at the edge of the hilltop on the rim of an old
pitcher where someone had scratched compare-and-set! on an atom: expected 0, set to 1. Caw,
her hands trembling, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a Clojure expression that computes the value of the atom after a successful CAS.

---

I let the runtime mediate the change before reading the final value.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (compare-and-set! a 0 1) @a)"}}]}
```

### G9-04 record 2  •  form `(do (def a (atom 5)) (compare-and-set! a 0 99) @a)`  •  expected `5`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

"There is no need to evaluate that," Korvus the crow said, with great whoops of laughter.
"Anyone with a sharp eye can see what compare-and-set! when the expected value doesn't match (no change) comes to."
Sable the crow, who at the edge of the village had grown used to such claims, asked
him to actually write the form `(do (def a (atom 5)) (compare-and-set! a 0 99) @a)` and drop it
into the REPL — just to be sure.

What Clojure form computes the value of the atom after a CAS that does not fire? Submit it via `eval`.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 5)) (compare-and-set! a 0 99) @a)"}}]}
```

### G9-04 record 3  •  form `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)`  •  expected `1`

```
Hunger and thirst had driven the Crow far from her usual perch.

Caw the crow had been trying to teach Sable the crow how the REPL
works. "Look here," she said, pointing to compare-and-set! on an atom: expected 0, set to 1.
"You hand the form `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, her beak cracked with thirst, agreed to try.

Question: write a Clojure expression for the value of the atom after a successful CAS.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (compare-and-set! a 0 1) @a)"}}]}
```

### G9-04 record 4  •  form `(do (def a (atom 5)) (compare-and-set! a 0 99) @a)`  •  expected `5`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A small audience of sparrows had gathered by the market to watch
Caw the crow attempt to outwit Sable the crow at the rim of an old
pitcher. Sable pointed to compare-and-set! when the expected value doesn't match (no change) and read out the form
aloud: `(do (def a (atom 5)) (compare-and-set! a 0 99) @a)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives the value of the atom after a CAS that does not fire.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 5)) (compare-and-set! a 0 99) @a)"}}]}
```

### G9-04 record 5  •  form `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)`  •  expected `1`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Korvus the crow and Sable the crow alighted by the market on the rim of an old
pitcher where someone had scratched compare-and-set! on an atom: expected 0, set to 1. Korvus,
with growing alarm, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Question: write a Clojure expression for the value of the atom after a successful CAS.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (compare-and-set! a 0 1) @a)"}}]}
```

## G9-05: Watch on atom

### G9-05 record 1  •  form `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)`  •  expected `[1]`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Sable the crow etched a wager along the rim of a chipped pitcher
near the market: whoever predicted the result of `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)` first would set
the next day's foraging route. Korvus the crow, without complaint, said it
would be simpler to drop the form into the REPL than to bicker about
an atom with a watch that appends each new value to a log.

What Clojure form computes the contents of the log after one swap? Submit it via `eval`.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)"}}]}
```

### G9-05 record 2  •  form `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)`  •  expected `[1]`

```
Hunger and thirst had driven the Crow far from her usual perch.

Caw the crow kept a small ledger of state near the market — a value that
might change as the day went on, like the water level rising stone
by stone. She explained that the form `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)`
captured an atom with a watch that appends each new value to a log: a careful, ordered update.
Sable the crow, with a smug grin, asked the REPL to confirm the final
value.

Question: write a Clojure expression for the contents of the log after one swap.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)"}}]}
```

### G9-05 record 3  •  form `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)`  •  expected `[1]`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust atop the hilltop: whoever guessed the result of `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)`
first would win the right to claim the next clear water they found.
Korvus the crow, with steady, careful steps, said it was easier to ask the REPL
about an atom with a watch that appends each new value to a log than to argue.

Write a form whose evaluation gives the contents of the log after one swap.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)"}}]}
```

### G9-05 record 4  •  form `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)`  •  expected `[1]`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Korvus the crow kept a small ledger of state at the edge of the meadow — a value that
might change as the day went on, like the water level rising stone
by stone. He explained that the form `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)`
captured an atom with a watch that appends each new value to a log: a careful, ordered update.
Caw the crow, with a smug grin, asked the REPL to confirm the final
value.

Write a form whose evaluation gives the contents of the log after one swap.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)"}}]}
```

### G9-05 record 5  •  form `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)`  •  expected `[1]`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was atop the hilltop.

Korvus the crow had been keeping a small leather notebook of every form
he had successfully dropped into the REPL — one entry per
stone, one rise per form. Today atop the hilltop, the next entry was
an atom with a watch that appends each new value to a log. Sable the crow peered over his shoulder
at the form `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)` and asked what it would come out to.

What Clojure form computes the contents of the log after one swap? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)"}}]}
```

## G9-06: Validator on atom

### G9-06 record 1  •  form `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)`  •  expected `1`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Sable the crow had been keeping a small leather notebook of every form
they had successfully dropped into the REPL — one entry per
stone, one rise per form. Today at the edge of the garden, the next entry was
an atom with a number? validator, incremented once. Korvus the crow peered over their shoulder
at the form `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)` and asked what it would come out to.

Question: write a Clojure expression for the value of the atom after a valid update.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)"}}]}
```

### G9-06 record 2  •  form `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)`  •  expected `1`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

A wooden sign nailed to a tree along the road carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)`. Korvus laughed, puffed up with pride, and declared it
too easy. Sable said patiently that the only way to be sure of
an atom with a number? validator, incremented once was to drop it into the REPL.

Question: write a Clojure expression for the value of the atom after a valid update.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)"}}]}
```

### G9-06 record 3  •  form `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)`  •  expected `1`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

At a moss-flecked pitcher at the edge of the market, Sable the crow sketched a small
wager: whoever guessed the result of `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)` first would drink
first when the water rose. Caw the crow, with steady, careful steps, said it was
simpler to type the form into the REPL than to argue about
an atom with a number? validator, incremented once.

Write a Clojure expression that computes the value of the atom after a valid update.

---

I let each form raise the surface a little closer to the answer.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)"}}]}
```

### G9-06 record 4  •  form `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)`  •  expected `1`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place in the village.

Caw the crow and Sable the crow alighted in the village on the rim of an old
pitcher where someone had scratched an atom with a number? validator, incremented once. Caw,
wide-eyed with fear, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a Clojure expression that computes the value of the atom after a valid update.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)"}}]}
```

### G9-06 record 5  •  form `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)`  •  expected `1`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

"Why bother with all this?" Caw the crow demanded in the village.
"She could just splash the new value in!"
Korvus the crow, without complaint, sketched out an atom with a number? validator, incremented once
instead and showed the form `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)`: the proper way for the
runtime to manage change. They agreed to submit it to the REPL.

What Clojure form computes the value of the atom after a valid update? Submit it via `eval`.

---

I wrap the def, the update, and the deref together in a do block.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)"}}]}
```

## G9-07: Ref introduction

### G9-07 record 1  •  form `(do (def r (ref 0)) (dosync (alter r inc)) @r)`  •  expected `1`

```
Hunger and thirst had driven the Crow far from her usual perch.

"There is no need to evaluate that," Korvus the crow said, boasting at every turn.
"Anyone with a sharp eye can see what a ref incremented inside a dosync transaction comes to."
Caw the crow, who by the farm had grown used to such claims, asked
him to actually write the form `(do (def r (ref 0)) (dosync (alter r inc)) @r)` and drop it
into the REPL — just to be sure.

Question: write a Clojure expression for the value of the ref after dosync alter inc.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 0)) (dosync (alter r inc)) @r)"}}]}
```

### G9-07 record 2  •  form `(do (def r (ref 100)) (dosync (ref-set r 7)) @r)`  •  expected `7`

```
Hunger and thirst had driven the Crow far from her usual perch.

At a moss-flecked pitcher along the road, Caw the crow sketched a small
wager: whoever guessed the result of `(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` first would drink
first when the water rose. Korvus the crow, stepping deliberately, said it was
simpler to type the form into the REPL than to argue about
a ref ref-set to 7 inside dosync.

Question: write a Clojure expression for the value of the ref after ref-set 7.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 100)) (dosync (ref-set r 7)) @r)"}}]}
```

### G9-07 record 3  •  form `(do (def r (ref 0)) (dosync (alter r inc)) @r)`  •  expected `1`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

At a moss-flecked pitcher near the orchard, Korvus the crow sketched a small
wager: whoever guessed the result of `(do (def r (ref 0)) (dosync (alter r inc)) @r)` first would drink
first when the water rose. Sable the crow, untroubled by what others thought, said it was
simpler to type the form into the REPL than to argue about
a ref incremented inside a dosync transaction.

Question: write a Clojure expression for the value of the ref after dosync alter inc.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 0)) (dosync (alter r inc)) @r)"}}]}
```

### G9-07 record 4  •  form `(do (def r (ref 100)) (dosync (ref-set r 7)) @r)`  •  expected `7`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A small audience of sparrows had gathered near the village to watch
Korvus the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to a ref ref-set to 7 inside dosync and read out the form
aloud: `(do (def r (ref 100)) (dosync (ref-set r 7)) @r)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

What Clojure form computes the value of the ref after ref-set 7? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 100)) (dosync (ref-set r 7)) @r)"}}]}
```

### G9-07 record 5  •  form `(do (def r (ref 0)) (dosync (alter r inc)) @r)`  •  expected `1`

```
Hunger and thirst had driven the Crow far from her usual perch. It happened near the market.

Caw the crow etched a wager along the rim of a chipped pitcher
in the market: whoever predicted the result of `(do (def r (ref 0)) (dosync (alter r inc)) @r)` first would set
the next day's foraging route. Sable the crow, untroubled by what others thought, said it
would be simpler to drop the form into the REPL than to bicker about
a ref incremented inside a dosync transaction.

Write a form whose evaluation gives the value of the ref after dosync alter inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 0)) (dosync (alter r inc)) @r)"}}]}
```

## G9-08: dosync and alter

### G9-08 record 1  •  form `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])`  •  expected `[2, 3]`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Korvus the crow etched a wager along the rim of a chipped pitcher
in the meadow: whoever predicted the result of `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])` first would set
the next day's foraging route. Caw the crow, with steady, careful steps, said it
would be simpler to drop the form into the REPL than to bicker about
two refs each incremented inside a single dosync.

Question: write a Clojure expression for the pair [a b] after the coordinated transaction.

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])"}}]}
```

### G9-08 record 2  •  form `(do (def r (ref 10)) (dosync (alter r + 5)) @r)`  •  expected `15`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Korvus the crow and Caw the crow alighted at the edge of the village on the rim of an old
pitcher where someone had scratched a ref altered by + 5 inside dosync. Korvus,
in a panic, declared the answer beyond reach. Caw, patient as
ever, suggested they drop the form `(do (def r (ref 10)) (dosync (alter r + 5)) @r)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Question: write a Clojure expression for the value of the ref after alter + 5.

---

I let the runtime mediate the change before reading the final value.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 10)) (dosync (alter r + 5)) @r)"}}]}
```

### G9-08 record 3  •  form `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])`  •  expected `[2, 3]`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

At a moss-flecked pitcher on the hilltop, Korvus the crow sketched a small
wager: whoever guessed the result of `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])` first would drink
first when the water rose. Sable the crow, without complaint, said it was
simpler to type the form into the REPL than to argue about
two refs each incremented inside a single dosync.

Write a Clojure expression that computes the pair [a b] after the coordinated transaction.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])"}}]}
```

### G9-08 record 4  •  form `(do (def r (ref 10)) (dosync (alter r + 5)) @r)`  •  expected `15`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Halfway through a long thirsty afternoon, Sable the crow alighted
at the edge of the garden and refused to fly on until someone could prove what the form
`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` evaluated to. Sable called it impossible.
Korvus the crow, gliding down at an unhurried pace, simply said: "Drop
a ref altered by + 5 inside dosync into the REPL. Whatever rises is the answer."

Write a form whose evaluation gives the value of the ref after alter + 5.

---

I let each form raise the surface a little closer to the answer.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 10)) (dosync (alter r + 5)) @r)"}}]}
```

### G9-08 record 5  •  form `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])`  •  expected `[2, 3]`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Caw the crow had been keeping a small leather notebook of every form
she had successfully dropped into the REPL — one entry per
stone, one rise per form. Today by the farm, the next entry was
two refs each incremented inside a single dosync. Sable the crow peered over her shoulder
at the form `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])` and asked what it would come out to.

What Clojure form computes the pair [a b] after the coordinated transaction? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])"}}]}
```

## G9-09: Ref vs atom

### G9-09 record 1  •  form `(do (def a (atom 0)) (swap! a inc) @a)`  •  expected `1`

```
Hunger and thirst had driven the Crow far from her usual perch.

A small audience of sparrows had gathered by the farm to watch
Sable the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to an atom updated via swap! and read out the form
aloud: `(do (def a (atom 0)) (swap! a inc) @a)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

What Clojure form computes the value of the atom after one swap! inc? Submit it via `eval`.

---

I bind the state, perform the update, then dereference.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
```

### G9-09 record 2  •  form `(do (def r (ref 0)) (dosync (alter r inc)) @r)`  •  expected `1`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust by the meadow: whoever guessed the result of `(do (def r (ref 0)) (dosync (alter r inc)) @r)`
first would win the right to claim the next clear water they found.
Sable the crow, without complaint, said it was easier to ask the REPL
about a ref updated via alter inside dosync than to argue.

Write a form whose evaluation gives the value of the ref after one dosync alter inc.

---

I let the runtime mediate the change before reading the final value.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 0)) (dosync (alter r inc)) @r)"}}]}
```

### G9-09 record 3  •  form `(do (def a (atom 0)) (swap! a inc) @a)`  •  expected `1`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened at the edge of the hilltop.

A wooden sign nailed to a tree at the edge of the hilltop carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do (def a (atom 0)) (swap! a inc) @a)`. Caw laughed, puffed up with pride, and declared it
too easy. Korvus said patiently that the only way to be sure of
an atom updated via swap! was to drop it into the REPL.

Write a form whose evaluation gives the value of the atom after one swap! inc.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
```

### G9-09 record 4  •  form `(do (def r (ref 0)) (dosync (alter r inc)) @r)`  •  expected `1`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was in the meadow.

A wooden sign nailed to a tree in the meadow carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do (def r (ref 0)) (dosync (alter r inc)) @r)`. Korvus laughed, puffed up with pride, and declared it
too easy. Caw said patiently that the only way to be sure of
a ref updated via alter inside dosync was to drop it into the REPL.

Write a form whose evaluation gives the value of the ref after one dosync alter inc.

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 0)) (dosync (alter r inc)) @r)"}}]}
```

### G9-09 record 5  •  form `(do (def a (atom 0)) (swap! a inc) @a)`  •  expected `1`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened near the road.

"There is no need to evaluate that," Caw the crow said, boasting at every turn.
"Anyone with a sharp eye can see what an atom updated via swap! comes to."
Korvus the crow, who on the road had grown used to such claims, asked
her to actually write the form `(do (def a (atom 0)) (swap! a inc) @a)` and drop it
into the REPL — just to be sure.

Question: write a Clojure expression for the value of the atom after one swap! inc.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
```

## G9-10: Agent introduction

### G9-10 record 1  •  form `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`  •  expected `1`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Caw the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," she said, pointing to an agent sent inc and awaited.
"You hand the form `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, with a thirst that hurt to bear, agreed to try.

Question: write a Clojure expression for the value of the agent after send inc and await.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

### G9-10 record 2  •  form `(do (def ag (agent 5)) (send ag + 10) (await ag) @ag)`  •  expected `15`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Halfway through a long thirsty afternoon, Korvus the crow alighted
in the market and refused to fly on until someone could prove what the form
`(do (def ag (agent 5)) (send ag + 10) (await ag) @ag)` evaluated to. Korvus called it impossible.
Caw the crow, gliding down at an unhurried pace, simply said: "Drop
an agent sent (+ 10) and awaited into the REPL. Whatever rises is the answer."

Write a Clojure expression that computes the value of the agent after send + 10 and await.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 5)) (send ag + 10) (await ag) @ag)"}}]}
```

### G9-10 record 3  •  form `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`  •  expected `1`

```
Hunger and thirst had driven the Crow far from her usual perch.

Halfway through a long thirsty afternoon, Korvus the crow alighted
near the orchard and refused to fly on until someone could prove what the form
`(do (def ag (agent 0)) (send ag inc) (await ag) @ag)` evaluated to. Korvus called it impossible.
Caw the crow, gliding down at an unhurried pace, simply said: "Drop
an agent sent inc and awaited into the REPL. Whatever rises is the answer."

Question: write a Clojure expression for the value of the agent after send inc and await.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

### G9-10 record 4  •  form `(do (def ag (agent 5)) (send ag + 10) (await ag) @ag)`  •  expected `15`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Sable the crow had been trying to teach Caw the crow how the REPL
works. "Look here," they said, pointing to an agent sent (+ 10) and awaited.
"You hand the form `(do (def ag (agent 5)) (send ag + 10) (await ag) @ag)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Caw, parched from the long flight, agreed to try.

What Clojure form computes the value of the agent after send + 10 and await? Submit it via `eval`.

---

I bind the state, perform the update, then dereference.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 5)) (send ag + 10) (await ag) @ag)"}}]}
```

### G9-10 record 5  •  form `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`  •  expected `1`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

At a moss-flecked pitcher along the road, Caw the crow sketched a small
wager: whoever guessed the result of `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)` first would drink
first when the water rose. Korvus the crow, saying very little, said it was
simpler to type the form into the REPL than to argue about
an agent sent inc and awaited.

Write a Clojure expression that computes the value of the agent after send inc and await.

---

I let the runtime mediate the change before reading the final value.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

## G9-11: send and send-off

### G9-11 record 1  •  form `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`  •  expected `1`

```
Hunger and thirst had driven the Crow far from her usual perch.

Korvus the crow had been keeping a small leather notebook of every form
he had successfully dropped into the REPL — one entry per
stone, one rise per form. Today in the village, the next entry was
send used on an agent, then awaited. Caw the crow peered over his shoulder
at the form `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)` and asked what it would come out to.

Write a form whose evaluation gives the agent's value after send inc.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

### G9-11 record 2  •  form `(do (def ag (agent 0)) (send-off ag inc) (await ag) @ag)`  •  expected `1`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust on the road: whoever guessed the result of `(do (def ag (agent 0)) (send-off ag inc) (await ag) @ag)`
first would win the right to claim the next clear water they found.
Korvus the crow, stepping deliberately, said it was easier to ask the REPL
about send-off used on an agent, then awaited than to argue.

Write a Clojure expression that computes the agent's value after send-off inc.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send-off ag inc) (await ag) @ag)"}}]}
```

### G9-11 record 3  •  form `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`  •  expected `1`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. This was by the market.

A small audience of sparrows had gathered by the market to watch
Sable the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to send used on an agent, then awaited and read out the form
aloud: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

What Clojure form computes the agent's value after send inc? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

### G9-11 record 4  •  form `(do (def ag (agent 0)) (send-off ag inc) (await ag) @ag)`  •  expected `1`

```
Hunger and thirst had driven the Crow far from her usual perch.

Caw the crow etched a wager along the rim of a chipped pitcher
near the road: whoever predicted the result of `(do (def ag (agent 0)) (send-off ag inc) (await ag) @ag)` first would set
the next day's foraging route. Korvus the crow, saying very little, said it
would be simpler to drop the form into the REPL than to bicker about
send-off used on an agent, then awaited.

Question: write a Clojure expression for the agent's value after send-off inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send-off ag inc) (await ag) @ag)"}}]}
```

### G9-11 record 5  •  form `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`  •  expected `1`

```
Hunger and thirst had driven the Crow far from her usual perch.

Korvus the crow and Caw the crow alighted in the village on the rim of an old
pitcher where someone had scratched send used on an agent, then awaited. Korvus,
her hands trembling, declared the answer beyond reach. Caw, patient as
ever, suggested they drop the form `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

What Clojure form computes the agent's value after send inc? Submit it via `eval`.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

## G9-12: await — synchronizing on agents

### G9-12 record 1  •  form `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)`  •  expected `2`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

"Why bother with all this?" Korvus the crow demanded by the village.
"He could just splash the new value in!"
Sable the crow, with steady, careful steps, sketched out two send inc calls then await before deref
instead and showed the form `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)`: the proper way for the
runtime to manage change. They agreed to submit it to the REPL.

Write a form whose evaluation gives the agent's value after two sends and await.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)"}}]}
```

### G9-12 record 2  •  form `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)`  •  expected `2`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened in the orchard.

At a moss-flecked pitcher near the orchard, Korvus the crow sketched a small
wager: whoever guessed the result of `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)` first would drink
first when the water rose. Caw the crow, stepping deliberately, said it was
simpler to type the form into the REPL than to argue about
two send inc calls then await before deref.

Write a form whose evaluation gives the agent's value after two sends and await.

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)"}}]}
```

### G9-12 record 3  •  form `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)`  •  expected `2`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Sable the crow etched a wager along the rim of a chipped pitcher
on the road: whoever predicted the result of `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)` first would set
the next day's foraging route. Korvus the crow, with steady, careful steps, said it
would be simpler to drop the form into the REPL than to bicker about
two send inc calls then await before deref.

Write a form whose evaluation gives the agent's value after two sends and await.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)"}}]}
```

### G9-12 record 4  •  form `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)`  •  expected `2`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Sable the crow and Korvus the crow alighted in the village on the rim of an old
pitcher where someone had scratched two send inc calls then await before deref. Sable,
shouting until her voice cracked, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

What Clojure form computes the agent's value after two sends and await? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)"}}]}
```

### G9-12 record 5  •  form `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)`  •  expected `2`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened near the hilltop.

Halfway through a long thirsty afternoon, Sable the crow alighted
atop the hilltop and refused to fly on until someone could prove what the form
`(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)` evaluated to. Sable called it impossible.
Korvus the crow, gliding down at an unhurried pace, simply said: "Drop
two send inc calls then await before deref into the REPL. Whatever rises is the answer."

Write a Clojure expression that computes the agent's value after two sends and await.

---

I let each form raise the surface a little closer to the answer.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)"}}]}
```

## G9-13: future introduction

### G9-13 record 1  •  form `@(future (+ 1 2))`  •  expected `3`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A small audience of sparrows had gathered near the hilltop to watch
Korvus the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to a future computing (+ 1 2), dereferenced and read out the form
aloud: `@(future (+ 1 2))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives the value of the future for (+ 1 2).

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"@(future (+ 1 2))"}}]}
```

### G9-13 record 2  •  form `@(future (* 6 7))`  •  expected `42`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was in the farm.

Caw the crow had been trying to teach Sable the crow how the REPL
works. "Look here," she said, pointing to a future computing (* 6 7), dereferenced.
"You hand the form `@(future (* 6 7))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, with a thirst that hurt to bear, agreed to try.

What Clojure form computes the value of the future for (* 6 7)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"@(future (* 6 7))"}}]}
```

### G9-13 record 3  •  form `@(future (+ 1 2))`  •  expected `3`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was near the market.

At a moss-flecked pitcher in the market, Sable the crow sketched a small
wager: whoever guessed the result of `@(future (+ 1 2))` first would drink
first when the water rose. Caw the crow, with steady, careful steps, said it was
simpler to type the form into the REPL than to argue about
a future computing (+ 1 2), dereferenced.

Write a form whose evaluation gives the value of the future for (+ 1 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"@(future (+ 1 2))"}}]}
```

### G9-13 record 4  •  form `@(future (* 6 7))`  •  expected `42`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust at the edge of the village: whoever guessed the result of `@(future (* 6 7))`
first would win the right to claim the next clear water they found.
Caw the crow, her eyes always on the path, said it was easier to ask the REPL
about a future computing (* 6 7), dereferenced than to argue.

What Clojure form computes the value of the future for (* 6 7)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"@(future (* 6 7))"}}]}
```

### G9-13 record 5  •  form `@(future (+ 1 2))`  •  expected `3`

```
Hunger and thirst had driven the Crow far from her usual perch.

A small audience of sparrows had gathered by the garden to watch
Sable the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to a future computing (+ 1 2), dereferenced and read out the form
aloud: `@(future (+ 1 2))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Question: write a Clojure expression for the value of the future for (+ 1 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"@(future (+ 1 2))"}}]}
```

## G9-14: deref @ shorthand

### G9-14 record 1  •  form `(do (def a (atom 7)) @a)`  •  expected `7`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. This was in the village.

Korvus the crow had been trying to teach Sable the crow how the REPL
works. "Look here," he said, pointing to deref via @ on an atom holding 7.
"You hand the form `(do (def a (atom 7)) @a)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, parched from the long flight, agreed to try.

Write a Clojure expression that computes the value of the atom via @.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 7)) @a)"}}]}
```

### G9-14 record 2  •  form `(do (def a (atom 7)) (deref a))`  •  expected `7`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place along the road.

"There is no need to evaluate that," Caw the crow said, puffed up with pride.
"Anyone with a sharp eye can see what deref via the function form on an atom comes to."
Korvus the crow, who near the road had grown used to such claims, asked
her to actually write the form `(do (def a (atom 7)) (deref a))` and drop it
into the REPL — just to be sure.

Write a form whose evaluation gives the value of the atom via the deref function.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 7)) (deref a))"}}]}
```

### G9-14 record 3  •  form `(do (def a (atom 7)) @a)`  •  expected `7`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was by the market.

Halfway through a long thirsty afternoon, Caw the crow alighted
at the edge of the market and refused to fly on until someone could prove what the form
`(do (def a (atom 7)) @a)` evaluated to. Caw called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
deref via @ on an atom holding 7 into the REPL. Whatever rises is the answer."

Question: write a Clojure expression for the value of the atom via @.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 7)) @a)"}}]}
```

### G9-14 record 4  •  form `(do (def a (atom 7)) (deref a))`  •  expected `7`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was at the edge of the garden.

Caw the crow etched a wager along the rim of a chipped pitcher
at the edge of the garden: whoever predicted the result of `(do (def a (atom 7)) (deref a))` first would set
the next day's foraging route. Korvus the crow, her eyes always on the path, said it
would be simpler to drop the form into the REPL than to bicker about
deref via the function form on an atom.

Question: write a Clojure expression for the value of the atom via the deref function.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 7)) (deref a))"}}]}
```

### G9-14 record 5  •  form `(do (def a (atom 7)) @a)`  •  expected `7`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place at the edge of the market.

"There is no need to evaluate that," Sable the crow said, with great whoops of laughter.
"Anyone with a sharp eye can see what deref via @ on an atom holding 7 comes to."
Caw the crow, who near the market had grown used to such claims, asked
them to actually write the form `(do (def a (atom 7)) @a)` and drop it
into the REPL — just to be sure.

Write a form whose evaluation gives the value of the atom via @.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 7)) @a)"}}]}
```

## G9-15: promise — deliver and deref

### G9-15 record 1  •  form `(do (def p (promise)) (deliver p :done) @p)`  •  expected `':done'`

```
Hunger and thirst had driven the Crow far from her usual perch.

Korvus the crow kept a small ledger of state on the hilltop — a value that
might change as the day went on, like the water level rising stone
by stone. He explained that the form `(do (def p (promise)) (deliver p :done) @p)`
captured a promise delivered with :done, then dereffed: a careful, ordered update.
Caw the crow, swaggering through the underbrush, asked the REPL to confirm the final
value.

Write a Clojure expression that computes the value of the promise after deliver.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def p (promise)) (deliver p :done) @p)"}}]}
```

### G9-15 record 2  •  form `(do (def p (promise)) (deliver p 42) @p)`  •  expected `42`

```
Hunger and thirst had driven the Crow far from her usual perch. This was atop the hilltop.

A small audience of sparrows had gathered atop the hilltop to watch
Caw the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to a promise delivered with 42 and read out the form
aloud: `(do (def p (promise)) (deliver p 42) @p)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a Clojure expression that computes the value of the promise after deliver 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def p (promise)) (deliver p 42) @p)"}}]}
```

### G9-15 record 3  •  form `(do (def p (promise)) (deliver p :done) @p)`  •  expected `':done'`

```
Hunger and thirst had driven the Crow far from her usual perch.

"There is no need to evaluate that," Caw the crow said, with a smug grin.
"Anyone with a sharp eye can see what a promise delivered with :done, then dereffed comes to."
Sable the crow, who along the road had grown used to such claims, asked
her to actually write the form `(do (def p (promise)) (deliver p :done) @p)` and drop it
into the REPL — just to be sure.

Write a form whose evaluation gives the value of the promise after deliver.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def p (promise)) (deliver p :done) @p)"}}]}
```

### G9-15 record 4  •  form `(do (def p (promise)) (deliver p 42) @p)`  •  expected `42`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened in the market.

A small audience of sparrows had gathered in the market to watch
Korvus the crow attempt to outwit Sable the crow at the rim of an old
pitcher. Sable pointed to a promise delivered with 42 and read out the form
aloud: `(do (def p (promise)) (deliver p 42) @p)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Question: write a Clojure expression for the value of the promise after deliver 42.

---

I wrap the def, the update, and the deref together in a do block.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def p (promise)) (deliver p 42) @p)"}}]}
```

### G9-15 record 5  •  form `(do (def p (promise)) (deliver p :done) @p)`  •  expected `':done'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened by the village.

Halfway through a long thirsty afternoon, Sable the crow alighted
in the village and refused to fly on until someone could prove what the form
`(do (def p (promise)) (deliver p :done) @p)` evaluated to. Sable called it impossible.
Caw the crow, gliding down at an unhurried pace, simply said: "Drop
a promise delivered with :done, then dereffed into the REPL. Whatever rises is the answer."

What Clojure form computes the value of the promise after deliver? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def p (promise)) (deliver p :done) @p)"}}]}
```

## G9-16: volatile — when STM is too heavy

### G9-16 record 1  •  form `(do (def v (volatile! 0)) (vswap! v inc) @v)`  •  expected `1`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

At a moss-flecked pitcher near the orchard, Caw the crow sketched a small
wager: whoever guessed the result of `(do (def v (volatile! 0)) (vswap! v inc) @v)` first would drink
first when the water rose. Korvus the crow, stepping deliberately, said it was
simpler to type the form into the REPL than to argue about
a volatile! incremented via vswap!.

Write a form whose evaluation gives the value of the volatile after one vswap! inc.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def v (volatile! 0)) (vswap! v inc) @v)"}}]}
```

### G9-16 record 2  •  form `(do (def v (volatile! 5)) (vreset! v 99) @v)`  •  expected `99`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust by the market: whoever guessed the result of `(do (def v (volatile! 5)) (vreset! v 99) @v)`
first would win the right to claim the next clear water they found.
Sable the crow, with steady, careful steps, said it was easier to ask the REPL
about a volatile! reset via vreset! than to argue.

Write a form whose evaluation gives the value of the volatile after vreset! 99.

---

I wrap the def, the update, and the deref together in a do block.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def v (volatile! 5)) (vreset! v 99) @v)"}}]}
```

### G9-16 record 3  •  form `(do (def v (volatile! 0)) (vswap! v inc) @v)`  •  expected `1`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

At a moss-flecked pitcher atop the hilltop, Korvus the crow sketched a small
wager: whoever guessed the result of `(do (def v (volatile! 0)) (vswap! v inc) @v)` first would drink
first when the water rose. Sable the crow, her eyes always on the path, said it was
simpler to type the form into the REPL than to argue about
a volatile! incremented via vswap!.

Write a Clojure expression that computes the value of the volatile after one vswap! inc.

---

I let the runtime mediate the change before reading the final value.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def v (volatile! 0)) (vswap! v inc) @v)"}}]}
```

### G9-16 record 4  •  form `(do (def v (volatile! 5)) (vreset! v 99) @v)`  •  expected `99`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Caw the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," she said, pointing to a volatile! reset via vreset!.
"You hand the form `(do (def v (volatile! 5)) (vreset! v 99) @v)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, her beak cracked with thirst, agreed to try.

Question: write a Clojure expression for the value of the volatile after vreset! 99.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def v (volatile! 5)) (vreset! v 99) @v)"}}]}
```

### G9-16 record 5  •  form `(do (def v (volatile! 0)) (vswap! v inc) @v)`  •  expected `1`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was near the garden.

A small audience of sparrows had gathered near the garden to watch
Sable the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to a volatile! incremented via vswap! and read out the form
aloud: `(do (def v (volatile! 0)) (vswap! v inc) @v)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a Clojure expression that computes the value of the volatile after one vswap! inc.

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def v (volatile! 0)) (vswap! v inc) @v)"}}]}
```

## G9-17: binding — thread-local

### G9-17 record 1  •  form `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))`  •  expected `99`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A wooden sign nailed to a tree along the road carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))`. Sable laughed, swaggering through the underbrush, and declared it
too easy. Korvus said patiently that the only way to be sure of
a dynamic var *p* rebound to 99 inside binding was to drop it into the REPL.

What Clojure form computes the value of *p* inside the binding form? Submit it via `eval`.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))"}}]}
```

### G9-17 record 2  •  form `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)`  •  expected `1`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place along the road.

A small audience of sparrows had gathered along the road to watch
Korvus the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to the value of *p* AFTER the binding form exits and read out the form
aloud: `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

What Clojure form computes the original value of *p* once binding has unwound? Submit it via `eval`.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)"}}]}
```

### G9-17 record 3  •  form `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))`  •  expected `99`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Halfway through a long thirsty afternoon, Sable the crow alighted
near the garden and refused to fly on until someone could prove what the form
`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` evaluated to. Sable called it impossible.
Caw the crow, gliding down at an unhurried pace, simply said: "Drop
a dynamic var *p* rebound to 99 inside binding into the REPL. Whatever rises is the answer."

Question: write a Clojure expression for the value of *p* inside the binding form.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))"}}]}
```

### G9-17 record 4  •  form `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)`  •  expected `1`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A small audience of sparrows had gathered along the road to watch
Sable the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to the value of *p* AFTER the binding form exits and read out the form
aloud: `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives the original value of *p* once binding has unwound.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)"}}]}
```

### G9-17 record 5  •  form `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))`  •  expected `99`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Caw the crow etched a wager along the rim of a chipped pitcher
near the meadow: whoever predicted the result of `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` first would set
the next day's foraging route. Sable the crow, with steady, careful steps, said it
would be simpler to drop the form into the REPL than to bicker about
a dynamic var *p* rebound to 99 inside binding.

What Clojure form computes the value of *p* inside the binding form? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))"}}]}
```

## G9-18: locking — last resort

### G9-18 record 1  •  form `(do (def lock (Object.)) (locking lock (+ 1 2)))`  •  expected `3`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust at the edge of the village: whoever guessed the result of `(do (def lock (Object.)) (locking lock (+ 1 2)))`
first would win the right to claim the next clear water they found.
Caw the crow, without complaint, said it was easier to ask the REPL
about a locking form around (+ 1 2) using a fresh Object as monitor than to argue.

Write a form whose evaluation gives the result of the body inside locking.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def lock (Object.)) (locking lock (+ 1 2)))"}}]}
```

### G9-18 record 2  •  form `(do (def lock (Object.)) (locking lock 42))`  •  expected `42`

```
Hunger and thirst had driven the Crow far from her usual perch.

Halfway through a long thirsty afternoon, Sable the crow alighted
in the meadow and refused to fly on until someone could prove what the form
`(do (def lock (Object.)) (locking lock 42))` evaluated to. Sable called it impossible.
Korvus the crow, gliding down at an unhurried pace, simply said: "Drop
a locking form whose body is just the literal 42 into the REPL. Whatever rises is the answer."

Write a form whose evaluation gives the value the locking form returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def lock (Object.)) (locking lock 42))"}}]}
```

### G9-18 record 3  •  form `(do (def lock (Object.)) (locking lock (+ 1 2)))`  •  expected `3`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

A small audience of sparrows had gathered at the edge of the meadow to watch
Sable the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to a locking form around (+ 1 2) using a fresh Object as monitor and read out the form
aloud: `(do (def lock (Object.)) (locking lock (+ 1 2)))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a Clojure expression that computes the result of the body inside locking.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def lock (Object.)) (locking lock (+ 1 2)))"}}]}
```

### G9-18 record 4  •  form `(do (def lock (Object.)) (locking lock 42))`  •  expected `42`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was along the road.

"Why bother with all this?" Korvus the crow demanded on the road.
"He could just splash the new value in!"
Sable the crow, without complaint, sketched out a locking form whose body is just the literal 42
instead and showed the form `(do (def lock (Object.)) (locking lock 42))`: the proper way for the
runtime to manage change. They agreed to submit it to the REPL.

Write a form whose evaluation gives the value the locking form returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def lock (Object.)) (locking lock 42))"}}]}
```

### G9-18 record 5  •  form `(do (def lock (Object.)) (locking lock (+ 1 2)))`  •  expected `3`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. This was by the farm.

Korvus the crow had been trying to teach Caw the crow how the REPL
works. "Look here," he said, pointing to a locking form around (+ 1 2) using a fresh Object as monitor.
"You hand the form `(do (def lock (Object.)) (locking lock (+ 1 2)))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Caw, parched from the long flight, agreed to try.

Write a Clojure expression that computes the result of the body inside locking.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def lock (Object.)) (locking lock (+ 1 2)))"}}]}
```

