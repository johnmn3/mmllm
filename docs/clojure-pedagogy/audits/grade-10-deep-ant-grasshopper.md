# Deep spot-check: grade 10 ant-grasshopper (5 records per subject)

Manual-review dump for hand-audit. Each subject gets 5 rendered records sampled across different seeds so subplot/character/location variety is visible.

---

## G10-01: quote, unquote, unquote-splice

### G10-01 record 1

**form**: `(quote (+ 1 2))`  •  **expected**: `['+', 1, 2]`

```
Two creatures of the meadow approached the coming winter very differently.

Toc the ant had spent the morning atop the hilltop sketching a tiny language of
her own — a notebook of macros that wrote other forms. The
next entry was the quoted form (quote (+ 1 2)), and the form `(quote (+ 1 2))` was what
Toc wanted Skip the grasshopper to submit so the REPL could show what
code it produced or what value it returned.

What Clojure form computes the value of (quote (+ 1 2)) — the unevaluated list? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(quote (+ 1 2))"}}]}
```

### G10-01 record 2

**form**: `(quote (+ 1 2))`  •  **expected**: `['+', 1, 2]`

```
Two creatures of the meadow approached the coming winter very differently. It happened in the farm.

Halfway through the morning's work, Hum the grasshopper blocked
Bit the ant's path in the farm and refused to step aside until someone
could prove what the form `(quote (+ 1 2))` evaluated to. Hum
called it impossible. Bit the ant, walking up at their usual
pace, simply said: "Submit the quoted form (quote (+ 1 2)) to the REPL. Whatever comes
back is the answer."

Write a form whose evaluation gives the value of (quote (+ 1 2)) — the unevaluated list.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(quote (+ 1 2))"}}]}
```

### G10-01 record 3

**form**: `(quote (+ 1 2))`  •  **expected**: `['+', 1, 2]`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

With a twig, Skip the grasshopper marked out a wager on the hilltop: whoever
guessed the result of `(quote (+ 1 2))` first would win the right to
choose the next song. Bit the ant, untroubled by what others thought, said it was easier
to ask the REPL about the quoted form (quote (+ 1 2)) than to argue.

Write a form whose evaluation gives the value of (quote (+ 1 2)) — the unevaluated list.

---

{"tool_calls":[{"name":"eval","args":{"form":"(quote (+ 1 2))"}}]}
```

### G10-01 record 4

**form**: `(quote (+ 1 2))`  •  **expected**: `['+', 1, 2]`

```
All summer long, the Ant worked while the Grasshopper sang.

A small notebook lay open by the orchard where the Ant had been studying
syntax-quote. The page showed the quoted form (quote (+ 1 2)), with the form
`(quote (+ 1 2))` circled in pencil. Skip the grasshopper, her legs heavy from sprinting of
the lecture, agreed to write the form to settle once and for all
what it produced.

Write a form whose evaluation gives the value of (quote (+ 1 2)) — the unevaluated list.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(quote (+ 1 2))"}}]}
```

### G10-01 record 5

**form**: `(quote (+ 1 2))`  •  **expected**: `['+', 1, 2]`

```
Two creatures of the meadow approached the coming winter very differently.

Halfway through the morning's work, Skip the grasshopper blocked
Toc the ant's path at the edge of the forest and refused to step aside until someone
could prove what the form `(quote (+ 1 2))` evaluated to. Skip
called it impossible. Toc the ant, walking up at her usual
pace, simply said: "Submit the quoted form (quote (+ 1 2)) to the REPL. Whatever comes
back is the answer."

Question: write a Clojure expression for the value of (quote (+ 1 2)) — the unevaluated list.

---

