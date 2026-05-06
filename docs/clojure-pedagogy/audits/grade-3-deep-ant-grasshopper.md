# Deep spot-check: grade 3 ant-grasshopper (5 records per subject)

Manual-review dump for hand-audit. Each subject gets 5 rendered records sampled across different seeds so subplot/character/location variety is visible.

---

## G3-01: def — top-level binding

### G3-01 record 1

**form**: `(do (def x 42) x)`  •  **expected**: `42`

```
Two creatures of the meadow approached the coming winter very differently.

Toc the ant had been keeping a small leather notebook of every form
she had successfully evaluated. Today atop the hilltop, the next entry
was the binding (def x 42) followed by x. Skip the grasshopper peered over
her shoulder at the form `(do (def x 42) x)` and asked what it
would come out to.

What Clojure form computes the value bound to x after (def x 42)? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 42) x)"}}]}
```

### G3-01 record 2

**form**: `(do (def x 42) x)`  •  **expected**: `42`

```
Two creatures of the meadow approached the coming winter very differently. It happened in the farm.

Bit the ant had been trying to teach Hum the grasshopper how the REPL
works. "Look here," they said, pointing to the binding (def x 42) followed by x.
"You hand the form `(do (def x 42) x)` to the runtime, and the runtime hands
you back what it evaluates to." Hum, lulled by the gentle wind, agreed to
try.

Write a form whose evaluation gives the value bound to x after (def x 42).

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 42) x)"}}]}
```

### G3-01 record 3

**form**: `(do (def x 42) x)`  •  **expected**: `42`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Skip the grasshopper chalked a wager on a flat slate on the hilltop: whoever
predicted the result of `(do (def x 42) x)` first would set the next day's
ration. Bit the ant, untroubled by what others thought, said it would be simpler to type
the form into the REPL than to bicker about the binding (def x 42) followed by x.

Write a form whose evaluation gives the value bound to x after (def x 42).

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 42) x)"}}]}
```

### G3-01 record 4

**form**: `(do (def x 42) x)`  •  **expected**: `42`

```
All summer long, the Ant worked while the Grasshopper sang.

Bit the ant kept a small stockpile-ledger by the orchard where every meaningful
quantity got its own name. They pointed to today's
entry: the binding (def x 42) followed by x. The form `(do (def x 42) x)` would settle it once
Skip the grasshopper agreed to look at the binding.

Write a form whose evaluation gives the value bound to x after (def x 42).

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 42) x)"}}]}
```

### G3-01 record 5

**form**: `(do (def x 42) x)`  •  **expected**: `42`

```
Two creatures of the meadow approached the coming winter very differently.

Toc the ant had been trying to teach Skip the grasshopper how the REPL
works. "Look here," she said, pointing to the binding (def x 42) followed by x.
"You hand the form `(do (def x 42) x)` to the runtime, and the runtime hands
you back what it evaluates to." Skip, her legs heavy from sprinting, agreed to
try.

Question: write a Clojure expression for the value bound to x after (def x 42).

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 42) x)"}}]}
```

## G3-02: def — redefinition

### G3-02 record 1

**form**: `(do (def x 1) (def x 99) x)`  •  **expected**: `99`

```
Two creatures of the meadow approached the coming winter very differently.

Halfway through the morning's work, Chirp the grasshopper blocked
Bit the ant's path atop the hilltop and refused to step aside until someone
could prove what the form `(do (def x 1) (def x 99) x)` evaluated to. Chirp
called it impossible. Bit the ant, walking up at their usual
pace, simply said: "Submit the redefined x to the REPL. Whatever comes
back is the answer."

Question: write a Clojure expression for the value of x after redefinition.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 1) (def x 99) x)"}}]}
```

### G3-02 record 2

**form**: `(do (def x 1) (def x 99) x)`  •  **expected**: `99`

```
Two creatures of the meadow approached the coming winter very differently.

With a twig, Chirp the grasshopper marked out a wager atop the hilltop: whoever
guessed the result of `(do (def x 1) (def x 99) x)` first would win the right to
choose the next song. Bit the ant, untroubled by what others thought, said it was easier
to ask the REPL about the redefined x than to argue.

What Clojure form computes the value of x after redefinition? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 1) (def x 99) x)"}}]}
```

### G3-02 record 3

**form**: `(do (def x 1) (def x 99) x)`  •  **expected**: `99`

```
All summer long, the Ant worked while the Grasshopper sang. This was near the orchard.

Toc the ant kept a small stockpile-ledger by the orchard where every meaningful
quantity got its own name. She pointed to today's
entry: the redefined x. The form `(do (def x 1) (def x 99) x)` would settle it once
Hum the grasshopper agreed to look at the binding.

Write a Clojure expression that computes the value of x after redefinition.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 1) (def x 99) x)"}}]}
```

### G3-02 record 4

**form**: `(do (def x 1) (def x 99) x)`  •  **expected**: `99`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

With a twig, Chirp the grasshopper marked out a wager by the garden: whoever
guessed the result of `(do (def x 1) (def x 99) x)` first would win the right to
choose the next song. Toc the ant, untroubled by what others thought, said it was easier
to ask the REPL about the redefined x than to argue.

Write a Clojure expression that computes the value of x after redefinition.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 1) (def x 99) x)"}}]}
```

### G3-02 record 5

**form**: `(do (def x 1) (def x 99) x)`  •  **expected**: `99`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

"You can call it whatever you like," Tic said by the orchard, "but the
form is what matters." He drew the binding for
Skip the grasshopper: the form `(do (def x 1) (def x 99) x)` captured the redefined x, and
the REPL would do the rest.

Write a Clojure expression that computes the value of x after redefinition.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 1) (def x 99) x)"}}]}
```

## G3-03: let — local binding

### G3-03 record 1

**form**: `(let [x 3] (+ x 1))`  •  **expected**: `4`

```
All summer long, the Ant worked while the Grasshopper sang. All this took place at the edge of the garden.

Tic the ant had been trying to teach Skip the grasshopper how the REPL
works. "Look here," he said, pointing to the form (let [x 3] (+ x 1)).
"You hand the form `(let [x 3] (+ x 1))` to the runtime, and the runtime hands
you back what it evaluates to." Skip, drowsy from the warm sun, agreed to
try.

Question: write a Clojure expression for the result of (let [x 3] (+ x 1)).

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
```

### G3-03 record 2

**form**: `(let [x 3] (+ x 1))`  •  **expected**: `4`

```
Two creatures of the meadow approached the coming winter very differently.

At the edge of a stockpile in the meadow, Skip the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(let [x 3] (+ x 1))`
first would win the right to set the next day's count.
Tic the ant, without complaint, said it was simpler to type the form into
the REPL than to argue about the form (let [x 3] (+ x 1)).

What Clojure form computes the result of (let [x 3] (+ x 1))? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
```

