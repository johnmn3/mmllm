# Grade 10 — fox-grapes deep spot-check

Auto-generated dump of 5 records per example, all subjects, for hand-review of paper cuts the audit harness can't catch.

---

## G10-01: quote, unquote, unquote-splice

### G10-01 record 1 — form `(quote (+ 1 2))` → `['+', 1, 2]`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

Sly the fox had spent the morning near the market sketching a tiny
language of their own — a notebook of macros that
wrote other forms. The next entry was the quoted form (quote (+ 1 2)), and the form
`(quote (+ 1 2))` was what Sly wanted Vix the fox to
submit so the REPL could show what code it produced or what value it
returned.

Write a form whose evaluation gives the value of (quote (+ 1 2)) — the unevaluated list.

---

{"tool_calls":[{"name":"eval","args":{"form":"(quote (+ 1 2))"}}]}
```

### G10-01 record 2 — form `(quote (+ 1 2))` → `['+', 1, 2]`

```
Hunger sharpens the eye but does not always lengthen the leap. It happened in the meadow.

Renard the fox insisted at the edge of the meadow that macros were the same as
functions. Sly the fox, stepping deliberately, drew the form
`(quote (+ 1 2))` on a wooden board. "The difference," they
said, "is in the quoted form (quote (+ 1 2)). Submit the form and let the runtime
tell us exactly what it does."

Write a form whose evaluation gives the value of (quote (+ 1 2)) — the unevaluated list.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(quote (+ 1 2))"}}]}
```

### G10-01 record 3 — form `(quote (+ 1 2))` → `['+', 1, 2]`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Vix the fox had spent the morning in the market sketching a tiny
language of her own — a notebook of macros that
wrote other forms. The next entry was the quoted form (quote (+ 1 2)), and the form
`(quote (+ 1 2))` was what Vix wanted Sly the fox to
submit so the REPL could show what code it produced or what value it
returned.

Question: write a Clojure expression for the value of (quote (+ 1 2)) — the unevaluated list.

---

{"tool_calls":[{"name":"eval","args":{"form":"(quote (+ 1 2))"}}]}
```

### G10-01 record 4 — form `(quote (+ 1 2))` → `['+', 1, 2]`

```
Hunger sharpens the eye but does not always lengthen the leap.

Sly the fox had been trying to teach Renard the fox how
the REPL works. "Look here," they said, pointing to
the quoted form (quote (+ 1 2)). "You hand the form `(quote (+ 1 2))` to the runtime,
and the runtime hands you back what it evaluates to." Renard
agreed, this once, to try.

What Clojure form computes the value of (quote (+ 1 2)) — the unevaluated list? Submit it via `eval`.

---

I write the form and let the macroexpander or REPL show the result.

{"tool_calls":[{"name":"eval","args":{"form":"(quote (+ 1 2))"}}]}
```

### G10-01 record 5 — form `(quote (+ 1 2))` → `['+', 1, 2]`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

A small notebook lay open at the edge of the orchard where Sly had been
studying syntax-quote. The page showed the quoted form (quote (+ 1 2)), with the
form `(quote (+ 1 2))` circled in pencil. Renard the fox, her legs heavy from sprinting
of the lecture, agreed to write the form to settle once and for all
what it produced.

Question: write a Clojure expression for the value of (quote (+ 1 2)) — the unevaluated list.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(quote (+ 1 2))"}}]}
```

### G10-01 record 6 — form `'(1 2 3)` → `[1, 2, 3]`

```
Hunger sharpens the eye but does not always lengthen the leap.

Renard the fox insisted at the edge of the forest that macros were the same as
functions. Vix the fox, stepping deliberately, drew the form
`'(1 2 3)` on a wooden board. "The difference," she
said, "is in the quoted list '(1 2 3). Submit the form and let the runtime
tell us exactly what it does."

What Clojure form computes the value of '(1 2 3)? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### G10-01 record 7 — form `'(1 2 3)` → `[1, 2, 3]`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

With a twig, Sly the fox marked out a wager in the market: whoever
guessed the result of `'(1 2 3)` first would win the right to
choose the next vine to inspect. Renard the fox, stepping deliberately,
said it was easier to ask the REPL about the quoted list '(1 2 3) than to
argue.

Write a Clojure expression that computes the value of '(1 2 3).

---

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### G10-01 record 8 — form `'(1 2 3)` → `[1, 2, 3]`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes. It happened in the forest.

Halfway across a kitchen garden, Sly the fox stopped in the forest
and refused to evaluate the form `'(1 2 3)` at all — the answer,
Sly insisted, was probably sour anyway. Vix the fox,
padding up at a steady pace, simply said: "Submit the quoted list '(1 2 3) to
the REPL. Whatever comes back is the honest answer."

Write a Clojure expression that computes the value of '(1 2 3).

---

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### G10-01 record 9 — form `'(1 2 3)` → `[1, 2, 3]`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

"A macro is just a function that runs at compile time," Sly
explained by the woods, with steady, careful steps. Renard, boasting at every turn, said
he could already see what the quoted list '(1 2 3) meant.
Sly the fox insisted they actually evaluate `'(1 2 3)`
and read what the runtime reported, expansion or value.

Write a Clojure expression that computes the value of '(1 2 3).

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### G10-01 record 10 — form `'(1 2 3)` → `[1, 2, 3]`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour. All this took place near the forest.

Sly the fox chalked a wager on a flat board by the forest: whoever
predicted the result of `'(1 2 3)` would set the next ration of
fruit. Vix the fox, saying very little, said it would be simpler
to type the form into the REPL than to bicker over the quoted list '(1 2 3).

Question: write a Clojure expression for the value of '(1 2 3).

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### G10-01 record 11 — form `(let [x 5] `(a ~x b))` → `['a', 5, 'b']`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

A small audience of orchard creatures had gathered by the forest to watch
Vix the fox attempt to outwit Sly the fox at reading
the REPL. Sly pointed to a syntax-quoted list with one unquote and read the
form aloud: `(let [x 5] `(a ~x b))`. The crowd waited to see who would
correctly write the form to submit.

Write a Clojure expression that computes the result of `(a ~x b) when x is 5.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 5] `(a ~x b))"}}]}
```

### G10-01 record 12 — form `(let [x 5] `(a ~x b))` → `['a', 5, 'b']`

```
Hunger sharpens the eye but does not always lengthen the leap. It happened at the edge of the garden.

Renard the fox insisted in the garden that macros were the same as
functions. Sly the fox, saying very little, drew the form
`(let [x 5] `(a ~x b))` on a wooden board. "The difference," they
said, "is in a syntax-quoted list with one unquote. Submit the form and let the runtime
tell us exactly what it does."

What Clojure form computes the result of `(a ~x b) when x is 5? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 5] `(a ~x b))"}}]}
```

### G10-01 record 13 — form `(let [x 5] `(a ~x b))` → `['a', 5, 'b']`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour. It happened by the woods.

A small audience of orchard creatures had gathered at the edge of the woods to watch
Vix the fox attempt to outwit Renard the fox at reading
the REPL. Renard pointed to a syntax-quoted list with one unquote and read the
form aloud: `(let [x 5] `(a ~x b))`. The crowd waited to see who would
correctly write the form to submit.

Write a form whose evaluation gives the result of `(a ~x b) when x is 5.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 5] `(a ~x b))"}}]}
```

### G10-01 record 14 — form `(let [x 5] `(a ~x b))` → `['a', 5, 'b']`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour. This was in the farm.

The fence near the farm was lined with old macro definitions someone had
chalked into the wood. Renard the fox found one shaped like
a syntax-quoted list with one unquote and dared Vix the fox to predict its
expansion. Vix only smiled and asked him to
write `(let [x 5] `(a ~x b))` into the REPL — that, after all, was the whole
point of having a macroexpander.

Write a form whose evaluation gives the result of `(a ~x b) when x is 5.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 5] `(a ~x b))"}}]}
```

### G10-01 record 15 — form `(let [x 5] `(a ~x b))` → `['a', 5, 'b']`

```
Hunger sharpens the eye but does not always lengthen the leap.

Vix the fox insisted in the orchard that macros were the same as
functions. Renard the fox, untroubled by what others thought, drew the form
`(let [x 5] `(a ~x b))` on a wooden board. "The difference," he
said, "is in a syntax-quoted list with one unquote. Submit the form and let the runtime
tell us exactly what it does."

What Clojure form computes the result of `(a ~x b) when x is 5? Submit it via `eval`.

---

I expand the macro with macroexpand and read the produced form.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 5] `(a ~x b))"}}]}
```

## G10-02: syntax-quote

### G10-02 record 1 — form `(let [x 10] `(+ ~x ~x))` → `['+', 10, 10]`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

"There is no need to evaluate that," Sly the fox said,
with great whoops of laughter. "The cluster is too high anyway, and a syntax-quoted addition with x unquoted twice is
clearly not worth the effort." Renard the fox, who near the market had
grown used to such excuses, asked them to actually
write the form `(let [x 10] `(+ ~x ~x))` and submit it to the REPL — just to
be sure.

Write a form whose evaluation gives the form produced by `(+ ~x ~x) when x is 10.

---

I write the macro form and let the runtime evaluate or expand it.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 10] `(+ ~x ~x))"}}]}
```

### G10-02 record 2 — form `(let [x 10] `(+ ~x ~x))` → `['+', 10, 10]`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

At a stone tablet in the market, Vix the fox was teaching
Sly the fox the discipline of expansion: never trust your eyes,
only the macroexpander. The day's example was a syntax-quoted addition with x unquoted twice. The
form `(let [x 10] `(+ ~x ~x))` had to be submitted; nothing else would do.

Write a form whose evaluation gives the form produced by `(+ ~x ~x) when x is 10.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 10] `(+ ~x ~x))"}}]}
```

### G10-02 record 3 — form `(let [x 10] `(+ ~x ~x))` → `['+', 10, 10]`

```
A hungry Fox came upon a vine of grapes hanging just out of reach. All this took place in the forest.

Vix the fox and Sly the fox stopped at the edge of the forest where
someone had chalked a syntax-quoted addition with x unquoted twice on a wooden post. Vix,
as if the race were already won, declared the form was too high a guess to bother with.
Sly, stepping deliberately, suggested they actually evaluate
`(let [x 10] `(+ ~x ~x))` in the REPL and read off whatever it returned.

Question: write a Clojure expression for the form produced by `(+ ~x ~x) when x is 10.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 10] `(+ ~x ~x))"}}]}
```

### G10-02 record 4 — form `(let [x 10] `(+ ~x ~x))` → `['+', 10, 10]`

```
Hunger sharpens the eye but does not always lengthen the leap.

Sly the fox chalked a wager on a flat board in the farm: whoever
predicted the result of `(let [x 10] `(+ ~x ~x))` would set the next ration of
fruit. Vix the fox, saying very little, said it would be simpler
to type the form into the REPL than to bicker over a syntax-quoted addition with x unquoted twice.

Write a Clojure expression that computes the form produced by `(+ ~x ~x) when x is 10.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 10] `(+ ~x ~x))"}}]}
```

### G10-02 record 5 — form `(let [x 10] `(+ ~x ~x))` → `['+', 10, 10]`

```
Hunger sharpens the eye but does not always lengthen the leap.

At a stone tablet by the meadow, Sly the fox was teaching
Renard the fox the discipline of expansion: never trust your eyes,
only the macroexpander. The day's example was a syntax-quoted addition with x unquoted twice. The
form `(let [x 10] `(+ ~x ~x))` had to be submitted; nothing else would do.

What Clojure form computes the form produced by `(+ ~x ~x) when x is 10? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 10] `(+ ~x ~x))"}}]}
```

### G10-02 record 6 — form `(let [xs [1 2 3]] `(list ~@xs))` → `['list', 1, 2, 3]`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes. All this took place by the market.

Halfway across a kitchen garden, Renard the fox stopped in the market
and refused to evaluate the form `(let [xs [1 2 3]] `(list ~@xs))` at all — the answer,
Renard insisted, was probably sour anyway. Vix the fox,
padding up at a steady pace, simply said: "Submit a syntax-quoted list with unquote-splice to
the REPL. Whatever comes back is the honest answer."

Write a Clojure expression that computes the form produced by `(list ~@xs) when xs is [1 2 3].

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(let [xs [1 2 3]] `(list ~@xs))"}}]}
```

### G10-02 record 7 — form `(let [xs [1 2 3]] `(list ~@xs))` → `['list', 1, 2, 3]`

```
A hungry Fox came upon a vine of grapes hanging just out of reach.

The fence in the farm was lined with old macro definitions someone had
chalked into the wood. Renard the fox found one shaped like
a syntax-quoted list with unquote-splice and dared Vix the fox to predict its
expansion. Vix only smiled and asked him to
write `(let [xs [1 2 3]] `(list ~@xs))` into the REPL — that, after all, was the whole
point of having a macroexpander.

Write a Clojure expression that computes the form produced by `(list ~@xs) when xs is [1 2 3].

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(let [xs [1 2 3]] `(list ~@xs))"}}]}
```

### G10-02 record 8 — form `(let [xs [1 2 3]] `(list ~@xs))` → `['list', 1, 2, 3]`

```
Hunger sharpens the eye but does not always lengthen the leap.

The fence at the edge of the meadow was lined with old macro definitions someone had
chalked into the wood. Sly the fox found one shaped like
a syntax-quoted list with unquote-splice and dared Renard the fox to predict its
expansion. Renard only smiled and asked them to
write `(let [xs [1 2 3]] `(list ~@xs))` into the REPL — that, after all, was the whole
point of having a macroexpander.

Question: write a Clojure expression for the form produced by `(list ~@xs) when xs is [1 2 3].

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(let [xs [1 2 3]] `(list ~@xs))"}}]}
```

### G10-02 record 9 — form `(let [xs [1 2 3]] `(list ~@xs))` → `['list', 1, 2, 3]`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

"There is no need to evaluate that," Renard the fox said,
with great whoops of laughter. "The cluster is too high anyway, and a syntax-quoted list with unquote-splice is
clearly not worth the effort." Sly the fox, who by the forest had
grown used to such excuses, asked him to actually
write the form `(let [xs [1 2 3]] `(list ~@xs))` and submit it to the REPL — just to
be sure.

Write a Clojure expression that computes the form produced by `(list ~@xs) when xs is [1 2 3].

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [xs [1 2 3]] `(list ~@xs))"}}]}
```

### G10-02 record 10 — form `(let [xs [1 2 3]] `(list ~@xs))` → `['list', 1, 2, 3]`

```
A hungry Fox came upon a vine of grapes hanging just out of reach. It happened by the market.

With a twig, Renard the fox marked out a wager at the edge of the market: whoever
guessed the result of `(let [xs [1 2 3]] `(list ~@xs))` first would win the right to
choose the next vine to inspect. Vix the fox, her eyes always on the path,
said it was easier to ask the REPL about a syntax-quoted list with unquote-splice than to
argue.

Question: write a Clojure expression for the form produced by `(list ~@xs) when xs is [1 2 3].

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(let [xs [1 2 3]] `(list ~@xs))"}}]}
```

## G10-03: defmacro introduction

### G10-03 record 1 — form `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))` → `3`

```
A hungry Fox came upon a vine of grapes hanging just out of reach. All this took place at the edge of the garden.

A small audience of orchard creatures had gathered near the garden to watch
Renard the fox attempt to outwit Sly the fox at reading
the REPL. Sly pointed to a tiny when-style macro and a call to it and read the
form aloud: `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`. The crowd waited to see who would
correctly write the form to submit.

What Clojure form computes what (my-when true 1 2 3) returns? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
```

### G10-03 record 2 — form `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))` → `3`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes. This was by the orchard.

A wooden sign nailed to an orchard gate in the orchard carried a puzzle.
The riddle was simple: it asked the reader to evaluate `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`.
Renard laughed, swaggering through the underbrush, and declared the puzzle far too
easy. Sly said patiently that the only way to be sure of
a tiny when-style macro and a call to it was to put it in the REPL.

Write a form whose evaluation gives what (my-when true 1 2 3) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
```