{"tool_calls":[{"name":"eval","args":{"form":"(quote (+ 1 2))"}}]}
```

## G10-02: syntax-quote

### G10-02 record 1

**form**: `(let [x 10] `(+ ~x ~x))`  •  **expected**: `['+', 10, 10]`

```
Two creatures of the meadow approached the coming winter very differently.

"There is no need to evaluate that," Chirp the grasshopper said,
with great whoops of laughter. "Anyone can see what a syntax-quoted addition with x unquoted twice comes to."
Bit the ant, who atop the hilltop had grown used to such claims, asked
him to actually write the form `(let [x 10] `(+ ~x ~x))` and
submit it to the REPL — just to be sure.

Question: write a Clojure expression for the form produced by `(+ ~x ~x) when x is 10.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 10] `(+ ~x ~x))"}}]}
```

### G10-02 record 2

**form**: `(let [x 10] `(+ ~x ~x))`  •  **expected**: `['+', 10, 10]`

```
Two creatures of the meadow approached the coming winter very differently.

Bit the ant had been trying to teach Chirp the grasshopper how the REPL
works. "Look here," they said, pointing to a syntax-quoted addition with x unquoted twice.
"You hand the form `(let [x 10] `(+ ~x ~x))` to the runtime, and the runtime hands
you back what it evaluates to." Chirp, yawning at the soft moss, agreed to
try.

What Clojure form computes the form produced by `(+ ~x ~x) when x is 10? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 10] `(+ ~x ~x))"}}]}
```

### G10-02 record 3

**form**: `(let [x 10] `(+ ~x ~x))`  •  **expected**: `['+', 10, 10]`

```
All summer long, the Ant worked while the Grasshopper sang. This was near the orchard.

A small notebook lay open by the orchard where the Ant had been studying
syntax-quote. The page showed a syntax-quoted addition with x unquoted twice, with the form
`(let [x 10] `(+ ~x ~x))` circled in pencil. Hum the grasshopper, weary from the morning's effort of
the lecture, agreed to write the form to settle once and for all
what it produced.

Write a Clojure expression that computes the form produced by `(+ ~x ~x) when x is 10.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 10] `(+ ~x ~x))"}}]}
```

### G10-02 record 4

**form**: `(let [x 10] `(+ ~x ~x))`  •  **expected**: `['+', 10, 10]`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Toc the ant had been trying to teach Chirp the grasshopper how the REPL
works. "Look here," she said, pointing to a syntax-quoted addition with x unquoted twice.
"You hand the form `(let [x 10] `(+ ~x ~x))` to the runtime, and the runtime hands
you back what it evaluates to." Chirp, drowsy from the warm sun, agreed to
try.

Write a Clojure expression that computes the form produced by `(+ ~x ~x) when x is 10.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 10] `(+ ~x ~x))"}}]}
```

### G10-02 record 5

**form**: `(let [x 10] `(+ ~x ~x))`  •  **expected**: `['+', 10, 10]`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

At a stone tablet by the orchard, Tic the ant was teaching Skip the grasshopper
the discipline of expansion: never trust your eyes, only the
macroexpander. The day's example was a syntax-quoted addition with x unquoted twice. The form
`(let [x 10] `(+ ~x ~x))` had to be submitted; nothing else would do.

Write a Clojure expression that computes the form produced by `(+ ~x ~x) when x is 10.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 10] `(+ ~x ~x))"}}]}
```

## G10-03: defmacro introduction

### G10-03 record 1

**form**: `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`  •  **expected**: `3`

```
All summer long, the Ant worked while the Grasshopper sang. All this took place at the edge of the garden.

A small audience of meadow creatures had gathered near the garden to watch
Skip the grasshopper attempt to outwit Tic the ant at reading the
REPL. Tic pointed to a tiny when-style macro and a call to it and read out the form aloud:
`(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`. The crowd waited to see who would correctly write the
form to submit.

Question: write a Clojure expression for what (my-when true 1 2 3) returns.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
```

### G10-03 record 2

**form**: `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`  •  **expected**: `3`

```
Two creatures of the meadow approached the coming winter very differently.

Skip the grasshopper chalked a wager on a flat slate in the meadow: whoever
predicted the result of `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))` first would set the next day's
ration. Tic the ant, without complaint, said it would be simpler to type
the form into the REPL than to bicker about a tiny when-style macro and a call to it.

What Clojure form computes what (my-when true 1 2 3) returns? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
```

### G10-03 record 3

**form**: `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`  •  **expected**: `3`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

"There is no need to evaluate that," Chirp the grasshopper said,
swaggering through the underbrush. "Anyone can see what a tiny when-style macro and a call to it comes to."
Bit the ant, who by the garden had grown used to such claims, asked
him to actually write the form `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))` and
submit it to the REPL — just to be sure.

What Clojure form computes what (my-when true 1 2 3) returns? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
```

### G10-03 record 4

**form**: `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`  •  **expected**: `3`

```
Two creatures of the meadow approached the coming winter very differently. It happened by the orchard.

The path in the orchard was littered with old macro definitions someone had
carved into bark. Skip the grasshopper found one shaped like
a tiny when-style macro and a call to it and dared Toc the ant to predict its expansion.
Toc only smiled and asked her to write `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`
into the REPL — that, after all, was the whole point of having a
macroexpander.

Write a Clojure expression that computes what (my-when true 1 2 3) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
```

### G10-03 record 5

**form**: `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`  •  **expected**: `3`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Halfway through the morning's work, Chirp the grasshopper blocked
Tic the ant's path by the farm and refused to step aside until someone
could prove what the form `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))` evaluated to. Chirp
called it impossible. Tic the ant, walking up at his usual
pace, simply said: "Submit a tiny when-style macro and a call to it to the REPL. Whatever comes
back is the answer."

What Clojure form computes what (my-when true 1 2 3) returns? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
```

## G10-04: Macro expansion rule

### G10-04 record 1

**form**: `(macroexpand-1 '(when true 1))`  •  **expected**: `['if', True, ['do', 1]]`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

A small audience of meadow creatures had gathered on the hilltop to watch
Chirp the grasshopper attempt to outwit Toc the ant at reading the
REPL. Toc pointed to the one-step expansion of (when true 1) and read out the form aloud:
`(macroexpand-1 '(when true 1))`. The crowd waited to see who would correctly write the
form to submit.

Write a Clojure expression that computes what macroexpand-1 returns for (when true 1).

