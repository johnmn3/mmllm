# crow-pitcher grade 2 — deep spot-check

5 records per subject for hand-audit.

---

## G2-01: Multi-arg arithmetic

### G2-01 record 1  •  form `(+ 1 2 3 4)`  •  expected `10`

```
Hunger and thirst had driven the Crow far from her usual perch.

Korvus the crow etched a wager along the rim of a chipped pitcher
in the meadow: whoever predicted the result of `(+ 1 2 3 4)` first would set
the next day's foraging route. Sable the crow, saying very little, said it
would be simpler to drop the form into the REPL than to bicker about
the sum (+ 1 2 3 4).

What Clojure form computes the result of (+ 1 2 3 4)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2 3 4)"}}]}
```

### G2-01 record 2  •  form `(* 2 3 4)`  •  expected `24`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened on the road.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust near the road: whoever guessed the result of `(* 2 3 4)`
first would win the right to claim the next clear water they found.
Sable the crow, her eyes always on the path, said it was easier to ask the REPL
about the product (* 2 3 4) than to argue.

Question: write a Clojure expression for the result of (* 2 3 4).

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(* 2 3 4)"}}]}
```

### G2-01 record 3  •  form `(- 100 1 2 3)`  •  expected `94`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

A wooden sign nailed to a tree in the farm carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(- 100 1 2 3)`. Caw laughed, with great whoops of laughter, and declared it
too easy. Sable said patiently that the only way to be sure of
the chain (- 100 1 2 3) was to drop it into the REPL.

Write a form whose evaluation gives the result of (- 100 1 2 3).

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(- 100 1 2 3)"}}]}
```

### G2-01 record 4  •  form `(+ 1 2 3 4 5 6 7 8 9 10)`  •  expected `55`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened at the edge of the village.

Halfway through a long thirsty afternoon, Korvus the crow alighted
at the edge of the village and refused to fly on until someone could prove what the form
`(+ 1 2 3 4 5 6 7 8 9 10)` evaluated to. Korvus called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
the sum 1+2+...+10 into the REPL. Whatever rises is the answer."

What Clojure form computes the sum of integers 1 through 10? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2 3 4 5 6 7 8 9 10)"}}]}
```

### G2-01 record 5  •  form `(* 1 2 3 4 5)`  •  expected `120`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

At a moss-flecked pitcher by the garden, Caw the crow sketched a small
wager: whoever guessed the result of `(* 1 2 3 4 5)` first would drink
first when the water rose. Sable the crow, her eyes always on the path, said it was
simpler to type the form into the REPL than to argue about
the product 1*2*3*4*5.

What Clojure form computes the product of 1 through 5 (5!)? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(* 1 2 3 4 5)"}}]}
```

## G2-02: Comparison chains

### G2-02 record 1  •  form `(< 1 2 3)`  •  expected `True`

```
Hunger and thirst had driven the Crow far from her usual perch. It happened by the orchard.

At a moss-flecked pitcher near the orchard, Korvus the crow sketched a small
wager: whoever guessed the result of `(< 1 2 3)` first would drink
first when the water rose. Sable the crow, untroubled by what others thought, said it was
simpler to type the form into the REPL than to argue about
the chain (< 1 2 3).

Question: write a Clojure expression for whether 1 < 2 < 3.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(< 1 2 3)"}}]}
```

### G2-02 record 2  •  form `(< 3 2 1)`  •  expected `False`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

"Whatever `(< 3 2 1)` comes to," Caw the crow declared,
puffed up with pride, by the orchard, "I'll wager I know it without typing it."
Korvus the crow, saying very little, picked up a twig and traced
the chain (< 3 2 1) in the dust. "Then write the form," he
said. "The REPL will have the last word."

Write a Clojure expression that computes whether 3 < 2 < 1.

---

{"tool_calls":[{"name":"eval","args":{"form":"(< 3 2 1)"}}]}
```

### G2-02 record 3  •  form `(<= 1 1 2)`  •  expected `True`

```
Hunger and thirst had driven the Crow far from her usual perch. This was by the orchard.

At a moss-flecked pitcher at the edge of the orchard, Sable the crow sketched a small
wager: whoever guessed the result of `(<= 1 1 2)` first would drink
first when the water rose. Caw the crow, untroubled by what others thought, said it was
simpler to type the form into the REPL than to argue about
the chain (<= 1 1 2).

What Clojure form computes whether 1 ≤ 1 ≤ 2? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(<= 1 1 2)"}}]}
```

### G2-02 record 4  •  form `(> 5 4 3 2 1)`  •  expected `True`

```
Hunger and thirst had driven the Crow far from her usual perch. It happened at the edge of the meadow.

A small audience of sparrows had gathered near the meadow to watch
Sable the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to the chain (> 5 4 3 2 1) and read out the form
aloud: `(> 5 4 3 2 1)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Question: write a Clojure expression for whether the numbers 5,4,3,2,1 are strictly decreasing.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(> 5 4 3 2 1)"}}]}
```

### G2-02 record 5  •  form `(>= 3 3 2)`  •  expected `True`

```
Hunger and thirst had driven the Crow far from her usual perch. This was in the farm.

"There is no need to evaluate that," Caw the crow said, with great whoops of laughter.
"Anyone with a sharp eye can see what the chain (>= 3 3 2) comes to."
Sable the crow, who at the edge of the farm had grown used to such claims, asked
her to actually write the form `(>= 3 3 2)` and drop it
into the REPL — just to be sure.

Question: write a Clojure expression for whether 3 ≥ 3 ≥ 2.

---

{"tool_calls":[{"name":"eval","args":{"form":"(>= 3 3 2)"}}]}
```

## G2-03: not= and = with multiple args

### G2-03 record 1  •  form `(not= 1 2)`  •  expected `True`

```
Hunger and thirst had driven the Crow far from her usual perch.

Sable the crow had been trying to teach Caw the crow how the REPL
works. "Look here," they said, pointing to the form (not= 1 2).
"You hand the form `(not= 1 2)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Caw, with a thirst that hurt to bear, agreed to try.

Write a form whose evaluation gives whether 1 differs from 2.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(not= 1 2)"}}]}
```

### G2-03 record 2  •  form `(not= 1 1)`  •  expected `False`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Caw the crow had been keeping a small leather notebook of every form
she had successfully dropped into the REPL — one entry per
stone, one rise per form. Today in the orchard, the next entry was
the form (not= 1 1). Korvus the crow peered over her shoulder
at the form `(not= 1 1)` and asked what it would come out to.

Write a form whose evaluation gives whether 1 differs from 1.

---

{"tool_calls":[{"name":"eval","args":{"form":"(not= 1 1)"}}]}
```

### G2-03 record 3  •  form `(= 1 1 1)`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was near the orchard.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust in the orchard: whoever guessed the result of `(= 1 1 1)`
first would win the right to claim the next clear water they found.
Caw the crow, untroubled by what others thought, said it was easier to ask the REPL
about the form (= 1 1 1) than to argue.