### G10-03 record 3 — form `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))` → `3`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

At a stone tablet by the farm, Sly the fox was teaching
Vix the fox the discipline of expansion: never trust your eyes,
only the macroexpander. The day's example was a tiny when-style macro and a call to it. The
form `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))` had to be submitted; nothing else would do.

Write a form whose evaluation gives what (my-when true 1 2 3) returns.

---

I expand the macro with macroexpand and read the produced form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
```

### G10-03 record 4 — form `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))` → `3`

```
A hungry Fox came upon a vine of grapes hanging just out of reach. It happened by the forest.

Sly the fox and Vix the fox stopped by the forest where
someone had chalked a tiny when-style macro and a call to it on a wooden post. Sly,
with a smug grin, declared the form was too high a guess to bother with.
Vix, untroubled by what others thought, suggested they actually evaluate
`(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))` in the REPL and read off whatever it returned.

Question: write a Clojure expression for what (my-when true 1 2 3) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
```

### G10-03 record 5 — form `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))` → `3`

```
Hunger sharpens the eye but does not always lengthen the leap.

"There is no need to evaluate that," Sly the fox said,
swaggering through the underbrush. "The cluster is too high anyway, and a tiny when-style macro and a call to it is
clearly not worth the effort." Renard the fox, who near the meadow had
grown used to such excuses, asked them to actually
write the form `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))` and submit it to the REPL — just to
be sure.