### G3-03 record 3

**form**: `(let [x 3] (+ x 1))`  •  **expected**: `4`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Halfway through the morning's work, Chirp the grasshopper blocked
Bit the ant's path by the garden and refused to step aside until someone
could prove what the form `(let [x 3] (+ x 1))` evaluated to. Chirp
called it impossible. Bit the ant, walking up at their usual
pace, simply said: "Submit the form (let [x 3] (+ x 1)) to the REPL. Whatever comes
back is the answer."

What Clojure form computes the result of (let [x 3] (+ x 1))? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
```

### G3-03 record 4

**form**: `(let [x 3] (+ x 1))`  •  **expected**: `4`

```
Two creatures of the meadow approached the coming winter very differently. It happened by the orchard.

A wooden sign nailed to a stalk in the orchard carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(let [x 3] (+ x 1))`. Skip
laughed, swaggering through the underbrush, and declared it too easy. Toc said patiently
that the only way to be sure of the form (let [x 3] (+ x 1)) was to put it in the
REPL.

Write a Clojure expression that computes the result of (let [x 3] (+ x 1)).

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
```

### G3-03 record 5

**form**: `(let [x 3] (+ x 1))`  •  **expected**: `4`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Tic the ant had been trying to teach Chirp the grasshopper how the REPL
works. "Look here," he said, pointing to the form (let [x 3] (+ x 1)).
"You hand the form `(let [x 3] (+ x 1))` to the runtime, and the runtime hands
you back what it evaluates to." Chirp, lulled by the gentle wind, agreed to
try.

What Clojure form computes the result of (let [x 3] (+ x 1))? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
```

## G3-04: let — multi-binding

### G3-04 record 1

**form**: `(let [a 1 b 2] (+ a b))`  •  **expected**: `3`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Toc the ant had been trying to teach Chirp the grasshopper how the REPL
works. "Look here," she said, pointing to the form with two bindings.
"You hand the form `(let [a 1 b 2] (+ a b))` to the runtime, and the runtime hands
you back what it evaluates to." Chirp, her legs heavy from sprinting, agreed to
try.

Write a Clojure expression that computes the result of (let [a 1 b 2] (+ a b)).

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 1 b 2] (+ a b))"}}]}
```

### G3-04 record 2

**form**: `(let [a 1 b 2] (+ a b))`  •  **expected**: `3`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. This was on the hilltop.

Tic the ant had been trying to teach Chirp the grasshopper how the REPL
works. "Look here," he said, pointing to the form with two bindings.
"You hand the form `(let [a 1 b 2] (+ a b))` to the runtime, and the runtime hands
you back what it evaluates to." Chirp, yawning at the soft moss, agreed to
try.

Write a Clojure expression that computes the result of (let [a 1 b 2] (+ a b)).

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 1 b 2] (+ a b))"}}]}
```

### G3-04 record 3

**form**: `(let [a 1 b 2] (+ a b))`  •  **expected**: `3`

```
Two creatures of the meadow approached the coming winter very differently.

With a twig, Skip the grasshopper marked out a wager in the garden: whoever
guessed the result of `(let [a 1 b 2] (+ a b))` first would win the right to
choose the next song. Tic the ant, her eyes always on the path, said it was easier
to ask the REPL about the form with two bindings than to argue.

What Clojure form computes the result of (let [a 1 b 2] (+ a b))? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 1 b 2] (+ a b))"}}]}
```

### G3-04 record 4

**form**: `(let [a 1 b 2] (+ a b))`  •  **expected**: `3`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

A small audience of meadow creatures had gathered in the orchard to watch
Chirp the grasshopper attempt to outwit Toc the ant at reading the
REPL. Toc pointed to the form with two bindings and read out the form aloud:
`(let [a 1 b 2] (+ a b))`. The crowd waited to see who would correctly write the
form to submit.

Write a Clojure expression that computes the result of (let [a 1 b 2] (+ a b)).

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 1 b 2] (+ a b))"}}]}
```

### G3-04 record 5

**form**: `(let [a 1 b 2] (+ a b))`  •  **expected**: `3`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. All this took place in the orchard.

A wooden sign nailed to a stalk by the orchard carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(let [a 1 b 2] (+ a b))`. Skip
laughed, puffed up with pride, and declared it too easy. Toc said patiently
that the only way to be sure of the form with two bindings was to put it in the
REPL.

Write a Clojure expression that computes the result of (let [a 1 b 2] (+ a b)).

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 1 b 2] (+ a b))"}}]}
```

## G3-05: let — shadowing outer def

### G3-05 record 1

**form**: `(do (def x 10) (let [x 99] x))`  •  **expected**: `99`

```
Two creatures of the meadow approached the coming winter very differently.

Halfway through the morning's work, Skip the grasshopper blocked
Toc the ant's path at the edge of the woods and refused to step aside until someone
could prove what the form `(do (def x 10) (let [x 99] x))` evaluated to. Skip
called it impossible. Toc the ant, walking up at her usual
pace, simply said: "Submit an inner let shadowing the outer def to the REPL. Whatever comes
back is the answer."

Write a form whose evaluation gives the inner-let value of x.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 10) (let [x 99] x))"}}]}
```

### G3-05 record 2

**form**: `(do (def x 10) (let [x 99] x))`  •  **expected**: `99`

```
Two creatures of the meadow approached the coming winter very differently. All this took place atop the hilltop.

"There is no need to evaluate that," Hum the grasshopper said,
with great whoops of laughter. "Anyone can see what an inner let shadowing the outer def comes to."
Tic the ant, who atop the hilltop had grown used to such claims, asked
them to actually write the form `(do (def x 10) (let [x 99] x))` and
submit it to the REPL — just to be sure.

Question: write a Clojure expression for the inner-let value of x.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 10) (let [x 99] x))"}}]}
```

### G3-05 record 3

**form**: `(do (def x 10) (let [x 99] x))`  •  **expected**: `99`

```
Two creatures of the meadow approached the coming winter very differently. This was near the woods.

Tic the ant and Skip the grasshopper stopped in the woods where someone had
written an inner let shadowing the outer def on a flat stone. Skip, swaggering through the underbrush,
declared that she could see the answer at a glance.
Tic, her eyes always on the path, suggested they actually evaluate the form
`(do (def x 10) (let [x 99] x))` in the REPL and read off whatever it returned.

What Clojure form computes the inner-let value of x? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 10) (let [x 99] x))"}}]}
```

### G3-05 record 4

**form**: `(do (def x 10) (let [x 99] x))`  •  **expected**: `99`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