---

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(when true 1))"}}]}
```

### G10-04 record 2

**form**: `(macroexpand-1 '(when true 1))`  •  **expected**: `['if', True, ['do', 1]]`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. This was on the hilltop.

Halfway through the morning's work, Chirp the grasshopper blocked
Tic the ant's path near the hilltop and refused to step aside until someone
could prove what the form `(macroexpand-1 '(when true 1))` evaluated to. Chirp
called it impossible. Tic the ant, walking up at his usual
pace, simply said: "Submit the one-step expansion of (when true 1) to the REPL. Whatever comes
back is the answer."

Write a Clojure expression that computes what macroexpand-1 returns for (when true 1).

---

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(when true 1))"}}]}
```

### G10-04 record 3

**form**: `(macroexpand-1 '(when true 1))`  •  **expected**: `['if', True, ['do', 1]]`

```
Two creatures of the meadow approached the coming winter very differently.

Tic the ant had been trying to teach Skip the grasshopper how the REPL
works. "Look here," he said, pointing to the one-step expansion of (when true 1).
"You hand the form `(macroexpand-1 '(when true 1))` to the runtime, and the runtime hands
you back what it evaluates to." Skip, weary from the morning's effort, agreed to
try.

What Clojure form computes what macroexpand-1 returns for (when true 1)? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(when true 1))"}}]}
```

### G10-04 record 4

**form**: `(macroexpand-1 '(when true 1))`  •  **expected**: `['if', True, ['do', 1]]`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Toc the ant had been keeping a small leather notebook of every form
she had successfully evaluated. Today in the orchard, the next entry
was the one-step expansion of (when true 1). Chirp the grasshopper peered over
her shoulder at the form `(macroexpand-1 '(when true 1))` and asked what it
would come out to.

Write a Clojure expression that computes what macroexpand-1 returns for (when true 1).

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(when true 1))"}}]}
```

### G10-04 record 5

**form**: `(macroexpand-1 '(when true 1))`  •  **expected**: `['if', True, ['do', 1]]`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. All this took place in the orchard.

The path by the orchard was littered with old macro definitions someone had
carved into bark. Skip the grasshopper found one shaped like
the one-step expansion of (when true 1) and dared Toc the ant to predict its expansion.
Toc only smiled and asked her to write `(macroexpand-1 '(when true 1))`
into the REPL — that, after all, was the whole point of having a
macroexpander.

Write a Clojure expression that computes what macroexpand-1 returns for (when true 1).

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(when true 1))"}}]}
```

## G10-05: macroexpand

### G10-05 record 1

**form**: `(macroexpand '(when true 1))`  •  **expected**: `['if', True, ['do', 1]]`

```
Two creatures of the meadow approached the coming winter very differently.

"There is no need to evaluate that," Skip the grasshopper said,
swaggering through the underbrush. "Anyone can see what the full expansion of (when true 1) comes to."
Toc the ant, who at the edge of the woods had grown used to such claims, asked
her to actually write the form `(macroexpand '(when true 1))` and
submit it to the REPL — just to be sure.

Write a form whose evaluation gives what macroexpand returns for (when true 1).

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(when true 1))"}}]}
```

### G10-05 record 2

**form**: `(macroexpand '(when true 1))`  •  **expected**: `['if', True, ['do', 1]]`

```
Two creatures of the meadow approached the coming winter very differently. All this took place atop the hilltop.

"A macro is just a function that runs at compile time," Tic explained
atop the hilltop, saying very little. Hum, with great whoops of laughter, said
they could already see what the full expansion of (when true 1) meant.
Tic the ant insisted they actually evaluate `(macroexpand '(when true 1))` and read
what the runtime reported, expansion or value.

Question: write a Clojure expression for what macroexpand returns for (when true 1).

---

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(when true 1))"}}]}
```

### G10-05 record 3

**form**: `(macroexpand '(when true 1))`  •  **expected**: `['if', True, ['do', 1]]`

```
Two creatures of the meadow approached the coming winter very differently. This was near the woods.

Tic the ant and Skip the grasshopper stopped in the woods where someone had
written the full expansion of (when true 1) on a flat stone. Skip, swaggering through the underbrush,
declared that she could see the answer at a glance.
Tic, her eyes always on the path, suggested they actually evaluate the form
`(macroexpand '(when true 1))` in the REPL and read off whatever it returned.

What Clojure form computes what macroexpand returns for (when true 1)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(when true 1))"}}]}
```

### G10-05 record 4

**form**: `(macroexpand '(when true 1))`  •  **expected**: `['if', True, ['do', 1]]`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

The path at the edge of the farm was littered with old macro definitions someone had
carved into bark. Hum the grasshopper found one shaped like
the full expansion of (when true 1) and dared Tic the ant to predict its expansion.
Tic only smiled and asked them to write `(macroexpand '(when true 1))`
into the REPL — that, after all, was the whole point of having a
macroexpander.

Write a Clojure expression that computes what macroexpand returns for (when true 1).

---

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(when true 1))"}}]}
```

### G10-05 record 5

**form**: `(macroexpand '(when true 1))`  •  **expected**: `['if', True, ['do', 1]]`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

At the edge of a stockpile atop the hilltop, Hum the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(macroexpand '(when true 1))`
first would win the right to set the next day's count.
Toc the ant, her eyes always on the path, said it was simpler to type the form into
the REPL than to argue about the full expansion of (when true 1).

What Clojure form computes what macroexpand returns for (when true 1)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(when true 1))"}}]}
```

## G10-06: when and when-not as macros

### G10-06 record 1

**form**: `(when true 1 2 3)`  •  **expected**: `3`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

A small notebook lay open near the woods where the Ant had been studying
syntax-quote. The page showed the form (when true 1 2 3), with the form
`(when true 1 2 3)` circled in pencil. Chirp the grasshopper, weary from the morning's effort of
the lecture, agreed to write the form to settle once and for all
what it produced.

Write a form whose evaluation gives what (when true 1 2 3) returns.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(when true 1 2 3)"}}]}
```

### G10-06 record 2

**form**: `(when true 1 2 3)`  •  **expected**: `3`

```
All summer long, the Ant worked while the Grasshopper sang. This was near the orchard.

A wooden sign nailed to a stalk by the orchard carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(when true 1 2 3)`. Hum
laughed, boasting at every turn, and declared it too easy. Tic said patiently
that the only way to be sure of the form (when true 1 2 3) was to put it in the
REPL.

Write a Clojure expression that computes what (when true 1 2 3) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(when true 1 2 3)"}}]}
```

### G10-06 record 3

**form**: `(when true 1 2 3)`  •  **expected**: `3`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

At a stone tablet in the orchard, Toc the ant was teaching Hum the grasshopper
the discipline of expansion: never trust your eyes, only the
macroexpander. The day's example was the form (when true 1 2 3). The form
`(when true 1 2 3)` had to be submitted; nothing else would do.

Write a Clojure expression that computes what (when true 1 2 3) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(when true 1 2 3)"}}]}
```

### G10-06 record 4

**form**: `(when true 1 2 3)`  •  **expected**: `3`

```
Two creatures of the meadow approached the coming winter very differently. All this took place at the edge of the forest.

Halfway through the morning's work, Skip the grasshopper blocked
Toc the ant's path in the forest and refused to step aside until someone
could prove what the form `(when true 1 2 3)` evaluated to. Skip
called it impossible. Toc the ant, walking up at her usual
pace, simply said: "Submit the form (when true 1 2 3) to the REPL. Whatever comes
back is the answer."

Question: write a Clojure expression for what (when true 1 2 3) returns.

---

I write the macro form and let the runtime evaluate or expand it.

{"tool_calls":[{"name":"eval","args":{"form":"(when true 1 2 3)"}}]}
```

### G10-06 record 5

**form**: `(when true 1 2 3)`  •  **expected**: `3`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. This was in the meadow.

A small audience of meadow creatures had gathered by the meadow to watch
Skip the grasshopper attempt to outwit Bit the ant at reading the
REPL. Bit pointed to the form (when true 1 2 3) and read out the form aloud:
`(when true 1 2 3)`. The crowd waited to see who would correctly write the
form to submit.

Question: write a Clojure expression for what (when true 1 2 3) returns.

---

I write the macro form and let the runtime evaluate or expand it.

{"tool_calls":[{"name":"eval","args":{"form":"(when true 1 2 3)"}}]}
```

## G10-07: Threading macros revisited

### G10-07 record 1

**form**: `(-> 5 inc inc inc)`  •  **expected**: `8`

```
Two creatures of the meadow approached the coming winter very differently.

Tic the ant had been keeping a small leather notebook of every form
he had successfully evaluated. Today by the forest, the next entry
was the thread-first form (-> 5 inc inc inc). Hum the grasshopper peered over
his shoulder at the form `(-> 5 inc inc inc)` and asked what it
would come out to.

Question: write a Clojure expression for what (-> 5 inc inc inc) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(-> 5 inc inc inc)"}}]}
```

### G10-07 record 2

**form**: `(-> 5 inc inc inc)`  •  **expected**: `8`

```
All summer long, the Ant worked while the Grasshopper sang. All this took place at the edge of the farm.

Hum the grasshopper insisted in the farm that macros were the same as
functions. Toc the ant, saying very little, drew the form `(-> 5 inc inc inc)` on
a strip of bark. "The difference," she said, "is in
the thread-first form (-> 5 inc inc inc). Submit the form and let the runtime tell us
exactly what it does."

Write a Clojure expression that computes what (-> 5 inc inc inc) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(-> 5 inc inc inc)"}}]}
```

### G10-07 record 3

**form**: `(-> 5 inc inc inc)`  •  **expected**: `8`

```
All summer long, the Ant worked while the Grasshopper sang.

Bit the ant had been trying to teach Skip the grasshopper how the REPL
works. "Look here," they said, pointing to the thread-first form (-> 5 inc inc inc).
"You hand the form `(-> 5 inc inc inc)` to the runtime, and the runtime hands
you back what it evaluates to." Skip, lulled by the gentle wind, agreed to
try.

Question: write a Clojure expression for what (-> 5 inc inc inc) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(-> 5 inc inc inc)"}}]}
```

### G10-07 record 4

**form**: `(-> 5 inc inc inc)`  •  **expected**: `8`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

A small notebook lay open near the orchard where the Ant had been studying
syntax-quote. The page showed the thread-first form (-> 5 inc inc inc), with the form
`(-> 5 inc inc inc)` circled in pencil. Hum the grasshopper, yawning at the soft moss of
the lecture, agreed to write the form to settle once and for all
what it produced.

Write a form whose evaluation gives what (-> 5 inc inc inc) returns.

---

I write the form and let the macroexpander or REPL show the result.

{"tool_calls":[{"name":"eval","args":{"form":"(-> 5 inc inc inc)"}}]}
```

### G10-07 record 5

**form**: `(-> 5 inc inc inc)`  •  **expected**: `8`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. This was atop the hilltop.

At a stone tablet near the hilltop, Toc the ant was teaching Chirp the grasshopper
the discipline of expansion: never trust your eyes, only the
macroexpander. The day's example was the thread-first form (-> 5 inc inc inc). The form
`(-> 5 inc inc inc)` had to be submitted; nothing else would do.

Question: write a Clojure expression for what (-> 5 inc inc inc) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(-> 5 inc inc inc)"}}]}
```

## G10-08: Macro vs fn

### G10-08 record 1

**form**: `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))`  •  **expected**: `7`

```
Two creatures of the meadow approached the coming winter very differently. It happened on the hilltop.

At the edge of a stockpile atop the hilltop, Chirp the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))`
first would win the right to set the next day's count.
Tic the ant, without complaint, said it was simpler to type the form into
the REPL than to argue about a plain function adding two numbers.

What Clojure form computes the result of calling a function (args evaluated)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))"}}]}
```

### G10-08 record 2

**form**: `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))`  •  **expected**: `7`

```
Two creatures of the meadow approached the coming winter very differently. All this took place by the garden.

With a twig, Skip the grasshopper marked out a wager by the garden: whoever
guessed the result of `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` first would win the right to
choose the next song. Tic the ant, her eyes always on the path, said it was easier
to ask the REPL about a plain function adding two numbers than to argue.

Question: write a Clojure expression for the result of calling a function (args evaluated).

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))"}}]}
```

### G10-08 record 3

**form**: `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))`  •  **expected**: `7`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. This was at the edge of the forest.

A small audience of meadow creatures had gathered in the forest to watch
Hum the grasshopper attempt to outwit Bit the ant at reading the
REPL. Bit pointed to a plain function adding two numbers and read out the form aloud:
`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))`. The crowd waited to see who would correctly write the
form to submit.

Write a form whose evaluation gives the result of calling a function (args evaluated).

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))"}}]}
```

### G10-08 record 4

**form**: `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))`  •  **expected**: `7`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Chirp the grasshopper chalked a wager on a flat slate near the farm: whoever
predicted the result of `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` first would set the next day's
ration. Tic the ant, with steady, careful steps, said it would be simpler to type
the form into the REPL than to bicker about a plain function adding two numbers.

Question: write a Clojure expression for the result of calling a function (args evaluated).

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))"}}]}
```