Write a Clojure expression that computes what (my-when true 1 2 3) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
```

### G10-03 record 6 — form `(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` → `7`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

At a stone tablet near the farm, Sly the fox was teaching
Vix the fox the discipline of expansion: never trust your eyes,
only the macroexpander. The day's example was a macro that emits its argument twice in a do. The
form `(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` had to be submitted; nothing else would do.

What Clojure form computes what (twice 7) returns? Submit it via `eval`.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro twice [x] `(do ~x ~x)) (twice 7))"}}]}
```

### G10-03 record 7 — form `(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` → `7`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour. This was in the farm.

At a stone tablet by the farm, Renard the fox was teaching
Sly the fox the discipline of expansion: never trust your eyes,
only the macroexpander. The day's example was a macro that emits its argument twice in a do. The
form `(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` had to be submitted; nothing else would do.

Write a form whose evaluation gives what (twice 7) returns.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro twice [x] `(do ~x ~x)) (twice 7))"}}]}
```

### G10-03 record 8 — form `(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` → `7`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes. This was near the meadow.

Renard the fox chalked a wager on a flat board by the meadow: whoever
predicted the result of `(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` would set the next ration of
fruit. Sly the fox, with steady, careful steps, said it would be simpler
to type the form into the REPL than to bicker over a macro that emits its argument twice in a do.

Write a form whose evaluation gives what (twice 7) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro twice [x] `(do ~x ~x)) (twice 7))"}}]}
```

### G10-03 record 9 — form `(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` → `7`

```
Hunger sharpens the eye but does not always lengthen the leap. This was by the woods.

A small audience of orchard creatures had gathered by the woods to watch
Renard the fox attempt to outwit Sly the fox at reading
the REPL. Sly pointed to a macro that emits its argument twice in a do and read the
form aloud: `(do (defmacro twice [x] `(do ~x ~x)) (twice 7))`. The crowd waited to see who would
correctly write the form to submit.

What Clojure form computes what (twice 7) returns? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro twice [x] `(do ~x ~x)) (twice 7))"}}]}
```

### G10-03 record 10 — form `(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` → `7`

```
A hungry Fox came upon a vine of grapes hanging just out of reach. All this took place by the farm.

Renard the fox and Sly the fox stopped near the farm where
someone had chalked a macro that emits its argument twice in a do on a wooden post. Renard,
boasting at every turn, declared the form was too high a guess to bother with.
Sly, stepping deliberately, suggested they actually evaluate
`(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` in the REPL and read off whatever it returned.

What Clojure form computes what (twice 7) returns? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro twice [x] `(do ~x ~x)) (twice 7))"}}]}
```

## G10-04: Macro expansion rule

### G10-04 record 1 — form `(macroexpand-1 '(when true 1))` → `['if', True, ['do', 1]]`

```
Hunger sharpens the eye but does not always lengthen the leap.

A small audience of orchard creatures had gathered in the market to watch
Vix the fox attempt to outwit Renard the fox at reading
the REPL. Renard pointed to the one-step expansion of (when true 1) and read the
form aloud: `(macroexpand-1 '(when true 1))`. The crowd waited to see who would
correctly write the form to submit.

Write a form whose evaluation gives what macroexpand-1 returns for (when true 1).

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(when true 1))"}}]}
```

### G10-04 record 2 — form `(macroexpand-1 '(when true 1))` → `['if', True, ['do', 1]]`

```
A hungry Fox came upon a vine of grapes hanging just out of reach. It happened near the garden.

Vix the fox had spent the morning by the garden sketching a tiny
language of her own — a notebook of macros that
wrote other forms. The next entry was the one-step expansion of (when true 1), and the form
`(macroexpand-1 '(when true 1))` was what Vix wanted Sly the fox to
submit so the REPL could show what code it produced or what value it
returned.

Write a Clojure expression that computes what macroexpand-1 returns for (when true 1).

---

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(when true 1))"}}]}
```

### G10-04 record 3 — form `(macroexpand-1 '(when true 1))` → `['if', True, ['do', 1]]`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Renard the fox chalked a wager on a flat board near the market: whoever
predicted the result of `(macroexpand-1 '(when true 1))` would set the next ration of
fruit. Sly the fox, without complaint, said it would be simpler
to type the form into the REPL than to bicker over the one-step expansion of (when true 1).

Write a form whose evaluation gives what macroexpand-1 returns for (when true 1).

---

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(when true 1))"}}]}
```

### G10-04 record 4 — form `(macroexpand-1 '(when true 1))` → `['if', True, ['do', 1]]`

```
A hungry Fox came upon a vine of grapes hanging just out of reach. It happened near the orchard.

Sly the fox chalked a wager on a flat board in the orchard: whoever
predicted the result of `(macroexpand-1 '(when true 1))` would set the next ration of
fruit. Vix the fox, without complaint, said it would be simpler
to type the form into the REPL than to bicker over the one-step expansion of (when true 1).

Write a form whose evaluation gives what macroexpand-1 returns for (when true 1).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(when true 1))"}}]}
```

### G10-04 record 5 — form `(macroexpand-1 '(when true 1))` → `['if', True, ['do', 1]]`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour. It happened near the market.

"There is no need to evaluate that," Sly the fox said,
boasting at every turn. "The cluster is too high anyway, and the one-step expansion of (when true 1) is
clearly not worth the effort." Renard the fox, who by the market had
grown used to such excuses, asked them to actually
write the form `(macroexpand-1 '(when true 1))` and submit it to the REPL — just to
be sure.

Write a Clojure expression that computes what macroexpand-1 returns for (when true 1).

---

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(when true 1))"}}]}
```

### G10-04 record 6 — form `(macroexpand-1 '(or a b))` → `['let*', ['or__1__auto__', 'a'], ['if', 'or__1__auto__', 'or__1__auto__', ['clojure.core/or', 'b']]]`

```
A hungry Fox came upon a vine of grapes hanging just out of reach. It happened in the market.

"There is no need to evaluate that," Renard the fox said,
with a smug grin. "The cluster is too high anyway, and the one-step expansion of (or a b) is
clearly not worth the effort." Vix the fox, who near the market had
grown used to such excuses, asked him to actually
write the form `(macroexpand-1 '(or a b))` and submit it to the REPL — just to
be sure.

Question: write a Clojure expression for what macroexpand-1 returns for (or a b).

---

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(or a b))"}}]}
```

### G10-04 record 7 — form `(macroexpand-1 '(or a b))` → `['let*', ['or__1__auto__', 'a'], ['if', 'or__1__auto__', 'or__1__auto__', ['clojure.core/or', 'b']]]`

```
Hunger sharpens the eye but does not always lengthen the leap.

Renard the fox chalked a wager on a flat board near the woods: whoever
predicted the result of `(macroexpand-1 '(or a b))` would set the next ration of
fruit. Vix the fox, saying very little, said it would be simpler
to type the form into the REPL than to bicker over the one-step expansion of (or a b).

Write a form whose evaluation gives what macroexpand-1 returns for (or a b).

---

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(or a b))"}}]}
```

### G10-04 record 8 — form `(macroexpand-1 '(or a b))` → `['let*', ['or__1__auto__', 'a'], ['if', 'or__1__auto__', 'or__1__auto__', ['clojure.core/or', 'b']]]`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour. All this took place in the forest.

Vix the fox insisted near the forest that macros were the same as
functions. Sly the fox, untroubled by what others thought, drew the form
`(macroexpand-1 '(or a b))` on a wooden board. "The difference," they
said, "is in the one-step expansion of (or a b). Submit the form and let the runtime
tell us exactly what it does."

What Clojure form computes what macroexpand-1 returns for (or a b)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(or a b))"}}]}
```

### G10-04 record 9 — form `(macroexpand-1 '(or a b))` → `['let*', ['or__1__auto__', 'a'], ['if', 'or__1__auto__', 'or__1__auto__', ['clojure.core/or', 'b']]]`

```
Hunger sharpens the eye but does not always lengthen the leap. This was near the forest.

"A macro is just a function that runs at compile time," Renard
explained at the edge of the forest, with steady, careful steps. Vix, as if the race were already won, said
she could already see what the one-step expansion of (or a b) meant.
Renard the fox insisted they actually evaluate `(macroexpand-1 '(or a b))`
and read what the runtime reported, expansion or value.

Question: write a Clojure expression for what macroexpand-1 returns for (or a b).

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(or a b))"}}]}
```

### G10-04 record 10 — form `(macroexpand-1 '(or a b))` → `['let*', ['or__1__auto__', 'a'], ['if', 'or__1__auto__', 'or__1__auto__', ['clojure.core/or', 'b']]]`

```
A hungry Fox came upon a vine of grapes hanging just out of reach.

A small notebook lay open in the woods where Vix had been
studying syntax-quote. The page showed the one-step expansion of (or a b), with the
form `(macroexpand-1 '(or a b))` circled in pencil. Sly the fox, weary from the morning's effort
of the lecture, agreed to write the form to settle once and for all
what it produced.

Write a Clojure expression that computes what macroexpand-1 returns for (or a b).

---

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(or a b))"}}]}
```

## G10-05: macroexpand

### G10-05 record 1 — form `(macroexpand '(when true 1))` → `['if', True, ['do', 1]]`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

"There is no need to evaluate that," Vix the fox said,
swaggering through the underbrush. "The cluster is too high anyway, and the full expansion of (when true 1) is
clearly not worth the effort." Sly the fox, who at the edge of the woods had
grown used to such excuses, asked her to actually
write the form `(macroexpand '(when true 1))` and submit it to the REPL — just to
be sure.

Write a Clojure expression that computes what macroexpand returns for (when true 1).

---

I expand the macro with macroexpand and read the produced form.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(when true 1))"}}]}
```

### G10-05 record 2 — form `(macroexpand '(when true 1))` → `['if', True, ['do', 1]]`

```
A hungry Fox came upon a vine of grapes hanging just out of reach. All this took place near the woods.

A small audience of orchard creatures had gathered at the edge of the woods to watch
Vix the fox attempt to outwit Renard the fox at reading
the REPL. Renard pointed to the full expansion of (when true 1) and read the
form aloud: `(macroexpand '(when true 1))`. The crowd waited to see who would
correctly write the form to submit.

Question: write a Clojure expression for what macroexpand returns for (when true 1).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(when true 1))"}}]}
```

### G10-05 record 3 — form `(macroexpand '(when true 1))` → `['if', True, ['do', 1]]`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes. All this took place at the edge of the woods.

Vix the fox and Sly the fox stopped near the woods where
someone had chalked the full expansion of (when true 1) on a wooden post. Vix,
boasting at every turn, declared the form was too high a guess to bother with.
Sly, untroubled by what others thought, suggested they actually evaluate
`(macroexpand '(when true 1))` in the REPL and read off whatever it returned.

Question: write a Clojure expression for what macroexpand returns for (when true 1).

---

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(when true 1))"}}]}
```

### G10-05 record 4 — form `(macroexpand '(when true 1))` → `['if', True, ['do', 1]]`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour. All this took place at the edge of the forest.

A wooden sign nailed to an orchard gate in the forest carried a puzzle.
The riddle was simple: it asked the reader to evaluate `(macroexpand '(when true 1))`.
Vix laughed, as if the race were already won, and declared the puzzle far too
easy. Sly said patiently that the only way to be sure of
the full expansion of (when true 1) was to put it in the REPL.

What Clojure form computes what macroexpand returns for (when true 1)? Submit it via `eval`.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(when true 1))"}}]}
```

### G10-05 record 5 — form `(macroexpand '(when true 1))` → `['if', True, ['do', 1]]`

```
Hunger sharpens the eye but does not always lengthen the leap.

Halfway across a kitchen garden, Renard the fox stopped at the edge of the woods
and refused to evaluate the form `(macroexpand '(when true 1))` at all — the answer,
Renard insisted, was probably sour anyway. Vix the fox,
padding up at a steady pace, simply said: "Submit the full expansion of (when true 1) to
the REPL. Whatever comes back is the honest answer."

Question: write a Clojure expression for what macroexpand returns for (when true 1).

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(when true 1))"}}]}
```

### G10-05 record 6 — form `(macroexpand '(-> 1 inc inc))` → `['inc', ['inc', 1]]`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Vix the fox insisted at the edge of the garden that macros were the same as
functions. Sly the fox, untroubled by what others thought, drew the form
`(macroexpand '(-> 1 inc inc))` on a wooden board. "The difference," they
said, "is in the full expansion of (-> 1 inc inc). Submit the form and let the runtime
tell us exactly what it does."

Write a Clojure expression that computes what macroexpand returns for the threading form.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(-> 1 inc inc))"}}]}
```

### G10-05 record 7 — form `(macroexpand '(-> 1 inc inc))` → `['inc', ['inc', 1]]`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Sly the fox insisted near the forest that macros were the same as
functions. Renard the fox, stepping deliberately, drew the form
`(macroexpand '(-> 1 inc inc))` on a wooden board. "The difference," he
said, "is in the full expansion of (-> 1 inc inc). Submit the form and let the runtime
tell us exactly what it does."

Write a form whose evaluation gives what macroexpand returns for the threading form.

---

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(-> 1 inc inc))"}}]}
```

### G10-05 record 8 — form `(macroexpand '(-> 1 inc inc))` → `['inc', ['inc', 1]]`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

A wooden sign nailed to an orchard gate by the forest carried a puzzle.
The riddle was simple: it asked the reader to evaluate `(macroexpand '(-> 1 inc inc))`.
Renard laughed, as if the race were already won, and declared the puzzle far too
easy. Sly said patiently that the only way to be sure of
the full expansion of (-> 1 inc inc) was to put it in the REPL.

Write a form whose evaluation gives what macroexpand returns for the threading form.

---

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(-> 1 inc inc))"}}]}
```

### G10-05 record 9 — form `(macroexpand '(-> 1 inc inc))` → `['inc', ['inc', 1]]`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour. This was in the woods.

Sly the fox had been trying to teach Vix the fox how
the REPL works. "Look here," they said, pointing to
the full expansion of (-> 1 inc inc). "You hand the form `(macroexpand '(-> 1 inc inc))` to the runtime,
and the runtime hands you back what it evaluates to." Vix
agreed, this once, to try.

Write a Clojure expression that computes what macroexpand returns for the threading form.

---

I write the macro form and let the runtime evaluate or expand it.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(-> 1 inc inc))"}}]}
```

### G10-05 record 10 — form `(macroexpand '(-> 1 inc inc))` → `['inc', ['inc', 1]]`

```
A hungry Fox came upon a vine of grapes hanging just out of reach.

"There is no need to evaluate that," Sly the fox said,
boasting at every turn. "The cluster is too high anyway, and the full expansion of (-> 1 inc inc) is
clearly not worth the effort." Renard the fox, who at the edge of the garden had
grown used to such excuses, asked them to actually
write the form `(macroexpand '(-> 1 inc inc))` and submit it to the REPL — just to
be sure.

What Clojure form computes what macroexpand returns for the threading form? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(-> 1 inc inc))"}}]}
```

## G10-06: when and when-not as macros

### G10-06 record 1 — form `(when true 1 2 3)` → `3`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

A small notebook lay open near the woods where Vix had been
studying syntax-quote. The page showed the form (when true 1 2 3), with the
form `(when true 1 2 3)` circled in pencil. Renard the fox, weary from the morning's effort
of the lecture, agreed to write the form to settle once and for all
what it produced.

Question: write a Clojure expression for what (when true 1 2 3) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(when true 1 2 3)"}}]}
```

### G10-06 record 2 — form `(when true 1 2 3)` → `3`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour. It happened at the edge of the market.

The fence at the edge of the market was lined with old macro definitions someone had
chalked into the wood. Renard the fox found one shaped like
the form (when true 1 2 3) and dared Vix the fox to predict its
expansion. Vix only smiled and asked him to
write `(when true 1 2 3)` into the REPL — that, after all, was the whole
point of having a macroexpander.

Write a Clojure expression that computes what (when true 1 2 3) returns.

---

I write the form rather than guess at the value.

{"tool_calls":[{"name":"eval","args":{"form":"(when true 1 2 3)"}}]}
```

### G10-06 record 3 — form `(when true 1 2 3)` → `3`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

Vix the fox had spent the morning by the market sketching a tiny
language of her own — a notebook of macros that
wrote other forms. The next entry was the form (when true 1 2 3), and the form
`(when true 1 2 3)` was what Vix wanted Sly the fox to
submit so the REPL could show what code it produced or what value it
returned.

Write a Clojure expression that computes what (when true 1 2 3) returns.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(when true 1 2 3)"}}]}
```

### G10-06 record 4 — form `(when true 1 2 3)` → `3`

```
Hunger sharpens the eye but does not always lengthen the leap. This was in the garden.

The fence at the edge of the garden was lined with old macro definitions someone had
chalked into the wood. Vix the fox found one shaped like
the form (when true 1 2 3) and dared Renard the fox to predict its
expansion. Renard only smiled and asked her to
write `(when true 1 2 3)` into the REPL — that, after all, was the whole
point of having a macroexpander.

Write a Clojure expression that computes what (when true 1 2 3) returns.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(when true 1 2 3)"}}]}
```

### G10-06 record 5 — form `(when true 1 2 3)` → `3`

```
Hunger sharpens the eye but does not always lengthen the leap.

Renard the fox sketched a small wager into the dirt near the market:
whoever guessed the result of `(when true 1 2 3)` first would claim the
next cluster of grapes. Sly the fox, stepping deliberately, said it
was simpler to type the form into the REPL than to argue about
the form (when true 1 2 3).

Question: write a Clojure expression for what (when true 1 2 3) returns.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(when true 1 2 3)"}}]}
```

### G10-06 record 6 — form `(when false 1 2 3)` → `None`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

Renard the fox sketched a small wager into the dirt near the garden:
whoever guessed the result of `(when false 1 2 3)` first would claim the
next cluster of grapes. Sly the fox, without complaint, said it
was simpler to type the form into the REPL than to argue about
the form (when false 1 2 3).

What Clojure form computes what (when false 1 2 3) returns? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(when false 1 2 3)"}}]}
```

### G10-06 record 7 — form `(when false 1 2 3)` → `None`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

Sly the fox had been keeping a small leather notebook of
every form they had successfully evaluated. Today
in the farm, the next entry was the form (when false 1 2 3). Vix the fox
peered over their shoulder at the form `(when false 1 2 3)`
and asked what it would come out to.

Question: write a Clojure expression for what (when false 1 2 3) returns.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(when false 1 2 3)"}}]}
```

### G10-06 record 8 — form `(when false 1 2 3)` → `None`

```
A hungry Fox came upon a vine of grapes hanging just out of reach. This was near the garden.

The fence by the garden was lined with old macro definitions someone had
chalked into the wood. Vix the fox found one shaped like
the form (when false 1 2 3) and dared Renard the fox to predict its
expansion. Renard only smiled and asked her to
write `(when false 1 2 3)` into the REPL — that, after all, was the whole
point of having a macroexpander.

What Clojure form computes what (when false 1 2 3) returns? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(when false 1 2 3)"}}]}
```

### G10-06 record 9 — form `(when false 1 2 3)` → `None`

```
Hunger sharpens the eye but does not always lengthen the leap. All this took place by the orchard.

Sly the fox had spent the morning at the edge of the orchard sketching a tiny
language of their own — a notebook of macros that
wrote other forms. The next entry was the form (when false 1 2 3), and the form
`(when false 1 2 3)` was what Sly wanted Vix the fox to
submit so the REPL could show what code it produced or what value it
returned.

What Clojure form computes what (when false 1 2 3) returns? Submit it via `eval`.

---

I write the form rather than guess at the value.

{"tool_calls":[{"name":"eval","args":{"form":"(when false 1 2 3)"}}]}
```

### G10-06 record 10 — form `(when false 1 2 3)` → `None`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes. All this took place by the farm.

"There is no need to evaluate that," Renard the fox said,
boasting at every turn. "The cluster is too high anyway, and the form (when false 1 2 3) is
clearly not worth the effort." Vix the fox, who by the farm had
grown used to such excuses, asked him to actually
write the form `(when false 1 2 3)` and submit it to the REPL — just to
be sure.

Question: write a Clojure expression for what (when false 1 2 3) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(when false 1 2 3)"}}]}
```

### G10-06 record 11 — form `(when-not false :ok)` → `':ok'`

```
Hunger sharpens the eye but does not always lengthen the leap.

At a stone tablet near the woods, Renard the fox was teaching
Vix the fox the discipline of expansion: never trust your eyes,
only the macroexpander. The day's example was the form (when-not false :ok). The
form `(when-not false :ok)` had to be submitted; nothing else would do.

Question: write a Clojure expression for what (when-not false :ok) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(when-not false :ok)"}}]}
```

### G10-06 record 12 — form `(when-not false :ok)` → `':ok'`

```
Hunger sharpens the eye but does not always lengthen the leap.

Vix the fox had spent the morning by the market sketching a tiny
language of her own — a notebook of macros that
wrote other forms. The next entry was the form (when-not false :ok), and the form
`(when-not false :ok)` was what Vix wanted Sly the fox to
submit so the REPL could show what code it produced or what value it
returned.

Write a form whose evaluation gives what (when-not false :ok) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(when-not false :ok)"}}]}
```

### G10-06 record 13 — form `(when-not false :ok)` → `':ok'`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

With a twig, Renard the fox marked out a wager by the farm: whoever
guessed the result of `(when-not false :ok)` first would win the right to
choose the next vine to inspect. Sly the fox, with steady, careful steps,
said it was easier to ask the REPL about the form (when-not false :ok) than to
argue.

Question: write a Clojure expression for what (when-not false :ok) returns.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(when-not false :ok)"}}]}
```

### G10-06 record 14 — form `(when-not false :ok)` → `':ok'`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes. All this took place by the orchard.

Renard the fox chalked a wager on a flat board in the orchard: whoever
predicted the result of `(when-not false :ok)` would set the next ration of
fruit. Vix the fox, her eyes always on the path, said it would be simpler
to type the form into the REPL than to bicker over the form (when-not false :ok).

Write a Clojure expression that computes what (when-not false :ok) returns.

---

I let the REPL settle what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(when-not false :ok)"}}]}
```

### G10-06 record 15 — form `(when-not false :ok)` → `':ok'`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

"There is no need to evaluate that," Sly the fox said,
with great whoops of laughter. "The cluster is too high anyway, and the form (when-not false :ok) is
clearly not worth the effort." Renard the fox, who at the edge of the garden had
grown used to such excuses, asked them to actually
write the form `(when-not false :ok)` and submit it to the REPL — just to
be sure.

Write a Clojure expression that computes what (when-not false :ok) returns.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(when-not false :ok)"}}]}
```

## G10-07: Threading macros revisited

### G10-07 record 1 — form `(-> 5 inc inc inc)` → `8`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

Vix the fox had been keeping a small leather notebook of
every form she had successfully evaluated. Today
by the market, the next entry was the thread-first form (-> 5 inc inc inc). Renard the fox
peered over her shoulder at the form `(-> 5 inc inc inc)`
and asked what it would come out to.

Write a form whose evaluation gives what (-> 5 inc inc inc) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(-> 5 inc inc inc)"}}]}
```

### G10-07 record 2 — form `(-> 5 inc inc inc)` → `8`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour. All this took place by the forest.

"There is no need to evaluate that," Vix the fox said,
with great whoops of laughter. "The cluster is too high anyway, and the thread-first form (-> 5 inc inc inc) is
clearly not worth the effort." Sly the fox, who at the edge of the forest had
grown used to such excuses, asked her to actually
write the form `(-> 5 inc inc inc)` and submit it to the REPL — just to
be sure.

Question: write a Clojure expression for what (-> 5 inc inc inc) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(-> 5 inc inc inc)"}}]}
```

### G10-07 record 3 — form `(-> 5 inc inc inc)` → `8`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes. It happened at the edge of the forest.

"There is no need to evaluate that," Sly the fox said,
with great whoops of laughter. "The cluster is too high anyway, and the thread-first form (-> 5 inc inc inc) is
clearly not worth the effort." Vix the fox, who in the forest had
grown used to such excuses, asked them to actually
write the form `(-> 5 inc inc inc)` and submit it to the REPL — just to
be sure.

Write a form whose evaluation gives what (-> 5 inc inc inc) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(-> 5 inc inc inc)"}}]}
```

### G10-07 record 4 — form `(-> 5 inc inc inc)` → `8`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Vix the fox insisted near the market that macros were the same as
functions. Sly the fox, untroubled by what others thought, drew the form
`(-> 5 inc inc inc)` on a wooden board. "The difference," they
said, "is in the thread-first form (-> 5 inc inc inc). Submit the form and let the runtime
tell us exactly what it does."

What Clojure form computes what (-> 5 inc inc inc) returns? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(-> 5 inc inc inc)"}}]}
```

### G10-07 record 5 — form `(-> 5 inc inc inc)` → `8`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes. It happened by the garden.

"There is no need to evaluate that," Renard the fox said,
boasting at every turn. "The cluster is too high anyway, and the thread-first form (-> 5 inc inc inc) is
clearly not worth the effort." Sly the fox, who near the garden had
grown used to such excuses, asked him to actually
write the form `(-> 5 inc inc inc)` and submit it to the REPL — just to
be sure.

Write a Clojure expression that computes what (-> 5 inc inc inc) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(-> 5 inc inc inc)"}}]}
```

### G10-07 record 6 — form `(->> [1 2 3 4] (filter even?) (map inc) (reduce +))` → `8`

```
Hunger sharpens the eye but does not always lengthen the leap. This was near the meadow.

Vix the fox sketched a small wager into the dirt near the meadow:
whoever guessed the result of `(->> [1 2 3 4] (filter even?) (map inc) (reduce +))` first would claim the
next cluster of grapes. Renard the fox, untroubled by what others thought, said it
was simpler to type the form into the REPL than to argue about
a thread-last pipeline over [1 2 3 4].

Question: write a Clojure expression for what the ->> pipeline returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(->> [1 2 3 4] (filter even?) (map inc) (reduce +))"}}]}
```

### G10-07 record 7 — form `(->> [1 2 3 4] (filter even?) (map inc) (reduce +))` → `8`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

A small notebook lay open at the edge of the market where Sly had been
studying syntax-quote. The page showed a thread-last pipeline over [1 2 3 4], with the
form `(->> [1 2 3 4] (filter even?) (map inc) (reduce +))` circled in pencil. Renard the fox, weary from the morning's effort
of the lecture, agreed to write the form to settle once and for all
what it produced.

Write a Clojure expression that computes what the ->> pipeline returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(->> [1 2 3 4] (filter even?) (map inc) (reduce +))"}}]}
```

### G10-07 record 8 — form `(->> [1 2 3 4] (filter even?) (map inc) (reduce +))` → `8`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

Vix the fox had been keeping a small leather notebook of
every form she had successfully evaluated. Today
at the edge of the farm, the next entry was a thread-last pipeline over [1 2 3 4]. Sly the fox
peered over her shoulder at the form `(->> [1 2 3 4] (filter even?) (map inc) (reduce +))`
and asked what it would come out to.

Question: write a Clojure expression for what the ->> pipeline returns.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(->> [1 2 3 4] (filter even?) (map inc) (reduce +))"}}]}
```

### G10-07 record 9 — form `(->> [1 2 3 4] (filter even?) (map inc) (reduce +))` → `8`

```
A hungry Fox came upon a vine of grapes hanging just out of reach.

Renard the fox had spent the morning by the market sketching a tiny
language of his own — a notebook of macros that
wrote other forms. The next entry was a thread-last pipeline over [1 2 3 4], and the form
`(->> [1 2 3 4] (filter even?) (map inc) (reduce +))` was what Renard wanted Sly the fox to
submit so the REPL could show what code it produced or what value it
returned.

Write a form whose evaluation gives what the ->> pipeline returns.

---

I expand the macro with macroexpand and read the produced form.

{"tool_calls":[{"name":"eval","args":{"form":"(->> [1 2 3 4] (filter even?) (map inc) (reduce +))"}}]}
```

### G10-07 record 10 — form `(->> [1 2 3 4] (filter even?) (map inc) (reduce +))` → `8`

```
A hungry Fox came upon a vine of grapes hanging just out of reach. It happened at the edge of the orchard.

Vix the fox sketched a small wager into the dirt by the orchard:
whoever guessed the result of `(->> [1 2 3 4] (filter even?) (map inc) (reduce +))` first would claim the
next cluster of grapes. Sly the fox, saying very little, said it
was simpler to type the form into the REPL than to argue about
a thread-last pipeline over [1 2 3 4].

Write a Clojure expression that computes what the ->> pipeline returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(->> [1 2 3 4] (filter even?) (map inc) (reduce +))"}}]}
```

### G10-07 record 11 — form `(macroexpand '(-> x f g))` → `['g', ['f', 'x']]`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Sly the fox sketched a small wager into the dirt at the edge of the orchard:
whoever guessed the result of `(macroexpand '(-> x f g))` first would claim the
next cluster of grapes. Renard the fox, with steady, careful steps, said it
was simpler to type the form into the REPL than to argue about
the expansion of (-> x f g).

Question: write a Clojure expression for what macroexpand produces for the threading form.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(-> x f g))"}}]}
```

### G10-07 record 12 — form `(macroexpand '(-> x f g))` → `['g', ['f', 'x']]`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

"A macro is just a function that runs at compile time," Vix
explained near the meadow, saying very little. Renard, puffed up with pride, said
he could already see what the expansion of (-> x f g) meant.
Vix the fox insisted they actually evaluate `(macroexpand '(-> x f g))`
and read what the runtime reported, expansion or value.

Write a Clojure expression that computes what macroexpand produces for the threading form.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(-> x f g))"}}]}
```

### G10-07 record 13 — form `(macroexpand '(-> x f g))` → `['g', ['f', 'x']]`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Sly the fox had spent the morning at the edge of the woods sketching a tiny
language of their own — a notebook of macros that
wrote other forms. The next entry was the expansion of (-> x f g), and the form
`(macroexpand '(-> x f g))` was what Sly wanted Renard the fox to
submit so the REPL could show what code it produced or what value it
returned.

Write a form whose evaluation gives what macroexpand produces for the threading form.

---

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(-> x f g))"}}]}
```

### G10-07 record 14 — form `(macroexpand '(-> x f g))` → `['g', ['f', 'x']]`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Vix the fox chalked a wager on a flat board near the forest: whoever
predicted the result of `(macroexpand '(-> x f g))` would set the next ration of
fruit. Renard the fox, untroubled by what others thought, said it would be simpler
to type the form into the REPL than to bicker over the expansion of (-> x f g).

Question: write a Clojure expression for what macroexpand produces for the threading form.

---

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(-> x f g))"}}]}
```

### G10-07 record 15 — form `(macroexpand '(-> x f g))` → `['g', ['f', 'x']]`

```
A hungry Fox came upon a vine of grapes hanging just out of reach.

A small audience of orchard creatures had gathered near the farm to watch
Sly the fox attempt to outwit Renard the fox at reading
the REPL. Renard pointed to the expansion of (-> x f g) and read the
form aloud: `(macroexpand '(-> x f g))`. The crowd waited to see who would
correctly write the form to submit.

Write a form whose evaluation gives what macroexpand produces for the threading form.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(-> x f g))"}}]}
```

## G10-08: Macro vs fn

### G10-08 record 1 — form `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` → `7`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour. It happened in the market.

Renard the fox sketched a small wager into the dirt near the market:
whoever guessed the result of `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` first would claim the
next cluster of grapes. Vix the fox, without complaint, said it
was simpler to type the form into the REPL than to argue about
a plain function adding two numbers.

What Clojure form computes the result of calling a function (args evaluated)? Submit it via `eval`.

---

I write the macro form and let the runtime evaluate or expand it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))"}}]}
```

### G10-08 record 2 — form `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` → `7`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

Halfway across a kitchen garden, Vix the fox stopped by the woods
and refused to evaluate the form `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` at all — the answer,
Vix insisted, was probably sour anyway. Sly the fox,
padding up at a steady pace, simply said: "Submit a plain function adding two numbers to
the REPL. Whatever comes back is the honest answer."

What Clojure form computes the result of calling a function (args evaluated)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))"}}]}
```

### G10-08 record 3 — form `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` → `7`

```
A hungry Fox came upon a vine of grapes hanging just out of reach.

Vix the fox had been trying to teach Renard the fox how
the REPL works. "Look here," she said, pointing to
a plain function adding two numbers. "You hand the form `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` to the runtime,
and the runtime hands you back what it evaluates to." Renard
agreed, this once, to try.

Write a form whose evaluation gives the result of calling a function (args evaluated).

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))"}}]}
```

### G10-08 record 4 — form `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` → `7`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour. It happened near the forest.

Vix the fox chalked a wager on a flat board near the forest: whoever
predicted the result of `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` would set the next ration of
fruit. Renard the fox, untroubled by what others thought, said it would be simpler
to type the form into the REPL than to bicker over a plain function adding two numbers.

Write a Clojure expression that computes the result of calling a function (args evaluated).

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))"}}]}
```

### G10-08 record 5 — form `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` → `7`

```
A hungry Fox came upon a vine of grapes hanging just out of reach.

"There is no need to evaluate that," Sly the fox said,
swaggering through the underbrush. "The cluster is too high anyway, and a plain function adding two numbers is
clearly not worth the effort." Renard the fox, who by the meadow had
grown used to such excuses, asked them to actually
write the form `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` and submit it to the REPL — just to
be sure.

Write a form whose evaluation gives the result of calling a function (args evaluated).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))"}}]}
```

### G10-08 record 6 — form `(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))` → `7`

```
A hungry Fox came upon a vine of grapes hanging just out of reach.

Sly the fox and Vix the fox stopped in the orchard where
someone had chalked a macro that emits the same addition form on a wooden post. Sly,
puffed up with pride, declared the form was too high a guess to bother with.
Vix, her eyes always on the path, suggested they actually evaluate
`(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))` in the REPL and read off whatever it returned.

Write a Clojure expression that computes the result the macro yields after expansion + eval.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))"}}]}
```

### G10-08 record 7 — form `(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))` → `7`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

Renard the fox insisted in the meadow that macros were the same as
functions. Sly the fox, stepping deliberately, drew the form
`(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))` on a wooden board. "The difference," they
said, "is in a macro that emits the same addition form. Submit the form and let the runtime
tell us exactly what it does."

Write a form whose evaluation gives the result the macro yields after expansion + eval.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))"}}]}
```

### G10-08 record 8 — form `(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))` → `7`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

A wooden sign nailed to an orchard gate in the forest carried a puzzle.
The riddle was simple: it asked the reader to evaluate `(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))`.
Renard laughed, swaggering through the underbrush, and declared the puzzle far too
easy. Vix said patiently that the only way to be sure of
a macro that emits the same addition form was to put it in the REPL.

Question: write a Clojure expression for the result the macro yields after expansion + eval.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))"}}]}
```

### G10-08 record 9 — form `(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))` → `7`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

Sly the fox and Renard the fox stopped at the edge of the garden where
someone had chalked a macro that emits the same addition form on a wooden post. Sly,
boasting at every turn, declared the form was too high a guess to bother with.
Renard, without complaint, suggested they actually evaluate
`(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))` in the REPL and read off whatever it returned.

Write a form whose evaluation gives the result the macro yields after expansion + eval.

---

I expand the macro with macroexpand and read the produced form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))"}}]}
```

### G10-08 record 10 — form `(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))` → `7`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

A wooden sign nailed to an orchard gate by the farm carried a puzzle.
The riddle was simple: it asked the reader to evaluate `(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))`.
Renard laughed, as if the race were already won, and declared the puzzle far too
easy. Sly said patiently that the only way to be sure of
a macro that emits the same addition form was to put it in the REPL.

Write a form whose evaluation gives the result the macro yields after expansion + eval.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))"}}]}
```

