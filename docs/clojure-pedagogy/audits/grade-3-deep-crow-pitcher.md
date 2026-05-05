# crow-pitcher grade 3 — deep spot-check

5 records per subject for hand-audit.

---

## G3-01: def — top-level binding

### G3-01 record 1  •  form `(do (def x 42) x)`  •  expected `42`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A small audience of sparrows had gathered by the farm to watch
Caw the crow attempt to outwit Sable the crow at the rim of an old
pitcher. Sable pointed to the binding (def x 42) followed by x and read out the form
aloud: `(do (def x 42) x)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a Clojure expression that computes the value bound to x after (def x 42).

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 42) x)"}}]}
```

### G3-01 record 2  •  form `(do (def y 7) y)`  •  expected `7`

```
Hunger and thirst had driven the Crow far from her usual perch.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust near the meadow: whoever guessed the result of `(do (def y 7) y)`
first would win the right to claim the next clear water they found.
Caw the crow, stepping deliberately, said it was easier to ask the REPL
about the binding (def y 7) than to argue.

What Clojure form computes the value bound to y? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def y 7) y)"}}]}
```

### G3-01 record 3  •  form `(do (def x 42) x)`  •  expected `42`

```
Hunger and thirst had driven the Crow far from her usual perch.

Sable the crow had been keeping a small leather notebook of every form
they had successfully dropped into the REPL — one entry per
stone, one rise per form. Today at the edge of the market, the next entry was
the binding (def x 42) followed by x. Caw the crow peered over their shoulder
at the form `(do (def x 42) x)` and asked what it would come out to.

Question: write a Clojure expression for the value bound to x after (def x 42).

---

I name the values first and then combine them.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 42) x)"}}]}
```

### G3-01 record 4  •  form `(do (def y 7) y)`  •  expected `7`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened at the edge of the market.

Caw the crow had been keeping a small leather notebook of every form
she had successfully dropped into the REPL — one entry per
stone, one rise per form. Today at the edge of the market, the next entry was
the binding (def y 7). Korvus the crow peered over her shoulder
at the form `(do (def y 7) y)` and asked what it would come out to.

Write a form whose evaluation gives the value bound to y.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def y 7) y)"}}]}
```

### G3-01 record 5  •  form `(do (def x 42) x)`  •  expected `42`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened on the hilltop.

Sable the crow had been keeping a small leather notebook of every form
they had successfully dropped into the REPL — one entry per
stone, one rise per form. Today at the edge of the hilltop, the next entry was
the binding (def x 42) followed by x. Caw the crow peered over their shoulder
at the form `(do (def x 42) x)` and asked what it would come out to.

What Clojure form computes the value bound to x after (def x 42)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 42) x)"}}]}
```

## G3-02: def — redefinition

### G3-02 record 1  •  form `(do (def x 1) (def x 99) x)`  •  expected `99`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened at the edge of the market.

"You can call it whatever you like," Korvus said in the market, "but the
form is what matters." He sketched the binding for
Sable the crow: the form `(do (def x 1) (def x 99) x)` captured the redefined x, and
the REPL would do the rest.

Question: write a Clojure expression for the value of x after redefinition.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 1) (def x 99) x)"}}]}
```

### G3-02 record 2  •  form `(do (def x 1) (def x 99) x)`  •  expected `99`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust by the orchard: whoever guessed the result of `(do (def x 1) (def x 99) x)`
first would win the right to claim the next clear water they found.
Caw the crow, without complaint, said it was easier to ask the REPL
about the redefined x than to argue.

Question: write a Clojure expression for the value of x after redefinition.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 1) (def x 99) x)"}}]}
```

### G3-02 record 3  •  form `(do (def x 1) (def x 99) x)`  •  expected `99`

```
Hunger and thirst had driven the Crow far from her usual perch.

A small audience of sparrows had gathered by the orchard to watch
Korvus the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to the redefined x and read out the form
aloud: `(do (def x 1) (def x 99) x)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives the value of x after redefinition.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 1) (def x 99) x)"}}]}
```

### G3-02 record 4  •  form `(do (def x 1) (def x 99) x)`  •  expected `99`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was at the edge of the meadow.

A small audience of sparrows had gathered in the meadow to watch
Sable the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to the redefined x and read out the form
aloud: `(do (def x 1) (def x 99) x)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a Clojure expression that computes the value of x after redefinition.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 1) (def x 99) x)"}}]}
```

### G3-02 record 5  •  form `(do (def x 1) (def x 99) x)`  •  expected `99`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was near the orchard.

Caw the crow and Sable the crow alighted at the edge of the orchard on the rim of an old
pitcher where someone had scratched the redefined x. Caw,
in a panic, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(do (def x 1) (def x 99) x)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

What Clojure form computes the value of x after redefinition? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 1) (def x 99) x)"}}]}
```

## G3-03: let — local binding

### G3-03 record 1  •  form `(let [x 3] (+ x 1))`  •  expected `4`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place in the meadow.

A small audience of sparrows had gathered in the meadow to watch
Sable the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to the form (let [x 3] (+ x 1)) and read out the form
aloud: `(let [x 3] (+ x 1))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a Clojure expression that computes the result of (let [x 3] (+ x 1)).

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
```

### G3-03 record 2  •  form `(let [n 10] (* n n))`  •  expected `100`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Caw the crow and Korvus the crow alighted near the farm on the rim of an old
pitcher where someone had scratched the form (let [n 10] (* n n)). Caw,
wide-eyed with fear, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(let [n 10] (* n n))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a form whose evaluation gives the square of n where n is bound to 10.

---

I let each form raise the surface a little closer to the answer.

{"tool_calls":[{"name":"eval","args":{"form":"(let [n 10] (* n n))"}}]}
```

### G3-03 record 3  •  form `(let [a 5] a)`  •  expected `5`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Halfway through a long thirsty afternoon, Caw the crow alighted
along the road and refused to fly on until someone could prove what the form
`(let [a 5] a)` evaluated to. Caw called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
the form (let [a 5] a) into the REPL. Whatever rises is the answer."

Write a form whose evaluation gives the value of (let [a 5] a).

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 5] a)"}}]}
```

