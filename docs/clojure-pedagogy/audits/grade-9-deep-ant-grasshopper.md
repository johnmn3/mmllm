# Deep spot-check: grade 9 ant-grasshopper (5 records per subject)

Manual-review dump for hand-audit. Each subject gets 5 rendered records sampled across different seeds so subplot/character/location variety is visible.

---

## G9-01: Immutability as default — review

### G9-01 record 1

**form**: `(let [m {:a 1}] (assoc m :b 2) m)`  •  **expected**: `{':a': 1}`

```
Two creatures of the meadow approached the coming winter very differently.

Toc the ant had been keeping a small leather notebook of every form
she had successfully evaluated. Today atop the hilltop, the next entry
was binding m, calling (assoc m :b 2), then returning m unchanged. Skip the grasshopper peered over
her shoulder at the form `(let [m {:a 1}] (assoc m :b 2) m)` and asked what it
would come out to.

What Clojure form computes the original map after a non-mutating assoc? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :b 2) m)"}}]}
```

### G9-01 record 2

**form**: `(let [m {:a 1}] (assoc m :b 2) m)`  •  **expected**: `{':a': 1}`

```
Two creatures of the meadow approached the coming winter very differently. It happened in the farm.

Bit the ant had been trying to teach Hum the grasshopper how the REPL
works. "Look here," they said, pointing to binding m, calling (assoc m :b 2), then returning m unchanged.
"You hand the form `(let [m {:a 1}] (assoc m :b 2) m)` to the runtime, and the runtime hands
you back what it evaluates to." Hum, lulled by the gentle wind, agreed to
try.

Write a form whose evaluation gives the original map after a non-mutating assoc.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :b 2) m)"}}]}
```

### G9-01 record 3

**form**: `(let [m {:a 1}] (assoc m :b 2) m)`  •  **expected**: `{':a': 1}`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Skip the grasshopper chalked a wager on a flat slate on the hilltop: whoever
predicted the result of `(let [m {:a 1}] (assoc m :b 2) m)` first would set the next day's
ration. Bit the ant, untroubled by what others thought, said it would be simpler to type
the form into the REPL than to bicker about binding m, calling (assoc m :b 2), then returning m unchanged.

Write a form whose evaluation gives the original map after a non-mutating assoc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :b 2) m)"}}]}
```

### G9-01 record 4

**form**: `(let [m {:a 1}] (assoc m :b 2) m)`  •  **expected**: `{':a': 1}`

```
All summer long, the Ant worked while the Grasshopper sang.

Bit the ant kept a small ledger of state by the orchard — a value that might
change as the season went on. They explained that the form
`(let [m {:a 1}] (assoc m :b 2) m)` captured binding m, calling (assoc m :b 2), then returning m unchanged: a careful, ordered update.
Skip the grasshopper, as if the race were already won, asked the REPL to confirm the final
value.

Write a form whose evaluation gives the original map after a non-mutating assoc.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :b 2) m)"}}]}
```

### G9-01 record 5

**form**: `(let [m {:a 1}] (assoc m :b 2) m)`  •  **expected**: `{':a': 1}`

```
Two creatures of the meadow approached the coming winter very differently.

Toc the ant had been trying to teach Skip the grasshopper how the REPL
works. "Look here," she said, pointing to binding m, calling (assoc m :b 2), then returning m unchanged.
"You hand the form `(let [m {:a 1}] (assoc m :b 2) m)` to the runtime, and the runtime hands
you back what it evaluates to." Skip, her legs heavy from sprinting, agreed to
try.

Question: write a Clojure expression for the original map after a non-mutating assoc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :b 2) m)"}}]}
```

## G9-02: Why state at all

### G9-02 record 1

**form**: `(do (def counter (atom 0)) (swap! counter inc) @counter)`  •  **expected**: `1`

```
Two creatures of the meadow approached the coming winter very differently.

Halfway through the morning's work, Chirp the grasshopper blocked
Bit the ant's path atop the hilltop and refused to step aside until someone
could prove what the form `(do (def counter (atom 0)) (swap! counter inc) @counter)` evaluated to. Chirp
called it impossible. Bit the ant, walking up at their usual
pace, simply said: "Submit an atom counter, incremented once, then read to the REPL. Whatever comes
back is the answer."

Question: write a Clojure expression for the value of counter after one swap! inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def counter (atom 0)) (swap! counter inc) @counter)"}}]}
```

### G9-02 record 2

**form**: `(do (def counter (atom 0)) (swap! counter inc) @counter)`  •  **expected**: `1`

```
Two creatures of the meadow approached the coming winter very differently.

With a twig, Chirp the grasshopper marked out a wager atop the hilltop: whoever
guessed the result of `(do (def counter (atom 0)) (swap! counter inc) @counter)` first would win the right to
choose the next song. Bit the ant, untroubled by what others thought, said it was easier
to ask the REPL about an atom counter, incremented once, then read than to argue.

What Clojure form computes the value of counter after one swap! inc? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def counter (atom 0)) (swap! counter inc) @counter)"}}]}
```

### G9-02 record 3

**form**: `(do (def counter (atom 0)) (swap! counter inc) @counter)`  •  **expected**: `1`

```
All summer long, the Ant worked while the Grasshopper sang. This was near the orchard.

Toc the ant kept a small ledger of state by the orchard — a value that might
change as the season went on. She explained that the form
`(do (def counter (atom 0)) (swap! counter inc) @counter)` captured an atom counter, incremented once, then read: a careful, ordered update.
Hum the grasshopper, with a smug grin, asked the REPL to confirm the final
value.

Write a Clojure expression that computes the value of counter after one swap! inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def counter (atom 0)) (swap! counter inc) @counter)"}}]}
```

### G9-02 record 4

**form**: `(do (def counter (atom 0)) (swap! counter inc) @counter)`  •  **expected**: `1`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

With a twig, Chirp the grasshopper marked out a wager by the garden: whoever
guessed the result of `(do (def counter (atom 0)) (swap! counter inc) @counter)` first would win the right to
choose the next song. Toc the ant, untroubled by what others thought, said it was easier
to ask the REPL about an atom counter, incremented once, then read than to argue.

Write a Clojure expression that computes the value of counter after one swap! inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def counter (atom 0)) (swap! counter inc) @counter)"}}]}
```

### G9-02 record 5