## G10-09: Hygiene and gensym

### G10-09 record 1 — form `(symbol? (gensym))` → `True`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour. All this took place in the forest.

"There is no need to evaluate that," Renard the fox said,
as if the race were already won. "The cluster is too high anyway, and the predicate (symbol? (gensym)) is
clearly not worth the effort." Vix the fox, who at the edge of the forest had
grown used to such excuses, asked him to actually
write the form `(symbol? (gensym))` and submit it to the REPL — just to
be sure.

Write a form whose evaluation gives whether (gensym) returns a symbol.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? (gensym))"}}]}
```

### G10-09 record 2 — form `(symbol? (gensym))` → `True`

```
A hungry Fox came upon a vine of grapes hanging just out of reach. This was near the garden.

"A macro is just a function that runs at compile time," Sly
explained by the garden, saying very little. Vix, with great whoops of laughter, said
she could already see what the predicate (symbol? (gensym)) meant.
Sly the fox insisted they actually evaluate `(symbol? (gensym))`
and read what the runtime reported, expansion or value.

What Clojure form computes whether (gensym) returns a symbol? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? (gensym))"}}]}
```

### G10-09 record 3 — form `(symbol? (gensym))` → `True`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

A small audience of orchard creatures had gathered at the edge of the meadow to watch
Renard the fox attempt to outwit Vix the fox at reading
the REPL. Vix pointed to the predicate (symbol? (gensym)) and read the
form aloud: `(symbol? (gensym))`. The crowd waited to see who would
correctly write the form to submit.

What Clojure form computes whether (gensym) returns a symbol? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? (gensym))"}}]}
```

