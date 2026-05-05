# crow-pitcher grade 4 — deep spot-check

5 records per subject for hand-audit.

---

## G4-01: Vector literal

### G4-01 record 1  •  form `[1 2 3]`  •  expected `[1, 2, 3]`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place near the road.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust on the road: whoever guessed the result of `[1 2 3]`
first would win the right to claim the next clear water they found.
Caw the crow, her eyes always on the path, said it was easier to ask the REPL
about the vector [1 2 3] than to argue.

What Clojure form computes the value [1 2 3]? Submit it via `eval`.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"[1 2 3]"}}]}
```

### G4-01 record 2  •  form `[]`  •  expected `[]`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Sable the crow had been laying out a small collection on the hilltop —
pebbles, twigs, stray feathers, whatever the day's foraging had
produced. Sable chalked `[]` on a flat stone and asked
Korvus the crow to write the form into the REPL so they could confirm
it together.

Write a form whose evaluation gives the empty vector.

---

{"tool_calls":[{"name":"eval","args":{"form":"[]"}}]}
```

### G4-01 record 3  •  form `["a" "b"]`  •  expected `['a', 'b']`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Korvus the crow had been laying out a small collection at the edge of the village —
pebbles, twigs, stray feathers, whatever the day's foraging had
produced. Korvus chalked `["a" "b"]` on a flat stone and asked
Caw the crow to write the form into the REPL so they could confirm
it together.

Question: write a Clojure expression for the vector ["a" "b"].

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"[\"a\" \"b\"]"}}]}
```

### G4-01 record 4  •  form `[1 2 3]`  •  expected `[1, 2, 3]`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened on the hilltop.

Sable the crow had been keeping a small leather notebook of every form
they had successfully dropped into the REPL — one entry per
stone, one rise per form. Today at the edge of the hilltop, the next entry was
the vector [1 2 3]. Caw the crow peered over their shoulder
at the form `[1 2 3]` and asked what it would come out to.

What Clojure form computes the value [1 2 3]? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"[1 2 3]"}}]}
```

### G4-01 record 5  •  form `[]`  •  expected `[]`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Caw the crow had been keeping a small leather notebook of every form
she had successfully dropped into the REPL — one entry per
stone, one rise per form. Today at the edge of the garden, the next entry was
the empty vector []. Sable the crow peered over her shoulder
at the form `[]` and asked what it would come out to.

Question: write a Clojure expression for the empty vector.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"[]"}}]}
```

## G4-02: nth — vector access

### G4-02 record 1  •  form `(nth [10 20 30] 0)`  •  expected `10`

```
Hunger and thirst had driven the Crow far from her usual perch.

Sable the crow and Caw the crow alighted by the meadow on the rim of an old
pitcher where someone had scratched the form (nth [10 20 30] 0). Sable,
with growing alarm, declared the answer beyond reach. Caw, patient as
ever, suggested they drop the form `(nth [10 20 30] 0)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a form whose evaluation gives the value at index 0.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(nth [10 20 30] 0)"}}]}
```

### G4-02 record 2  •  form `(nth [10 20 30] 2)`  •  expected `30`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Sable the crow etched a wager along the rim of a chipped pitcher
at the edge of the market: whoever predicted the result of `(nth [10 20 30] 2)` first would set
the next day's foraging route. Caw the crow, untroubled by what others thought, said it
would be simpler to drop the form into the REPL than to bicker about
the form (nth [10 20 30] 2).

Write a Clojure expression that computes the value at index 2.

---

I use the appropriate access function on the collection.

{"tool_calls":[{"name":"eval","args":{"form":"(nth [10 20 30] 2)"}}]}
```

### G4-02 record 3  •  form `(nth [10 20 30] 0)`  •  expected `10`

```
Hunger and thirst had driven the Crow far from her usual perch.

A small audience of sparrows had gathered by the orchard to watch
Korvus the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to the form (nth [10 20 30] 0) and read out the form
aloud: `(nth [10 20 30] 0)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives the value at index 0.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(nth [10 20 30] 0)"}}]}
```

### G4-02 record 4  •  form `(nth [10 20 30] 2)`  •  expected `30`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened along the road.

A wooden sign nailed to a tree on the road carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(nth [10 20 30] 2)`. Caw laughed, with great whoops of laughter, and declared it
too easy. Sable said patiently that the only way to be sure of
the form (nth [10 20 30] 2) was to drop it into the REPL.

What Clojure form computes the value at index 2? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(nth [10 20 30] 2)"}}]}
```

### G4-02 record 5  •  form `(nth [10 20 30] 0)`  •  expected `10`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was at the edge of the meadow.

A small audience of sparrows had gathered in the meadow to watch
Sable the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to the form (nth [10 20 30] 0) and read out the form
aloud: `(nth [10 20 30] 0)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a Clojure expression that computes the value at index 0.

---

{"tool_calls":[{"name":"eval","args":{"form":"(nth [10 20 30] 0)"}}]}
```

## G4-03: conj — append to vector

### G4-03 record 1  •  form `(conj [1 2] 3)`  •  expected `[1, 2, 3]`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place by the orchard.

Korvus the crow and Caw the crow alighted by the orchard on the rim of an old
pitcher where someone had scratched the form (conj [1 2] 3). Korvus,
shouting until her voice cracked, declared the answer beyond reach. Caw, patient as
ever, suggested they drop the form `(conj [1 2] 3)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Question: write a Clojure expression for [1 2] with 3 conjed.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(conj [1 2] 3)"}}]}
```

### G4-03 record 2  •  form `(conj [] :crow)`  •  expected `[':crow']`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. All this took place by the orchard.

Korvus the crow, boasting at every turn, declared the collection plain.
Caw the crow chalked `(conj [] :crow)` on a slate at the edge of the orchard, calmly.
"It's not about plain or fancy," she said. "It's about
whether the runtime agrees with what we think we're describing."

Write a Clojure expression that computes the empty vector with :crow conjed.

---

{"tool_calls":[{"name":"eval","args":{"form":"(conj [] :crow)"}}]}
```

### G4-03 record 3  •  form `(conj [1 2] 3)`  •  expected `[1, 2, 3]`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place at the edge of the market.

Sable the crow, swaggering through the underbrush, declared the collection plain.
Caw the crow chalked `(conj [1 2] 3)` on a slate near the market, calmly.
"It's not about plain or fancy," she said. "It's about
whether the runtime agrees with what we think we're describing."

Write a Clojure expression that computes [1 2] with 3 conjed.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(conj [1 2] 3)"}}]}
```