**form**: `(do (def counter (atom 0)) (swap! counter inc) @counter)`  •  **expected**: `1`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

"Why bother with all this?" Skip the grasshopper demanded by the orchard.
"She could just write the new value!" Tic the ant,
her eyes always on the path, sketched out an atom counter, incremented once, then read instead and showed the form
`(do (def counter (atom 0)) (swap! counter inc) @counter)`: the proper way for the runtime to manage change. They
agreed to submit it to the REPL.

Write a Clojure expression that computes the value of counter after one swap! inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def counter (atom 0)) (swap! counter inc) @counter)"}}]}
```

## G9-03: Atom introduction

### G9-03 record 1

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

```
All summer long, the Ant worked while the Grasshopper sang. All this took place at the edge of the garden.

Tic the ant had been trying to teach Skip the grasshopper how the REPL
works. "Look here," he said, pointing to an atom starting at 0, incremented once via swap!.
"You hand the form `(do (def a (atom 0)) (swap! a inc) @a)` to the runtime, and the runtime hands
you back what it evaluates to." Skip, drowsy from the warm sun, agreed to
try.

Question: write a Clojure expression for the value of the atom after one swap! inc.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
```

### G9-03 record 2

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

```
Two creatures of the meadow approached the coming winter very differently.

At the edge of a stockpile in the meadow, Skip the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(do (def a (atom 0)) (swap! a inc) @a)`
first would win the right to set the next day's count.
Tic the ant, without complaint, said it was simpler to type the form into
the REPL than to argue about an atom starting at 0, incremented once via swap!.

What Clojure form computes the value of the atom after one swap! inc? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
```

### G9-03 record 3

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Halfway through the morning's work, Chirp the grasshopper blocked
Bit the ant's path by the garden and refused to step aside until someone
could prove what the form `(do (def a (atom 0)) (swap! a inc) @a)` evaluated to. Chirp
called it impossible. Bit the ant, walking up at their usual
pace, simply said: "Submit an atom starting at 0, incremented once via swap! to the REPL. Whatever comes
back is the answer."

What Clojure form computes the value of the atom after one swap! inc? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
```

### G9-03 record 4

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

```
Two creatures of the meadow approached the coming winter very differently. It happened by the orchard.

A wooden sign nailed to a stalk in the orchard carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(do (def a (atom 0)) (swap! a inc) @a)`. Skip
laughed, swaggering through the underbrush, and declared it too easy. Toc said patiently
that the only way to be sure of an atom starting at 0, incremented once via swap! was to put it in the
REPL.

Write a Clojure expression that computes the value of the atom after one swap! inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
```

### G9-03 record 5

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Tic the ant had been trying to teach Chirp the grasshopper how the REPL
works. "Look here," he said, pointing to an atom starting at 0, incremented once via swap!.
"You hand the form `(do (def a (atom 0)) (swap! a inc) @a)` to the runtime, and the runtime hands
you back what it evaluates to." Chirp, lulled by the gentle wind, agreed to
try.

What Clojure form computes the value of the atom after one swap! inc? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
```

## G9-04: Atom CAS semantics

### G9-04 record 1

**form**: `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)`  •  **expected**: `1`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Toc the ant had been trying to teach Chirp the grasshopper how the REPL
works. "Look here," she said, pointing to compare-and-set! on an atom: expected 0, set to 1.
"You hand the form `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` to the runtime, and the runtime hands
you back what it evaluates to." Chirp, her legs heavy from sprinting, agreed to
try.

Write a Clojure expression that computes the value of the atom after a successful CAS.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (compare-and-set! a 0 1) @a)"}}]}
```

### G9-04 record 2

**form**: `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)`  •  **expected**: `1`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. This was on the hilltop.

Tic the ant had been trying to teach Chirp the grasshopper how the REPL
works. "Look here," he said, pointing to compare-and-set! on an atom: expected 0, set to 1.
"You hand the form `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` to the runtime, and the runtime hands
you back what it evaluates to." Chirp, yawning at the soft moss, agreed to
try.

Write a Clojure expression that computes the value of the atom after a successful CAS.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (compare-and-set! a 0 1) @a)"}}]}
```

### G9-04 record 3

**form**: `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)`  •  **expected**: `1`

```
Two creatures of the meadow approached the coming winter very differently.

With a twig, Skip the grasshopper marked out a wager in the garden: whoever
guessed the result of `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` first would win the right to
choose the next song. Tic the ant, her eyes always on the path, said it was easier
to ask the REPL about compare-and-set! on an atom: expected 0, set to 1 than to argue.

What Clojure form computes the value of the atom after a successful CAS? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (compare-and-set! a 0 1) @a)"}}]}
```

### G9-04 record 4

**form**: `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)`  •  **expected**: `1`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

A small audience of meadow creatures had gathered in the orchard to watch
Chirp the grasshopper attempt to outwit Toc the ant at reading the
REPL. Toc pointed to compare-and-set! on an atom: expected 0, set to 1 and read out the form aloud:
`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)`. The crowd waited to see who would correctly write the
form to submit.

Write a Clojure expression that computes the value of the atom after a successful CAS.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (compare-and-set! a 0 1) @a)"}}]}
```

### G9-04 record 5

**form**: `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)`  •  **expected**: `1`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. All this took place in the orchard.

A wooden sign nailed to a stalk by the orchard carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)`. Skip
laughed, puffed up with pride, and declared it too easy. Toc said patiently
that the only way to be sure of compare-and-set! on an atom: expected 0, set to 1 was to put it in the
REPL.

Write a Clojure expression that computes the value of the atom after a successful CAS.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (compare-and-set! a 0 1) @a)"}}]}
```

## G9-05: Watch on atom

### G9-05 record 1

**form**: `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)`  •  **expected**: `[1]`

```
Two creatures of the meadow approached the coming winter very differently.

Halfway through the morning's work, Skip the grasshopper blocked
Toc the ant's path at the edge of the woods and refused to step aside until someone
could prove what the form `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)` evaluated to. Skip
called it impossible. Toc the ant, walking up at her usual
pace, simply said: "Submit an atom with a watch that appends each new value to a log to the REPL. Whatever comes
back is the answer."

Write a form whose evaluation gives the contents of the log after one swap.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)"}}]}
```

### G9-05 record 2

**form**: `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)`  •  **expected**: `[1]`

