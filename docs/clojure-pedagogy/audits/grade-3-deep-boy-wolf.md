# Boy-wolf Grade 3 — deep spot-check

5 generated records per subject (across all examples and a variety of seeds). Read every record carefully. Flag anything that reads odd to a careful reader, including issues the structural audit can't catch (prose flow, contextual fit, cliché repetition, subplot/example mismatch, etc.)

---

## G3-01: def — top-level binding

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do (def x 42) x)` • **expected**: `42`

**concept_phrase**: `the binding (def x 42) followed by x`

**question_what**: `the value bound to x after (def x 42)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Alice kept a small ledger near the woods where every meaningful
quantity in the village got its own labeled mark on the slate.
She pointed to today's entry: the binding (def x 42) followed by x. The form
`(do (def x 42) x)` would settle it once Pat agreed to look at
the binding rather than guess.

Write a Clojure expression that computes the value bound to x after (def x 42).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 42) x)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (def y 7) y)` • **expected**: `7`

**concept_phrase**: `the binding (def y 7)`

**question_what**: `the value bound to y`

```
The boy on the hill thought the trick clever the first time he played it.

Lou called down from a stone in the village where someone had
chalked the binding (def y 7) on a flat board. Lou, puffed up with pride,
declared she already knew what would come back. Sam,
untroubled by what others thought, asked her to actually submit the form
`(do (def y 7) y)` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the value bound to y.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def y 7) y)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (def x 42) x)` • **expected**: `42`

**concept_phrase**: `the binding (def x 42) followed by x`

**question_what**: `the value bound to x after (def x 42)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Frank kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today by the village the next entry was
the binding (def x 42) followed by x. Pat peered over his shoulder
at the form `(do (def x 42) x)` and was asked, gently, to be the one to
submit it.

Write a Clojure expression that computes the value bound to x after (def x 42).

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 42) x)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (def y 7) y)` • **expected**: `7`

**concept_phrase**: `the binding (def y 7)`

**question_what**: `the value bound to y`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden notice nailed to a post by the orchard carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (def y 7) y)`. Pat
laughed, puffed up with pride, and declared it too easy to bother with.
Oliver said, patiently, that the only way to be certain of
the binding (def y 7) was to put it in the REPL.

What Clojure form computes the value bound to y? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def y 7) y)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (def x 42) x)` • **expected**: `42`

**concept_phrase**: `the binding (def x 42) followed by x`

**question_what**: `the value bound to x after (def x 42)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Lou called down from a stone on the road where someone had
chalked the binding (def x 42) followed by x on a flat board. Lou, with great whoops of laughter,
declared she already knew what would come back. Alex,
stepping deliberately, asked her to actually submit the form
`(do (def x 42) x)` to the REPL — the village had stopped trusting answers
that weren't checked.

What Clojure form computes the value bound to x after (def x 42)? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 42) x)"}}]}
```

---

## G3-02: def — redefinition

**Examples:** 1 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 1

**form**: `(do (def x 1) (def x 99) x)` • **expected**: `99`

**concept_phrase**: `the redefined x`

**question_what**: `the value of x after redefinition`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Will called down from a stone by the orchard where someone had
chalked the redefined x on a flat board. Will, with a smug grin,
declared he already knew what would come back. Morgan,
stepping deliberately, asked him to actually submit the form
`(do (def x 1) (def x 99) x)` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a form whose evaluation gives the value of x after redefinition.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 1) (def x 99) x)"}}]}
```

### Record 2 — example 1 of 1

**form**: `(do (def x 1) (def x 99) x)` • **expected**: `99`

**concept_phrase**: `the redefined x`

**question_what**: `the value of x after redefinition`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place by the woods.

Tom called down from a stone by the woods where someone had
chalked the redefined x on a flat board. Tom, boasting at every turn,
declared he already knew what would come back. Alice,
with steady, careful steps, asked him to actually submit the form
`(do (def x 1) (def x 99) x)` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a form whose evaluation gives the value of x after redefinition.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 1) (def x 99) x)"}}]}
```

### Record 3 — example 1 of 1

**form**: `(do (def x 1) (def x 99) x)` • **expected**: `99`

**concept_phrase**: `the redefined x`

**question_what**: `the value of x after redefinition`

```
The boy on the hill thought the trick clever the first time he played it. It happened by the woods.

A wooden notice nailed to a post in the woods carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (def x 1) (def x 99) x)`. Pat
laughed, swaggering through the underbrush, and declared it too easy to bother with.
Alice said, patiently, that the only way to be certain of
the redefined x was to put it in the REPL.

Write a form whose evaluation gives the value of x after redefinition.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 1) (def x 99) x)"}}]}
```

### Record 4 — example 1 of 1

**form**: `(do (def x 1) (def x 99) x)` • **expected**: `99`

**concept_phrase**: `the redefined x`

**question_what**: `the value of x after redefinition`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place by the orchard.

"You can call it whatever you like," Carol said near the orchard, "but the
form is what matters." She drew the binding for
Pat: the form `(do (def x 1) (def x 99) x)` captured the redefined x,
and the REPL would do the rest — no claims required, just the
runtime's answer.

Write a Clojure expression that computes the value of x after redefinition.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 1) (def x 99) x)"}}]}
```

### Record 5 — example 1 of 1

**form**: `(do (def x 1) (def x 99) x)` • **expected**: `99`

**concept_phrase**: `the redefined x`

**question_what**: `the value of x after redefinition`

```
The boy on the hill thought the trick clever the first time he played it. This was by the forest.

A small crowd of villagers had gathered at the edge of the forest to watch
Lou attempt to predict, off the cuff, what the REPL would
return. George pointed to the redefined x and read out the
form aloud: `(do (def x 1) (def x 99) x)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

What Clojure form computes the value of x after redefinition? Submit it via `eval`.

---

I bind the inputs in a let, then compute.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 1) (def x 99) x)"}}]}
```

---

## G3-03: let — local binding

**Examples:** 3 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 3

**form**: `(let [x 3] (+ x 1))` • **expected**: `4`

**concept_phrase**: `the form (let [x 3] (+ x 1))`

**question_what**: `the result of (let [x 3] (+ x 1))`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place at the edge of the village.

Alice had been trying to teach Will how the REPL
works. "Look here," she said, pointing to the form (let [x 3] (+ x 1)).
"You hand the form `(let [x 3] (+ x 1))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Will, drowsy from the warm sun, agreed to try.

Write a Clojure expression that computes the result of (let [x 3] (+ x 1)).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
```

### Record 2 — example 2 of 3

**form**: `(let [n 10] (* n n))` • **expected**: `100`

**concept_phrase**: `the form (let [n 10] (* n n))`

**question_what**: `the square of n where n is bound to 10`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened near the meadow.

Oliver had been trying to teach Lou how the REPL
works. "Look here," he said, pointing to the form (let [n 10] (* n n)).
"You hand the form `(let [n 10] (* n n))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Lou, yawning at the soft moss, agreed to try.

Write a form whose evaluation gives the square of n where n is bound to 10.

---

I bind the inputs in a let, then compute.

