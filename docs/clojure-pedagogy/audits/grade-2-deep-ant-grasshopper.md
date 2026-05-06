# Deep spot-check: grade 2 ant-grasshopper (5 records per subject)

Manual-review dump for hand-audit. Each subject gets 5 rendered records sampled across different seeds so subplot/character/location variety is visible.

---

## G2-01: Multi-arg arithmetic

### G2-01 record 1

**form**: `(+ 1 2 3 4)`  •  **expected**: `10`

```
Two creatures of the meadow approached the coming winter very differently.

Toc the ant had been keeping a small leather notebook of every form
she had successfully evaluated. Today atop the hilltop, the next entry
was the sum (+ 1 2 3 4). Skip the grasshopper peered over
her shoulder at the form `(+ 1 2 3 4)` and asked what it
would come out to.

What Clojure form computes the result of (+ 1 2 3 4)? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2 3 4)"}}]}
```

### G2-01 record 2

**form**: `(+ 1 2 3 4)`  •  **expected**: `10`

```
Two creatures of the meadow approached the coming winter very differently. It happened in the farm.

Bit the ant had been trying to teach Hum the grasshopper how the REPL
works. "Look here," they said, pointing to the sum (+ 1 2 3 4).
"You hand the form `(+ 1 2 3 4)` to the runtime, and the runtime hands
you back what it evaluates to." Hum, lulled by the gentle wind, agreed to
try.

Write a form whose evaluation gives the result of (+ 1 2 3 4).

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2 3 4)"}}]}
```

### G2-01 record 3

**form**: `(+ 1 2 3 4)`  •  **expected**: `10`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Skip the grasshopper chalked a wager on a flat slate on the hilltop: whoever
predicted the result of `(+ 1 2 3 4)` first would set the next day's
ration. Bit the ant, untroubled by what others thought, said it would be simpler to type
the form into the REPL than to bicker about the sum (+ 1 2 3 4).

Write a form whose evaluation gives the result of (+ 1 2 3 4).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2 3 4)"}}]}
```

### G2-01 record 4

**form**: `(+ 1 2 3 4)`  •  **expected**: `10`

```
All summer long, the Ant worked while the Grasshopper sang.

Bit the ant had been laying out a chain of small computations on a
slate by the orchard — one operation, then another, all to settle a question
Skip the grasshopper had raised. The current form on the slate was
`(+ 1 2 3 4)`, and Bit explained that the sum (+ 1 2 3 4) would be
settled the moment the form was evaluated.

Write a form whose evaluation gives the result of (+ 1 2 3 4).

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2 3 4)"}}]}
```

### G2-01 record 5

**form**: `(+ 1 2 3 4)`  •  **expected**: `10`

```
Two creatures of the meadow approached the coming winter very differently.

Toc the ant had been trying to teach Skip the grasshopper how the REPL
works. "Look here," she said, pointing to the sum (+ 1 2 3 4).
"You hand the form `(+ 1 2 3 4)` to the runtime, and the runtime hands
you back what it evaluates to." Skip, her legs heavy from sprinting, agreed to
try.

Question: write a Clojure expression for the result of (+ 1 2 3 4).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2 3 4)"}}]}
```

## G2-02: Comparison chains

### G2-02 record 1

**form**: `(< 1 2 3)`  •  **expected**: `True`

```
Two creatures of the meadow approached the coming winter very differently.

Halfway through the morning's work, Chirp the grasshopper blocked
Bit the ant's path atop the hilltop and refused to step aside until someone
could prove what the form `(< 1 2 3)` evaluated to. Chirp
called it impossible. Bit the ant, walking up at their usual
pace, simply said: "Submit the chain (< 1 2 3) to the REPL. Whatever comes
back is the answer."

Question: write a Clojure expression for whether 1 < 2 < 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(< 1 2 3)"}}]}
```

### G2-02 record 2

**form**: `(< 1 2 3)`  •  **expected**: `True`

```
Two creatures of the meadow approached the coming winter very differently.

With a twig, Chirp the grasshopper marked out a wager atop the hilltop: whoever
guessed the result of `(< 1 2 3)` first would win the right to
choose the next song. Bit the ant, untroubled by what others thought, said it was easier
to ask the REPL about the chain (< 1 2 3) than to argue.

What Clojure form computes whether 1 < 2 < 3? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(< 1 2 3)"}}]}
```

### G2-02 record 3

**form**: `(< 1 2 3)`  •  **expected**: `True`

```
All summer long, the Ant worked while the Grasshopper sang. This was near the orchard.

Toc the ant had been laying out a chain of small computations on a
slate by the orchard — one operation, then another, all to settle a question
Hum the grasshopper had raised. The current form on the slate was
`(< 1 2 3)`, and Toc explained that the chain (< 1 2 3) would be
settled the moment the form was evaluated.

Write a Clojure expression that computes whether 1 < 2 < 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(< 1 2 3)"}}]}
```

### G2-02 record 4

**form**: `(< 1 2 3)`  •  **expected**: `True`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

With a twig, Chirp the grasshopper marked out a wager by the garden: whoever
guessed the result of `(< 1 2 3)` first would win the right to
choose the next song. Toc the ant, untroubled by what others thought, said it was easier
to ask the REPL about the chain (< 1 2 3) than to argue.

Write a Clojure expression that computes whether 1 < 2 < 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(< 1 2 3)"}}]}
```

### G2-02 record 5

**form**: `(< 1 2 3)`  •  **expected**: `True`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

"Whatever `(< 1 2 3)` comes to," Skip the grasshopper declared
puffed up with pride by the orchard, "I'll wager I know it without typing it."
Tic the ant, her eyes always on the path, picked up a stick and drew
the chain (< 1 2 3) in the dust. "Then write the form," he
said. "The REPL will have the last word."

Write a Clojure expression that computes whether 1 < 2 < 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(< 1 2 3)"}}]}
```

## G2-03: not= and = with multiple args

### G2-03 record 1

**form**: `(not= 1 2)`  •  **expected**: `True`

```
All summer long, the Ant worked while the Grasshopper sang. All this took place at the edge of the garden.

Tic the ant had been trying to teach Skip the grasshopper how the REPL
works. "Look here," he said, pointing to the form (not= 1 2).
"You hand the form `(not= 1 2)` to the runtime, and the runtime hands
you back what it evaluates to." Skip, drowsy from the warm sun, agreed to
try.

Question: write a Clojure expression for whether 1 differs from 2.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(not= 1 2)"}}]}
```

### G2-03 record 2

**form**: `(not= 1 2)`  •  **expected**: `True`

```
Two creatures of the meadow approached the coming winter very differently.

At the edge of a stockpile in the meadow, Skip the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(not= 1 2)`
first would win the right to set the next day's count.
Tic the ant, without complaint, said it was simpler to type the form into
the REPL than to argue about the form (not= 1 2).

What Clojure form computes whether 1 differs from 2? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(not= 1 2)"}}]}
```

### G2-03 record 3

**form**: `(not= 1 2)`  •  **expected**: `True`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Halfway through the morning's work, Chirp the grasshopper blocked
Bit the ant's path by the garden and refused to step aside until someone
could prove what the form `(not= 1 2)` evaluated to. Chirp
called it impossible. Bit the ant, walking up at their usual
pace, simply said: "Submit the form (not= 1 2) to the REPL. Whatever comes
back is the answer."

What Clojure form computes whether 1 differs from 2? Submit it via `eval`.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(not= 1 2)"}}]}
```

### G2-03 record 4

**form**: `(not= 1 2)`  •  **expected**: `True`

```
Two creatures of the meadow approached the coming winter very differently. It happened by the orchard.

