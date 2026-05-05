# crow-pitcher grade 10 — deep spot-check

5 records per subject for hand-audit.

---

## G10-01: quote, unquote, unquote-splice

### G10-01 record 1  •  form `(quote (+ 1 2))`  •  expected `['+', 1, 2]`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

"There is no need to evaluate that," Caw the crow said, swaggering through the underbrush.
"Anyone with a sharp eye can see what the quoted form (quote (+ 1 2)) comes to."
Korvus the crow, who near the meadow had grown used to such claims, asked
her to actually write the form `(quote (+ 1 2))` and drop it
into the REPL — just to be sure.

Write a form whose evaluation gives the value of (quote (+ 1 2)).

---

I expand the macro with macroexpand and read the produced form.

{"tool_calls":[{"name":"eval","args":{"form":"(quote (+ 1 2))"}}]}
```

### G10-01 record 2  •  form `'(1 2 3)`  •  expected `[1, 2, 3]`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

"A macro is just a function that runs at compile time," Caw
explained at the edge of the village, saying very little. Korvus, with a smug grin, said
he could already see what the quoted list '(1 2 3) meant.
Caw the crow insisted they actually evaluate `'(1 2 3)` and
read what the runtime reported, expansion or value.

Write a form whose evaluation gives the value of '(1 2 3).

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### G10-01 record 3  •  form `(let [x 5] `(a ~x b))`  •  expected `['a', 5, 'b']`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Caw the crow etched a wager along the rim of a chipped pitcher
by the market: whoever predicted the result of `(let [x 5] `(a ~x b))` first would set
the next day's foraging route. Sable the crow, her eyes always on the path, said it
would be simpler to drop the form into the REPL than to bicker about
a syntax-quoted list with one unquote.

What Clojure form computes the result of `(a ~x b) when x is 5? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 5] `(a ~x b))"}}]}
```

### G10-01 record 4  •  form `(quote (+ 1 2))`  •  expected `['+', 1, 2]`

```
Hunger and thirst had driven the Crow far from her usual perch.

Caw the crow and Sable the crow alighted by the farm on the rim of an old
pitcher where someone had scratched the quoted form (quote (+ 1 2)). Caw,
shouting until her voice cracked, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(quote (+ 1 2))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

What Clojure form computes the value of (quote (+ 1 2))? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(quote (+ 1 2))"}}]}
```

### G10-01 record 5  •  form `'(1 2 3)`  •  expected `[1, 2, 3]`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A small notebook lay open near the farm where the clever crow had been
studying syntax-quote. The page showed the quoted list '(1 2 3), with the
form `'(1 2 3)` circled in pencil. Sable the crow, weary from the morning's effort
of the lecture, agreed to write the form to settle once and for all
what it produced.

What Clojure form computes the value of '(1 2 3)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

## G10-02: syntax-quote

### G10-02 record 1  •  form `(let [x 10] `(+ ~x ~x))`  •  expected `['+', 10, 10]`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Caw the crow and Korvus the crow alighted near the meadow on the rim of an old
pitcher where someone had scratched a syntax-quoted addition with x unquoted twice. Caw,
her hands trembling, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(let [x 10] `(+ ~x ~x))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

What Clojure form computes the form produced by `(+ ~x ~x) when x is 10? Submit it via `eval`.

---

I write the form and let the macroexpander or REPL show the result.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 10] `(+ ~x ~x))"}}]}
```

### G10-02 record 2  •  form `(let [xs [1 2 3]] `(list ~@xs))`  •  expected `['list', 1, 2, 3]`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Halfway through a long thirsty afternoon, Caw the crow alighted
in the market and refused to fly on until someone could prove what the form
`(let [xs [1 2 3]] `(list ~@xs))` evaluated to. Caw called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
a syntax-quoted list with unquote-splice into the REPL. Whatever rises is the answer."

Write a form whose evaluation gives the form produced by `(list ~@xs) when xs is [1 2 3].

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [xs [1 2 3]] `(list ~@xs))"}}]}
```

### G10-02 record 3  •  form `(let [x 10] `(+ ~x ~x))`  •  expected `['+', 10, 10]`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was near the garden.

A small audience of sparrows had gathered in the garden to watch
Caw the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to a syntax-quoted addition with x unquoted twice and read out the form
aloud: `(let [x 10] `(+ ~x ~x))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives the form produced by `(+ ~x ~x) when x is 10.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 10] `(+ ~x ~x))"}}]}
```

### G10-02 record 4  •  form `(let [xs [1 2 3]] `(list ~@xs))`  •  expected `['list', 1, 2, 3]`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust at the edge of the orchard: whoever guessed the result of `(let [xs [1 2 3]] `(list ~@xs))`
first would win the right to claim the next clear water they found.
Sable the crow, saying very little, said it was easier to ask the REPL
about a syntax-quoted list with unquote-splice than to argue.

Write a Clojure expression that computes the form produced by `(list ~@xs) when xs is [1 2 3].

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(let [xs [1 2 3]] `(list ~@xs))"}}]}
```

### G10-02 record 5  •  form `(let [x 10] `(+ ~x ~x))`  •  expected `['+', 10, 10]`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. All this took place near the farm.

Korvus the crow etched a wager along the rim of a chipped pitcher
in the farm: whoever predicted the result of `(let [x 10] `(+ ~x ~x))` first would set
the next day's foraging route. Caw the crow, saying very little, said it
would be simpler to drop the form into the REPL than to bicker about
a syntax-quoted addition with x unquoted twice.

Write a Clojure expression that computes the form produced by `(+ ~x ~x) when x is 10.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 10] `(+ ~x ~x))"}}]}
```

## G10-03: defmacro introduction