{"tool_calls":[{"name":"eval","args":{"form":"(let [n 10] (* n n))"}}]}
```

### Record 3 — example 3 of 3

**form**: `(let [a 5] a)` • **expected**: `5`

**concept_phrase**: `the form (let [a 5] a)`

**question_what**: `the value of (let [a 5] a)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A wooden notice nailed to a post at the edge of the meadow carried a small puzzle. The
riddle simply asked the reader to evaluate `(let [a 5] a)`. Will
laughed, swaggering through the underbrush, and declared it too easy to bother with.
Oliver said, patiently, that the only way to be certain of
the form (let [a 5] a) was to put it in the REPL.

Question: write a Clojure expression for the value of (let [a 5] a).

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 5] a)"}}]}
```

### Record 4 — example 1 of 3

**form**: `(let [x 3] (+ x 1))` • **expected**: `4`

**concept_phrase**: `the form (let [x 3] (+ x 1))`

**question_what**: `the result of (let [x 3] (+ x 1))`

```
The boy on the hill thought the trick clever the first time he played it.

Frank had been trying to teach Will how the REPL
works. "Look here," he said, pointing to the form (let [x 3] (+ x 1)).
"You hand the form `(let [x 3] (+ x 1))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Will, lulled by the gentle wind, agreed to try.

What Clojure form computes the result of (let [x 3] (+ x 1))? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
```

### Record 5 — example 2 of 3

**form**: `(let [n 10] (* n n))` • **expected**: `100`

**concept_phrase**: `the form (let [n 10] (* n n))`

**question_what**: `the square of n where n is bound to 10`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

The elder of the village kept a small slate at the edge of the orchard, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the form (let [n 10] (* n n)). George read
out the form `(let [n 10] (* n n))` so Will could write it
properly into the REPL and earn an honest mark on the slate.

Write a form whose evaluation gives the square of n where n is bound to 10.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(let [n 10] (* n n))"}}]}
```

---

## G3-04: let — multi-binding

**Examples:** 3 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 3

**form**: `(let [a 1 b 2] (+ a b))` • **expected**: `3`

**concept_phrase**: `the form with two bindings`

**question_what**: `the result of (let [a 1 b 2] (+ a b))`

```
The boy on the hill thought the trick clever the first time he played it.

"You can call it whatever you like," Bob said near the farm, "but the
form is what matters." He drew the binding for
Pat: the form `(let [a 1 b 2] (+ a b))` captured the form with two bindings,
and the REPL would do the rest — no claims required, just the
runtime's answer.

Write a Clojure expression that computes the result of (let [a 1 b 2] (+ a b)).

---

I name the values first and then combine them.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 1 b 2] (+ a b))"}}]}
```

### Record 2 — example 2 of 3

**form**: `(let [x 5 y 3] (- x y))` • **expected**: `2`

**concept_phrase**: `the form (let [x 5 y 3] (- x y))`

**question_what**: `the result of (- x y) when x=5, y=3`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened at the edge of the village.

"You can call it whatever you like," George said near the village, "but the
form is what matters." He drew the binding for
Jess: the form `(let [x 5 y 3] (- x y))` captured the form (let [x 5 y 3] (- x y)),
and the REPL would do the rest — no claims required, just the
runtime's answer.

Write a Clojure expression that computes the result of (- x y) when x=5, y=3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 5 y 3] (- x y))"}}]}
```

### Record 3 — example 3 of 3

**form**: `(let [a 2 b 3 c 4] (+ a b c))` • **expected**: `9`

**concept_phrase**: `a let with three bindings`

**question_what**: `the sum of a, b, c when a=2, b=3, c=4`

```
The boy on the hill thought the trick clever the first time he played it.

Carol had been trying to teach Pat how the REPL
works. "Look here," she said, pointing to a let with three bindings.
"You hand the form `(let [a 2 b 3 c 4] (+ a b c))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Pat, lulled by the gentle wind, agreed to try.

Question: write a Clojure expression for the sum of a, b, c when a=2, b=3, c=4.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 2 b 3 c 4] (+ a b c))"}}]}
```

### Record 4 — example 1 of 3

**form**: `(let [a 1 b 2] (+ a b))` • **expected**: `3`

**concept_phrase**: `the form with two bindings`

**question_what**: `the result of (let [a 1 b 2] (+ a b))`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A small crowd of villagers had gathered at the edge of the forest to watch
Jess attempt to predict, off the cuff, what the REPL would
return. Oliver pointed to the form with two bindings and read out the
form aloud: `(let [a 1 b 2] (+ a b))`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a form whose evaluation gives the result of (let [a 1 b 2] (+ a b)).

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 1 b 2] (+ a b))"}}]}
```

### Record 5 — example 2 of 3

**form**: `(let [x 5 y 3] (- x y))` • **expected**: `2`

**concept_phrase**: `the form (let [x 5 y 3] (- x y))`

**question_what**: `the result of (- x y) when x=5, y=3`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A small slate sat on a flat stone in the village; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(let [x 5 y 3] (- x y))`, and the page
heading read the form (let [x 5 y 3] (- x y)). Frank nodded at Lou to
write the form properly so the slate would carry an honest entry.

Question: write a Clojure expression for the result of (- x y) when x=5, y=3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 5 y 3] (- x y))"}}]}
```

---

## G3-05: let — shadowing outer def

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do (def x 10) (let [x 99] x))` • **expected**: `99`

**concept_phrase**: `an inner let shadowing the outer def`

**question_what**: `the inner-let value of x`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Halfway through the morning watch, Jess called out
near the hilltop, demanding a verdict on the form `(do (def x 10) (let [x 99] x))` and refusing
to descend until somebody confirmed it. Jess insisted
she already knew the answer. Alice, walking up
at an unhurried pace, simply said: "Submit an inner let shadowing the outer def to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the inner-let value of x.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 10) (let [x 99] x))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (def x 10) (let [x 99] x) x)` • **expected**: `10`

**concept_phrase**: `the outer x after the inner let returns`

**question_what**: `the outer x after the let scope ends`

```
The boy on the hill thought the trick clever the first time he played it.

A wooden notice nailed to a post in the forest carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (def x 10) (let [x 99] x) x)`. Tom
laughed, with great whoops of laughter, and declared it too easy to bother with.
Alex said, patiently, that the only way to be certain of
the outer x after the inner let returns was to put it in the REPL.

What Clojure form computes the outer x after the let scope ends? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 10) (let [x 99] x) x)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (def x 10) (let [x 99] x))` • **expected**: `99`

**concept_phrase**: `an inner let shadowing the outer def`

**question_what**: `the inner-let value of x`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place at the edge of the orchard.

Grace had been trying to teach Jess how the REPL
works. "Look here," she said, pointing to an inner let shadowing the outer def.
"You hand the form `(do (def x 10) (let [x 99] x))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, weary from the morning's effort, agreed to try.