A wooden sign nailed to a stalk in the orchard carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(not= 1 2)`. Skip
laughed, swaggering through the underbrush, and declared it too easy. Toc said patiently
that the only way to be sure of the form (not= 1 2) was to put it in the
REPL.

Write a Clojure expression that computes whether 1 differs from 2.

---

{"tool_calls":[{"name":"eval","args":{"form":"(not= 1 2)"}}]}
```

### G2-03 record 5

**form**: `(not= 1 2)`  •  **expected**: `True`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Tic the ant had been trying to teach Chirp the grasshopper how the REPL
works. "Look here," he said, pointing to the form (not= 1 2).
"You hand the form `(not= 1 2)` to the runtime, and the runtime hands
you back what it evaluates to." Chirp, lulled by the gentle wind, agreed to
try.

What Clojure form computes whether 1 differs from 2? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(not= 1 2)"}}]}
```

## G2-04: min and max

### G2-04 record 1

**form**: `(min 1 2 3)`  •  **expected**: `1`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Toc the ant had been trying to teach Chirp the grasshopper how the REPL
works. "Look here," she said, pointing to the form (min 1 2 3).
"You hand the form `(min 1 2 3)` to the runtime, and the runtime hands
you back what it evaluates to." Chirp, her legs heavy from sprinting, agreed to
try.

Write a Clojure expression that computes the smallest of 1, 2, 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(min 1 2 3)"}}]}
```

### G2-04 record 2

**form**: `(min 1 2 3)`  •  **expected**: `1`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. This was on the hilltop.

Tic the ant had been trying to teach Chirp the grasshopper how the REPL
works. "Look here," he said, pointing to the form (min 1 2 3).
"You hand the form `(min 1 2 3)` to the runtime, and the runtime hands
you back what it evaluates to." Chirp, yawning at the soft moss, agreed to
try.

Write a Clojure expression that computes the smallest of 1, 2, 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(min 1 2 3)"}}]}
```

### G2-04 record 3

**form**: `(min 1 2 3)`  •  **expected**: `1`

```
Two creatures of the meadow approached the coming winter very differently.

With a twig, Skip the grasshopper marked out a wager in the garden: whoever
guessed the result of `(min 1 2 3)` first would win the right to
choose the next song. Tic the ant, her eyes always on the path, said it was easier
to ask the REPL about the form (min 1 2 3) than to argue.

What Clojure form computes the smallest of 1, 2, 3? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(min 1 2 3)"}}]}
```

### G2-04 record 4

**form**: `(min 1 2 3)`  •  **expected**: `1`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

A small audience of meadow creatures had gathered in the orchard to watch
Chirp the grasshopper attempt to outwit Toc the ant at reading the
REPL. Toc pointed to the form (min 1 2 3) and read out the form aloud:
`(min 1 2 3)`. The crowd waited to see who would correctly write the
form to submit.

Write a Clojure expression that computes the smallest of 1, 2, 3.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(min 1 2 3)"}}]}
```

### G2-04 record 5

**form**: `(min 1 2 3)`  •  **expected**: `1`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. All this took place in the orchard.

A wooden sign nailed to a stalk by the orchard carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(min 1 2 3)`. Skip
laughed, puffed up with pride, and declared it too easy. Toc said patiently
that the only way to be sure of the form (min 1 2 3) was to put it in the
REPL.

Write a Clojure expression that computes the smallest of 1, 2, 3.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(min 1 2 3)"}}]}
```

## G2-05: quot, rem, mod

### G2-05 record 1

**form**: `(quot 17 5)`  •  **expected**: `3`

```
Two creatures of the meadow approached the coming winter very differently.

Halfway through the morning's work, Skip the grasshopper blocked
Toc the ant's path at the edge of the woods and refused to step aside until someone
could prove what the form `(quot 17 5)` evaluated to. Skip
called it impossible. Toc the ant, walking up at her usual
pace, simply said: "Submit the form (quot 17 5) to the REPL. Whatever comes
back is the answer."

Write a form whose evaluation gives the integer quotient of 17 by 5.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(quot 17 5)"}}]}
```

### G2-05 record 2

**form**: `(quot 17 5)`  •  **expected**: `3`

```
Two creatures of the meadow approached the coming winter very differently. All this took place atop the hilltop.

"There is no need to evaluate that," Hum the grasshopper said,
with great whoops of laughter. "Anyone can see what the form (quot 17 5) comes to."
Tic the ant, who atop the hilltop had grown used to such claims, asked
them to actually write the form `(quot 17 5)` and
submit it to the REPL — just to be sure.

Question: write a Clojure expression for the integer quotient of 17 by 5.

---

{"tool_calls":[{"name":"eval","args":{"form":"(quot 17 5)"}}]}
```

### G2-05 record 3

**form**: `(quot 17 5)`  •  **expected**: `3`

```
Two creatures of the meadow approached the coming winter very differently. This was near the woods.

Tic the ant and Skip the grasshopper stopped in the woods where someone had
written the form (quot 17 5) on a flat stone. Skip, swaggering through the underbrush,
declared that she could see the answer at a glance.
Tic, her eyes always on the path, suggested they actually evaluate the form
`(quot 17 5)` in the REPL and read off whatever it returned.

What Clojure form computes the integer quotient of 17 by 5? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(quot 17 5)"}}]}
```

### G2-05 record 4

**form**: `(quot 17 5)`  •  **expected**: `3`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

A wooden sign nailed to a stalk at the edge of the farm carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(quot 17 5)`. Hum
laughed, swaggering through the underbrush, and declared it too easy. Tic said patiently
that the only way to be sure of the form (quot 17 5) was to put it in the
REPL.

Write a Clojure expression that computes the integer quotient of 17 by 5.

---

{"tool_calls":[{"name":"eval","args":{"form":"(quot 17 5)"}}]}
```

### G2-05 record 5

**form**: `(quot 17 5)`  •  **expected**: `3`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

At the edge of a stockpile atop the hilltop, Hum the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(quot 17 5)`
first would win the right to set the next day's count.
Toc the ant, her eyes always on the path, said it was simpler to type the form into
the REPL than to argue about the form (quot 17 5).

What Clojure form computes the integer quotient of 17 by 5? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(quot 17 5)"}}]}
```

## G2-06: inc and dec

### G2-06 record 1

**form**: `(inc 4)`  •  **expected**: `5`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Tic the ant had been laying out a chain of small computations on a
slate near the woods — one operation, then another, all to settle a question
Chirp the grasshopper had raised. The current form on the slate was
`(inc 4)`, and Tic explained that the form (inc 4) would be
settled the moment the form was evaluated.

Write a form whose evaluation gives the value of (inc 4).

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(inc 4)"}}]}
```

### G2-06 record 2

**form**: `(inc 4)`  •  **expected**: `5`

```
All summer long, the Ant worked while the Grasshopper sang. This was near the orchard.

Halfway through the morning's work, Hum the grasshopper blocked
Tic the ant's path by the orchard and refused to step aside until someone
could prove what the form `(inc 4)` evaluated to. Hum
called it impossible. Tic the ant, walking up at his usual
pace, simply said: "Submit the form (inc 4) to the REPL. Whatever comes
back is the answer."

Write a Clojure expression that computes the value of (inc 4).

---

{"tool_calls":[{"name":"eval","args":{"form":"(inc 4)"}}]}
```

### G2-06 record 3

**form**: `(inc 4)`  •  **expected**: `5`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

"Whatever `(inc 4)` comes to," Hum the grasshopper declared
boasting at every turn in the orchard, "I'll wager I know it without typing it."
Toc the ant, untroubled by what others thought, picked up a stick and drew
the form (inc 4) in the dust. "Then write the form," she
said. "The REPL will have the last word."

Write a Clojure expression that computes the value of (inc 4).

---

{"tool_calls":[{"name":"eval","args":{"form":"(inc 4)"}}]}
```