### G10-08 record 5

**form**: `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))`  •  **expected**: `7`

```
All summer long, the Ant worked while the Grasshopper sang.

A small notebook lay open at the edge of the garden where the Ant had been studying
syntax-quote. The page showed a plain function adding two numbers, with the form
`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` circled in pencil. Chirp the grasshopper, drowsy from the warm sun of
the lecture, agreed to write the form to settle once and for all
what it produced.

Write a form whose evaluation gives the result of calling a function (args evaluated).

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))"}}]}
```

## G10-09: Hygiene and gensym

### G10-09 record 1

**form**: `(symbol? (gensym))`  •  **expected**: `True`

```
Two creatures of the meadow approached the coming winter very differently. All this took place in the forest.

"There is no need to evaluate that," Chirp the grasshopper said,
as if the race were already won. "Anyone can see what the predicate (symbol? (gensym)) comes to."
Tic the ant, who at the edge of the forest had grown used to such claims, asked
him to actually write the form `(symbol? (gensym))` and
submit it to the REPL — just to be sure.

Write a Clojure expression that computes whether (gensym) returns a symbol.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? (gensym))"}}]}
```

### G10-09 record 2

**form**: `(symbol? (gensym))`  •  **expected**: `True`

```
Two creatures of the meadow approached the coming winter very differently.

Toc the ant and Hum the grasshopper stopped at the edge of the meadow where someone had
written the predicate (symbol? (gensym)) on a flat stone. Hum, as if the race were already won,
declared that they could see the answer at a glance.
Toc, without complaint, suggested they actually evaluate the form
`(symbol? (gensym))` in the REPL and read off whatever it returned.

Question: write a Clojure expression for whether (gensym) returns a symbol.

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? (gensym))"}}]}
```