Write a form whose evaluation gives the inner-let value of x.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 10) (let [x 99] x))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (def x 10) (let [x 99] x) x)` • **expected**: `10`

**concept_phrase**: `the outer x after the inner let returns`

**question_what**: `the outer x after the let scope ends`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden notice nailed to a post in the farm carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (def x 10) (let [x 99] x) x)`. Lou
laughed, with great whoops of laughter, and declared it too easy to bother with.
Carol said, patiently, that the only way to be certain of
the outer x after the inner let returns was to put it in the REPL.

Question: write a Clojure expression for the outer x after the let scope ends.

---

I name the values first and then combine them.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 10) (let [x 99] x) x)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (def x 10) (let [x 99] x))` • **expected**: `99`

**concept_phrase**: `an inner let shadowing the outer def`

**question_what**: `the inner-let value of x`

```
The boy on the hill thought the trick clever the first time he played it.

A wooden notice nailed to a post at the edge of the farm carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (def x 10) (let [x 99] x))`. Jess
laughed, boasting at every turn, and declared it too easy to bother with.
Carol said, patiently, that the only way to be certain of
an inner let shadowing the outer def was to put it in the REPL.

What Clojure form computes the inner-let value of x? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 10) (let [x 99] x))"}}]}
```

---

## G3-06: let — binding can reference prior

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(let [a 5 b (* a 2)] b)` • **expected**: `10`

**concept_phrase**: `a let where b uses a`

**question_what**: `the value of b when a=5 and b is (* a 2)`

```
The boy on the hill thought the trick clever the first time he played it.

Frank kept a small ledger atop the hilltop where every meaningful
quantity in the village got its own labeled mark on the slate.
He pointed to today's entry: a let where b uses a. The form
`(let [a 5 b (* a 2)] b)` would settle it once Will agreed to look at
the binding rather than guess.

Write a Clojure expression that computes the value of b when a=5 and b is (* a 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 5 b (* a 2)] b)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(let [a 3 b (+ a 1) c (* b 2)] c)` • **expected**: `8`

**concept_phrase**: `a let with sequential bindings`

**question_what**: `the result of the chained binding c`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Halfway through the morning watch, Pat called out
near the woods, demanding a verdict on the form `(let [a 3 b (+ a 1) c (* b 2)] c)` and refusing
to descend until somebody confirmed it. Pat insisted
they already knew the answer. Robin, walking up
at an unhurried pace, simply said: "Submit a let with sequential bindings to the
REPL. Whatever comes back is the answer."

What Clojure form computes the result of the chained binding c? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 3 b (+ a 1) c (* b 2)] c)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(let [a 5 b (* a 2)] b)` • **expected**: `10`

**concept_phrase**: `a let where b uses a`

**question_what**: `the value of b when a=5 and b is (* a 2)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A wooden notice nailed to a post atop the hilltop carried a small puzzle. The
riddle simply asked the reader to evaluate `(let [a 5 b (* a 2)] b)`. Jess
laughed, as if the race were already won, and declared it too easy to bother with.
Morgan said, patiently, that the only way to be certain of
a let where b uses a was to put it in the REPL.

Question: write a Clojure expression for the value of b when a=5 and b is (* a 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 5 b (* a 2)] b)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(let [a 3 b (+ a 1) c (* b 2)] c)` • **expected**: `8`

**concept_phrase**: `a let with sequential bindings`

**question_what**: `the result of the chained binding c`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(let [a 3 b (+ a 1) c (* b 2)] c)`, and the line
above it read a let with sequential bindings. Robin handed the page to
Pat, who, lulled by the gentle wind, agreed to write it out properly.

Write a Clojure expression that computes the result of the chained binding c.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 3 b (+ a 1) c (* b 2)] c)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(let [a 5 b (* a 2)] b)` • **expected**: `10`

**concept_phrase**: `a let where b uses a`

**question_what**: `the value of b when a=5 and b is (* a 2)`

```
Every shepherd in the valley knew the danger of crying wolf for sport. It happened along the road.

A small slate sat on a flat stone near the road; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(let [a 5 b (* a 2)] b)`, and the page
heading read a let where b uses a. George nodded at Will to
write the form properly so the slate would carry an honest entry.

What Clojure form computes the value of b when a=5 and b is (* a 2)? Submit it via `eval`.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 5 b (* a 2)] b)"}}]}
```

---

## G3-07: fn — anonymous function

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `((fn [x] (+ x 1)) 4)` • **expected**: `5`

**concept_phrase**: `an anonymous function applied to 4`

**question_what**: `the result of applying (fn [x] (+ x 1)) to 4`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A small crowd of villagers had gathered by the woods to watch
Tom attempt to predict, off the cuff, what the REPL would
return. Robin pointed to an anonymous function applied to 4 and read out the
form aloud: `((fn [x] (+ x 1)) 4)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

What Clojure form computes the result of applying (fn [x] (+ x 1)) to 4? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] (+ x 1)) 4)"}}]}
```

### Record 2 — example 2 of 2

**form**: `((fn [a b] (* a b)) 3 4)` • **expected**: `12`

**concept_phrase**: `a two-arg anonymous function`

**question_what**: `the result of applying (fn [a b] (* a b)) to 3 and 4`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place near the meadow.

A wooden notice nailed to a post by the meadow carried a small puzzle. The
riddle simply asked the reader to evaluate `((fn [a b] (* a b)) 3 4)`. Jess
laughed, puffed up with pride, and declared it too easy to bother with.
Oliver said, patiently, that the only way to be certain of
a two-arg anonymous function was to put it in the REPL.

Write a Clojure expression that computes the result of applying (fn [a b] (* a b)) to 3 and 4.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [a b] (* a b)) 3 4)"}}]}
```

### Record 3 — example 1 of 2

**form**: `((fn [x] (+ x 1)) 4)` • **expected**: `5`

**concept_phrase**: `an anonymous function applied to 4`

**question_what**: `the result of applying (fn [x] (+ x 1)) to 4`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place on the hilltop.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `((fn [x] (+ x 1)) 4)`, and the line
above it read an anonymous function applied to 4. Oliver handed the page to
Will, who, her legs heavy from sprinting, agreed to write it out properly.

What Clojure form computes the result of applying (fn [x] (+ x 1)) to 4? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] (+ x 1)) 4)"}}]}
```

### Record 4 — example 2 of 2

**form**: `((fn [a b] (* a b)) 3 4)` • **expected**: `12`

**concept_phrase**: `a two-arg anonymous function`

**question_what**: `the result of applying (fn [a b] (* a b)) to 3 and 4`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Halfway through the morning watch, Tom called out
in the orchard, demanding a verdict on the form `((fn [a b] (* a b)) 3 4)` and refusing
to descend until somebody confirmed it. Tom insisted
he already knew the answer. Alex, walking up
at an unhurried pace, simply said: "Submit a two-arg anonymous function to the
REPL. Whatever comes back is the answer."

Write a Clojure expression that computes the result of applying (fn [a b] (* a b)) to 3 and 4.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [a b] (* a b)) 3 4)"}}]}
```

### Record 5 — example 1 of 2

**form**: `((fn [x] (+ x 1)) 4)` • **expected**: `5`

**concept_phrase**: `an anonymous function applied to 4`