A wooden sign nailed to a stalk at the edge of the farm carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(do (def x 10) (let [x 99] x))`. Hum
laughed, swaggering through the underbrush, and declared it too easy. Tic said patiently
that the only way to be sure of an inner let shadowing the outer def was to put it in the
REPL.

Write a Clojure expression that computes the inner-let value of x.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 10) (let [x 99] x))"}}]}
```

### G3-05 record 5

**form**: `(do (def x 10) (let [x 99] x))`  •  **expected**: `99`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

At the edge of a stockpile atop the hilltop, Hum the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(do (def x 10) (let [x 99] x))`
first would win the right to set the next day's count.
Toc the ant, her eyes always on the path, said it was simpler to type the form into
the REPL than to argue about an inner let shadowing the outer def.

What Clojure form computes the inner-let value of x? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 10) (let [x 99] x))"}}]}
```

## G3-06: let — binding can reference prior

### G3-06 record 1

**form**: `(let [a 5 b (* a 2)] b)`  •  **expected**: `10`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Tic the ant kept a small stockpile-ledger near the woods where every meaningful
quantity got its own name. He pointed to today's
entry: a let where b uses a. The form `(let [a 5 b (* a 2)] b)` would settle it once
Chirp the grasshopper agreed to look at the binding.

Write a form whose evaluation gives the value of b when a=5 and b is (* a 2).

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 5 b (* a 2)] b)"}}]}
```

### G3-06 record 2

**form**: `(let [a 5 b (* a 2)] b)`  •  **expected**: `10`

```
All summer long, the Ant worked while the Grasshopper sang. This was near the orchard.

Halfway through the morning's work, Hum the grasshopper blocked
Tic the ant's path by the orchard and refused to step aside until someone
could prove what the form `(let [a 5 b (* a 2)] b)` evaluated to. Hum
called it impossible. Tic the ant, walking up at his usual
pace, simply said: "Submit a let where b uses a to the REPL. Whatever comes
back is the answer."

Write a Clojure expression that computes the value of b when a=5 and b is (* a 2).

---

I name the values first and then combine them.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 5 b (* a 2)] b)"}}]}
```

### G3-06 record 3

**form**: `(let [a 5 b (* a 2)] b)`  •  **expected**: `10`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

"You can call it whatever you like," Toc said in the orchard, "but the
form is what matters." She drew the binding for
Hum the grasshopper: the form `(let [a 5 b (* a 2)] b)` captured a let where b uses a, and
the REPL would do the rest.

Write a Clojure expression that computes the value of b when a=5 and b is (* a 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 5 b (* a 2)] b)"}}]}
```

### G3-06 record 4

**form**: `(let [a 5 b (* a 2)] b)`  •  **expected**: `10`

```
Two creatures of the meadow approached the coming winter very differently. All this took place at the edge of the forest.

Toc the ant had been trying to teach Skip the grasshopper how the REPL
works. "Look here," she said, pointing to a let where b uses a.
"You hand the form `(let [a 5 b (* a 2)] b)` to the runtime, and the runtime hands
you back what it evaluates to." Skip, weary from the morning's effort, agreed to
try.

Question: write a Clojure expression for the value of b when a=5 and b is (* a 2).

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 5 b (* a 2)] b)"}}]}
```

### G3-06 record 5

**form**: `(let [a 5 b (* a 2)] b)`  •  **expected**: `10`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. This was in the meadow.

Bit the ant had been trying to teach Skip the grasshopper how the REPL
works. "Look here," they said, pointing to a let where b uses a.
"You hand the form `(let [a 5 b (* a 2)] b)` to the runtime, and the runtime hands
you back what it evaluates to." Skip, lulled by the gentle wind, agreed to
try.

Question: write a Clojure expression for the value of b when a=5 and b is (* a 2).

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 5 b (* a 2)] b)"}}]}
```

## G3-07: fn — anonymous function

### G3-07 record 1

**form**: `((fn [x] (+ x 1)) 4)`  •  **expected**: `5`

```
Two creatures of the meadow approached the coming winter very differently.

A small audience of meadow creatures had gathered by the forest to watch
Hum the grasshopper attempt to outwit Tic the ant at reading the
REPL. Tic pointed to an anonymous function applied to 4 and read out the form aloud:
`((fn [x] (+ x 1)) 4)`. The crowd waited to see who would correctly write the
form to submit.

Question: write a Clojure expression for the result of applying (fn [x] (+ x 1)) to 4.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] (+ x 1)) 4)"}}]}
```

### G3-07 record 2

**form**: `((fn [x] (+ x 1)) 4)`  •  **expected**: `5`

```
All summer long, the Ant worked while the Grasshopper sang. All this took place at the edge of the farm.

A wooden sign nailed to a stalk in the farm carried a puzzle. The riddle
was simple: it asked the reader to evaluate `((fn [x] (+ x 1)) 4)`. Hum
laughed, with great whoops of laughter, and declared it too easy. Toc said patiently
that the only way to be sure of an anonymous function applied to 4 was to put it in the
REPL.

Write a Clojure expression that computes the result of applying (fn [x] (+ x 1)) to 4.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] (+ x 1)) 4)"}}]}
```

### G3-07 record 3

**form**: `((fn [x] (+ x 1)) 4)`  •  **expected**: `5`

```
All summer long, the Ant worked while the Grasshopper sang.

With a twig, Skip the grasshopper marked out a wager at the edge of the orchard: whoever
guessed the result of `((fn [x] (+ x 1)) 4)` first would win the right to
choose the next song. Bit the ant, saying very little, said it was easier
to ask the REPL about an anonymous function applied to 4 than to argue.

Question: write a Clojure expression for the result of applying (fn [x] (+ x 1)) to 4.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] (+ x 1)) 4)"}}]}
```

### G3-07 record 4

**form**: `((fn [x] (+ x 1)) 4)`  •  **expected**: `5`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Toc the ant kept a small stockpile-ledger near the orchard where every meaningful
quantity got its own name. She pointed to today's
entry: an anonymous function applied to 4. The form `((fn [x] (+ x 1)) 4)` would settle it once
Hum the grasshopper agreed to look at the binding.

Write a form whose evaluation gives the result of applying (fn [x] (+ x 1)) to 4.

---

I bind the inputs in a let, then compute.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] (+ x 1)) 4)"}}]}
```

### G3-07 record 5

**form**: `((fn [x] (+ x 1)) 4)`  •  **expected**: `5`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. This was atop the hilltop.

"You can call it whatever you like," Toc said near the hilltop, "but the
form is what matters." She drew the binding for
Chirp the grasshopper: the form `((fn [x] (+ x 1)) 4)` captured an anonymous function applied to 4, and
the REPL would do the rest.