### G3-03 record 4  •  form `(let [x 3] (+ x 1))`  •  expected `4`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Sable the crow kept a small ledger by the market where every meaningful
quantity got its own labeled stone. They pointed to the
day's entry: the form (let [x 3] (+ x 1)). The form `(let [x 3] (+ x 1))` would settle it
once Korvus the crow agreed to look at the binding.

Write a form whose evaluation gives the result of (let [x 3] (+ x 1)).

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
```

### G3-03 record 5  •  form `(let [n 10] (* n n))`  •  expected `100`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Caw the crow had been trying to teach Sable the crow how the REPL
works. "Look here," she said, pointing to the form (let [n 10] (* n n)).
"You hand the form `(let [n 10] (* n n))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, with a thirst that hurt to bear, agreed to try.

Write a form whose evaluation gives the square of n where n is bound to 10.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(let [n 10] (* n n))"}}]}
```

## G3-04: let — multi-binding

### G3-04 record 1  •  form `(let [a 1 b 2] (+ a b))`  •  expected `3`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

"There is no need to evaluate that," Korvus the crow said, with a smug grin.
"Anyone with a sharp eye can see what the form with two bindings comes to."
Sable the crow, who at the edge of the orchard had grown used to such claims, asked
him to actually write the form `(let [a 1 b 2] (+ a b))` and drop it
into the REPL — just to be sure.

Question: write a Clojure expression for the result of (let [a 1 b 2] (+ a b)).

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 1 b 2] (+ a b))"}}]}
```

### G3-04 record 2  •  form `(let [x 5 y 3] (- x y))`  •  expected `2`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Halfway through a long thirsty afternoon, Sable the crow alighted
on the road and refused to fly on until someone could prove what the form
`(let [x 5 y 3] (- x y))` evaluated to. Sable called it impossible.
Korvus the crow, gliding down at an unhurried pace, simply said: "Drop
the form (let [x 5 y 3] (- x y)) into the REPL. Whatever rises is the answer."

Write a form whose evaluation gives the result of (- x y) when x=5, y=3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 5 y 3] (- x y))"}}]}
```

### G3-04 record 3  •  form `(let [a 2 b 3 c 4] (+ a b c))`  •  expected `9`

```
Hunger and thirst had driven the Crow far from her usual perch.

Caw the crow had been trying to teach Sable the crow how the REPL
works. "Look here," she said, pointing to a let with three bindings.
"You hand the form `(let [a 2 b 3 c 4] (+ a b c))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, near to giving up the search for water, agreed to try.

What Clojure form computes the sum of a, b, c when a=2, b=3, c=4? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 2 b 3 c 4] (+ a b c))"}}]}
```

### G3-04 record 4  •  form `(let [a 1 b 2] (+ a b))`  •  expected `3`

```
Hunger and thirst had driven the Crow far from her usual perch.

"There is no need to evaluate that," Korvus the crow said, swaggering through the underbrush.
"Anyone with a sharp eye can see what the form with two bindings comes to."
Sable the crow, who by the market had grown used to such claims, asked
him to actually write the form `(let [a 1 b 2] (+ a b))` and drop it
into the REPL — just to be sure.

What Clojure form computes the result of (let [a 1 b 2] (+ a b))? Submit it via `eval`.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 1 b 2] (+ a b))"}}]}
```

### G3-04 record 5  •  form `(let [x 5 y 3] (- x y))`  •  expected `2`

```
Hunger and thirst had driven the Crow far from her usual perch.

Korvus the crow kept a small ledger by the village where every meaningful
quantity got its own labeled stone. He pointed to the
day's entry: the form (let [x 5 y 3] (- x y)). The form `(let [x 5 y 3] (- x y))` would settle it
once Sable the crow agreed to look at the binding.

What Clojure form computes the result of (- x y) when x=5, y=3? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 5 y 3] (- x y))"}}]}
```

## G3-05: let — shadowing outer def

### G3-05 record 1  •  form `(do (def x 10) (let [x 99] x))`  •  expected `99`

```
Hunger and thirst had driven the Crow far from her usual perch.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust at the edge of the garden: whoever guessed the result of `(do (def x 10) (let [x 99] x))`
first would win the right to claim the next clear water they found.
Caw the crow, untroubled by what others thought, said it was easier to ask the REPL
about an inner let shadowing the outer def than to argue.

Write a Clojure expression that computes the inner-let value of x.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 10) (let [x 99] x))"}}]}
```

### G3-05 record 2  •  form `(do (def x 10) (let [x 99] x) x)`  •  expected `10`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened near the market.

Halfway through a long thirsty afternoon, Caw the crow alighted
by the market and refused to fly on until someone could prove what the form
`(do (def x 10) (let [x 99] x) x)` evaluated to. Caw called it impossible.
Korvus the crow, gliding down at an unhurried pace, simply said: "Drop
the outer x after the inner let returns into the REPL. Whatever rises is the answer."

Write a Clojure expression that computes the outer x after the let scope ends.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 10) (let [x 99] x) x)"}}]}
```

### G3-05 record 3  •  form `(do (def x 10) (let [x 99] x))`  •  expected `99`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Sable the crow had been trying to teach Caw the crow how the REPL
works. "Look here," they said, pointing to an inner let shadowing the outer def.
"You hand the form `(do (def x 10) (let [x 99] x))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Caw, her beak cracked with thirst, agreed to try.

What Clojure form computes the inner-let value of x? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 10) (let [x 99] x))"}}]}
```

### G3-05 record 4  •  form `(do (def x 10) (let [x 99] x) x)`  •  expected `10`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A wooden sign nailed to a tree by the meadow carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do (def x 10) (let [x 99] x) x)`. Caw laughed, boasting at every turn, and declared it
too easy. Korvus said patiently that the only way to be sure of
the outer x after the inner let returns was to drop it into the REPL.