**question_what**: `the result of applying (fn [x] (+ x 1)) to 4`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A small slate sat on a flat stone near the farm; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `((fn [x] (+ x 1)) 4)`, and the page
heading read an anonymous function applied to 4. George nodded at Jess to
write the form properly so the slate would carry an honest entry.

What Clojure form computes the result of applying (fn [x] (+ x 1)) to 4? Submit it via `eval`.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] (+ x 1)) 4)"}}]}
```

---

## G3-08: fn — multi-arg

**Examples:** 1 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 1

**form**: `((fn [a b c] (+ a b c)) 1 2 3)` • **expected**: `6`

**concept_phrase**: `a three-arg anonymous function`

**question_what**: `the sum of a, b, c`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened near the orchard.

Oliver kept a small ledger in the orchard where every meaningful
quantity in the village got its own labeled mark on the slate.
He pointed to today's entry: a three-arg anonymous function. The form
`((fn [a b c] (+ a b c)) 1 2 3)` would settle it once Tom agreed to look at
the binding rather than guess.

Write a form whose evaluation gives the sum of a, b, c.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [a b c] (+ a b c)) 1 2 3)"}}]}
```

### Record 2 — example 1 of 1

**form**: `((fn [a b c] (+ a b c)) 1 2 3)` • **expected**: `6`

**concept_phrase**: `a three-arg anonymous function`

**question_what**: `the sum of a, b, c`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Halfway through the morning watch, Tom called out
at the edge of the village, demanding a verdict on the form `((fn [a b c] (+ a b c)) 1 2 3)` and refusing
to descend until somebody confirmed it. Tom insisted
he already knew the answer. Oliver, walking up
at an unhurried pace, simply said: "Submit a three-arg anonymous function to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the sum of a, b, c.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [a b c] (+ a b c)) 1 2 3)"}}]}
```

### Record 3 — example 1 of 1

**form**: `((fn [a b c] (+ a b c)) 1 2 3)` • **expected**: `6`

**concept_phrase**: `a three-arg anonymous function`

**question_what**: `the sum of a, b, c`

```
The boy on the hill thought the trick clever the first time he played it. It happened at the edge of the farm.

A wooden notice nailed to a post near the farm carried a small puzzle. The
riddle simply asked the reader to evaluate `((fn [a b c] (+ a b c)) 1 2 3)`. Will
laughed, as if the race were already won, and declared it too easy to bother with.
Grace said, patiently, that the only way to be certain of
a three-arg anonymous function was to put it in the REPL.

Write a Clojure expression that computes the sum of a, b, c.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [a b c] (+ a b c)) 1 2 3)"}}]}
```

### Record 4 — example 1 of 1

**form**: `((fn [a b c] (+ a b c)) 1 2 3)` • **expected**: `6`

**concept_phrase**: `a three-arg anonymous function`

**question_what**: `the sum of a, b, c`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Sam had been trying to teach Lou how the REPL
works. "Look here," they said, pointing to a three-arg anonymous function.
"You hand the form `((fn [a b c] (+ a b c)) 1 2 3)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Lou, drowsy from the warm sun, agreed to try.

Write a Clojure expression that computes the sum of a, b, c.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [a b c] (+ a b c)) 1 2 3)"}}]}
```

### Record 5 — example 1 of 1

**form**: `((fn [a b c] (+ a b c)) 1 2 3)` • **expected**: `6`

**concept_phrase**: `a three-arg anonymous function`

**question_what**: `the sum of a, b, c`

```
The boy on the hill thought the trick clever the first time he played it.

"There is no need to evaluate that," Pat said, with great whoops of laughter.
"Anyone can see what a three-arg anonymous function comes to." Oliver, who
by the orchard had heard such claims many times, asked them to
actually write the form `((fn [a b c] (+ a b c)) 1 2 3)` and submit it to the REPL —
just to be sure.

Write a Clojure expression that computes the sum of a, b, c.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [a b c] (+ a b c)) 1 2 3)"}}]}
```

---

## G3-09: defn — shorthand

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do (defn dbl [x] (* x 2)) (dbl 5))` • **expected**: `10`

**concept_phrase**: `a defn that doubles its argument`

**question_what**: `the doubled value (dbl 5)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place in the woods.

Halfway through the morning watch, Will called out
at the edge of the woods, demanding a verdict on the form `(do (defn dbl [x] (* x 2)) (dbl 5))` and refusing
to descend until somebody confirmed it. Will insisted
he already knew the answer. George, walking up
at an unhurried pace, simply said: "Submit a defn that doubles its argument to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the doubled value (dbl 5).

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn dbl [x] (* x 2)) (dbl 5))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` • **expected**: `6`

**concept_phrase**: `a defn with three args`

**question_what**: `the result of (add3 1 2 3)`