Question: write a Clojure expression for the result of applying (fn [x] (+ x 1)) to 4.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] (+ x 1)) 4)"}}]}
```

## G3-08: fn — multi-arg

### G3-08 record 1

**form**: `((fn [a b c] (+ a b c)) 1 2 3)`  •  **expected**: `6`

```
Two creatures of the meadow approached the coming winter very differently. It happened on the hilltop.

At the edge of a stockpile atop the hilltop, Chirp the grasshopper sketched a
small wager into the dust: whoever guessed the result of `((fn [a b c] (+ a b c)) 1 2 3)`
first would win the right to set the next day's count.
Tic the ant, without complaint, said it was simpler to type the form into
the REPL than to argue about a three-arg anonymous function.

What Clojure form computes the sum of a, b, c? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [a b c] (+ a b c)) 1 2 3)"}}]}
```

### G3-08 record 2

**form**: `((fn [a b c] (+ a b c)) 1 2 3)`  •  **expected**: `6`

```
Two creatures of the meadow approached the coming winter very differently. All this took place by the garden.

Skip the grasshopper chalked a wager on a flat slate by the garden: whoever
predicted the result of `((fn [a b c] (+ a b c)) 1 2 3)` first would set the next day's
ration. Tic the ant, her eyes always on the path, said it would be simpler to type
the form into the REPL than to bicker about a three-arg anonymous function.

Question: write a Clojure expression for the sum of a, b, c.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [a b c] (+ a b c)) 1 2 3)"}}]}
```

### G3-08 record 3

**form**: `((fn [a b c] (+ a b c)) 1 2 3)`  •  **expected**: `6`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. This was at the edge of the forest.

With a twig, Hum the grasshopper marked out a wager in the forest: whoever
guessed the result of `((fn [a b c] (+ a b c)) 1 2 3)` first would win the right to
choose the next song. Bit the ant, her eyes always on the path, said it was easier
to ask the REPL about a three-arg anonymous function than to argue.

Write a form whose evaluation gives the sum of a, b, c.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [a b c] (+ a b c)) 1 2 3)"}}]}
```

### G3-08 record 4

**form**: `((fn [a b c] (+ a b c)) 1 2 3)`  •  **expected**: `6`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Chirp the grasshopper chalked a wager on a flat slate near the farm: whoever
predicted the result of `((fn [a b c] (+ a b c)) 1 2 3)` first would set the next day's
ration. Tic the ant, with steady, careful steps, said it would be simpler to type
the form into the REPL than to bicker about a three-arg anonymous function.

Question: write a Clojure expression for the sum of a, b, c.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [a b c] (+ a b c)) 1 2 3)"}}]}
```

### G3-08 record 5

**form**: `((fn [a b c] (+ a b c)) 1 2 3)`  •  **expected**: `6`

```
All summer long, the Ant worked while the Grasshopper sang.

Toc the ant kept a small stockpile-ledger at the edge of the garden where every meaningful
quantity got its own name. She pointed to today's
entry: a three-arg anonymous function. The form `((fn [a b c] (+ a b c)) 1 2 3)` would settle it once
Chirp the grasshopper agreed to look at the binding.

Write a form whose evaluation gives the sum of a, b, c.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [a b c] (+ a b c)) 1 2 3)"}}]}
```

## G3-09: defn — shorthand

### G3-09 record 1

**form**: `(do (defn dbl [x] (* x 2)) (dbl 5))`  •  **expected**: `10`

```
Two creatures of the meadow approached the coming winter very differently. All this took place in the forest.

Halfway through the morning's work, Chirp the grasshopper blocked
Tic the ant's path at the edge of the forest and refused to step aside until someone
could prove what the form `(do (defn dbl [x] (* x 2)) (dbl 5))` evaluated to. Chirp
called it impossible. Tic the ant, walking up at his usual
pace, simply said: "Submit a defn that doubles its argument to the REPL. Whatever comes
back is the answer."

Write a Clojure expression that computes the doubled value (dbl 5).

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn dbl [x] (* x 2)) (dbl 5))"}}]}
```

### G3-09 record 2

**form**: `(do (defn dbl [x] (* x 2)) (dbl 5))`  •  **expected**: `10`

```
Two creatures of the meadow approached the coming winter very differently.

Toc the ant and Hum the grasshopper stopped at the edge of the meadow where someone had
written a defn that doubles its argument on a flat stone. Hum, as if the race were already won,
declared that they could see the answer at a glance.
Toc, without complaint, suggested they actually evaluate the form
`(do (defn dbl [x] (* x 2)) (dbl 5))` in the REPL and read off whatever it returned.

Question: write a Clojure expression for the doubled value (dbl 5).

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn dbl [x] (* x 2)) (dbl 5))"}}]}
```

### G3-09 record 3

**form**: `(do (defn dbl [x] (* x 2)) (dbl 5))`  •  **expected**: `10`

```
All summer long, the Ant worked while the Grasshopper sang. This was by the farm.

Halfway through the morning's work, Skip the grasshopper blocked
Toc the ant's path in the farm and refused to step aside until someone
could prove what the form `(do (defn dbl [x] (* x 2)) (dbl 5))` evaluated to. Skip
called it impossible. Toc the ant, walking up at her usual
pace, simply said: "Submit a defn that doubles its argument to the REPL. Whatever comes
back is the answer."

Write a form whose evaluation gives the doubled value (dbl 5).

---

I name the values first and then combine them.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn dbl [x] (* x 2)) (dbl 5))"}}]}
```

### G3-09 record 4

**form**: `(do (defn dbl [x] (* x 2)) (dbl 5))`  •  **expected**: `10`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. It happened at the edge of the garden.

A wooden sign nailed to a stalk near the garden carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(do (defn dbl [x] (* x 2)) (dbl 5))`. Skip
laughed, as if the race were already won, and declared it too easy. Tic said patiently
that the only way to be sure of a defn that doubles its argument was to put it in the
REPL.

Write a form whose evaluation gives the doubled value (dbl 5).

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn dbl [x] (* x 2)) (dbl 5))"}}]}
```

### G3-09 record 5

**form**: `(do (defn dbl [x] (* x 2)) (dbl 5))`  •  **expected**: `10`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. It happened at the edge of the meadow.

With a twig, Hum the grasshopper marked out a wager near the meadow: whoever
guessed the result of `(do (defn dbl [x] (* x 2)) (dbl 5))` first would win the right to
choose the next song. Toc the ant, untroubled by what others thought, said it was easier
to ask the REPL about a defn that doubles its argument than to argue.

What Clojure form computes the doubled value (dbl 5)? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn dbl [x] (* x 2)) (dbl 5))"}}]}
```

## G3-10: anonymous shorthand #()

### G3-10 record 1

