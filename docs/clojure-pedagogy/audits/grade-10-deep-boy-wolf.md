# Boy-wolf Grade 10 — deep spot-check

5 generated records per subject (across all examples and a variety of seeds). Read every record carefully. Flag anything that reads odd to a careful reader, including issues the structural audit can't catch (prose flow, contextual fit, cliché repetition, subplot/example mismatch, etc.)

---

## G10-01: quote, unquote, unquote-splice

**Examples:** 3 | **Subplots:** 16 | **Plan-pool size:** 11

### Record 1 — example 1 of 3

**form**: `(quote (+ 1 2))` • **expected**: `['+', 1, 2]`

**concept_phrase**: `the quoted form (quote (+ 1 2))`

**question_what**: `the value of (quote (+ 1 2)) — the unevaluated list`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Pat insisted near the woods that macros were the same as
functions. Alice, without complaint, drew the form `(quote (+ 1 2))`
on a strip of bark. "The difference," she said, "is in
the quoted form (quote (+ 1 2)). Submit the form and let the runtime tell us exactly
what it does."

Write a Clojure expression that computes the value of (quote (+ 1 2)) — the unevaluated list.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(quote (+ 1 2))"}}]}
```

### Record 2 — example 2 of 3

**form**: `'(1 2 3)` • **expected**: `[1, 2, 3]`

**concept_phrase**: `the quoted list '(1 2 3)`

**question_what**: `the value of '(1 2 3)`

```
The boy on the hill thought the trick clever the first time he played it.

The elder of the village kept a small slate in the village, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the quoted list '(1 2 3). Sam read
out the form `'(1 2 3)` so Lou could write it
properly into the REPL and earn an honest mark on the slate.

Write a Clojure expression that computes the value of '(1 2 3).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### Record 3 — example 3 of 3

**form**: `(let [x 5] `(a ~x b))` • **expected**: `['a', 5, 'b']`

**concept_phrase**: `a syntax-quoted list with one unquote`

**question_what**: `the result of `(a ~x b) when x is 5`

```
Every shepherd in the valley knew the danger of crying wolf for sport. This was near the road.

The elder of the village kept a small slate on the road, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was a syntax-quoted list with one unquote. George read
out the form `(let [x 5] `(a ~x b))` so Tom could write it
properly into the REPL and earn an honest mark on the slate.

Question: write a Clojure expression for the result of `(a ~x b) when x is 5.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 5] `(a ~x b))"}}]}
```

### Record 4 — example 1 of 3

**form**: `(quote (+ 1 2))` • **expected**: `['+', 1, 2]`

**concept_phrase**: `the quoted form (quote (+ 1 2))`

**question_what**: `the value of (quote (+ 1 2)) — the unevaluated list`

```
Every shepherd in the valley knew the danger of crying wolf for sport. It happened at the edge of the village.

Jess insisted by the village that macros were the same as
functions. Frank, stepping deliberately, drew the form `(quote (+ 1 2))`
on a strip of bark. "The difference," he said, "is in
the quoted form (quote (+ 1 2)). Submit the form and let the runtime tell us exactly
what it does."

Write a Clojure expression that computes the value of (quote (+ 1 2)) — the unevaluated list.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(quote (+ 1 2))"}}]}
```

### Record 5 — example 2 of 3

**form**: `'(1 2 3)` • **expected**: `[1, 2, 3]`

**concept_phrase**: `the quoted list '(1 2 3)`

**question_what**: `the value of '(1 2 3)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

The path near the hilltop was littered with old macro definitions someone had
carved into bark. Tom found one shaped like
the quoted list '(1 2 3) and dared Oliver to predict its expansion.
Oliver only smiled and asked him to write
`'(1 2 3)` into the REPL — that, after all, was the whole point of
having a macroexpander.

Question: write a Clojure expression for the value of '(1 2 3).

---

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

---

## G10-02: syntax-quote

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 11

### Record 1 — example 1 of 2

**form**: `(let [x 10] `(+ ~x ~x))` • **expected**: `['+', 10, 10]`

**concept_phrase**: `a syntax-quoted addition with x unquoted twice`

**question_what**: `the form produced by `(+ ~x ~x) when x is 10`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Will called down from a stone by the orchard where someone had
chalked a syntax-quoted addition with x unquoted twice on a flat board. Will, with a smug grin,
declared he already knew what would come back. Morgan,
stepping deliberately, asked him to actually submit the form
`(let [x 10] `(+ ~x ~x))` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a form whose evaluation gives the form produced by `(+ ~x ~x) when x is 10.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 10] `(+ ~x ~x))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(let [xs [1 2 3]] `(list ~@xs))` • **expected**: `['list', 1, 2, 3]`

**concept_phrase**: `a syntax-quoted list with unquote-splice`

**question_what**: `the form produced by `(list ~@xs) when xs is [1 2 3]`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place by the woods.

At a stone tablet at the edge of the woods, Grace was teaching Tom
the discipline of expansion: never trust your eyes, only the
macroexpander. The day's example was a syntax-quoted list with unquote-splice. The form
`(let [xs [1 2 3]] `(list ~@xs))` had to be submitted; nothing else would do.

Write a Clojure expression that computes the form produced by `(list ~@xs) when xs is [1 2 3].

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [xs [1 2 3]] `(list ~@xs))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(let [x 10] `(+ ~x ~x))` • **expected**: `['+', 10, 10]`

**concept_phrase**: `a syntax-quoted addition with x unquoted twice`

**question_what**: `the form produced by `(+ ~x ~x) when x is 10`

```
The boy on the hill thought the trick clever the first time he played it. It happened by the woods.

The path in the woods was littered with old macro definitions someone had
carved into bark. Pat found one shaped like
a syntax-quoted addition with x unquoted twice and dared Alice to predict its expansion.
Alice only smiled and asked them to write
`(let [x 10] `(+ ~x ~x))` into the REPL — that, after all, was the whole point of
having a macroexpander.

Write a form whose evaluation gives the form produced by `(+ ~x ~x) when x is 10.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 10] `(+ ~x ~x))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(let [xs [1 2 3]] `(list ~@xs))` • **expected**: `['list', 1, 2, 3]`

**concept_phrase**: `a syntax-quoted list with unquote-splice`

**question_what**: `the form produced by `(list ~@xs) when xs is [1 2 3]`

```
The boy on the hill thought the trick clever the first time he played it. This was along the road.

George kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today on the road the next entry was
a syntax-quoted list with unquote-splice. Jess peered over his shoulder
at the form `(let [xs [1 2 3]] `(list ~@xs))` and was asked, gently, to be the one to
submit it.

Write a Clojure expression that computes the form produced by `(list ~@xs) when xs is [1 2 3].

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [xs [1 2 3]] `(list ~@xs))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(let [x 10] `(+ ~x ~x))` • **expected**: `['+', 10, 10]`

**concept_phrase**: `a syntax-quoted addition with x unquoted twice`

**question_what**: `the form produced by `(+ ~x ~x) when x is 10`