```
The boy on the hill thought the trick clever the first time he played it.

"There is no need to evaluate that," Pat said, swaggering through the underbrush.
"Anyone can see what a defn with three args comes to." Alice, who
by the forest had heard such claims many times, asked them to
actually write the form `(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` and submit it to the REPL —
just to be sure.

Write a form whose evaluation gives the result of (add3 1 2 3).

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (defn dbl [x] (* x 2)) (dbl 5))` • **expected**: `10`

**concept_phrase**: `a defn that doubles its argument`

**question_what**: `the doubled value (dbl 5)`

```
The boy on the hill thought the trick clever the first time he played it.

"You can call it whatever you like," Morgan said in the orchard, "but the
form is what matters." They drew the binding for
Jess: the form `(do (defn dbl [x] (* x 2)) (dbl 5))` captured a defn that doubles its argument,
and the REPL would do the rest — no claims required, just the
runtime's answer.

Write a Clojure expression that computes the doubled value (dbl 5).

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn dbl [x] (* x 2)) (dbl 5))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` • **expected**: `6`

**concept_phrase**: `a defn with three args`

**question_what**: `the result of (add3 1 2 3)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Halfway through the morning watch, Pat called out
at the edge of the woods, demanding a verdict on the form `(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` and refusing
to descend until somebody confirmed it. Pat insisted
they already knew the answer. Carol, walking up
at an unhurried pace, simply said: "Submit a defn with three args to the
REPL. Whatever comes back is the answer."

Write a form whose evaluation gives the result of (add3 1 2 3).

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (defn dbl [x] (* x 2)) (dbl 5))` • **expected**: `10`

**concept_phrase**: `a defn that doubles its argument`

**question_what**: `the doubled value (dbl 5)`

```
The boy on the hill thought the trick clever the first time he played it.

A small crowd of villagers had gathered by the woods to watch
Tom attempt to predict, off the cuff, what the REPL would
return. George pointed to a defn that doubles its argument and read out the
form aloud: `(do (defn dbl [x] (* x 2)) (dbl 5))`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Question: write a Clojure expression for the doubled value (dbl 5).

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn dbl [x] (* x 2)) (dbl 5))"}}]}
```

---

## G3-10: anonymous shorthand #()

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(#(+ % 1) 5)` • **expected**: `6`

**concept_phrase**: `the shorthand #(+ % 1) applied to 5`

**question_what**: `the result of (#(+ % 1) 5)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Lou called down from a stone atop the hilltop where someone had
chalked the shorthand #(+ % 1) applied to 5 on a flat board. Lou, boasting at every turn,
declared she already knew what would come back. Grace,
with steady, careful steps, asked her to actually submit the form
`(#(+ % 1) 5)` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the result of (#(+ % 1) 5).

---

{"tool_calls":[{"name":"eval","args":{"form":"(#(+ % 1) 5)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(#(* %1 %2) 3 4)` • **expected**: `12`

**concept_phrase**: `the shorthand #(* %1 %2) applied to 3 and 4`

**question_what**: `the result of (#(* %1 %2) 3 4)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. This was near the orchard.

"There is no need to evaluate that," Pat said, with a smug grin.
"Anyone can see what the shorthand #(* %1 %2) applied to 3 and 4 comes to." Carol, who
near the orchard had heard such claims many times, asked them to
actually write the form `(#(* %1 %2) 3 4)` and submit it to the REPL —
just to be sure.

Question: write a Clojure expression for the result of (#(* %1 %2) 3 4).

---

{"tool_calls":[{"name":"eval","args":{"form":"(#(* %1 %2) 3 4)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(#(+ % 1) 5)` • **expected**: `6`

**concept_phrase**: `the shorthand #(+ % 1) applied to 5`

**question_what**: `the result of (#(+ % 1) 5)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Alice had been trying to teach Tom how the REPL
works. "Look here," she said, pointing to the shorthand #(+ % 1) applied to 5.
"You hand the form `(#(+ % 1) 5)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Tom, drowsy from the warm sun, agreed to try.

What Clojure form computes the result of (#(+ % 1) 5)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(#(+ % 1) 5)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(#(* %1 %2) 3 4)` • **expected**: `12`

**concept_phrase**: `the shorthand #(* %1 %2) applied to 3 and 4`

**question_what**: `the result of (#(* %1 %2) 3 4)`

```
The boy on the hill thought the trick clever the first time he played it. This was along the road.

"You can call it whatever you like," Alice said along the road, "but the
form is what matters." She drew the binding for
Tom: the form `(#(* %1 %2) 3 4)` captured the shorthand #(* %1 %2) applied to 3 and 4,
and the REPL would do the rest — no claims required, just the
runtime's answer.

Question: write a Clojure expression for the result of (#(* %1 %2) 3 4).

---

{"tool_calls":[{"name":"eval","args":{"form":"(#(* %1 %2) 3 4)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(#(+ % 1) 5)` • **expected**: `6`

**concept_phrase**: `the shorthand #(+ % 1) applied to 5`

**question_what**: `the result of (#(+ % 1) 5)`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

"You can call it whatever you like," Robin said by the farm, "but the
form is what matters." They drew the binding for
Tom: the form `(#(+ % 1) 5)` captured the shorthand #(+ % 1) applied to 5,
and the REPL would do the rest — no claims required, just the
runtime's answer.

Write a form whose evaluation gives the result of (#(+ % 1) 5).

---

{"tool_calls":[{"name":"eval","args":{"form":"(#(+ % 1) 5)"}}]}
```

---

## G3-11: Substitution rule

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(let [a 7] (+ a a))` • **expected**: `14`

**concept_phrase**: `the let where a is referenced twice`

**question_what**: `the result of (+ a a) when a=7`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened in the meadow.

Halfway through the morning watch, Will called out
in the meadow, demanding a verdict on the form `(let [a 7] (+ a a))` and refusing
to descend until somebody confirmed it. Will insisted
he already knew the answer. Bob, walking up
at an unhurried pace, simply said: "Submit the let where a is referenced twice to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the result of (+ a a) when a=7.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 7] (+ a a))"}}]}
```

### Record 2 — example 2 of 2

**form**: `((fn [x] (* x x)) 6)` • **expected**: `36`

**concept_phrase**: `applying square to 6`

**question_what**: `the square of 6`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place near the road.

A small slate sat on a flat stone near the road; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `((fn [x] (* x x)) 6)`, and the page
heading read applying square to 6. Sam nodded at Jess to
write the form properly so the slate would carry an honest entry.

Write a Clojure expression that computes the square of 6.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] (* x x)) 6)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(let [a 7] (+ a a))` • **expected**: `14`

**concept_phrase**: `the let where a is referenced twice`

**question_what**: `the result of (+ a a) when a=7`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A wooden notice nailed to a post in the village carried a small puzzle. The
riddle simply asked the reader to evaluate `(let [a 7] (+ a a))`. Will
laughed, with great whoops of laughter, and declared it too easy to bother with.
Alex said, patiently, that the only way to be certain of
the let where a is referenced twice was to put it in the REPL.

Write a Clojure expression that computes the result of (+ a a) when a=7.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 7] (+ a a))"}}]}
```

### Record 4 — example 2 of 2

**form**: `((fn [x] (* x x)) 6)` • **expected**: `36`

**concept_phrase**: `applying square to 6`

**question_what**: `the square of 6`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. This was on the road.

"There is no need to evaluate that," Lou said, with great whoops of laughter.
"Anyone can see what applying square to 6 comes to." George, who
on the road had heard such claims many times, asked her to
actually write the form `((fn [x] (* x x)) 6)` and submit it to the REPL —
just to be sure.

What Clojure form computes the square of 6? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] (* x x)) 6)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(let [a 7] (+ a a))` • **expected**: `14`

**concept_phrase**: `the let where a is referenced twice`

**question_what**: `the result of (+ a a) when a=7`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place by the orchard.

A small crowd of villagers had gathered near the orchard to watch
Lou attempt to predict, off the cuff, what the REPL would
return. Carol pointed to the let where a is referenced twice and read out the
form aloud: `(let [a 7] (+ a a))`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a form whose evaluation gives the result of (+ a a) when a=7.

---

I bind the inputs in a let, then compute.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 7] (+ a a))"}}]}
```

---

## G3-12: Scope vs namespace

**Examples:** 1 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 1

**form**: `(do (def g 5) (let [g 99] (+ g 1)))` • **expected**: `100`

**concept_phrase**: `an inner let masking the outer def g`

**question_what**: `the value computed inside the inner scope`

```
The boy on the hill thought the trick clever the first time he played it. This was near the orchard.

Grace kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the orchard the next entry was
an inner let masking the outer def g. Jess peered over her shoulder
at the form `(do (def g 5) (let [g 99] (+ g 1)))` and was asked, gently, to be the one to
submit it.

Write a Clojure expression that computes the value computed inside the inner scope.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def g 5) (let [g 99] (+ g 1)))"}}]}
```

### Record 2 — example 1 of 1

**form**: `(do (def g 5) (let [g 99] (+ g 1)))` • **expected**: `100`

**concept_phrase**: `an inner let masking the outer def g`

**question_what**: `the value computed inside the inner scope`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

"There is no need to evaluate that," Pat said, swaggering through the underbrush.
"Anyone can see what an inner let masking the outer def g comes to." Alex, who
along the road had heard such claims many times, asked them to
actually write the form `(do (def g 5) (let [g 99] (+ g 1)))` and submit it to the REPL —
just to be sure.

Question: write a Clojure expression for the value computed inside the inner scope.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def g 5) (let [g 99] (+ g 1)))"}}]}
```

### Record 3 — example 1 of 1

**form**: `(do (def g 5) (let [g 99] (+ g 1)))` • **expected**: `100`

**concept_phrase**: `an inner let masking the outer def g`

**question_what**: `the value computed inside the inner scope`

```
The boy on the hill thought the trick clever the first time he played it. It happened along the road.

The elder of the village kept a small slate near the road, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was an inner let masking the outer def g. George read
out the form `(do (def g 5) (let [g 99] (+ g 1)))` so Tom could write it
properly into the REPL and earn an honest mark on the slate.

What Clojure form computes the value computed inside the inner scope? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def g 5) (let [g 99] (+ g 1)))"}}]}
```

### Record 4 — example 1 of 1

**form**: `(do (def g 5) (let [g 99] (+ g 1)))` • **expected**: `100`

**concept_phrase**: `an inner let masking the outer def g`

**question_what**: `the value computed inside the inner scope`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened at the edge of the orchard.

Lou called down from a stone at the edge of the orchard where someone had
chalked an inner let masking the outer def g on a flat board. Lou, puffed up with pride,
declared she already knew what would come back. Morgan,
saying very little, asked her to actually submit the form
`(do (def g 5) (let [g 99] (+ g 1)))` to the REPL — the village had stopped trusting answers
that weren't checked.

Question: write a Clojure expression for the value computed inside the inner scope.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def g 5) (let [g 99] (+ g 1)))"}}]}
```

### Record 5 — example 1 of 1

**form**: `(do (def g 5) (let [g 99] (+ g 1)))` • **expected**: `100`

**concept_phrase**: `an inner let masking the outer def g`

**question_what**: `the value computed inside the inner scope`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

"You can call it whatever you like," Oliver said in the farm, "but the
form is what matters." He drew the binding for
Tom: the form `(do (def g 5) (let [g 99] (+ g 1)))` captured an inner let masking the outer def g,
and the REPL would do the rest — no claims required, just the
runtime's answer.

What Clojure form computes the value computed inside the inner scope? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def g 5) (let [g 99] (+ g 1)))"}}]}
```

---

## G3-13: fn body returns last form

**Examples:** 1 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 1

**form**: `((fn [x] x x x 99) 1)` • **expected**: `99`

**concept_phrase**: `a fn whose body has multiple forms; only the last is returned`

**question_what**: `the value of a fn body that ends with 99`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden notice nailed to a post at the edge of the woods carried a small puzzle. The
riddle simply asked the reader to evaluate `((fn [x] x x x 99) 1)`. Pat
laughed, with great whoops of laughter, and declared it too easy to bother with.
Sam said, patiently, that the only way to be certain of
a fn whose body has multiple forms; only the last is returned was to put it in the REPL.

Write a Clojure expression that computes the value of a fn body that ends with 99.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] x x x 99) 1)"}}]}
```

### Record 2 — example 1 of 1

**form**: `((fn [x] x x x 99) 1)` • **expected**: `99`

**concept_phrase**: `a fn whose body has multiple forms; only the last is returned`

**question_what**: `the value of a fn body that ends with 99`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A small crowd of villagers had gathered in the village to watch
Pat attempt to predict, off the cuff, what the REPL would
return. Morgan pointed to a fn whose body has multiple forms; only the last is returned and read out the
form aloud: `((fn [x] x x x 99) 1)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

What Clojure form computes the value of a fn body that ends with 99? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] x x x 99) 1)"}}]}
```

### Record 3 — example 1 of 1

**form**: `((fn [x] x x x 99) 1)` • **expected**: `99`

**concept_phrase**: `a fn whose body has multiple forms; only the last is returned`

**question_what**: `the value of a fn body that ends with 99`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened at the edge of the farm.

Bob had been trying to teach Tom how the REPL
works. "Look here," he said, pointing to a fn whose body has multiple forms; only the last is returned.
"You hand the form `((fn [x] x x x 99) 1)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Tom, drowsy from the warm sun, agreed to try.

What Clojure form computes the value of a fn body that ends with 99? Submit it via `eval`.

---

I write the let-form so the REPL can substitute.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] x x x 99) 1)"}}]}
```

### Record 4 — example 1 of 1

**form**: `((fn [x] x x x 99) 1)` • **expected**: `99`

**concept_phrase**: `a fn whose body has multiple forms; only the last is returned`

**question_what**: `the value of a fn body that ends with 99`

```
The boy on the hill thought the trick clever the first time he played it.

Oliver had been trying to teach Will how the REPL
works. "Look here," he said, pointing to a fn whose body has multiple forms; only the last is returned.
"You hand the form `((fn [x] x x x 99) 1)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Will, weary from the morning's effort, agreed to try.

Question: write a Clojure expression for the value of a fn body that ends with 99.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] x x x 99) 1)"}}]}
```

### Record 5 — example 1 of 1

**form**: `((fn [x] x x x 99) 1)` • **expected**: `99`

**concept_phrase**: `a fn whose body has multiple forms; only the last is returned`

**question_what**: `the value of a fn body that ends with 99`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Lou called down from a stone near the woods where someone had
chalked a fn whose body has multiple forms; only the last is returned on a flat board. Lou, boasting at every turn,
declared she already knew what would come back. Alex,
stepping deliberately, asked her to actually submit the form
`((fn [x] x x x 99) 1)` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the value of a fn body that ends with 99.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] x x x 99) 1)"}}]}
```