**form**: `(#(+ % 1) 5)`  •  **expected**: `6`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Bit the ant and Skip the grasshopper stopped near the woods where someone had
written the shorthand #(+ % 1) applied to 5 on a flat stone. Skip, boasting at every turn,
declared that she could see the answer at a glance.
Bit, with steady, careful steps, suggested they actually evaluate the form
`(#(+ % 1) 5)` in the REPL and read off whatever it returned.

What Clojure form computes the result of (#(+ % 1) 5)? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(#(+ % 1) 5)"}}]}
```

### G3-10 record 2

**form**: `(#(+ % 1) 5)`  •  **expected**: `6`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Chirp the grasshopper chalked a wager on a flat slate at the edge of the garden: whoever
predicted the result of `(#(+ % 1) 5)` first would set the next day's
ration. Tic the ant, her eyes always on the path, said it would be simpler to type
the form into the REPL than to bicker about the shorthand #(+ % 1) applied to 5.

Write a form whose evaluation gives the result of (#(+ % 1) 5).

---

{"tool_calls":[{"name":"eval","args":{"form":"(#(+ % 1) 5)"}}]}
```

### G3-10 record 3

**form**: `(#(+ % 1) 5)`  •  **expected**: `6`

```
All summer long, the Ant worked while the Grasshopper sang.

"There is no need to evaluate that," Chirp the grasshopper said,
with a smug grin. "Anyone can see what the shorthand #(+ % 1) applied to 5 comes to."
Toc the ant, who by the garden had grown used to such claims, asked
him to actually write the form `(#(+ % 1) 5)` and
submit it to the REPL — just to be sure.

Write a form whose evaluation gives the result of (#(+ % 1) 5).

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(#(+ % 1) 5)"}}]}
```

### G3-10 record 4

**form**: `(#(+ % 1) 5)`  •  **expected**: `6`

```
Two creatures of the meadow approached the coming winter very differently. This was at the edge of the farm.

A small audience of meadow creatures had gathered in the farm to watch
Skip the grasshopper attempt to outwit Bit the ant at reading the
REPL. Bit pointed to the shorthand #(+ % 1) applied to 5 and read out the form aloud:
`(#(+ % 1) 5)`. The crowd waited to see who would correctly write the
form to submit.

Write a Clojure expression that computes the result of (#(+ % 1) 5).

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(#(+ % 1) 5)"}}]}
```

### G3-10 record 5

**form**: `(#(+ % 1) 5)`  •  **expected**: `6`

```
All summer long, the Ant worked while the Grasshopper sang. It happened at the edge of the farm.

A wooden sign nailed to a stalk in the farm carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(#(+ % 1) 5)`. Chirp
laughed, boasting at every turn, and declared it too easy. Bit said patiently
that the only way to be sure of the shorthand #(+ % 1) applied to 5 was to put it in the
REPL.

Write a Clojure expression that computes the result of (#(+ % 1) 5).

---

{"tool_calls":[{"name":"eval","args":{"form":"(#(+ % 1) 5)"}}]}
```

## G3-11: Substitution rule

### G3-11 record 1

**form**: `(let [a 7] (+ a a))`  •  **expected**: `14`

```
Two creatures of the meadow approached the coming winter very differently. It happened in the meadow.

Halfway through the morning's work, Chirp the grasshopper blocked
Tic the ant's path in the meadow and refused to step aside until someone
could prove what the form `(let [a 7] (+ a a))` evaluated to. Chirp
called it impossible. Tic the ant, walking up at his usual
pace, simply said: "Submit the let where a is referenced twice to the REPL. Whatever comes
back is the answer."

Question: write a Clojure expression for the result of (+ a a) when a=7.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 7] (+ a a))"}}]}
```

### G3-11 record 2

**form**: `(let [a 7] (+ a a))`  •  **expected**: `14`

```
Two creatures of the meadow approached the coming winter very differently. This was near the forest.

At the edge of a stockpile at the edge of the forest, Skip the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(let [a 7] (+ a a))`
first would win the right to set the next day's count.
Toc the ant, with steady, careful steps, said it was simpler to type the form into
the REPL than to argue about the let where a is referenced twice.

Write a form whose evaluation gives the result of (+ a a) when a=7.

---

I bind the inputs in a let, then compute.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 7] (+ a a))"}}]}
```

### G3-11 record 3

**form**: `(let [a 7] (+ a a))`  •  **expected**: `14`

```
Two creatures of the meadow approached the coming winter very differently. This was at the edge of the forest.

A wooden sign nailed to a stalk in the forest carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(let [a 7] (+ a a))`. Skip
laughed, puffed up with pride, and declared it too easy. Bit said patiently
that the only way to be sure of the let where a is referenced twice was to put it in the
REPL.

Question: write a Clojure expression for the result of (+ a a) when a=7.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 7] (+ a a))"}}]}
```

### G3-11 record 4

**form**: `(let [a 7] (+ a a))`  •  **expected**: `14`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Tic the ant had been keeping a small leather notebook of every form
he had successfully evaluated. Today in the woods, the next entry
was the let where a is referenced twice. Hum the grasshopper peered over
his shoulder at the form `(let [a 7] (+ a a))` and asked what it
would come out to.

What Clojure form computes the result of (+ a a) when a=7? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 7] (+ a a))"}}]}
```

### G3-11 record 5

**form**: `(let [a 7] (+ a a))`  •  **expected**: `14`

```
All summer long, the Ant worked while the Grasshopper sang.

A wooden sign nailed to a stalk by the garden carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(let [a 7] (+ a a))`. Skip
laughed, swaggering through the underbrush, and declared it too easy. Bit said patiently
that the only way to be sure of the let where a is referenced twice was to put it in the
REPL.

Write a form whose evaluation gives the result of (+ a a) when a=7.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 7] (+ a a))"}}]}
```

## G3-12: Scope vs namespace

### G3-12 record 1

**form**: `(do (def g 5) (let [g 99] (+ g 1)))`  •  **expected**: `100`

```
Two creatures of the meadow approached the coming winter very differently.

At the edge of a stockpile atop the hilltop, Skip the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(do (def g 5) (let [g 99] (+ g 1)))`
first would win the right to set the next day's count.
Toc the ant, stepping deliberately, said it was simpler to type the form into
the REPL than to argue about an inner let masking the outer def g.

Write a form whose evaluation gives the value computed inside the inner scope.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def g 5) (let [g 99] (+ g 1)))"}}]}
```

### G3-12 record 2

**form**: `(do (def g 5) (let [g 99] (+ g 1)))`  •  **expected**: `100`

```
Two creatures of the meadow approached the coming winter very differently.

Bit the ant kept a small stockpile-ledger at the edge of the garden where every meaningful
quantity got its own name. They pointed to today's
entry: an inner let masking the outer def g. The form `(do (def g 5) (let [g 99] (+ g 1)))` would settle it once
Hum the grasshopper agreed to look at the binding.

Write a form whose evaluation gives the value computed inside the inner scope.

---

I write the let-form so the REPL can substitute.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def g 5) (let [g 99] (+ g 1)))"}}]}
```

### G3-12 record 3

**form**: `(do (def g 5) (let [g 99] (+ g 1)))`  •  **expected**: `100`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. It happened at the edge of the woods.

A wooden sign nailed to a stalk in the woods carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(do (def g 5) (let [g 99] (+ g 1)))`. Hum
laughed, with great whoops of laughter, and declared it too easy. Toc said patiently
that the only way to be sure of an inner let masking the outer def g was to put it in the
REPL.

Write a form whose evaluation gives the value computed inside the inner scope.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def g 5) (let [g 99] (+ g 1)))"}}]}
```

### G3-12 record 4

**form**: `(do (def g 5) (let [g 99] (+ g 1)))`  •  **expected**: `100`

```
Two creatures of the meadow approached the coming winter very differently.

A wooden sign nailed to a stalk in the garden carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(do (def g 5) (let [g 99] (+ g 1)))`. Skip
laughed, with great whoops of laughter, and declared it too easy. Tic said patiently
that the only way to be sure of an inner let masking the outer def g was to put it in the
REPL.

Write a Clojure expression that computes the value computed inside the inner scope.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def g 5) (let [g 99] (+ g 1)))"}}]}
```

### G3-12 record 5

**form**: `(do (def g 5) (let [g 99] (+ g 1)))`  •  **expected**: `100`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. It happened near the forest.

Halfway through the morning's work, Chirp the grasshopper blocked
Toc the ant's path at the edge of the forest and refused to step aside until someone
could prove what the form `(do (def g 5) (let [g 99] (+ g 1)))` evaluated to. Chirp
called it impossible. Toc the ant, walking up at her usual
pace, simply said: "Submit an inner let masking the outer def g to the REPL. Whatever comes
back is the answer."

Write a Clojure expression that computes the value computed inside the inner scope.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def g 5) (let [g 99] (+ g 1)))"}}]}
```

## G3-13: fn body returns last form

### G3-13 record 1

**form**: `((fn [x] x x x 99) 1)`  •  **expected**: `99`

```
Two creatures of the meadow approached the coming winter very differently.

At the edge of a stockpile at the edge of the orchard, Hum the grasshopper sketched a
small wager into the dust: whoever guessed the result of `((fn [x] x x x 99) 1)`
first would win the right to set the next day's count.
Toc the ant, with steady, careful steps, said it was simpler to type the form into
the REPL than to argue about a fn whose body has multiple forms; only the last is returned.

Write a form whose evaluation gives the value of a fn body that ends with 99.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] x x x 99) 1)"}}]}
```

### G3-13 record 2

**form**: `((fn [x] x x x 99) 1)`  •  **expected**: `99`

```
Two creatures of the meadow approached the coming winter very differently.

A wooden sign nailed to a stalk by the farm carried a puzzle. The riddle
was simple: it asked the reader to evaluate `((fn [x] x x x 99) 1)`. Chirp
laughed, swaggering through the underbrush, and declared it too easy. Tic said patiently
that the only way to be sure of a fn whose body has multiple forms; only the last is returned was to put it in the
REPL.

Write a Clojure expression that computes the value of a fn body that ends with 99.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] x x x 99) 1)"}}]}
```

### G3-13 record 3

**form**: `((fn [x] x x x 99) 1)`  •  **expected**: `99`

```
All summer long, the Ant worked while the Grasshopper sang. It happened atop the hilltop.

Tic the ant had been keeping a small leather notebook of every form
he had successfully evaluated. Today on the hilltop, the next entry
was a fn whose body has multiple forms; only the last is returned. Chirp the grasshopper peered over
his shoulder at the form `((fn [x] x x x 99) 1)` and asked what it
would come out to.

Write a Clojure expression that computes the value of a fn body that ends with 99.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] x x x 99) 1)"}}]}
```

### G3-13 record 4

**form**: `((fn [x] x x x 99) 1)`  •  **expected**: `99`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Chirp the grasshopper chalked a wager on a flat slate by the farm: whoever
predicted the result of `((fn [x] x x x 99) 1)` first would set the next day's
ration. Tic the ant, without complaint, said it would be simpler to type
the form into the REPL than to bicker about a fn whose body has multiple forms; only the last is returned.

What Clojure form computes the value of a fn body that ends with 99? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] x x x 99) 1)"}}]}
```

### G3-13 record 5

**form**: `((fn [x] x x x 99) 1)`  •  **expected**: `99`

```
Two creatures of the meadow approached the coming winter very differently. All this took place in the forest.

A small audience of meadow creatures had gathered in the forest to watch
Chirp the grasshopper attempt to outwit Bit the ant at reading the
REPL. Bit pointed to a fn whose body has multiple forms; only the last is returned and read out the form aloud:
`((fn [x] x x x 99) 1)`. The crowd waited to see who would correctly write the
form to submit.

Question: write a Clojure expression for the value of a fn body that ends with 99.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] x x x 99) 1)"}}]}
```

## G3-14: do form

### G3-14 record 1

**form**: `(do 1 2 3)`  •  **expected**: `3`

```
Two creatures of the meadow approached the coming winter very differently.