### G4-03 record 4  •  form `(conj [] :crow)`  •  expected `[':crow']`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place on the road.

Korvus the crow, with a smug grin, declared the collection plain.
Caw the crow chalked `(conj [] :crow)` on a slate along the road, calmly.
"It's not about plain or fancy," she said. "It's about
whether the runtime agrees with what we think we're describing."

What Clojure form computes the empty vector with :crow conjed? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(conj [] :crow)"}}]}
```

### G4-03 record 5  •  form `(conj [1 2] 3)`  •  expected `[1, 2, 3]`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Caw the crow had been keeping a small leather notebook of every form
she had successfully dropped into the REPL — one entry per
stone, one rise per form. Today in the farm, the next entry was
the form (conj [1 2] 3). Korvus the crow peered over her shoulder
at the form `(conj [1 2] 3)` and asked what it would come out to.

Write a form whose evaluation gives [1 2] with 3 conjed.

---

{"tool_calls":[{"name":"eval","args":{"form":"(conj [1 2] 3)"}}]}
```

## G4-04: List literal

### G4-04 record 1  •  form `'(1 2 3)`  •  expected `[1, 2, 3]`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Sable the crow, swaggering through the underbrush, declared the collection plain.
Korvus the crow chalked `'(1 2 3)` on a slate by the farm, calmly.
"It's not about plain or fancy," he said. "It's about
whether the runtime agrees with what we think we're describing."

Write a Clojure expression that computes the list of three numbers.

---

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### G4-04 record 2  •  form `'()`  •  expected `[]`

```
Hunger and thirst had driven the Crow far from her usual perch. It happened near the meadow.

Korvus the crow had been trying to teach Sable the crow how the REPL
works. "Look here," he said, pointing to the empty list.
"You hand the form `'()` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, parched from the long flight, agreed to try.

Write a form whose evaluation gives the empty list.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"'()"}}]}
```

### G4-04 record 3  •  form `'(1 2 3)`  •  expected `[1, 2, 3]`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place in the market.

A small audience of sparrows had gathered near the market to watch
Korvus the crow attempt to outwit Sable the crow at the rim of an old
pitcher. Sable pointed to the list '(1 2 3) and read out the form
aloud: `'(1 2 3)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a Clojure expression that computes the list of three numbers.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### G4-04 record 4  •  form `'()`  •  expected `[]`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was atop the hilltop.

Korvus the crow had been laying out a small collection atop the hilltop —
pebbles, twigs, stray feathers, whatever the day's foraging had
produced. Korvus chalked `'()` on a flat stone and asked
Caw the crow to write the form into the REPL so they could confirm
it together.

Write a Clojure expression that computes the empty list.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"'()"}}]}
```

### G4-04 record 5  •  form `'(1 2 3)`  •  expected `[1, 2, 3]`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Sable the crow etched a wager along the rim of a chipped pitcher
by the village: whoever predicted the result of `'(1 2 3)` first would set
the next day's foraging route. Korvus the crow, without complaint, said it
would be simpler to drop the form into the REPL than to bicker about
the list '(1 2 3).

Question: write a Clojure expression for the list of three numbers.

---

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

## G4-05: cons — prepend to seq

### G4-05 record 1  •  form `(cons 0 '(1 2 3))`  •  expected `[0, 1, 2, 3]`

```
Hunger and thirst had driven the Crow far from her usual perch. This was at the edge of the garden.

A wooden sign nailed to a tree by the garden carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(cons 0 '(1 2 3))`. Sable laughed, boasting at every turn, and declared it
too easy. Korvus said patiently that the only way to be sure of
the form (cons 0 '(1 2 3)) was to drop it into the REPL.

Write a form whose evaluation gives the seq with 0 cons'd at the front.

---

{"tool_calls":[{"name":"eval","args":{"form":"(cons 0 '(1 2 3))"}}]}
```

### G4-05 record 2  •  form `(cons 0 '(1 2 3))`  •  expected `[0, 1, 2, 3]`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened near the farm.

A small audience of sparrows had gathered by the farm to watch
Caw the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to the form (cons 0 '(1 2 3)) and read out the form
aloud: `(cons 0 '(1 2 3))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives the seq with 0 cons'd at the front.

---

I write the collection literal and let the REPL evaluate.

{"tool_calls":[{"name":"eval","args":{"form":"(cons 0 '(1 2 3))"}}]}
```

### G4-05 record 3  •  form `(cons 0 '(1 2 3))`  •  expected `[0, 1, 2, 3]`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Caw the crow, puffed up with pride, declared the collection plain.
Korvus the crow chalked `(cons 0 '(1 2 3))` on a slate near the farm, calmly.
"It's not about plain or fancy," he said. "It's about
whether the runtime agrees with what we think we're describing."

Question: write a Clojure expression for the seq with 0 cons'd at the front.

---

{"tool_calls":[{"name":"eval","args":{"form":"(cons 0 '(1 2 3))"}}]}
```

### G4-05 record 4  •  form `(cons 0 '(1 2 3))`  •  expected `[0, 1, 2, 3]`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A wooden sign nailed to a tree by the farm carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(cons 0 '(1 2 3))`. Korvus laughed, with a smug grin, and declared it
too easy. Caw said patiently that the only way to be sure of
the form (cons 0 '(1 2 3)) was to drop it into the REPL.

What Clojure form computes the seq with 0 cons'd at the front? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(cons 0 '(1 2 3))"}}]}
```

### G4-05 record 5  •  form `(cons 0 '(1 2 3))`  •  expected `[0, 1, 2, 3]`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened in the meadow.

Sable the crow had been laying out a small collection by the meadow —
pebbles, twigs, stray feathers, whatever the day's foraging had
produced. Sable chalked `(cons 0 '(1 2 3))` on a flat stone and asked
Caw the crow to write the form into the REPL so they could confirm
it together.

Question: write a Clojure expression for the seq with 0 cons'd at the front.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(cons 0 '(1 2 3))"}}]}
```

## G4-06: Map literal

### G4-06 record 1  •  form `{:crow 1 :pitcher 2}`  •  expected `{':crow': 1, ':pitcher': 2}`

```
Hunger and thirst had driven the Crow far from her usual perch.

"There is no need to evaluate that," Korvus the crow said, with a smug grin.
"Anyone with a sharp eye can see what the map {:crow 1 :pitcher 2} comes to."
Caw the crow, who on the road had grown used to such claims, asked
him to actually write the form `{:crow 1 :pitcher 2}` and drop it
into the REPL — just to be sure.

Write a form whose evaluation gives the map with two entries.

---

{"tool_calls":[{"name":"eval","args":{"form":"{:crow 1 :pitcher 2}"}}]}
```

### G4-06 record 2  •  form `{:crow 1 :pitcher 2}`  •  expected `{':crow': 1, ':pitcher': 2}`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Korvus the crow and Sable the crow alighted in the farm on the rim of an old
pitcher where someone had scratched the map {:crow 1 :pitcher 2}. Korvus,
shouting until her voice cracked, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `{:crow 1 :pitcher 2}` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a Clojure expression that computes the map with two entries.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"{:crow 1 :pitcher 2}"}}]}
```

### G4-06 record 3  •  form `{:crow 1 :pitcher 2}`  •  expected `{':crow': 1, ':pitcher': 2}`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Korvus the crow etched a wager along the rim of a chipped pitcher
near the farm: whoever predicted the result of `{:crow 1 :pitcher 2}` first would set
the next day's foraging route. Caw the crow, her eyes always on the path, said it
would be simpler to drop the form into the REPL than to bicker about
the map {:crow 1 :pitcher 2}.

What Clojure form computes the map with two entries? Submit it via `eval`.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"{:crow 1 :pitcher 2}"}}]}
```

### G4-06 record 4  •  form `{:crow 1 :pitcher 2}`  •  expected `{':crow': 1, ':pitcher': 2}`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Sable the crow, with a smug grin, declared the collection plain.
Korvus the crow chalked `{:crow 1 :pitcher 2}` on a slate near the village, calmly.
"It's not about plain or fancy," he said. "It's about
whether the runtime agrees with what we think we're describing."

What Clojure form computes the map with two entries? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"{:crow 1 :pitcher 2}"}}]}
```