---

## G3-14: do form

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do 1 2 3)` • **expected**: `3`

**concept_phrase**: `the do form (do 1 2 3)`

**question_what**: `the value of (do 1 2 3)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Carol had been trying to teach Jess how the REPL
works. "Look here," she said, pointing to the do form (do 1 2 3).
"You hand the form `(do 1 2 3)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, lulled by the gentle wind, agreed to try.

Question: write a Clojure expression for the value of (do 1 2 3).

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do 1 2 3)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (+ 1 1) (+ 2 2) (+ 3 3))` • **expected**: `6`

**concept_phrase**: `a do with three forms — last wins`

**question_what**: `the value of (do (+ 1 1) (+ 2 2) (+ 3 3))`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. This was along the road.

A wooden notice nailed to a post along the road carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (+ 1 1) (+ 2 2) (+ 3 3))`. Pat
laughed, with a smug grin, and declared it too easy to bother with.
Grace said, patiently, that the only way to be certain of
a do with three forms — last wins was to put it in the REPL.

Question: write a Clojure expression for the value of (do (+ 1 1) (+ 2 2) (+ 3 3)).

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (+ 1 1) (+ 2 2) (+ 3 3))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do 1 2 3)` • **expected**: `3`

**concept_phrase**: `the do form (do 1 2 3)`

**question_what**: `the value of (do 1 2 3)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Morgan had been trying to teach Will how the REPL
works. "Look here," they said, pointing to the do form (do 1 2 3).
"You hand the form `(do 1 2 3)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Will, yawning at the soft moss, agreed to try.