```
The boy on the hill thought the trick clever the first time he played it. This was by the forest.

Halfway through the morning watch, Lou called out
at the edge of the forest, demanding a verdict on the form `(let [x 10] `(+ ~x ~x))` and refusing
to descend until somebody confirmed it. Lou insisted
she already knew the answer. George, walking up
at an unhurried pace, simply said: "Submit a syntax-quoted addition with x unquoted twice to the
REPL. Whatever comes back is the answer."

What Clojure form computes the form produced by `(+ ~x ~x) when x is 10? Submit it via `eval`.

---

I write the form and let the macroexpander or REPL show the result.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 10] `(+ ~x ~x))"}}]}
```

---

## G10-03: defmacro introduction

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 11

### Record 1 — example 1 of 2

**form**: `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))` • **expected**: `3`

**concept_phrase**: `a tiny when-style macro and a call to it`

**question_what**: `what (my-when true 1 2 3) returns`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place at the edge of the village.

A small crowd of villagers had gathered near the village to watch
Will attempt to predict, off the cuff, what the REPL would
return. Alice pointed to a tiny when-style macro and a call to it and read out the
form aloud: `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a Clojure expression that computes what (my-when true 1 2 3) returns.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` • **expected**: `7`

**concept_phrase**: `a macro that emits its argument twice in a do`

**question_what**: `what (twice 7) returns`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened near the meadow.

Halfway through the morning watch, Lou called out
near the meadow, demanding a verdict on the form `(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` and refusing
to descend until somebody confirmed it. Lou insisted
she already knew the answer. Oliver, walking up
at an unhurried pace, simply said: "Submit a macro that emits its argument twice in a do to the
REPL. Whatever comes back is the answer."

Write a form whose evaluation gives what (twice 7) returns.

---

I write the form and let the macroexpander or REPL show the result.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro twice [x] `(do ~x ~x)) (twice 7))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))` • **expected**: `3`

**concept_phrase**: `a tiny when-style macro and a call to it`

**question_what**: `what (my-when true 1 2 3) returns`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A wooden notice nailed to a post by the farm carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`. Pat
laughed, with great whoops of laughter, and declared it too easy to bother with.
Frank said, patiently, that the only way to be certain of
a tiny when-style macro and a call to it was to put it in the REPL.

Write a Clojure expression that computes what (my-when true 1 2 3) returns.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` • **expected**: `7`

**concept_phrase**: `a macro that emits its argument twice in a do`

**question_what**: `what (twice 7) returns`

```
The boy on the hill thought the trick clever the first time he played it.

The elder of the village kept a small slate near the village, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was a macro that emits its argument twice in a do. Bob read
out the form `(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` so Will could write it
properly into the REPL and earn an honest mark on the slate.

What Clojure form computes what (twice 7) returns? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro twice [x] `(do ~x ~x)) (twice 7))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))` • **expected**: `3`

**concept_phrase**: `a tiny when-style macro and a call to it`

**question_what**: `what (my-when true 1 2 3) returns`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

At a stone tablet by the village, Robin was teaching Will
the discipline of expansion: never trust your eyes, only the
macroexpander. The day's example was a tiny when-style macro and a call to it. The form
`(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))` had to be submitted; nothing else would do.