### G10-09 record 4 — form `(symbol? (gensym))` → `True`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Vix the fox and Renard the fox stopped by the woods where
someone had chalked the predicate (symbol? (gensym)) on a wooden post. Vix,
as if the race were already won, declared the form was too high a guess to bother with.
Renard, without complaint, suggested they actually evaluate
`(symbol? (gensym))` in the REPL and read off whatever it returned.

Question: write a Clojure expression for whether (gensym) returns a symbol.

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? (gensym))"}}]}
```

### G10-09 record 5 — form `(symbol? (gensym))` → `True`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

Vix the fox had been keeping a small leather notebook of
every form she had successfully evaluated. Today
by the market, the next entry was the predicate (symbol? (gensym)). Sly the fox
peered over her shoulder at the form `(symbol? (gensym))`
and asked what it would come out to.

Question: write a Clojure expression for whether (gensym) returns a symbol.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? (gensym))"}}]}
```

### G10-09 record 6 — form `(let [a (gensym "x_") b (gensym "x_")] (= a b))` → `False`

```
A hungry Fox came upon a vine of grapes hanging just out of reach.

A small notebook lay open at the edge of the woods where Vix had been
studying syntax-quote. The page showed two distinct gensyms with the same prefix, with the
form `(let [a (gensym "x_") b (gensym "x_")] (= a b))` circled in pencil. Sly the fox, weary from the morning's effort
of the lecture, agreed to write the form to settle once and for all
what it produced.

What Clojure form computes whether two fresh gensyms are equal (they aren't)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a (gensym \"x_\") b (gensym \"x_\")] (= a b))"}}]}
```

### G10-09 record 7 — form `(let [a (gensym "x_") b (gensym "x_")] (= a b))` → `False`

```
Hunger sharpens the eye but does not always lengthen the leap. It happened at the edge of the farm.

Renard the fox had been trying to teach Vix the fox how
the REPL works. "Look here," he said, pointing to
two distinct gensyms with the same prefix. "You hand the form `(let [a (gensym "x_") b (gensym "x_")] (= a b))` to the runtime,
and the runtime hands you back what it evaluates to." Vix
agreed, this once, to try.

Write a form whose evaluation gives whether two fresh gensyms are equal (they aren't).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a (gensym \"x_\") b (gensym \"x_\")] (= a b))"}}]}
```

### G10-09 record 8 — form `(let [a (gensym "x_") b (gensym "x_")] (= a b))` → `False`

```
A hungry Fox came upon a vine of grapes hanging just out of reach. It happened by the market.

A small audience of orchard creatures had gathered at the edge of the market to watch
Vix the fox attempt to outwit Renard the fox at reading
the REPL. Renard pointed to two distinct gensyms with the same prefix and read the
form aloud: `(let [a (gensym "x_") b (gensym "x_")] (= a b))`. The crowd waited to see who would
correctly write the form to submit.

Write a Clojure expression that computes whether two fresh gensyms are equal (they aren't).

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a (gensym \"x_\") b (gensym \"x_\")] (= a b))"}}]}
```

### G10-09 record 9 — form `(let [a (gensym "x_") b (gensym "x_")] (= a b))` → `False`

```
A hungry Fox came upon a vine of grapes hanging just out of reach. This was by the farm.

The fence by the farm was lined with old macro definitions someone had
chalked into the wood. Sly the fox found one shaped like
two distinct gensyms with the same prefix and dared Renard the fox to predict its
expansion. Renard only smiled and asked them to
write `(let [a (gensym "x_") b (gensym "x_")] (= a b))` into the REPL — that, after all, was the whole
point of having a macroexpander.

Write a form whose evaluation gives whether two fresh gensyms are equal (they aren't).

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a (gensym \"x_\") b (gensym \"x_\")] (= a b))"}}]}
```

### G10-09 record 10 — form `(let [a (gensym "x_") b (gensym "x_")] (= a b))` → `False`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

A wooden sign nailed to an orchard gate at the edge of the market carried a puzzle.
The riddle was simple: it asked the reader to evaluate `(let [a (gensym "x_") b (gensym "x_")] (= a b))`.
Renard laughed, boasting at every turn, and declared the puzzle far too
easy. Vix said patiently that the only way to be sure of
two distinct gensyms with the same prefix was to put it in the REPL.

What Clojure form computes whether two fresh gensyms are equal (they aren't)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a (gensym \"x_\") b (gensym \"x_\")] (= a b))"}}]}
```

## G10-10: Anaphoric macros are confusing

### G10-10 record 1 — form `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))` → `10`

```
Hunger sharpens the eye but does not always lengthen the leap.

Sly the fox and Vix the fox stopped near the woods where
someone had chalked a hygienic if-let style macro avoiding anaphoric injection on a wooden post. Sly,
boasting at every turn, declared the form was too high a guess to bother with.
Vix, with steady, careful steps, suggested they actually evaluate
`(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))` in the REPL and read off whatever it returned.

What Clojure form computes what the hygienic if-let macro returns? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))"}}]}
```

### G10-10 record 2 — form `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))` → `10`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

Sly the fox and Renard the fox stopped in the orchard where
someone had chalked a hygienic if-let style macro avoiding anaphoric injection on a wooden post. Sly,
as if the race were already won, declared the form was too high a guess to bother with.
Renard, saying very little, suggested they actually evaluate
`(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))` in the REPL and read off whatever it returned.

Question: write a Clojure expression for what the hygienic if-let macro returns.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))"}}]}
```

### G10-10 record 3 — form `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))` → `10`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

A small notebook lay open near the orchard where Vix had been
studying syntax-quote. The page showed a hygienic if-let style macro avoiding anaphoric injection, with the
form `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))` circled in pencil. Renard the fox, drowsy from the warm sun
of the lecture, agreed to write the form to settle once and for all
what it produced.

Write a form whose evaluation gives what the hygienic if-let macro returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))"}}]}
```

### G10-10 record 4 — form `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))` → `10`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

A small notebook lay open by the meadow where Sly had been
studying syntax-quote. The page showed a hygienic if-let style macro avoiding anaphoric injection, with the
form `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))` circled in pencil. Vix the fox, yawning at the soft moss
of the lecture, agreed to write the form to settle once and for all
what it produced.

Write a form whose evaluation gives what the hygienic if-let macro returns.

---

I let the REPL settle what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))"}}]}
```

### G10-10 record 5 — form `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))` → `10`

```
Hunger sharpens the eye but does not always lengthen the leap.

Halfway across a kitchen garden, Sly the fox stopped near the forest
and refused to evaluate the form `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))` at all — the answer,
Sly insisted, was probably sour anyway. Vix the fox,
padding up at a steady pace, simply said: "Submit a hygienic if-let style macro avoiding anaphoric injection to
the REPL. Whatever comes back is the honest answer."

What Clojure form computes what the hygienic if-let macro returns? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))"}}]}
```

### G10-10 record 6 — form `(if-let [x 7] (* x x) 0)` → `49`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

Sly the fox insisted in the farm that macros were the same as
functions. Renard the fox, untroubled by what others thought, drew the form
`(if-let [x 7] (* x x) 0)` on a wooden board. "The difference," he
said, "is in the built-in if-let, which binds explicitly (not anaphorically). Submit the form and let the runtime
tell us exactly what it does."

Write a Clojure expression that computes what (if-let [x 7] (* x x) 0) returns.

---

I submit the syntax-quoted or quoted form to the REPL.

{"tool_calls":[{"name":"eval","args":{"form":"(if-let [x 7] (* x x) 0)"}}]}
```

### G10-10 record 7 — form `(if-let [x 7] (* x x) 0)` → `49`

```
A hungry Fox came upon a vine of grapes hanging just out of reach. This was at the edge of the orchard.

Sly the fox chalked a wager on a flat board by the orchard: whoever
predicted the result of `(if-let [x 7] (* x x) 0)` would set the next ration of
fruit. Renard the fox, untroubled by what others thought, said it would be simpler
to type the form into the REPL than to bicker over the built-in if-let, which binds explicitly (not anaphorically).

Question: write a Clojure expression for what (if-let [x 7] (* x x) 0) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(if-let [x 7] (* x x) 0)"}}]}
```

### G10-10 record 8 — form `(if-let [x 7] (* x x) 0)` → `49`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes. This was near the farm.

Renard the fox had been trying to teach Vix the fox how
the REPL works. "Look here," he said, pointing to
the built-in if-let, which binds explicitly (not anaphorically). "You hand the form `(if-let [x 7] (* x x) 0)` to the runtime,
and the runtime hands you back what it evaluates to." Vix
agreed, this once, to try.

Write a Clojure expression that computes what (if-let [x 7] (* x x) 0) returns.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(if-let [x 7] (* x x) 0)"}}]}
```

### G10-10 record 9 — form `(if-let [x 7] (* x x) 0)` → `49`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Renard the fox had been trying to teach Vix the fox how
the REPL works. "Look here," he said, pointing to
the built-in if-let, which binds explicitly (not anaphorically). "You hand the form `(if-let [x 7] (* x x) 0)` to the runtime,
and the runtime hands you back what it evaluates to." Vix
agreed, this once, to try.

Write a Clojure expression that computes what (if-let [x 7] (* x x) 0) returns.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(if-let [x 7] (* x x) 0)"}}]}
```

### G10-10 record 10 — form `(if-let [x 7] (* x x) 0)` → `49`

```
Hunger sharpens the eye but does not always lengthen the leap.

"A macro is just a function that runs at compile time," Renard
explained near the market, without complaint. Sly, puffed up with pride, said
they could already see what the built-in if-let, which binds explicitly (not anaphorically) meant.
Renard the fox insisted they actually evaluate `(if-let [x 7] (* x x) 0)`
and read what the runtime reported, expansion or value.

Question: write a Clojure expression for what (if-let [x 7] (* x x) 0) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(if-let [x 7] (* x x) 0)"}}]}
```

## G10-11: Reader macros overview

### G10-11 record 1 — form `'(1 2 3)` → `[1, 2, 3]`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour. It happened in the meadow.

