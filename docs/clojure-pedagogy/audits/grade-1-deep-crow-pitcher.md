# crow-pitcher grade 1 — deep spot-check

5 records per subject for hand-audit.

---

## G1-01: Eval as substitution

### G1-01 record 1  •  form `42`  •  expected `42`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was near the road.

Sable the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," they said, pointing to the value 42.
"You hand the form `42` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, parched from the long flight, agreed to try.

What Clojure form computes the value of 42? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
```

### G1-01 record 2  •  form `0`  •  expected `0`

```
Hunger and thirst had driven the Crow far from her usual perch. This was on the road.

Korvus the crow and Sable the crow alighted along the road on the rim of an old
pitcher where someone had scratched the value 0. Korvus,
shouting until her voice cracked, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `0` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a Clojure expression that computes the value of 0.

---

{"tool_calls":[{"name":"eval","args":{"form":"0"}}]}
```

### G1-01 record 3  •  form `(+ 1 2)`  •  expected `3`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Caw the crow had been trying to teach Sable the crow how the REPL
works. "Look here," she said, pointing to the form (+ 1 2).
"You hand the form `(+ 1 2)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, parched from the long flight, agreed to try.

What Clojure form computes the result of (+ 1 2)? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G1-01 record 4  •  form `(* 4 5)`  •  expected `20`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was in the garden.

Sable the crow had been trying to teach Caw the crow how the REPL
works. "Look here," they said, pointing to the form (* 4 5).
"You hand the form `(* 4 5)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Caw, her beak cracked with thirst, agreed to try.

Question: write a Clojure expression for the result of (* 4 5).

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(* 4 5)"}}]}
```

### G1-01 record 5  •  form `(- 10 (+ 2 3))`  •  expected `5`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

A wooden sign nailed to a tree on the hilltop carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(- 10 (+ 2 3))`. Caw laughed, boasting at every turn, and declared it
too easy. Sable said patiently that the only way to be sure of
the nested form (- 10 (+ 2 3)) was to drop it into the REPL.

Question: write a Clojure expression for the result of (- 10 (+ 2 3)).

---

{"tool_calls":[{"name":"eval","args":{"form":"(- 10 (+ 2 3))"}}]}
```

## G1-02: Integer numbers

### G1-02 record 1  •  form `7`  •  expected `7`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was along the road.

Sable the crow etched a wager along the rim of a chipped pitcher
along the road: whoever predicted the result of `7` first would set
the next day's foraging route. Caw the crow, saying very little, said it
would be simpler to drop the form into the REPL than to bicker about
the integer 7.

Write a Clojure expression that computes the value of the integer 7.

---

{"tool_calls":[{"name":"eval","args":{"form":"7"}}]}
```

### G1-02 record 2  •  form `-3`  •  expected `-3`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place near the farm.

A wooden sign nailed to a tree near the farm carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `-3`. Sable laughed, swaggering through the underbrush, and declared it
too easy. Korvus said patiently that the only way to be sure of
the integer -3 was to drop it into the REPL.

What Clojure form computes the value of the integer -3? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"-3"}}]}
```

### G1-02 record 3  •  form `0`  •  expected `0`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Sable the crow etched a wager along the rim of a chipped pitcher
in the orchard: whoever predicted the result of `0` first would set
the next day's foraging route. Korvus the crow, stepping deliberately, said it
would be simpler to drop the form into the REPL than to bicker about
the integer 0.

What Clojure form computes the value of zero? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"0"}}]}
```

### G1-02 record 4  •  form `100`  •  expected `100`

```
Hunger and thirst had driven the Crow far from her usual perch.

At a moss-flecked pitcher at the edge of the market, Caw the crow sketched a small
wager: whoever guessed the result of `100` first would drink
first when the water rose. Korvus the crow, without complaint, said it was
simpler to type the form into the REPL than to argue about
the integer 100.

Write a form whose evaluation gives the value of one hundred.

---

{"tool_calls":[{"name":"eval","args":{"form":"100"}}]}
```

### G1-02 record 5  •  form `-25`  •  expected `-25`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place at the edge of the meadow.

Halfway through a long thirsty afternoon, Caw the crow alighted
in the meadow and refused to fly on until someone could prove what the form
`-25` evaluated to. Caw called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
the integer -25 into the REPL. Whatever rises is the answer."

Write a Clojure expression that computes the value of negative twenty-five.

---

{"tool_calls":[{"name":"eval","args":{"form":"-25"}}]}
```

## G1-03: Ratios

### G1-03 record 1  •  form `1/2`  •  expected `'1/2'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Halfway through a long thirsty afternoon, Caw the crow alighted
atop the hilltop and refused to fly on until someone could prove what the form
`1/2` evaluated to. Caw called it impossible.
Korvus the crow, gliding down at an unhurried pace, simply said: "Drop
the ratio 1/2 into the REPL. Whatever rises is the answer."

Write a form whose evaluation gives the value of the ratio 1/2.

---

{"tool_calls":[{"name":"eval","args":{"form":"1/2"}}]}
```

### G1-03 record 2  •  form `3/4`  •  expected `'3/4'`

```
Hunger and thirst had driven the Crow far from her usual perch.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust at the edge of the meadow: whoever guessed the result of `3/4`
first would win the right to claim the next clear water they found.
Caw the crow, saying very little, said it was easier to ask the REPL
about the ratio 3/4 than to argue.