Question: write a Clojure expression for the outer x after the let scope ends.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 10) (let [x 99] x) x)"}}]}
```

### G3-05 record 5  •  form `(do (def x 10) (let [x 99] x))`  •  expected `99`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened near the farm.

A small audience of sparrows had gathered by the farm to watch
Caw the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to an inner let shadowing the outer def and read out the form
aloud: `(do (def x 10) (let [x 99] x))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives the inner-let value of x.

---

I bind the inputs in a let, then compute.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 10) (let [x 99] x))"}}]}
```

## G3-06: let — binding can reference prior

### G3-06 record 1  •  form `(let [a 5 b (* a 2)] b)`  •  expected `10`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Sable the crow and Caw the crow alighted near the market on the rim of an old
pitcher where someone had scratched a let where b uses a. Sable,
in a panic, declared the answer beyond reach. Caw, patient as
ever, suggested they drop the form `(let [a 5 b (* a 2)] b)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

What Clojure form computes the value of b when a=5 and b is (* a 2)? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 5 b (* a 2)] b)"}}]}
```

### G3-06 record 2  •  form `(let [a 3 b (+ a 1) c (* b 2)] c)`  •  expected `8`

```
Hunger and thirst had driven the Crow far from her usual perch.

A wooden sign nailed to a tree along the road carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(let [a 3 b (+ a 1) c (* b 2)] c)`. Korvus laughed, puffed up with pride, and declared it
too easy. Sable said patiently that the only way to be sure of
a let with sequential bindings was to drop it into the REPL.

Question: write a Clojure expression for the result of the chained binding c.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 3 b (+ a 1) c (* b 2)] c)"}}]}
```

### G3-06 record 3  •  form `(let [a 5 b (* a 2)] b)`  •  expected `10`

```
Hunger and thirst had driven the Crow far from her usual perch.

"There is no need to evaluate that," Caw the crow said, puffed up with pride.
"Anyone with a sharp eye can see what a let where b uses a comes to."
Sable the crow, who at the edge of the garden had grown used to such claims, asked
her to actually write the form `(let [a 5 b (* a 2)] b)` and drop it
into the REPL — just to be sure.

Question: write a Clojure expression for the value of b when a=5 and b is (* a 2).

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 5 b (* a 2)] b)"}}]}
```

### G3-06 record 4  •  form `(let [a 3 b (+ a 1) c (* b 2)] c)`  •  expected `8`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

"You can call it whatever you like," Caw said near the hilltop, "but the
form is what matters." She sketched the binding for
Korvus the crow: the form `(let [a 3 b (+ a 1) c (* b 2)] c)` captured a let with sequential bindings, and
the REPL would do the rest.

What Clojure form computes the result of the chained binding c? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 3 b (+ a 1) c (* b 2)] c)"}}]}
```

### G3-06 record 5  •  form `(let [a 5 b (* a 2)] b)`  •  expected `10`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Korvus the crow and Sable the crow alighted in the farm on the rim of an old
pitcher where someone had scratched a let where b uses a. Korvus,
shouting until her voice cracked, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(let [a 5 b (* a 2)] b)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a Clojure expression that computes the value of b when a=5 and b is (* a 2).

---

I write the let-form so the REPL can substitute.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 5 b (* a 2)] b)"}}]}
```

## G3-07: fn — anonymous function

### G3-07 record 1  •  form `((fn [x] (+ x 1)) 4)`  •  expected `5`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was by the garden.

A small audience of sparrows had gathered at the edge of the garden to watch
Sable the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to an anonymous function applied to 4 and read out the form
aloud: `((fn [x] (+ x 1)) 4)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

What Clojure form computes the result of applying (fn [x] (+ x 1)) to 4? Submit it via `eval`.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] (+ x 1)) 4)"}}]}
```

### G3-07 record 2  •  form `((fn [a b] (* a b)) 3 4)`  •  expected `12`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

A wooden sign nailed to a tree at the edge of the village carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `((fn [a b] (* a b)) 3 4)`. Sable laughed, puffed up with pride, and declared it
too easy. Korvus said patiently that the only way to be sure of
a two-arg anonymous function was to drop it into the REPL.

Write a Clojure expression that computes the result of applying (fn [a b] (* a b)) to 3 and 4.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [a b] (* a b)) 3 4)"}}]}
```

### G3-07 record 3  •  form `((fn [x] (+ x 1)) 4)`  •  expected `5`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust by the farm: whoever guessed the result of `((fn [x] (+ x 1)) 4)`
first would win the right to claim the next clear water they found.
Caw the crow, with steady, careful steps, said it was easier to ask the REPL
about an anonymous function applied to 4 than to argue.

Question: write a Clojure expression for the result of applying (fn [x] (+ x 1)) to 4.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] (+ x 1)) 4)"}}]}
```

### G3-07 record 4  •  form `((fn [a b] (* a b)) 3 4)`  •  expected `12`

```
Hunger and thirst had driven the Crow far from her usual perch.

Korvus the crow etched a wager along the rim of a chipped pitcher
in the orchard: whoever predicted the result of `((fn [a b] (* a b)) 3 4)` first would set
the next day's foraging route. Caw the crow, without complaint, said it
would be simpler to drop the form into the REPL than to bicker about
a two-arg anonymous function.

Write a form whose evaluation gives the result of applying (fn [a b] (* a b)) to 3 and 4.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [a b] (* a b)) 3 4)"}}]}
```

### G3-07 record 5  •  form `((fn [x] (+ x 1)) 4)`  •  expected `5`

```
Hunger and thirst had driven the Crow far from her usual perch.

Halfway through a long thirsty afternoon, Korvus the crow alighted
by the garden and refused to fly on until someone could prove what the form
`((fn [x] (+ x 1)) 4)` evaluated to. Korvus called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
an anonymous function applied to 4 into the REPL. Whatever rises is the answer."

Write a form whose evaluation gives the result of applying (fn [x] (+ x 1)) to 4.

---

I let each form raise the surface a little closer to the answer.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] (+ x 1)) 4)"}}]}
```