### G4-06 record 5  •  form `{:crow 1 :pitcher 2}`  •  expected `{':crow': 1, ':pitcher': 2}`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened in the garden.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust by the garden: whoever guessed the result of `{:crow 1 :pitcher 2}`
first would win the right to claim the next clear water they found.
Caw the crow, stepping deliberately, said it was easier to ask the REPL
about the map {:crow 1 :pitcher 2} than to argue.

Write a form whose evaluation gives the map with two entries.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"{:crow 1 :pitcher 2}"}}]}
```

## G4-07: get — map lookup

### G4-07 record 1  •  form `(get {:a 1 :b 2} :a)`  •  expected `1`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened in the farm.

Sable the crow and Korvus the crow alighted near the farm on the rim of an old
pitcher where someone had scratched the form (get {:a 1 :b 2} :a). Sable,
in a panic, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(get {:a 1 :b 2} :a)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Question: write a Clojure expression for the value at :a.

---

I let each form raise the surface a little closer to the answer.

{"tool_calls":[{"name":"eval","args":{"form":"(get {:a 1 :b 2} :a)"}}]}
```

### G4-07 record 2  •  form `(get {:a 1} :missing :default)`  •  expected `':default'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

At a moss-flecked pitcher in the village, Caw the crow sketched a small
wager: whoever guessed the result of `(get {:a 1} :missing :default)` first would drink
first when the water rose. Korvus the crow, with steady, careful steps, said it was
simpler to type the form into the REPL than to argue about
the form (get {:a 1} :missing :default).

Write a Clojure expression that computes the default value when key missing.

---

{"tool_calls":[{"name":"eval","args":{"form":"(get {:a 1} :missing :default)"}}]}
```

### G4-07 record 3  •  form `(get {:a 1 :b 2} :a)`  •  expected `1`

```
Hunger and thirst had driven the Crow far from her usual perch.

Halfway through a long thirsty afternoon, Korvus the crow alighted
by the garden and refused to fly on until someone could prove what the form
`(get {:a 1 :b 2} :a)` evaluated to. Korvus called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
the form (get {:a 1 :b 2} :a) into the REPL. Whatever rises is the answer."

Write a form whose evaluation gives the value at :a.

---

I let each form raise the surface a little closer to the answer.

{"tool_calls":[{"name":"eval","args":{"form":"(get {:a 1 :b 2} :a)"}}]}
```

### G4-07 record 4  •  form `(get {:a 1} :missing :default)`  •  expected `':default'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A small audience of sparrows had gathered at the edge of the hilltop to watch
Sable the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to the form (get {:a 1} :missing :default) and read out the form
aloud: `(get {:a 1} :missing :default)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a Clojure expression that computes the default value when key missing.

---

I use the appropriate access function on the collection.

{"tool_calls":[{"name":"eval","args":{"form":"(get {:a 1} :missing :default)"}}]}
```

### G4-07 record 5  •  form `(get {:a 1 :b 2} :a)`  •  expected `1`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

At a moss-flecked pitcher at the edge of the garden, Sable the crow sketched a small
wager: whoever guessed the result of `(get {:a 1 :b 2} :a)` first would drink
first when the water rose. Caw the crow, her eyes always on the path, said it was
simpler to type the form into the REPL than to argue about
the form (get {:a 1 :b 2} :a).

Write a form whose evaluation gives the value at :a.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(get {:a 1 :b 2} :a)"}}]}
```

## G4-08: assoc — map update

### G4-08 record 1  •  form `(assoc {:a 1} :b 2)`  •  expected `{':a': 1, ':b': 2}`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened in the village.

Korvus the crow etched a wager along the rim of a chipped pitcher
at the edge of the village: whoever predicted the result of `(assoc {:a 1} :b 2)` first would set
the next day's foraging route. Sable the crow, without complaint, said it
would be simpler to drop the form into the REPL than to bicker about
the form (assoc {:a 1} :b 2).

Question: write a Clojure expression for the map after assoc'ing :b 2.

---

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:a 1} :b 2)"}}]}
```

### G4-08 record 2  •  form `(assoc {:a 1} :a 99)`  •  expected `{':a': 99}`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Halfway through a long thirsty afternoon, Sable the crow alighted
at the edge of the hilltop and refused to fly on until someone could prove what the form
`(assoc {:a 1} :a 99)` evaluated to. Sable called it impossible.
Caw the crow, gliding down at an unhurried pace, simply said: "Drop
the form (assoc {:a 1} :a 99) into the REPL. Whatever rises is the answer."

Question: write a Clojure expression for the map after updating :a to 99.