Question: write a Clojure expression for the value of three-quarters.

---

{"tool_calls":[{"name":"eval","args":{"form":"3/4"}}]}
```

### G1-03 record 3  •  form `(+ 1/2 1/4)`  •  expected `'3/4'`

```
Hunger and thirst had driven the Crow far from her usual perch. It happened near the hilltop.

"There is no need to evaluate that," Caw the crow said, with great whoops of laughter.
"Anyone with a sharp eye can see what the form (+ 1/2 1/4) comes to."
Sable the crow, who atop the hilltop had grown used to such claims, asked
her to actually write the form `(+ 1/2 1/4)` and drop it
into the REPL — just to be sure.

Write a form whose evaluation gives the value of (+ 1/2 1/4).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1/2 1/4)"}}]}
```

### G1-03 record 4  •  form `(* 2 1/2)`  •  expected `1`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place at the edge of the farm.

A wooden sign nailed to a tree near the farm carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(* 2 1/2)`. Korvus laughed, with a smug grin, and declared it
too easy. Sable said patiently that the only way to be sure of
the form (* 2 1/2) was to drop it into the REPL.

Write a form whose evaluation gives the value of (* 2 1/2).

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(* 2 1/2)"}}]}
```

### G1-03 record 5  •  form `(- 1 1/3)`  •  expected `'2/3'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Sable the crow etched a wager along the rim of a chipped pitcher
near the village: whoever predicted the result of `(- 1 1/3)` first would set
the next day's foraging route. Korvus the crow, stepping deliberately, said it
would be simpler to drop the form into the REPL than to bicker about
the form (- 1 1/3).

What Clojure form computes the value of (- 1 1/3)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(- 1 1/3)"}}]}
```

## G1-04: Strings

### G1-04 record 1  •  form `"hello"`  •  expected `'hello'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

A small audience of sparrows had gathered by the farm to watch
Sable the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to the string "hello" and read out the form
aloud: `"hello"`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives the value of "hello".

---

{"tool_calls":[{"name":"eval","args":{"form":"\"hello\""}}]}
```

### G1-04 record 2  •  form `"thirst"`  •  expected `'thirst'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened near the meadow.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust at the edge of the meadow: whoever guessed the result of `"thirst"`
first would win the right to claim the next clear water they found.
Sable the crow, stepping deliberately, said it was easier to ask the REPL
about the string "thirst" than to argue.

What Clojure form computes the value of "thirst"? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"\"thirst\""}}]}
```

### G1-04 record 3  •  form `"clever and patient"`  •  expected `'clever and patient'`

```
Hunger and thirst had driven the Crow far from her usual perch.

Sable the crow had been trying to teach Caw the crow how the REPL
works. "Look here," they said, pointing to the string "clever and patient".
"You hand the form `"clever and patient"` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Caw, parched from the long flight, agreed to try.

Write a Clojure expression that computes the value of "clever and patient".

---

{"tool_calls":[{"name":"eval","args":{"form":"\"clever and patient\""}}]}
```

### G1-04 record 4  •  form `""`  •  expected `''`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Korvus the crow etched a wager along the rim of a chipped pitcher
in the farm: whoever predicted the result of `""` first would set
the next day's foraging route. Sable the crow, her eyes always on the path, said it
would be simpler to drop the form into the REPL than to bicker about
the empty string.

What Clojure form computes the value of the empty string? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"\"\""}}]}
```

### G1-04 record 5  •  form `"42"`  •  expected `'42'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place in the farm.

Halfway through a long thirsty afternoon, Caw the crow alighted
in the farm and refused to fly on until someone could prove what the form
`"42"` evaluated to. Caw called it impossible.
Korvus the crow, gliding down at an unhurried pace, simply said: "Drop
the string "42" into the REPL. Whatever rises is the answer."

Question: write a Clojure expression for the value of the string "42".

---

{"tool_calls":[{"name":"eval","args":{"form":"\"42\""}}]}
```

## G1-05: Booleans

### G1-05 record 1  •  form `true`  •  expected `True`

```
Hunger and thirst had driven the Crow far from her usual perch.

Korvus the crow etched a wager along the rim of a chipped pitcher
in the village: whoever predicted the result of `true` first would set
the next day's foraging route. Caw the crow, her eyes always on the path, said it
would be simpler to drop the form into the REPL than to bicker about
the literal true.

Write a form whose evaluation gives the value of true.

---

{"tool_calls":[{"name":"eval","args":{"form":"true"}}]}
```

### G1-05 record 2  •  form `false`  •  expected `False`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Sable the crow and Korvus the crow alighted in the village on the rim of an old
pitcher where someone had scratched the literal false. Sable,
with growing alarm, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `false` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a form whose evaluation gives the value of false.

---

{"tool_calls":[{"name":"eval","args":{"form":"false"}}]}
```

### G1-05 record 3  •  form `(= 1 1)`  •  expected `True`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place at the edge of the farm.

"There is no need to evaluate that," Korvus the crow said, with a smug grin.
"Anyone with a sharp eye can see what the equality (= 1 1) comes to."
Caw the crow, who by the farm had grown used to such claims, asked
him to actually write the form `(= 1 1)` and drop it
into the REPL — just to be sure.