### G10-03 record 1  •  form `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`  •  expected `3`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened in the village.

Caw the crow had been keeping a small leather notebook of every form
she had successfully dropped into the REPL — one entry per
stone, one rise per form. Today in the village, the next entry was
a tiny when-style macro and a call to it. Korvus the crow peered over her shoulder
at the form `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))` and asked what it would come out to.

What Clojure form computes what (my-when true 1 2 3) returns? Submit it via `eval`.

---

I expand the macro with macroexpand and read the produced form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
```

### G10-03 record 2  •  form `(do (defmacro twice [x] `(do ~x ~x)) (twice 7))`  •  expected `7`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

A small audience of sparrows had gathered at the edge of the garden to watch
Sable the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to a macro that emits its argument twice in a do and read out the form
aloud: `(do (defmacro twice [x] `(do ~x ~x)) (twice 7))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a Clojure expression that computes what (twice 7) returns.

---

I submit the syntax-quoted or quoted form to the REPL.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro twice [x] `(do ~x ~x)) (twice 7))"}}]}
```

### G10-03 record 3  •  form `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`  •  expected `3`

```
Hunger and thirst had driven the Crow far from her usual perch.

A small notebook lay open at the edge of the meadow where the clever crow had been
studying syntax-quote. The page showed a tiny when-style macro and a call to it, with the
form `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))` circled in pencil. Sable the crow, drowsy from the warm sun
of the lecture, agreed to write the form to settle once and for all
what it produced.

Write a Clojure expression that computes what (my-when true 1 2 3) returns.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
```

### G10-03 record 4  •  form `(do (defmacro twice [x] `(do ~x ~x)) (twice 7))`  •  expected `7`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

At a moss-flecked pitcher by the meadow, Caw the crow sketched a small
wager: whoever guessed the result of `(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` first would drink
first when the water rose. Sable the crow, without complaint, said it was
simpler to type the form into the REPL than to argue about
a macro that emits its argument twice in a do.

What Clojure form computes what (twice 7) returns? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro twice [x] `(do ~x ~x)) (twice 7))"}}]}
```

### G10-03 record 5  •  form `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`  •  expected `3`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

At a moss-flecked pitcher in the farm, Caw the crow sketched a small
wager: whoever guessed the result of `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))` first would drink
first when the water rose. Sable the crow, her eyes always on the path, said it was
simpler to type the form into the REPL than to argue about
a tiny when-style macro and a call to it.