Toc the ant had been trying to teach Skip the grasshopper how the REPL
works. "Look here," she said, pointing to the do form (do 1 2 3).
"You hand the form `(do 1 2 3)` to the runtime, and the runtime hands
you back what it evaluates to." Skip, lulled by the gentle wind, agreed to
try.

Write a Clojure expression that computes the value of (do 1 2 3).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do 1 2 3)"}}]}
```

### G3-14 record 2

**form**: `(do 1 2 3)`  •  **expected**: `3`

```
Two creatures of the meadow approached the coming winter very differently.

At the edge of a stockpile by the woods, Hum the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(do 1 2 3)`
first would win the right to set the next day's count.
Toc the ant, without complaint, said it was simpler to type the form into
the REPL than to argue about the do form (do 1 2 3).

Write a form whose evaluation gives the value of (do 1 2 3).

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do 1 2 3)"}}]}
```

### G3-14 record 3

**form**: `(do 1 2 3)`  •  **expected**: `3`

```
All summer long, the Ant worked while the Grasshopper sang.

Hum the grasshopper chalked a wager on a flat slate at the edge of the hilltop: whoever
predicted the result of `(do 1 2 3)` first would set the next day's
ration. Bit the ant, stepping deliberately, said it would be simpler to type
the form into the REPL than to bicker about the do form (do 1 2 3).

What Clojure form computes the value of (do 1 2 3)? Submit it via `eval`.

---

I write the let-form so the REPL can substitute.

{"tool_calls":[{"name":"eval","args":{"form":"(do 1 2 3)"}}]}
```