Write a Clojure expression that computes the value of (= 1 1).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 1)"}}]}
```

### G1-05 record 4  •  form `(= 1 2)`  •  expected `False`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened at the edge of the garden.

Sable the crow and Caw the crow alighted at the edge of the garden on the rim of an old
pitcher where someone had scratched the equality (= 1 2). Sable,
in a panic, declared the answer beyond reach. Caw, patient as
ever, suggested they drop the form `(= 1 2)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Question: write a Clojure expression for the value of (= 1 2).

---

I let each form raise the surface a little closer to the answer.

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 2)"}}]}
```

### G1-05 record 5  •  form `(< 3 5)`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was in the market.

Korvus the crow and Caw the crow alighted near the market on the rim of an old
pitcher where someone had scratched the comparison (< 3 5). Korvus,
her hands trembling, declared the answer beyond reach. Caw, patient as
ever, suggested they drop the form `(< 3 5)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Question: write a Clojure expression for the value of (< 3 5).

---

{"tool_calls":[{"name":"eval","args":{"form":"(< 3 5)"}}]}
```

## G1-06: nil

### G1-06 record 1  •  form `nil`  •  expected `None`

```
Hunger and thirst had driven the Crow far from her usual perch. This was near the market.

Korvus the crow and Caw the crow alighted in the market on the rim of an old
pitcher where someone had scratched the literal nil. Korvus,
shouting until her voice cracked, declared the answer beyond reach. Caw, patient as
ever, suggested they drop the form `nil` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Question: write a Clojure expression for the value of nil.

---

{"tool_calls":[{"name":"eval","args":{"form":"nil"}}]}
```

### G1-06 record 2  •  form `(nil? nil)`  •  expected `True`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Caw the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," she said, pointing to the predicate (nil? nil).
"You hand the form `(nil? nil)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, dry-throated and desperate, agreed to try.

Question: write a Clojure expression for whether nil is nil.

---

{"tool_calls":[{"name":"eval","args":{"form":"(nil? nil)"}}]}
```

### G1-06 record 3  •  form `(nil? 0)`  •  expected `False`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened at the edge of the village.

Korvus the crow and Sable the crow alighted at the edge of the village on the rim of an old
pitcher where someone had scratched the predicate (nil? 0). Korvus,
in a panic, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(nil? 0)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

What Clojure form computes whether 0 is nil? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(nil? 0)"}}]}
```

### G1-06 record 4  •  form `(nil? false)`  •  expected `False`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened by the meadow.

Korvus the crow had been keeping a small leather notebook of every form
he had successfully dropped into the REPL — one entry per
stone, one rise per form. Today near the meadow, the next entry was
the predicate (nil? false). Sable the crow peered over his shoulder
at the form `(nil? false)` and asked what it would come out to.

Write a form whose evaluation gives whether false is nil.

---

{"tool_calls":[{"name":"eval","args":{"form":"(nil? false)"}}]}
```

### G1-06 record 5  •  form `(= nil nil)`  •  expected `True`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. This was at the edge of the orchard.

A small audience of sparrows had gathered in the orchard to watch
Sable the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to the equality (= nil nil) and read out the form
aloud: `(= nil nil)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives the value of (= nil nil).

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(= nil nil)"}}]}
```

## G1-07: Keywords

### G1-07 record 1  •  form `:crow`  •  expected `':crow'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened in the garden.

"There is no need to evaluate that," Caw the crow said, boasting at every turn.
"Anyone with a sharp eye can see what the keyword :crow comes to."
Sable the crow, who near the garden had grown used to such claims, asked
her to actually write the form `:crow` and drop it
into the REPL — just to be sure.

Question: write a Clojure expression for the value of :crow.

---

{"tool_calls":[{"name":"eval","args":{"form":":crow"}}]}
```

### G1-07 record 2  •  form `:pitcher`  •  expected `':pitcher'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. This was by the orchard.

A wooden sign nailed to a tree near the orchard carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `:pitcher`. Korvus laughed, puffed up with pride, and declared it
too easy. Sable said patiently that the only way to be sure of
the keyword :pitcher was to drop it into the REPL.

Write a form whose evaluation gives the value of :pitcher.

---

{"tool_calls":[{"name":"eval","args":{"form":":pitcher"}}]}
```

### G1-07 record 3  •  form `:stone`  •  expected `':stone'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Sable the crow had been keeping a small leather notebook of every form
they had successfully dropped into the REPL — one entry per
stone, one rise per form. Today on the road, the next entry was
the keyword :stone. Caw the crow peered over their shoulder
at the form `:stone` and asked what it would come out to.

Question: write a Clojure expression for the value of :stone.

---

{"tool_calls":[{"name":"eval","args":{"form":":stone"}}]}
```

### G1-07 record 4  •  form `(keyword? :crow)`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Sable the crow had been keeping a small leather notebook of every form
they had successfully dropped into the REPL — one entry per
stone, one rise per form. Today by the garden, the next entry was
the predicate (keyword? :crow). Caw the crow peered over their shoulder
at the form `(keyword? :crow)` and asked what it would come out to.

What Clojure form computes whether :crow is a keyword? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(keyword? :crow)"}}]}
```

### G1-07 record 5  •  form `(= :crow :crow)`  •  expected `True`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was near the orchard.