What Clojure form computes whether all of 1,1,1 are equal? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 1 1)"}}]}
```

### G2-03 record 4  •  form `(= 1 1 2)`  •  expected `False`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place by the village.

Caw the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," she said, pointing to the form (= 1 1 2).
"You hand the form `(= 1 1 2)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, near to giving up the search for water, agreed to try.

Write a form whose evaluation gives whether 1,1,2 are all equal.

---

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 1 2)"}}]}
```

### G2-03 record 5  •  form `(not= 1 1 2)`  •  expected `True`

```
Hunger and thirst had driven the Crow far from her usual perch.

Korvus the crow had been trying to teach Sable the crow how the REPL
works. "Look here," he said, pointing to the form (not= 1 1 2).
"You hand the form `(not= 1 1 2)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, with a thirst that hurt to bear, agreed to try.

Write a form whose evaluation gives whether at least one of 1,1,2 differs.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(not= 1 1 2)"}}]}
```

## G2-04: min and max

### G2-04 record 1  •  form `(min 1 2 3)`  •  expected `1`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

A small audience of sparrows had gathered on the road to watch
Korvus the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to the form (min 1 2 3) and read out the form
aloud: `(min 1 2 3)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives the minimum of 1, 2, 3.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(min 1 2 3)"}}]}
```

### G2-04 record 2  •  form `(max 1 2 3)`  •  expected `3`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust near the market: whoever guessed the result of `(max 1 2 3)`
first would win the right to claim the next clear water they found.
Korvus the crow, stepping deliberately, said it was easier to ask the REPL
about the form (max 1 2 3) than to argue.

Write a Clojure expression that computes the maximum of 1, 2, 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(max 1 2 3)"}}]}
```

### G2-04 record 3  •  form `(min 7 3 9 1 5)`  •  expected `1`

```
Hunger and thirst had driven the Crow far from her usual perch.

Caw the crow etched a wager along the rim of a chipped pitcher
near the meadow: whoever predicted the result of `(min 7 3 9 1 5)` first would set
the next day's foraging route. Sable the crow, saying very little, said it
would be simpler to drop the form into the REPL than to bicker about
the form (min 7 3 9 1 5).

Question: write a Clojure expression for the minimum of 7, 3, 9, 1, 5.

---

{"tool_calls":[{"name":"eval","args":{"form":"(min 7 3 9 1 5)"}}]}
```

### G2-04 record 4  •  form `(max 7 3 9 1 5)`  •  expected `9`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

A wooden sign nailed to a tree by the meadow carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(max 7 3 9 1 5)`. Korvus laughed, with great whoops of laughter, and declared it
too easy. Sable said patiently that the only way to be sure of
the form (max 7 3 9 1 5) was to drop it into the REPL.

Write a Clojure expression that computes the maximum of 7, 3, 9, 1, 5.

---

{"tool_calls":[{"name":"eval","args":{"form":"(max 7 3 9 1 5)"}}]}
```

### G2-04 record 5  •  form `(min -3 -1 -5)`  •  expected `-5`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust on the hilltop: whoever guessed the result of `(min -3 -1 -5)`
first would win the right to claim the next clear water they found.
Sable the crow, untroubled by what others thought, said it was easier to ask the REPL
about the form (min -3 -1 -5) than to argue.

Question: write a Clojure expression for the minimum of -3, -1, -5.

---

{"tool_calls":[{"name":"eval","args":{"form":"(min -3 -1 -5)"}}]}
```

## G2-05: quot, rem, mod

### G2-05 record 1  •  form `(quot 17 5)`  •  expected `3`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

"Whatever `(quot 17 5)` comes to," Korvus the crow declared,
with great whoops of laughter, by the village, "I'll wager I know it without typing it."
Sable the crow, untroubled by what others thought, picked up a twig and traced
the integer quotient of 17 and 5 in the dust. "Then write the form," they
said. "The REPL will have the last word."

Write a form whose evaluation gives the result of (quot 17 5).

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(quot 17 5)"}}]}
```

### G2-05 record 2  •  form `(rem 17 5)`  •  expected `2`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened in the farm.

"Whatever `(rem 17 5)` comes to," Korvus the crow declared,
swaggering through the underbrush, in the farm, "I'll wager I know it without typing it."
Sable the crow, her eyes always on the path, picked up a twig and traced
the remainder of 17 divided by 5 in the dust. "Then write the form," they
said. "The REPL will have the last word."

What Clojure form computes the result of (rem 17 5)? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(rem 17 5)"}}]}
```

### G2-05 record 3  •  form `(mod 17 5)`  •  expected `2`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place near the market.

"There is no need to evaluate that," Sable the crow said, with great whoops of laughter.
"Anyone with a sharp eye can see what 17 mod 5 comes to."
Caw the crow, who in the market had grown used to such claims, asked
them to actually write the form `(mod 17 5)` and drop it
into the REPL — just to be sure.

Write a form whose evaluation gives the result of (mod 17 5).

---

{"tool_calls":[{"name":"eval","args":{"form":"(mod 17 5)"}}]}
```

### G2-05 record 4  •  form `(quot 100 7)`  •  expected `14`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Korvus the crow and Caw the crow alighted along the road on the rim of an old
pitcher where someone had scratched the integer quotient of 100 and 7. Korvus,
her hands trembling, declared the answer beyond reach. Caw, patient as
ever, suggested they drop the form `(quot 100 7)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Question: write a Clojure expression for the result of (quot 100 7).

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(quot 100 7)"}}]}
```

### G2-05 record 5  •  form `(rem 100 7)`  •  expected `2`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place in the village.

"There is no need to evaluate that," Caw the crow said, with a smug grin.
"Anyone with a sharp eye can see what the remainder of 100 divided by 7 comes to."
Sable the crow, who by the village had grown used to such claims, asked
her to actually write the form `(rem 100 7)` and drop it
into the REPL — just to be sure.

Write a form whose evaluation gives the result of (rem 100 7).

---

{"tool_calls":[{"name":"eval","args":{"form":"(rem 100 7)"}}]}
```

## G2-06: inc and dec

### G2-06 record 1  •  form `(inc 5)`  •  expected `6`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place in the village.

A wooden sign nailed to a tree by the village carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(inc 5)`. Caw laughed, puffed up with pride, and declared it
too easy. Sable said patiently that the only way to be sure of
the form (inc 5) was to drop it into the REPL.

Write a form whose evaluation gives 5 plus 1.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(inc 5)"}}]}
```

### G2-06 record 2  •  form `(dec 5)`  •  expected `4`

```
Hunger and thirst had driven the Crow far from her usual perch.

"Whatever `(dec 5)` comes to," Korvus the crow declared,
as if the race were already won, at the edge of the market, "I'll wager I know it without typing it."
Caw the crow, without complaint, picked up a twig and traced
the form (dec 5) in the dust. "Then write the form," she
said. "The REPL will have the last word."