---

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:a 1} :a 99)"}}]}
```

### G4-08 record 3  •  form `(assoc {:a 1} :b 2)`  •  expected `{':a': 1, ':b': 2}`

```
Hunger and thirst had driven the Crow far from her usual perch. It happened at the edge of the farm.

At a moss-flecked pitcher near the farm, Korvus the crow sketched a small
wager: whoever guessed the result of `(assoc {:a 1} :b 2)` first would drink
first when the water rose. Caw the crow, saying very little, said it was
simpler to type the form into the REPL than to argue about
the form (assoc {:a 1} :b 2).

What Clojure form computes the map after assoc'ing :b 2? Submit it via `eval`.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:a 1} :b 2)"}}]}
```

### G4-08 record 4  •  form `(assoc {:a 1} :a 99)`  •  expected `{':a': 99}`

```
Hunger and thirst had driven the Crow far from her usual perch.

Sable the crow, boasting at every turn, declared the collection plain.
Caw the crow chalked `(assoc {:a 1} :a 99)` on a slate near the hilltop, calmly.
"It's not about plain or fancy," she said. "It's about
whether the runtime agrees with what we think we're describing."

Question: write a Clojure expression for the map after updating :a to 99.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:a 1} :a 99)"}}]}
```

### G4-08 record 5  •  form `(assoc {:a 1} :b 2)`  •  expected `{':a': 1, ':b': 2}`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Korvus the crow had been laying out a small collection in the farm —
pebbles, twigs, stray feathers, whatever the day's foraging had
produced. Korvus chalked `(assoc {:a 1} :b 2)` on a flat stone and asked
Caw the crow to write the form into the REPL so they could confirm
it together.

Write a form whose evaluation gives the map after assoc'ing :b 2.

---

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:a 1} :b 2)"}}]}
```

## G4-09: dissoc — map remove key

### G4-09 record 1  •  form `(dissoc {:a 1 :b 2} :a)`  •  expected `{':b': 2}`

```
Hunger and thirst had driven the Crow far from her usual perch.

Halfway through a long thirsty afternoon, Korvus the crow alighted
at the edge of the village and refused to fly on until someone could prove what the form
`(dissoc {:a 1 :b 2} :a)` evaluated to. Korvus called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
the form (dissoc {:a 1 :b 2} :a) into the REPL. Whatever rises is the answer."

Question: write a Clojure expression for the map without :a.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(dissoc {:a 1 :b 2} :a)"}}]}
```

### G4-09 record 2  •  form `(dissoc {:a 1 :b 2} :a)`  •  expected `{':b': 2}`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Korvus the crow had been keeping a small leather notebook of every form
he had successfully dropped into the REPL — one entry per
stone, one rise per form. Today in the meadow, the next entry was
the form (dissoc {:a 1 :b 2} :a). Sable the crow peered over his shoulder
at the form `(dissoc {:a 1 :b 2} :a)` and asked what it would come out to.

Write a Clojure expression that computes the map without :a.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(dissoc {:a 1 :b 2} :a)"}}]}
```

### G4-09 record 3  •  form `(dissoc {:a 1 :b 2} :a)`  •  expected `{':b': 2}`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Caw the crow, puffed up with pride, declared the collection plain.
Korvus the crow chalked `(dissoc {:a 1 :b 2} :a)` on a slate near the road, calmly.
"It's not about plain or fancy," he said. "It's about
whether the runtime agrees with what we think we're describing."

Write a Clojure expression that computes the map without :a.

---

{"tool_calls":[{"name":"eval","args":{"form":"(dissoc {:a 1 :b 2} :a)"}}]}
```

### G4-09 record 4  •  form `(dissoc {:a 1 :b 2} :a)`  •  expected `{':b': 2}`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust in the meadow: whoever guessed the result of `(dissoc {:a 1 :b 2} :a)`
first would win the right to claim the next clear water they found.
Sable the crow, saying very little, said it was easier to ask the REPL
about the form (dissoc {:a 1 :b 2} :a) than to argue.

Write a form whose evaluation gives the map without :a.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(dissoc {:a 1 :b 2} :a)"}}]}
```

### G4-09 record 5  •  form `(dissoc {:a 1 :b 2} :a)`  •  expected `{':b': 2}`

```
Hunger and thirst had driven the Crow far from her usual perch.

Korvus the crow, with a smug grin, declared the collection plain.
Caw the crow chalked `(dissoc {:a 1 :b 2} :a)` on a slate near the village, calmly.
"It's not about plain or fancy," she said. "It's about
whether the runtime agrees with what we think we're describing."

What Clojure form computes the map without :a? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(dissoc {:a 1 :b 2} :a)"}}]}
```

## G4-10: keys and vals

### G4-10 record 1  •  form `(count (keys {:a 1 :b 2 :c 3}))`  •  expected `3`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A small audience of sparrows had gathered by the orchard to watch
Caw the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to the form (count (keys ...)) and read out the form
aloud: `(count (keys {:a 1 :b 2 :c 3}))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Question: write a Clojure expression for the number of keys in the map.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(count (keys {:a 1 :b 2 :c 3}))"}}]}
```

### G4-10 record 2  •  form `(count (keys {:a 1 :b 2 :c 3}))`  •  expected `3`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place near the market.

Korvus the crow, puffed up with pride, declared the collection plain.
Sable the crow chalked `(count (keys {:a 1 :b 2 :c 3}))` on a slate by the market, calmly.
"It's not about plain or fancy," they said. "It's about
whether the runtime agrees with what we think we're describing."

Question: write a Clojure expression for the number of keys in the map.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(count (keys {:a 1 :b 2 :c 3}))"}}]}
```

### G4-10 record 3  •  form `(count (keys {:a 1 :b 2 :c 3}))`  •  expected `3`

```
Hunger and thirst had driven the Crow far from her usual perch.

Sable the crow etched a wager along the rim of a chipped pitcher
by the orchard: whoever predicted the result of `(count (keys {:a 1 :b 2 :c 3}))` first would set
the next day's foraging route. Caw the crow, untroubled by what others thought, said it
would be simpler to drop the form into the REPL than to bicker about
the form (count (keys ...)).

Question: write a Clojure expression for the number of keys in the map.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count (keys {:a 1 :b 2 :c 3}))"}}]}
```

### G4-10 record 4  •  form `(count (keys {:a 1 :b 2 :c 3}))`  •  expected `3`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust on the road: whoever guessed the result of `(count (keys {:a 1 :b 2 :c 3}))`
first would win the right to claim the next clear water they found.
Sable the crow, without complaint, said it was easier to ask the REPL
about the form (count (keys ...)) than to argue.