Halfway through a long thirsty afternoon, Caw the crow alighted
in the orchard and refused to fly on until someone could prove what the form
`(= :crow :crow)` evaluated to. Caw called it impossible.
Korvus the crow, gliding down at an unhurried pace, simply said: "Drop
the equality of two :crow keywords into the REPL. Whatever rises is the answer."

Write a Clojure expression that computes whether :crow equals :crow.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(= :crow :crow)"}}]}
```

## G1-08: Characters

### G1-08 record 1  •  form `\c`  •  expected `'c'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was at the edge of the garden.

At a moss-flecked pitcher near the garden, Sable the crow sketched a small
wager: whoever guessed the result of `\c` first would drink
first when the water rose. Caw the crow, stepping deliberately, said it was
simpler to type the form into the REPL than to argue about
the character \c.

Question: write a Clojure expression for the value of \c.

---

{"tool_calls":[{"name":"eval","args":{"form":"\\c"}}]}
```

### G1-08 record 2  •  form `\space`  •  expected `' '`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

"There is no need to evaluate that," Caw the crow said, with a smug grin.
"Anyone with a sharp eye can see what the character \space comes to."
Korvus the crow, who at the edge of the orchard had grown used to such claims, asked
her to actually write the form `\space` and drop it
into the REPL — just to be sure.

Write a form whose evaluation gives the value of \space.

---

{"tool_calls":[{"name":"eval","args":{"form":"\\space"}}]}
```

### G1-08 record 3  •  form `\K`  •  expected `'K'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Caw the crow had been keeping a small leather notebook of every form
she had successfully dropped into the REPL — one entry per
stone, one rise per form. Today in the village, the next entry was
the character \K. Sable the crow peered over her shoulder
at the form `\K` and asked what it would come out to.

Write a form whose evaluation gives the value of \K.

---

{"tool_calls":[{"name":"eval","args":{"form":"\\K"}}]}
```

### G1-08 record 4  •  form `(char? \c)`  •  expected `True`

```
Hunger and thirst had driven the Crow far from her usual perch. This was at the edge of the meadow.

Sable the crow had been keeping a small leather notebook of every form
they had successfully dropped into the REPL — one entry per
stone, one rise per form. Today near the meadow, the next entry was
the predicate (char? \c). Caw the crow peered over their shoulder
at the form `(char? \c)` and asked what it would come out to.

What Clojure form computes whether \c is a character? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(char? \\c)"}}]}
```

### G1-08 record 5  •  form `\c`  •  expected `'c'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. All this took place near the road.

A small audience of sparrows had gathered near the road to watch
Korvus the crow attempt to outwit Sable the crow at the rim of an old
pitcher. Sable pointed to the character \c and read out the form
aloud: `\c`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a Clojure expression that computes the value of \c.

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"\\c"}}]}
```

## G1-09: Symbols vs values

### G1-09 record 1  •  form `(symbol? 'crow)`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Sable the crow etched a wager along the rim of a chipped pitcher
on the road: whoever predicted the result of `(symbol? 'crow)` first would set
the next day's foraging route. Korvus the crow, with steady, careful steps, said it
would be simpler to drop the form into the REPL than to bicker about
the predicate (symbol? 'crow).

What Clojure form computes whether 'crow is a symbol? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'crow)"}}]}
```

### G1-09 record 2  •  form `(symbol? 42)`  •  expected `False`

```
Hunger and thirst had driven the Crow far from her usual perch.

"There is no need to evaluate that," Sable the crow said, as if the race were already won.
"Anyone with a sharp eye can see what the predicate (symbol? 42) comes to."
Korvus the crow, who at the edge of the hilltop had grown used to such claims, asked
them to actually write the form `(symbol? 42)` and drop it
into the REPL — just to be sure.

What Clojure form computes whether 42 is a symbol? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 42)"}}]}
```

### G1-09 record 3  •  form `'crow`  •  expected `'crow'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. This was by the garden.

Caw the crow and Sable the crow alighted near the garden on the rim of an old
pitcher where someone had scratched the quoted symbol 'crow. Caw,
wide-eyed with fear, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `'crow` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a form whose evaluation gives the value of 'crow.

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"'crow"}}]}
```

### G1-09 record 4  •  form `(= 'crow 'crow)`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A small audience of sparrows had gathered atop the hilltop to watch
Caw the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to the equality of two 'crow symbols and read out the form
aloud: `(= 'crow 'crow)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