```
Two creatures of the meadow approached the coming winter very differently. All this took place atop the hilltop.

"There is no need to evaluate that," Hum the grasshopper said,
with great whoops of laughter. "Anyone can see what an atom with a watch that appends each new value to a log comes to."
Tic the ant, who atop the hilltop had grown used to such claims, asked
them to actually write the form `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)` and
submit it to the REPL — just to be sure.

Question: write a Clojure expression for the contents of the log after one swap.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)"}}]}
```

### G9-05 record 3

**form**: `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)`  •  **expected**: `[1]`

```
Two creatures of the meadow approached the coming winter very differently. This was near the woods.

Tic the ant and Skip the grasshopper stopped in the woods where someone had
written an atom with a watch that appends each new value to a log on a flat stone. Skip, swaggering through the underbrush,
declared that she could see the answer at a glance.
Tic, her eyes always on the path, suggested they actually evaluate the form
`(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)` in the REPL and read off whatever it returned.

What Clojure form computes the contents of the log after one swap? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)"}}]}
```

### G9-05 record 4

**form**: `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)`  •  **expected**: `[1]`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

A wooden sign nailed to a stalk at the edge of the farm carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)`. Hum
laughed, swaggering through the underbrush, and declared it too easy. Tic said patiently
that the only way to be sure of an atom with a watch that appends each new value to a log was to put it in the
REPL.

Write a Clojure expression that computes the contents of the log after one swap.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)"}}]}
```

### G9-05 record 5

**form**: `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)`  •  **expected**: `[1]`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

At the edge of a stockpile atop the hilltop, Hum the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)`
first would win the right to set the next day's count.
Toc the ant, her eyes always on the path, said it was simpler to type the form into
the REPL than to argue about an atom with a watch that appends each new value to a log.

What Clojure form computes the contents of the log after one swap? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)"}}]}
```

## G9-06: Validator on atom

### G9-06 record 1

**form**: `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)`  •  **expected**: `1`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Tic the ant kept a small ledger of state near the woods — a value that might
change as the season went on. He explained that the form
`(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)` captured an atom with a number? validator, incremented once: a careful, ordered update.
Chirp the grasshopper, swaggering through the underbrush, asked the REPL to confirm the final
value.

Write a form whose evaluation gives the value of the atom after a valid update.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)"}}]}
```

### G9-06 record 2

**form**: `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)`  •  **expected**: `1`

```
All summer long, the Ant worked while the Grasshopper sang. This was near the orchard.

Halfway through the morning's work, Hum the grasshopper blocked
Tic the ant's path by the orchard and refused to step aside until someone
could prove what the form `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)` evaluated to. Hum
called it impossible. Tic the ant, walking up at his usual
pace, simply said: "Submit an atom with a number? validator, incremented once to the REPL. Whatever comes
back is the answer."

Write a Clojure expression that computes the value of the atom after a valid update.

---

I wrap the def, the update, and the deref together in a do block.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)"}}]}
```

### G9-06 record 3

**form**: `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)`  •  **expected**: `1`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

"Why bother with all this?" Hum the grasshopper demanded in the orchard.
"They could just write the new value!" Toc the ant,
untroubled by what others thought, sketched out an atom with a number? validator, incremented once instead and showed the form
`(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)`: the proper way for the runtime to manage change. They
agreed to submit it to the REPL.

Write a Clojure expression that computes the value of the atom after a valid update.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)"}}]}
```

### G9-06 record 4

**form**: `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)`  •  **expected**: `1`

```
Two creatures of the meadow approached the coming winter very differently. All this took place at the edge of the forest.

Toc the ant had been trying to teach Skip the grasshopper how the REPL
works. "Look here," she said, pointing to an atom with a number? validator, incremented once.
"You hand the form `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)` to the runtime, and the runtime hands
you back what it evaluates to." Skip, weary from the morning's effort, agreed to
try.

Question: write a Clojure expression for the value of the atom after a valid update.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)"}}]}
```

### G9-06 record 5

**form**: `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)`  •  **expected**: `1`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. This was in the meadow.

Bit the ant had been trying to teach Skip the grasshopper how the REPL
works. "Look here," they said, pointing to an atom with a number? validator, incremented once.
"You hand the form `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)` to the runtime, and the runtime hands
you back what it evaluates to." Skip, lulled by the gentle wind, agreed to
try.

Question: write a Clojure expression for the value of the atom after a valid update.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)"}}]}
```

## G9-07: Ref introduction

### G9-07 record 1

**form**: `(do (def r (ref 0)) (dosync (alter r inc)) @r)`  •  **expected**: `1`

```
Two creatures of the meadow approached the coming winter very differently.

A small audience of meadow creatures had gathered by the forest to watch
Hum the grasshopper attempt to outwit Tic the ant at reading the
REPL. Tic pointed to a ref incremented inside a dosync transaction and read out the form aloud:
`(do (def r (ref 0)) (dosync (alter r inc)) @r)`. The crowd waited to see who would correctly write the
form to submit.

Question: write a Clojure expression for the value of the ref after dosync alter inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 0)) (dosync (alter r inc)) @r)"}}]}
```

### G9-07 record 2

**form**: `(do (def r (ref 0)) (dosync (alter r inc)) @r)`  •  **expected**: `1`

```
All summer long, the Ant worked while the Grasshopper sang. All this took place at the edge of the farm.

A wooden sign nailed to a stalk in the farm carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(do (def r (ref 0)) (dosync (alter r inc)) @r)`. Hum
laughed, with great whoops of laughter, and declared it too easy. Toc said patiently
that the only way to be sure of a ref incremented inside a dosync transaction was to put it in the
REPL.

Write a Clojure expression that computes the value of the ref after dosync alter inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 0)) (dosync (alter r inc)) @r)"}}]}
```

### G9-07 record 3

**form**: `(do (def r (ref 0)) (dosync (alter r inc)) @r)`  •  **expected**: `1`

```
All summer long, the Ant worked while the Grasshopper sang.

With a twig, Skip the grasshopper marked out a wager at the edge of the orchard: whoever
guessed the result of `(do (def r (ref 0)) (dosync (alter r inc)) @r)` first would win the right to
choose the next song. Bit the ant, saying very little, said it was easier
to ask the REPL about a ref incremented inside a dosync transaction than to argue.

Question: write a Clojure expression for the value of the ref after dosync alter inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 0)) (dosync (alter r inc)) @r)"}}]}
```