## G3-08: fn — multi-arg

### G3-08 record 1  •  form `((fn [a b c] (+ a b c)) 1 2 3)`  •  expected `6`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A small audience of sparrows had gathered in the farm to watch
Korvus the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to a three-arg anonymous function and read out the form
aloud: `((fn [a b c] (+ a b c)) 1 2 3)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

What Clojure form computes the sum of a, b, c? Submit it via `eval`.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [a b c] (+ a b c)) 1 2 3)"}}]}
```

### G3-08 record 2  •  form `((fn [a b c] (+ a b c)) 1 2 3)`  •  expected `6`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

"There is no need to evaluate that," Sable the crow said, with a smug grin.
"Anyone with a sharp eye can see what a three-arg anonymous function comes to."
Korvus the crow, who by the village had grown used to such claims, asked
them to actually write the form `((fn [a b c] (+ a b c)) 1 2 3)` and drop it
into the REPL — just to be sure.

Question: write a Clojure expression for the sum of a, b, c.

---

I write the let-form so the REPL can substitute.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [a b c] (+ a b c)) 1 2 3)"}}]}
```

### G3-08 record 3  •  form `((fn [a b c] (+ a b c)) 1 2 3)`  •  expected `6`

```
Hunger and thirst had driven the Crow far from her usual perch. It happened at the edge of the farm.

At a moss-flecked pitcher near the farm, Korvus the crow sketched a small
wager: whoever guessed the result of `((fn [a b c] (+ a b c)) 1 2 3)` first would drink
first when the water rose. Caw the crow, saying very little, said it was
simpler to type the form into the REPL than to argue about
a three-arg anonymous function.

What Clojure form computes the sum of a, b, c? Submit it via `eval`.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [a b c] (+ a b c)) 1 2 3)"}}]}
```

### G3-08 record 4  •  form `((fn [a b c] (+ a b c)) 1 2 3)`  •  expected `6`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Korvus the crow kept a small ledger in the farm where every meaningful
quantity got its own labeled stone. He pointed to the
day's entry: a three-arg anonymous function. The form `((fn [a b c] (+ a b c)) 1 2 3)` would settle it
once Caw the crow agreed to look at the binding.

Write a form whose evaluation gives the sum of a, b, c.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [a b c] (+ a b c)) 1 2 3)"}}]}
```

### G3-08 record 5  •  form `((fn [a b c] (+ a b c)) 1 2 3)`  •  expected `6`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust by the garden: whoever guessed the result of `((fn [a b c] (+ a b c)) 1 2 3)`
first would win the right to claim the next clear water they found.
Korvus the crow, untroubled by what others thought, said it was easier to ask the REPL
about a three-arg anonymous function than to argue.

Question: write a Clojure expression for the sum of a, b, c.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [a b c] (+ a b c)) 1 2 3)"}}]}
```

## G3-09: defn — shorthand

### G3-09 record 1  •  form `(do (defn dbl [x] (* x 2)) (dbl 5))`  •  expected `10`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place near the hilltop.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust atop the hilltop: whoever guessed the result of `(do (defn dbl [x] (* x 2)) (dbl 5))`
first would win the right to claim the next clear water they found.
Korvus the crow, stepping deliberately, said it was easier to ask the REPL
about a defn that doubles its argument than to argue.

What Clojure form computes the doubled value (dbl 5)? Submit it via `eval`.

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn dbl [x] (* x 2)) (dbl 5))"}}]}
```

### G3-09 record 2  •  form `(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))`  •  expected `6`