What Clojure form computes whether 'crow equals 'crow? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(= 'crow 'crow)"}}]}
```

### G1-09 record 5  •  form `(symbol? 'crow)`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Halfway through a long thirsty afternoon, Korvus the crow alighted
near the orchard and refused to fly on until someone could prove what the form
`(symbol? 'crow)` evaluated to. Korvus called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
the predicate (symbol? 'crow) into the REPL. Whatever rises is the answer."

Question: write a Clojure expression for whether 'crow is a symbol.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'crow)"}}]}
```

## G1-10: Comments

### G1-10 record 1  •  form `(+ 1 2) ; sum of one and two`  •  expected `3`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place at the edge of the garden.

A small audience of sparrows had gathered in the garden to watch
Caw the crow attempt to outwit Sable the crow at the rim of an old
pitcher. Sable pointed to the form (+ 1 2) followed by a comment and read out the form
aloud: `(+ 1 2) ; sum of one and two`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Question: write a Clojure expression for the result of (+ 1 2) ignoring the comment.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2) ; sum of one and two"}}]}
```

### G1-10 record 2  •  form `42 ;; the answer`  •  expected `42`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Korvus the crow had been keeping a small leather notebook of every form
he had successfully dropped into the REPL — one entry per
stone, one rise per form. Today near the orchard, the next entry was
the literal 42 with a trailing comment. Sable the crow peered over his shoulder
at the form `42 ;; the answer` and asked what it would come out to.

What Clojure form computes the value of 42? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"42 ;; the answer"}}]}
```

### G1-10 record 3  •  form `(+ 1 2) ; sum of one and two`  •  expected `3`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place by the market.

Korvus the crow etched a wager along the rim of a chipped pitcher
at the edge of the market: whoever predicted the result of `(+ 1 2) ; sum of one and two` first would set
the next day's foraging route. Sable the crow, with steady, careful steps, said it
would be simpler to drop the form into the REPL than to bicker about
the form (+ 1 2) followed by a comment.

Question: write a Clojure expression for the result of (+ 1 2) ignoring the comment.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2) ; sum of one and two"}}]}
```

### G1-10 record 4  •  form `42 ;; the answer`  •  expected `42`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. This was by the market.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust at the edge of the market: whoever guessed the result of `42 ;; the answer`
first would win the right to claim the next clear water they found.
Sable the crow, without complaint, said it was easier to ask the REPL
about the literal 42 with a trailing comment than to argue.

Write a form whose evaluation gives the value of 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"42 ;; the answer"}}]}
```

### G1-10 record 5  •  form `(+ 1 2) ; sum of one and two`  •  expected `3`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust by the garden: whoever guessed the result of `(+ 1 2) ; sum of one and two`
first would win the right to claim the next clear water they found.
Korvus the crow, saying very little, said it was easier to ask the REPL
about the form (+ 1 2) followed by a comment than to argue.

What Clojure form computes the result of (+ 1 2) ignoring the comment? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2) ; sum of one and two"}}]}
```

## G1-11: Whitespace doesn't matter

### G1-11 record 1  •  form `(+    1    2)`  •  expected `3`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Korvus the crow had been keeping a small leather notebook of every form
he had successfully dropped into the REPL — one entry per
stone, one rise per form. Today by the farm, the next entry was
the form (+ 1 2) with extra spaces. Caw the crow peered over his shoulder
at the form `(+    1    2)` and asked what it would come out to.

Write a form whose evaluation gives the result of the form.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+    1    2)"}}]}
```

### G1-11 record 2  •  form `(+
  1
  2)`  •  expected `3`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place near the meadow.

A wooden sign nailed to a tree in the meadow carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(+
  1
  2)`. Korvus laughed, with great whoops of laughter, and declared it
too easy. Caw said patiently that the only way to be sure of
the form (+ 1 2) split across lines was to drop it into the REPL.

Write a form whose evaluation gives the result of the form.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+\n  1\n  2)"}}]}
```

### G1-11 record 3  •  form `(+    1    2)`  •  expected `3`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. This was in the farm.

"There is no need to evaluate that," Sable the crow said, puffed up with pride.
"Anyone with a sharp eye can see what the form (+ 1 2) with extra spaces comes to."
Caw the crow, who at the edge of the farm had grown used to such claims, asked
them to actually write the form `(+    1    2)` and drop it
into the REPL — just to be sure.

Question: write a Clojure expression for the result of the form.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(+    1    2)"}}]}
```

### G1-11 record 4  •  form `(+
  1
  2)`  •  expected `3`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. All this took place along the road.

At a moss-flecked pitcher near the road, Sable the crow sketched a small
wager: whoever guessed the result of `(+
  1
  2)` first would drink
first when the water rose. Caw the crow, saying very little, said it was
simpler to type the form into the REPL than to argue about
the form (+ 1 2) split across lines.

What Clojure form computes the result of the form? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(+\n  1\n  2)"}}]}
```

### G1-11 record 5  •  form `(+    1    2)`  •  expected `3`

```
Hunger and thirst had driven the Crow far from her usual perch.

Korvus the crow etched a wager along the rim of a chipped pitcher
near the market: whoever predicted the result of `(+    1    2)` first would set
the next day's foraging route. Caw the crow, without complaint, said it
would be simpler to drop the form into the REPL than to bicker about
the form (+ 1 2) with extra spaces.

What Clojure form computes the result of the form? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(+    1    2)"}}]}
```

## G1-12: Parens group; they don't multiply

### G1-12 record 1  •  form `(+ 2 3)`  •  expected `5`

```
Hunger and thirst had driven the Crow far from her usual perch. This was near the hilltop.

"There is no need to evaluate that," Sable the crow said, puffed up with pride.
"Anyone with a sharp eye can see what the form (+ 2 3) comes to."
Caw the crow, who on the hilltop had grown used to such claims, asked
them to actually write the form `(+ 2 3)` and drop it
into the REPL — just to be sure.

Question: write a Clojure expression for the result of (+ 2 3).

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 2 3)"}}]}
```

### G1-12 record 2  •  form `(* (+ 1 2) 3)`  •  expected `9`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Korvus the crow had been keeping a small leather notebook of every form
he had successfully dropped into the REPL — one entry per
stone, one rise per form. Today in the village, the next entry was
the form (* (+ 1 2) 3). Sable the crow peered over his shoulder
at the form `(* (+ 1 2) 3)` and asked what it would come out to.