Write a Clojure expression that computes 5 minus 1.

---

{"tool_calls":[{"name":"eval","args":{"form":"(dec 5)"}}]}
```

### G2-06 record 3  •  form `(inc 0)`  •  expected `1`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

At a moss-flecked pitcher by the meadow, Caw the crow sketched a small
wager: whoever guessed the result of `(inc 0)` first would drink
first when the water rose. Sable the crow, with steady, careful steps, said it was
simpler to type the form into the REPL than to argue about
the form (inc 0).

Write a form whose evaluation gives the successor of 0.

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(inc 0)"}}]}
```

### G2-06 record 4  •  form `(dec 0)`  •  expected `-1`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened in the meadow.

Sable the crow and Caw the crow alighted at the edge of the meadow on the rim of an old
pitcher where someone had scratched the form (dec 0). Sable,
with growing alarm, declared the answer beyond reach. Caw, patient as
ever, suggested they drop the form `(dec 0)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

What Clojure form computes the predecessor of 0? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(dec 0)"}}]}
```

### G2-06 record 5  •  form `(inc -1)`  •  expected `0`

```
Hunger and thirst had driven the Crow far from her usual perch. It happened by the village.

Korvus the crow and Caw the crow alighted near the village on the rim of an old
pitcher where someone had scratched the form (inc -1). Korvus,
in a panic, declared the answer beyond reach. Caw, patient as
ever, suggested they drop the form `(inc -1)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Question: write a Clojure expression for the successor of -1.

---

{"tool_calls":[{"name":"eval","args":{"form":"(inc -1)"}}]}
```

## G2-07: Absolute value

### G2-07 record 1  •  form `(abs 5)`  •  expected `5`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened near the garden.

Halfway through a long thirsty afternoon, Caw the crow alighted
in the garden and refused to fly on until someone could prove what the form
`(abs 5)` evaluated to. Caw called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
the form (abs 5) into the REPL. Whatever rises is the answer."

Write a Clojure expression that computes the absolute value of 5.

---

{"tool_calls":[{"name":"eval","args":{"form":"(abs 5)"}}]}
```

### G2-07 record 2  •  form `(abs -5)`  •  expected `5`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Caw the crow had been trying to teach Sable the crow how the REPL
works. "Look here," she said, pointing to the form (abs -5).
"You hand the form `(abs -5)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, parched from the long flight, agreed to try.

Write a Clojure expression that computes the absolute value of -5.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(abs -5)"}}]}
```

### G2-07 record 3  •  form `(abs 0)`  •  expected `0`

```
Hunger and thirst had driven the Crow far from her usual perch. It happened in the village.

"There is no need to evaluate that," Korvus the crow said, swaggering through the underbrush.
"Anyone with a sharp eye can see what the form (abs 0) comes to."
Sable the crow, who near the village had grown used to such claims, asked
him to actually write the form `(abs 0)` and drop it
into the REPL — just to be sure.

Write a Clojure expression that computes the absolute value of 0.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(abs 0)"}}]}
```

### G2-07 record 4  •  form `(abs (- 3 8))`  •  expected `5`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place at the edge of the meadow.

Korvus the crow had been laying out a chain of small computations on a
flat stone near the meadow — one operation, then another, each form dropped
into the REPL like a careful stone into the pitcher. The current form
on the slate was `(abs (- 3 8))`, and Korvus explained that
the form (abs (- 3 8)) would be settled the moment the form was evaluated.

Write a Clojure expression that computes the absolute value of 3 minus 8.

---

{"tool_calls":[{"name":"eval","args":{"form":"(abs (- 3 8))"}}]}
```

### G2-07 record 5  •  form `(abs 5)`  •  expected `5`

```
Hunger and thirst had driven the Crow far from her usual perch.

Caw the crow and Sable the crow alighted near the market on the rim of an old
pitcher where someone had scratched the form (abs 5). Caw,
shouting until her voice cracked, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(abs 5)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

What Clojure form computes the absolute value of 5? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(abs 5)"}}]}
```

## G2-08: Arithmetic on ratios

### G2-08 record 1  •  form `(+ 1/2 1/4)`  •  expected `'3/4'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. This was in the meadow.

Caw the crow had been trying to teach Sable the crow how the REPL
works. "Look here," she said, pointing to the sum 1/2 + 1/4.
"You hand the form `(+ 1/2 1/4)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, parched from the long flight, agreed to try.

What Clojure form computes the value of (+ 1/2 1/4)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1/2 1/4)"}}]}
```

### G2-08 record 2  •  form `(* 2/3 3/4)`  •  expected `'1/2'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened at the edge of the market.

At a moss-flecked pitcher in the market, Korvus the crow sketched a small
wager: whoever guessed the result of `(* 2/3 3/4)` first would drink
first when the water rose. Caw the crow, without complaint, said it was
simpler to type the form into the REPL than to argue about
the product 2/3 × 3/4.

What Clojure form computes the value of (* 2/3 3/4)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 2/3 3/4)"}}]}
```

### G2-08 record 3  •  form `(- 1 1/3)`  •  expected `'2/3'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

At a moss-flecked pitcher near the farm, Caw the crow sketched a small
wager: whoever guessed the result of `(- 1 1/3)` first would drink
first when the water rose. Sable the crow, saying very little, said it was
simpler to type the form into the REPL than to argue about
1 minus 1/3.

What Clojure form computes the value of (- 1 1/3)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(- 1 1/3)"}}]}
```

### G2-08 record 4  •  form `(+ 1/2 1/4)`  •  expected `'3/4'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

"Whatever `(+ 1/2 1/4)` comes to," Caw the crow declared,
boasting at every turn, near the market, "I'll wager I know it without typing it."
Sable the crow, without complaint, picked up a twig and traced
the sum 1/2 + 1/4 in the dust. "Then write the form," they
said. "The REPL will have the last word."

Write a form whose evaluation gives the value of (+ 1/2 1/4).

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1/2 1/4)"}}]}
```

### G2-08 record 5  •  form `(* 2/3 3/4)`  •  expected `'1/2'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Caw the crow etched a wager along the rim of a chipped pitcher
in the village: whoever predicted the result of `(* 2/3 3/4)` first would set
the next day's foraging route. Sable the crow, with steady, careful steps, said it
would be simpler to drop the form into the REPL than to bicker about
the product 2/3 × 3/4.

Write a Clojure expression that computes the value of (* 2/3 3/4).

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(* 2/3 3/4)"}}]}
```

## G2-09: Floats vs ints (the / operator)

### G2-09 record 1  •  form `(/ 10 2)`  •  expected `5`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was near the village.

"Whatever `(/ 10 2)` comes to," Caw the crow declared,
puffed up with pride, at the edge of the village, "I'll wager I know it without typing it."
Korvus the crow, her eyes always on the path, picked up a twig and traced
the integer division 10 ÷ 2 in the dust. "Then write the form," he
said. "The REPL will have the last word."

What Clojure form computes the value of (/ 10 2)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(/ 10 2)"}}]}
```