### G10-09 record 3

**form**: `(symbol? (gensym))`  •  **expected**: `True`

```
All summer long, the Ant worked while the Grasshopper sang. This was by the farm.

A wooden sign nailed to a stalk in the farm carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(symbol? (gensym))`. Skip
laughed, swaggering through the underbrush, and declared it too easy. Toc said patiently
that the only way to be sure of the predicate (symbol? (gensym)) was to put it in the
REPL.

Write a form whose evaluation gives whether (gensym) returns a symbol.

---

I expand the macro with macroexpand and read the produced form.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? (gensym))"}}]}
```

### G10-09 record 4

**form**: `(symbol? (gensym))`  •  **expected**: `True`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. It happened at the edge of the garden.

Skip the grasshopper insisted near the garden that macros were the same as
functions. Tic the ant, stepping deliberately, drew the form `(symbol? (gensym))` on
a strip of bark. "The difference," he said, "is in
the predicate (symbol? (gensym)). Submit the form and let the runtime tell us
exactly what it does."

Write a form whose evaluation gives whether (gensym) returns a symbol.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? (gensym))"}}]}
```

### G10-09 record 5

**form**: `(symbol? (gensym))`  •  **expected**: `True`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. It happened at the edge of the meadow.

Toc the ant had been trying to teach Hum the grasshopper how the REPL
works. "Look here," she said, pointing to the predicate (symbol? (gensym)).
"You hand the form `(symbol? (gensym))` to the runtime, and the runtime hands
you back what it evaluates to." Hum, lulled by the gentle wind, agreed to
try.

What Clojure form computes whether (gensym) returns a symbol? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? (gensym))"}}]}
```

## G10-10: Anaphoric macros are confusing

### G10-10 record 1

**form**: `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))`  •  **expected**: `10`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Bit the ant and Skip the grasshopper stopped near the woods where someone had
written a hygienic if-let style macro avoiding anaphoric injection on a flat stone. Skip, boasting at every turn,
declared that she could see the answer at a glance.
Bit, with steady, careful steps, suggested they actually evaluate the form
`(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))` in the REPL and read off whatever it returned.

What Clojure form computes what the hygienic if-let macro returns? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))"}}]}
```

### G10-10 record 2

**form**: `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))`  •  **expected**: `10`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

With a twig, Chirp the grasshopper marked out a wager at the edge of the garden: whoever
guessed the result of `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))` first would win the right to
choose the next song. Tic the ant, her eyes always on the path, said it was easier
to ask the REPL about a hygienic if-let style macro avoiding anaphoric injection than to argue.

Write a form whose evaluation gives what the hygienic if-let macro returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))"}}]}
```

### G10-10 record 3

**form**: `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))`  •  **expected**: `10`

```
All summer long, the Ant worked while the Grasshopper sang.

"A macro is just a function that runs at compile time," Toc explained
by the garden, stepping deliberately. Chirp, with a smug grin, said
he could already see what a hygienic if-let style macro avoiding anaphoric injection meant.
Toc the ant insisted they actually evaluate `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))` and read
what the runtime reported, expansion or value.

Write a form whose evaluation gives what the hygienic if-let macro returns.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))"}}]}
```

### G10-10 record 4

**form**: `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))`  •  **expected**: `10`

```
Two creatures of the meadow approached the coming winter very differently. This was at the edge of the farm.

Bit the ant had been keeping a small leather notebook of every form
they had successfully evaluated. Today in the farm, the next entry
was a hygienic if-let style macro avoiding anaphoric injection. Skip the grasshopper peered over
their shoulder at the form `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))` and asked what it
would come out to.

Write a Clojure expression that computes what the hygienic if-let macro returns.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))"}}]}
```

### G10-10 record 5

**form**: `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))`  •  **expected**: `10`

```
All summer long, the Ant worked while the Grasshopper sang. It happened at the edge of the farm.

Chirp the grasshopper insisted in the farm that macros were the same as
functions. Bit the ant, with steady, careful steps, drew the form `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))` on
a strip of bark. "The difference," they said, "is in
a hygienic if-let style macro avoiding anaphoric injection. Submit the form and let the runtime tell us
exactly what it does."

Write a Clojure expression that computes what the hygienic if-let macro returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))"}}]}
```

## G10-11: Reader macros overview

### G10-11 record 1

**form**: `'(1 2 3)`  •  **expected**: `[1, 2, 3]`