Write a Clojure expression that computes the number of keys in the map.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count (keys {:a 1 :b 2 :c 3}))"}}]}
```

### G4-10 record 5  •  form `(count (keys {:a 1 :b 2 :c 3}))`  •  expected `3`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place near the road.

Caw the crow and Korvus the crow alighted on the road on the rim of an old
pitcher where someone had scratched the form (count (keys ...)). Caw,
in a panic, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(count (keys {:a 1 :b 2 :c 3}))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a form whose evaluation gives the number of keys in the map.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count (keys {:a 1 :b 2 :c 3}))"}}]}
```

## G4-11: Set literal

### G4-11 record 1  •  form `(count #{1 2 3})`  •  expected `3`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Sable the crow etched a wager along the rim of a chipped pitcher
at the edge of the village: whoever predicted the result of `(count #{1 2 3})` first would set
the next day's foraging route. Korvus the crow, her eyes always on the path, said it
would be simpler to drop the form into the REPL than to bicker about
the count of #{1 2 3}.

Write a Clojure expression that computes the size of the set.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count #{1 2 3})"}}]}
```

### G4-11 record 2  •  form `(count #{1 1 1})`  •  expected `1`

```
Hunger and thirst had driven the Crow far from her usual perch. This was atop the hilltop.

"There is no need to evaluate that," Caw the crow said, with a smug grin.
"Anyone with a sharp eye can see what the count of #{1 1 1} (dedup'd) comes to."
Sable the crow, who atop the hilltop had grown used to such claims, asked
her to actually write the form `(count #{1 1 1})` and drop it
into the REPL — just to be sure.

Question: write a Clojure expression for the size of the set.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count #{1 1 1})"}}]}
```

### G4-11 record 3  •  form `(count #{1 2 3})`  •  expected `3`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place near the road.

Halfway through a long thirsty afternoon, Korvus the crow alighted
on the road and refused to fly on until someone could prove what the form
`(count #{1 2 3})` evaluated to. Korvus called it impossible.
Caw the crow, gliding down at an unhurried pace, simply said: "Drop
the count of #{1 2 3} into the REPL. Whatever rises is the answer."

Write a Clojure expression that computes the size of the set.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(count #{1 2 3})"}}]}
```

### G4-11 record 4  •  form `(count #{1 1 1})`  •  expected `1`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Korvus the crow and Sable the crow alighted by the village on the rim of an old
pitcher where someone had scratched the count of #{1 1 1} (dedup'd). Korvus,
her hands trembling, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(count #{1 1 1})` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a form whose evaluation gives the size of the set.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count #{1 1 1})"}}]}
```

### G4-11 record 5  •  form `(count #{1 2 3})`  •  expected `3`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

At a moss-flecked pitcher by the orchard, Caw the crow sketched a small
wager: whoever guessed the result of `(count #{1 2 3})` first would drink
first when the water rose. Sable the crow, with steady, careful steps, said it was
simpler to type the form into the REPL than to argue about
the count of #{1 2 3}.

What Clojure form computes the size of the set? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count #{1 2 3})"}}]}
```

## G4-12: Set membership

### G4-12 record 1  •  form `(contains? #{1 2 3} 2)`  •  expected `True`

```
Hunger and thirst had driven the Crow far from her usual perch.

Caw the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," she said, pointing to the form (contains? #{1 2 3} 2).
"You hand the form `(contains? #{1 2 3} 2)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, near to giving up the search for water, agreed to try.

What Clojure form computes whether 2 is in the set? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{1 2 3} 2)"}}]}
```

### G4-12 record 2  •  form `(contains? #{1 2 3} 4)`  •  expected `False`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened at the edge of the market.

"There is no need to evaluate that," Caw the crow said, puffed up with pride.
"Anyone with a sharp eye can see what the form (contains? #{1 2 3} 4) comes to."
Sable the crow, who at the edge of the market had grown used to such claims, asked
her to actually write the form `(contains? #{1 2 3} 4)` and drop it
into the REPL — just to be sure.

Write a form whose evaluation gives whether 4 is in the set.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{1 2 3} 4)"}}]}
```

### G4-12 record 3  •  form `(contains? #{1 2 3} 2)`  •  expected `True`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Korvus the crow had been laying out a small collection at the edge of the farm —
pebbles, twigs, stray feathers, whatever the day's foraging had
produced. Korvus chalked `(contains? #{1 2 3} 2)` on a flat stone and asked
Caw the crow to write the form into the REPL so they could confirm
it together.

Write a form whose evaluation gives whether 2 is in the set.

---

{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{1 2 3} 2)"}}]}
```

### G4-12 record 4  •  form `(contains? #{1 2 3} 4)`  •  expected `False`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Caw the crow, swaggering through the underbrush, declared the collection plain.
Korvus the crow chalked `(contains? #{1 2 3} 4)` on a slate in the meadow, calmly.
"It's not about plain or fancy," he said. "It's about
whether the runtime agrees with what we think we're describing."

What Clojure form computes whether 4 is in the set? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{1 2 3} 4)"}}]}
```

### G4-12 record 5  •  form `(contains? #{1 2 3} 2)`  •  expected `True`

```
Hunger and thirst had driven the Crow far from her usual perch.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust in the meadow: whoever guessed the result of `(contains? #{1 2 3} 2)`
first would win the right to claim the next clear water they found.
Caw the crow, saying very little, said it was easier to ask the REPL
about the form (contains? #{1 2 3} 2) than to argue.

Write a Clojure expression that computes whether 2 is in the set.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{1 2 3} 2)"}}]}
```

## G4-13: count — universal

### G4-13 record 1  •  form `(count [1 2 3 4 5])`  •  expected `5`

```
Hunger and thirst had driven the Crow far from her usual perch.

"There is no need to evaluate that," Caw the crow said, swaggering through the underbrush.
"Anyone with a sharp eye can see what the count of a 5-element vector comes to."
Sable the crow, who at the edge of the market had grown used to such claims, asked
her to actually write the form `(count [1 2 3 4 5])` and drop it
into the REPL — just to be sure.

Question: write a Clojure expression for the count.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count [1 2 3 4 5])"}}]}
```

### G4-13 record 2  •  form `(count {:a 1 :b 2})`  •  expected `2`

```
Hunger and thirst had driven the Crow far from her usual perch. This was by the farm.

At a moss-flecked pitcher by the farm, Korvus the crow sketched a small
wager: whoever guessed the result of `(count {:a 1 :b 2})` first would drink
first when the water rose. Sable the crow, untroubled by what others thought, said it was
simpler to type the form into the REPL than to argue about
the count of a 2-key map.

Write a form whose evaluation gives the count.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(count {:a 1 :b 2})"}}]}
```

### G4-13 record 3  •  form `(count #{:a :b :c})`  •  expected `3`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. This was along the road.

Korvus the crow had been laying out a small collection on the road —
pebbles, twigs, stray feathers, whatever the day's foraging had
produced. Korvus chalked `(count #{:a :b :c})` on a flat stone and asked
Caw the crow to write the form into the REPL so they could confirm
it together.

Question: write a Clojure expression for the count.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(count #{:a :b :c})"}}]}
```

### G4-13 record 4  •  form `(count "tortoise")`  •  expected `8`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Korvus the crow had been laying out a small collection at the edge of the village —
pebbles, twigs, stray feathers, whatever the day's foraging had
produced. Korvus chalked `(count "tortoise")` on a flat stone and asked
Sable the crow to write the form into the REPL so they could confirm
it together.

What Clojure form computes the string length? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count \"tortoise\")"}}]}
```

### G4-13 record 5  •  form `(count [1 2 3 4 5])`  •  expected `5`

```
Hunger and thirst had driven the Crow far from her usual perch. This was at the edge of the village.

Caw the crow and Korvus the crow alighted near the village on the rim of an old
pitcher where someone had scratched the count of a 5-element vector. Caw,
her hands trembling, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(count [1 2 3 4 5])` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a Clojure expression that computes the count.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(count [1 2 3 4 5])"}}]}
```

## G4-14: empty?

### G4-14 record 1  •  form `(empty? [])`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

At a moss-flecked pitcher in the farm, Caw the crow sketched a small
wager: whoever guessed the result of `(empty? [])` first would drink
first when the water rose. Sable the crow, with steady, careful steps, said it was
simpler to type the form into the REPL than to argue about
the form (empty? []).

What Clojure form computes whether [] is empty? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(empty? [])"}}]}
```

### G4-14 record 2  •  form `(empty? [1])`  •  expected `False`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust in the garden: whoever guessed the result of `(empty? [1])`
first would win the right to claim the next clear water they found.
Korvus the crow, without complaint, said it was easier to ask the REPL
about the form (empty? [1]) than to argue.

Write a form whose evaluation gives whether [1] is empty.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(empty? [1])"}}]}
```

### G4-14 record 3  •  form `(empty? "")`  •  expected `True`

```
Hunger and thirst had driven the Crow far from her usual perch. This was at the edge of the meadow.

Caw the crow had been laying out a small collection at the edge of the meadow —
pebbles, twigs, stray feathers, whatever the day's foraging had
produced. Caw chalked `(empty? "")` on a flat stone and asked
Sable the crow to write the form into the REPL so they could confirm
it together.

What Clojure form computes whether the empty string is empty? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(empty? \"\")"}}]}
```

### G4-14 record 4  •  form `(empty? [])`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Caw the crow etched a wager along the rim of a chipped pitcher
near the garden: whoever predicted the result of `(empty? [])` first would set
the next day's foraging route. Sable the crow, untroubled by what others thought, said it
would be simpler to drop the form into the REPL than to bicker about
the form (empty? []).

Write a form whose evaluation gives whether [] is empty.

---

I write the collection literal and let the REPL evaluate.

{"tool_calls":[{"name":"eval","args":{"form":"(empty? [])"}}]}
```

### G4-14 record 5  •  form `(empty? [1])`  •  expected `False`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was along the road.

A wooden sign nailed to a tree along the road carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(empty? [1])`. Korvus laughed, swaggering through the underbrush, and declared it
too easy. Caw said patiently that the only way to be sure of
the form (empty? [1]) was to drop it into the REPL.

What Clojure form computes whether [1] is empty? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(empty? [1])"}}]}
```

## G4-15: first, rest, last

### G4-15 record 1  •  form `(first [10 20 30])`  •  expected `10`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was near the road.

Caw the crow etched a wager along the rim of a chipped pitcher
near the road: whoever predicted the result of `(first [10 20 30])` first would set
the next day's foraging route. Sable the crow, untroubled by what others thought, said it
would be simpler to drop the form into the REPL than to bicker about
the first of the vector.

Question: write a Clojure expression for the first element.

---

{"tool_calls":[{"name":"eval","args":{"form":"(first [10 20 30])"}}]}
```

### G4-15 record 2  •  form `(last  [10 20 30])`  •  expected `30`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust at the edge of the market: whoever guessed the result of `(last  [10 20 30])`
first would win the right to claim the next clear water they found.
Korvus the crow, her eyes always on the path, said it was easier to ask the REPL
about the last of the vector than to argue.

What Clojure form computes the last element? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(last  [10 20 30])"}}]}
```

### G4-15 record 3  •  form `(count (rest [10 20 30]))`  •  expected `2`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place by the orchard.

"There is no need to evaluate that," Korvus the crow said, swaggering through the underbrush.
"Anyone with a sharp eye can see what the rest of [10 20 30] (count) comes to."
Sable the crow, who in the orchard had grown used to such claims, asked
him to actually write the form `(count (rest [10 20 30]))` and drop it
into the REPL — just to be sure.

Write a Clojure expression that computes the count after removing first.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(count (rest [10 20 30]))"}}]}
```

### G4-15 record 4  •  form `(first [10 20 30])`  •  expected `10`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place on the hilltop.

"There is no need to evaluate that," Sable the crow said, puffed up with pride.
"Anyone with a sharp eye can see what the first of the vector comes to."
Korvus the crow, who on the hilltop had grown used to such claims, asked
them to actually write the form `(first [10 20 30])` and drop it
into the REPL — just to be sure.

What Clojure form computes the first element? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(first [10 20 30])"}}]}
```

### G4-15 record 5  •  form `(last  [10 20 30])`  •  expected `30`

```
Hunger and thirst had driven the Crow far from her usual perch.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust by the market: whoever guessed the result of `(last  [10 20 30])`
first would win the right to claim the next clear water they found.
Caw the crow, stepping deliberately, said it was easier to ask the REPL
about the last of the vector than to argue.

Write a form whose evaluation gives the last element.

---

I write the collection literal and let the REPL evaluate.

{"tool_calls":[{"name":"eval","args":{"form":"(last  [10 20 30])"}}]}
```

## G4-16: into and conj on collections

### G4-16 record 1  •  form `(into [] '(1 2 3))`  •  expected `[1, 2, 3]`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

At a moss-flecked pitcher in the meadow, Caw the crow sketched a small
wager: whoever guessed the result of `(into [] '(1 2 3))` first would drink
first when the water rose. Korvus the crow, saying very little, said it was
simpler to type the form into the REPL than to argue about
the form (into [] '(1 2 3)).

Write a Clojure expression that computes the vector built from a list.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] '(1 2 3))"}}]}
```

### G4-16 record 2  •  form `(into #{} [1 2 2 3])`  •  expected `[1, 2, 3]`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. This was near the meadow.

Halfway through a long thirsty afternoon, Korvus the crow alighted
by the meadow and refused to fly on until someone could prove what the form
`(into #{} [1 2 2 3])` evaluated to. Korvus called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
the form (into #{} [1 2 2 3]) into the REPL. Whatever rises is the answer."

Write a form whose evaluation gives the set built from a vector (dups removed).

---

{"tool_calls":[{"name":"eval","args":{"form":"(into #{} [1 2 2 3])"}}]}
```

### G4-16 record 3  •  form `(into [] '(1 2 3))`  •  expected `[1, 2, 3]`

```
Hunger and thirst had driven the Crow far from her usual perch.

Halfway through a long thirsty afternoon, Caw the crow alighted
near the village and refused to fly on until someone could prove what the form
`(into [] '(1 2 3))` evaluated to. Caw called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
the form (into [] '(1 2 3)) into the REPL. Whatever rises is the answer."

Question: write a Clojure expression for the vector built from a list.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] '(1 2 3))"}}]}
```

### G4-16 record 4  •  form `(into #{} [1 2 2 3])`  •  expected `[1, 2, 3]`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. All this took place near the village.

At a moss-flecked pitcher in the village, Sable the crow sketched a small
wager: whoever guessed the result of `(into #{} [1 2 2 3])` first would drink
first when the water rose. Korvus the crow, untroubled by what others thought, said it was
simpler to type the form into the REPL than to argue about
the form (into #{} [1 2 2 3]).

Write a Clojure expression that computes the set built from a vector (dups removed).

---

{"tool_calls":[{"name":"eval","args":{"form":"(into #{} [1 2 2 3])"}}]}
```

### G4-16 record 5  •  form `(into [] '(1 2 3))`  •  expected `[1, 2, 3]`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Caw the crow had been trying to teach Sable the crow how the REPL
works. "Look here," she said, pointing to the form (into [] '(1 2 3)).
"You hand the form `(into [] '(1 2 3))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, with a thirst that hurt to bear, agreed to try.

What Clojure form computes the vector built from a list? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] '(1 2 3))"}}]}
```

## G4-17: Immutability — assoc returns new

### G4-17 record 1  •  form `(let [m {:a 1}] (assoc m :a 99) m)`  •  expected `{':a': 1}`

```
Hunger and thirst had driven the Crow far from her usual perch. It happened near the orchard.

Halfway through a long thirsty afternoon, Sable the crow alighted
at the edge of the orchard and refused to fly on until someone could prove what the form
`(let [m {:a 1}] (assoc m :a 99) m)` evaluated to. Sable called it impossible.
Korvus the crow, gliding down at an unhurried pace, simply said: "Drop
the form showing assoc returns a new map into the REPL. Whatever rises is the answer."

What Clojure form computes the original map after assoc? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :a 99) m)"}}]}
```

### G4-17 record 2  •  form `(let [m {:a 1}] (assoc m :a 99) m)`  •  expected `{':a': 1}`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened near the farm.

Sable the crow had been trying to teach Caw the crow how the REPL
works. "Look here," they said, pointing to the form showing assoc returns a new map.
"You hand the form `(let [m {:a 1}] (assoc m :a 99) m)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Caw, near to giving up the search for water, agreed to try.

Write a Clojure expression that computes the original map after assoc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :a 99) m)"}}]}
```

### G4-17 record 3  •  form `(let [m {:a 1}] (assoc m :a 99) m)`  •  expected `{':a': 1}`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A small audience of sparrows had gathered near the road to watch
Caw the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to the form showing assoc returns a new map and read out the form
aloud: `(let [m {:a 1}] (assoc m :a 99) m)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

What Clojure form computes the original map after assoc? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :a 99) m)"}}]}
```

### G4-17 record 4  •  form `(let [m {:a 1}] (assoc m :a 99) m)`  •  expected `{':a': 1}`

```
Hunger and thirst had driven the Crow far from her usual perch. This was near the hilltop.

A small audience of sparrows had gathered near the hilltop to watch
Sable the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to the form showing assoc returns a new map and read out the form
aloud: `(let [m {:a 1}] (assoc m :a 99) m)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives the original map after assoc.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :a 99) m)"}}]}
```

### G4-17 record 5  •  form `(let [m {:a 1}] (assoc m :a 99) m)`  •  expected `{':a': 1}`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

"There is no need to evaluate that," Korvus the crow said, with a smug grin.
"Anyone with a sharp eye can see what the form showing assoc returns a new map comes to."
Caw the crow, who by the orchard had grown used to such claims, asked
him to actually write the form `(let [m {:a 1}] (assoc m :a 99) m)` and drop it
into the REPL — just to be sure.

Write a Clojure expression that computes the original map after assoc.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :a 99) m)"}}]}
```

## G4-18: Equality of vectors and lists

### G4-18 record 1  •  form `(= [1 2 3] '(1 2 3))`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened near the village.

Caw the crow etched a wager along the rim of a chipped pitcher
at the edge of the village: whoever predicted the result of `(= [1 2 3] '(1 2 3))` first would set
the next day's foraging route. Korvus the crow, without complaint, said it
would be simpler to drop the form into the REPL than to bicker about
the form (= [1 2 3] '(1 2 3)).

Write a form whose evaluation gives whether vector and list with same elements are equal.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(= [1 2 3] '(1 2 3))"}}]}
```

### G4-18 record 2  •  form `(= [1 2 3] '(1 2 3))`  •  expected `True`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

"There is no need to evaluate that," Korvus the crow said, swaggering through the underbrush.
"Anyone with a sharp eye can see what the form (= [1 2 3] '(1 2 3)) comes to."
Caw the crow, who on the hilltop had grown used to such claims, asked
him to actually write the form `(= [1 2 3] '(1 2 3))` and drop it
into the REPL — just to be sure.

What Clojure form computes whether vector and list with same elements are equal? Submit it via `eval`.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(= [1 2 3] '(1 2 3))"}}]}
```

### G4-18 record 3  •  form `(= [1 2 3] '(1 2 3))`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was by the farm.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust at the edge of the farm: whoever guessed the result of `(= [1 2 3] '(1 2 3))`
first would win the right to claim the next clear water they found.
Caw the crow, with steady, careful steps, said it was easier to ask the REPL
about the form (= [1 2 3] '(1 2 3)) than to argue.

Question: write a Clojure expression for whether vector and list with same elements are equal.

---

{"tool_calls":[{"name":"eval","args":{"form":"(= [1 2 3] '(1 2 3))"}}]}
```

### G4-18 record 4  •  form `(= [1 2 3] '(1 2 3))`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was by the market.

Halfway through a long thirsty afternoon, Sable the crow alighted
by the market and refused to fly on until someone could prove what the form
`(= [1 2 3] '(1 2 3))` evaluated to. Sable called it impossible.
Caw the crow, gliding down at an unhurried pace, simply said: "Drop
the form (= [1 2 3] '(1 2 3)) into the REPL. Whatever rises is the answer."

Write a Clojure expression that computes whether vector and list with same elements are equal.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(= [1 2 3] '(1 2 3))"}}]}
```

### G4-18 record 5  •  form `(= [1 2 3] '(1 2 3))`  •  expected `True`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place atop the hilltop.

"There is no need to evaluate that," Sable the crow said, with a smug grin.
"Anyone with a sharp eye can see what the form (= [1 2 3] '(1 2 3)) comes to."
Caw the crow, who at the edge of the hilltop had grown used to such claims, asked
them to actually write the form `(= [1 2 3] '(1 2 3))` and drop it
into the REPL — just to be sure.

Question: write a Clojure expression for whether vector and list with same elements are equal.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(= [1 2 3] '(1 2 3))"}}]}
```

## G4-19: range and seq

### G4-19 record 1  •  form `(count (range 5))`  •  expected `5`

```
Hunger and thirst had driven the Crow far from her usual perch.

A small audience of sparrows had gathered at the edge of the farm to watch
Caw the crow attempt to outwit Sable the crow at the rim of an old
pitcher. Sable pointed to the count of (range 5) and read out the form
aloud: `(count (range 5))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives the count of range 0..4.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count (range 5))"}}]}
```

### G4-19 record 2  •  form `(first (range 1 100))`  •  expected `1`

```
Hunger and thirst had driven the Crow far from her usual perch.

Korvus the crow etched a wager along the rim of a chipped pitcher
near the market: whoever predicted the result of `(first (range 1 100))` first would set
the next day's foraging route. Caw the crow, untroubled by what others thought, said it
would be simpler to drop the form into the REPL than to bicker about
the first of (range 1 100).

Write a Clojure expression that computes the first of range 1..99.

---

{"tool_calls":[{"name":"eval","args":{"form":"(first (range 1 100))"}}]}
```

### G4-19 record 3  •  form `(count (range 5))`  •  expected `5`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was at the edge of the market.

"There is no need to evaluate that," Sable the crow said, puffed up with pride.
"Anyone with a sharp eye can see what the count of (range 5) comes to."
Korvus the crow, who near the market had grown used to such claims, asked
them to actually write the form `(count (range 5))` and drop it
into the REPL — just to be sure.

What Clojure form computes the count of range 0..4? Submit it via `eval`.

---

I write the collection literal and let the REPL evaluate.

{"tool_calls":[{"name":"eval","args":{"form":"(count (range 5))"}}]}
```

### G4-19 record 4  •  form `(first (range 1 100))`  •  expected `1`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Caw the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," she said, pointing to the first of (range 1 100).
"You hand the form `(first (range 1 100))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, with a thirst that hurt to bear, agreed to try.

Write a form whose evaluation gives the first of range 1..99.

---

{"tool_calls":[{"name":"eval","args":{"form":"(first (range 1 100))"}}]}
```

### G4-19 record 5  •  form `(count (range 5))`  •  expected `5`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Caw the crow and Sable the crow alighted by the meadow on the rim of an old
pitcher where someone had scratched the count of (range 5). Caw,
shouting until her voice cracked, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(count (range 5))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Question: write a Clojure expression for the count of range 0..4.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count (range 5))"}}]}
```

## G4-20: Collection vs sequence

### G4-20 record 1  •  form `(count (seq [1 2 3]))`  •  expected `3`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place on the hilltop.

"There is no need to evaluate that," Sable the crow said, with a smug grin.
"Anyone with a sharp eye can see what the form (count (seq [1 2 3])) comes to."
Caw the crow, who at the edge of the hilltop had grown used to such claims, asked
them to actually write the form `(count (seq [1 2 3]))` and drop it
into the REPL — just to be sure.

Write a form whose evaluation gives the count of seq over a vector.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count (seq [1 2 3]))"}}]}
```

### G4-20 record 2  •  form `(seq [])`  •  expected `None`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place at the edge of the market.

Caw the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," she said, pointing to the form (seq []).
"You hand the form `(seq [])` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, her beak cracked with thirst, agreed to try.

What Clojure form computes what (seq []) returns? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(seq [])"}}]}
```

### G4-20 record 3  •  form `(count (seq [1 2 3]))`  •  expected `3`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Korvus the crow, puffed up with pride, declared the collection plain.
Caw the crow chalked `(count (seq [1 2 3]))` on a slate in the village, calmly.
"It's not about plain or fancy," she said. "It's about
whether the runtime agrees with what we think we're describing."

Question: write a Clojure expression for the count of seq over a vector.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(count (seq [1 2 3]))"}}]}
```

### G4-20 record 4  •  form `(seq [])`  •  expected `None`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Sable the crow had been laying out a small collection near the village —
pebbles, twigs, stray feathers, whatever the day's foraging had
produced. Sable chalked `(seq [])` on a flat stone and asked
Caw the crow to write the form into the REPL so they could confirm
it together.

Question: write a Clojure expression for what (seq []) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(seq [])"}}]}
```

### G4-20 record 5  •  form `(count (seq [1 2 3]))`  •  expected `3`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Korvus the crow and Sable the crow alighted in the market on the rim of an old
pitcher where someone had scratched the form (count (seq [1 2 3])). Korvus,
shouting until her voice cracked, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(count (seq [1 2 3]))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a Clojure expression that computes the count of seq over a vector.

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(count (seq [1 2 3]))"}}]}
```