What Clojure form computes what (my-when true 1 2 3) returns? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
```

## G10-04: Macro expansion rule

### G10-04 record 1  •  form `(macroexpand-1 '(when true 1))`  •  expected `['if', True, ['do', 1]]`

```
Hunger and thirst had driven the Crow far from her usual perch.

Korvus the crow had been trying to teach Sable the crow how the REPL
works. "Look here," he said, pointing to the one-step expansion of (when true 1).
"You hand the form `(macroexpand-1 '(when true 1))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, parched from the long flight, agreed to try.

What Clojure form computes what macroexpand-1 returns for (when true 1)? Submit it via `eval`.

---

I submit the syntax-quoted or quoted form to the REPL.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(when true 1))"}}]}
```

### G10-04 record 2  •  form `(macroexpand-1 '(or a b))`  •  expected `['let*', ['or__1__auto__', 'a'], ['if', 'or__1__auto__', 'or__1__auto__', ['clojure.core/or', 'b']]]`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Sable the crow had spent the morning near the meadow sketching a tiny
language of their own — a notebook of macros that wrote
other forms. The next entry was the one-step expansion of (or a b), and the form
`(macroexpand-1 '(or a b))` was what Sable wanted Caw the crow to submit so
the REPL could show what code it produced or what value it returned.

Write a Clojure expression that computes what macroexpand-1 returns for (or a b).

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(or a b))"}}]}
```

### G10-04 record 3  •  form `(macroexpand-1 '(when true 1))`  •  expected `['if', True, ['do', 1]]`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Korvus the crow and Sable the crow alighted by the market on the rim of an old
pitcher where someone had scratched the one-step expansion of (when true 1). Korvus,
with growing alarm, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(macroexpand-1 '(when true 1))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Question: write a Clojure expression for what macroexpand-1 returns for (when true 1).

---

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(when true 1))"}}]}
```

### G10-04 record 4  •  form `(macroexpand-1 '(or a b))`  •  expected `['let*', ['or__1__auto__', 'a'], ['if', 'or__1__auto__', 'or__1__auto__', ['clojure.core/or', 'b']]]`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

The path in the market was littered with old macro definitions someone
had carved into bark. Caw the crow found one shaped like
the one-step expansion of (or a b) and dared Sable the crow to predict its expansion.
Sable only smiled and asked her to write
`(macroexpand-1 '(or a b))` into the REPL — that, after all, was the whole point
of having a macroexpander.

Write a form whose evaluation gives what macroexpand-1 returns for (or a b).

---

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(or a b))"}}]}
```

### G10-04 record 5  •  form `(macroexpand-1 '(when true 1))`  •  expected `['if', True, ['do', 1]]`

```
Hunger and thirst had driven the Crow far from her usual perch.

Halfway through a long thirsty afternoon, Korvus the crow alighted
by the village and refused to fly on until someone could prove what the form
`(macroexpand-1 '(when true 1))` evaluated to. Korvus called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
the one-step expansion of (when true 1) into the REPL. Whatever rises is the answer."

Write a form whose evaluation gives what macroexpand-1 returns for (when true 1).

---

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(when true 1))"}}]}
```

## G10-05: macroexpand

### G10-05 record 1  •  form `(macroexpand '(when true 1))`  •  expected `['if', True, ['do', 1]]`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

"There is no need to evaluate that," Caw the crow said, swaggering through the underbrush.
"Anyone with a sharp eye can see what the full expansion of (when true 1) comes to."
Sable the crow, who by the farm had grown used to such claims, asked
her to actually write the form `(macroexpand '(when true 1))` and drop it
into the REPL — just to be sure.

Write a Clojure expression that computes what macroexpand returns for (when true 1).

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(when true 1))"}}]}
```

### G10-05 record 2  •  form `(macroexpand '(-> 1 inc inc))`  •  expected `['inc', ['inc', 1]]`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. This was near the road.

A small notebook lay open on the road where the clever crow had been
studying syntax-quote. The page showed the full expansion of (-> 1 inc inc), with the
form `(macroexpand '(-> 1 inc inc))` circled in pencil. Sable the crow, weary from the morning's effort
of the lecture, agreed to write the form to settle once and for all
what it produced.

Write a form whose evaluation gives what macroexpand returns for the threading form.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(-> 1 inc inc))"}}]}
```

### G10-05 record 3  •  form `(macroexpand '(when true 1))`  •  expected `['if', True, ['do', 1]]`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Korvus the crow had been trying to teach Caw the crow how the REPL
works. "Look here," he said, pointing to the full expansion of (when true 1).
"You hand the form `(macroexpand '(when true 1))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Caw, dry-throated and desperate, agreed to try.

Write a form whose evaluation gives what macroexpand returns for (when true 1).

---

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(when true 1))"}}]}
```

### G10-05 record 4  •  form `(macroexpand '(-> 1 inc inc))`  •  expected `['inc', ['inc', 1]]`

```
Hunger and thirst had driven the Crow far from her usual perch.

Halfway through a long thirsty afternoon, Caw the crow alighted
at the edge of the market and refused to fly on until someone could prove what the form
`(macroexpand '(-> 1 inc inc))` evaluated to. Caw called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
the full expansion of (-> 1 inc inc) into the REPL. Whatever rises is the answer."

Write a form whose evaluation gives what macroexpand returns for the threading form.

---

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(-> 1 inc inc))"}}]}
```

### G10-05 record 5  •  form `(macroexpand '(when true 1))`  •  expected `['if', True, ['do', 1]]`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Caw the crow insisted at the edge of the meadow that macros were the same as
functions. Korvus the crow, stepping deliberately, sketched the form
`(macroexpand '(when true 1))` on a strip of bark. "The difference," he
said, "is in the full expansion of (when true 1). Submit the form and let the runtime
tell us exactly what it does."

Write a form whose evaluation gives what macroexpand returns for (when true 1).

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(when true 1))"}}]}
```

## G10-06: when and when-not as macros

### G10-06 record 1  •  form `(when true 1 2 3)`  •  expected `3`

```
Hunger and thirst had driven the Crow far from her usual perch.

"There is no need to evaluate that," Caw the crow said, as if the race were already won.
"Anyone with a sharp eye can see what the form (when true 1 2 3) comes to."
Korvus the crow, who in the market had grown used to such claims, asked
her to actually write the form `(when true 1 2 3)` and drop it
into the REPL — just to be sure.

Write a Clojure expression that computes what (when true 1 2 3) returns.

---

I write the macro form and let the runtime evaluate or expand it.

{"tool_calls":[{"name":"eval","args":{"form":"(when true 1 2 3)"}}]}
```

### G10-06 record 2  •  form `(when false 1 2 3)`  •  expected `None`

```
Hunger and thirst had driven the Crow far from her usual perch. It happened in the village.

Caw the crow etched a wager along the rim of a chipped pitcher
near the village: whoever predicted the result of `(when false 1 2 3)` first would set
the next day's foraging route. Sable the crow, saying very little, said it
would be simpler to drop the form into the REPL than to bicker about
the form (when false 1 2 3).

Write a form whose evaluation gives what (when false 1 2 3) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(when false 1 2 3)"}}]}
```

### G10-06 record 3  •  form `(when-not false :ok)`  •  expected `':ok'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Korvus the crow had been keeping a small leather notebook of every form
he had successfully dropped into the REPL — one entry per
stone, one rise per form. Today in the farm, the next entry was
the form (when-not false :ok). Caw the crow peered over his shoulder
at the form `(when-not false :ok)` and asked what it would come out to.

Write a form whose evaluation gives what (when-not false :ok) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(when-not false :ok)"}}]}
```

### G10-06 record 4  •  form `(when true 1 2 3)`  •  expected `3`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Sable the crow etched a wager along the rim of a chipped pitcher
at the edge of the market: whoever predicted the result of `(when true 1 2 3)` first would set
the next day's foraging route. Caw the crow, with steady, careful steps, said it
would be simpler to drop the form into the REPL than to bicker about
the form (when true 1 2 3).

Write a Clojure expression that computes what (when true 1 2 3) returns.

---

I let each form raise the surface a little closer to the answer.

{"tool_calls":[{"name":"eval","args":{"form":"(when true 1 2 3)"}}]}
```

### G10-06 record 5  •  form `(when false 1 2 3)`  •  expected `None`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A small audience of sparrows had gathered on the road to watch
Korvus the crow attempt to outwit Sable the crow at the rim of an old
pitcher. Sable pointed to the form (when false 1 2 3) and read out the form
aloud: `(when false 1 2 3)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a Clojure expression that computes what (when false 1 2 3) returns.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(when false 1 2 3)"}}]}
```

## G10-07: Threading macros revisited

### G10-07 record 1  •  form `(-> 5 inc inc inc)`  •  expected `8`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. This was near the market.

"A macro is just a function that runs at compile time," Korvus
explained near the market, her eyes always on the path. Sable, as if the race were already won, said
they could already see what the thread-first form (-> 5 inc inc inc) meant.
Korvus the crow insisted they actually evaluate `(-> 5 inc inc inc)` and
read what the runtime reported, expansion or value.

Write a form whose evaluation gives what (-> 5 inc inc inc) returns.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(-> 5 inc inc inc)"}}]}
```

### G10-07 record 2  •  form `(->> [1 2 3 4] (filter even?) (map inc) (reduce +))`  •  expected `8`

```
Hunger and thirst had driven the Crow far from her usual perch.

Halfway through a long thirsty afternoon, Korvus the crow alighted
near the market and refused to fly on until someone could prove what the form
`(->> [1 2 3 4] (filter even?) (map inc) (reduce +))` evaluated to. Korvus called it impossible.
Caw the crow, gliding down at an unhurried pace, simply said: "Drop
a thread-last pipeline over [1 2 3 4] into the REPL. Whatever rises is the answer."

Write a Clojure expression that computes what the ->> pipeline returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(->> [1 2 3 4] (filter even?) (map inc) (reduce +))"}}]}
```

### G10-07 record 3  •  form `(macroexpand '(-> x f g))`  •  expected `['g', ['f', 'x']]`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust on the road: whoever guessed the result of `(macroexpand '(-> x f g))`
first would win the right to claim the next clear water they found.
Caw the crow, stepping deliberately, said it was easier to ask the REPL
about the expansion of (-> x f g) than to argue.

Write a form whose evaluation gives what macroexpand produces for the threading form.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(-> x f g))"}}]}
```

### G10-07 record 4  •  form `(-> 5 inc inc inc)`  •  expected `8`

```
Hunger and thirst had driven the Crow far from her usual perch. It happened near the market.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust in the market: whoever guessed the result of `(-> 5 inc inc inc)`
first would win the right to claim the next clear water they found.
Sable the crow, untroubled by what others thought, said it was easier to ask the REPL
about the thread-first form (-> 5 inc inc inc) than to argue.

Write a form whose evaluation gives what (-> 5 inc inc inc) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(-> 5 inc inc inc)"}}]}
```

### G10-07 record 5  •  form `(->> [1 2 3 4] (filter even?) (map inc) (reduce +))`  •  expected `8`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Caw the crow had spent the morning by the meadow sketching a tiny
language of her own — a notebook of macros that wrote
other forms. The next entry was a thread-last pipeline over [1 2 3 4], and the form
`(->> [1 2 3 4] (filter even?) (map inc) (reduce +))` was what Caw wanted Korvus the crow to submit so
the REPL could show what code it produced or what value it returned.

Write a Clojure expression that computes what the ->> pipeline returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(->> [1 2 3 4] (filter even?) (map inc) (reduce +))"}}]}
```

## G10-08: Macro vs fn

### G10-08 record 1  •  form `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))`  •  expected `7`

```
Hunger and thirst had driven the Crow far from her usual perch.

Korvus the crow and Sable the crow alighted at the edge of the market on the rim of an old
pitcher where someone had scratched a plain function adding two numbers. Korvus,
in a panic, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a Clojure expression that computes the result of calling a function whose args are evaluated.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))"}}]}
```

### G10-08 record 2  •  form `(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))`  •  expected `7`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

"There is no need to evaluate that," Caw the crow said, boasting at every turn.
"Anyone with a sharp eye can see what a macro that emits the same addition form comes to."
Sable the crow, who by the garden had grown used to such claims, asked
her to actually write the form `(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))` and drop it
into the REPL — just to be sure.

What Clojure form computes the result the macro yields after expansion + eval? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))"}}]}
```