### G2-06 record 4

**form**: `(inc 4)`  •  **expected**: `5`

```
Two creatures of the meadow approached the coming winter very differently. All this took place at the edge of the forest.

Toc the ant had been trying to teach Skip the grasshopper how the REPL
works. "Look here," she said, pointing to the form (inc 4).
"You hand the form `(inc 4)` to the runtime, and the runtime hands
you back what it evaluates to." Skip, weary from the morning's effort, agreed to
try.

Question: write a Clojure expression for the value of (inc 4).

---

{"tool_calls":[{"name":"eval","args":{"form":"(inc 4)"}}]}
```

### G2-06 record 5

**form**: `(inc 4)`  •  **expected**: `5`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. This was in the meadow.

Bit the ant had been trying to teach Skip the grasshopper how the REPL
works. "Look here," they said, pointing to the form (inc 4).
"You hand the form `(inc 4)` to the runtime, and the runtime hands
you back what it evaluates to." Skip, lulled by the gentle wind, agreed to
try.

Question: write a Clojure expression for the value of (inc 4).

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(inc 4)"}}]}
```

## G2-07: abs (absolute value)

### G2-07 record 1

**form**: `(Math/abs -7)`  •  **expected**: `7`

```
Two creatures of the meadow approached the coming winter very differently.

A small audience of meadow creatures had gathered by the forest to watch
Hum the grasshopper attempt to outwit Tic the ant at reading the
REPL. Tic pointed to the form (Math/abs -7) and read out the form aloud:
`(Math/abs -7)`. The crowd waited to see who would correctly write the
form to submit.

Question: write a Clojure expression for the absolute value of -7.

---

{"tool_calls":[{"name":"eval","args":{"form":"(Math/abs -7)"}}]}
```

### G2-07 record 2

**form**: `(Math/abs -7)`  •  **expected**: `7`

```
All summer long, the Ant worked while the Grasshopper sang. All this took place at the edge of the farm.

A wooden sign nailed to a stalk in the farm carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(Math/abs -7)`. Hum
laughed, with great whoops of laughter, and declared it too easy. Toc said patiently
that the only way to be sure of the form (Math/abs -7) was to put it in the
REPL.

Write a Clojure expression that computes the absolute value of -7.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(Math/abs -7)"}}]}
```

### G2-07 record 3

**form**: `(Math/abs -7)`  •  **expected**: `7`

```
All summer long, the Ant worked while the Grasshopper sang.

With a twig, Skip the grasshopper marked out a wager at the edge of the orchard: whoever
guessed the result of `(Math/abs -7)` first would win the right to
choose the next song. Bit the ant, saying very little, said it was easier
to ask the REPL about the form (Math/abs -7) than to argue.

Question: write a Clojure expression for the absolute value of -7.

---

{"tool_calls":[{"name":"eval","args":{"form":"(Math/abs -7)"}}]}
```

### G2-07 record 4

**form**: `(Math/abs -7)`  •  **expected**: `7`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Toc the ant had been laying out a chain of small computations on a
slate near the orchard — one operation, then another, all to settle a question
Hum the grasshopper had raised. The current form on the slate was
`(Math/abs -7)`, and Toc explained that the form (Math/abs -7) would be
settled the moment the form was evaluated.

Write a form whose evaluation gives the absolute value of -7.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(Math/abs -7)"}}]}
```

### G2-07 record 5

**form**: `(Math/abs -7)`  •  **expected**: `7`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. This was atop the hilltop.

"Whatever `(Math/abs -7)` comes to," Chirp the grasshopper declared
puffed up with pride near the hilltop, "I'll wager I know it without typing it."
Toc the ant, her eyes always on the path, picked up a stick and drew
the form (Math/abs -7) in the dust. "Then write the form," she
said. "The REPL will have the last word."

Question: write a Clojure expression for the absolute value of -7.

---

{"tool_calls":[{"name":"eval","args":{"form":"(Math/abs -7)"}}]}
```

## G2-08: Arithmetic on ratios

### G2-08 record 1

**form**: `(+ 1/2 1/4)`  •  **expected**: `'3/4'`

```
Two creatures of the meadow approached the coming winter very differently. It happened on the hilltop.

At the edge of a stockpile atop the hilltop, Chirp the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(+ 1/2 1/4)`
first would win the right to set the next day's count.
Tic the ant, without complaint, said it was simpler to type the form into
the REPL than to argue about the form (+ 1/2 1/4).

What Clojure form computes the value of one-half plus one-quarter? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1/2 1/4)"}}]}
```

### G2-08 record 2

**form**: `(+ 1/2 1/4)`  •  **expected**: `'3/4'`

```
Two creatures of the meadow approached the coming winter very differently. All this took place by the garden.

Skip the grasshopper chalked a wager on a flat slate by the garden: whoever
predicted the result of `(+ 1/2 1/4)` first would set the next day's
ration. Tic the ant, her eyes always on the path, said it would be simpler to type
the form into the REPL than to bicker about the form (+ 1/2 1/4).

Question: write a Clojure expression for the value of one-half plus one-quarter.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1/2 1/4)"}}]}
```

### G2-08 record 3

**form**: `(+ 1/2 1/4)`  •  **expected**: `'3/4'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. This was at the edge of the forest.

With a twig, Hum the grasshopper marked out a wager in the forest: whoever
guessed the result of `(+ 1/2 1/4)` first would win the right to
choose the next song. Bit the ant, her eyes always on the path, said it was easier
to ask the REPL about the form (+ 1/2 1/4) than to argue.

Write a form whose evaluation gives the value of one-half plus one-quarter.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1/2 1/4)"}}]}
```

### G2-08 record 4

**form**: `(+ 1/2 1/4)`  •  **expected**: `'3/4'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Chirp the grasshopper chalked a wager on a flat slate near the farm: whoever
predicted the result of `(+ 1/2 1/4)` first would set the next day's
ration. Tic the ant, with steady, careful steps, said it would be simpler to type
the form into the REPL than to bicker about the form (+ 1/2 1/4).

Question: write a Clojure expression for the value of one-half plus one-quarter.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1/2 1/4)"}}]}
```

### G2-08 record 5

**form**: `(+ 1/2 1/4)`  •  **expected**: `'3/4'`

```
All summer long, the Ant worked while the Grasshopper sang.

Toc the ant had been laying out a chain of small computations on a
slate at the edge of the garden — one operation, then another, all to settle a question
Chirp the grasshopper had raised. The current form on the slate was
`(+ 1/2 1/4)`, and Toc explained that the form (+ 1/2 1/4) would be
settled the moment the form was evaluated.

Write a form whose evaluation gives the value of one-half plus one-quarter.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1/2 1/4)"}}]}
```

## G2-09: Floats vs ints

### G2-09 record 1

**form**: `(/ 10 2)`  •  **expected**: `5`

```
Two creatures of the meadow approached the coming winter very differently. All this took place in the forest.

Halfway through the morning's work, Chirp the grasshopper blocked
Tic the ant's path at the edge of the forest and refused to step aside until someone
could prove what the form `(/ 10 2)` evaluated to. Chirp
called it impossible. Tic the ant, walking up at his usual
pace, simply said: "Submit the form (/ 10 2) to the REPL. Whatever comes
back is the answer."