Question: write a Clojure expression for the value of (do 1 2 3).

---

{"tool_calls":[{"name":"eval","args":{"form":"(do 1 2 3)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (+ 1 1) (+ 2 2) (+ 3 3))` • **expected**: `6`

**concept_phrase**: `a do with three forms — last wins`

**question_what**: `the value of (do (+ 1 1) (+ 2 2) (+ 3 3))`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

"There is no need to evaluate that," Tom said, with a smug grin.
"Anyone can see what a do with three forms — last wins comes to." Alice, who
at the edge of the farm had heard such claims many times, asked him to
actually write the form `(do (+ 1 1) (+ 2 2) (+ 3 3))` and submit it to the REPL —
just to be sure.

Write a Clojure expression that computes the value of (do (+ 1 1) (+ 2 2) (+ 3 3)).

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (+ 1 1) (+ 2 2) (+ 3 3))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do 1 2 3)` • **expected**: `3`

**concept_phrase**: `the do form (do 1 2 3)`

**question_what**: `the value of (do 1 2 3)`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Halfway through the morning watch, Jess called out
near the woods, demanding a verdict on the form `(do 1 2 3)` and refusing
to descend until somebody confirmed it. Jess insisted
she already knew the answer. Grace, walking up
at an unhurried pace, simply said: "Submit the do form (do 1 2 3) to the
REPL. Whatever comes back is the answer."

What Clojure form computes the value of (do 1 2 3)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do 1 2 3)"}}]}
```

---

## G3-15: Side-effects in body

**Examples:** 1 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 1

**form**: `(do (println "hi") 42)` • **expected**: `42`

**concept_phrase**: `the form (do (println "hi") 42)`

**question_what**: `the return value of the do`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Grace kept a small ledger near the meadow where every meaningful
quantity in the village got its own labeled mark on the slate.
She pointed to today's entry: the form (do (println "hi") 42). The form
`(do (println "hi") 42)` would settle it once Lou agreed to look at
the binding rather than guess.

What Clojure form computes the return value of the do? Submit it via `eval`.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (println \"hi\") 42)"}}]}
```

### Record 2 — example 1 of 1

**form**: `(do (println "hi") 42)` • **expected**: `42`

**concept_phrase**: `the form (do (println "hi") 42)`

**question_what**: `the return value of the do`

```
Every shepherd in the valley knew the danger of crying wolf for sport. This was near the meadow.

A wooden notice nailed to a post at the edge of the meadow carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (println "hi") 42)`. Jess
laughed, swaggering through the underbrush, and declared it too easy to bother with.
Robin said, patiently, that the only way to be certain of
the form (do (println "hi") 42) was to put it in the REPL.

Question: write a Clojure expression for the return value of the do.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do (println \"hi\") 42)"}}]}
```

### Record 3 — example 1 of 1

**form**: `(do (println "hi") 42)` • **expected**: `42`

**concept_phrase**: `the form (do (println "hi") 42)`

**question_what**: `the return value of the do`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A wooden notice nailed to a post near the orchard carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (println "hi") 42)`. Lou
laughed, boasting at every turn, and declared it too easy to bother with.
George said, patiently, that the only way to be certain of
the form (do (println "hi") 42) was to put it in the REPL.

Write a Clojure expression that computes the return value of the do.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (println \"hi\") 42)"}}]}
```

### Record 4 — example 1 of 1

**form**: `(do (println "hi") 42)` • **expected**: `42`

**concept_phrase**: `the form (do (println "hi") 42)`

**question_what**: `the return value of the do`

```
The boy on the hill thought the trick clever the first time he played it. This was near the village.

"You can call it whatever you like," Sam said in the village, "but the
form is what matters." They drew the binding for
Tom: the form `(do (println "hi") 42)` captured the form (do (println "hi") 42),
and the REPL would do the rest — no claims required, just the
runtime's answer.

Write a form whose evaluation gives the return value of the do.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (println \"hi\") 42)"}}]}
```

### Record 5 — example 1 of 1

**form**: `(do (println "hi") 42)` • **expected**: `42`

**concept_phrase**: `the form (do (println "hi") 42)`

**question_what**: `the return value of the do`

```
The boy on the hill thought the trick clever the first time he played it. All this took place in the village.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(do (println "hi") 42)`, and the line
above it read the form (do (println "hi") 42). Carol handed the page to
Jess, who, her legs heavy from sprinting, agreed to write it out properly.

Write a Clojure expression that computes the return value of the do.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (println \"hi\") 42)"}}]}
```

---

## G3-16: Name collision: namespace vs let

**Examples:** 1 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 1

**form**: `(let [+ 99] +)` • **expected**: `99`

**concept_phrase**: `a let that shadows the + function`

**question_what**: `the value bound to the (locally shadowed) +`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Halfway through the morning watch, Pat called out
by the orchard, demanding a verdict on the form `(let [+ 99] +)` and refusing
to descend until somebody confirmed it. Pat insisted
they already knew the answer. Sam, walking up
at an unhurried pace, simply said: "Submit a let that shadows the + function to the
REPL. Whatever comes back is the answer."

Write a form whose evaluation gives the value bound to the (locally shadowed) +.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [+ 99] +)"}}]}
```

### Record 2 — example 1 of 1

**form**: `(let [+ 99] +)` • **expected**: `99`

**concept_phrase**: `a let that shadows the + function`

**question_what**: `the value bound to the (locally shadowed) +`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened near the woods.

Halfway through the morning watch, Will called out
at the edge of the woods, demanding a verdict on the form `(let [+ 99] +)` and refusing
to descend until somebody confirmed it. Will insisted
he already knew the answer. George, walking up
at an unhurried pace, simply said: "Submit a let that shadows the + function to the
REPL. Whatever comes back is the answer."

Write a Clojure expression that computes the value bound to the (locally shadowed) +.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(let [+ 99] +)"}}]}
```

### Record 3 — example 1 of 1

**form**: `(let [+ 99] +)` • **expected**: `99`

**concept_phrase**: `a let that shadows the + function`

**question_what**: `the value bound to the (locally shadowed) +`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A wooden notice nailed to a post in the farm carried a small puzzle. The
riddle simply asked the reader to evaluate `(let [+ 99] +)`. Pat
laughed, puffed up with pride, and declared it too easy to bother with.
Bob said, patiently, that the only way to be certain of
a let that shadows the + function was to put it in the REPL.

Question: write a Clojure expression for the value bound to the (locally shadowed) +.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [+ 99] +)"}}]}
```

### Record 4 — example 1 of 1

**form**: `(let [+ 99] +)` • **expected**: `99`

**concept_phrase**: `a let that shadows the + function`

**question_what**: `the value bound to the (locally shadowed) +`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A small crowd of villagers had gathered near the forest to watch
Tom attempt to predict, off the cuff, what the REPL would
return. Sam pointed to a let that shadows the + function and read out the
form aloud: `(let [+ 99] +)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a form whose evaluation gives the value bound to the (locally shadowed) +.

---

I write the let-form so the REPL can substitute.

{"tool_calls":[{"name":"eval","args":{"form":"(let [+ 99] +)"}}]}
```