### G10-08 record 3  •  form `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))`  •  expected `7`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Caw the crow had spent the morning by the farm sketching a tiny
language of her own — a notebook of macros that wrote
other forms. The next entry was a plain function adding two numbers, and the form
`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` was what Caw wanted Sable the crow to submit so
the REPL could show what code it produced or what value it returned.

What Clojure form computes the result of calling a function whose args are evaluated? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))"}}]}
```

### G10-08 record 4  •  form `(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))`  •  expected `7`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened by the farm.

Halfway through a long thirsty afternoon, Caw the crow alighted
near the farm and refused to fly on until someone could prove what the form
`(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))` evaluated to. Caw called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
a macro that emits the same addition form into the REPL. Whatever rises is the answer."

Write a form whose evaluation gives the result the macro yields after expansion + eval.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))"}}]}
```

### G10-08 record 5  •  form `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))`  •  expected `7`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. All this took place in the meadow.

Sable the crow had spent the morning near the meadow sketching a tiny
language of their own — a notebook of macros that wrote
other forms. The next entry was a plain function adding two numbers, and the form
`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` was what Sable wanted Caw the crow to submit so
the REPL could show what code it produced or what value it returned.

What Clojure form computes the result of calling a function whose args are evaluated? Submit it via `eval`.

---

I expand the macro with macroexpand and read the produced form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))"}}]}
```

## G10-09: Hygiene and gensym

### G10-09 record 1  •  form `(symbol? (gensym))`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was by the meadow.

Sable the crow had spent the morning at the edge of the meadow sketching a tiny
language of their own — a notebook of macros that wrote
other forms. The next entry was the predicate (symbol? (gensym)), and the form
`(symbol? (gensym))` was what Sable wanted Korvus the crow to submit so
the REPL could show what code it produced or what value it returned.

Write a Clojure expression that computes whether (gensym) returns a symbol.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? (gensym))"}}]}
```