Write a Clojure expression that computes the integer quotient when division is exact.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(/ 10 2)"}}]}
```

### G2-09 record 2

**form**: `(/ 10 2)`  •  **expected**: `5`

```
Two creatures of the meadow approached the coming winter very differently.

Toc the ant and Hum the grasshopper stopped at the edge of the meadow where someone had
written the form (/ 10 2) on a flat stone. Hum, as if the race were already won,
declared that they could see the answer at a glance.
Toc, without complaint, suggested they actually evaluate the form
`(/ 10 2)` in the REPL and read off whatever it returned.

Question: write a Clojure expression for the integer quotient when division is exact.

---

{"tool_calls":[{"name":"eval","args":{"form":"(/ 10 2)"}}]}
```

### G2-09 record 3

**form**: `(/ 10 2)`  •  **expected**: `5`

```
All summer long, the Ant worked while the Grasshopper sang. This was by the farm.

Halfway through the morning's work, Skip the grasshopper blocked
Toc the ant's path in the farm and refused to step aside until someone
could prove what the form `(/ 10 2)` evaluated to. Skip
called it impossible. Toc the ant, walking up at her usual
pace, simply said: "Submit the form (/ 10 2) to the REPL. Whatever comes
back is the answer."

Write a form whose evaluation gives the integer quotient when division is exact.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(/ 10 2)"}}]}
```

### G2-09 record 4

**form**: `(/ 10 2)`  •  **expected**: `5`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. It happened at the edge of the garden.

A wooden sign nailed to a stalk near the garden carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(/ 10 2)`. Skip
laughed, as if the race were already won, and declared it too easy. Tic said patiently
that the only way to be sure of the form (/ 10 2) was to put it in the
REPL.

Write a form whose evaluation gives the integer quotient when division is exact.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(/ 10 2)"}}]}
```

### G2-09 record 5

**form**: `(/ 10 2)`  •  **expected**: `5`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. It happened at the edge of the meadow.

With a twig, Hum the grasshopper marked out a wager near the meadow: whoever
guessed the result of `(/ 10 2)` first would win the right to
choose the next song. Toc the ant, untroubled by what others thought, said it was easier
to ask the REPL about the form (/ 10 2) than to argue.

What Clojure form computes the integer quotient when division is exact? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(/ 10 2)"}}]}
```

## G2-10: Power by repeated multiplication

### G2-10 record 1

**form**: `(* 2 2 2)`  •  **expected**: `8`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Bit the ant and Skip the grasshopper stopped near the woods where someone had
written the form (* 2 2 2) — 2^3 by repeated multiplication on a flat stone. Skip, boasting at every turn,
declared that she could see the answer at a glance.
Bit, with steady, careful steps, suggested they actually evaluate the form
`(* 2 2 2)` in the REPL and read off whatever it returned.

What Clojure form computes the result of two cubed? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(* 2 2 2)"}}]}
```

### G2-10 record 2

**form**: `(* 2 2 2)`  •  **expected**: `8`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Chirp the grasshopper chalked a wager on a flat slate at the edge of the garden: whoever
predicted the result of `(* 2 2 2)` first would set the next day's
ration. Tic the ant, her eyes always on the path, said it would be simpler to type
the form into the REPL than to bicker about the form (* 2 2 2) — 2^3 by repeated multiplication.

Write a form whose evaluation gives the result of two cubed.

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 2 2 2)"}}]}
```

### G2-10 record 3

**form**: `(* 2 2 2)`  •  **expected**: `8`

```
All summer long, the Ant worked while the Grasshopper sang.

"There is no need to evaluate that," Chirp the grasshopper said,
with a smug grin. "Anyone can see what the form (* 2 2 2) — 2^3 by repeated multiplication comes to."
Toc the ant, who by the garden had grown used to such claims, asked
him to actually write the form `(* 2 2 2)` and
submit it to the REPL — just to be sure.

Write a form whose evaluation gives the result of two cubed.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(* 2 2 2)"}}]}
```

### G2-10 record 4

**form**: `(* 2 2 2)`  •  **expected**: `8`

```
Two creatures of the meadow approached the coming winter very differently. This was at the edge of the farm.

A small audience of meadow creatures had gathered in the farm to watch
Skip the grasshopper attempt to outwit Bit the ant at reading the
REPL. Bit pointed to the form (* 2 2 2) — 2^3 by repeated multiplication and read out the form aloud:
`(* 2 2 2)`. The crowd waited to see who would correctly write the
form to submit.

Write a Clojure expression that computes the result of two cubed.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(* 2 2 2)"}}]}
```

### G2-10 record 5

**form**: `(* 2 2 2)`  •  **expected**: `8`

```
All summer long, the Ant worked while the Grasshopper sang. It happened at the edge of the farm.

A wooden sign nailed to a stalk in the farm carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(* 2 2 2)`. Chirp
laughed, boasting at every turn, and declared it too easy. Bit said patiently
that the only way to be sure of the form (* 2 2 2) — 2^3 by repeated multiplication was to put it in the
REPL.

Write a Clojure expression that computes the result of two cubed.

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 2 2 2)"}}]}
```

## G2-11: String concatenation with str

### G2-11 record 1

**form**: `(str "a" "b")`  •  **expected**: `'ab'`

```
Two creatures of the meadow approached the coming winter very differently. It happened in the meadow.

Halfway through the morning's work, Chirp the grasshopper blocked
Tic the ant's path in the meadow and refused to step aside until someone
could prove what the form `(str "a" "b")` evaluated to. Chirp
called it impossible. Tic the ant, walking up at his usual
pace, simply said: "Submit the form (str "a" "b") to the REPL. Whatever comes
back is the answer."

Question: write a Clojure expression for the concatenated string ab.

---

{"tool_calls":[{"name":"eval","args":{"form":"(str \"a\" \"b\")"}}]}
```

### G2-11 record 2

**form**: `(str "a" "b")`  •  **expected**: `'ab'`

```
Two creatures of the meadow approached the coming winter very differently. This was near the forest.

At the edge of a stockpile at the edge of the forest, Skip the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(str "a" "b")`
first would win the right to set the next day's count.
Toc the ant, with steady, careful steps, said it was simpler to type the form into
the REPL than to argue about the form (str "a" "b").

Write a form whose evaluation gives the concatenated string ab.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(str \"a\" \"b\")"}}]}
```

### G2-11 record 3

**form**: `(str "a" "b")`  •  **expected**: `'ab'`

```
Two creatures of the meadow approached the coming winter very differently. This was at the edge of the forest.

A wooden sign nailed to a stalk in the forest carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(str "a" "b")`. Skip
laughed, puffed up with pride, and declared it too easy. Bit said patiently
that the only way to be sure of the form (str "a" "b") was to put it in the
REPL.

Question: write a Clojure expression for the concatenated string ab.

---

{"tool_calls":[{"name":"eval","args":{"form":"(str \"a\" \"b\")"}}]}
```

### G2-11 record 4

**form**: `(str "a" "b")`  •  **expected**: `'ab'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Tic the ant had been keeping a small leather notebook of every form
he had successfully evaluated. Today in the woods, the next entry
was the form (str "a" "b"). Hum the grasshopper peered over
his shoulder at the form `(str "a" "b")` and asked what it
would come out to.

What Clojure form computes the concatenated string ab? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(str \"a\" \"b\")"}}]}
```

### G2-11 record 5

**form**: `(str "a" "b")`  •  **expected**: `'ab'`

```
All summer long, the Ant worked while the Grasshopper sang.

A wooden sign nailed to a stalk by the garden carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(str "a" "b")`. Skip
laughed, swaggering through the underbrush, and declared it too easy. Bit said patiently
that the only way to be sure of the form (str "a" "b") was to put it in the
REPL.

Write a form whose evaluation gives the concatenated string ab.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(str \"a\" \"b\")"}}]}
```