### Record 5 — example 1 of 1

**form**: `(let [+ 99] +)` • **expected**: `99`

**concept_phrase**: `a let that shadows the + function`

**question_what**: `the value bound to the (locally shadowed) +`

```
The boy on the hill thought the trick clever the first time he played it. This was by the orchard.

Frank kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today at the edge of the orchard the next entry was
a let that shadows the + function. Pat peered over his shoulder
at the form `(let [+ 99] +)` and was asked, gently, to be the one to
submit it.

Write a form whose evaluation gives the value bound to the (locally shadowed) +.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(let [+ 99] +)"}}]}
```

---

## G3-17: Naming conventions (kebab-case)

**Examples:** 1 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 1

**form**: `(let [flock-size 8 stray-count 2] (- flock-size stray-count))` • **expected**: `6`

**concept_phrase**: `a let with kebab-case names`

**question_what**: `the difference of the two counts`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place by the forest.

"There is no need to evaluate that," Will said, with a smug grin.
"Anyone can see what a let with kebab-case names comes to." Grace, who
in the forest had heard such claims many times, asked him to
actually write the form `(let [flock-size 8 stray-count 2] (- flock-size stray-count))` and submit it to the REPL —
just to be sure.

Question: write a Clojure expression for the difference of the two counts.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [flock-size 8 stray-count 2] (- flock-size stray-count))"}}]}
```

### Record 2 — example 1 of 1

**form**: `(let [flock-size 8 stray-count 2] (- flock-size stray-count))` • **expected**: `6`

**concept_phrase**: `a let with kebab-case names`

**question_what**: `the difference of the two counts`

```
Every shepherd in the valley knew the danger of crying wolf for sport. It happened near the village.

A small slate sat on a flat stone at the edge of the village; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(let [flock-size 8 stray-count 2] (- flock-size stray-count))`, and the page
heading read a let with kebab-case names. Frank nodded at Pat to
write the form properly so the slate would carry an honest entry.

Write a form whose evaluation gives the difference of the two counts.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(let [flock-size 8 stray-count 2] (- flock-size stray-count))"}}]}
```

### Record 3 — example 1 of 1

**form**: `(let [flock-size 8 stray-count 2] (- flock-size stray-count))` • **expected**: `6`

**concept_phrase**: `a let with kebab-case names`

**question_what**: `the difference of the two counts`

```
The boy on the hill thought the trick clever the first time he played it.

The elder of the village kept a small slate at the edge of the meadow, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was a let with kebab-case names. Carol read
out the form `(let [flock-size 8 stray-count 2] (- flock-size stray-count))` so Tom could write it
properly into the REPL and earn an honest mark on the slate.

Question: write a Clojure expression for the difference of the two counts.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(let [flock-size 8 stray-count 2] (- flock-size stray-count))"}}]}
```

### Record 4 — example 1 of 1

**form**: `(let [flock-size 8 stray-count 2] (- flock-size stray-count))` • **expected**: `6`

**concept_phrase**: `a let with kebab-case names`

**question_what**: `the difference of the two counts`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened at the edge of the forest.

Carol had been trying to teach Jess how the REPL
works. "Look here," she said, pointing to a let with kebab-case names.
"You hand the form `(let [flock-size 8 stray-count 2] (- flock-size stray-count))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, lulled by the gentle wind, agreed to try.

Write a form whose evaluation gives the difference of the two counts.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [flock-size 8 stray-count 2] (- flock-size stray-count))"}}]}
```

### Record 5 — example 1 of 1

**form**: `(let [flock-size 8 stray-count 2] (- flock-size stray-count))` • **expected**: `6`

**concept_phrase**: `a let with kebab-case names`

**question_what**: `the difference of the two counts`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden notice nailed to a post by the woods carried a small puzzle. The
riddle simply asked the reader to evaluate `(let [flock-size 8 stray-count 2] (- flock-size stray-count))`. Pat
laughed, swaggering through the underbrush, and declared it too easy to bother with.
Morgan said, patiently, that the only way to be certain of
a let with kebab-case names was to put it in the REPL.

Write a Clojure expression that computes the difference of the two counts.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(let [flock-size 8 stray-count 2] (- flock-size stray-count))"}}]}
```

---

## G3-18: When to name vs inline

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(let [n 5] (* n n n))` • **expected**: `125`

**concept_phrase**: `naming n once and using it three times`

**question_what**: `n cubed where n=5`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A small crowd of villagers had gathered near the meadow to watch
Pat attempt to predict, off the cuff, what the REPL would
return. Alice pointed to naming n once and using it three times and read out the
form aloud: `(let [n 5] (* n n n))`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a Clojure expression that computes n cubed where n=5.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(let [n 5] (* n n n))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(* 5 5 5)` • **expected**: `125`

**concept_phrase**: `the inline form (* 5 5 5)`

**question_what**: `5 cubed (without binding)`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Robin had been trying to teach Jess how the REPL
works. "Look here," they said, pointing to the inline form (* 5 5 5).
"You hand the form `(* 5 5 5)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, weary from the morning's effort, agreed to try.

Write a Clojure expression that computes 5 cubed (without binding).

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 5 5 5)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(let [n 5] (* n n n))` • **expected**: `125`

**concept_phrase**: `naming n once and using it three times`

**question_what**: `n cubed where n=5`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Sam kept a small ledger near the road where every meaningful
quantity in the village got its own labeled mark on the slate.
They pointed to today's entry: naming n once and using it three times. The form
`(let [n 5] (* n n n))` would settle it once Lou agreed to look at
the binding rather than guess.

Write a form whose evaluation gives n cubed where n=5.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(let [n 5] (* n n n))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(* 5 5 5)` • **expected**: `125`

**concept_phrase**: `the inline form (* 5 5 5)`

**question_what**: `5 cubed (without binding)`

```
The boy on the hill thought the trick clever the first time he played it. All this took place near the meadow.

A small crowd of villagers had gathered near the meadow to watch
Will attempt to predict, off the cuff, what the REPL would
return. Oliver pointed to the inline form (* 5 5 5) and read out the
form aloud: `(* 5 5 5)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a form whose evaluation gives 5 cubed (without binding).

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 5 5 5)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(let [n 5] (* n n n))` • **expected**: `125`

**concept_phrase**: `naming n once and using it three times`

**question_what**: `n cubed where n=5`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A wooden notice nailed to a post by the village carried a small puzzle. The
riddle simply asked the reader to evaluate `(let [n 5] (* n n n))`. Lou
laughed, with great whoops of laughter, and declared it too easy to bother with.
Sam said, patiently, that the only way to be certain of
naming n once and using it three times was to put it in the REPL.

Write a Clojure expression that computes n cubed where n=5.

---

I name the values first and then combine them.

{"tool_calls":[{"name":"eval","args":{"form":"(let [n 5] (* n n n))"}}]}
```

---