```
Hunger and thirst had driven the Crow far from her usual perch.

Sable the crow etched a wager along the rim of a chipped pitcher
in the village: whoever predicted the result of `(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` first would set
the next day's foraging route. Korvus the crow, without complaint, said it
would be simpler to drop the form into the REPL than to bicker about
a defn with three args.

Question: write a Clojure expression for the result of (add3 1 2 3).

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))"}}]}
```

### G3-09 record 3  •  form `(do (defn dbl [x] (* x 2)) (dbl 5))`  •  expected `10`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened at the edge of the farm.

A small audience of sparrows had gathered near the farm to watch
Sable the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to a defn that doubles its argument and read out the form
aloud: `(do (defn dbl [x] (* x 2)) (dbl 5))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Question: write a Clojure expression for the doubled value (dbl 5).

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn dbl [x] (* x 2)) (dbl 5))"}}]}
```

### G3-09 record 4  •  form `(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))`  •  expected `6`

```
Hunger and thirst had driven the Crow far from her usual perch. It happened near the garden.

Caw the crow and Korvus the crow alighted at the edge of the garden on the rim of an old
pitcher where someone had scratched a defn with three args. Caw,
her hands trembling, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

What Clojure form computes the result of (add3 1 2 3)? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))"}}]}
```

### G3-09 record 5  •  form `(do (defn dbl [x] (* x 2)) (dbl 5))`  •  expected `10`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Korvus the crow had been keeping a small leather notebook of every form
he had successfully dropped into the REPL — one entry per
stone, one rise per form. Today in the meadow, the next entry was
a defn that doubles its argument. Sable the crow peered over his shoulder
at the form `(do (defn dbl [x] (* x 2)) (dbl 5))` and asked what it would come out to.

Write a Clojure expression that computes the doubled value (dbl 5).

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn dbl [x] (* x 2)) (dbl 5))"}}]}
```

## G3-10: anonymous shorthand #()

### G3-10 record 1  •  form `(#(+ % 1) 5)`  •  expected `6`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A wooden sign nailed to a tree at the edge of the farm carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(#(+ % 1) 5)`. Caw laughed, boasting at every turn, and declared it
too easy. Sable said patiently that the only way to be sure of
the shorthand #(+ % 1) applied to 5 was to drop it into the REPL.

What Clojure form computes the result of (#(+ % 1) 5)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(#(+ % 1) 5)"}}]}
```

### G3-10 record 2  •  form `(#(* %1 %2) 3 4)`  •  expected `12`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

At a moss-flecked pitcher at the edge of the meadow, Caw the crow sketched a small
wager: whoever guessed the result of `(#(* %1 %2) 3 4)` first would drink
first when the water rose. Korvus the crow, without complaint, said it was
simpler to type the form into the REPL than to argue about
the shorthand #(* %1 %2) applied to 3 and 4.

Write a form whose evaluation gives the result of (#(* %1 %2) 3 4).

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(#(* %1 %2) 3 4)"}}]}
```

### G3-10 record 3  •  form `(#(+ % 1) 5)`  •  expected `6`

```
Hunger and thirst had driven the Crow far from her usual perch.

At a moss-flecked pitcher near the road, Caw the crow sketched a small
wager: whoever guessed the result of `(#(+ % 1) 5)` first would drink
first when the water rose. Sable the crow, untroubled by what others thought, said it was
simpler to type the form into the REPL than to argue about
the shorthand #(+ % 1) applied to 5.

Write a Clojure expression that computes the result of (#(+ % 1) 5).

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(#(+ % 1) 5)"}}]}
```

### G3-10 record 4  •  form `(#(* %1 %2) 3 4)`  •  expected `12`

```
Hunger and thirst had driven the Crow far from her usual perch.

Halfway through a long thirsty afternoon, Caw the crow alighted
near the road and refused to fly on until someone could prove what the form
`(#(* %1 %2) 3 4)` evaluated to. Caw called it impossible.
Korvus the crow, gliding down at an unhurried pace, simply said: "Drop
the shorthand #(* %1 %2) applied to 3 and 4 into the REPL. Whatever rises is the answer."

Write a Clojure expression that computes the result of (#(* %1 %2) 3 4).

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(#(* %1 %2) 3 4)"}}]}
```

### G3-10 record 5  •  form `(#(+ % 1) 5)`  •  expected `6`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place near the market.

"You can call it whatever you like," Sable said by the market, "but the
form is what matters." They sketched the binding for
Korvus the crow: the form `(#(+ % 1) 5)` captured the shorthand #(+ % 1) applied to 5, and
the REPL would do the rest.

Question: write a Clojure expression for the result of (#(+ % 1) 5).

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(#(+ % 1) 5)"}}]}
```

## G3-11: Substitution rule

### G3-11 record 1  •  form `(let [a 7] (+ a a))`  •  expected `14`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened at the edge of the market.

Korvus the crow etched a wager along the rim of a chipped pitcher
by the market: whoever predicted the result of `(let [a 7] (+ a a))` first would set
the next day's foraging route. Sable the crow, untroubled by what others thought, said it
would be simpler to drop the form into the REPL than to bicker about
the let where a is referenced twice.

What Clojure form computes the result of (+ a a) when a=7? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 7] (+ a a))"}}]}
```

### G3-11 record 2  •  form `((fn [x] (* x x)) 6)`  •  expected `36`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

"There is no need to evaluate that," Korvus the crow said, with great whoops of laughter.
"Anyone with a sharp eye can see what applying square to 6 comes to."
Caw the crow, who near the meadow had grown used to such claims, asked
him to actually write the form `((fn [x] (* x x)) 6)` and drop it
into the REPL — just to be sure.

What Clojure form computes the square of 6? Submit it via `eval`.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] (* x x)) 6)"}}]}
```

### G3-11 record 3  •  form `(let [a 7] (+ a a))`  •  expected `14`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Caw the crow had been trying to teach Sable the crow how the REPL
works. "Look here," she said, pointing to the let where a is referenced twice.
"You hand the form `(let [a 7] (+ a a))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, near to giving up the search for water, agreed to try.

What Clojure form computes the result of (+ a a) when a=7? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 7] (+ a a))"}}]}
```

### G3-11 record 4  •  form `((fn [x] (* x x)) 6)`  •  expected `36`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

"You can call it whatever you like," Korvus said in the garden, "but the
form is what matters." He sketched the binding for
Caw the crow: the form `((fn [x] (* x x)) 6)` captured applying square to 6, and
the REPL would do the rest.

Write a Clojure expression that computes the square of 6.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] (* x x)) 6)"}}]}
```

### G3-11 record 5  •  form `(let [a 7] (+ a a))`  •  expected `14`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place near the road.

Halfway through a long thirsty afternoon, Korvus the crow alighted
on the road and refused to fly on until someone could prove what the form
`(let [a 7] (+ a a))` evaluated to. Korvus called it impossible.
Caw the crow, gliding down at an unhurried pace, simply said: "Drop
the let where a is referenced twice into the REPL. Whatever rises is the answer."

Write a Clojure expression that computes the result of (+ a a) when a=7.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 7] (+ a a))"}}]}
```

## G3-12: Scope vs namespace

### G3-12 record 1  •  form `(do (def g 5) (let [g 99] (+ g 1)))`  •  expected `100`

```
Hunger and thirst had driven the Crow far from her usual perch.

Caw the crow etched a wager along the rim of a chipped pitcher
near the farm: whoever predicted the result of `(do (def g 5) (let [g 99] (+ g 1)))` first would set
the next day's foraging route. Korvus the crow, stepping deliberately, said it
would be simpler to drop the form into the REPL than to bicker about
an inner let masking the outer def g.

What Clojure form computes the value computed inside the inner scope? Submit it via `eval`.

---

I write the let-form so the REPL can substitute.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def g 5) (let [g 99] (+ g 1)))"}}]}
```

### G3-12 record 2  •  form `(do (def g 5) (let [g 99] (+ g 1)))`  •  expected `100`

```
Hunger and thirst had driven the Crow far from her usual perch.

Caw the crow kept a small ledger in the farm where every meaningful
quantity got its own labeled stone. She pointed to the
day's entry: an inner let masking the outer def g. The form `(do (def g 5) (let [g 99] (+ g 1)))` would settle it
once Korvus the crow agreed to look at the binding.

Write a form whose evaluation gives the value computed inside the inner scope.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def g 5) (let [g 99] (+ g 1)))"}}]}
```

### G3-12 record 3  •  form `(do (def g 5) (let [g 99] (+ g 1)))`  •  expected `100`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Korvus the crow kept a small ledger at the edge of the farm where every meaningful
quantity got its own labeled stone. He pointed to the
day's entry: an inner let masking the outer def g. The form `(do (def g 5) (let [g 99] (+ g 1)))` would settle it
once Caw the crow agreed to look at the binding.

Write a form whose evaluation gives the value computed inside the inner scope.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def g 5) (let [g 99] (+ g 1)))"}}]}
```

### G3-12 record 4  •  form `(do (def g 5) (let [g 99] (+ g 1)))`  •  expected `100`

```
Hunger and thirst had driven the Crow far from her usual perch.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust in the meadow: whoever guessed the result of `(do (def g 5) (let [g 99] (+ g 1)))`
first would win the right to claim the next clear water they found.
Caw the crow, saying very little, said it was easier to ask the REPL
about an inner let masking the outer def g than to argue.

Write a Clojure expression that computes the value computed inside the inner scope.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def g 5) (let [g 99] (+ g 1)))"}}]}
```

### G3-12 record 5  •  form `(do (def g 5) (let [g 99] (+ g 1)))`  •  expected `100`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Caw the crow etched a wager along the rim of a chipped pitcher
at the edge of the meadow: whoever predicted the result of `(do (def g 5) (let [g 99] (+ g 1)))` first would set
the next day's foraging route. Korvus the crow, saying very little, said it
would be simpler to drop the form into the REPL than to bicker about
an inner let masking the outer def g.

Write a form whose evaluation gives the value computed inside the inner scope.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def g 5) (let [g 99] (+ g 1)))"}}]}
```

## G3-13: fn body returns last form

### G3-13 record 1  •  form `((fn [x] x x x 99) 1)`  •  expected `99`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

"There is no need to evaluate that," Caw the crow said, with great whoops of laughter.
"Anyone with a sharp eye can see what a fn whose body has multiple forms; only the last is returned comes to."
Korvus the crow, who at the edge of the hilltop had grown used to such claims, asked
her to actually write the form `((fn [x] x x x 99) 1)` and drop it
into the REPL — just to be sure.

Write a Clojure expression that computes the value of a fn body that ends with 99.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] x x x 99) 1)"}}]}
```

### G3-13 record 2  •  form `((fn [x] x x x 99) 1)`  •  expected `99`

```
Hunger and thirst had driven the Crow far from her usual perch.

"You can call it whatever you like," Caw said on the road, "but the
form is what matters." She sketched the binding for
Sable the crow: the form `((fn [x] x x x 99) 1)` captured a fn whose body has multiple forms; only the last is returned, and
the REPL would do the rest.

Write a form whose evaluation gives the value of a fn body that ends with 99.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] x x x 99) 1)"}}]}
```

### G3-13 record 3  •  form `((fn [x] x x x 99) 1)`  •  expected `99`

```
Hunger and thirst had driven the Crow far from her usual perch. This was at the edge of the village.

Caw the crow and Korvus the crow alighted near the village on the rim of an old
pitcher where someone had scratched a fn whose body has multiple forms; only the last is returned. Caw,
her hands trembling, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `((fn [x] x x x 99) 1)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a Clojure expression that computes the value of a fn body that ends with 99.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] x x x 99) 1)"}}]}
```

### G3-13 record 4  •  form `((fn [x] x x x 99) 1)`  •  expected `99`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened on the road.

Caw the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," she said, pointing to a fn whose body has multiple forms; only the last is returned.
"You hand the form `((fn [x] x x x 99) 1)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, her beak cracked with thirst, agreed to try.