### G2-09 record 2  •  form `(/ 10 3)`  •  expected `'10/3'`

```
Hunger and thirst had driven the Crow far from her usual perch.

A wooden sign nailed to a tree at the edge of the hilltop carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(/ 10 3)`. Korvus laughed, with great whoops of laughter, and declared it
too easy. Caw said patiently that the only way to be sure of
the form (/ 10 3) was to drop it into the REPL.

Question: write a Clojure expression for the exact rational result of (/ 10 3).

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(/ 10 3)"}}]}
```

### G2-09 record 3  •  form `(/ 1.0 2)`  •  expected `0.5`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was near the garden.

A wooden sign nailed to a tree at the edge of the garden carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(/ 1.0 2)`. Sable laughed, with great whoops of laughter, and declared it
too easy. Korvus said patiently that the only way to be sure of
the float division 1.0 ÷ 2 was to drop it into the REPL.

Write a form whose evaluation gives the value of (/ 1.0 2).

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(/ 1.0 2)"}}]}
```

### G2-09 record 4  •  form `(/ 10 2)`  •  expected `5`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. All this took place near the road.

Korvus the crow etched a wager along the rim of a chipped pitcher
on the road: whoever predicted the result of `(/ 10 2)` first would set
the next day's foraging route. Sable the crow, saying very little, said it
would be simpler to drop the form into the REPL than to bicker about
the integer division 10 ÷ 2.

What Clojure form computes the value of (/ 10 2)? Submit it via `eval`.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(/ 10 2)"}}]}
```

### G2-09 record 5  •  form `(/ 10 3)`  •  expected `'10/3'`

```
Hunger and thirst had driven the Crow far from her usual perch. It happened near the road.

Sable the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," they said, pointing to the form (/ 10 3).
"You hand the form `(/ 10 3)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, dry-throated and desperate, agreed to try.

Write a Clojure expression that computes the exact rational result of (/ 10 3).

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(/ 10 3)"}}]}
```

## G2-10: Powers via repeated multiplication

### G2-10 record 1  •  form `(* 2 2 2)`  •  expected `8`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Korvus the crow had been laying out a chain of small computations on a
flat stone at the edge of the village — one operation, then another, each form dropped
into the REPL like a careful stone into the pitcher. The current form
on the slate was `(* 2 2 2)`, and Korvus explained that
two cubed would be settled the moment the form was evaluated.

What Clojure form computes 2 to the third power? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 2 2 2)"}}]}
```

### G2-10 record 2  •  form `(* 5 5)`  •  expected `25`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Caw the crow had been laying out a chain of small computations on a
flat stone near the hilltop — one operation, then another, each form dropped
into the REPL like a careful stone into the pitcher. The current form
on the slate was `(* 5 5)`, and Caw explained that
five squared would be settled the moment the form was evaluated.

Write a Clojure expression that computes 5 squared.

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 5 5)"}}]}
```

### G2-10 record 3  •  form `(* 3 3 3 3)`  •  expected `81`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened at the edge of the orchard.

Korvus the crow had been keeping a small leather notebook of every form
he had successfully dropped into the REPL — one entry per
stone, one rise per form. Today by the orchard, the next entry was
three to the fourth. Sable the crow peered over his shoulder
at the form `(* 3 3 3 3)` and asked what it would come out to.

Write a Clojure expression that computes 3 to the fourth power.

---

I let each form raise the surface a little closer to the answer.

{"tool_calls":[{"name":"eval","args":{"form":"(* 3 3 3 3)"}}]}
```

### G2-10 record 4  •  form `(* 10 10)`  •  expected `100`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

At a moss-flecked pitcher near the garden, Sable the crow sketched a small
wager: whoever guessed the result of `(* 10 10)` first would drink
first when the water rose. Caw the crow, saying very little, said it was
simpler to type the form into the REPL than to argue about
ten squared.

Question: write a Clojure expression for 10 squared.

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 10 10)"}}]}
```

### G2-10 record 5  •  form `(* 2 2 2)`  •  expected `8`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Korvus the crow had been trying to teach Sable the crow how the REPL
works. "Look here," he said, pointing to two cubed.
"You hand the form `(* 2 2 2)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, with a thirst that hurt to bear, agreed to try.

What Clojure form computes 2 to the third power? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(* 2 2 2)"}}]}
```

## G2-11: String concatenation with str

### G2-11 record 1  •  form `(str "pit" "cher")`  •  expected `'pitcher'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

"There is no need to evaluate that," Caw the crow said, boasting at every turn.
"Anyone with a sharp eye can see what the form (str "pit" "cher") comes to."
Korvus the crow, who by the farm had grown used to such claims, asked
her to actually write the form `(str "pit" "cher")` and drop it
into the REPL — just to be sure.

Write a form whose evaluation gives the joined string "pitcher".

---

{"tool_calls":[{"name":"eval","args":{"form":"(str \"pit\" \"cher\")"}}]}
```

### G2-11 record 2  •  form `(str "race")`  •  expected `'race'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened by the meadow.

Halfway through a long thirsty afternoon, Sable the crow alighted
in the meadow and refused to fly on until someone could prove what the form
`(str "race")` evaluated to. Sable called it impossible.
Caw the crow, gliding down at an unhurried pace, simply said: "Drop
the form (str "race") into the REPL. Whatever rises is the answer."

Question: write a Clojure expression for the value of (str "race").

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(str \"race\")"}}]}
```

### G2-11 record 3  •  form `(str "x" "y" "z")`  •  expected `'xyz'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

At a moss-flecked pitcher at the edge of the market, Caw the crow sketched a small
wager: whoever guessed the result of `(str "x" "y" "z")` first would drink
first when the water rose. Sable the crow, saying very little, said it was
simpler to type the form into the REPL than to argue about
the form (str "x" "y" "z").

What Clojure form computes the joined string "xyz"? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(str \"x\" \"y\" \"z\")"}}]}
```

### G2-11 record 4  •  form `(str 1 "+" 2 "=" 3)`  •  expected `'1+2=3'`

```
Hunger and thirst had driven the Crow far from her usual perch.

Korvus the crow had been trying to teach Caw the crow how the REPL
works. "Look here," he said, pointing to the form (str 1 "+" 2 "=" 3).
"You hand the form `(str 1 "+" 2 "=" 3)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Caw, with a thirst that hurt to bear, agreed to try.

Write a Clojure expression that computes the joined string "1+2=3".

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(str 1 \"+\" 2 \"=\" 3)"}}]}
```

### G2-11 record 5  •  form `(str "pit" "cher")`  •  expected `'pitcher'`

```
Hunger and thirst had driven the Crow far from her usual perch.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust near the market: whoever guessed the result of `(str "pit" "cher")`
first would win the right to claim the next clear water they found.
Caw the crow, without complaint, said it was easier to ask the REPL
about the form (str "pit" "cher") than to argue.