```
Two creatures of the meadow approached the coming winter very differently. It happened in the meadow.

A wooden sign nailed to a stalk in the meadow carried a puzzle. The riddle
was simple: it asked the reader to evaluate `'(1 2 3)`. Chirp
laughed, boasting at every turn, and declared it too easy. Tic said patiently
that the only way to be sure of the quote reader macro 'foo was to put it in the
REPL.

Question: write a Clojure expression for what '(1 2 3) reads as.

---

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### G10-11 record 2

**form**: `'(1 2 3)`  •  **expected**: `[1, 2, 3]`

```
Two creatures of the meadow approached the coming winter very differently. This was near the forest.

At the edge of a stockpile at the edge of the forest, Skip the grasshopper sketched a
small wager into the dust: whoever guessed the result of `'(1 2 3)`
first would win the right to set the next day's count.
Toc the ant, with steady, careful steps, said it was simpler to type the form into
the REPL than to argue about the quote reader macro 'foo.

Write a form whose evaluation gives what '(1 2 3) reads as.

---

I write the form and let the macroexpander or REPL show the result.

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### G10-11 record 3

**form**: `'(1 2 3)`  •  **expected**: `[1, 2, 3]`

```
Two creatures of the meadow approached the coming winter very differently. This was at the edge of the forest.

Skip the grasshopper insisted in the forest that macros were the same as
functions. Bit the ant, saying very little, drew the form `'(1 2 3)` on
a strip of bark. "The difference," they said, "is in
the quote reader macro 'foo. Submit the form and let the runtime tell us
exactly what it does."

Question: write a Clojure expression for what '(1 2 3) reads as.

---

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### G10-11 record 4

**form**: `'(1 2 3)`  •  **expected**: `[1, 2, 3]`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

A wooden sign nailed to a stalk in the woods carried a puzzle. The riddle
was simple: it asked the reader to evaluate `'(1 2 3)`. Hum
laughed, with a smug grin, and declared it too easy. Tic said patiently
that the only way to be sure of the quote reader macro 'foo was to put it in the
REPL.

What Clojure form computes what '(1 2 3) reads as? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### G10-11 record 5

**form**: `'(1 2 3)`  •  **expected**: `[1, 2, 3]`

```
All summer long, the Ant worked while the Grasshopper sang.

Skip the grasshopper insisted by the garden that macros were the same as
functions. Bit the ant, saying very little, drew the form `'(1 2 3)` on
a strip of bark. "The difference," they said, "is in
the quote reader macro 'foo. Submit the form and let the runtime tell us
exactly what it does."

Write a form whose evaluation gives what '(1 2 3) reads as.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

## G10-12: Tagged literals

### G10-12 record 1

**form**: `(inst? #inst "2024-01-01")`  •  **expected**: `True`