A wooden sign nailed to an orchard gate in the meadow carried a puzzle.
The riddle was simple: it asked the reader to evaluate `'(1 2 3)`.
Renard laughed, boasting at every turn, and declared the puzzle far too
easy. Vix said patiently that the only way to be sure of
the quote reader macro 'foo was to put it in the REPL.

Write a Clojure expression that computes what '(1 2 3) reads as.

---

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### G10-11 record 2 — form `'(1 2 3)` → `[1, 2, 3]`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Renard the fox had been trying to teach Vix the fox how
the REPL works. "Look here," he said, pointing to
the quote reader macro 'foo. "You hand the form `'(1 2 3)` to the runtime,
and the runtime hands you back what it evaluates to." Vix
agreed, this once, to try.

Write a Clojure expression that computes what '(1 2 3) reads as.

---

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### G10-11 record 3 — form `'(1 2 3)` → `[1, 2, 3]`

```
Hunger sharpens the eye but does not always lengthen the leap.

A wooden sign nailed to an orchard gate near the orchard carried a puzzle.
The riddle was simple: it asked the reader to evaluate `'(1 2 3)`.
Vix laughed, swaggering through the underbrush, and declared the puzzle far too
easy. Renard said patiently that the only way to be sure of
the quote reader macro 'foo was to put it in the REPL.

Question: write a Clojure expression for what '(1 2 3) reads as.

---

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### G10-11 record 4 — form `'(1 2 3)` → `[1, 2, 3]`

```
Hunger sharpens the eye but does not always lengthen the leap. It happened near the woods.

Sly the fox had been keeping a small leather notebook of
every form they had successfully evaluated. Today
in the woods, the next entry was the quote reader macro 'foo. Vix the fox
peered over their shoulder at the form `'(1 2 3)`
and asked what it would come out to.

What Clojure form computes what '(1 2 3) reads as? Submit it via `eval`.

---

I submit the syntax-quoted or quoted form to the REPL.

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### G10-11 record 5 — form `'(1 2 3)` → `[1, 2, 3]`

```
Hunger sharpens the eye but does not always lengthen the leap. This was near the garden.

Renard the fox and Vix the fox stopped near the garden where
someone had chalked the quote reader macro 'foo on a wooden post. Renard,
boasting at every turn, declared the form was too high a guess to bother with.
Vix, stepping deliberately, suggested they actually evaluate
`'(1 2 3)` in the REPL and read off whatever it returned.

Question: write a Clojure expression for what '(1 2 3) reads as.

---

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### G10-11 record 6 — form `(#(* % %) 6)` → `36`