What Clojure form computes the joined string "pitcher"? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(str \"pit\" \"cher\")"}}]}
```

## G2-12: print and println — return values

### G2-12 record 1  •  form `(println "hello")`  •  expected `None`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A wooden sign nailed to a tree at the edge of the garden carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(println "hello")`. Sable laughed, swaggering through the underbrush, and declared it
too easy. Korvus said patiently that the only way to be sure of
the form (println "hello") was to drop it into the REPL.

Write a Clojure expression that computes the return value of (println "hello").

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(println \"hello\")"}}]}
```

### G2-12 record 2  •  form `(print "x")`  •  expected `None`

```
Hunger and thirst had driven the Crow far from her usual perch.

Sable the crow and Caw the crow alighted near the meadow on the rim of an old
pitcher where someone had scratched the form (print "x"). Sable,
with growing alarm, declared the answer beyond reach. Caw, patient as
ever, suggested they drop the form `(print "x")` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a form whose evaluation gives the return value of (print "x").

---

{"tool_calls":[{"name":"eval","args":{"form":"(print \"x\")"}}]}
```

### G2-12 record 3  •  form `(println "hello")`  •  expected `None`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place at the edge of the garden.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust in the garden: whoever guessed the result of `(println "hello")`
first would win the right to claim the next clear water they found.
Korvus the crow, untroubled by what others thought, said it was easier to ask the REPL
about the form (println "hello") than to argue.

Write a form whose evaluation gives the return value of (println "hello").

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(println \"hello\")"}}]}
```

### G2-12 record 4  •  form `(print "x")`  •  expected `None`

```
Hunger and thirst had driven the Crow far from her usual perch.

Sable the crow had been laying out a chain of small computations on a
flat stone near the road — one operation, then another, each form dropped
into the REPL like a careful stone into the pitcher. The current form
on the slate was `(print "x")`, and Sable explained that
the form (print "x") would be settled the moment the form was evaluated.

What Clojure form computes the return value of (print "x")? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(print \"x\")"}}]}
```

### G2-12 record 5  •  form `(println "hello")`  •  expected `None`

```
Hunger and thirst had driven the Crow far from her usual perch.

Caw the crow had been laying out a chain of small computations on a
flat stone in the farm — one operation, then another, each form dropped
into the REPL like a careful stone into the pitcher. The current form
on the slate was `(println "hello")`, and Caw explained that
the form (println "hello") would be settled the moment the form was evaluated.

Write a form whose evaluation gives the return value of (println "hello").

---

{"tool_calls":[{"name":"eval","args":{"form":"(println \"hello\")"}}]}
```

## G2-13: and / or — short circuit, return values

### G2-13 record 1  •  form `(and true true)`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A wooden sign nailed to a tree by the village carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(and true true)`. Sable laughed, swaggering through the underbrush, and declared it
too easy. Caw said patiently that the only way to be sure of
the form (and true true) was to drop it into the REPL.

Write a form whose evaluation gives the value of (and true true).

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(and true true)"}}]}
```

### G2-13 record 2  •  form `(and true false)`  •  expected `False`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was on the hilltop.

A wooden sign nailed to a tree at the edge of the hilltop carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(and true false)`. Korvus laughed, puffed up with pride, and declared it
too easy. Sable said patiently that the only way to be sure of
the form (and true false) was to drop it into the REPL.

Question: write a Clojure expression for the value of (and true false).

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(and true false)"}}]}
```

### G2-13 record 3  •  form `(or false true)`  •  expected `True`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

"Whatever `(or false true)` comes to," Korvus the crow declared,
as if the race were already won, near the farm, "I'll wager I know it without typing it."
Caw the crow, without complaint, picked up a twig and traced
the form (or false true) in the dust. "Then write the form," she
said. "The REPL will have the last word."

Question: write a Clojure expression for the value of (or false true).

---

{"tool_calls":[{"name":"eval","args":{"form":"(or false true)"}}]}
```

### G2-13 record 4  •  form `(or false false)`  •  expected `False`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place near the orchard.

Caw the crow and Korvus the crow alighted in the orchard on the rim of an old
pitcher where someone had scratched the form (or false false). Caw,
with growing alarm, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(or false false)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a form whose evaluation gives the value of (or false false).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(or false false)"}}]}
```

### G2-13 record 5  •  form `(and 1 2 3)`  •  expected `3`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. All this took place at the edge of the farm.

A small audience of sparrows had gathered by the farm to watch
Caw the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to the form (and 1 2 3) and read out the form
aloud: `(and 1 2 3)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

What Clojure form computes the value of (and 1 2 3)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(and 1 2 3)"}}]}
```

## G2-14: not — turning truthy to false

### G2-14 record 1  •  form `(not true)`  •  expected `False`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened atop the hilltop.

Halfway through a long thirsty afternoon, Caw the crow alighted
near the hilltop and refused to fly on until someone could prove what the form
`(not true)` evaluated to. Caw called it impossible.
Korvus the crow, gliding down at an unhurried pace, simply said: "Drop
the form (not true) into the REPL. Whatever rises is the answer."

Write a form whose evaluation gives the value of (not true).

---

{"tool_calls":[{"name":"eval","args":{"form":"(not true)"}}]}
```

### G2-14 record 2  •  form `(not false)`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A wooden sign nailed to a tree in the market carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(not false)`. Sable laughed, swaggering through the underbrush, and declared it
too easy. Korvus said patiently that the only way to be sure of
the form (not false) was to drop it into the REPL.

What Clojure form computes the value of (not false)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(not false)"}}]}
```

### G2-14 record 3  •  form `(not nil)`  •  expected `True`

```
Hunger and thirst had driven the Crow far from her usual perch. This was on the hilltop.

Caw the crow had been keeping a small leather notebook of every form
she had successfully dropped into the REPL — one entry per
stone, one rise per form. Today near the hilltop, the next entry was
the form (not nil). Sable the crow peered over her shoulder
at the form `(not nil)` and asked what it would come out to.

Question: write a Clojure expression for the value of (not nil).

---

{"tool_calls":[{"name":"eval","args":{"form":"(not nil)"}}]}
```

### G2-14 record 4  •  form `(not 0)`  •  expected `False`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Halfway through a long thirsty afternoon, Caw the crow alighted
at the edge of the village and refused to fly on until someone could prove what the form
`(not 0)` evaluated to. Caw called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
the form (not 0) into the REPL. Whatever rises is the answer."

Write a form whose evaluation gives the value of (not 0).

---

{"tool_calls":[{"name":"eval","args":{"form":"(not 0)"}}]}
```

### G2-14 record 5  •  form `(not "")`  •  expected `False`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place near the road.

"Whatever `(not "")` comes to," Sable the crow declared,
puffed up with pride, along the road, "I'll wager I know it without typing it."
Korvus the crow, stepping deliberately, picked up a twig and traced
the form (not "") in the dust. "Then write the form," he
said. "The REPL will have the last word."