### G9-07 record 4

**form**: `(do (def r (ref 0)) (dosync (alter r inc)) @r)`  •  **expected**: `1`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Toc the ant kept a small ledger of state near the orchard — a value that might
change as the season went on. She explained that the form
`(do (def r (ref 0)) (dosync (alter r inc)) @r)` captured a ref incremented inside a dosync transaction: a careful, ordered update.
Hum the grasshopper, as if the race were already won, asked the REPL to confirm the final
value.

Write a form whose evaluation gives the value of the ref after dosync alter inc.

---

I bind the state, perform the update, then dereference.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 0)) (dosync (alter r inc)) @r)"}}]}
```

### G9-07 record 5

**form**: `(do (def r (ref 0)) (dosync (alter r inc)) @r)`  •  **expected**: `1`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. This was atop the hilltop.

"Why bother with all this?" Chirp the grasshopper demanded near the hilltop.
"He could just write the new value!" Toc the ant,
her eyes always on the path, sketched out a ref incremented inside a dosync transaction instead and showed the form
`(do (def r (ref 0)) (dosync (alter r inc)) @r)`: the proper way for the runtime to manage change. They
agreed to submit it to the REPL.

Question: write a Clojure expression for the value of the ref after dosync alter inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 0)) (dosync (alter r inc)) @r)"}}]}
```

## G9-08: dosync and alter

### G9-08 record 1

**form**: `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])`  •  **expected**: `[2, 3]`

```
Two creatures of the meadow approached the coming winter very differently. It happened on the hilltop.

At the edge of a stockpile atop the hilltop, Chirp the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])`
first would win the right to set the next day's count.
Tic the ant, without complaint, said it was simpler to type the form into
the REPL than to argue about two refs each incremented inside a single dosync.

What Clojure form computes the pair [a b] after the coordinated transaction? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])"}}]}
```

### G9-08 record 2

**form**: `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])`  •  **expected**: `[2, 3]`

```
Two creatures of the meadow approached the coming winter very differently. All this took place by the garden.

Skip the grasshopper chalked a wager on a flat slate by the garden: whoever
predicted the result of `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])` first would set the next day's
ration. Tic the ant, her eyes always on the path, said it would be simpler to type
the form into the REPL than to bicker about two refs each incremented inside a single dosync.

Question: write a Clojure expression for the pair [a b] after the coordinated transaction.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])"}}]}
```

### G9-08 record 3

**form**: `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])`  •  **expected**: `[2, 3]`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. This was at the edge of the forest.

With a twig, Hum the grasshopper marked out a wager in the forest: whoever
guessed the result of `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])` first would win the right to
choose the next song. Bit the ant, her eyes always on the path, said it was easier
to ask the REPL about two refs each incremented inside a single dosync than to argue.

Write a form whose evaluation gives the pair [a b] after the coordinated transaction.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])"}}]}
```

### G9-08 record 4

**form**: `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])`  •  **expected**: `[2, 3]`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Chirp the grasshopper chalked a wager on a flat slate near the farm: whoever
predicted the result of `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])` first would set the next day's
ration. Tic the ant, with steady, careful steps, said it would be simpler to type
the form into the REPL than to bicker about two refs each incremented inside a single dosync.

Question: write a Clojure expression for the pair [a b] after the coordinated transaction.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])"}}]}
```

### G9-08 record 5

**form**: `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])`  •  **expected**: `[2, 3]`

```
All summer long, the Ant worked while the Grasshopper sang.

Toc the ant kept a small ledger of state at the edge of the garden — a value that might
change as the season went on. She explained that the form
`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])` captured two refs each incremented inside a single dosync: a careful, ordered update.
Chirp the grasshopper, with a smug grin, asked the REPL to confirm the final
value.

Write a form whose evaluation gives the pair [a b] after the coordinated transaction.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])"}}]}
```

## G9-09: Ref vs atom

### G9-09 record 1

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

```
Two creatures of the meadow approached the coming winter very differently. All this took place in the forest.

Halfway through the morning's work, Chirp the grasshopper blocked
Tic the ant's path at the edge of the forest and refused to step aside until someone
could prove what the form `(do (def a (atom 0)) (swap! a inc) @a)` evaluated to. Chirp
called it impossible. Tic the ant, walking up at his usual
pace, simply said: "Submit an atom updated via swap! to the REPL. Whatever comes
back is the answer."

Write a Clojure expression that computes the value of the atom after one swap! inc.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
```

### G9-09 record 2

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

```
Two creatures of the meadow approached the coming winter very differently.

Toc the ant and Hum the grasshopper stopped at the edge of the meadow where someone had
written an atom updated via swap! on a flat stone. Hum, as if the race were already won,
declared that they could see the answer at a glance.
Toc, without complaint, suggested they actually evaluate the form
`(do (def a (atom 0)) (swap! a inc) @a)` in the REPL and read off whatever it returned.

Question: write a Clojure expression for the value of the atom after one swap! inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
```

### G9-09 record 3

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

```
All summer long, the Ant worked while the Grasshopper sang. This was by the farm.

Halfway through the morning's work, Skip the grasshopper blocked
Toc the ant's path in the farm and refused to step aside until someone
could prove what the form `(do (def a (atom 0)) (swap! a inc) @a)` evaluated to. Skip
called it impossible. Toc the ant, walking up at her usual
pace, simply said: "Submit an atom updated via swap! to the REPL. Whatever comes
back is the answer."

Write a form whose evaluation gives the value of the atom after one swap! inc.

---

I wrap the def, the update, and the deref together in a do block.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
```

### G9-09 record 4

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. It happened at the edge of the garden.

A wooden sign nailed to a stalk near the garden carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(do (def a (atom 0)) (swap! a inc) @a)`. Skip
laughed, as if the race were already won, and declared it too easy. Tic said patiently
that the only way to be sure of an atom updated via swap! was to put it in the
REPL.

Write a form whose evaluation gives the value of the atom after one swap! inc.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
```

### G9-09 record 5

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. It happened at the edge of the meadow.

With a twig, Hum the grasshopper marked out a wager near the meadow: whoever
guessed the result of `(do (def a (atom 0)) (swap! a inc) @a)` first would win the right to
choose the next song. Toc the ant, untroubled by what others thought, said it was easier
to ask the REPL about an atom updated via swap! than to argue.

What Clojure form computes the value of the atom after one swap! inc? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
```