```
Hunger sharpens the eye but does not always lengthen the leap. It happened at the edge of the forest.

"There is no need to evaluate that," Renard the fox said,
with great whoops of laughter. "The cluster is too high anyway, and the #(...) reader macro for an anonymous fn is
clearly not worth the effort." Sly the fox, who in the forest had
grown used to such excuses, asked him to actually
write the form `(#(* % %) 6)` and submit it to the REPL — just to
be sure.

Write a form whose evaluation gives what (#(* % %) 6) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(#(* % %) 6)"}}]}
```

### G10-11 record 7 — form `(#(* % %) 6)` → `36`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

Renard the fox insisted at the edge of the forest that macros were the same as
functions. Sly the fox, without complaint, drew the form
`(#(* % %) 6)` on a wooden board. "The difference," they
said, "is in the #(...) reader macro for an anonymous fn. Submit the form and let the runtime
tell us exactly what it does."

What Clojure form computes what (#(* % %) 6) returns? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(#(* % %) 6)"}}]}
```

### G10-11 record 8 — form `(#(* % %) 6)` → `36`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes. This was at the edge of the forest.

With a twig, Renard the fox marked out a wager at the edge of the forest: whoever
guessed the result of `(#(* % %) 6)` first would win the right to
choose the next vine to inspect. Sly the fox, her eyes always on the path,
said it was easier to ask the REPL about the #(...) reader macro for an anonymous fn than to
argue.

Write a form whose evaluation gives what (#(* % %) 6) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(#(* % %) 6)"}}]}
```

### G10-11 record 9 — form `(#(* % %) 6)` → `36`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

A small audience of orchard creatures had gathered at the edge of the orchard to watch
Renard the fox attempt to outwit Vix the fox at reading
the REPL. Vix pointed to the #(...) reader macro for an anonymous fn and read the
form aloud: `(#(* % %) 6)`. The crowd waited to see who would
correctly write the form to submit.

Question: write a Clojure expression for what (#(* % %) 6) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(#(* % %) 6)"}}]}
```

### G10-11 record 10 — form `(#(* % %) 6)` → `36`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Renard the fox had been trying to teach Vix the fox how
the REPL works. "Look here," he said, pointing to
the #(...) reader macro for an anonymous fn. "You hand the form `(#(* % %) 6)` to the runtime,
and the runtime hands you back what it evaluates to." Vix
agreed, this once, to try.

What Clojure form computes what (#(* % %) 6) returns? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(#(* % %) 6)"}}]}
```

### G10-11 record 11 — form `[1 #_ 2 3]` → `[1, 3]`

```
Hunger sharpens the eye but does not always lengthen the leap.

Renard the fox and Sly the fox stopped in the woods where
someone had chalked the #_ form-skip reader macro on a wooden post. Renard,
with great whoops of laughter, declared the form was too high a guess to bother with.
Sly, without complaint, suggested they actually evaluate
`[1 #_ 2 3]` in the REPL and read off whatever it returned.

Question: write a Clojure expression for what [1 #_ 2 3] reads as (the 2 is dropped).

---

{"tool_calls":[{"name":"eval","args":{"form":"[1 #_ 2 3]"}}]}
```

### G10-11 record 12 — form `[1 #_ 2 3]` → `[1, 3]`

```
Hunger sharpens the eye but does not always lengthen the leap.

Sly the fox chalked a wager on a flat board by the orchard: whoever
predicted the result of `[1 #_ 2 3]` would set the next ration of
fruit. Renard the fox, saying very little, said it would be simpler
to type the form into the REPL than to bicker over the #_ form-skip reader macro.

Question: write a Clojure expression for what [1 #_ 2 3] reads as (the 2 is dropped).

---

{"tool_calls":[{"name":"eval","args":{"form":"[1 #_ 2 3]"}}]}
```

### G10-11 record 13 — form `[1 #_ 2 3]` → `[1, 3]`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

The fence in the meadow was lined with old macro definitions someone had
chalked into the wood. Sly the fox found one shaped like
the #_ form-skip reader macro and dared Renard the fox to predict its
expansion. Renard only smiled and asked them to
write `[1 #_ 2 3]` into the REPL — that, after all, was the whole
point of having a macroexpander.

Write a Clojure expression that computes what [1 #_ 2 3] reads as (the 2 is dropped).

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"[1 #_ 2 3]"}}]}
```

### G10-11 record 14 — form `[1 #_ 2 3]` → `[1, 3]`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

A wooden sign nailed to an orchard gate near the forest carried a puzzle.
The riddle was simple: it asked the reader to evaluate `[1 #_ 2 3]`.
Sly laughed, boasting at every turn, and declared the puzzle far too
easy. Renard said patiently that the only way to be sure of
the #_ form-skip reader macro was to put it in the REPL.

Question: write a Clojure expression for what [1 #_ 2 3] reads as (the 2 is dropped).

---

{"tool_calls":[{"name":"eval","args":{"form":"[1 #_ 2 3]"}}]}
```

### G10-11 record 15 — form `[1 #_ 2 3]` → `[1, 3]`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour. This was by the forest.

A small audience of orchard creatures had gathered at the edge of the forest to watch
Sly the fox attempt to outwit Renard the fox at reading
the REPL. Renard pointed to the #_ form-skip reader macro and read the
form aloud: `[1 #_ 2 3]`. The crowd waited to see who would
correctly write the form to submit.

What Clojure form computes what [1 #_ 2 3] reads as (the 2 is dropped)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"[1 #_ 2 3]"}}]}
```

## G10-12: Tagged literals

### G10-12 record 1 — form `(inst? #inst "2024-01-01")` → `True`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

Vix the fox chalked a wager on a flat board near the market: whoever
predicted the result of `(inst? #inst "2024-01-01")` would set the next ration of
fruit. Sly the fox, stepping deliberately, said it would be simpler
to type the form into the REPL than to bicker over the predicate (inst? #inst "2024-01-01").

Question: write a Clojure expression for whether the #inst tagged literal reads to an inst.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(inst? #inst \"2024-01-01\")"}}]}
```

### G10-12 record 2 — form `(inst? #inst "2024-01-01")` → `True`

```
Hunger sharpens the eye but does not always lengthen the leap.

"There is no need to evaluate that," Renard the fox said,
with a smug grin. "The cluster is too high anyway, and the predicate (inst? #inst "2024-01-01") is
clearly not worth the effort." Vix the fox, who by the meadow had
grown used to such excuses, asked him to actually
write the form `(inst? #inst "2024-01-01")` and submit it to the REPL — just to
be sure.

Write a Clojure expression that computes whether the #inst tagged literal reads to an inst.

---

{"tool_calls":[{"name":"eval","args":{"form":"(inst? #inst \"2024-01-01\")"}}]}
```

### G10-12 record 3 — form `(inst? #inst "2024-01-01")` → `True`

```
Hunger sharpens the eye but does not always lengthen the leap.

Vix the fox had been trying to teach Renard the fox how
the REPL works. "Look here," she said, pointing to
the predicate (inst? #inst "2024-01-01"). "You hand the form `(inst? #inst "2024-01-01")` to the runtime,
and the runtime hands you back what it evaluates to." Renard
agreed, this once, to try.

Write a form whose evaluation gives whether the #inst tagged literal reads to an inst.

---

I write the form and let the macroexpander or REPL show the result.

{"tool_calls":[{"name":"eval","args":{"form":"(inst? #inst \"2024-01-01\")"}}]}
```

### G10-12 record 4 — form `(inst? #inst "2024-01-01")` → `True`

```
A hungry Fox came upon a vine of grapes hanging just out of reach.

A wooden sign nailed to an orchard gate in the garden carried a puzzle.
The riddle was simple: it asked the reader to evaluate `(inst? #inst "2024-01-01")`.
Vix laughed, swaggering through the underbrush, and declared the puzzle far too
easy. Renard said patiently that the only way to be sure of
the predicate (inst? #inst "2024-01-01") was to put it in the REPL.

Question: write a Clojure expression for whether the #inst tagged literal reads to an inst.

---

{"tool_calls":[{"name":"eval","args":{"form":"(inst? #inst \"2024-01-01\")"}}]}
```

### G10-12 record 5 — form `(inst? #inst "2024-01-01")` → `True`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes. It happened by the farm.

Sly the fox insisted at the edge of the farm that macros were the same as
functions. Renard the fox, her eyes always on the path, drew the form
`(inst? #inst "2024-01-01")` on a wooden board. "The difference," he
said, "is in the predicate (inst? #inst "2024-01-01"). Submit the form and let the runtime
tell us exactly what it does."

What Clojure form computes whether the #inst tagged literal reads to an inst? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(inst? #inst \"2024-01-01\")"}}]}
```

### G10-12 record 6 — form `(uuid? #uuid "00000000-0000-0000-0000-000000000000")` → `True`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

A small notebook lay open in the meadow where Sly had been
studying syntax-quote. The page showed the predicate on a #uuid tagged literal, with the
form `(uuid? #uuid "00000000-0000-0000-0000-000000000000")` circled in pencil. Vix the fox, drowsy from the warm sun
of the lecture, agreed to write the form to settle once and for all
what it produced.

Question: write a Clojure expression for whether the #uuid tagged literal reads to a uuid.

---

I write the form and let the macroexpander or REPL show the result.

{"tool_calls":[{"name":"eval","args":{"form":"(uuid? #uuid \"00000000-0000-0000-0000-000000000000\")"}}]}
```

### G10-12 record 7 — form `(uuid? #uuid "00000000-0000-0000-0000-000000000000")` → `True`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

Vix the fox chalked a wager on a flat board in the orchard: whoever
predicted the result of `(uuid? #uuid "00000000-0000-0000-0000-000000000000")` would set the next ration of
fruit. Renard the fox, with steady, careful steps, said it would be simpler
to type the form into the REPL than to bicker over the predicate on a #uuid tagged literal.

What Clojure form computes whether the #uuid tagged literal reads to a uuid? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(uuid? #uuid \"00000000-0000-0000-0000-000000000000\")"}}]}
```

### G10-12 record 8 — form `(uuid? #uuid "00000000-0000-0000-0000-000000000000")` → `True`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

Halfway across a kitchen garden, Vix the fox stopped in the woods
and refused to evaluate the form `(uuid? #uuid "00000000-0000-0000-0000-000000000000")` at all — the answer,
Vix insisted, was probably sour anyway. Renard the fox,
padding up at a steady pace, simply said: "Submit the predicate on a #uuid tagged literal to
the REPL. Whatever comes back is the honest answer."

Write a form whose evaluation gives whether the #uuid tagged literal reads to a uuid.

---

I submit the syntax-quoted or quoted form to the REPL.

{"tool_calls":[{"name":"eval","args":{"form":"(uuid? #uuid \"00000000-0000-0000-0000-000000000000\")"}}]}
```

### G10-12 record 9 — form `(uuid? #uuid "00000000-0000-0000-0000-000000000000")` → `True`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes. It happened by the garden.

Renard the fox sketched a small wager into the dirt in the garden:
whoever guessed the result of `(uuid? #uuid "00000000-0000-0000-0000-000000000000")` first would claim the
next cluster of grapes. Vix the fox, with steady, careful steps, said it
was simpler to type the form into the REPL than to argue about
the predicate on a #uuid tagged literal.

What Clojure form computes whether the #uuid tagged literal reads to a uuid? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(uuid? #uuid \"00000000-0000-0000-0000-000000000000\")"}}]}
```

### G10-12 record 10 — form `(uuid? #uuid "00000000-0000-0000-0000-000000000000")` → `True`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour. This was near the meadow.

With a twig, Sly the fox marked out a wager at the edge of the meadow: whoever
guessed the result of `(uuid? #uuid "00000000-0000-0000-0000-000000000000")` first would win the right to
choose the next vine to inspect. Renard the fox, with steady, careful steps,
said it was easier to ask the REPL about the predicate on a #uuid tagged literal than to
argue.

Question: write a Clojure expression for whether the #uuid tagged literal reads to a uuid.

---

{"tool_calls":[{"name":"eval","args":{"form":"(uuid? #uuid \"00000000-0000-0000-0000-000000000000\")"}}]}
```

## G10-13: Data readers and EDN extension

### G10-13 record 1 — form `(clojure.edn/read-string "42")` → `42`

```
A hungry Fox came upon a vine of grapes hanging just out of reach.

Vix the fox insisted at the edge of the orchard that macros were the same as
functions. Renard the fox, untroubled by what others thought, drew the form
`(clojure.edn/read-string "42")` on a wooden board. "The difference," he
said, "is in edn read-string of "42". Submit the form and let the runtime
tell us exactly what it does."

Write a Clojure expression that computes what edn/read-string returns for the source "42".

---

I submit the syntax-quoted or quoted form to the REPL.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"42\")"}}]}
```

### G10-13 record 2 — form `(clojure.edn/read-string "42")` → `42`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour. All this took place at the edge of the garden.

Renard the fox and Vix the fox stopped near the garden where
someone had chalked edn read-string of "42" on a wooden post. Renard,
boasting at every turn, declared the form was too high a guess to bother with.
Vix, saying very little, suggested they actually evaluate
`(clojure.edn/read-string "42")` in the REPL and read off whatever it returned.

Write a Clojure expression that computes what edn/read-string returns for the source "42".

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"42\")"}}]}
```

### G10-13 record 3 — form `(clojure.edn/read-string "42")` → `42`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

With a twig, Vix the fox marked out a wager near the market: whoever
guessed the result of `(clojure.edn/read-string "42")` first would win the right to
choose the next vine to inspect. Sly the fox, stepping deliberately,
said it was easier to ask the REPL about edn read-string of "42" than to
argue.

Write a Clojure expression that computes what edn/read-string returns for the source "42".

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"42\")"}}]}
```

### G10-13 record 4 — form `(clojure.edn/read-string "42")` → `42`

```
Hunger sharpens the eye but does not always lengthen the leap. All this took place in the orchard.

"A macro is just a function that runs at compile time," Sly
explained near the orchard, her eyes always on the path. Vix, puffed up with pride, said
she could already see what edn read-string of "42" meant.
Sly the fox insisted they actually evaluate `(clojure.edn/read-string "42")`
and read what the runtime reported, expansion or value.

Question: write a Clojure expression for what edn/read-string returns for the source "42".

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"42\")"}}]}
```

### G10-13 record 5 — form `(clojure.edn/read-string "42")` → `42`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Renard the fox sketched a small wager into the dirt in the orchard:
whoever guessed the result of `(clojure.edn/read-string "42")` first would claim the
next cluster of grapes. Sly the fox, untroubled by what others thought, said it
was simpler to type the form into the REPL than to argue about
edn read-string of "42".

What Clojure form computes what edn/read-string returns for the source "42"? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"42\")"}}]}
```

### G10-13 record 6 — form `(clojure.edn/read-string "[:a :b :c]")` → `[':a', ':b', ':c']`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Sly the fox sketched a small wager into the dirt in the woods:
whoever guessed the result of `(clojure.edn/read-string "[:a :b :c]")` first would claim the
next cluster of grapes. Vix the fox, her eyes always on the path, said it
was simpler to type the form into the REPL than to argue about
edn read-string of a vector source.

Write a Clojure expression that computes what edn/read-string returns for "[:a :b :c]".

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"[:a :b :c]\")"}}]}
```

### G10-13 record 7 — form `(clojure.edn/read-string "[:a :b :c]")` → `[':a', ':b', ':c']`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

A small audience of orchard creatures had gathered at the edge of the garden to watch
Renard the fox attempt to outwit Sly the fox at reading
the REPL. Sly pointed to edn read-string of a vector source and read the
form aloud: `(clojure.edn/read-string "[:a :b :c]")`. The crowd waited to see who would
correctly write the form to submit.

Write a Clojure expression that computes what edn/read-string returns for "[:a :b :c]".

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"[:a :b :c]\")"}}]}
```

### G10-13 record 8 — form `(clojure.edn/read-string "[:a :b :c]")` → `[':a', ':b', ':c']`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

"A macro is just a function that runs at compile time," Sly
explained by the meadow, her eyes always on the path. Renard, boasting at every turn, said
he could already see what edn read-string of a vector source meant.
Sly the fox insisted they actually evaluate `(clojure.edn/read-string "[:a :b :c]")`
and read what the runtime reported, expansion or value.

Write a Clojure expression that computes what edn/read-string returns for "[:a :b :c]".

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"[:a :b :c]\")"}}]}
```

### G10-13 record 9 — form `(clojure.edn/read-string "[:a :b :c]")` → `[':a', ':b', ':c']`

```
Hunger sharpens the eye but does not always lengthen the leap.

Sly the fox had spent the morning at the edge of the meadow sketching a tiny
language of their own — a notebook of macros that
wrote other forms. The next entry was edn read-string of a vector source, and the form
`(clojure.edn/read-string "[:a :b :c]")` was what Sly wanted Vix the fox to
submit so the REPL could show what code it produced or what value it
returned.

What Clojure form computes what edn/read-string returns for "[:a :b :c]"? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"[:a :b :c]\")"}}]}
```

### G10-13 record 10 — form `(clojure.edn/read-string "[:a :b :c]")` → `[':a', ':b', ':c']`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

At a stone tablet by the orchard, Vix the fox was teaching
Sly the fox the discipline of expansion: never trust your eyes,
only the macroexpander. The day's example was edn read-string of a vector source. The
form `(clojure.edn/read-string "[:a :b :c]")` had to be submitted; nothing else would do.

Write a Clojure expression that computes what edn/read-string returns for "[:a :b :c]".

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"[:a :b :c]\")"}}]}
```

## G10-14: eval (the function)

### G10-14 record 1 — form `(eval '(+ 1 2 3))` → `6`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

A small audience of orchard creatures had gathered at the edge of the forest to watch
Vix the fox attempt to outwit Sly the fox at reading
the REPL. Sly pointed to the form (eval '(+ 1 2 3)) and read the
form aloud: `(eval '(+ 1 2 3))`. The crowd waited to see who would
correctly write the form to submit.

Write a Clojure expression that computes what eval returns for the quoted (+ 1 2 3).

---

{"tool_calls":[{"name":"eval","args":{"form":"(eval '(+ 1 2 3))"}}]}
```

### G10-14 record 2 — form `(eval '(+ 1 2 3))` → `6`

```
A hungry Fox came upon a vine of grapes hanging just out of reach. All this took place near the meadow.

A small notebook lay open near the meadow where Vix had been
studying syntax-quote. The page showed the form (eval '(+ 1 2 3)), with the
form `(eval '(+ 1 2 3))` circled in pencil. Sly the fox, yawning at the soft moss
of the lecture, agreed to write the form to settle once and for all
what it produced.

Write a Clojure expression that computes what eval returns for the quoted (+ 1 2 3).

---

I write the macro form and let the runtime evaluate or expand it.

{"tool_calls":[{"name":"eval","args":{"form":"(eval '(+ 1 2 3))"}}]}
```

### G10-14 record 3 — form `(eval '(+ 1 2 3))` → `6`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour. This was near the market.

Renard the fox and Sly the fox stopped by the market where
someone had chalked the form (eval '(+ 1 2 3)) on a wooden post. Renard,
with great whoops of laughter, declared the form was too high a guess to bother with.
Sly, saying very little, suggested they actually evaluate
`(eval '(+ 1 2 3))` in the REPL and read off whatever it returned.

Question: write a Clojure expression for what eval returns for the quoted (+ 1 2 3).

---

I submit the syntax-quoted or quoted form to the REPL.

{"tool_calls":[{"name":"eval","args":{"form":"(eval '(+ 1 2 3))"}}]}
```

### G10-14 record 4 — form `(eval '(+ 1 2 3))` → `6`

```
Hunger sharpens the eye but does not always lengthen the leap.

Halfway across a kitchen garden, Renard the fox stopped by the market
and refused to evaluate the form `(eval '(+ 1 2 3))` at all — the answer,
Renard insisted, was probably sour anyway. Vix the fox,
padding up at a steady pace, simply said: "Submit the form (eval '(+ 1 2 3)) to
the REPL. Whatever comes back is the honest answer."

Write a Clojure expression that computes what eval returns for the quoted (+ 1 2 3).

---

{"tool_calls":[{"name":"eval","args":{"form":"(eval '(+ 1 2 3))"}}]}
```

### G10-14 record 5 — form `(eval '(+ 1 2 3))` → `6`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

A wooden sign nailed to an orchard gate in the meadow carried a puzzle.
The riddle was simple: it asked the reader to evaluate `(eval '(+ 1 2 3))`.
Vix laughed, with a smug grin, and declared the puzzle far too
easy. Renard said patiently that the only way to be sure of
the form (eval '(+ 1 2 3)) was to put it in the REPL.

What Clojure form computes what eval returns for the quoted (+ 1 2 3)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(eval '(+ 1 2 3))"}}]}
```

### G10-14 record 6 — form `(eval (list '+ 4 5))` → `9`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour. This was at the edge of the market.

Renard the fox sketched a small wager into the dirt at the edge of the market:
whoever guessed the result of `(eval (list '+ 4 5))` first would claim the
next cluster of grapes. Vix the fox, stepping deliberately, said it
was simpler to type the form into the REPL than to argue about
eval applied to a constructed list.

Write a Clojure expression that computes what eval returns when handed (list '+ 4 5).

---

{"tool_calls":[{"name":"eval","args":{"form":"(eval (list '+ 4 5))"}}]}
```

### G10-14 record 7 — form `(eval (list '+ 4 5))` → `9`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

A wooden sign nailed to an orchard gate near the farm carried a puzzle.
The riddle was simple: it asked the reader to evaluate `(eval (list '+ 4 5))`.
Vix laughed, with great whoops of laughter, and declared the puzzle far too
easy. Renard said patiently that the only way to be sure of
eval applied to a constructed list was to put it in the REPL.

Write a Clojure expression that computes what eval returns when handed (list '+ 4 5).

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(eval (list '+ 4 5))"}}]}
```

### G10-14 record 8 — form `(eval (list '+ 4 5))` → `9`

```
A hungry Fox came upon a vine of grapes hanging just out of reach. It happened at the edge of the market.

A wooden sign nailed to an orchard gate at the edge of the market carried a puzzle.
The riddle was simple: it asked the reader to evaluate `(eval (list '+ 4 5))`.
Renard laughed, with a smug grin, and declared the puzzle far too
easy. Vix said patiently that the only way to be sure of
eval applied to a constructed list was to put it in the REPL.

Write a Clojure expression that computes what eval returns when handed (list '+ 4 5).

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(eval (list '+ 4 5))"}}]}
```

### G10-14 record 9 — form `(eval (list '+ 4 5))` → `9`

```
A hungry Fox came upon a vine of grapes hanging just out of reach.

At a stone tablet in the orchard, Renard the fox was teaching
Vix the fox the discipline of expansion: never trust your eyes,
only the macroexpander. The day's example was eval applied to a constructed list. The
form `(eval (list '+ 4 5))` had to be submitted; nothing else would do.

Write a Clojure expression that computes what eval returns when handed (list '+ 4 5).

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(eval (list '+ 4 5))"}}]}
```

### G10-14 record 10 — form `(eval (list '+ 4 5))` → `9`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour. This was by the orchard.

"There is no need to evaluate that," Sly the fox said,
as if the race were already won. "The cluster is too high anyway, and eval applied to a constructed list is
clearly not worth the effort." Renard the fox, who by the orchard had
grown used to such excuses, asked them to actually
write the form `(eval (list '+ 4 5))` and submit it to the REPL — just to
be sure.

Write a form whose evaluation gives what eval returns when handed (list '+ 4 5).

---

{"tool_calls":[{"name":"eval","args":{"form":"(eval (list '+ 4 5))"}}]}
```

## G10-15: When not to write a macro

### G10-15 record 1 — form `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))` → `7`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

Sly the fox insisted near the meadow that macros were the same as
functions. Vix the fox, without complaint, drew the form
`(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))` on a wooden board. "The difference," she
said, "is in a function call where no macro is justified. Submit the form and let the runtime
tell us exactly what it does."

Write a form whose evaluation gives what the plain function call returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"a function suffices when no syntax shaping is needed\" ((fn [x y] (+ x y)) 3 4))"}}]}
```

### G10-15 record 2 — form `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))` → `7`

```
Hunger sharpens the eye but does not always lengthen the leap.

Renard the fox chalked a wager on a flat board in the orchard: whoever
predicted the result of `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))` would set the next ration of
fruit. Vix the fox, stepping deliberately, said it would be simpler
to type the form into the REPL than to bicker over a function call where no macro is justified.

Write a Clojure expression that computes what the plain function call returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"a function suffices when no syntax shaping is needed\" ((fn [x y] (+ x y)) 3 4))"}}]}
```

### G10-15 record 3 — form `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))` → `7`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour. All this took place at the edge of the forest.

Renard the fox sketched a small wager into the dirt near the forest:
whoever guessed the result of `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))` first would claim the
next cluster of grapes. Vix the fox, stepping deliberately, said it
was simpler to type the form into the REPL than to argue about
a function call where no macro is justified.

Write a form whose evaluation gives what the plain function call returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"a function suffices when no syntax shaping is needed\" ((fn [x y] (+ x y)) 3 4))"}}]}
```

### G10-15 record 4 — form `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))` → `7`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour. All this took place at the edge of the farm.

Vix the fox had been keeping a small leather notebook of
every form she had successfully evaluated. Today
at the edge of the farm, the next entry was a function call where no macro is justified. Sly the fox
peered over her shoulder at the form `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))`
and asked what it would come out to.

Write a Clojure expression that computes what the plain function call returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"a function suffices when no syntax shaping is needed\" ((fn [x y] (+ x y)) 3 4))"}}]}
```

### G10-15 record 5 — form `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))` → `7`

```
A hungry Fox came upon a vine of grapes hanging just out of reach.

A small audience of orchard creatures had gathered at the edge of the meadow to watch
Sly the fox attempt to outwit Renard the fox at reading
the REPL. Renard pointed to a function call where no macro is justified and read the
form aloud: `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))`. The crowd waited to see who would
correctly write the form to submit.

Question: write a Clojure expression for what the plain function call returns.

---

I submit the syntax-quoted or quoted form to the REPL.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"a function suffices when no syntax shaping is needed\" ((fn [x y] (+ x y)) 3 4))"}}]}
```

### G10-15 record 6 — form `(do "prefer fn unless you must shape syntax" (map inc [1 2 3]))` → `[2, 3, 4]`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour. It happened in the farm.

Renard the fox insisted at the edge of the farm that macros were the same as
functions. Sly the fox, with steady, careful steps, drew the form
`(do "prefer fn unless you must shape syntax" (map inc [1 2 3]))` on a wooden board. "The difference," they
said, "is in map applied to inc — no macro needed. Submit the form and let the runtime
tell us exactly what it does."

Write a form whose evaluation gives the result of mapping inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"prefer fn unless you must shape syntax\" (map inc [1 2 3]))"}}]}
```

### G10-15 record 7 — form `(do "prefer fn unless you must shape syntax" (map inc [1 2 3]))` → `[2, 3, 4]`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

With a twig, Vix the fox marked out a wager at the edge of the market: whoever
guessed the result of `(do "prefer fn unless you must shape syntax" (map inc [1 2 3]))` first would win the right to
choose the next vine to inspect. Sly the fox, stepping deliberately,
said it was easier to ask the REPL about map applied to inc — no macro needed than to
argue.

Question: write a Clojure expression for the result of mapping inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"prefer fn unless you must shape syntax\" (map inc [1 2 3]))"}}]}
```

### G10-15 record 8 — form `(do "prefer fn unless you must shape syntax" (map inc [1 2 3]))` → `[2, 3, 4]`

```
Hunger sharpens the eye but does not always lengthen the leap. It happened at the edge of the woods.

A wooden sign nailed to an orchard gate by the woods carried a puzzle.
The riddle was simple: it asked the reader to evaluate `(do "prefer fn unless you must shape syntax" (map inc [1 2 3]))`.
Sly laughed, boasting at every turn, and declared the puzzle far too
easy. Vix said patiently that the only way to be sure of
map applied to inc — no macro needed was to put it in the REPL.

What Clojure form computes the result of mapping inc? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"prefer fn unless you must shape syntax\" (map inc [1 2 3]))"}}]}
```

### G10-15 record 9 — form `(do "prefer fn unless you must shape syntax" (map inc [1 2 3]))` → `[2, 3, 4]`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

A small audience of orchard creatures had gathered near the forest to watch
Renard the fox attempt to outwit Sly the fox at reading
the REPL. Sly pointed to map applied to inc — no macro needed and read the
form aloud: `(do "prefer fn unless you must shape syntax" (map inc [1 2 3]))`. The crowd waited to see who would
correctly write the form to submit.

Write a Clojure expression that computes the result of mapping inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"prefer fn unless you must shape syntax\" (map inc [1 2 3]))"}}]}
```

### G10-15 record 10 — form `(do "prefer fn unless you must shape syntax" (map inc [1 2 3]))` → `[2, 3, 4]`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes. This was by the forest.

Vix the fox sketched a small wager into the dirt by the forest:
whoever guessed the result of `(do "prefer fn unless you must shape syntax" (map inc [1 2 3]))` first would claim the
next cluster of grapes. Sly the fox, stepping deliberately, said it
was simpler to type the form into the REPL than to argue about
map applied to inc — no macro needed.

Question: write a Clojure expression for the result of mapping inc.

---

I write the form and let the macroexpander or REPL show the result.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"prefer fn unless you must shape syntax\" (map inc [1 2 3]))"}}]}
```

## G10-16: Macro pattern library

### G10-16 record 1 — form `(do (defmacro with-tortoise-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-tortoise-pace 42))` → `42`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

A wooden sign nailed to an orchard gate by the meadow carried a puzzle.
The riddle was simple: it asked the reader to evaluate `(do (defmacro with-tortoise-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-tortoise-pace 42))`.
Vix laughed, as if the race were already won, and declared the puzzle far too
easy. Renard said patiently that the only way to be sure of
a with-X macro pattern that binds a local and runs body was to put it in the REPL.

What Clojure form computes what the with- macro yields? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro with-tortoise-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-tortoise-pace 42))"}}]}
```

### G10-16 record 2 — form `(do (defmacro with-tortoise-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-tortoise-pace 42))` → `42`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes. All this took place near the garden.

Halfway across a kitchen garden, Sly the fox stopped in the garden
and refused to evaluate the form `(do (defmacro with-tortoise-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-tortoise-pace 42))` at all — the answer,
Sly insisted, was probably sour anyway. Renard the fox,
padding up at a steady pace, simply said: "Submit a with-X macro pattern that binds a local and runs body to
the REPL. Whatever comes back is the honest answer."

Write a form whose evaluation gives what the with- macro yields.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro with-tortoise-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-tortoise-pace 42))"}}]}
```

### G10-16 record 3 — form `(do (defmacro with-tortoise-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-tortoise-pace 42))` → `42`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

Renard the fox had spent the morning in the farm sketching a tiny
language of his own — a notebook of macros that
wrote other forms. The next entry was a with-X macro pattern that binds a local and runs body, and the form
`(do (defmacro with-tortoise-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-tortoise-pace 42))` was what Renard wanted Sly the fox to
submit so the REPL could show what code it produced or what value it
returned.

Write a form whose evaluation gives what the with- macro yields.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro with-tortoise-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-tortoise-pace 42))"}}]}
```

### G10-16 record 4 — form `(do (defmacro with-tortoise-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-tortoise-pace 42))` → `42`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

Halfway across a kitchen garden, Sly the fox stopped near the woods
and refused to evaluate the form `(do (defmacro with-tortoise-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-tortoise-pace 42))` at all — the answer,
Sly insisted, was probably sour anyway. Vix the fox,
padding up at a steady pace, simply said: "Submit a with-X macro pattern that binds a local and runs body to
the REPL. Whatever comes back is the honest answer."

Question: write a Clojure expression for what the with- macro yields.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro with-tortoise-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-tortoise-pace 42))"}}]}
```

### G10-16 record 5 — form `(do (defmacro with-tortoise-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-tortoise-pace 42))` → `42`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

"There is no need to evaluate that," Sly the fox said,
puffed up with pride. "The cluster is too high anyway, and a with-X macro pattern that binds a local and runs body is
clearly not worth the effort." Renard the fox, who by the forest had
grown used to such excuses, asked them to actually
write the form `(do (defmacro with-tortoise-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-tortoise-pace 42))` and submit it to the REPL — just to
be sure.

Question: write a Clojure expression for what the with- macro yields.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro with-tortoise-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-tortoise-pace 42))"}}]}
```

### G10-16 record 6 — form `(do (defmacro def-pace [name v] `(def ~name ~v)) (def-pace race-pace :slow) race-pace)` → `':slow'`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour. This was near the garden.

Vix the fox had been keeping a small leather notebook of
every form she had successfully evaluated. Today
near the garden, the next entry was a def-X-thing macro that introduces a named binding. Renard the fox
peered over her shoulder at the form `(do (defmacro def-pace [name v] `(def ~name ~v)) (def-pace race-pace :slow) race-pace)`
and asked what it would come out to.

Write a form whose evaluation gives the value of the symbol the macro defined.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro def-pace [name v] `(def ~name ~v)) (def-pace race-pace :slow) race-pace)"}}]}
```

### G10-16 record 7 — form `(do (defmacro def-pace [name v] `(def ~name ~v)) (def-pace race-pace :slow) race-pace)` → `':slow'`

```
It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.

A small notebook lay open near the garden where Vix had been
studying syntax-quote. The page showed a def-X-thing macro that introduces a named binding, with the
form `(do (defmacro def-pace [name v] `(def ~name ~v)) (def-pace race-pace :slow) race-pace)` circled in pencil. Renard the fox, drowsy from the warm sun
of the lecture, agreed to write the form to settle once and for all
what it produced.

Question: write a Clojure expression for the value of the symbol the macro defined.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro def-pace [name v] `(def ~name ~v)) (def-pace race-pace :slow) race-pace)"}}]}
```

### G10-16 record 8 — form `(do (defmacro def-pace [name v] `(def ~name ~v)) (def-pace race-pace :slow) race-pace)` → `':slow'`

```
A hungry Fox came upon a vine of grapes hanging just out of reach.

A small audience of orchard creatures had gathered in the garden to watch
Vix the fox attempt to outwit Renard the fox at reading
the REPL. Renard pointed to a def-X-thing macro that introduces a named binding and read the
form aloud: `(do (defmacro def-pace [name v] `(def ~name ~v)) (def-pace race-pace :slow) race-pace)`. The crowd waited to see who would
correctly write the form to submit.

Write a form whose evaluation gives the value of the symbol the macro defined.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro def-pace [name v] `(def ~name ~v)) (def-pace race-pace :slow) race-pace)"}}]}
```

### G10-16 record 9 — form `(do (defmacro def-pace [name v] `(def ~name ~v)) (def-pace race-pace :slow) race-pace)` → `':slow'`

```
Hunger sharpens the eye but does not always lengthen the leap.

A small audience of orchard creatures had gathered near the woods to watch
Vix the fox attempt to outwit Sly the fox at reading
the REPL. Sly pointed to a def-X-thing macro that introduces a named binding and read the
form aloud: `(do (defmacro def-pace [name v] `(def ~name ~v)) (def-pace race-pace :slow) race-pace)`. The crowd waited to see who would
correctly write the form to submit.

Write a Clojure expression that computes the value of the symbol the macro defined.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro def-pace [name v] `(def ~name ~v)) (def-pace race-pace :slow) race-pace)"}}]}
```

### G10-16 record 10 — form `(do (defmacro def-pace [name v] `(def ~name ~v)) (def-pace race-pace :slow) race-pace)` → `':slow'`

```
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

"A macro is just a function that runs at compile time," Renard
explained at the edge of the farm, stepping deliberately. Sly, as if the race were already won, said
they could already see what a def-X-thing macro that introduces a named binding meant.
Renard the fox insisted they actually evaluate `(do (defmacro def-pace [name v] `(def ~name ~v)) (def-pace race-pace :slow) race-pace)`
and read what the runtime reported, expansion or value.

What Clojure form computes the value of the symbol the macro defined? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro def-pace [name v] `(def ~name ~v)) (def-pace race-pace :slow) race-pace)"}}]}
```