Write a Clojure expression that computes what (my-when true 1 2 3) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
```

---

## G10-04: Macro expansion rule

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 11

### Record 1 — example 1 of 2

**form**: `(macroexpand-1 '(when true 1))` • **expected**: `['if', True, ['do', 1]]`

**concept_phrase**: `the one-step expansion of (when true 1)`

**question_what**: `what macroexpand-1 returns for (when true 1)`

```
The boy on the hill thought the trick clever the first time he played it.

A small notebook lay open near the farm where the elder had been studying
syntax-quote. The page showed the one-step expansion of (when true 1), with the form
`(macroexpand-1 '(when true 1))` circled in pencil. Pat, lulled by the gentle wind of
the lecture, agreed to write the form to settle once and for all what
it produced.

Write a Clojure expression that computes what macroexpand-1 returns for (when true 1).

---

I expand the macro with macroexpand and read the produced form.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(when true 1))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(macroexpand-1 '(or a b))` • **expected**: `['let*', ['or__1__auto__', 'a'], ['if', 'or__1__auto__', 'or__1__auto__', ['clojure.core/or', 'b']]]`

**concept_phrase**: `the one-step expansion of (or a b)`

**question_what**: `what macroexpand-1 returns for (or a b)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened at the edge of the village.

At a stone tablet near the village, George was teaching Jess
the discipline of expansion: never trust your eyes, only the
macroexpander. The day's example was the one-step expansion of (or a b). The form
`(macroexpand-1 '(or a b))` had to be submitted; nothing else would do.

Write a Clojure expression that computes what macroexpand-1 returns for (or a b).

---

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(or a b))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(macroexpand-1 '(when true 1))` • **expected**: `['if', True, ['do', 1]]`

**concept_phrase**: `the one-step expansion of (when true 1)`

**question_what**: `what macroexpand-1 returns for (when true 1)`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

"A macro is just a function that runs at compile time," Sam
explained near the road, with steady, careful steps. Tom, swaggering through the underbrush, said
he could already see what the one-step expansion of (when true 1) meant.
Sam insisted they actually evaluate `(macroexpand-1 '(when true 1))` and read
what the runtime reported, expansion or value.

Write a Clojure expression that computes what macroexpand-1 returns for (when true 1).

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(when true 1))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(macroexpand-1 '(or a b))` • **expected**: `['let*', ['or__1__auto__', 'a'], ['if', 'or__1__auto__', 'or__1__auto__', ['clojure.core/or', 'b']]]`

**concept_phrase**: `the one-step expansion of (or a b)`

**question_what**: `what macroexpand-1 returns for (or a b)`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden notice nailed to a post at the edge of the orchard carried a small puzzle. The
riddle simply asked the reader to evaluate `(macroexpand-1 '(or a b))`. Tom
laughed, puffed up with pride, and declared it too easy to bother with.
Bob said, patiently, that the only way to be certain of
the one-step expansion of (or a b) was to put it in the REPL.

Write a form whose evaluation gives what macroexpand-1 returns for (or a b).

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(or a b))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(macroexpand-1 '(when true 1))` • **expected**: `['if', True, ['do', 1]]`

**concept_phrase**: `the one-step expansion of (when true 1)`

**question_what**: `what macroexpand-1 returns for (when true 1)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place at the edge of the orchard.

A small crowd of villagers had gathered near the orchard to watch
Lou attempt to predict, off the cuff, what the REPL would
return. Oliver pointed to the one-step expansion of (when true 1) and read out the
form aloud: `(macroexpand-1 '(when true 1))`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

What Clojure form computes what macroexpand-1 returns for (when true 1)? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(when true 1))"}}]}
```

---

## G10-05: macroexpand

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 11

### Record 1 — example 1 of 2

**form**: `(macroexpand '(when true 1))` • **expected**: `['if', True, ['do', 1]]`

**concept_phrase**: `the full expansion of (when true 1)`

**question_what**: `what macroexpand returns for (when true 1)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

"There is no need to evaluate that," Jess said, swaggering through the underbrush.
"Anyone can see what the full expansion of (when true 1) comes to." Alice, who
near the hilltop had heard such claims many times, asked her to
actually write the form `(macroexpand '(when true 1))` and submit it to the REPL —
just to be sure.

Question: write a Clojure expression for what macroexpand returns for (when true 1).

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(when true 1))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(macroexpand '(-> 1 inc inc))` • **expected**: `['inc', ['inc', 1]]`

**concept_phrase**: `the full expansion of (-> 1 inc inc)`

**question_what**: `what macroexpand returns for the threading form`

```
The boy on the hill thought the trick clever the first time he played it.

The path in the forest was littered with old macro definitions someone had
carved into bark. Tom found one shaped like
the full expansion of (-> 1 inc inc) and dared Alex to predict its expansion.
Alex only smiled and asked him to write
`(macroexpand '(-> 1 inc inc))` into the REPL — that, after all, was the whole point of
having a macroexpander.

What Clojure form computes what macroexpand returns for the threading form? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(-> 1 inc inc))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(macroexpand '(when true 1))` • **expected**: `['if', True, ['do', 1]]`

**concept_phrase**: `the full expansion of (when true 1)`

**question_what**: `what macroexpand returns for (when true 1)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place at the edge of the orchard.

Halfway through the morning watch, Jess called out
in the orchard, demanding a verdict on the form `(macroexpand '(when true 1))` and refusing
to descend until somebody confirmed it. Jess insisted
she already knew the answer. Grace, walking up
at an unhurried pace, simply said: "Submit the full expansion of (when true 1) to the
REPL. Whatever comes back is the answer."

Write a form whose evaluation gives what macroexpand returns for (when true 1).

---

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(when true 1))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(macroexpand '(-> 1 inc inc))` • **expected**: `['inc', ['inc', 1]]`

**concept_phrase**: `the full expansion of (-> 1 inc inc)`

**question_what**: `what macroexpand returns for the threading form`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

The path in the farm was littered with old macro definitions someone had
carved into bark. Lou found one shaped like
the full expansion of (-> 1 inc inc) and dared Carol to predict its expansion.
Carol only smiled and asked her to write
`(macroexpand '(-> 1 inc inc))` into the REPL — that, after all, was the whole point of
having a macroexpander.

Question: write a Clojure expression for what macroexpand returns for the threading form.

---

I expand the macro with macroexpand and read the produced form.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(-> 1 inc inc))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(macroexpand '(when true 1))` • **expected**: `['if', True, ['do', 1]]`

**concept_phrase**: `the full expansion of (when true 1)`

**question_what**: `what macroexpand returns for (when true 1)`

```
The boy on the hill thought the trick clever the first time he played it.

The path at the edge of the farm was littered with old macro definitions someone had
carved into bark. Jess found one shaped like
the full expansion of (when true 1) and dared Carol to predict its expansion.
Carol only smiled and asked her to write
`(macroexpand '(when true 1))` into the REPL — that, after all, was the whole point of
having a macroexpander.

What Clojure form computes what macroexpand returns for (when true 1)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(when true 1))"}}]}
```

---

## G10-06: when and when-not as macros

**Examples:** 3 | **Subplots:** 16 | **Plan-pool size:** 11

### Record 1 — example 1 of 3

**form**: `(when true 1 2 3)` • **expected**: `3`

**concept_phrase**: `the form (when true 1 2 3)`

**question_what**: `what (when true 1 2 3) returns`

```
The boy on the hill thought the trick clever the first time he played it.

A small notebook lay open atop the hilltop where the elder had been studying
syntax-quote. The page showed the form (when true 1 2 3), with the form
`(when true 1 2 3)` circled in pencil. Will, weary from the morning's effort of
the lecture, agreed to write the form to settle once and for all what
it produced.

Write a Clojure expression that computes what (when true 1 2 3) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(when true 1 2 3)"}}]}
```

### Record 2 — example 2 of 3

**form**: `(when false 1 2 3)` • **expected**: `None`

**concept_phrase**: `the form (when false 1 2 3)`

**question_what**: `what (when false 1 2 3) returns`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

"There is no need to evaluate that," Pat said, with a smug grin.
"Anyone can see what the form (when false 1 2 3) comes to." Robin, who
near the woods had heard such claims many times, asked them to
actually write the form `(when false 1 2 3)` and submit it to the REPL —
just to be sure.

What Clojure form computes what (when false 1 2 3) returns? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(when false 1 2 3)"}}]}
```

### Record 3 — example 3 of 3

**form**: `(when-not false :ok)` • **expected**: `':ok'`

**concept_phrase**: `the form (when-not false :ok)`

**question_what**: `what (when-not false :ok) returns`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Robin had been trying to teach Tom how the REPL
works. "Look here," they said, pointing to the form (when-not false :ok).
"You hand the form `(when-not false :ok)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Tom, her legs heavy from sprinting, agreed to try.

Question: write a Clojure expression for what (when-not false :ok) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(when-not false :ok)"}}]}
```

### Record 4 — example 1 of 3

**form**: `(when true 1 2 3)` • **expected**: `3`

**concept_phrase**: `the form (when true 1 2 3)`

**question_what**: `what (when true 1 2 3) returns`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A small notebook lay open at the edge of the hilltop where the elder had been studying
syntax-quote. The page showed the form (when true 1 2 3), with the form
`(when true 1 2 3)` circled in pencil. Lou, lulled by the gentle wind of
the lecture, agreed to write the form to settle once and for all what
it produced.

Write a form whose evaluation gives what (when true 1 2 3) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(when true 1 2 3)"}}]}
```

### Record 5 — example 2 of 3

**form**: `(when false 1 2 3)` • **expected**: `None`

**concept_phrase**: `the form (when false 1 2 3)`

**question_what**: `what (when false 1 2 3) returns`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

The path near the village was littered with old macro definitions someone had
carved into bark. Jess found one shaped like
the form (when false 1 2 3) and dared Bob to predict its expansion.
Bob only smiled and asked her to write
`(when false 1 2 3)` into the REPL — that, after all, was the whole point of
having a macroexpander.

What Clojure form computes what (when false 1 2 3) returns? Submit it via `eval`.

---

I write the form and let the macroexpander or REPL show the result.

{"tool_calls":[{"name":"eval","args":{"form":"(when false 1 2 3)"}}]}
```

---

## G10-07: Threading macros revisited

**Examples:** 3 | **Subplots:** 16 | **Plan-pool size:** 11

### Record 1 — example 1 of 3

**form**: `(-> 5 inc inc inc)` • **expected**: `8`

**concept_phrase**: `the thread-first form (-> 5 inc inc inc)`

**question_what**: `what (-> 5 inc inc inc) returns`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(-> 5 inc inc inc)`, and the line
above it read the thread-first form (-> 5 inc inc inc). Robin handed the page to
Tom, who, lulled by the gentle wind, agreed to write it out properly.

What Clojure form computes what (-> 5 inc inc inc) returns? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(-> 5 inc inc inc)"}}]}
```

### Record 2 — example 2 of 3

**form**: `(->> [1 2 3 4] (filter even?) (map inc) (reduce +))` • **expected**: `8`

**concept_phrase**: `a thread-last pipeline over [1 2 3 4]`

**question_what**: `what the ->> pipeline returns`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place near the meadow.

The path by the meadow was littered with old macro definitions someone had
carved into bark. Jess found one shaped like
a thread-last pipeline over [1 2 3 4] and dared Oliver to predict its expansion.
Oliver only smiled and asked her to write
`(->> [1 2 3 4] (filter even?) (map inc) (reduce +))` into the REPL — that, after all, was the whole point of
having a macroexpander.

Write a Clojure expression that computes what the ->> pipeline returns.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(->> [1 2 3 4] (filter even?) (map inc) (reduce +))"}}]}
```

### Record 3 — example 3 of 3

**form**: `(macroexpand '(-> x f g))` • **expected**: `['g', ['f', 'x']]`

**concept_phrase**: `the expansion of (-> x f g)`

**question_what**: `what macroexpand produces for the threading form`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Lou called down from a stone near the village where someone had
chalked the expansion of (-> x f g) on a flat board. Lou, boasting at every turn,
declared she already knew what would come back. Frank,
without complaint, asked her to actually submit the form
`(macroexpand '(-> x f g))` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes what macroexpand produces for the threading form.

---

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(-> x f g))"}}]}
```

### Record 4 — example 1 of 3

**form**: `(-> 5 inc inc inc)` • **expected**: `8`

**concept_phrase**: `the thread-first form (-> 5 inc inc inc)`

**question_what**: `what (-> 5 inc inc inc) returns`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A small crowd of villagers had gathered at the edge of the farm to watch
Lou attempt to predict, off the cuff, what the REPL would
return. Morgan pointed to the thread-first form (-> 5 inc inc inc) and read out the
form aloud: `(-> 5 inc inc inc)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a form whose evaluation gives what (-> 5 inc inc inc) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(-> 5 inc inc inc)"}}]}
```

### Record 5 — example 2 of 3

**form**: `(->> [1 2 3 4] (filter even?) (map inc) (reduce +))` • **expected**: `8`

**concept_phrase**: `a thread-last pipeline over [1 2 3 4]`

**question_what**: `what the ->> pipeline returns`

```
The boy on the hill thought the trick clever the first time he played it. This was at the edge of the hilltop.

Carol had spent the morning on the hilltop sketching a tiny language
of her own — a notebook of macros that wrote other forms.
The next entry was a thread-last pipeline over [1 2 3 4], and the form `(->> [1 2 3 4] (filter even?) (map inc) (reduce +))` was
what Carol wanted Pat to submit so the REPL could
show what code it produced or what value it returned.

Write a form whose evaluation gives what the ->> pipeline returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(->> [1 2 3 4] (filter even?) (map inc) (reduce +))"}}]}
```

---

## G10-08: Macro vs fn

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 11

### Record 1 — example 1 of 2

**form**: `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` • **expected**: `7`

**concept_phrase**: `a plain function adding two numbers`

**question_what**: `the result of calling a function (args evaluated)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened near the orchard.

A small notebook lay open in the orchard where the elder had been studying
syntax-quote. The page showed a plain function adding two numbers, with the form
`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` circled in pencil. Tom, lulled by the gentle wind of
the lecture, agreed to write the form to settle once and for all what
it produced.

Write a form whose evaluation gives the result of calling a function (args evaluated).

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))` • **expected**: `7`

**concept_phrase**: `a macro that emits the same addition form`

**question_what**: `the result the macro yields after expansion + eval`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened by the orchard.

Alex had spent the morning by the orchard sketching a tiny language
of their own — a notebook of macros that wrote other forms.
The next entry was a macro that emits the same addition form, and the form `(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))` was
what Alex wanted Pat to submit so the REPL could
show what code it produced or what value it returned.

Write a Clojure expression that computes the result the macro yields after expansion + eval.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` • **expected**: `7`

**concept_phrase**: `a plain function adding two numbers`

**question_what**: `the result of calling a function (args evaluated)`

```
The boy on the hill thought the trick clever the first time he played it. It happened at the edge of the farm.

Will insisted near the farm that macros were the same as
functions. Grace, stepping deliberately, drew the form `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))`
on a strip of bark. "The difference," she said, "is in
a plain function adding two numbers. Submit the form and let the runtime tell us exactly
what it does."

Write a Clojure expression that computes the result of calling a function (args evaluated).

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))` • **expected**: `7`

**concept_phrase**: `a macro that emits the same addition form`

**question_what**: `the result the macro yields after expansion + eval`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place in the meadow.

A wooden notice nailed to a post near the meadow carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))`. Tom
laughed, with a smug grin, and declared it too easy to bother with.
Sam said, patiently, that the only way to be certain of
a macro that emits the same addition form was to put it in the REPL.

Write a Clojure expression that computes the result the macro yields after expansion + eval.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` • **expected**: `7`