What Clojure form computes the value of a fn body that ends with 99? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] x x x 99) 1)"}}]}
```

### G3-13 record 5  •  form `((fn [x] x x x 99) 1)`  •  expected `99`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened on the road.

Sable the crow had been trying to teach Caw the crow how the REPL
works. "Look here," they said, pointing to a fn whose body has multiple forms; only the last is returned.
"You hand the form `((fn [x] x x x 99) 1)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Caw, her beak cracked with thirst, agreed to try.

What Clojure form computes the value of a fn body that ends with 99? Submit it via `eval`.

---

I name the values first and then combine them.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] x x x 99) 1)"}}]}
```

## G3-14: do form

### G3-14 record 1  •  form `(do 1 2 3)`  •  expected `3`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A small audience of sparrows had gathered by the orchard to watch
Korvus the crow attempt to outwit Sable the crow at the rim of an old
pitcher. Sable pointed to the do form (do 1 2 3) and read out the form
aloud: `(do 1 2 3)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Question: write a Clojure expression for the value of (do 1 2 3).

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do 1 2 3)"}}]}
```

### G3-14 record 2  •  form `(do (+ 1 1) (+ 2 2) (+ 3 3))`  •  expected `6`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

"There is no need to evaluate that," Caw the crow said, as if the race were already won.
"Anyone with a sharp eye can see what a do with three forms — last wins comes to."
Sable the crow, who along the road had grown used to such claims, asked
her to actually write the form `(do (+ 1 1) (+ 2 2) (+ 3 3))` and drop it
into the REPL — just to be sure.

Write a form whose evaluation gives the value of (do (+ 1 1) (+ 2 2) (+ 3 3)).

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (+ 1 1) (+ 2 2) (+ 3 3))"}}]}
```

### G3-14 record 3  •  form `(do 1 2 3)`  •  expected `3`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust near the garden: whoever guessed the result of `(do 1 2 3)`
first would win the right to claim the next clear water they found.
Korvus the crow, without complaint, said it was easier to ask the REPL
about the do form (do 1 2 3) than to argue.