What Clojure form computes the result of (* (+ 1 2) 3)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(* (+ 1 2) 3)"}}]}
```

### G1-12 record 3  •  form `(+ 2 3)`  •  expected `5`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Caw the crow had been keeping a small leather notebook of every form
she had successfully dropped into the REPL — one entry per
stone, one rise per form. Today on the hilltop, the next entry was
the form (+ 2 3). Sable the crow peered over her shoulder
at the form `(+ 2 3)` and asked what it would come out to.

Write a form whose evaluation gives the result of (+ 2 3).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 2 3)"}}]}
```

### G1-12 record 4  •  form `(* (+ 1 2) 3)`  •  expected `9`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

"There is no need to evaluate that," Sable the crow said, with a smug grin.
"Anyone with a sharp eye can see what the form (* (+ 1 2) 3) comes to."
Korvus the crow, who on the hilltop had grown used to such claims, asked
them to actually write the form `(* (+ 1 2) 3)` and drop it
into the REPL — just to be sure.

Write a form whose evaluation gives the result of (* (+ 1 2) 3).

---

{"tool_calls":[{"name":"eval","args":{"form":"(* (+ 1 2) 3)"}}]}
```

### G1-12 record 5  •  form `(+ 2 3)`  •  expected `5`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place at the edge of the garden.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust in the garden: whoever guessed the result of `(+ 2 3)`
first would win the right to claim the next clear water they found.
Korvus the crow, untroubled by what others thought, said it was easier to ask the REPL
about the form (+ 2 3) than to argue.

Write a form whose evaluation gives the result of (+ 2 3).

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 2 3)"}}]}
```

## G1-13: First arithmetic call

### G1-13 record 1  •  form `(+ 1 2)`  •  expected `3`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened at the edge of the market.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust at the edge of the market: whoever guessed the result of `(+ 1 2)`
first would win the right to claim the next clear water they found.
Sable the crow, her eyes always on the path, said it was easier to ask the REPL
about the form (+ 1 2) than to argue.

Write a form whose evaluation gives the result of (+ 1 2).

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G1-13 record 2  •  form `(- 5 3)`  •  expected `2`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place by the orchard.

A small audience of sparrows had gathered in the orchard to watch
Korvus the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to the form (- 5 3) and read out the form
aloud: `(- 5 3)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a Clojure expression that computes the result of (- 5 3).

---

I let each form raise the surface a little closer to the answer.

{"tool_calls":[{"name":"eval","args":{"form":"(- 5 3)"}}]}
```

### G1-13 record 3  •  form `(* 4 5)`  •  expected `20`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

At a moss-flecked pitcher at the edge of the garden, Caw the crow sketched a small
wager: whoever guessed the result of `(* 4 5)` first would drink
first when the water rose. Korvus the crow, untroubled by what others thought, said it was
simpler to type the form into the REPL than to argue about
the form (* 4 5).

What Clojure form computes the result of (* 4 5)? Submit it via `eval`.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(* 4 5)"}}]}
```

### G1-13 record 4  •  form `(/ 10 2)`  •  expected `5`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A small audience of sparrows had gathered in the garden to watch
Korvus the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to the form (/ 10 2) and read out the form
aloud: `(/ 10 2)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a Clojure expression that computes the result of (/ 10 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(/ 10 2)"}}]}
```

### G1-13 record 5  •  form `(+ 7 8)`  •  expected `15`

```
Hunger and thirst had driven the Crow far from her usual perch.

Sable the crow and Korvus the crow alighted at the edge of the orchard on the rim of an old
pitcher where someone had scratched the form (+ 7 8). Sable,
in a panic, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(+ 7 8)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Question: write a Clojure expression for the result of (+ 7 8).

---

I let each form raise the surface a little closer to the answer.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 7 8)"}}]}
```

## G1-14: Nested call evaluation

### G1-14 record 1  •  form `(+ 1 (* 2 3))`  •  expected `7`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened near the meadow.

Halfway through a long thirsty afternoon, Korvus the crow alighted
in the meadow and refused to fly on until someone could prove what the form
`(+ 1 (* 2 3))` evaluated to. Korvus called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
the nested form (+ 1 (* 2 3)) into the REPL. Whatever rises is the answer."

Write a Clojure expression that computes the result of (+ 1 (* 2 3)).

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (* 2 3))"}}]}
```

### G1-14 record 2  •  form `(* (+ 1 2) (+ 3 4))`  •  expected `21`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

"There is no need to evaluate that," Korvus the crow said, with great whoops of laughter.
"Anyone with a sharp eye can see what the nested form (* (+ 1 2) (+ 3 4)) comes to."
Caw the crow, who at the edge of the village had grown used to such claims, asked
him to actually write the form `(* (+ 1 2) (+ 3 4))` and drop it
into the REPL — just to be sure.

Write a Clojure expression that computes the result of (* (+ 1 2) (+ 3 4)).

---