### G3-14 record 4

**form**: `(do 1 2 3)`  •  **expected**: `3`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Chirp the grasshopper chalked a wager on a flat slate at the edge of the farm: whoever
predicted the result of `(do 1 2 3)` first would set the next day's
ration. Tic the ant, saying very little, said it would be simpler to type
the form into the REPL than to bicker about the do form (do 1 2 3).

Write a form whose evaluation gives the value of (do 1 2 3).

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do 1 2 3)"}}]}
```

### G3-14 record 5

**form**: `(do 1 2 3)`  •  **expected**: `3`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

"There is no need to evaluate that," Chirp the grasshopper said,
puffed up with pride. "Anyone can see what the do form (do 1 2 3) comes to."
Toc the ant, who near the hilltop had grown used to such claims, asked
him to actually write the form `(do 1 2 3)` and
submit it to the REPL — just to be sure.

Write a Clojure expression that computes the value of (do 1 2 3).

---

I bind the inputs in a let, then compute.

{"tool_calls":[{"name":"eval","args":{"form":"(do 1 2 3)"}}]}
```

## G3-15: Side-effects in body

### G3-15 record 1

**form**: `(do (println "hi") 42)`  •  **expected**: `42`

```
Two creatures of the meadow approached the coming winter very differently.

Bit the ant kept a small stockpile-ledger near the meadow where every meaningful
quantity got its own name. They pointed to today's
entry: the form (do (println "hi") 42). The form `(do (println "hi") 42)` would settle it once
Skip the grasshopper agreed to look at the binding.

Write a form whose evaluation gives the return value of the do (the println side-effects, but the do returns 42).

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (println \"hi\") 42)"}}]}
```

### G3-15 record 2

**form**: `(do (println "hi") 42)`  •  **expected**: `42`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Hum the grasshopper chalked a wager on a flat slate by the garden: whoever
predicted the result of `(do (println "hi") 42)` first would set the next day's
ration. Toc the ant, her eyes always on the path, said it would be simpler to type
the form into the REPL than to bicker about the form (do (println "hi") 42).

Write a form whose evaluation gives the return value of the do (the println side-effects, but the do returns 42).

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (println \"hi\") 42)"}}]}
```

### G3-15 record 3

**form**: `(do (println "hi") 42)`  •  **expected**: `42`

```
Two creatures of the meadow approached the coming winter very differently.

With a twig, Hum the grasshopper marked out a wager near the meadow: whoever
guessed the result of `(do (println "hi") 42)` first would win the right to
choose the next song. Bit the ant, with steady, careful steps, said it was easier
to ask the REPL about the form (do (println "hi") 42) than to argue.

Write a form whose evaluation gives the return value of the do (the println side-effects, but the do returns 42).

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (println \"hi\") 42)"}}]}
```

### G3-15 record 4

**form**: `(do (println "hi") 42)`  •  **expected**: `42`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Tic the ant had been trying to teach Hum the grasshopper how the REPL
works. "Look here," he said, pointing to the form (do (println "hi") 42).
"You hand the form `(do (println "hi") 42)` to the runtime, and the runtime hands
you back what it evaluates to." Hum, yawning at the soft moss, agreed to
try.

Question: write a Clojure expression for the return value of the do (the println side-effects, but the do returns 42).

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do (println \"hi\") 42)"}}]}
```

### G3-15 record 5

**form**: `(do (println "hi") 42)`  •  **expected**: `42`

```
Two creatures of the meadow approached the coming winter very differently. All this took place at the edge of the garden.

Toc the ant and Skip the grasshopper stopped in the garden where someone had
written the form (do (println "hi") 42) on a flat stone. Skip, with a smug grin,
declared that she could see the answer at a glance.
Toc, with steady, careful steps, suggested they actually evaluate the form
`(do (println "hi") 42)` in the REPL and read off whatever it returned.

Write a Clojure expression that computes the return value of the do (the println side-effects, but the do returns 42).

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (println \"hi\") 42)"}}]}
```

## G3-16: Name collision: namespace vs let

### G3-16 record 1

**form**: `(let [+ 99] +)`  •  **expected**: `99`

```
Two creatures of the meadow approached the coming winter very differently. All this took place at the edge of the farm.

"There is no need to evaluate that," Hum the grasshopper said,
as if the race were already won. "Anyone can see what a let that shadows the + function comes to."
Toc the ant, who by the farm had grown used to such claims, asked
them to actually write the form `(let [+ 99] +)` and
submit it to the REPL — just to be sure.

Write a form whose evaluation gives the value bound to the (locally shadowed) +.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(let [+ 99] +)"}}]}
```

### G3-16 record 2

**form**: `(let [+ 99] +)`  •  **expected**: `99`

```
All summer long, the Ant worked while the Grasshopper sang.

Hum the grasshopper chalked a wager on a flat slate in the woods: whoever
predicted the result of `(let [+ 99] +)` first would set the next day's
ration. Tic the ant, her eyes always on the path, said it would be simpler to type
the form into the REPL than to bicker about a let that shadows the + function.

What Clojure form computes the value bound to the (locally shadowed) +? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [+ 99] +)"}}]}
```

### G3-16 record 3

**form**: `(let [+ 99] +)`  •  **expected**: `99`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. All this took place by the woods.

"There is no need to evaluate that," Chirp the grasshopper said,
with a smug grin. "Anyone can see what a let that shadows the + function comes to."
Tic the ant, who by the woods had grown used to such claims, asked
him to actually write the form `(let [+ 99] +)` and
submit it to the REPL — just to be sure.

Write a form whose evaluation gives the value bound to the (locally shadowed) +.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [+ 99] +)"}}]}
```

### G3-16 record 4

**form**: `(let [+ 99] +)`  •  **expected**: `99`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

A wooden sign nailed to a stalk near the forest carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(let [+ 99] +)`. Chirp
laughed, boasting at every turn, and declared it too easy. Bit said patiently
that the only way to be sure of a let that shadows the + function was to put it in the
REPL.

Write a Clojure expression that computes the value bound to the (locally shadowed) +.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(let [+ 99] +)"}}]}
```

### G3-16 record 5

**form**: `(let [+ 99] +)`  •  **expected**: `99`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. All this took place near the garden.

"There is no need to evaluate that," Skip the grasshopper said,
swaggering through the underbrush. "Anyone can see what a let that shadows the + function comes to."
Bit the ant, who at the edge of the garden had grown used to such claims, asked
her to actually write the form `(let [+ 99] +)` and
submit it to the REPL — just to be sure.

Write a form whose evaluation gives the value bound to the (locally shadowed) +.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [+ 99] +)"}}]}
```