## G2-12: print and println

### G2-12 record 1

**form**: `(with-out-str (print "x"))`  •  **expected**: `'x'`

```
Two creatures of the meadow approached the coming winter very differently.

At the edge of a stockpile atop the hilltop, Skip the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(with-out-str (print "x"))`
first would win the right to set the next day's count.
Toc the ant, stepping deliberately, said it was simpler to type the form into
the REPL than to argue about a captured (print "x").

Write a form whose evaluation gives the captured output of (print "x").

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (print \"x\"))"}}]}
```

### G2-12 record 2

**form**: `(with-out-str (print "x"))`  •  **expected**: `'x'`

```
Two creatures of the meadow approached the coming winter very differently.

Bit the ant had been laying out a chain of small computations on a
slate at the edge of the garden — one operation, then another, all to settle a question
Hum the grasshopper had raised. The current form on the slate was
`(with-out-str (print "x"))`, and Bit explained that a captured (print "x") would be
settled the moment the form was evaluated.

Write a form whose evaluation gives the captured output of (print "x").

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (print \"x\"))"}}]}
```

### G2-12 record 3

**form**: `(with-out-str (print "x"))`  •  **expected**: `'x'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. It happened at the edge of the woods.

A wooden sign nailed to a stalk in the woods carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(with-out-str (print "x"))`. Hum
laughed, with great whoops of laughter, and declared it too easy. Toc said patiently
that the only way to be sure of a captured (print "x") was to put it in the
REPL.

Write a form whose evaluation gives the captured output of (print "x").

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (print \"x\"))"}}]}
```

### G2-12 record 4

**form**: `(with-out-str (print "x"))`  •  **expected**: `'x'`

```
Two creatures of the meadow approached the coming winter very differently.

A wooden sign nailed to a stalk in the garden carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(with-out-str (print "x"))`. Skip
laughed, with great whoops of laughter, and declared it too easy. Tic said patiently
that the only way to be sure of a captured (print "x") was to put it in the
REPL.

Write a Clojure expression that computes the captured output of (print "x").

---

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (print \"x\"))"}}]}
```

### G2-12 record 5

**form**: `(with-out-str (print "x"))`  •  **expected**: `'x'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. It happened near the forest.

Halfway through the morning's work, Chirp the grasshopper blocked
Toc the ant's path at the edge of the forest and refused to step aside until someone
could prove what the form `(with-out-str (print "x"))` evaluated to. Chirp
called it impossible. Toc the ant, walking up at her usual
pace, simply said: "Submit a captured (print "x") to the REPL. Whatever comes
back is the answer."

Write a Clojure expression that computes the captured output of (print "x").

---

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (print \"x\"))"}}]}
```

## G2-13: and / or — short-circuit and value

### G2-13 record 1

**form**: `(and 1 2 3)`  •  **expected**: `3`

```
Two creatures of the meadow approached the coming winter very differently.

At the edge of a stockpile at the edge of the orchard, Hum the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(and 1 2 3)`
first would win the right to set the next day's count.
Toc the ant, with steady, careful steps, said it was simpler to type the form into
the REPL than to argue about the form (and 1 2 3).

Write a form whose evaluation gives the last truthy value of and.

---

{"tool_calls":[{"name":"eval","args":{"form":"(and 1 2 3)"}}]}
```

### G2-13 record 2

**form**: `(and 1 2 3)`  •  **expected**: `3`

```
Two creatures of the meadow approached the coming winter very differently.

A wooden sign nailed to a stalk by the farm carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(and 1 2 3)`. Chirp
laughed, swaggering through the underbrush, and declared it too easy. Tic said patiently
that the only way to be sure of the form (and 1 2 3) was to put it in the
REPL.

Write a Clojure expression that computes the last truthy value of and.

---

{"tool_calls":[{"name":"eval","args":{"form":"(and 1 2 3)"}}]}
```

### G2-13 record 3

**form**: `(and 1 2 3)`  •  **expected**: `3`

```
All summer long, the Ant worked while the Grasshopper sang. It happened atop the hilltop.

Tic the ant had been keeping a small leather notebook of every form
he had successfully evaluated. Today on the hilltop, the next entry
was the form (and 1 2 3). Chirp the grasshopper peered over
his shoulder at the form `(and 1 2 3)` and asked what it
would come out to.

Write a Clojure expression that computes the last truthy value of and.

---

{"tool_calls":[{"name":"eval","args":{"form":"(and 1 2 3)"}}]}
```

### G2-13 record 4

**form**: `(and 1 2 3)`  •  **expected**: `3`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Chirp the grasshopper chalked a wager on a flat slate by the farm: whoever
predicted the result of `(and 1 2 3)` first would set the next day's
ration. Tic the ant, without complaint, said it would be simpler to type
the form into the REPL than to bicker about the form (and 1 2 3).

What Clojure form computes the last truthy value of and? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(and 1 2 3)"}}]}
```

### G2-13 record 5

**form**: `(and 1 2 3)`  •  **expected**: `3`

```
Two creatures of the meadow approached the coming winter very differently. All this took place in the forest.

A small audience of meadow creatures had gathered in the forest to watch
Chirp the grasshopper attempt to outwit Bit the ant at reading the
REPL. Bit pointed to the form (and 1 2 3) and read out the form aloud:
`(and 1 2 3)`. The crowd waited to see who would correctly write the
form to submit.

Question: write a Clojure expression for the last truthy value of and.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(and 1 2 3)"}}]}
```

## G2-14: not — turning truthy to false

### G2-14 record 1

**form**: `(not true)`  •  **expected**: `False`

```
Two creatures of the meadow approached the coming winter very differently.

Toc the ant had been trying to teach Skip the grasshopper how the REPL
works. "Look here," she said, pointing to the form (not true).
"You hand the form `(not true)` to the runtime, and the runtime hands
you back what it evaluates to." Skip, lulled by the gentle wind, agreed to
try.

Write a Clojure expression that computes the negation of true.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(not true)"}}]}
```

### G2-14 record 2

**form**: `(not true)`  •  **expected**: `False`

```
Two creatures of the meadow approached the coming winter very differently.

At the edge of a stockpile by the woods, Hum the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(not true)`
first would win the right to set the next day's count.
Toc the ant, without complaint, said it was simpler to type the form into
the REPL than to argue about the form (not true).

Write a form whose evaluation gives the negation of true.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(not true)"}}]}
```

### G2-14 record 3

**form**: `(not true)`  •  **expected**: `False`

```
All summer long, the Ant worked while the Grasshopper sang.

Hum the grasshopper chalked a wager on a flat slate at the edge of the hilltop: whoever
predicted the result of `(not true)` first would set the next day's
ration. Bit the ant, stepping deliberately, said it would be simpler to type
the form into the REPL than to bicker about the form (not true).

What Clojure form computes the negation of true? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(not true)"}}]}
```

### G2-14 record 4

**form**: `(not true)`  •  **expected**: `False`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Chirp the grasshopper chalked a wager on a flat slate at the edge of the farm: whoever
predicted the result of `(not true)` first would set the next day's
ration. Tic the ant, saying very little, said it would be simpler to type
the form into the REPL than to bicker about the form (not true).

Write a form whose evaluation gives the negation of true.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(not true)"}}]}
```

### G2-14 record 5

**form**: `(not true)`  •  **expected**: `False`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

"There is no need to evaluate that," Chirp the grasshopper said,
puffed up with pride. "Anyone can see what the form (not true) comes to."
Toc the ant, who near the hilltop had grown used to such claims, asked
him to actually write the form `(not true)` and
submit it to the REPL — just to be sure.