**concept_phrase**: `a plain function adding two numbers`

**question_what**: `the result of calling a function (args evaluated)`

```
The boy on the hill thought the trick clever the first time he played it.

"A macro is just a function that runs at compile time," Oliver
explained by the orchard, untroubled by what others thought. Pat, with great whoops of laughter, said
they could already see what a plain function adding two numbers meant.
Oliver insisted they actually evaluate `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` and read
what the runtime reported, expansion or value.

Write a Clojure expression that computes the result of calling a function (args evaluated).

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))"}}]}
```

---

## G10-09: Hygiene and gensym

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 11

### Record 1 — example 1 of 2

**form**: `(symbol? (gensym))` • **expected**: `True`

**concept_phrase**: `the predicate (symbol? (gensym))`

**question_what**: `whether (gensym) returns a symbol`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place in the woods.

"There is no need to evaluate that," Will said, as if the race were already won.
"Anyone can see what the predicate (symbol? (gensym)) comes to." George, who
at the edge of the woods had heard such claims many times, asked him to
actually write the form `(symbol? (gensym))` and submit it to the REPL —
just to be sure.

Question: write a Clojure expression for whether (gensym) returns a symbol.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? (gensym))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(let [a (gensym "x_") b (gensym "x_")] (= a b))` • **expected**: `False`

**concept_phrase**: `two distinct gensyms with the same prefix`

**question_what**: `whether two fresh gensyms are equal`

```
The boy on the hill thought the trick clever the first time he played it.