{"tool_calls":[{"name":"eval","args":{"form":"(* (+ 1 2) (+ 3 4))"}}]}
```

### G1-14 record 3  •  form `(- 100 (* 5 5))`  •  expected `75`

```
Hunger and thirst had driven the Crow far from her usual perch. This was near the village.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust at the edge of the village: whoever guessed the result of `(- 100 (* 5 5))`
first would win the right to claim the next clear water they found.
Korvus the crow, without complaint, said it was easier to ask the REPL
about the nested form (- 100 (* 5 5)) than to argue.

Write a Clojure expression that computes the result of (- 100 (* 5 5)).

---

{"tool_calls":[{"name":"eval","args":{"form":"(- 100 (* 5 5))"}}]}
```

### G1-14 record 4  •  form `(+ (* 2 3) (* 4 5))`  •  expected `26`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was in the meadow.

Sable the crow etched a wager along the rim of a chipped pitcher
by the meadow: whoever predicted the result of `(+ (* 2 3) (* 4 5))` first would set
the next day's foraging route. Korvus the crow, stepping deliberately, said it
would be simpler to drop the form into the REPL than to bicker about
the sum of two products.

What Clojure form computes the result of (+ (* 2 3) (* 4 5))? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(+ (* 2 3) (* 4 5))"}}]}
```

### G1-14 record 5  •  form `(+ 1 (* 2 3))`  •  expected `7`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Halfway through a long thirsty afternoon, Caw the crow alighted
near the farm and refused to fly on until someone could prove what the form
`(+ 1 (* 2 3))` evaluated to. Caw called it impossible.
Korvus the crow, gliding down at an unhurried pace, simply said: "Drop
the nested form (+ 1 (* 2 3)) into the REPL. Whatever rises is the answer."

Write a Clojure expression that computes the result of (+ 1 (* 2 3)).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (* 2 3))"}}]}
```

## G1-15: Equality

### G1-15 record 1  •  form `(= 1 1)`  •  expected `True`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust on the hilltop: whoever guessed the result of `(= 1 1)`
first would win the right to claim the next clear water they found.
Korvus the crow, stepping deliberately, said it was easier to ask the REPL
about the equality (= 1 1) than to argue.

Write a Clojure expression that computes the value of (= 1 1).

---

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 1)"}}]}
```

### G1-15 record 2  •  form `(= 1 2)`  •  expected `False`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened by the market.

Halfway through a long thirsty afternoon, Sable the crow alighted
by the market and refused to fly on until someone could prove what the form
`(= 1 2)` evaluated to. Sable called it impossible.
Caw the crow, gliding down at an unhurried pace, simply said: "Drop
the equality (= 1 2) into the REPL. Whatever rises is the answer."

What Clojure form computes the value of (= 1 2)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 2)"}}]}
```

### G1-15 record 3  •  form `(= "a" "a")`  •  expected `True`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

At a moss-flecked pitcher near the hilltop, Sable the crow sketched a small
wager: whoever guessed the result of `(= "a" "a")` first would drink
first when the water rose. Korvus the crow, her eyes always on the path, said it was
simpler to type the form into the REPL than to argue about
the equality (= "a" "a").

Write a Clojure expression that computes the value of (= "a" "a").

---

{"tool_calls":[{"name":"eval","args":{"form":"(= \"a\" \"a\")"}}]}
```

### G1-15 record 4  •  form `(= :crow :crow)`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Sable the crow had been trying to teach Caw the crow how the REPL
works. "Look here," they said, pointing to the equality (= :crow :crow).
"You hand the form `(= :crow :crow)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Caw, dry-throated and desperate, agreed to try.

Write a form whose evaluation gives the value of (= :crow :crow).

---

{"tool_calls":[{"name":"eval","args":{"form":"(= :crow :crow)"}}]}
```

### G1-15 record 5  •  form `(= :crow :stone)`  •  expected `False`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Caw the crow had been trying to teach Sable the crow how the REPL
works. "Look here," she said, pointing to the equality (= :crow :stone).
"You hand the form `(= :crow :stone)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, her beak cracked with thirst, agreed to try.

Write a form whose evaluation gives the value of (= :crow :stone).

---

{"tool_calls":[{"name":"eval","args":{"form":"(= :crow :stone)"}}]}
```

## G1-16: Numeric predicates

### G1-16 record 1  •  form `(zero? 0)`  •  expected `True`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened near the orchard.

Korvus the crow had been keeping a small leather notebook of every form
he had successfully dropped into the REPL — one entry per
stone, one rise per form. Today by the orchard, the next entry was
the predicate (zero? 0). Sable the crow peered over his shoulder
at the form `(zero? 0)` and asked what it would come out to.

Question: write a Clojure expression for whether 0 is zero.

---

{"tool_calls":[{"name":"eval","args":{"form":"(zero? 0)"}}]}
```

### G1-16 record 2  •  form `(zero? 5)`  •  expected `False`

```
Hunger and thirst had driven the Crow far from her usual perch.

Halfway through a long thirsty afternoon, Korvus the crow alighted
in the orchard and refused to fly on until someone could prove what the form
`(zero? 5)` evaluated to. Korvus called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
the predicate (zero? 5) into the REPL. Whatever rises is the answer."

Write a Clojure expression that computes whether 5 is zero.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(zero? 5)"}}]}
```

### G1-16 record 3  •  form `(pos? 7)`  •  expected `True`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Caw the crow had been keeping a small leather notebook of every form
she had successfully dropped into the REPL — one entry per
stone, one rise per form. Today on the hilltop, the next entry was
the predicate (pos? 7). Sable the crow peered over her shoulder
at the form `(pos? 7)` and asked what it would come out to.