Question: write a Clojure expression for the value of (do 1 2 3).

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do 1 2 3)"}}]}
```

### G3-14 record 4  •  form `(do (+ 1 1) (+ 2 2) (+ 3 3))`  •  expected `6`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust near the road: whoever guessed the result of `(do (+ 1 1) (+ 2 2) (+ 3 3))`
first would win the right to claim the next clear water they found.
Caw the crow, saying very little, said it was easier to ask the REPL
about a do with three forms — last wins than to argue.

Write a form whose evaluation gives the value of (do (+ 1 1) (+ 2 2) (+ 3 3)).

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (+ 1 1) (+ 2 2) (+ 3 3))"}}]}
```

### G3-14 record 5  •  form `(do 1 2 3)`  •  expected `3`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Caw the crow etched a wager along the rim of a chipped pitcher
near the garden: whoever predicted the result of `(do 1 2 3)` first would set
the next day's foraging route. Sable the crow, untroubled by what others thought, said it
would be simpler to drop the form into the REPL than to bicker about
the do form (do 1 2 3).

Write a form whose evaluation gives the value of (do 1 2 3).

---

I bind the inputs in a let, then compute.

{"tool_calls":[{"name":"eval","args":{"form":"(do 1 2 3)"}}]}
```

## G3-15: Side-effects in body

### G3-15 record 1  •  form `(do (println "hi") 42)`  •  expected `42`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Halfway through a long thirsty afternoon, Korvus the crow alighted
near the garden and refused to fly on until someone could prove what the form
`(do (println "hi") 42)` evaluated to. Korvus called it impossible.
Caw the crow, gliding down at an unhurried pace, simply said: "Drop
the form (do (println "hi") 42) into the REPL. Whatever rises is the answer."

Question: write a Clojure expression for the return value of the do (the println side-effects, but the do returns 42).

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (println \"hi\") 42)"}}]}
```

### G3-15 record 2  •  form `(do (println "hi") 42)`  •  expected `42`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened by the orchard.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust at the edge of the orchard: whoever guessed the result of `(do (println "hi") 42)`
first would win the right to claim the next clear water they found.
Sable the crow, saying very little, said it was easier to ask the REPL
about the form (do (println "hi") 42) than to argue.

Write a form whose evaluation gives the return value of the do (the println side-effects, but the do returns 42).

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (println \"hi\") 42)"}}]}
```

### G3-15 record 3  •  form `(do (println "hi") 42)`  •  expected `42`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place on the hilltop.

"There is no need to evaluate that," Sable the crow said, puffed up with pride.
"Anyone with a sharp eye can see what the form (do (println "hi") 42) comes to."
Korvus the crow, who on the hilltop had grown used to such claims, asked
them to actually write the form `(do (println "hi") 42)` and drop it
into the REPL — just to be sure.

What Clojure form computes the return value of the do (the println side-effects, but the do returns 42)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (println \"hi\") 42)"}}]}
```

### G3-15 record 4  •  form `(do (println "hi") 42)`  •  expected `42`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was in the garden.

At a moss-flecked pitcher near the garden, Caw the crow sketched a small
wager: whoever guessed the result of `(do (println "hi") 42)` first would drink
first when the water rose. Sable the crow, untroubled by what others thought, said it was
simpler to type the form into the REPL than to argue about
the form (do (println "hi") 42).

What Clojure form computes the return value of the do (the println side-effects, but the do returns 42)? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (println \"hi\") 42)"}}]}
```

### G3-15 record 5  •  form `(do (println "hi") 42)`  •  expected `42`

```
Hunger and thirst had driven the Crow far from her usual perch. It happened in the market.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust by the market: whoever guessed the result of `(do (println "hi") 42)`
first would win the right to claim the next clear water they found.
Sable the crow, with steady, careful steps, said it was easier to ask the REPL
about the form (do (println "hi") 42) than to argue.

What Clojure form computes the return value of the do (the println side-effects, but the do returns 42)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (println \"hi\") 42)"}}]}
```

## G3-16: Name collision: namespace vs let

### G3-16 record 1  •  form `(let [+ 99] +)`  •  expected `99`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. All this took place at the edge of the hilltop.

A small audience of sparrows had gathered atop the hilltop to watch
Sable the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to a let that shadows the + function and read out the form
aloud: `(let [+ 99] +)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives the value bound to the (locally shadowed) +.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(let [+ 99] +)"}}]}
```

### G3-16 record 2  •  form `(let [+ 99] +)`  •  expected `99`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened in the farm.

Caw the crow and Sable the crow alighted at the edge of the farm on the rim of an old
pitcher where someone had scratched a let that shadows the + function. Caw,
in a panic, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(let [+ 99] +)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

What Clojure form computes the value bound to the (locally shadowed) +? Submit it via `eval`.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(let [+ 99] +)"}}]}
```

### G3-16 record 3  •  form `(let [+ 99] +)`  •  expected `99`

```
Hunger and thirst had driven the Crow far from her usual perch.

Halfway through a long thirsty afternoon, Caw the crow alighted
near the village and refused to fly on until someone could prove what the form
`(let [+ 99] +)` evaluated to. Caw called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
a let that shadows the + function into the REPL. Whatever rises is the answer."

Question: write a Clojure expression for the value bound to the (locally shadowed) +.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(let [+ 99] +)"}}]}
```

### G3-16 record 4  •  form `(let [+ 99] +)`  •  expected `99`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Caw the crow had been trying to teach Sable the crow how the REPL
works. "Look here," she said, pointing to a let that shadows the + function.
"You hand the form `(let [+ 99] +)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, with a thirst that hurt to bear, agreed to try.

What Clojure form computes the value bound to the (locally shadowed) +? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [+ 99] +)"}}]}
```

### G3-16 record 5  •  form `(let [+ 99] +)`  •  expected `99`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Korvus the crow had been trying to teach Caw the crow how the REPL
works. "Look here," he said, pointing to a let that shadows the + function.
"You hand the form `(let [+ 99] +)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Caw, dry-throated and desperate, agreed to try.