## G9-10: Agent introduction

### G9-10 record 1

**form**: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`  •  **expected**: `1`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Bit the ant and Skip the grasshopper stopped near the woods where someone had
written an agent sent inc and awaited on a flat stone. Skip, boasting at every turn,
declared that she could see the answer at a glance.
Bit, with steady, careful steps, suggested they actually evaluate the form
`(do (def ag (agent 0)) (send ag inc) (await ag) @ag)` in the REPL and read off whatever it returned.

What Clojure form computes the value of the agent after send inc and await? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

### G9-10 record 2

**form**: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`  •  **expected**: `1`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Chirp the grasshopper chalked a wager on a flat slate at the edge of the garden: whoever
predicted the result of `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)` first would set the next day's
ration. Tic the ant, her eyes always on the path, said it would be simpler to type
the form into the REPL than to bicker about an agent sent inc and awaited.

Write a form whose evaluation gives the value of the agent after send inc and await.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

### G9-10 record 3

**form**: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`  •  **expected**: `1`

```
All summer long, the Ant worked while the Grasshopper sang.

"There is no need to evaluate that," Chirp the grasshopper said,
with a smug grin. "Anyone can see what an agent sent inc and awaited comes to."
Toc the ant, who by the garden had grown used to such claims, asked
him to actually write the form `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)` and
submit it to the REPL — just to be sure.

Write a form whose evaluation gives the value of the agent after send inc and await.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

### G9-10 record 4

**form**: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`  •  **expected**: `1`

```
Two creatures of the meadow approached the coming winter very differently. This was at the edge of the farm.

A small audience of meadow creatures had gathered in the farm to watch
Skip the grasshopper attempt to outwit Bit the ant at reading the
REPL. Bit pointed to an agent sent inc and awaited and read out the form aloud:
`(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`. The crowd waited to see who would correctly write the
form to submit.

Write a Clojure expression that computes the value of the agent after send inc and await.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

### G9-10 record 5

**form**: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`  •  **expected**: `1`

```
All summer long, the Ant worked while the Grasshopper sang. It happened at the edge of the farm.

A wooden sign nailed to a stalk in the farm carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`. Chirp
laughed, boasting at every turn, and declared it too easy. Bit said patiently
that the only way to be sure of an agent sent inc and awaited was to put it in the
REPL.

Write a Clojure expression that computes the value of the agent after send inc and await.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

## G9-11: send and send-off

### G9-11 record 1

**form**: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`  •  **expected**: `1`

```
Two creatures of the meadow approached the coming winter very differently. It happened in the meadow.

Halfway through the morning's work, Chirp the grasshopper blocked
Tic the ant's path in the meadow and refused to step aside until someone
could prove what the form `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)` evaluated to. Chirp
called it impossible. Tic the ant, walking up at his usual
pace, simply said: "Submit send used on an agent, then awaited to the REPL. Whatever comes
back is the answer."

Question: write a Clojure expression for the agent's value after send inc.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

### G9-11 record 2

**form**: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`  •  **expected**: `1`

```
Two creatures of the meadow approached the coming winter very differently. This was near the forest.

At the edge of a stockpile at the edge of the forest, Skip the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`
first would win the right to set the next day's count.
Toc the ant, with steady, careful steps, said it was simpler to type the form into
the REPL than to argue about send used on an agent, then awaited.

Write a form whose evaluation gives the agent's value after send inc.

---

I bind the state, perform the update, then dereference.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

### G9-11 record 3

**form**: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`  •  **expected**: `1`

```
Two creatures of the meadow approached the coming winter very differently. This was at the edge of the forest.

A wooden sign nailed to a stalk in the forest carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`. Skip
laughed, puffed up with pride, and declared it too easy. Bit said patiently
that the only way to be sure of send used on an agent, then awaited was to put it in the
REPL.

Question: write a Clojure expression for the agent's value after send inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

### G9-11 record 4

**form**: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`  •  **expected**: `1`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Tic the ant had been keeping a small leather notebook of every form
he had successfully evaluated. Today in the woods, the next entry
was send used on an agent, then awaited. Hum the grasshopper peered over
his shoulder at the form `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)` and asked what it
would come out to.

What Clojure form computes the agent's value after send inc? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

### G9-11 record 5

**form**: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`  •  **expected**: `1`

```
All summer long, the Ant worked while the Grasshopper sang.

A wooden sign nailed to a stalk by the garden carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`. Skip
laughed, swaggering through the underbrush, and declared it too easy. Bit said patiently
that the only way to be sure of send used on an agent, then awaited was to put it in the
REPL.

Write a form whose evaluation gives the agent's value after send inc.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

## G9-12: await — synchronizing on agents

### G9-12 record 1

**form**: `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)`  •  **expected**: `2`

```
Two creatures of the meadow approached the coming winter very differently.

At the edge of a stockpile atop the hilltop, Skip the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)`
first would win the right to set the next day's count.
Toc the ant, stepping deliberately, said it was simpler to type the form into
the REPL than to argue about two send inc calls then await before deref.

Write a form whose evaluation gives the agent's value after two sends and await.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)"}}]}
```

### G9-12 record 2

**form**: `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)`  •  **expected**: `2`

```
Two creatures of the meadow approached the coming winter very differently.

Bit the ant kept a small ledger of state at the edge of the garden — a value that might
change as the season went on. They explained that the form
`(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)` captured two send inc calls then await before deref: a careful, ordered update.
Hum the grasshopper, puffed up with pride, asked the REPL to confirm the final
value.

Write a form whose evaluation gives the agent's value after two sends and await.

---

I let the runtime mediate the change before reading the final value.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)"}}]}
```

### G9-12 record 3

**form**: `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)`  •  **expected**: `2`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. It happened at the edge of the woods.

A wooden sign nailed to a stalk in the woods carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)`. Hum
laughed, with great whoops of laughter, and declared it too easy. Toc said patiently
that the only way to be sure of two send inc calls then await before deref was to put it in the
REPL.

Write a form whose evaluation gives the agent's value after two sends and await.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)"}}]}
```

### G9-12 record 4

**form**: `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)`  •  **expected**: `2`

```
Two creatures of the meadow approached the coming winter very differently.

A wooden sign nailed to a stalk in the garden carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)`. Skip
laughed, with great whoops of laughter, and declared it too easy. Tic said patiently
that the only way to be sure of two send inc calls then await before deref was to put it in the
REPL.