Write a Clojure expression that computes the negation of true.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(not true)"}}]}
```

## G2-15: Falsey values

### G2-15 record 1

**form**: `(boolean nil)`  •  **expected**: `False`

```
Two creatures of the meadow approached the coming winter very differently.

Bit the ant had been laying out a chain of small computations on a
slate near the meadow — one operation, then another, all to settle a question
Skip the grasshopper had raised. The current form on the slate was
`(boolean nil)`, and Bit explained that the form (boolean nil) would be
settled the moment the form was evaluated.

Write a form whose evaluation gives the truthiness of nil.

---

{"tool_calls":[{"name":"eval","args":{"form":"(boolean nil)"}}]}
```

### G2-15 record 2

**form**: `(boolean nil)`  •  **expected**: `False`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Hum the grasshopper chalked a wager on a flat slate by the garden: whoever
predicted the result of `(boolean nil)` first would set the next day's
ration. Toc the ant, her eyes always on the path, said it would be simpler to type
the form into the REPL than to bicker about the form (boolean nil).

Write a form whose evaluation gives the truthiness of nil.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(boolean nil)"}}]}
```

### G2-15 record 3

**form**: `(boolean nil)`  •  **expected**: `False`

```
Two creatures of the meadow approached the coming winter very differently.

With a twig, Hum the grasshopper marked out a wager near the meadow: whoever
guessed the result of `(boolean nil)` first would win the right to
choose the next song. Bit the ant, with steady, careful steps, said it was easier
to ask the REPL about the form (boolean nil) than to argue.

Write a form whose evaluation gives the truthiness of nil.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(boolean nil)"}}]}
```

### G2-15 record 4

**form**: `(boolean nil)`  •  **expected**: `False`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Tic the ant had been trying to teach Hum the grasshopper how the REPL
works. "Look here," he said, pointing to the form (boolean nil).
"You hand the form `(boolean nil)` to the runtime, and the runtime hands
you back what it evaluates to." Hum, yawning at the soft moss, agreed to
try.

Question: write a Clojure expression for the truthiness of nil.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(boolean nil)"}}]}
```

### G2-15 record 5

**form**: `(boolean nil)`  •  **expected**: `False`

```
Two creatures of the meadow approached the coming winter very differently. All this took place at the edge of the garden.

Toc the ant and Skip the grasshopper stopped in the garden where someone had
written the form (boolean nil) on a flat stone. Skip, with a smug grin,
declared that she could see the answer at a glance.
Toc, with steady, careful steps, suggested they actually evaluate the form
`(boolean nil)` in the REPL and read off whatever it returned.

Write a Clojure expression that computes the truthiness of nil.

---

{"tool_calls":[{"name":"eval","args":{"form":"(boolean nil)"}}]}
```

## G2-16: Coercion pitfalls in if

### G2-16 record 1

**form**: `(if 0 :a :b)`  •  **expected**: `':a'`

```
Two creatures of the meadow approached the coming winter very differently. All this took place at the edge of the farm.

"There is no need to evaluate that," Hum the grasshopper said,
as if the race were already won. "Anyone can see what the form (if 0 :a :b) — 0 is truthy in Clojure comes to."
Toc the ant, who by the farm had grown used to such claims, asked
them to actually write the form `(if 0 :a :b)` and
submit it to the REPL — just to be sure.

Write a form whose evaluation gives which branch (if 0 ...) takes.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(if 0 :a :b)"}}]}
```

### G2-16 record 2

**form**: `(if 0 :a :b)`  •  **expected**: `':a'`

```
All summer long, the Ant worked while the Grasshopper sang.

Hum the grasshopper chalked a wager on a flat slate in the woods: whoever
predicted the result of `(if 0 :a :b)` first would set the next day's
ration. Tic the ant, her eyes always on the path, said it would be simpler to type
the form into the REPL than to bicker about the form (if 0 :a :b) — 0 is truthy in Clojure.

What Clojure form computes which branch (if 0 ...) takes? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(if 0 :a :b)"}}]}
```

### G2-16 record 3

**form**: `(if 0 :a :b)`  •  **expected**: `':a'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. All this took place by the woods.

"There is no need to evaluate that," Chirp the grasshopper said,
with a smug grin. "Anyone can see what the form (if 0 :a :b) — 0 is truthy in Clojure comes to."
Tic the ant, who by the woods had grown used to such claims, asked
him to actually write the form `(if 0 :a :b)` and
submit it to the REPL — just to be sure.

Write a form whose evaluation gives which branch (if 0 ...) takes.

---

{"tool_calls":[{"name":"eval","args":{"form":"(if 0 :a :b)"}}]}
```

### G2-16 record 4

**form**: `(if 0 :a :b)`  •  **expected**: `':a'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

A wooden sign nailed to a stalk near the forest carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(if 0 :a :b)`. Chirp
laughed, boasting at every turn, and declared it too easy. Bit said patiently
that the only way to be sure of the form (if 0 :a :b) — 0 is truthy in Clojure was to put it in the
REPL.

Write a Clojure expression that computes which branch (if 0 ...) takes.

---

{"tool_calls":[{"name":"eval","args":{"form":"(if 0 :a :b)"}}]}
```

### G2-16 record 5

**form**: `(if 0 :a :b)`  •  **expected**: `':a'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. All this took place near the garden.

"There is no need to evaluate that," Skip the grasshopper said,
swaggering through the underbrush. "Anyone can see what the form (if 0 :a :b) — 0 is truthy in Clojure comes to."
Bit the ant, who at the edge of the garden had grown used to such claims, asked
her to actually write the form `(if 0 :a :b)` and
submit it to the REPL — just to be sure.

Write a form whose evaluation gives which branch (if 0 ...) takes.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(if 0 :a :b)"}}]}
```

## G2-17: Keyword as function

### G2-17 record 1

**form**: `(:a {:a 1 :b 2})`  •  **expected**: `1`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. All this took place by the meadow.

"There is no need to evaluate that," Skip the grasshopper said,
with a smug grin. "Anyone can see what the form (:a {:a 1 :b 2}) comes to."
Tic the ant, who in the meadow had grown used to such claims, asked
her to actually write the form `(:a {:a 1 :b 2})` and
submit it to the REPL — just to be sure.

Question: write a Clojure expression for the value at :a in the map.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:a {:a 1 :b 2})"}}]}
```

### G2-17 record 2

**form**: `(:a {:a 1 :b 2})`  •  **expected**: `1`

```
Two creatures of the meadow approached the coming winter very differently. All this took place in the forest.

"Whatever `(:a {:a 1 :b 2})` comes to," Hum the grasshopper declared
as if the race were already won near the forest, "I'll wager I know it without typing it."
Bit the ant, stepping deliberately, picked up a stick and drew
the form (:a {:a 1 :b 2}) in the dust. "Then write the form," they
said. "The REPL will have the last word."

Write a form whose evaluation gives the value at :a in the map.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:a {:a 1 :b 2})"}}]}
```

### G2-17 record 3

**form**: `(:a {:a 1 :b 2})`  •  **expected**: `1`

```
All summer long, the Ant worked while the Grasshopper sang. It happened in the orchard.

Toc the ant and Hum the grasshopper stopped in the orchard where someone had
written the form (:a {:a 1 :b 2}) on a flat stone. Hum, with great whoops of laughter,
declared that they could see the answer at a glance.
Toc, saying very little, suggested they actually evaluate the form
`(:a {:a 1 :b 2})` in the REPL and read off whatever it returned.