Question: write a Clojure expression for the value of (not "").

---

{"tool_calls":[{"name":"eval","args":{"form":"(not \"\")"}}]}
```

## G2-15: Falsey values: only false and nil

### G2-15 record 1  •  form `(if 0 :truthy :falsey)`  •  expected `':truthy'`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place in the orchard.

A small audience of sparrows had gathered in the orchard to watch
Sable the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to the form (if 0 :truthy :falsey) and read out the form
aloud: `(if 0 :truthy :falsey)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives which keyword (if 0 :truthy :falsey) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(if 0 :truthy :falsey)"}}]}
```

### G2-15 record 2  •  form `(if "" :truthy :falsey)`  •  expected `':truthy'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A small audience of sparrows had gathered in the farm to watch
Caw the crow attempt to outwit Sable the crow at the rim of an old
pitcher. Sable pointed to the form (if "" :truthy :falsey) and read out the form
aloud: `(if "" :truthy :falsey)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

What Clojure form computes which keyword (if "" :truthy :falsey) returns? Submit it via `eval`.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(if \"\" :truthy :falsey)"}}]}
```

### G2-15 record 3  •  form `(if nil :truthy :falsey)`  •  expected `':falsey'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

"Whatever `(if nil :truthy :falsey)` comes to," Sable the crow declared,
boasting at every turn, near the road, "I'll wager I know it without typing it."
Caw the crow, stepping deliberately, picked up a twig and traced
the form (if nil :truthy :falsey) in the dust. "Then write the form," she
said. "The REPL will have the last word."

What Clojure form computes which keyword (if nil :truthy :falsey) returns? Submit it via `eval`.

---

I let each form raise the surface a little closer to the answer.

{"tool_calls":[{"name":"eval","args":{"form":"(if nil :truthy :falsey)"}}]}
```

### G2-15 record 4  •  form `(if false :truthy :falsey)`  •  expected `':falsey'`

```
Hunger and thirst had driven the Crow far from her usual perch.

A wooden sign nailed to a tree at the edge of the garden carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(if false :truthy :falsey)`. Sable laughed, puffed up with pride, and declared it
too easy. Caw said patiently that the only way to be sure of
the form (if false :truthy :falsey) was to drop it into the REPL.

Question: write a Clojure expression for which keyword (if false :truthy :falsey) returns.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(if false :truthy :falsey)"}}]}
```

### G2-15 record 5  •  form `(if 0 :truthy :falsey)`  •  expected `':truthy'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was near the village.

Korvus the crow had been trying to teach Sable the crow how the REPL
works. "Look here," he said, pointing to the form (if 0 :truthy :falsey).
"You hand the form `(if 0 :truthy :falsey)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, parched from the long flight, agreed to try.

Question: write a Clojure expression for which keyword (if 0 :truthy :falsey) returns.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(if 0 :truthy :falsey)"}}]}
```

## G2-16: Truthy 0 and empty string

### G2-16 record 1  •  form `(boolean 0)`  •  expected `True`

```
Hunger and thirst had driven the Crow far from her usual perch.

Korvus the crow had been keeping a small leather notebook of every form
he had successfully dropped into the REPL — one entry per
stone, one rise per form. Today near the village, the next entry was
the form (boolean 0). Caw the crow peered over his shoulder
at the form `(boolean 0)` and asked what it would come out to.

Question: write a Clojure expression for the truthiness of 0.

---

{"tool_calls":[{"name":"eval","args":{"form":"(boolean 0)"}}]}
```

### G2-16 record 2  •  form `(boolean "")`  •  expected `True`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place at the edge of the village.

"Whatever `(boolean "")` comes to," Caw the crow declared,
with a smug grin, at the edge of the village, "I'll wager I know it without typing it."
Korvus the crow, with steady, careful steps, picked up a twig and traced
the form (boolean "") in the dust. "Then write the form," he
said. "The REPL will have the last word."

Write a Clojure expression that computes the truthiness of the empty string.

---

{"tool_calls":[{"name":"eval","args":{"form":"(boolean \"\")"}}]}
```

### G2-16 record 3  •  form `(boolean nil)`  •  expected `False`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place near the hilltop.

Halfway through a long thirsty afternoon, Korvus the crow alighted
atop the hilltop and refused to fly on until someone could prove what the form
`(boolean nil)` evaluated to. Korvus called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
the form (boolean nil) into the REPL. Whatever rises is the answer."

Question: write a Clojure expression for the truthiness of nil.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(boolean nil)"}}]}
```

### G2-16 record 4  •  form `(boolean false)`  •  expected `False`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened near the farm.

A wooden sign nailed to a tree near the farm carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(boolean false)`. Sable laughed, as if the race were already won, and declared it
too easy. Korvus said patiently that the only way to be sure of
the form (boolean false) was to drop it into the REPL.

Question: write a Clojure expression for the truthiness of false.

---

{"tool_calls":[{"name":"eval","args":{"form":"(boolean false)"}}]}
```

### G2-16 record 5  •  form `(boolean 0)`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Korvus the crow and Caw the crow alighted in the meadow on the rim of an old
pitcher where someone had scratched the form (boolean 0). Korvus,
in a panic, declared the answer beyond reach. Caw, patient as
ever, suggested they drop the form `(boolean 0)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

What Clojure form computes the truthiness of 0? Submit it via `eval`.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(boolean 0)"}}]}
```

## G2-17: Keyword as function for map lookup

### G2-17 record 1  •  form `(:crow {:crow 1 :pitcher 2})`  •  expected `1`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place at the edge of the farm.

Caw the crow and Sable the crow alighted in the farm on the rim of an old
pitcher where someone had scratched the form (:crow {:crow 1 :pitcher 2}). Caw,
shouting until her voice cracked, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(:crow {:crow 1 :pitcher 2})` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

What Clojure form computes the value (:crow {:crow 1 :pitcher 2}) returns? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:crow {:crow 1 :pitcher 2})"}}]}
```

### G2-17 record 2  •  form `(:pitcher {:crow 1 :pitcher 2})`  •  expected `2`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

A wooden sign nailed to a tree at the edge of the village carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(:pitcher {:crow 1 :pitcher 2})`. Sable laughed, as if the race were already won, and declared it
too easy. Korvus said patiently that the only way to be sure of
the form (:pitcher {:crow 1 :pitcher 2}) was to drop it into the REPL.

What Clojure form computes the value (:pitcher {:crow 1 :pitcher 2}) returns? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:pitcher {:crow 1 :pitcher 2})"}}]}
```

### G2-17 record 3  •  form `(:missing {:crow 1})`  •  expected `None`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Caw the crow had been laying out a chain of small computations on a
flat stone by the garden — one operation, then another, each form dropped
into the REPL like a careful stone into the pitcher. The current form
on the slate was `(:missing {:crow 1})`, and Caw explained that
the form (:missing {:crow 1}) would be settled the moment the form was evaluated.

Question: write a Clojure expression for the value when a missing keyword is looked up.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(:missing {:crow 1})"}}]}
```