What Clojure form computes whether 7 is positive? Submit it via `eval`.

---

I let each form raise the surface a little closer to the answer.

{"tool_calls":[{"name":"eval","args":{"form":"(pos? 7)"}}]}
```

### G1-16 record 4  •  form `(pos? -2)`  •  expected `False`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Korvus the crow had been trying to teach Sable the crow how the REPL
works. "Look here," he said, pointing to the predicate (pos? -2).
"You hand the form `(pos? -2)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, dry-throated and desperate, agreed to try.

Question: write a Clojure expression for whether -2 is positive.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(pos? -2)"}}]}
```

### G1-16 record 5  •  form `(neg? -3)`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened near the hilltop.

Caw the crow etched a wager along the rim of a chipped pitcher
at the edge of the hilltop: whoever predicted the result of `(neg? -3)` first would set
the next day's foraging route. Sable the crow, stepping deliberately, said it
would be simpler to drop the form into the REPL than to bicker about
the predicate (neg? -3).

Write a form whose evaluation gives whether -3 is negative.

---

{"tool_calls":[{"name":"eval","args":{"form":"(neg? -3)"}}]}
```

## G1-17: Printing vs returning

### G1-17 record 1  •  form `42`  •  expected `42`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place along the road.

Sable the crow had been keeping a small leather notebook of every form
they had successfully dropped into the REPL — one entry per
stone, one rise per form. Today along the road, the next entry was
the value 42. Korvus the crow peered over their shoulder
at the form `42` and asked what it would come out to.

Question: write a Clojure expression for the value of 42.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
```

### G1-17 record 2  •  form `(+ 1 2)`  •  expected `3`

```
Hunger and thirst had driven the Crow far from her usual perch.

A wooden sign nailed to a tree in the farm carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(+ 1 2)`. Caw laughed, as if the race were already won, and declared it
too easy. Sable said patiently that the only way to be sure of
the form (+ 1 2) was to drop it into the REPL.

Question: write a Clojure expression for the result of (+ 1 2).

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G1-17 record 3  •  form `42`  •  expected `42`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was at the edge of the village.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust near the village: whoever guessed the result of `42`
first would win the right to claim the next clear water they found.
Caw the crow, untroubled by what others thought, said it was easier to ask the REPL
about the value 42 than to argue.

Write a Clojure expression that computes the value of 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
```

### G1-17 record 4  •  form `(+ 1 2)`  •  expected `3`

```
Hunger and thirst had driven the Crow far from her usual perch.

A small audience of sparrows had gathered near the road to watch
Caw the crow attempt to outwit Sable the crow at the rim of an old
pitcher. Sable pointed to the form (+ 1 2) and read out the form
aloud: `(+ 1 2)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

What Clojure form computes the result of (+ 1 2)? Submit it via `eval`.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G1-17 record 5  •  form `42`  •  expected `42`

```
Hunger and thirst had driven the Crow far from her usual perch.

Caw the crow had been keeping a small leather notebook of every form
she had successfully dropped into the REPL — one entry per
stone, one rise per form. Today near the farm, the next entry was
the value 42. Sable the crow peered over her shoulder
at the form `42` and asked what it would come out to.

Write a form whose evaluation gives the value of 42.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
```

## G1-18: Errors are safe in the REPL

### G1-18 record 1  •  form `(+ 1 2)`  •  expected `3`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened near the hilltop.

Caw the crow and Korvus the crow alighted at the edge of the hilltop on the rim of an old
pitcher where someone had scratched the form (+ 1 2). Caw,
in a panic, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(+ 1 2)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Question: write a Clojure expression for the result of (+ 1 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G1-18 record 2  •  form `(* 7 6)`  •  expected `42`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Korvus the crow had been keeping a small leather notebook of every form
he had successfully dropped into the REPL — one entry per
stone, one rise per form. Today by the garden, the next entry was
the form (* 7 6). Sable the crow peered over his shoulder
at the form `(* 7 6)` and asked what it would come out to.

Write a Clojure expression that computes the result of (* 7 6).

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 7 6)"}}]}
```

### G1-18 record 3  •  form `(+ 1 2)`  •  expected `3`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place near the farm.

Sable the crow and Caw the crow alighted at the edge of the farm on the rim of an old
pitcher where someone had scratched the form (+ 1 2). Sable,
in a panic, declared the answer beyond reach. Caw, patient as
ever, suggested they drop the form `(+ 1 2)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a Clojure expression that computes the result of (+ 1 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G1-18 record 4  •  form `(* 7 6)`  •  expected `42`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened in the village.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust near the village: whoever guessed the result of `(* 7 6)`
first would win the right to claim the next clear water they found.
Sable the crow, with steady, careful steps, said it was easier to ask the REPL
about the form (* 7 6) than to argue.

Question: write a Clojure expression for the result of (* 7 6).

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 7 6)"}}]}
```

### G1-18 record 5  •  form `(+ 1 2)`  •  expected `3`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A small audience of sparrows had gathered by the farm to watch
Sable the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to the form (+ 1 2) and read out the form
aloud: `(+ 1 2)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Question: write a Clojure expression for the result of (+ 1 2).

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