Question: write a Clojure expression for the value at :a in the map.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:a {:a 1 :b 2})"}}]}
```

### G2-17 record 4

**form**: `(:a {:a 1 :b 2})`  •  **expected**: `1`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

A wooden sign nailed to a stalk in the garden carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(:a {:a 1 :b 2})`. Chirp
laughed, puffed up with pride, and declared it too easy. Toc said patiently
that the only way to be sure of the form (:a {:a 1 :b 2}) was to put it in the
REPL.

Write a Clojure expression that computes the value at :a in the map.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:a {:a 1 :b 2})"}}]}
```

### G2-17 record 5

**form**: `(:a {:a 1 :b 2})`  •  **expected**: `1`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Toc the ant had been laying out a chain of small computations on a
slate by the farm — one operation, then another, all to settle a question
Hum the grasshopper had raised. The current form on the slate was
`(:a {:a 1 :b 2})`, and Toc explained that the form (:a {:a 1 :b 2}) would be
settled the moment the form was evaluated.

What Clojure form computes the value at :a in the map? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(:a {:a 1 :b 2})"}}]}
```

## G2-18: Symbols evaluate to their bindings

### G2-18 record 1

**form**: `(do (def grain 5) grain)`  •  **expected**: `5`

```
All summer long, the Ant worked while the Grasshopper sang.

"Whatever `(do (def grain 5) grain)` comes to," Skip the grasshopper declared
puffed up with pride by the farm, "I'll wager I know it without typing it."
Toc the ant, with steady, careful steps, picked up a stick and drew
binding grain to 5, then referring to grain in the dust. "Then write the form," she
said. "The REPL will have the last word."

What Clojure form computes the value the symbol grain evaluates to? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def grain 5) grain)"}}]}
```

### G2-18 record 2

**form**: `(do (def grain 5) grain)`  •  **expected**: `5`

```
All summer long, the Ant worked while the Grasshopper sang. All this took place near the farm.

With a twig, Hum the grasshopper marked out a wager at the edge of the farm: whoever
guessed the result of `(do (def grain 5) grain)` first would win the right to
choose the next song. Bit the ant, with steady, careful steps, said it was easier
to ask the REPL about binding grain to 5, then referring to grain than to argue.

Write a form whose evaluation gives the value the symbol grain evaluates to.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def grain 5) grain)"}}]}
```

### G2-18 record 3

**form**: `(do (def grain 5) grain)`  •  **expected**: `5`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

"There is no need to evaluate that," Hum the grasshopper said,
as if the race were already won. "Anyone can see what binding grain to 5, then referring to grain comes to."
Toc the ant, who in the farm had grown used to such claims, asked
them to actually write the form `(do (def grain 5) grain)` and
submit it to the REPL — just to be sure.

Write a Clojure expression that computes the value the symbol grain evaluates to.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def grain 5) grain)"}}]}
```

### G2-18 record 4

**form**: `(do (def grain 5) grain)`  •  **expected**: `5`

```
All summer long, the Ant worked while the Grasshopper sang.

Tic the ant had been trying to teach Skip the grasshopper how the REPL
works. "Look here," he said, pointing to binding grain to 5, then referring to grain.
"You hand the form `(do (def grain 5) grain)` to the runtime, and the runtime hands
you back what it evaluates to." Skip, yawning at the soft moss, agreed to
try.

Question: write a Clojure expression for the value the symbol grain evaluates to.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def grain 5) grain)"}}]}
```

### G2-18 record 5

**form**: `(do (def grain 5) grain)`  •  **expected**: `5`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. All this took place in the garden.

Halfway through the morning's work, Hum the grasshopper blocked
Toc the ant's path near the garden and refused to step aside until someone
could prove what the form `(do (def grain 5) grain)` evaluated to. Hum
called it impossible. Toc the ant, walking up at her usual
pace, simply said: "Submit binding grain to 5, then referring to grain to the REPL. Whatever comes
back is the answer."

Write a form whose evaluation gives the value the symbol grain evaluates to.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def grain 5) grain)"}}]}
```

## G2-19: Quoting introduction

### G2-19 record 1

**form**: `'ant`  •  **expected**: `'ant'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Toc the ant had been laying out a chain of small computations on a
slate in the meadow — one operation, then another, all to settle a question
Skip the grasshopper had raised. The current form on the slate was
`'ant`, and Toc explained that the quoted symbol 'ant would be
settled the moment the form was evaluated.

Write a form whose evaluation gives the quoted symbol's value.

---

{"tool_calls":[{"name":"eval","args":{"form":"'ant"}}]}
```

### G2-19 record 2

**form**: `'ant`  •  **expected**: `'ant'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Hum the grasshopper chalked a wager on a flat slate at the edge of the woods: whoever
predicted the result of `'ant` first would set the next day's
ration. Toc the ant, her eyes always on the path, said it would be simpler to type
the form into the REPL than to bicker about the quoted symbol 'ant.

Write a Clojure expression that computes the quoted symbol's value.

---

{"tool_calls":[{"name":"eval","args":{"form":"'ant"}}]}
```

### G2-19 record 3

**form**: `'ant`  •  **expected**: `'ant'`

```
All summer long, the Ant worked while the Grasshopper sang.

"There is no need to evaluate that," Chirp the grasshopper said,
puffed up with pride. "Anyone can see what the quoted symbol 'ant comes to."
Toc the ant, who at the edge of the forest had grown used to such claims, asked
him to actually write the form `'ant` and
submit it to the REPL — just to be sure.

Write a form whose evaluation gives the quoted symbol's value.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"'ant"}}]}
```

### G2-19 record 4

**form**: `'ant`  •  **expected**: `'ant'`

```
All summer long, the Ant worked while the Grasshopper sang.

Bit the ant had been laying out a chain of small computations on a
slate near the woods — one operation, then another, all to settle a question
Hum the grasshopper had raised. The current form on the slate was
`'ant`, and Bit explained that the quoted symbol 'ant would be
settled the moment the form was evaluated.

Write a form whose evaluation gives the quoted symbol's value.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"'ant"}}]}
```

### G2-19 record 5

**form**: `'ant`  •  **expected**: `'ant'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

With a twig, Hum the grasshopper marked out a wager near the hilltop: whoever
guessed the result of `'ant` first would win the right to
choose the next song. Tic the ant, saying very little, said it was easier
to ask the REPL about the quoted symbol 'ant than to argue.

Question: write a Clojure expression for the quoted symbol's value.

---

{"tool_calls":[{"name":"eval","args":{"form":"'ant"}}]}
```

## G2-20: Numeric tower (auto-promotion)

### G2-20 record 1

**form**: `(* 1000 1000)`  •  **expected**: `1000000`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. It happened in the garden.

With a twig, Chirp the grasshopper marked out a wager in the garden: whoever
guessed the result of `(* 1000 1000)` first would win the right to
choose the next song. Tic the ant, stepping deliberately, said it was easier
to ask the REPL about the form (* 1000 1000) than to argue.

What Clojure form computes the product of 1000 and 1000? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 1000 1000)"}}]}
```

### G2-20 record 2

**form**: `(* 1000 1000)`  •  **expected**: `1000000`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Tic the ant and Chirp the grasshopper stopped by the garden where someone had
written the form (* 1000 1000) on a flat stone. Chirp, with a smug grin,
declared that he could see the answer at a glance.
Tic, stepping deliberately, suggested they actually evaluate the form
`(* 1000 1000)` in the REPL and read off whatever it returned.