### G10-09 record 2  •  form `(let [a (gensym "x_") b (gensym "x_")] (= a b))`  •  expected `False`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Sable the crow etched a wager along the rim of a chipped pitcher
at the edge of the market: whoever predicted the result of `(let [a (gensym "x_") b (gensym "x_")] (= a b))` first would set
the next day's foraging route. Caw the crow, stepping deliberately, said it
would be simpler to drop the form into the REPL than to bicker about
two distinct gensyms with the same prefix.

Write a Clojure expression that computes whether two fresh gensyms are equal.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a (gensym \"x_\") b (gensym \"x_\")] (= a b))"}}]}
```

### G10-09 record 3  •  form `(symbol? (gensym))`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened near the road.

"A macro is just a function that runs at compile time," Korvus
explained on the road, her eyes always on the path. Caw, boasting at every turn, said
she could already see what the predicate (symbol? (gensym)) meant.
Korvus the crow insisted they actually evaluate `(symbol? (gensym))` and
read what the runtime reported, expansion or value.

Question: write a Clojure expression for whether (gensym) returns a symbol.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? (gensym))"}}]}
```

### G10-09 record 4  •  form `(let [a (gensym "x_") b (gensym "x_")] (= a b))`  •  expected `False`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. This was along the road.

A small audience of sparrows had gathered near the road to watch
Korvus the crow attempt to outwit Sable the crow at the rim of an old
pitcher. Sable pointed to two distinct gensyms with the same prefix and read out the form
aloud: `(let [a (gensym "x_") b (gensym "x_")] (= a b))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a Clojure expression that computes whether two fresh gensyms are equal.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a (gensym \"x_\") b (gensym \"x_\")] (= a b))"}}]}
```

### G10-09 record 5  •  form `(symbol? (gensym))`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Halfway through a long thirsty afternoon, Korvus the crow alighted
at the edge of the village and refused to fly on until someone could prove what the form
`(symbol? (gensym))` evaluated to. Korvus called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
the predicate (symbol? (gensym)) into the REPL. Whatever rises is the answer."

Question: write a Clojure expression for whether (gensym) returns a symbol.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? (gensym))"}}]}
```

## G10-10: Anaphoric macros are confusing

### G10-10 record 1  •  form `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))`  •  expected `10`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Korvus the crow and Sable the crow alighted near the road on the rim of an old
pitcher where someone had scratched a hygienic if-let style macro avoiding anaphoric injection. Korvus,
shouting until her voice cracked, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Question: write a Clojure expression for what the hygienic if-let macro returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))"}}]}
```

### G10-10 record 2  •  form `(if-let [x 7] (* x x) 0)`  •  expected `49`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

A small notebook lay open on the hilltop where the clever crow had been
studying syntax-quote. The page showed the built-in if-let, which binds explicitly rather than anaphorically, with the
form `(if-let [x 7] (* x x) 0)` circled in pencil. Korvus the crow, her legs heavy from sprinting
of the lecture, agreed to write the form to settle once and for all
what it produced.

Question: write a Clojure expression for what (if-let [x 7] (* x x) 0) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(if-let [x 7] (* x x) 0)"}}]}
```

### G10-10 record 3  •  form `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))`  •  expected `10`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

At a moss-flecked pitcher along the road, Caw the crow sketched a small
wager: whoever guessed the result of `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))` first would drink
first when the water rose. Korvus the crow, saying very little, said it was
simpler to type the form into the REPL than to argue about
a hygienic if-let style macro avoiding anaphoric injection.

Write a Clojure expression that computes what the hygienic if-let macro returns.

---

I submit the syntax-quoted or quoted form to the REPL.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))"}}]}
```

### G10-10 record 4  •  form `(if-let [x 7] (* x x) 0)`  •  expected `49`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was at the edge of the market.

A small audience of sparrows had gathered near the market to watch
Sable the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to the built-in if-let, which binds explicitly rather than anaphorically and read out the form
aloud: `(if-let [x 7] (* x x) 0)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives what (if-let [x 7] (* x x) 0) returns.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(if-let [x 7] (* x x) 0)"}}]}
```

### G10-10 record 5  •  form `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))`  •  expected `10`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Korvus the crow had been keeping a small leather notebook of every form
he had successfully dropped into the REPL — one entry per
stone, one rise per form. Today by the garden, the next entry was
a hygienic if-let style macro avoiding anaphoric injection. Caw the crow peered over his shoulder
at the form `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))` and asked what it would come out to.

What Clojure form computes what the hygienic if-let macro returns? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))"}}]}
```

## G10-11: Reader macros overview

### G10-11 record 1  •  form `'(1 2 3)`  •  expected `[1, 2, 3]`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Halfway through a long thirsty afternoon, Caw the crow alighted
at the edge of the meadow and refused to fly on until someone could prove what the form
`'(1 2 3)` evaluated to. Caw called it impossible.
Korvus the crow, gliding down at an unhurried pace, simply said: "Drop
the quote reader macro 'foo into the REPL. Whatever rises is the answer."

Write a form whose evaluation gives what '(1 2 3) reads as.

---

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### G10-11 record 2  •  form `(#(* % %) 6)`  •  expected `36`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Korvus the crow insisted at the edge of the garden that macros were the same as
functions. Caw the crow, with steady, careful steps, sketched the form
`(#(* % %) 6)` on a strip of bark. "The difference," she
said, "is in the #(...) reader macro for an anonymous fn. Submit the form and let the runtime
tell us exactly what it does."