## G3-17: Naming conventions (kebab-case)

### G3-17 record 1

**form**: `(let [grasshopper-pace 4 ant-pace 1] (- grasshopper-pace ant-pace))`  •  **expected**: `3`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. All this took place by the meadow.

"There is no need to evaluate that," Skip the grasshopper said,
with a smug grin. "Anyone can see what a let with kebab-case names comes to."
Tic the ant, who in the meadow had grown used to such claims, asked
her to actually write the form `(let [grasshopper-pace 4 ant-pace 1] (- grasshopper-pace ant-pace))` and
submit it to the REPL — just to be sure.

Question: write a Clojure expression for the difference of the two paces.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [grasshopper-pace 4 ant-pace 1] (- grasshopper-pace ant-pace))"}}]}
```

### G3-17 record 2

**form**: `(let [grasshopper-pace 4 ant-pace 1] (- grasshopper-pace ant-pace))`  •  **expected**: `3`

```
Two creatures of the meadow approached the coming winter very differently. All this took place in the forest.

"You can call it whatever you like," Bit said near the forest, "but the
form is what matters." They drew the binding for
Hum the grasshopper: the form `(let [grasshopper-pace 4 ant-pace 1] (- grasshopper-pace ant-pace))` captured a let with kebab-case names, and
the REPL would do the rest.

Write a form whose evaluation gives the difference of the two paces.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [grasshopper-pace 4 ant-pace 1] (- grasshopper-pace ant-pace))"}}]}
```

### G3-17 record 3

**form**: `(let [grasshopper-pace 4 ant-pace 1] (- grasshopper-pace ant-pace))`  •  **expected**: `3`

```
All summer long, the Ant worked while the Grasshopper sang. It happened in the orchard.

Toc the ant and Hum the grasshopper stopped in the orchard where someone had
written a let with kebab-case names on a flat stone. Hum, with great whoops of laughter,
declared that they could see the answer at a glance.
Toc, saying very little, suggested they actually evaluate the form
`(let [grasshopper-pace 4 ant-pace 1] (- grasshopper-pace ant-pace))` in the REPL and read off whatever it returned.

Question: write a Clojure expression for the difference of the two paces.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [grasshopper-pace 4 ant-pace 1] (- grasshopper-pace ant-pace))"}}]}
```

### G3-17 record 4

**form**: `(let [grasshopper-pace 4 ant-pace 1] (- grasshopper-pace ant-pace))`  •  **expected**: `3`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

A wooden sign nailed to a stalk in the garden carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(let [grasshopper-pace 4 ant-pace 1] (- grasshopper-pace ant-pace))`. Chirp
laughed, puffed up with pride, and declared it too easy. Toc said patiently
that the only way to be sure of a let with kebab-case names was to put it in the
REPL.

Write a Clojure expression that computes the difference of the two paces.

---

I write the let-form so the REPL can substitute.

{"tool_calls":[{"name":"eval","args":{"form":"(let [grasshopper-pace 4 ant-pace 1] (- grasshopper-pace ant-pace))"}}]}
```

### G3-17 record 5

**form**: `(let [grasshopper-pace 4 ant-pace 1] (- grasshopper-pace ant-pace))`  •  **expected**: `3`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Toc the ant kept a small stockpile-ledger by the farm where every meaningful
quantity got its own name. She pointed to today's
entry: a let with kebab-case names. The form `(let [grasshopper-pace 4 ant-pace 1] (- grasshopper-pace ant-pace))` would settle it once
Hum the grasshopper agreed to look at the binding.

What Clojure form computes the difference of the two paces? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(let [grasshopper-pace 4 ant-pace 1] (- grasshopper-pace ant-pace))"}}]}
```

## G3-18: When to name vs inline

### G3-18 record 1

**form**: `(let [n 5] (* n n n))`  •  **expected**: `125`

```
All summer long, the Ant worked while the Grasshopper sang.

"You can call it whatever you like," Toc said by the farm, "but the
form is what matters." She drew the binding for
Skip the grasshopper: the form `(let [n 5] (* n n n))` captured naming n once and using it three times, and
the REPL would do the rest.

What Clojure form computes n cubed where n=5? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(let [n 5] (* n n n))"}}]}
```

### G3-18 record 2

**form**: `(let [n 5] (* n n n))`  •  **expected**: `125`

```
All summer long, the Ant worked while the Grasshopper sang. All this took place near the farm.

With a twig, Hum the grasshopper marked out a wager at the edge of the farm: whoever
guessed the result of `(let [n 5] (* n n n))` first would win the right to
choose the next song. Bit the ant, with steady, careful steps, said it was easier
to ask the REPL about naming n once and using it three times than to argue.

Write a form whose evaluation gives n cubed where n=5.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(let [n 5] (* n n n))"}}]}
```

### G3-18 record 3

**form**: `(let [n 5] (* n n n))`  •  **expected**: `125`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

"There is no need to evaluate that," Hum the grasshopper said,
as if the race were already won. "Anyone can see what naming n once and using it three times comes to."
Toc the ant, who in the farm had grown used to such claims, asked
them to actually write the form `(let [n 5] (* n n n))` and
submit it to the REPL — just to be sure.

Write a Clojure expression that computes n cubed where n=5.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [n 5] (* n n n))"}}]}
```

### G3-18 record 4

**form**: `(let [n 5] (* n n n))`  •  **expected**: `125`

```
All summer long, the Ant worked while the Grasshopper sang.

Tic the ant had been trying to teach Skip the grasshopper how the REPL
works. "Look here," he said, pointing to naming n once and using it three times.
"You hand the form `(let [n 5] (* n n n))` to the runtime, and the runtime hands
you back what it evaluates to." Skip, yawning at the soft moss, agreed to
try.

Question: write a Clojure expression for n cubed where n=5.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [n 5] (* n n n))"}}]}
```

### G3-18 record 5

**form**: `(let [n 5] (* n n n))`  •  **expected**: `125`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. All this took place in the garden.

Halfway through the morning's work, Hum the grasshopper blocked
Toc the ant's path near the garden and refused to step aside until someone
could prove what the form `(let [n 5] (* n n n))` evaluated to. Hum
called it impossible. Toc the ant, walking up at her usual
pace, simply said: "Submit naming n once and using it three times to the REPL. Whatever comes
back is the answer."

Write a form whose evaluation gives n cubed where n=5.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [n 5] (* n n n))"}}]}
```


---

**Grade 3 totals: 18 subjects, 90 records.**