Write a Clojure expression that computes the agent's value after two sends and await.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)"}}]}
```

### G9-12 record 5

**form**: `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)`  •  **expected**: `2`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. It happened near the forest.

Halfway through the morning's work, Chirp the grasshopper blocked
Toc the ant's path at the edge of the forest and refused to step aside until someone
could prove what the form `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)` evaluated to. Chirp
called it impossible. Toc the ant, walking up at her usual
pace, simply said: "Submit two send inc calls then await before deref to the REPL. Whatever comes
back is the answer."

Write a Clojure expression that computes the agent's value after two sends and await.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)"}}]}
```

## G9-13: future introduction

### G9-13 record 1

**form**: `@(future (+ 1 2))`  •  **expected**: `3`

```
Two creatures of the meadow approached the coming winter very differently.

At the edge of a stockpile at the edge of the orchard, Hum the grasshopper sketched a
small wager into the dust: whoever guessed the result of `@(future (+ 1 2))`
first would win the right to set the next day's count.
Toc the ant, with steady, careful steps, said it was simpler to type the form into
the REPL than to argue about a future computing (+ 1 2), dereferenced.

Write a form whose evaluation gives the value of the future for (+ 1 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"@(future (+ 1 2))"}}]}
```

### G9-13 record 2

**form**: `@(future (+ 1 2))`  •  **expected**: `3`

```
Two creatures of the meadow approached the coming winter very differently.

A wooden sign nailed to a stalk by the farm carried a puzzle. The riddle
was simple: it asked the reader to evaluate `@(future (+ 1 2))`. Chirp
laughed, swaggering through the underbrush, and declared it too easy. Tic said patiently
that the only way to be sure of a future computing (+ 1 2), dereferenced was to put it in the
REPL.

Write a Clojure expression that computes the value of the future for (+ 1 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"@(future (+ 1 2))"}}]}
```

### G9-13 record 3

**form**: `@(future (+ 1 2))`  •  **expected**: `3`

```
All summer long, the Ant worked while the Grasshopper sang. It happened atop the hilltop.

Tic the ant had been keeping a small leather notebook of every form
he had successfully evaluated. Today on the hilltop, the next entry
was a future computing (+ 1 2), dereferenced. Chirp the grasshopper peered over
his shoulder at the form `@(future (+ 1 2))` and asked what it
would come out to.

Write a Clojure expression that computes the value of the future for (+ 1 2).

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"@(future (+ 1 2))"}}]}
```

### G9-13 record 4

**form**: `@(future (+ 1 2))`  •  **expected**: `3`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Chirp the grasshopper chalked a wager on a flat slate by the farm: whoever
predicted the result of `@(future (+ 1 2))` first would set the next day's
ration. Tic the ant, without complaint, said it would be simpler to type
the form into the REPL than to bicker about a future computing (+ 1 2), dereferenced.

What Clojure form computes the value of the future for (+ 1 2)? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"@(future (+ 1 2))"}}]}
```

### G9-13 record 5

**form**: `@(future (+ 1 2))`  •  **expected**: `3`

```
Two creatures of the meadow approached the coming winter very differently. All this took place in the forest.

A small audience of meadow creatures had gathered in the forest to watch
Chirp the grasshopper attempt to outwit Bit the ant at reading the
REPL. Bit pointed to a future computing (+ 1 2), dereferenced and read out the form aloud:
`@(future (+ 1 2))`. The crowd waited to see who would correctly write the
form to submit.

Question: write a Clojure expression for the value of the future for (+ 1 2).

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"@(future (+ 1 2))"}}]}
```

## G9-14: deref @ shorthand

### G9-14 record 1

**form**: `(do (def a (atom 7)) @a)`  •  **expected**: `7`

```
Two creatures of the meadow approached the coming winter very differently.

Toc the ant had been trying to teach Skip the grasshopper how the REPL
works. "Look here," she said, pointing to deref via @ on an atom holding 7.
"You hand the form `(do (def a (atom 7)) @a)` to the runtime, and the runtime hands
you back what it evaluates to." Skip, lulled by the gentle wind, agreed to
try.

Write a Clojure expression that computes the value of the atom via @.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 7)) @a)"}}]}
```

### G9-14 record 2

**form**: `(do (def a (atom 7)) @a)`  •  **expected**: `7`

```
Two creatures of the meadow approached the coming winter very differently.

At the edge of a stockpile by the woods, Hum the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(do (def a (atom 7)) @a)`
first would win the right to set the next day's count.
Toc the ant, without complaint, said it was simpler to type the form into
the REPL than to argue about deref via @ on an atom holding 7.

Write a form whose evaluation gives the value of the atom via @.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 7)) @a)"}}]}
```

### G9-14 record 3

**form**: `(do (def a (atom 7)) @a)`  •  **expected**: `7`

```
All summer long, the Ant worked while the Grasshopper sang.

Hum the grasshopper chalked a wager on a flat slate at the edge of the hilltop: whoever
predicted the result of `(do (def a (atom 7)) @a)` first would set the next day's
ration. Bit the ant, stepping deliberately, said it would be simpler to type
the form into the REPL than to bicker about deref via @ on an atom holding 7.

What Clojure form computes the value of the atom via @? Submit it via `eval`.

---

I let the runtime mediate the change before reading the final value.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 7)) @a)"}}]}
```

### G9-14 record 4

**form**: `(do (def a (atom 7)) @a)`  •  **expected**: `7`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Chirp the grasshopper chalked a wager on a flat slate at the edge of the farm: whoever
predicted the result of `(do (def a (atom 7)) @a)` first would set the next day's
ration. Tic the ant, saying very little, said it would be simpler to type
the form into the REPL than to bicker about deref via @ on an atom holding 7.

Write a form whose evaluation gives the value of the atom via @.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 7)) @a)"}}]}
```

### G9-14 record 5

**form**: `(do (def a (atom 7)) @a)`  •  **expected**: `7`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

"There is no need to evaluate that," Chirp the grasshopper said,
puffed up with pride. "Anyone can see what deref via @ on an atom holding 7 comes to."
Toc the ant, who near the hilltop had grown used to such claims, asked
him to actually write the form `(do (def a (atom 7)) @a)` and
submit it to the REPL — just to be sure.

Write a Clojure expression that computes the value of the atom via @.

---

I bind the state, perform the update, then dereference.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 7)) @a)"}}]}
```