Question: write a Clojure expression for the product of 1000 and 1000.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(* 1000 1000)"}}]}
```

### G2-20 record 3

**form**: `(* 1000 1000)`  •  **expected**: `1000000`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. It happened near the woods.

Tic the ant had been keeping a small leather notebook of every form
he had successfully evaluated. Today near the woods, the next entry
was the form (* 1000 1000). Skip the grasshopper peered over
his shoulder at the form `(* 1000 1000)` and asked what it
would come out to.

Question: write a Clojure expression for the product of 1000 and 1000.

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 1000 1000)"}}]}
```

### G2-20 record 4

**form**: `(* 1000 1000)`  •  **expected**: `1000000`

```
All summer long, the Ant worked while the Grasshopper sang.

"Whatever `(* 1000 1000)` comes to," Skip the grasshopper declared
with a smug grin near the woods, "I'll wager I know it without typing it."
Tic the ant, untroubled by what others thought, picked up a stick and drew
the form (* 1000 1000) in the dust. "Then write the form," he
said. "The REPL will have the last word."

Write a Clojure expression that computes the product of 1000 and 1000.

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 1000 1000)"}}]}
```

### G2-20 record 5

**form**: `(* 1000 1000)`  •  **expected**: `1000000`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Halfway through the morning's work, Skip the grasshopper blocked
Toc the ant's path in the farm and refused to step aside until someone
could prove what the form `(* 1000 1000)` evaluated to. Skip
called it impossible. Toc the ant, walking up at her usual
pace, simply said: "Submit the form (* 1000 1000) to the REPL. Whatever comes
back is the answer."

Question: write a Clojure expression for the product of 1000 and 1000.

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 1000 1000)"}}]}
```

## G2-21: rand and rand-int

### G2-21 record 1

**form**: `(integer? (rand-int 10))`  •  **expected**: `True`

```
Two creatures of the meadow approached the coming winter very differently. It happened near the hilltop.

Halfway through the morning's work, Hum the grasshopper blocked
Tic the ant's path on the hilltop and refused to step aside until someone
could prove what the form `(integer? (rand-int 10))` evaluated to. Hum
called it impossible. Tic the ant, walking up at his usual
pace, simply said: "Submit the predicate that (rand-int 10) returns an integer to the REPL. Whatever comes
back is the answer."

What Clojure form computes whether (rand-int 10) is integer-typed? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(integer? (rand-int 10))"}}]}
```

### G2-21 record 2

**form**: `(integer? (rand-int 10))`  •  **expected**: `True`

```
All summer long, the Ant worked while the Grasshopper sang.

With a twig, Skip the grasshopper marked out a wager near the hilltop: whoever
guessed the result of `(integer? (rand-int 10))` first would win the right to
choose the next song. Toc the ant, without complaint, said it was easier
to ask the REPL about the predicate that (rand-int 10) returns an integer than to argue.

Question: write a Clojure expression for whether (rand-int 10) is integer-typed.

---

{"tool_calls":[{"name":"eval","args":{"form":"(integer? (rand-int 10))"}}]}
```

### G2-21 record 3

**form**: `(integer? (rand-int 10))`  •  **expected**: `True`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. It happened near the woods.

At the edge of a stockpile at the edge of the woods, Chirp the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(integer? (rand-int 10))`
first would win the right to set the next day's count.
Bit the ant, saying very little, said it was simpler to type the form into
the REPL than to argue about the predicate that (rand-int 10) returns an integer.

Question: write a Clojure expression for whether (rand-int 10) is integer-typed.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(integer? (rand-int 10))"}}]}
```

### G2-21 record 4

**form**: `(integer? (rand-int 10))`  •  **expected**: `True`

```
Two creatures of the meadow approached the coming winter very differently.

At the edge of a stockpile by the garden, Chirp the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(integer? (rand-int 10))`
first would win the right to set the next day's count.
Tic the ant, stepping deliberately, said it was simpler to type the form into
the REPL than to argue about the predicate that (rand-int 10) returns an integer.

What Clojure form computes whether (rand-int 10) is integer-typed? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(integer? (rand-int 10))"}}]}
```

### G2-21 record 5

**form**: `(integer? (rand-int 10))`  •  **expected**: `True`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Toc the ant had been keeping a small leather notebook of every form
she had successfully evaluated. Today at the edge of the farm, the next entry
was the predicate that (rand-int 10) returns an integer. Hum the grasshopper peered over
her shoulder at the form `(integer? (rand-int 10))` and asked what it
would come out to.

What Clojure form computes whether (rand-int 10) is integer-typed? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(integer? (rand-int 10))"}}]}
```

## G2-22: Composing pure arithmetic

### G2-22 record 1

**form**: `(quot (* 30 5) 2)`  •  **expected**: `75`

```
All summer long, the Ant worked while the Grasshopper sang. It happened by the woods.

Halfway through the morning's work, Chirp the grasshopper blocked
Toc the ant's path at the edge of the woods and refused to step aside until someone
could prove what the form `(quot (* 30 5) 2)` evaluated to. Chirp
called it impossible. Toc the ant, walking up at her usual
pace, simply said: "Submit a multi-step arithmetic form to the REPL. Whatever comes
back is the answer."

Write a form whose evaluation gives the result of dividing thirty-times-five by two.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(quot (* 30 5) 2)"}}]}
```

### G2-22 record 2

**form**: `(quot (* 30 5) 2)`  •  **expected**: `75`

```
Two creatures of the meadow approached the coming winter very differently.

Toc the ant had been trying to teach Skip the grasshopper how the REPL
works. "Look here," she said, pointing to a multi-step arithmetic form.
"You hand the form `(quot (* 30 5) 2)` to the runtime, and the runtime hands
you back what it evaluates to." Skip, weary from the morning's effort, agreed to
try.

Write a Clojure expression that computes the result of dividing thirty-times-five by two.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(quot (* 30 5) 2)"}}]}
```

### G2-22 record 3

**form**: `(quot (* 30 5) 2)`  •  **expected**: `75`

```
All summer long, the Ant worked while the Grasshopper sang.

Halfway through the morning's work, Skip the grasshopper blocked
Bit the ant's path by the woods and refused to step aside until someone
could prove what the form `(quot (* 30 5) 2)` evaluated to. Skip
called it impossible. Bit the ant, walking up at their usual
pace, simply said: "Submit a multi-step arithmetic form to the REPL. Whatever comes
back is the answer."

What Clojure form computes the result of dividing thirty-times-five by two? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(quot (* 30 5) 2)"}}]}
```

### G2-22 record 4

**form**: `(quot (* 30 5) 2)`  •  **expected**: `75`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

A small audience of meadow creatures had gathered in the woods to watch
Hum the grasshopper attempt to outwit Bit the ant at reading the
REPL. Bit pointed to a multi-step arithmetic form and read out the form aloud:
`(quot (* 30 5) 2)`. The crowd waited to see who would correctly write the
form to submit.

Question: write a Clojure expression for the result of dividing thirty-times-five by two.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(quot (* 30 5) 2)"}}]}
```

### G2-22 record 5

**form**: `(quot (* 30 5) 2)`  •  **expected**: `75`

```
Two creatures of the meadow approached the coming winter very differently. It happened at the edge of the meadow.

Tic the ant had been trying to teach Skip the grasshopper how the REPL
works. "Look here," he said, pointing to a multi-step arithmetic form.
"You hand the form `(quot (* 30 5) 2)` to the runtime, and the runtime hands
you back what it evaluates to." Skip, weary from the morning's effort, agreed to
try.

Write a Clojure expression that computes the result of dividing thirty-times-five by two.

---

{"tool_calls":[{"name":"eval","args":{"form":"(quot (* 30 5) 2)"}}]}
```


---

**Grade 2 totals: 22 subjects, 110 records.**