Alice had spent the morning by the forest sketching a tiny language
of her own — a notebook of macros that wrote other forms.
The next entry was two distinct gensyms with the same prefix, and the form `(let [a (gensym "x_") b (gensym "x_")] (= a b))` was
what Alice wanted Pat to submit so the REPL could
show what code it produced or what value it returned.

Write a form whose evaluation gives whether two fresh gensyms are equal.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a (gensym \"x_\") b (gensym \"x_\")] (= a b))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(symbol? (gensym))` • **expected**: `True`

**concept_phrase**: `the predicate (symbol? (gensym))`

**question_what**: `whether (gensym) returns a symbol`

```
The boy on the hill thought the trick clever the first time he played it.

A small notebook lay open in the orchard where the elder had been studying
syntax-quote. The page showed the predicate (symbol? (gensym)), with the form
`(symbol? (gensym))` circled in pencil. Jess, yawning at the soft moss of
the lecture, agreed to write the form to settle once and for all what
it produced.

Write a Clojure expression that computes whether (gensym) returns a symbol.

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? (gensym))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(let [a (gensym "x_") b (gensym "x_")] (= a b))` • **expected**: `False`

**concept_phrase**: `two distinct gensyms with the same prefix`

**question_what**: `whether two fresh gensyms are equal`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

"There is no need to evaluate that," Pat said, with great whoops of laughter.
"Anyone can see what two distinct gensyms with the same prefix comes to." Carol, who
at the edge of the woods had heard such claims many times, asked them to
actually write the form `(let [a (gensym "x_") b (gensym "x_")] (= a b))` and submit it to the REPL —
just to be sure.

Write a form whose evaluation gives whether two fresh gensyms are equal.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a (gensym \"x_\") b (gensym \"x_\")] (= a b))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(symbol? (gensym))` • **expected**: `True`

**concept_phrase**: `the predicate (symbol? (gensym))`

**question_what**: `whether (gensym) returns a symbol`

```
The boy on the hill thought the trick clever the first time he played it.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(symbol? (gensym))`, and the line
above it read the predicate (symbol? (gensym)). George handed the page to
Tom, who, yawning at the soft moss, agreed to write it out properly.

Question: write a Clojure expression for whether (gensym) returns a symbol.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? (gensym))"}}]}
```

---

## G10-10: Anaphoric macros are confusing

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 11

### Record 1 — example 1 of 2

**form**: `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))` • **expected**: `10`

**concept_phrase**: `a hygienic if-let style macro avoiding anaphoric injection`

**question_what**: `what the hygienic if-let macro returns`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Lou called down from a stone atop the hilltop where someone had
chalked a hygienic if-let style macro avoiding anaphoric injection on a flat board. Lou, boasting at every turn,
declared she already knew what would come back. Grace,
with steady, careful steps, asked her to actually submit the form
`(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes what the hygienic if-let macro returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(if-let [x 7] (* x x) 0)` • **expected**: `49`

**concept_phrase**: `the built-in if-let, which binds explicitly`

**question_what**: `what (if-let [x 7] (* x x) 0) returns`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. This was near the orchard.

"A macro is just a function that runs at compile time," Carol
explained near the orchard, saying very little. Pat, with a smug grin, said
they could already see what the built-in if-let, which binds explicitly meant.
Carol insisted they actually evaluate `(if-let [x 7] (* x x) 0)` and read
what the runtime reported, expansion or value.

Question: write a Clojure expression for what (if-let [x 7] (* x x) 0) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(if-let [x 7] (* x x) 0)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))` • **expected**: `10`

**concept_phrase**: `a hygienic if-let style macro avoiding anaphoric injection`

**question_what**: `what the hygienic if-let macro returns`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Halfway through the morning watch, Tom called out
on the hilltop, demanding a verdict on the form `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))` and refusing
to descend until somebody confirmed it. Tom insisted
he already knew the answer. Alice, walking up
at an unhurried pace, simply said: "Submit a hygienic if-let style macro avoiding anaphoric injection to the
REPL. Whatever comes back is the answer."

What Clojure form computes what the hygienic if-let macro returns? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(if-let [x 7] (* x x) 0)` • **expected**: `49`

**concept_phrase**: `the built-in if-let, which binds explicitly`

**question_what**: `what (if-let [x 7] (* x x) 0) returns`

```
The boy on the hill thought the trick clever the first time he played it. This was along the road.

At a stone tablet along the road, Alice was teaching Tom
the discipline of expansion: never trust your eyes, only the
macroexpander. The day's example was the built-in if-let, which binds explicitly. The form
`(if-let [x 7] (* x x) 0)` had to be submitted; nothing else would do.

Question: write a Clojure expression for what (if-let [x 7] (* x x) 0) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(if-let [x 7] (* x x) 0)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))` • **expected**: `10`

**concept_phrase**: `a hygienic if-let style macro avoiding anaphoric injection`

**question_what**: `what the hygienic if-let macro returns`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

At a stone tablet by the farm, Robin was teaching Tom
the discipline of expansion: never trust your eyes, only the
macroexpander. The day's example was a hygienic if-let style macro avoiding anaphoric injection. The form
`(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))` had to be submitted; nothing else would do.

Write a form whose evaluation gives what the hygienic if-let macro returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))"}}]}
```

---

## G10-11: Reader macros overview

**Examples:** 3 | **Subplots:** 16 | **Plan-pool size:** 11

### Record 1 — example 1 of 3

**form**: `'(1 2 3)` • **expected**: `[1, 2, 3]`

**concept_phrase**: `the quote reader macro 'foo`

**question_what**: `what '(1 2 3) reads as`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened in the meadow.

A wooden notice nailed to a post in the meadow carried a small puzzle. The
riddle simply asked the reader to evaluate `'(1 2 3)`. Will
laughed, boasting at every turn, and declared it too easy to bother with.
Bob said, patiently, that the only way to be certain of
the quote reader macro 'foo was to put it in the REPL.

Question: write a Clojure expression for what '(1 2 3) reads as.

---

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### Record 2 — example 2 of 3

**form**: `(#(* % %) 6)` • **expected**: `36`