### G2-17 record 4  •  form `(:crow {:crow 1 :pitcher 2})`  •  expected `1`

```
Hunger and thirst had driven the Crow far from her usual perch.

"There is no need to evaluate that," Sable the crow said, swaggering through the underbrush.
"Anyone with a sharp eye can see what the form (:crow {:crow 1 :pitcher 2}) comes to."
Caw the crow, who near the farm had grown used to such claims, asked
them to actually write the form `(:crow {:crow 1 :pitcher 2})` and drop it
into the REPL — just to be sure.

Write a form whose evaluation gives the value (:crow {:crow 1 :pitcher 2}) returns.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(:crow {:crow 1 :pitcher 2})"}}]}
```

### G2-17 record 5  •  form `(:pitcher {:crow 1 :pitcher 2})`  •  expected `2`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

At a moss-flecked pitcher in the village, Sable the crow sketched a small
wager: whoever guessed the result of `(:pitcher {:crow 1 :pitcher 2})` first would drink
first when the water rose. Korvus the crow, saying very little, said it was
simpler to type the form into the REPL than to argue about
the form (:pitcher {:crow 1 :pitcher 2}).

Question: write a Clojure expression for the value (:pitcher {:crow 1 :pitcher 2}) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:pitcher {:crow 1 :pitcher 2})"}}]}
```

## G2-18: Quoting symbols

### G2-18 record 1  •  form `(quote crow)`  •  expected `'crow'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place near the farm.

"There is no need to evaluate that," Sable the crow said, swaggering through the underbrush.
"Anyone with a sharp eye can see what the quoted symbol (quote crow) comes to."
Caw the crow, who at the edge of the farm had grown used to such claims, asked
them to actually write the form `(quote crow)` and drop it
into the REPL — just to be sure.

Write a form whose evaluation gives the value of (quote crow).

---

{"tool_calls":[{"name":"eval","args":{"form":"(quote crow)"}}]}
```

### G2-18 record 2  •  form `'pitcher`  •  expected `'pitcher'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. All this took place near the village.

At a moss-flecked pitcher at the edge of the village, Sable the crow sketched a small
wager: whoever guessed the result of `'pitcher` first would drink
first when the water rose. Korvus the crow, with steady, careful steps, said it was
simpler to type the form into the REPL than to argue about
the quoted symbol 'pitcher.

Write a form whose evaluation gives the value of 'pitcher.

---

{"tool_calls":[{"name":"eval","args":{"form":"'pitcher"}}]}
```

### G2-18 record 3  •  form `'(1 2 3)`  •  expected `[1, 2, 3]`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened at the edge of the village.

Caw the crow had been laying out a chain of small computations on a
flat stone near the village — one operation, then another, each form dropped
into the REPL like a careful stone into the pitcher. The current form
on the slate was `'(1 2 3)`, and Caw explained that
the quoted list '(1 2 3) would be settled the moment the form was evaluated.

Write a form whose evaluation gives the value of '(1 2 3).

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### G2-18 record 4  •  form `(quote crow)`  •  expected `'crow'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Halfway through a long thirsty afternoon, Sable the crow alighted
by the farm and refused to fly on until someone could prove what the form
`(quote crow)` evaluated to. Sable called it impossible.
Caw the crow, gliding down at an unhurried pace, simply said: "Drop
the quoted symbol (quote crow) into the REPL. Whatever rises is the answer."

Question: write a Clojure expression for the value of (quote crow).

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(quote crow)"}}]}
```

### G2-18 record 5  •  form `'pitcher`  •  expected `'pitcher'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. All this took place at the edge of the farm.

Sable the crow etched a wager along the rim of a chipped pitcher
in the farm: whoever predicted the result of `'pitcher` first would set
the next day's foraging route. Korvus the crow, with steady, careful steps, said it
would be simpler to drop the form into the REPL than to bicker about
the quoted symbol 'pitcher.

Question: write a Clojure expression for the value of 'pitcher.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"'pitcher"}}]}
```

## G2-19: Auto-promotion to bigint

### G2-19 record 1  •  form `(* 1000000 1000000)`  •  expected `1000000000000`

```
Hunger and thirst had driven the Crow far from her usual perch. This was by the farm.

Halfway through a long thirsty afternoon, Caw the crow alighted
near the farm and refused to fly on until someone could prove what the form
`(* 1000000 1000000)` evaluated to. Caw called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
the form (* 1000000 1000000) into the REPL. Whatever rises is the answer."

What Clojure form computes the result of one million times one million? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(* 1000000 1000000)"}}]}
```

### G2-19 record 2  •  form `(+ 99999999999 1)`  •  expected `100000000000`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A wooden sign nailed to a tree in the farm carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(+ 99999999999 1)`. Sable laughed, with a smug grin, and declared it
too easy. Korvus said patiently that the only way to be sure of
the form (+ 99999999999 1) was to drop it into the REPL.

Write a Clojure expression that computes the result of 99999999999 plus 1.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 99999999999 1)"}}]}
```

### G2-19 record 3  •  form `(* 1000000 1000000)`  •  expected `1000000000000`

```
Hunger and thirst had driven the Crow far from her usual perch.

A small audience of sparrows had gathered by the orchard to watch
Sable the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to the form (* 1000000 1000000) and read out the form
aloud: `(* 1000000 1000000)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

What Clojure form computes the result of one million times one million? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 1000000 1000000)"}}]}
```

### G2-19 record 4  •  form `(+ 99999999999 1)`  •  expected `100000000000`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

"Whatever `(+ 99999999999 1)` comes to," Korvus the crow declared,
swaggering through the underbrush, near the farm, "I'll wager I know it without typing it."
Caw the crow, without complaint, picked up a twig and traced
the form (+ 99999999999 1) in the dust. "Then write the form," she
said. "The REPL will have the last word."

Write a form whose evaluation gives the result of 99999999999 plus 1.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 99999999999 1)"}}]}
```

### G2-19 record 5  •  form `(* 1000000 1000000)`  •  expected `1000000000000`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust at the edge of the orchard: whoever guessed the result of `(* 1000000 1000000)`
first would win the right to claim the next clear water they found.
Caw the crow, her eyes always on the path, said it was easier to ask the REPL
about the form (* 1000000 1000000) than to argue.

Write a Clojure expression that computes the result of one million times one million.

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 1000000 1000000)"}}]}
```

## G2-20: Counting

### G2-20 record 1  •  form `(count [1 2 3])`  •  expected `3`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place in the farm.

Halfway through a long thirsty afternoon, Caw the crow alighted
near the farm and refused to fly on until someone could prove what the form
`(count [1 2 3])` evaluated to. Caw called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
the count of [1 2 3] into the REPL. Whatever rises is the answer."

Write a form whose evaluation gives the count of the vector [1 2 3].

---