```
Two creatures of the meadow approached the coming winter very differently.

Skip the grasshopper chalked a wager on a flat slate atop the hilltop: whoever
predicted the result of `(inst? #inst "2024-01-01")` first would set the next day's
ration. Toc the ant, stepping deliberately, said it would be simpler to type
the form into the REPL than to bicker about the predicate (inst? #inst "2024-01-01").

Write a form whose evaluation gives whether the #inst tagged literal reads to an inst.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(inst? #inst \"2024-01-01\")"}}]}
```

### G10-12 record 2

**form**: `(inst? #inst "2024-01-01")`  •  **expected**: `True`

```
Two creatures of the meadow approached the coming winter very differently.

A small notebook lay open at the edge of the garden where the Ant had been studying
syntax-quote. The page showed the predicate (inst? #inst "2024-01-01"), with the form
`(inst? #inst "2024-01-01")` circled in pencil. Hum the grasshopper, weary from the morning's effort of
the lecture, agreed to write the form to settle once and for all
what it produced.

Write a form whose evaluation gives whether the #inst tagged literal reads to an inst.

---

I submit the syntax-quoted or quoted form to the REPL.

{"tool_calls":[{"name":"eval","args":{"form":"(inst? #inst \"2024-01-01\")"}}]}
```

### G10-12 record 3

**form**: `(inst? #inst "2024-01-01")`  •  **expected**: `True`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. It happened at the edge of the woods.

The path in the woods was littered with old macro definitions someone had
carved into bark. Hum the grasshopper found one shaped like
the predicate (inst? #inst "2024-01-01") and dared Toc the ant to predict its expansion.
Toc only smiled and asked them to write `(inst? #inst "2024-01-01")`
into the REPL — that, after all, was the whole point of having a
macroexpander.

Write a form whose evaluation gives whether the #inst tagged literal reads to an inst.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(inst? #inst \"2024-01-01\")"}}]}
```

### G10-12 record 4

**form**: `(inst? #inst "2024-01-01")`  •  **expected**: `True`

```
Two creatures of the meadow approached the coming winter very differently.

The path in the garden was littered with old macro definitions someone had
carved into bark. Skip the grasshopper found one shaped like
the predicate (inst? #inst "2024-01-01") and dared Tic the ant to predict its expansion.
Tic only smiled and asked her to write `(inst? #inst "2024-01-01")`
into the REPL — that, after all, was the whole point of having a
macroexpander.

Write a Clojure expression that computes whether the #inst tagged literal reads to an inst.

---

{"tool_calls":[{"name":"eval","args":{"form":"(inst? #inst \"2024-01-01\")"}}]}
```

### G10-12 record 5

**form**: `(inst? #inst "2024-01-01")`  •  **expected**: `True`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. It happened near the forest.

"There is no need to evaluate that," Chirp the grasshopper said,
puffed up with pride. "Anyone can see what the predicate (inst? #inst "2024-01-01") comes to."
Toc the ant, who at the edge of the forest had grown used to such claims, asked
him to actually write the form `(inst? #inst "2024-01-01")` and
submit it to the REPL — just to be sure.

Write a Clojure expression that computes whether the #inst tagged literal reads to an inst.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(inst? #inst \"2024-01-01\")"}}]}
```

## G10-13: Data readers and EDN extension

### G10-13 record 1

**form**: `(clojure.edn/read-string "42")`  •  **expected**: `42`

```
Two creatures of the meadow approached the coming winter very differently.

At the edge of a stockpile at the edge of the orchard, Hum the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(clojure.edn/read-string "42")`
first would win the right to set the next day's count.
Toc the ant, with steady, careful steps, said it was simpler to type the form into
the REPL than to argue about edn read-string of "42".

Write a form whose evaluation gives what edn/read-string returns for the source "42".

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"42\")"}}]}
```

### G10-13 record 2

**form**: `(clojure.edn/read-string "42")`  •  **expected**: `42`

```
Two creatures of the meadow approached the coming winter very differently.

Chirp the grasshopper insisted by the farm that macros were the same as
functions. Tic the ant, with steady, careful steps, drew the form `(clojure.edn/read-string "42")` on
a strip of bark. "The difference," he said, "is in
edn read-string of "42". Submit the form and let the runtime tell us
exactly what it does."

Write a Clojure expression that computes what edn/read-string returns for the source "42".

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"42\")"}}]}
```

### G10-13 record 3

**form**: `(clojure.edn/read-string "42")`  •  **expected**: `42`

```
All summer long, the Ant worked while the Grasshopper sang. It happened atop the hilltop.

Tic the ant had spent the morning on the hilltop sketching a tiny language of
his own — a notebook of macros that wrote other forms. The
next entry was edn read-string of "42", and the form `(clojure.edn/read-string "42")` was what
Tic wanted Chirp the grasshopper to submit so the REPL could show what
code it produced or what value it returned.

Write a Clojure expression that computes what edn/read-string returns for the source "42".

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"42\")"}}]}
```

### G10-13 record 4

**form**: `(clojure.edn/read-string "42")`  •  **expected**: `42`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

With a twig, Chirp the grasshopper marked out a wager by the farm: whoever
guessed the result of `(clojure.edn/read-string "42")` first would win the right to
choose the next song. Tic the ant, without complaint, said it was easier
to ask the REPL about edn read-string of "42" than to argue.

What Clojure form computes what edn/read-string returns for the source "42"? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"42\")"}}]}
```

### G10-13 record 5

**form**: `(clojure.edn/read-string "42")`  •  **expected**: `42`

```
Two creatures of the meadow approached the coming winter very differently. All this took place in the forest.

Bit the ant had been keeping a small leather notebook of every form
they had successfully evaluated. Today in the forest, the next entry
was edn read-string of "42". Chirp the grasshopper peered over
their shoulder at the form `(clojure.edn/read-string "42")` and asked what it
would come out to.

Question: write a Clojure expression for what edn/read-string returns for the source "42".

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"42\")"}}]}
```

## G10-14: eval (the function)

### G10-14 record 1

**form**: `(eval '(+ 1 2 3))`  •  **expected**: `6`

```
Two creatures of the meadow approached the coming winter very differently.

A small audience of meadow creatures had gathered at the edge of the forest to watch
Skip the grasshopper attempt to outwit Toc the ant at reading the
REPL. Toc pointed to the form (eval '(+ 1 2 3)) and read out the form aloud:
`(eval '(+ 1 2 3))`. The crowd waited to see who would correctly write the
form to submit.

Write a Clojure expression that computes what eval returns for the quoted (+ 1 2 3).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(eval '(+ 1 2 3))"}}]}
```

### G10-14 record 2

**form**: `(eval '(+ 1 2 3))`  •  **expected**: `6`

```
Two creatures of the meadow approached the coming winter very differently.

At the edge of a stockpile by the woods, Hum the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(eval '(+ 1 2 3))`
first would win the right to set the next day's count.
Toc the ant, without complaint, said it was simpler to type the form into
the REPL than to argue about the form (eval '(+ 1 2 3)).

Write a form whose evaluation gives what eval returns for the quoted (+ 1 2 3).

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(eval '(+ 1 2 3))"}}]}
```

### G10-14 record 3

**form**: `(eval '(+ 1 2 3))`  •  **expected**: `6`

```
All summer long, the Ant worked while the Grasshopper sang.

With a twig, Hum the grasshopper marked out a wager at the edge of the hilltop: whoever
guessed the result of `(eval '(+ 1 2 3))` first would win the right to
choose the next song. Bit the ant, stepping deliberately, said it was easier
to ask the REPL about the form (eval '(+ 1 2 3)) than to argue.

What Clojure form computes what eval returns for the quoted (+ 1 2 3)? Submit it via `eval`.

---

I submit the syntax-quoted or quoted form to the REPL.

{"tool_calls":[{"name":"eval","args":{"form":"(eval '(+ 1 2 3))"}}]}
```

### G10-14 record 4

**form**: `(eval '(+ 1 2 3))`  •  **expected**: `6`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

With a twig, Chirp the grasshopper marked out a wager at the edge of the farm: whoever
guessed the result of `(eval '(+ 1 2 3))` first would win the right to
choose the next song. Tic the ant, saying very little, said it was easier
to ask the REPL about the form (eval '(+ 1 2 3)) than to argue.

Write a form whose evaluation gives what eval returns for the quoted (+ 1 2 3).

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(eval '(+ 1 2 3))"}}]}
```

### G10-14 record 5

**form**: `(eval '(+ 1 2 3))`  •  **expected**: `6`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

"A macro is just a function that runs at compile time," Toc explained
near the hilltop, without complaint. Chirp, puffed up with pride, said
he could already see what the form (eval '(+ 1 2 3)) meant.
Toc the ant insisted they actually evaluate `(eval '(+ 1 2 3))` and read
what the runtime reported, expansion or value.

Write a Clojure expression that computes what eval returns for the quoted (+ 1 2 3).

---

I write the form and let the macroexpander or REPL show the result.

{"tool_calls":[{"name":"eval","args":{"form":"(eval '(+ 1 2 3))"}}]}
```

## G10-15: When not to write a macro

### G10-15 record 1

**form**: `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))`  •  **expected**: `7`

```
Two creatures of the meadow approached the coming winter very differently.

Skip the grasshopper insisted near the meadow that macros were the same as
functions. Bit the ant, without complaint, drew the form `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))` on
a strip of bark. "The difference," they said, "is in
a function call where no macro is justified. Submit the form and let the runtime tell us
exactly what it does."

Write a form whose evaluation gives what the plain function call returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"a function suffices when no syntax shaping is needed\" ((fn [x y] (+ x y)) 3 4))"}}]}
```

### G10-15 record 2

**form**: `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))`  •  **expected**: `7`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

With a twig, Hum the grasshopper marked out a wager by the garden: whoever
guessed the result of `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))` first would win the right to
choose the next song. Toc the ant, her eyes always on the path, said it was easier
to ask the REPL about a function call where no macro is justified than to argue.

Write a form whose evaluation gives what the plain function call returns.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"a function suffices when no syntax shaping is needed\" ((fn [x y] (+ x y)) 3 4))"}}]}
```

### G10-15 record 3

**form**: `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))`  •  **expected**: `7`

```
Two creatures of the meadow approached the coming winter very differently.

Bit the ant had been trying to teach Hum the grasshopper how the REPL
works. "Look here," they said, pointing to a function call where no macro is justified.
"You hand the form `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))` to the runtime, and the runtime hands
you back what it evaluates to." Hum, weary from the morning's effort, agreed to
try.

Write a form whose evaluation gives what the plain function call returns.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"a function suffices when no syntax shaping is needed\" ((fn [x y] (+ x y)) 3 4))"}}]}
```

### G10-15 record 4

**form**: `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))`  •  **expected**: `7`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Halfway through the morning's work, Hum the grasshopper blocked
Tic the ant's path in the forest and refused to step aside until someone
could prove what the form `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))` evaluated to. Hum
called it impossible. Tic the ant, walking up at his usual
pace, simply said: "Submit a function call where no macro is justified to the REPL. Whatever comes
back is the answer."

Question: write a Clojure expression for what the plain function call returns.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"a function suffices when no syntax shaping is needed\" ((fn [x y] (+ x y)) 3 4))"}}]}
```

### G10-15 record 5

**form**: `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))`  •  **expected**: `7`

```
Two creatures of the meadow approached the coming winter very differently. All this took place at the edge of the garden.