Write a Clojure expression that computes what (#(* % %) 6) returns.

---

I expand the macro with macroexpand and read the produced form.

{"tool_calls":[{"name":"eval","args":{"form":"(#(* % %) 6)"}}]}
```

### G10-11 record 3  •  form `[1 #_ 2 3]`  •  expected `[1, 3]`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place at the edge of the meadow.

Sable the crow had been trying to teach Caw the crow how the REPL
works. "Look here," they said, pointing to the #_ form-skip reader macro.
"You hand the form `[1 #_ 2 3]` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Caw, dry-throated and desperate, agreed to try.

Write a form whose evaluation gives what [1 #_ 2 3] reads as when the 2 is dropped.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"[1 #_ 2 3]"}}]}
```

### G10-11 record 4  •  form `'(1 2 3)`  •  expected `[1, 2, 3]`

```
Hunger and thirst had driven the Crow far from her usual perch.

At a moss-flecked pitcher in the village, Korvus the crow sketched a small
wager: whoever guessed the result of `'(1 2 3)` first would drink
first when the water rose. Caw the crow, with steady, careful steps, said it was
simpler to type the form into the REPL than to argue about
the quote reader macro 'foo.

What Clojure form computes what '(1 2 3) reads as? Submit it via `eval`.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### G10-11 record 5  •  form `(#(* % %) 6)`  •  expected `36`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place at the edge of the garden.

Caw the crow had been trying to teach Sable the crow how the REPL
works. "Look here," she said, pointing to the #(...) reader macro for an anonymous fn.
"You hand the form `(#(* % %) 6)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, near to giving up the search for water, agreed to try.

Write a Clojure expression that computes what (#(* % %) 6) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(#(* % %) 6)"}}]}
```

## G10-12: Tagged literals

### G10-12 record 1  •  form `(inst? #inst "2024-01-01")`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was by the village.

Caw the crow had spent the morning near the village sketching a tiny
language of her own — a notebook of macros that wrote
other forms. The next entry was the predicate (inst? #inst "2024-01-01"), and the form
`(inst? #inst "2024-01-01")` was what Caw wanted Korvus the crow to submit so
the REPL could show what code it produced or what value it returned.

Write a form whose evaluation gives whether the #inst tagged literal reads to an inst.

---

I write the macro form and let the runtime evaluate or expand it.

{"tool_calls":[{"name":"eval","args":{"form":"(inst? #inst \"2024-01-01\")"}}]}
```

### G10-12 record 2  •  form `(uuid? #uuid "00000000-0000-0000-0000-000000000000")`  •  expected `True`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Korvus the crow etched a wager along the rim of a chipped pitcher
at the edge of the hilltop: whoever predicted the result of `(uuid? #uuid "00000000-0000-0000-0000-000000000000")` first would set
the next day's foraging route. Caw the crow, saying very little, said it
would be simpler to drop the form into the REPL than to bicker about
the predicate on a #uuid tagged literal.

Question: write a Clojure expression for whether the #uuid tagged literal reads to a uuid.

---

{"tool_calls":[{"name":"eval","args":{"form":"(uuid? #uuid \"00000000-0000-0000-0000-000000000000\")"}}]}
```

### G10-12 record 3  •  form `(inst? #inst "2024-01-01")`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust on the road: whoever guessed the result of `(inst? #inst "2024-01-01")`
first would win the right to claim the next clear water they found.
Korvus the crow, with steady, careful steps, said it was easier to ask the REPL
about the predicate (inst? #inst "2024-01-01") than to argue.

Write a form whose evaluation gives whether the #inst tagged literal reads to an inst.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(inst? #inst \"2024-01-01\")"}}]}
```

### G10-12 record 4  •  form `(uuid? #uuid "00000000-0000-0000-0000-000000000000")`  •  expected `True`

```
Hunger and thirst had driven the Crow far from her usual perch. This was on the hilltop.

At a stone tablet on the hilltop, Sable the crow was teaching
Korvus the crow the discipline of expansion: never trust your eyes,
only the macroexpander. The day's example was the predicate on a #uuid tagged literal.
The form `(uuid? #uuid "00000000-0000-0000-0000-000000000000")` had to be submitted; nothing else would
do.

Question: write a Clojure expression for whether the #uuid tagged literal reads to a uuid.

---

I write the macro form and let the runtime evaluate or expand it.

{"tool_calls":[{"name":"eval","args":{"form":"(uuid? #uuid \"00000000-0000-0000-0000-000000000000\")"}}]}
```

### G10-12 record 5  •  form `(inst? #inst "2024-01-01")`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

At a moss-flecked pitcher in the village, Sable the crow sketched a small
wager: whoever guessed the result of `(inst? #inst "2024-01-01")` first would drink
first when the water rose. Korvus the crow, without complaint, said it was
simpler to type the form into the REPL than to argue about
the predicate (inst? #inst "2024-01-01").

What Clojure form computes whether the #inst tagged literal reads to an inst? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(inst? #inst \"2024-01-01\")"}}]}
```

## G10-13: Data readers and EDN extension

### G10-13 record 1  •  form `(clojure.edn/read-string "42")`  •  expected `42`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Sable the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," they said, pointing to edn read-string of "42".
"You hand the form `(clojure.edn/read-string "42")` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, with a thirst that hurt to bear, agreed to try.

What Clojure form computes what edn/read-string returns for the source "42"? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"42\")"}}]}
```

### G10-13 record 2  •  form `(clojure.edn/read-string "[:a :b :c]")`  •  expected `[':a', ':b', ':c']`

```
Hunger and thirst had driven the Crow far from her usual perch.

A wooden sign nailed to a tree near the market carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(clojure.edn/read-string "[:a :b :c]")`. Sable laughed, puffed up with pride, and declared it
too easy. Korvus said patiently that the only way to be sure of
edn read-string of a vector source was to drop it into the REPL.

Write a Clojure expression that computes what edn/read-string returns for "[:a :b :c]".

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"[:a :b :c]\")"}}]}
```

### G10-13 record 3  •  form `(clojure.edn/read-string "42")`  •  expected `42`

```
Hunger and thirst had driven the Crow far from her usual perch.

Korvus the crow had been keeping a small leather notebook of every form
he had successfully dropped into the REPL — one entry per
stone, one rise per form. Today by the garden, the next entry was
edn read-string of "42". Sable the crow peered over his shoulder
at the form `(clojure.edn/read-string "42")` and asked what it would come out to.

Question: write a Clojure expression for what edn/read-string returns for the source "42".

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"42\")"}}]}
```

### G10-13 record 4  •  form `(clojure.edn/read-string "[:a :b :c]")`  •  expected `[':a', ':b', ':c']`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was in the village.

Caw the crow had been keeping a small leather notebook of every form
she had successfully dropped into the REPL — one entry per
stone, one rise per form. Today by the village, the next entry was
edn read-string of a vector source. Korvus the crow peered over her shoulder
at the form `(clojure.edn/read-string "[:a :b :c]")` and asked what it would come out to.

Write a Clojure expression that computes what edn/read-string returns for "[:a :b :c]".

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"[:a :b :c]\")"}}]}
```

### G10-13 record 5  •  form `(clojure.edn/read-string "42")`  •  expected `42`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was near the village.

"There is no need to evaluate that," Caw the crow said, with a smug grin.
"Anyone with a sharp eye can see what edn read-string of "42" comes to."
Sable the crow, who at the edge of the village had grown used to such claims, asked
her to actually write the form `(clojure.edn/read-string "42")` and drop it
into the REPL — just to be sure.

Write a form whose evaluation gives what edn/read-string returns for the source "42".

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"42\")"}}]}
```

## G10-14: eval (the function)

### G10-14 record 1  •  form `(eval '(+ 1 2 3))`  •  expected `6`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. This was at the edge of the garden.

Sable the crow had spent the morning at the edge of the garden sketching a tiny
language of their own — a notebook of macros that wrote
other forms. The next entry was the form (eval '(+ 1 2 3)), and the form
`(eval '(+ 1 2 3))` was what Sable wanted Caw the crow to submit so
the REPL could show what code it produced or what value it returned.

What Clojure form computes what eval returns for the quoted (+ 1 2 3)? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(eval '(+ 1 2 3))"}}]}
```

### G10-14 record 2  •  form `(eval (list '+ 4 5))`  •  expected `9`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Caw the crow insisted near the farm that macros were the same as
functions. Sable the crow, untroubled by what others thought, sketched the form
`(eval (list '+ 4 5))` on a strip of bark. "The difference," they
said, "is in eval applied to a constructed list. Submit the form and let the runtime
tell us exactly what it does."

Write a form whose evaluation gives what eval returns when handed (list '+ 4 5).

---

I submit the syntax-quoted or quoted form to the REPL.

{"tool_calls":[{"name":"eval","args":{"form":"(eval (list '+ 4 5))"}}]}
```

### G10-14 record 3  •  form `(eval '(+ 1 2 3))`  •  expected `6`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place at the edge of the market.

"A macro is just a function that runs at compile time," Caw
explained near the market, stepping deliberately. Sable, with great whoops of laughter, said
they could already see what the form (eval '(+ 1 2 3)) meant.
Caw the crow insisted they actually evaluate `(eval '(+ 1 2 3))` and
read what the runtime reported, expansion or value.

Write a form whose evaluation gives what eval returns for the quoted (+ 1 2 3).

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(eval '(+ 1 2 3))"}}]}
```

### G10-14 record 4  •  form `(eval (list '+ 4 5))`  •  expected `9`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Korvus the crow etched a wager along the rim of a chipped pitcher
at the edge of the hilltop: whoever predicted the result of `(eval (list '+ 4 5))` first would set
the next day's foraging route. Caw the crow, saying very little, said it
would be simpler to drop the form into the REPL than to bicker about
eval applied to a constructed list.

Write a form whose evaluation gives what eval returns when handed (list '+ 4 5).

---

{"tool_calls":[{"name":"eval","args":{"form":"(eval (list '+ 4 5))"}}]}
```

### G10-14 record 5  •  form `(eval '(+ 1 2 3))`  •  expected `6`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was near the village.

A wooden sign nailed to a tree near the village carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(eval '(+ 1 2 3))`. Caw laughed, swaggering through the underbrush, and declared it
too easy. Sable said patiently that the only way to be sure of
the form (eval '(+ 1 2 3)) was to drop it into the REPL.

Write a form whose evaluation gives what eval returns for the quoted (+ 1 2 3).

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(eval '(+ 1 2 3))"}}]}
```

## G10-15: When not to write a macro

### G10-15 record 1  •  form `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))`  •  expected `7`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

"A macro is just a function that runs at compile time," Sable
explained near the garden, saying very little. Caw, with a smug grin, said
she could already see what a function call where no macro is justified meant.
Sable the crow insisted they actually evaluate `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))` and
read what the runtime reported, expansion or value.

What Clojure form computes what the plain function call returns? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"a function suffices when no syntax shaping is needed\" ((fn [x y] (+ x y)) 3 4))"}}]}
```

### G10-15 record 2  •  form `(do "prefer fn unless you must shape syntax" (map inc [1 2 3]))`  •  expected `[2, 3, 4]`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

At a moss-flecked pitcher in the market, Korvus the crow sketched a small
wager: whoever guessed the result of `(do "prefer fn unless you must shape syntax" (map inc [1 2 3]))` first would drink
first when the water rose. Caw the crow, with steady, careful steps, said it was
simpler to type the form into the REPL than to argue about
map applied to inc where no macro is needed.

Write a form whose evaluation gives the result of mapping inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"prefer fn unless you must shape syntax\" (map inc [1 2 3]))"}}]}
```

### G10-15 record 3  •  form `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))`  •  expected `7`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened by the village.

A wooden sign nailed to a tree in the village carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))`. Sable laughed, with a smug grin, and declared it
too easy. Caw said patiently that the only way to be sure of
a function call where no macro is justified was to drop it into the REPL.

What Clojure form computes what the plain function call returns? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"a function suffices when no syntax shaping is needed\" ((fn [x y] (+ x y)) 3 4))"}}]}
```

### G10-15 record 4  •  form `(do "prefer fn unless you must shape syntax" (map inc [1 2 3]))`  •  expected `[2, 3, 4]`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. All this took place atop the hilltop.

Korvus the crow had spent the morning at the edge of the hilltop sketching a tiny
language of his own — a notebook of macros that wrote
other forms. The next entry was map applied to inc where no macro is needed, and the form
`(do "prefer fn unless you must shape syntax" (map inc [1 2 3]))` was what Korvus wanted Caw the crow to submit so
the REPL could show what code it produced or what value it returned.

Write a Clojure expression that computes the result of mapping inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"prefer fn unless you must shape syntax\" (map inc [1 2 3]))"}}]}
```

### G10-15 record 5  •  form `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))`  •  expected `7`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Caw the crow and Sable the crow alighted on the road on the rim of an old
pitcher where someone had scratched a function call where no macro is justified. Caw,
wide-eyed with fear, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a Clojure expression that computes what the plain function call returns.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"a function suffices when no syntax shaping is needed\" ((fn [x y] (+ x y)) 3 4))"}}]}
```

## G10-16: Macro pattern library

### G10-16 record 1  •  form `(do (defmacro with-clever-pace [& body] `(let [pace# :patient-and-clever] ~@body)) (with-clever-pace 42))`  •  expected `42`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened in the garden.

A small audience of sparrows had gathered near the garden to watch
Caw the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to a with-X macro pattern that binds a local and runs body and read out the form
aloud: `(do (defmacro with-clever-pace [& body] `(let [pace# :patient-and-clever] ~@body)) (with-clever-pace 42))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives what the with- macro yields.

---

I submit the syntax-quoted or quoted form to the REPL.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro with-clever-pace [& body] `(let [pace# :patient-and-clever] ~@body)) (with-clever-pace 42))"}}]}
```

### G10-16 record 2  •  form `(do (defmacro def-pace [name v] `(def ~name ~v)) (def-pace crow-pace :patient) crow-pace)`  •  expected `':patient'`

```
Hunger and thirst had driven the Crow far from her usual perch.

At a moss-flecked pitcher by the orchard, Korvus the crow sketched a small
wager: whoever guessed the result of `(do (defmacro def-pace [name v] `(def ~name ~v)) (def-pace crow-pace :patient) crow-pace)` first would drink
first when the water rose. Sable the crow, with steady, careful steps, said it was
simpler to type the form into the REPL than to argue about
a def-X-thing macro that introduces a named binding.

Question: write a Clojure expression for the value of the symbol the macro defined.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro def-pace [name v] `(def ~name ~v)) (def-pace crow-pace :patient) crow-pace)"}}]}
```

### G10-16 record 3  •  form `(do (defmacro with-clever-pace [& body] `(let [pace# :patient-and-clever] ~@body)) (with-clever-pace 42))`  •  expected `42`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was near the garden.

Korvus the crow had been keeping a small leather notebook of every form
he had successfully dropped into the REPL — one entry per
stone, one rise per form. Today near the garden, the next entry was
a with-X macro pattern that binds a local and runs body. Sable the crow peered over his shoulder
at the form `(do (defmacro with-clever-pace [& body] `(let [pace# :patient-and-clever] ~@body)) (with-clever-pace 42))` and asked what it would come out to.

Write a Clojure expression that computes what the with- macro yields.

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro with-clever-pace [& body] `(let [pace# :patient-and-clever] ~@body)) (with-clever-pace 42))"}}]}
```

### G10-16 record 4  •  form `(do (defmacro def-pace [name v] `(def ~name ~v)) (def-pace crow-pace :patient) crow-pace)`  •  expected `':patient'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Caw the crow had been keeping a small leather notebook of every form
she had successfully dropped into the REPL — one entry per
stone, one rise per form. Today near the farm, the next entry was
a def-X-thing macro that introduces a named binding. Sable the crow peered over her shoulder
at the form `(do (defmacro def-pace [name v] `(def ~name ~v)) (def-pace crow-pace :patient) crow-pace)` and asked what it would come out to.

Write a Clojure expression that computes the value of the symbol the macro defined.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro def-pace [name v] `(def ~name ~v)) (def-pace crow-pace :patient) crow-pace)"}}]}
```

### G10-16 record 5  •  form `(do (defmacro with-clever-pace [& body] `(let [pace# :patient-and-clever] ~@body)) (with-clever-pace 42))`  •  expected `42`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust on the hilltop: whoever guessed the result of `(do (defmacro with-clever-pace [& body] `(let [pace# :patient-and-clever] ~@body)) (with-clever-pace 42))`
first would win the right to claim the next clear water they found.
Caw the crow, stepping deliberately, said it was easier to ask the REPL
about a with-X macro pattern that binds a local and runs body than to argue.

What Clojure form computes what the with- macro yields? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro with-clever-pace [& body] `(let [pace# :patient-and-clever] ~@body)) (with-clever-pace 42))"}}]}
```