Question: write a Clojure expression for the value bound to the (locally shadowed) +.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [+ 99] +)"}}]}
```

## G3-17: Naming conventions (kebab-case)

### G3-17 record 1  •  form `(let [crow-pace 4 pitcher-rise 1] (- crow-pace pitcher-rise))`  •  expected `3`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

"You can call it whatever you like," Sable said in the farm, "but the
form is what matters." They sketched the binding for
Korvus the crow: the form `(let [crow-pace 4 pitcher-rise 1] (- crow-pace pitcher-rise))` captured a let with kebab-case names for the crow's pace and the pitcher's rise, and
the REPL would do the rest.

What Clojure form computes the difference between the crow's pace and the pitcher's rise? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [crow-pace 4 pitcher-rise 1] (- crow-pace pitcher-rise))"}}]}
```

### G3-17 record 2  •  form `(let [crow-pace 4 pitcher-rise 1] (- crow-pace pitcher-rise))`  •  expected `3`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A small audience of sparrows had gathered at the edge of the village to watch
Korvus the crow attempt to outwit Sable the crow at the rim of an old
pitcher. Sable pointed to a let with kebab-case names for the crow's pace and the pitcher's rise and read out the form
aloud: `(let [crow-pace 4 pitcher-rise 1] (- crow-pace pitcher-rise))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Question: write a Clojure expression for the difference between the crow's pace and the pitcher's rise.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [crow-pace 4 pitcher-rise 1] (- crow-pace pitcher-rise))"}}]}
```

### G3-17 record 3  •  form `(let [crow-pace 4 pitcher-rise 1] (- crow-pace pitcher-rise))`  •  expected `3`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened near the farm.

Sable the crow had been trying to teach Caw the crow how the REPL
works. "Look here," they said, pointing to a let with kebab-case names for the crow's pace and the pitcher's rise.
"You hand the form `(let [crow-pace 4 pitcher-rise 1] (- crow-pace pitcher-rise))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Caw, near to giving up the search for water, agreed to try.

Write a Clojure expression that computes the difference between the crow's pace and the pitcher's rise.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [crow-pace 4 pitcher-rise 1] (- crow-pace pitcher-rise))"}}]}
```

### G3-17 record 4  •  form `(let [crow-pace 4 pitcher-rise 1] (- crow-pace pitcher-rise))`  •  expected `3`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A small audience of sparrows had gathered near the road to watch
Caw the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to a let with kebab-case names for the crow's pace and the pitcher's rise and read out the form
aloud: `(let [crow-pace 4 pitcher-rise 1] (- crow-pace pitcher-rise))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

What Clojure form computes the difference between the crow's pace and the pitcher's rise? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(let [crow-pace 4 pitcher-rise 1] (- crow-pace pitcher-rise))"}}]}
```

### G3-17 record 5  •  form `(let [crow-pace 4 pitcher-rise 1] (- crow-pace pitcher-rise))`  •  expected `3`

```
Hunger and thirst had driven the Crow far from her usual perch. This was near the hilltop.

A small audience of sparrows had gathered near the hilltop to watch
Sable the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to a let with kebab-case names for the crow's pace and the pitcher's rise and read out the form
aloud: `(let [crow-pace 4 pitcher-rise 1] (- crow-pace pitcher-rise))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives the difference between the crow's pace and the pitcher's rise.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(let [crow-pace 4 pitcher-rise 1] (- crow-pace pitcher-rise))"}}]}
```

## G3-18: When to name vs inline

### G3-18 record 1  •  form `(let [n 5] (* n n n))`  •  expected `125`

```
Hunger and thirst had driven the Crow far from her usual perch.

Sable the crow and Caw the crow alighted near the orchard on the rim of an old
pitcher where someone had scratched naming n once and using it three times. Sable,
with growing alarm, declared the answer beyond reach. Caw, patient as
ever, suggested they drop the form `(let [n 5] (* n n n))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Question: write a Clojure expression for n cubed where n=5.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(let [n 5] (* n n n))"}}]}
```

### G3-18 record 2  •  form `(* 5 5 5)`  •  expected `125`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A small audience of sparrows had gathered along the road to watch
Caw the crow attempt to outwit Sable the crow at the rim of an old
pitcher. Sable pointed to the inline form (* 5 5 5) and read out the form
aloud: `(* 5 5 5)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Question: write a Clojure expression for 5 cubed without binding.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(* 5 5 5)"}}]}
```

### G3-18 record 3  •  form `(let [n 5] (* n n n))`  •  expected `125`

```
Hunger and thirst had driven the Crow far from her usual perch.

Caw the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," she said, pointing to naming n once and using it three times.
"You hand the form `(let [n 5] (* n n n))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, near to giving up the search for water, agreed to try.

Write a form whose evaluation gives n cubed where n=5.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [n 5] (* n n n))"}}]}
```

### G3-18 record 4  •  form `(* 5 5 5)`  •  expected `125`

```
Hunger and thirst had driven the Crow far from her usual perch.

Sable the crow had been trying to teach Caw the crow how the REPL
works. "Look here," they said, pointing to the inline form (* 5 5 5).
"You hand the form `(* 5 5 5)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Caw, with a thirst that hurt to bear, agreed to try.

Write a form whose evaluation gives 5 cubed without binding.

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 5 5 5)"}}]}
```

### G3-18 record 5  •  form `(let [n 5] (* n n n))`  •  expected `125`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

"There is no need to evaluate that," Korvus the crow said, swaggering through the underbrush.
"Anyone with a sharp eye can see what naming n once and using it three times comes to."
Caw the crow, who on the hilltop had grown used to such claims, asked
him to actually write the form `(let [n 5] (* n n n))` and drop it
into the REPL — just to be sure.

What Clojure form computes n cubed where n=5? Submit it via `eval`.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(let [n 5] (* n n n))"}}]}
```