Toc the ant and Skip the grasshopper stopped in the garden where someone had
written a function call where no macro is justified on a flat stone. Skip, with a smug grin,
declared that she could see the answer at a glance.
Toc, with steady, careful steps, suggested they actually evaluate the form
`(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))` in the REPL and read off whatever it returned.

Write a Clojure expression that computes what the plain function call returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"a function suffices when no syntax shaping is needed\" ((fn [x y] (+ x y)) 3 4))"}}]}
```

## G10-16: Macro pattern library

### G10-16 record 1

**form**: `(do (defmacro with-ant-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-ant-pace 42))`  •  **expected**: `42`

```
Two creatures of the meadow approached the coming winter very differently. All this took place at the edge of the farm.

"A macro is just a function that runs at compile time," Toc explained
by the farm, her eyes always on the path. Hum, as if the race were already won, said
they could already see what a with-X macro pattern that binds a local and runs body meant.
Toc the ant insisted they actually evaluate `(do (defmacro with-ant-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-ant-pace 42))` and read
what the runtime reported, expansion or value.

Write a form whose evaluation gives what the with- macro yields.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro with-ant-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-ant-pace 42))"}}]}
```

### G10-16 record 2

**form**: `(do (defmacro with-ant-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-ant-pace 42))`  •  **expected**: `42`

```
All summer long, the Ant worked while the Grasshopper sang.

With a twig, Hum the grasshopper marked out a wager in the woods: whoever
guessed the result of `(do (defmacro with-ant-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-ant-pace 42))` first would win the right to
choose the next song. Tic the ant, her eyes always on the path, said it was easier
to ask the REPL about a with-X macro pattern that binds a local and runs body than to argue.

What Clojure form computes what the with- macro yields? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro with-ant-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-ant-pace 42))"}}]}
```

### G10-16 record 3

**form**: `(do (defmacro with-ant-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-ant-pace 42))`  •  **expected**: `42`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. All this took place by the woods.

"A macro is just a function that runs at compile time," Tic explained
by the woods, without complaint. Chirp, with a smug grin, said
he could already see what a with-X macro pattern that binds a local and runs body meant.
Tic the ant insisted they actually evaluate `(do (defmacro with-ant-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-ant-pace 42))` and read
what the runtime reported, expansion or value.

Write a form whose evaluation gives what the with- macro yields.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro with-ant-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-ant-pace 42))"}}]}
```

### G10-16 record 4

**form**: `(do (defmacro with-ant-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-ant-pace 42))`  •  **expected**: `42`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Chirp the grasshopper insisted near the forest that macros were the same as
functions. Bit the ant, saying very little, drew the form `(do (defmacro with-ant-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-ant-pace 42))` on
a strip of bark. "The difference," they said, "is in
a with-X macro pattern that binds a local and runs body. Submit the form and let the runtime tell us
exactly what it does."

Write a Clojure expression that computes what the with- macro yields.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro with-ant-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-ant-pace 42))"}}]}
```

### G10-16 record 5

**form**: `(do (defmacro with-ant-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-ant-pace 42))`  •  **expected**: `42`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. All this took place near the garden.

"A macro is just a function that runs at compile time," Bit explained
at the edge of the garden, stepping deliberately. Skip, swaggering through the underbrush, said
she could already see what a with-X macro pattern that binds a local and runs body meant.
Bit the ant insisted they actually evaluate `(do (defmacro with-ant-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-ant-pace 42))` and read
what the runtime reported, expansion or value.

Write a form whose evaluation gives what the with- macro yields.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro with-ant-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-ant-pace 42))"}}]}
```


---

**Grade 10 totals: 16 subjects, 80 records.**