## G9-15: promise — deliver and deref

### G9-15 record 1

**form**: `(do (def p (promise)) (deliver p :done) @p)`  •  **expected**: `':done'`

```
Two creatures of the meadow approached the coming winter very differently.

Bit the ant kept a small ledger of state near the meadow — a value that might
change as the season went on. They explained that the form
`(do (def p (promise)) (deliver p :done) @p)` captured a promise delivered with :done, then dereffed: a careful, ordered update.
Skip the grasshopper, with great whoops of laughter, asked the REPL to confirm the final
value.

Write a form whose evaluation gives the value of the promise after deliver.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def p (promise)) (deliver p :done) @p)"}}]}
```

### G9-15 record 2

**form**: `(do (def p (promise)) (deliver p :done) @p)`  •  **expected**: `':done'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Hum the grasshopper chalked a wager on a flat slate by the garden: whoever
predicted the result of `(do (def p (promise)) (deliver p :done) @p)` first would set the next day's
ration. Toc the ant, her eyes always on the path, said it would be simpler to type
the form into the REPL than to bicker about a promise delivered with :done, then dereffed.

Write a form whose evaluation gives the value of the promise after deliver.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def p (promise)) (deliver p :done) @p)"}}]}
```

### G9-15 record 3

**form**: `(do (def p (promise)) (deliver p :done) @p)`  •  **expected**: `':done'`

```
Two creatures of the meadow approached the coming winter very differently.

With a twig, Hum the grasshopper marked out a wager near the meadow: whoever
guessed the result of `(do (def p (promise)) (deliver p :done) @p)` first would win the right to
choose the next song. Bit the ant, with steady, careful steps, said it was easier
to ask the REPL about a promise delivered with :done, then dereffed than to argue.

Write a form whose evaluation gives the value of the promise after deliver.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def p (promise)) (deliver p :done) @p)"}}]}
```

### G9-15 record 4

**form**: `(do (def p (promise)) (deliver p :done) @p)`  •  **expected**: `':done'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Tic the ant had been trying to teach Hum the grasshopper how the REPL
works. "Look here," he said, pointing to a promise delivered with :done, then dereffed.
"You hand the form `(do (def p (promise)) (deliver p :done) @p)` to the runtime, and the runtime hands
you back what it evaluates to." Hum, yawning at the soft moss, agreed to
try.

Question: write a Clojure expression for the value of the promise after deliver.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def p (promise)) (deliver p :done) @p)"}}]}
```

### G9-15 record 5

**form**: `(do (def p (promise)) (deliver p :done) @p)`  •  **expected**: `':done'`

```
Two creatures of the meadow approached the coming winter very differently. All this took place at the edge of the garden.

Toc the ant and Skip the grasshopper stopped in the garden where someone had
written a promise delivered with :done, then dereffed on a flat stone. Skip, with a smug grin,
declared that she could see the answer at a glance.
Toc, with steady, careful steps, suggested they actually evaluate the form
`(do (def p (promise)) (deliver p :done) @p)` in the REPL and read off whatever it returned.

Write a Clojure expression that computes the value of the promise after deliver.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def p (promise)) (deliver p :done) @p)"}}]}
```

## G9-16: volatile — when STM is too heavy

### G9-16 record 1

**form**: `(do (def v (volatile! 0)) (vswap! v inc) @v)`  •  **expected**: `1`

```
Two creatures of the meadow approached the coming winter very differently. All this took place at the edge of the farm.

"There is no need to evaluate that," Hum the grasshopper said,
as if the race were already won. "Anyone can see what a volatile! incremented via vswap! comes to."
Toc the ant, who by the farm had grown used to such claims, asked
them to actually write the form `(do (def v (volatile! 0)) (vswap! v inc) @v)` and
submit it to the REPL — just to be sure.

Write a form whose evaluation gives the value of the volatile after one vswap! inc.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def v (volatile! 0)) (vswap! v inc) @v)"}}]}
```

### G9-16 record 2

**form**: `(do (def v (volatile! 0)) (vswap! v inc) @v)`  •  **expected**: `1`

```
All summer long, the Ant worked while the Grasshopper sang.

Hum the grasshopper chalked a wager on a flat slate in the woods: whoever
predicted the result of `(do (def v (volatile! 0)) (vswap! v inc) @v)` first would set the next day's
ration. Tic the ant, her eyes always on the path, said it would be simpler to type
the form into the REPL than to bicker about a volatile! incremented via vswap!.

What Clojure form computes the value of the volatile after one vswap! inc? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def v (volatile! 0)) (vswap! v inc) @v)"}}]}
```

### G9-16 record 3

**form**: `(do (def v (volatile! 0)) (vswap! v inc) @v)`  •  **expected**: `1`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. All this took place by the woods.

"There is no need to evaluate that," Chirp the grasshopper said,
with a smug grin. "Anyone can see what a volatile! incremented via vswap! comes to."
Tic the ant, who by the woods had grown used to such claims, asked
him to actually write the form `(do (def v (volatile! 0)) (vswap! v inc) @v)` and
submit it to the REPL — just to be sure.

Write a form whose evaluation gives the value of the volatile after one vswap! inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def v (volatile! 0)) (vswap! v inc) @v)"}}]}
```

### G9-16 record 4

**form**: `(do (def v (volatile! 0)) (vswap! v inc) @v)`  •  **expected**: `1`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

A wooden sign nailed to a stalk near the forest carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(do (def v (volatile! 0)) (vswap! v inc) @v)`. Chirp
laughed, boasting at every turn, and declared it too easy. Bit said patiently
that the only way to be sure of a volatile! incremented via vswap! was to put it in the
REPL.

Write a Clojure expression that computes the value of the volatile after one vswap! inc.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def v (volatile! 0)) (vswap! v inc) @v)"}}]}
```

### G9-16 record 5

**form**: `(do (def v (volatile! 0)) (vswap! v inc) @v)`  •  **expected**: `1`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. All this took place near the garden.

"There is no need to evaluate that," Skip the grasshopper said,
swaggering through the underbrush. "Anyone can see what a volatile! incremented via vswap! comes to."
Bit the ant, who at the edge of the garden had grown used to such claims, asked
her to actually write the form `(do (def v (volatile! 0)) (vswap! v inc) @v)` and
submit it to the REPL — just to be sure.

Write a form whose evaluation gives the value of the volatile after one vswap! inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def v (volatile! 0)) (vswap! v inc) @v)"}}]}
```