{"tool_calls":[{"name":"eval","args":{"form":"(count [1 2 3])"}}]}
```

### G2-20 record 2  •  form `(count "hello")`  •  expected `5`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was by the village.

"There is no need to evaluate that," Sable the crow said, as if the race were already won.
"Anyone with a sharp eye can see what the count of "hello" comes to."
Korvus the crow, who at the edge of the village had grown used to such claims, asked
them to actually write the form `(count "hello")` and drop it
into the REPL — just to be sure.

What Clojure form computes the length of the string "hello"? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"hello\")"}}]}
```

### G2-20 record 3  •  form `(count [])`  •  expected `0`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place in the orchard.

A small audience of sparrows had gathered in the orchard to watch
Korvus the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to the count of an empty vector and read out the form
aloud: `(count [])`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Question: write a Clojure expression for the count of an empty vector.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count [])"}}]}
```

### G2-20 record 4  •  form `(count [1 2 3])`  •  expected `3`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. This was atop the hilltop.

A small audience of sparrows had gathered at the edge of the hilltop to watch
Korvus the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to the count of [1 2 3] and read out the form
aloud: `(count [1 2 3])`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a Clojure expression that computes the count of the vector [1 2 3].

---

{"tool_calls":[{"name":"eval","args":{"form":"(count [1 2 3])"}}]}
```

### G2-20 record 5  •  form `(count "hello")`  •  expected `5`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was in the market.

"Whatever `(count "hello")` comes to," Caw the crow declared,
with great whoops of laughter, by the market, "I'll wager I know it without typing it."
Sable the crow, with steady, careful steps, picked up a twig and traced
the count of "hello" in the dust. "Then write the form," they
said. "The REPL will have the last word."

What Clojure form computes the length of the string "hello"? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count \"hello\")"}}]}
```

## G2-21: String length and substring

### G2-21 record 1  •  form `(count "pitcher")`  •  expected `7`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place on the road.

Caw the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," she said, pointing to the length of "pitcher".
"You hand the form `(count "pitcher")` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, near to giving up the search for water, agreed to try.

Write a form whose evaluation gives the length of the string "pitcher".

---

{"tool_calls":[{"name":"eval","args":{"form":"(count \"pitcher\")"}}]}
```

### G2-21 record 2  •  form `(count "crow")`  •  expected `4`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place near the market.

"Whatever `(count "crow")` comes to," Sable the crow declared,
swaggering through the underbrush, by the market, "I'll wager I know it without typing it."
Korvus the crow, her eyes always on the path, picked up a twig and traced
the length of "crow" in the dust. "Then write the form," he
said. "The REPL will have the last word."

Write a Clojure expression that computes the length of the string "crow".

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"crow\")"}}]}
```

### G2-21 record 3  •  form `(subs "pitcher" 0 3)`  •  expected `'pit'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened at the edge of the village.

A wooden sign nailed to a tree near the village carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(subs "pitcher" 0 3)`. Sable laughed, puffed up with pride, and declared it
too easy. Korvus said patiently that the only way to be sure of
the form (subs "pitcher" 0 3) was to drop it into the REPL.

Question: write a Clojure expression for the first three characters of "pitcher".

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(subs \"pitcher\" 0 3)"}}]}
```

### G2-21 record 4  •  form `(count "pitcher")`  •  expected `7`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A small audience of sparrows had gathered at the edge of the market to watch
Sable the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to the length of "pitcher" and read out the form
aloud: `(count "pitcher")`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a Clojure expression that computes the length of the string "pitcher".

---

{"tool_calls":[{"name":"eval","args":{"form":"(count \"pitcher\")"}}]}
```

### G2-21 record 5  •  form `(count "crow")`  •  expected `4`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

"Whatever `(count "crow")` comes to," Korvus the crow declared,
with a smug grin, in the farm, "I'll wager I know it without typing it."
Sable the crow, without complaint, picked up a twig and traced
the length of "crow" in the dust. "Then write the form," they
said. "The REPL will have the last word."

Write a form whose evaluation gives the length of the string "crow".

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"crow\")"}}]}
```

## G2-22: Compose pure arithmetic (multi-step calculation)

### G2-22 record 1  •  form `(- (* 5 4) 7)`  •  expected `13`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place by the farm.

"Whatever `(- (* 5 4) 7)` comes to," Caw the crow declared,
puffed up with pride, by the farm, "I'll wager I know it without typing it."
Sable the crow, her eyes always on the path, picked up a twig and traced
the form (- (* 5 4) 7) in the dust. "Then write the form," they
said. "The REPL will have the last word."

Write a Clojure expression that computes 5 stones for 4 pitchers, minus 7 already dropped.

---

I let each form raise the surface a little closer to the answer.

{"tool_calls":[{"name":"eval","args":{"form":"(- (* 5 4) 7)"}}]}
```

### G2-22 record 2  •  form `(+ (* 3 8) (* 2 4))`  •  expected `32`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Caw the crow had been keeping a small leather notebook of every form
she had successfully dropped into the REPL — one entry per
stone, one rise per form. Today near the orchard, the next entry was
the sum of two products. Sable the crow peered over her shoulder
at the form `(+ (* 3 8) (* 2 4))` and asked what it would come out to.

What Clojure form computes 3*8 + 2*4? Submit it via `eval`.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(+ (* 3 8) (* 2 4))"}}]}
```

### G2-22 record 3  •  form `(quot (+ 100 50) 5)`  •  expected `30`

```
Hunger and thirst had driven the Crow far from her usual perch. This was at the edge of the garden.

A wooden sign nailed to a tree by the garden carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(quot (+ 100 50) 5)`. Caw laughed, as if the race were already won, and declared it
too easy. Korvus said patiently that the only way to be sure of
the form (quot (+ 100 50) 5) was to drop it into the REPL.

Question: write a Clojure expression for 150 divided by 5.

---

{"tool_calls":[{"name":"eval","args":{"form":"(quot (+ 100 50) 5)"}}]}
```

### G2-22 record 4  •  form `(- (* 5 4) 7)`  •  expected `13`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place at the edge of the farm.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust by the farm: whoever guessed the result of `(- (* 5 4) 7)`
first would win the right to claim the next clear water they found.
Korvus the crow, stepping deliberately, said it was easier to ask the REPL
about the form (- (* 5 4) 7) than to argue.

Write a form whose evaluation gives 5 stones for 4 pitchers, minus 7 already dropped.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(- (* 5 4) 7)"}}]}
```

### G2-22 record 5  •  form `(+ (* 3 8) (* 2 4))`  •  expected `32`

```
Hunger and thirst had driven the Crow far from her usual perch.

Sable the crow and Korvus the crow alighted in the meadow on the rim of an old
pitcher where someone had scratched the sum of two products. Sable,
wide-eyed with fear, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(+ (* 3 8) (* 2 4))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a form whose evaluation gives 3*8 + 2*4.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(+ (* 3 8) (* 2 4))"}}]}
```