**concept_phrase**: `the #(...) reader macro for an anonymous fn`

**question_what**: `what (#(* % %) 6) returns`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place near the road.

Sam kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the road the next entry was
the #(...) reader macro for an anonymous fn. Jess peered over their shoulder
at the form `(#(* % %) 6)` and was asked, gently, to be the one to
submit it.

Write a Clojure expression that computes what (#(* % %) 6) returns.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(#(* % %) 6)"}}]}
```

### Record 3 — example 3 of 3

**form**: `[1 #_ 2 3]` • **expected**: `[1, 3]`

**concept_phrase**: `the #_ form-skip reader macro`

**question_what**: `what [1 #_ 2 3] reads as`

```
The boy on the hill thought the trick clever the first time he played it.

A small notebook lay open at the edge of the village where the elder had been studying
syntax-quote. The page showed the #_ form-skip reader macro, with the form
`[1 #_ 2 3]` circled in pencil. Pat, drowsy from the warm sun of
the lecture, agreed to write the form to settle once and for all what
it produced.

Question: write a Clojure expression for what [1 #_ 2 3] reads as.

---

{"tool_calls":[{"name":"eval","args":{"form":"[1 #_ 2 3]"}}]}
```

### Record 4 — example 1 of 3

**form**: `'(1 2 3)` • **expected**: `[1, 2, 3]`

**concept_phrase**: `the quote reader macro 'foo`

**question_what**: `what '(1 2 3) reads as`

```
The boy on the hill thought the trick clever the first time he played it. All this took place by the woods.

Halfway through the morning watch, Lou called out
by the woods, demanding a verdict on the form `'(1 2 3)` and refusing
to descend until somebody confirmed it. Lou insisted
she already knew the answer. Frank, walking up
at an unhurried pace, simply said: "Submit the quote reader macro 'foo to the
REPL. Whatever comes back is the answer."

Write a Clojure expression that computes what '(1 2 3) reads as.

---

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### Record 5 — example 2 of 3

**form**: `(#(* % %) 6)` • **expected**: `36`

**concept_phrase**: `the #(...) reader macro for an anonymous fn`

**question_what**: `what (#(* % %) 6) returns`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. This was near the forest.

Halfway through the morning watch, Will called out
at the edge of the forest, demanding a verdict on the form `(#(* % %) 6)` and refusing
to descend until somebody confirmed it. Will insisted
he already knew the answer. Alex, walking up
at an unhurried pace, simply said: "Submit the #(...) reader macro for an anonymous fn to the
REPL. Whatever comes back is the answer."

Write a form whose evaluation gives what (#(* % %) 6) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(#(* % %) 6)"}}]}
```

---

## G10-12: Tagged literals

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 11

### Record 1 — example 1 of 2

**form**: `(inst? #inst "2024-01-01")` • **expected**: `True`

**concept_phrase**: `the predicate (inst? #inst "2024-01-01")`

**question_what**: `whether the #inst tagged literal reads to an inst`

```
The boy on the hill thought the trick clever the first time he played it. This was near the orchard.

A small crowd of villagers had gathered near the orchard to watch
Jess attempt to predict, off the cuff, what the REPL would
return. Grace pointed to the predicate (inst? #inst "2024-01-01") and read out the
form aloud: `(inst? #inst "2024-01-01")`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a Clojure expression that computes whether the #inst tagged literal reads to an inst.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(inst? #inst \"2024-01-01\")"}}]}
```

### Record 2 — example 2 of 2

**form**: `(uuid? #uuid "00000000-0000-0000-0000-000000000000")` • **expected**: `True`

**concept_phrase**: `the predicate on a #uuid tagged literal`

**question_what**: `whether the #uuid tagged literal reads to a uuid`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A small crowd of villagers had gathered in the meadow to watch
Will attempt to predict, off the cuff, what the REPL would
return. Frank pointed to the predicate on a #uuid tagged literal and read out the
form aloud: `(uuid? #uuid "00000000-0000-0000-0000-000000000000")`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Question: write a Clojure expression for whether the #uuid tagged literal reads to a uuid.

---

{"tool_calls":[{"name":"eval","args":{"form":"(uuid? #uuid \"00000000-0000-0000-0000-000000000000\")"}}]}
```

### Record 3 — example 1 of 2

**form**: `(inst? #inst "2024-01-01")` • **expected**: `True`

**concept_phrase**: `the predicate (inst? #inst "2024-01-01")`

**question_what**: `whether the #inst tagged literal reads to an inst`

```
The boy on the hill thought the trick clever the first time he played it. It happened along the road.

The elder of the village kept a small slate near the road, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the predicate (inst? #inst "2024-01-01"). George read
out the form `(inst? #inst "2024-01-01")` so Tom could write it
properly into the REPL and earn an honest mark on the slate.

What Clojure form computes whether the #inst tagged literal reads to an inst? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(inst? #inst \"2024-01-01\")"}}]}
```

### Record 4 — example 2 of 2

**form**: `(uuid? #uuid "00000000-0000-0000-0000-000000000000")` • **expected**: `True`

**concept_phrase**: `the predicate on a #uuid tagged literal`

**question_what**: `whether the #uuid tagged literal reads to a uuid`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A small slate sat on a flat stone on the road; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(uuid? #uuid "00000000-0000-0000-0000-000000000000")`, and the page
heading read the predicate on a #uuid tagged literal. Frank nodded at Will to
write the form properly so the slate would carry an honest entry.

Question: write a Clojure expression for whether the #uuid tagged literal reads to a uuid.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(uuid? #uuid \"00000000-0000-0000-0000-000000000000\")"}}]}
```

### Record 5 — example 1 of 2

**form**: `(inst? #inst "2024-01-01")` • **expected**: `True`

**concept_phrase**: `the predicate (inst? #inst "2024-01-01")`

**question_what**: `whether the #inst tagged literal reads to an inst`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

At a stone tablet in the farm, Oliver was teaching Tom
the discipline of expansion: never trust your eyes, only the
macroexpander. The day's example was the predicate (inst? #inst "2024-01-01"). The form
`(inst? #inst "2024-01-01")` had to be submitted; nothing else would do.

What Clojure form computes whether the #inst tagged literal reads to an inst? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(inst? #inst \"2024-01-01\")"}}]}
```

---

## G10-13: Data readers and EDN extension

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 11

### Record 1 — example 1 of 2

**form**: `(clojure.edn/read-string "42")` • **expected**: `42`

**concept_phrase**: `edn read-string of "42"`

**question_what**: `what edn/read-string returns for the source "42"`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Pat insisted at the edge of the woods that macros were the same as
functions. Sam, untroubled by what others thought, drew the form `(clojure.edn/read-string "42")`
on a strip of bark. "The difference," they said, "is in
edn read-string of "42". Submit the form and let the runtime tell us exactly
what it does."

Write a Clojure expression that computes what edn/read-string returns for the source "42".

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"42\")"}}]}
```

### Record 2 — example 2 of 2

**form**: `(clojure.edn/read-string "[:a :b :c]")` • **expected**: `[':a', ':b', ':c']`

**concept_phrase**: `edn read-string of a vector source`

**question_what**: `what edn/read-string returns for "[:a :b :c]"`

```
The boy on the hill thought the trick clever the first time he played it.

George had been trying to teach Jess how the REPL
works. "Look here," he said, pointing to edn read-string of a vector source.
"You hand the form `(clojure.edn/read-string "[:a :b :c]")` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, drowsy from the warm sun, agreed to try.

Write a Clojure expression that computes what edn/read-string returns for "[:a :b :c]".

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"[:a :b :c]\")"}}]}
```

### Record 3 — example 1 of 2

**form**: `(clojure.edn/read-string "42")` • **expected**: `42`

**concept_phrase**: `edn read-string of "42"`

**question_what**: `what edn/read-string returns for the source "42"`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened at the edge of the farm.

A small crowd of villagers had gathered in the farm to watch
Tom attempt to predict, off the cuff, what the REPL would
return. Bob pointed to edn read-string of "42" and read out the
form aloud: `(clojure.edn/read-string "42")`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

What Clojure form computes what edn/read-string returns for the source "42"? Submit it via `eval`.

---

I submit the syntax-quoted or quoted form to the REPL.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"42\")"}}]}
```

### Record 4 — example 2 of 2

**form**: `(clojure.edn/read-string "[:a :b :c]")` • **expected**: `[':a', ':b', ':c']`

**concept_phrase**: `edn read-string of a vector source`

**question_what**: `what edn/read-string returns for "[:a :b :c]"`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. This was at the edge of the forest.

The elder of the village kept a small slate near the forest, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was edn read-string of a vector source. Morgan read
out the form `(clojure.edn/read-string "[:a :b :c]")` so Lou could write it
properly into the REPL and earn an honest mark on the slate.

Write a Clojure expression that computes what edn/read-string returns for "[:a :b :c]".

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"[:a :b :c]\")"}}]}
```

### Record 5 — example 1 of 2

**form**: `(clojure.edn/read-string "42")` • **expected**: `42`

**concept_phrase**: `edn read-string of "42"`

**question_what**: `what edn/read-string returns for the source "42"`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Lou called down from a stone near the woods where someone had
chalked edn read-string of "42" on a flat board. Lou, boasting at every turn,
declared she already knew what would come back. Alex,
stepping deliberately, asked her to actually submit the form
`(clojure.edn/read-string "42")` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes what edn/read-string returns for the source "42".

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"42\")"}}]}
```

---

## G10-14: eval (the function)

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 11

### Record 1 — example 1 of 2

**form**: `(eval '(+ 1 2 3))` • **expected**: `6`

**concept_phrase**: `the form (eval '(+ 1 2 3))`

**question_what**: `what eval returns for the quoted (+ 1 2 3)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A small crowd of villagers had gathered at the edge of the orchard to watch
Jess attempt to predict, off the cuff, what the REPL would
return. Carol pointed to the form (eval '(+ 1 2 3)) and read out the
form aloud: `(eval '(+ 1 2 3))`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Question: write a Clojure expression for what eval returns for the quoted (+ 1 2 3).

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(eval '(+ 1 2 3))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(eval (list '+ 4 5))` • **expected**: `9`

**concept_phrase**: `eval applied to a constructed list`

**question_what**: `what eval returns when handed (list '+ 4 5)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. This was along the road.

Pat insisted along the road that macros were the same as
functions. Grace, without complaint, drew the form `(eval (list '+ 4 5))`
on a strip of bark. "The difference," she said, "is in
eval applied to a constructed list. Submit the form and let the runtime tell us exactly
what it does."

Question: write a Clojure expression for what eval returns when handed (list '+ 4 5).

---

{"tool_calls":[{"name":"eval","args":{"form":"(eval (list '+ 4 5))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(eval '(+ 1 2 3))` • **expected**: `6`

**concept_phrase**: `the form (eval '(+ 1 2 3))`

**question_what**: `what eval returns for the quoted (+ 1 2 3)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Halfway through the morning watch, Will called out
in the woods, demanding a verdict on the form `(eval '(+ 1 2 3))` and refusing
to descend until somebody confirmed it. Will insisted
he already knew the answer. Morgan, walking up
at an unhurried pace, simply said: "Submit the form (eval '(+ 1 2 3)) to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for what eval returns for the quoted (+ 1 2 3).

---

{"tool_calls":[{"name":"eval","args":{"form":"(eval '(+ 1 2 3))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(eval (list '+ 4 5))` • **expected**: `9`

**concept_phrase**: `eval applied to a constructed list`

**question_what**: `what eval returns when handed (list '+ 4 5)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

"A macro is just a function that runs at compile time," Alice
explained at the edge of the farm, untroubled by what others thought. Tom, with a smug grin, said
he could already see what eval applied to a constructed list meant.
Alice insisted they actually evaluate `(eval (list '+ 4 5))` and read
what the runtime reported, expansion or value.

Write a Clojure expression that computes what eval returns when handed (list '+ 4 5).

---

{"tool_calls":[{"name":"eval","args":{"form":"(eval (list '+ 4 5))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(eval '(+ 1 2 3))` • **expected**: `6`

**concept_phrase**: `the form (eval '(+ 1 2 3))`

**question_what**: `what eval returns for the quoted (+ 1 2 3)`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

"There is no need to evaluate that," Jess said, as if the race were already won.
"Anyone can see what the form (eval '(+ 1 2 3)) comes to." Grace, who
near the woods had heard such claims many times, asked her to
actually write the form `(eval '(+ 1 2 3))` and submit it to the REPL —
just to be sure.

What Clojure form computes what eval returns for the quoted (+ 1 2 3)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(eval '(+ 1 2 3))"}}]}
```

---

## G10-15: When not to write a macro

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 11

### Record 1 — example 1 of 2

**form**: `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))` • **expected**: `7`

**concept_phrase**: `a function call where no macro is justified`

**question_what**: `what the plain function call returns`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Lou insisted near the meadow that macros were the same as
functions. Grace, without complaint, drew the form `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))`
on a strip of bark. "The difference," she said, "is in
a function call where no macro is justified. Submit the form and let the runtime tell us exactly
what it does."

What Clojure form computes what the plain function call returns? Submit it via `eval`.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"a function suffices when no syntax shaping is needed\" ((fn [x y] (+ x y)) 3 4))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do "prefer fn unless you must shape syntax" (map inc [1 2 3]))` • **expected**: `[2, 3, 4]`

**concept_phrase**: `map applied to inc — no macro needed`

**question_what**: `the result of mapping inc`

```
Every shepherd in the valley knew the danger of crying wolf for sport. This was near the hilltop.

Tom called down from a stone atop the hilltop where someone had
chalked map applied to inc — no macro needed on a flat board. Tom, as if the race were already won,
declared he already knew what would come back. Alex,
untroubled by what others thought, asked him to actually submit the form
`(do "prefer fn unless you must shape syntax" (map inc [1 2 3]))` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the result of mapping inc.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"prefer fn unless you must shape syntax\" (map inc [1 2 3]))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))` • **expected**: `7`

**concept_phrase**: `a function call where no macro is justified`

**question_what**: `what the plain function call returns`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Lou insisted near the orchard that macros were the same as
functions. George, saying very little, drew the form `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))`
on a strip of bark. "The difference," he said, "is in
a function call where no macro is justified. Submit the form and let the runtime tell us exactly
what it does."

Write a Clojure expression that computes what the plain function call returns.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"a function suffices when no syntax shaping is needed\" ((fn [x y] (+ x y)) 3 4))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do "prefer fn unless you must shape syntax" (map inc [1 2 3]))` • **expected**: `[2, 3, 4]`

**concept_phrase**: `map applied to inc — no macro needed`

**question_what**: `the result of mapping inc`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Will insisted near the meadow that macros were the same as
functions. Frank, untroubled by what others thought, drew the form `(do "prefer fn unless you must shape syntax" (map inc [1 2 3]))`
on a strip of bark. "The difference," he said, "is in
map applied to inc — no macro needed. Submit the form and let the runtime tell us exactly
what it does."

Question: write a Clojure expression for the result of mapping inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"prefer fn unless you must shape syntax\" (map inc [1 2 3]))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))` • **expected**: `7`

**concept_phrase**: `a function call where no macro is justified`

**question_what**: `what the plain function call returns`

```
The boy on the hill thought the trick clever the first time he played it. All this took place in the village.

Carol had spent the morning at the edge of the village sketching a tiny language
of her own — a notebook of macros that wrote other forms.
The next entry was a function call where no macro is justified, and the form `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))` was
what Carol wanted Jess to submit so the REPL could
show what code it produced or what value it returned.

Write a Clojure expression that computes what the plain function call returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"a function suffices when no syntax shaping is needed\" ((fn [x y] (+ x y)) 3 4))"}}]}
```

---

## G10-16: Macro pattern library

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 11

### Record 1 — example 1 of 2

**form**: `(do (defmacro with-careful-watch [& body] `(let [pace# :alert-and-honest] ~@body)) (with-careful-watch 42))` • **expected**: `42`

**concept_phrase**: `a with-X macro pattern that binds a local and runs body`

**question_what**: `what the with- macro yields`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden notice nailed to a post by the orchard carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (defmacro with-careful-watch [& body] `(let [pace# :alert-and-honest] ~@body)) (with-careful-watch 42))`. Pat
laughed, as if the race were already won, and declared it too easy to bother with.
Sam said, patiently, that the only way to be certain of
a with-X macro pattern that binds a local and runs body was to put it in the REPL.

Write a form whose evaluation gives what the with- macro yields.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro with-careful-watch [& body] `(let [pace# :alert-and-honest] ~@body)) (with-careful-watch 42))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (defmacro def-watch [name v] `(def ~name ~v)) (def-watch watch-mode :alert) watch-mode)` • **expected**: `':alert'`

**concept_phrase**: `a def-X-thing macro that introduces a named binding`

**question_what**: `the value of the symbol the macro defined`

```
The boy on the hill thought the trick clever the first time he played it. All this took place near the village.

Alice had spent the morning at the edge of the village sketching a tiny language
of her own — a notebook of macros that wrote other forms.
The next entry was a def-X-thing macro that introduces a named binding, and the form `(do (defmacro def-watch [name v] `(def ~name ~v)) (def-watch watch-mode :alert) watch-mode)` was
what Alice wanted Tom to submit so the REPL could
show what code it produced or what value it returned.

What Clojure form computes the value of the symbol the macro defined? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro def-watch [name v] `(def ~name ~v)) (def-watch watch-mode :alert) watch-mode)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (defmacro with-careful-watch [& body] `(let [pace# :alert-and-honest] ~@body)) (with-careful-watch 42))` • **expected**: `42`

**concept_phrase**: `a with-X macro pattern that binds a local and runs body`

**question_what**: `what the with- macro yields`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

The path in the farm was littered with old macro definitions someone had
carved into bark. Pat found one shaped like
a with-X macro pattern that binds a local and runs body and dared Bob to predict its expansion.
Bob only smiled and asked them to write
`(do (defmacro with-careful-watch [& body] `(let [pace# :alert-and-honest] ~@body)) (with-careful-watch 42))` into the REPL — that, after all, was the whole point of
having a macroexpander.

Question: write a Clojure expression for what the with- macro yields.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro with-careful-watch [& body] `(let [pace# :alert-and-honest] ~@body)) (with-careful-watch 42))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (defmacro def-watch [name v] `(def ~name ~v)) (def-watch watch-mode :alert) watch-mode)` • **expected**: `':alert'`

**concept_phrase**: `a def-X-thing macro that introduces a named binding`

**question_what**: `the value of the symbol the macro defined`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Frank had been trying to teach Will how the REPL
works. "Look here," he said, pointing to a def-X-thing macro that introduces a named binding.
"You hand the form `(do (defmacro def-watch [name v] `(def ~name ~v)) (def-watch watch-mode :alert) watch-mode)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Will, drowsy from the warm sun, agreed to try.

Question: write a Clojure expression for the value of the symbol the macro defined.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro def-watch [name v] `(def ~name ~v)) (def-watch watch-mode :alert) watch-mode)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (defmacro with-careful-watch [& body] `(let [pace# :alert-and-honest] ~@body)) (with-careful-watch 42))` • **expected**: `42`

**concept_phrase**: `a with-X macro pattern that binds a local and runs body`

**question_what**: `what the with- macro yields`

```
The boy on the hill thought the trick clever the first time he played it. This was by the orchard.

Frank had been trying to teach Pat how the REPL
works. "Look here," he said, pointing to a with-X macro pattern that binds a local and runs body.
"You hand the form `(do (defmacro with-careful-watch [& body] `(let [pace# :alert-and-honest] ~@body)) (with-careful-watch 42))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Pat, drowsy from the warm sun, agreed to try.

Write a form whose evaluation gives what the with- macro yields.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro with-careful-watch [& body] `(let [pace# :alert-and-honest] ~@body)) (with-careful-watch 42))"}}]}
```

---