## G9-17: binding — thread-local

### G9-17 record 1

**form**: `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))`  •  **expected**: `99`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. All this took place by the meadow.

"There is no need to evaluate that," Skip the grasshopper said,
with a smug grin. "Anyone can see what a dynamic var *p* rebound to 99 inside binding comes to."
Tic the ant, who in the meadow had grown used to such claims, asked
her to actually write the form `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` and
submit it to the REPL — just to be sure.

Question: write a Clojure expression for the value of *p* inside the binding form.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))"}}]}
```

### G9-17 record 2

**form**: `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))`  •  **expected**: `99`

```
Two creatures of the meadow approached the coming winter very differently. All this took place in the forest.

"Why bother with all this?" Hum the grasshopper demanded near the forest.
"They could just write the new value!" Bit the ant,
stepping deliberately, sketched out a dynamic var *p* rebound to 99 inside binding instead and showed the form
`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))`: the proper way for the runtime to manage change. They
agreed to submit it to the REPL.

Write a form whose evaluation gives the value of *p* inside the binding form.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))"}}]}
```

### G9-17 record 3

**form**: `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))`  •  **expected**: `99`

```
All summer long, the Ant worked while the Grasshopper sang. It happened in the orchard.

Toc the ant and Hum the grasshopper stopped in the orchard where someone had
written a dynamic var *p* rebound to 99 inside binding on a flat stone. Hum, with great whoops of laughter,
declared that they could see the answer at a glance.
Toc, saying very little, suggested they actually evaluate the form
`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` in the REPL and read off whatever it returned.

Question: write a Clojure expression for the value of *p* inside the binding form.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))"}}]}
```

### G9-17 record 4

**form**: `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))`  •  **expected**: `99`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

A wooden sign nailed to a stalk in the garden carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))`. Chirp
laughed, puffed up with pride, and declared it too easy. Toc said patiently
that the only way to be sure of a dynamic var *p* rebound to 99 inside binding was to put it in the
REPL.

Write a Clojure expression that computes the value of *p* inside the binding form.

---

I let the runtime mediate the change before reading the final value.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))"}}]}
```

### G9-17 record 5

**form**: `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))`  •  **expected**: `99`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Toc the ant kept a small ledger of state by the farm — a value that might
change as the season went on. She explained that the form
`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` captured a dynamic var *p* rebound to 99 inside binding: a careful, ordered update.
Hum the grasshopper, boasting at every turn, asked the REPL to confirm the final
value.

What Clojure form computes the value of *p* inside the binding form? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))"}}]}
```

## G9-18: locking — last resort

### G9-18 record 1

**form**: `(do (def lock (Object.)) (locking lock (+ 1 2)))`  •  **expected**: `3`

```
All summer long, the Ant worked while the Grasshopper sang.

"Why bother with all this?" Skip the grasshopper demanded by the farm.
"She could just write the new value!" Toc the ant,
with steady, careful steps, sketched out a locking form around (+ 1 2) using a fresh Object as monitor instead and showed the form
`(do (def lock (Object.)) (locking lock (+ 1 2)))`: the proper way for the runtime to manage change. They
agreed to submit it to the REPL.

What Clojure form computes the result of the body inside locking? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def lock (Object.)) (locking lock (+ 1 2)))"}}]}
```

### G9-18 record 2

**form**: `(do (def lock (Object.)) (locking lock (+ 1 2)))`  •  **expected**: `3`

```
All summer long, the Ant worked while the Grasshopper sang. All this took place near the farm.

With a twig, Hum the grasshopper marked out a wager at the edge of the farm: whoever
guessed the result of `(do (def lock (Object.)) (locking lock (+ 1 2)))` first would win the right to
choose the next song. Bit the ant, with steady, careful steps, said it was easier
to ask the REPL about a locking form around (+ 1 2) using a fresh Object as monitor than to argue.

Write a form whose evaluation gives the result of the body inside locking.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def lock (Object.)) (locking lock (+ 1 2)))"}}]}
```

### G9-18 record 3

**form**: `(do (def lock (Object.)) (locking lock (+ 1 2)))`  •  **expected**: `3`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

"There is no need to evaluate that," Hum the grasshopper said,
as if the race were already won. "Anyone can see what a locking form around (+ 1 2) using a fresh Object as monitor comes to."
Toc the ant, who in the farm had grown used to such claims, asked
them to actually write the form `(do (def lock (Object.)) (locking lock (+ 1 2)))` and
submit it to the REPL — just to be sure.

Write a Clojure expression that computes the result of the body inside locking.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def lock (Object.)) (locking lock (+ 1 2)))"}}]}
```

### G9-18 record 4

**form**: `(do (def lock (Object.)) (locking lock (+ 1 2)))`  •  **expected**: `3`

```
All summer long, the Ant worked while the Grasshopper sang.

Tic the ant had been trying to teach Skip the grasshopper how the REPL
works. "Look here," he said, pointing to a locking form around (+ 1 2) using a fresh Object as monitor.
"You hand the form `(do (def lock (Object.)) (locking lock (+ 1 2)))` to the runtime, and the runtime hands
you back what it evaluates to." Skip, yawning at the soft moss, agreed to
try.

Question: write a Clojure expression for the result of the body inside locking.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def lock (Object.)) (locking lock (+ 1 2)))"}}]}
```

### G9-18 record 5

**form**: `(do (def lock (Object.)) (locking lock (+ 1 2)))`  •  **expected**: `3`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. All this took place in the garden.

Halfway through the morning's work, Hum the grasshopper blocked
Toc the ant's path near the garden and refused to step aside until someone
could prove what the form `(do (def lock (Object.)) (locking lock (+ 1 2)))` evaluated to. Hum
called it impossible. Toc the ant, walking up at her usual
pace, simply said: "Submit a locking form around (+ 1 2) using a fresh Object as monitor to the REPL. Whatever comes
back is the answer."

Write a form whose evaluation gives the result of the body inside locking.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def lock (Object.)) (locking lock (+ 1 2)))"}}]}
```


---

**Grade 9 totals: 18 subjects, 90 records.**
