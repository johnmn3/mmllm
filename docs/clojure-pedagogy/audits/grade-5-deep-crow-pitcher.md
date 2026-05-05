# crow-pitcher grade 5 — deep spot-check

5 records per subject for hand-audit.

---

## G5-01: if

### G5-01 record 1  •  form `(if true :a :b)`  •  expected `':a'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was by the farm.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust at the edge of the farm: whoever guessed the result of `(if true :a :b)`
first would win the right to claim the next clear water they found.
Sable the crow, with steady, careful steps, said it was easier to ask the REPL
about the form (if true :a :b) than to argue.

Write a form whose evaluation gives which of :a or :b is returned.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(if true :a :b)"}}]}
```

### G5-01 record 2  •  form `(if false :a :b)`  •  expected `':b'`

```
Hunger and thirst had driven the Crow far from her usual perch.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust at the edge of the farm: whoever guessed the result of `(if false :a :b)`
first would win the right to claim the next clear water they found.
Korvus the crow, saying very little, said it was easier to ask the REPL
about the form (if false :a :b) than to argue.

What Clojure form computes which of :a or :b is returned? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(if false :a :b)"}}]}
```

### G5-01 record 3  •  form `(if (> 5 3) :a :b)`  •  expected `':a'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Halfway through a long thirsty afternoon, Caw the crow alighted
along the road and refused to fly on until someone could prove what the form
`(if (> 5 3) :a :b)` evaluated to. Caw called it impossible.
Korvus the crow, gliding down at an unhurried pace, simply said: "Drop
the form (if (> 5 3) :a :b) into the REPL. Whatever rises is the answer."

Question: write a Clojure expression for the if's branch.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(if (> 5 3) :a :b)"}}]}
```

### G5-01 record 4  •  form `(if true :a :b)`  •  expected `':a'`

```
Hunger and thirst had driven the Crow far from her usual perch.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust near the garden: whoever guessed the result of `(if true :a :b)`
first would win the right to claim the next clear water they found.
Sable the crow, stepping deliberately, said it was easier to ask the REPL
about the form (if true :a :b) than to argue.

Question: write a Clojure expression for which of :a or :b is returned.

---

{"tool_calls":[{"name":"eval","args":{"form":"(if true :a :b)"}}]}
```

### G5-01 record 5  •  form `(if false :a :b)`  •  expected `':b'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Caw the crow had been keeping a small leather notebook of every form
she had successfully dropped into the REPL — one entry per
stone, one rise per form. Today by the meadow, the next entry was
the form (if false :a :b). Korvus the crow peered over her shoulder
at the form `(if false :a :b)` and asked what it would come out to.

What Clojure form computes which of :a or :b is returned? Submit it via `eval`.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(if false :a :b)"}}]}
```

## G5-02: if as expression

### G5-02 record 1  •  form `(+ 1 (if true 10 20))`  •  expected `11`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place in the garden.

Korvus the crow etched a wager along the rim of a chipped pitcher
near the garden: whoever predicted the result of `(+ 1 (if true 10 20))` first would set
the next day's foraging route. Caw the crow, stepping deliberately, said it
would be simpler to drop the form into the REPL than to bicker about
the form (+ 1 (if true 10 20)).

Write a form whose evaluation gives the result of adding 1 to the if expression.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (if true 10 20))"}}]}
```

### G5-02 record 2  •  form `(+ 1 (if true 10 20))`  •  expected `11`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was at the edge of the meadow.

A small audience of sparrows had gathered in the meadow to watch
Sable the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to the form (+ 1 (if true 10 20)) and read out the form
aloud: `(+ 1 (if true 10 20))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a Clojure expression that computes the result of adding 1 to the if expression.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (if true 10 20))"}}]}
```

### G5-02 record 3  •  form `(+ 1 (if true 10 20))`  •  expected `11`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was near the orchard.

Caw the crow and Sable the crow alighted at the edge of the orchard on the rim of an old
pitcher where someone had scratched the form (+ 1 (if true 10 20)). Caw,
in a panic, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(+ 1 (if true 10 20))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

What Clojure form computes the result of adding 1 to the if expression? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (if true 10 20))"}}]}
```

### G5-02 record 4  •  form `(+ 1 (if true 10 20))`  •  expected `11`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Sable the crow and Korvus the crow alighted on the road on the rim of an old
pitcher where someone had scratched the form (+ 1 (if true 10 20)). Sable,
shouting until her voice cracked, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(+ 1 (if true 10 20))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Question: write a Clojure expression for the result of adding 1 to the if expression.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (if true 10 20))"}}]}
```

### G5-02 record 5  •  form `(+ 1 (if true 10 20))`  •  expected `11`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened near the garden.

Sable the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," they said, pointing to the form (+ 1 (if true 10 20)).
"You hand the form `(+ 1 (if true 10 20))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, with a thirst that hurt to bear, agreed to try.

Write a form whose evaluation gives the result of adding 1 to the if expression.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (if true 10 20))"}}]}
```

## G5-03: when

### G5-03 record 1  •  form `(when true :yes)`  •  expected `':yes'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place in the orchard.

Caw the crow and Korvus the crow alighted near the orchard on the rim of an old
pitcher where someone had scratched the form (when true :yes). Caw,
her hands trembling, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(when true :yes)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Question: write a Clojure expression for the value of (when true :yes).

---

I let each form raise the surface a little closer to the answer.

{"tool_calls":[{"name":"eval","args":{"form":"(when true :yes)"}}]}
```

### G5-03 record 2  •  form `(when false :yes)`  •  expected `None`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust at the edge of the garden: whoever guessed the result of `(when false :yes)`
first would win the right to claim the next clear water they found.
Korvus the crow, stepping deliberately, said it was easier to ask the REPL
about the form (when false :yes) than to argue.

Question: write a Clojure expression for the value of (when false :yes).

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(when false :yes)"}}]}
```

### G5-03 record 3  •  form `(when true :yes)`  •  expected `':yes'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Caw the crow had been keeping a small leather notebook of every form
she had successfully dropped into the REPL — one entry per
stone, one rise per form. Today in the farm, the next entry was
the form (when true :yes). Korvus the crow peered over her shoulder
at the form `(when true :yes)` and asked what it would come out to.

Write a form whose evaluation gives the value of (when true :yes).

---

{"tool_calls":[{"name":"eval","args":{"form":"(when true :yes)"}}]}
```

### G5-03 record 4  •  form `(when false :yes)`  •  expected `None`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place at the edge of the meadow.

A small audience of sparrows had gathered near the meadow to watch
Korvus the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to the form (when false :yes) and read out the form
aloud: `(when false :yes)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a Clojure expression that computes the value of (when false :yes).

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(when false :yes)"}}]}
```

### G5-03 record 5  •  form `(when true :yes)`  •  expected `':yes'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

A wooden sign nailed to a tree by the village carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(when true :yes)`. Sable laughed, puffed up with pride, and declared it
too easy. Korvus said patiently that the only way to be sure of
the form (when true :yes) was to drop it into the REPL.

Write a form whose evaluation gives the value of (when true :yes).

---

I use map / filter / reduce as appropriate.

{"tool_calls":[{"name":"eval","args":{"form":"(when true :yes)"}}]}
```

## G5-04: cond

### G5-04 record 1  •  form `(cond (= 1 2) :a (= 1 1) :b :else :c)`  •  expected `':b'`

```
Hunger and thirst had driven the Crow far from her usual perch.

"Same trick, repeated cleverly," Caw said, stepping deliberately,
at the edge of the meadow, sketching the form `(cond (= 1 2) :a (= 1 1) :b :else :c)` into the dust. Korvus,
with great whoops of laughter, claimed to know exactly what the cond form would
produce — but Caw insisted, again, that the REPL was the only
honest judge.

What Clojure form computes which clause of the cond fires? Submit it via `eval`.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(cond (= 1 2) :a (= 1 1) :b :else :c)"}}]}
```

### G5-04 record 2  •  form `(cond (= 1 2) :a (= 1 1) :b :else :c)`  •  expected `':b'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Sable the crow etched a wager along the rim of a chipped pitcher
by the village: whoever predicted the result of `(cond (= 1 2) :a (= 1 1) :b :else :c)` first would set
the next day's foraging route. Korvus the crow, without complaint, said it
would be simpler to drop the form into the REPL than to bicker about
the cond form.

Question: write a Clojure expression for which clause of the cond fires.

---

{"tool_calls":[{"name":"eval","args":{"form":"(cond (= 1 2) :a (= 1 1) :b :else :c)"}}]}
```

### G5-04 record 3  •  form `(cond (= 1 2) :a (= 1 1) :b :else :c)`  •  expected `':b'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A small audience of sparrows had gathered atop the hilltop to watch
Caw the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to the cond form and read out the form
aloud: `(cond (= 1 2) :a (= 1 1) :b :else :c)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a Clojure expression that computes which clause of the cond fires.

---

{"tool_calls":[{"name":"eval","args":{"form":"(cond (= 1 2) :a (= 1 1) :b :else :c)"}}]}
```

### G5-04 record 4  •  form `(cond (= 1 2) :a (= 1 1) :b :else :c)`  •  expected `':b'`

```
Hunger and thirst had driven the Crow far from her usual perch.

Korvus the crow and Sable the crow alighted at the edge of the garden on the rim of an old
pitcher where someone had scratched the cond form. Korvus,
with growing alarm, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(cond (= 1 2) :a (= 1 1) :b :else :c)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a form whose evaluation gives which clause of the cond fires.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(cond (= 1 2) :a (= 1 1) :b :else :c)"}}]}
```

### G5-04 record 5  •  form `(cond (= 1 2) :a (= 1 1) :b :else :c)`  •  expected `':b'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

At a moss-flecked pitcher in the meadow, Korvus the crow sketched a small
wager: whoever guessed the result of `(cond (= 1 2) :a (= 1 1) :b :else :c)` first would drink
first when the water rose. Sable the crow, saying very little, said it was
simpler to type the form into the REPL than to argue about
the cond form.

Write a Clojure expression that computes which clause of the cond fires.

---

{"tool_calls":[{"name":"eval","args":{"form":"(cond (= 1 2) :a (= 1 1) :b :else :c)"}}]}
```

## G5-05: cond — :else

### G5-05 record 1  •  form `(cond false :a false :b :else :c)`  •  expected `':c'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place near the farm.

"There is no need to evaluate that," Korvus the crow said, puffed up with pride.
"Anyone with a sharp eye can see what the cond falling through to :else comes to."
Caw the crow, who by the farm had grown used to such claims, asked
him to actually write the form `(cond false :a false :b :else :c)` and drop it
into the REPL — just to be sure.

What Clojure form computes the :else value? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(cond false :a false :b :else :c)"}}]}
```

### G5-05 record 2  •  form `(cond false :a false :b :else :c)`  •  expected `':c'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

"Same trick, repeated cleverly," Korvus said, her eyes always on the path,
near the farm, sketching the form `(cond false :a false :b :else :c)` into the dust. Caw,
puffed up with pride, claimed to know exactly what the cond falling through to :else would
produce — but Korvus insisted, again, that the REPL was the only
honest judge.

Question: write a Clojure expression for the :else value.

---

{"tool_calls":[{"name":"eval","args":{"form":"(cond false :a false :b :else :c)"}}]}
```

### G5-05 record 3  •  form `(cond false :a false :b :else :c)`  •  expected `':c'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A wooden sign nailed to a tree by the farm carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(cond false :a false :b :else :c)`. Korvus laughed, with a smug grin, and declared it
too easy. Caw said patiently that the only way to be sure of
the cond falling through to :else was to drop it into the REPL.

What Clojure form computes the :else value? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(cond false :a false :b :else :c)"}}]}
```

### G5-05 record 4  •  form `(cond false :a false :b :else :c)`  •  expected `':c'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened in the meadow.

Sable the crow demonstrated by the meadow how the same operation, applied
to many things at once, was the heart of every long calculation. The
form `(cond false :a false :b :else :c)` captured the cond falling through to :else, and Caw the crow
agreed to write it for the REPL.

Question: write a Clojure expression for the :else value.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(cond false :a false :b :else :c)"}}]}
```

### G5-05 record 5  •  form `(cond false :a false :b :else :c)`  •  expected `':c'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

"Same trick, repeated cleverly," Korvus said, her eyes always on the path,
in the market, sketching the form `(cond false :a false :b :else :c)` into the dust. Caw,
with great whoops of laughter, claimed to know exactly what the cond falling through to :else would
produce — but Korvus insisted, again, that the REPL was the only
honest judge.

Write a Clojure expression that computes the :else value.

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(cond false :a false :b :else :c)"}}]}
```

## G5-06: case

### G5-06 record 1  •  form `(case 2 1 :one 2 :two 3 :three :default)`  •  expected `':two'`

```
Hunger and thirst had driven the Crow far from her usual perch. It happened in the garden.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust in the garden: whoever guessed the result of `(case 2 1 :one 2 :two 3 :three :default)`
first would win the right to claim the next clear water they found.
Sable the crow, saying very little, said it was easier to ask the REPL
about the case form than to argue.

Write a form whose evaluation gives the matched branch.

---

{"tool_calls":[{"name":"eval","args":{"form":"(case 2 1 :one 2 :two 3 :three :default)"}}]}
```

### G5-06 record 2  •  form `(case 99 1 :one 2 :two :default)`  •  expected `':default'`

```
Hunger and thirst had driven the Crow far from her usual perch. This was in the farm.

Korvus the crow had been trying to teach Sable the crow how the REPL
works. "Look here," he said, pointing to case falling through to default.
"You hand the form `(case 99 1 :one 2 :two :default)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, near to giving up the search for water, agreed to try.

What Clojure form computes the default branch? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(case 99 1 :one 2 :two :default)"}}]}
```

### G5-06 record 3  •  form `(case 2 1 :one 2 :two 3 :three :default)`  •  expected `':two'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Korvus the crow etched a wager along the rim of a chipped pitcher
near the farm: whoever predicted the result of `(case 2 1 :one 2 :two 3 :three :default)` first would set
the next day's foraging route. Caw the crow, her eyes always on the path, said it
would be simpler to drop the form into the REPL than to bicker about
the case form.

What Clojure form computes the matched branch? Submit it via `eval`.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(case 2 1 :one 2 :two 3 :three :default)"}}]}
```

### G5-06 record 4  •  form `(case 99 1 :one 2 :two :default)`  •  expected `':default'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

"There is no need to evaluate that," Sable the crow said, with great whoops of laughter.
"Anyone with a sharp eye can see what case falling through to default comes to."
Korvus the crow, who near the market had grown used to such claims, asked
them to actually write the form `(case 99 1 :one 2 :two :default)` and drop it
into the REPL — just to be sure.

Write a Clojure expression that computes the default branch.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(case 99 1 :one 2 :two :default)"}}]}
```

### G5-06 record 5  •  form `(case 2 1 :one 2 :two 3 :three :default)`  •  expected `':two'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

"Same trick, repeated cleverly," Korvus said, stepping deliberately,
near the village, sketching the form `(case 2 1 :one 2 :two 3 :three :default)` into the dust. Sable,
with a smug grin, claimed to know exactly what the case form would
produce — but Korvus insisted, again, that the REPL was the only
honest judge.

What Clojure form computes the matched branch? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(case 2 1 :one 2 :two 3 :three :default)"}}]}
```

## G5-07: and / or as control flow

### G5-07 record 1  •  form `(and 1 2 3)`  •  expected `3`

```
Hunger and thirst had driven the Crow far from her usual perch. It happened at the edge of the village.

Sable the crow had been trying to teach Caw the crow how the REPL
works. "Look here," they said, pointing to the form (and 1 2 3) returns last truthy.
"You hand the form `(and 1 2 3)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Caw, her beak cracked with thirst, agreed to try.

Write a form whose evaluation gives the last truthy value.

---

{"tool_calls":[{"name":"eval","args":{"form":"(and 1 2 3)"}}]}
```

### G5-07 record 2  •  form `(or nil false :found)`  •  expected `':found'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened at the edge of the farm.

Sable the crow and Caw the crow alighted by the farm on the rim of an old
pitcher where someone had scratched the form (or nil false :found). Sable,
wide-eyed with fear, declared the answer beyond reach. Caw, patient as
ever, suggested they drop the form `(or nil false :found)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a Clojure expression that computes the first truthy value.

---

{"tool_calls":[{"name":"eval","args":{"form":"(or nil false :found)"}}]}
```

### G5-07 record 3  •  form `(and 1 2 3)`  •  expected `3`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

At a moss-flecked pitcher at the edge of the garden, Sable the crow sketched a small
wager: whoever guessed the result of `(and 1 2 3)` first would drink
first when the water rose. Caw the crow, her eyes always on the path, said it was
simpler to type the form into the REPL than to argue about
the form (and 1 2 3) returns last truthy.

Write a form whose evaluation gives the last truthy value.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(and 1 2 3)"}}]}
```

### G5-07 record 4  •  form `(or nil false :found)`  •  expected `':found'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Korvus the crow and Sable the crow alighted along the road on the rim of an old
pitcher where someone had scratched the form (or nil false :found). Korvus,
with growing alarm, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(or nil false :found)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Question: write a Clojure expression for the first truthy value.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(or nil false :found)"}}]}
```

### G5-07 record 5  •  form `(and 1 2 3)`  •  expected `3`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

A small audience of sparrows had gathered at the edge of the meadow to watch
Sable the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to the form (and 1 2 3) returns last truthy and read out the form
aloud: `(and 1 2 3)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

What Clojure form computes the last truthy value? Submit it via `eval`.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(and 1 2 3)"}}]}
```

## G5-08: not

### G5-08 record 1  •  form `(not (> 1 2))`  •  expected `True`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

At a moss-flecked pitcher by the farm, Caw the crow sketched a small
wager: whoever guessed the result of `(not (> 1 2))` first would drink
first when the water rose. Korvus the crow, untroubled by what others thought, said it was
simpler to type the form into the REPL than to argue about
the form (not (> 1 2)).

Question: write a Clojure expression for the negated comparison.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(not (> 1 2))"}}]}
```

### G5-08 record 2  •  form `(not (> 1 2))`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Korvus the crow demonstrated in the farm how the same operation, applied
to many things at once, was the heart of every long calculation. The
form `(not (> 1 2))` captured the form (not (> 1 2)), and Caw the crow
agreed to write it for the REPL.

Write a form whose evaluation gives the negated comparison.

---

{"tool_calls":[{"name":"eval","args":{"form":"(not (> 1 2))"}}]}
```

### G5-08 record 3  •  form `(not (> 1 2))`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust by the garden: whoever guessed the result of `(not (> 1 2))`
first would win the right to claim the next clear water they found.
Korvus the crow, untroubled by what others thought, said it was easier to ask the REPL
about the form (not (> 1 2)) than to argue.

Question: write a Clojure expression for the negated comparison.

---

{"tool_calls":[{"name":"eval","args":{"form":"(not (> 1 2))"}}]}
```

### G5-08 record 4  •  form `(not (> 1 2))`  •  expected `True`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place in the market.

Sable the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," they said, pointing to the form (not (> 1 2)).
"You hand the form `(not (> 1 2))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, parched from the long flight, agreed to try.

Write a Clojure expression that computes the negated comparison.

---

I let each form raise the surface a little closer to the answer.

{"tool_calls":[{"name":"eval","args":{"form":"(not (> 1 2))"}}]}
```

### G5-08 record 5  •  form `(not (> 1 2))`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Caw the crow and Korvus the crow alighted near the road on the rim of an old
pitcher where someone had scratched the form (not (> 1 2)). Caw,
with growing alarm, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(not (> 1 2))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a Clojure expression that computes the negated comparison.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(not (> 1 2))"}}]}
```

## G5-09: fn as value

### G5-09 record 1  •  form `((fn [f x] (f (f x))) inc 5)`  •  expected `7`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A wooden sign nailed to a tree along the road carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `((fn [f x] (f (f x))) inc 5)`. Sable laughed, swaggering through the underbrush, and declared it
too easy. Korvus said patiently that the only way to be sure of
applying f twice to x where f is inc was to drop it into the REPL.

What Clojure form computes the result of inc applied twice? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [f x] (f (f x))) inc 5)"}}]}
```

### G5-09 record 2  •  form `((fn [f x] (f (f x))) inc 5)`  •  expected `7`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

"Same trick, repeated cleverly," Korvus said, saying very little,
near the road, sketching the form `((fn [f x] (f (f x))) inc 5)` into the dust. Caw,
puffed up with pride, claimed to know exactly what applying f twice to x where f is inc would
produce — but Korvus insisted, again, that the REPL was the only
honest judge.

Write a Clojure expression that computes the result of inc applied twice.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [f x] (f (f x))) inc 5)"}}]}
```

### G5-09 record 3  •  form `((fn [f x] (f (f x))) inc 5)`  •  expected `7`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust in the meadow: whoever guessed the result of `((fn [f x] (f (f x))) inc 5)`
first would win the right to claim the next clear water they found.
Sable the crow, saying very little, said it was easier to ask the REPL
about applying f twice to x where f is inc than to argue.

Write a form whose evaluation gives the result of inc applied twice.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [f x] (f (f x))) inc 5)"}}]}
```

### G5-09 record 4  •  form `((fn [f x] (f (f x))) inc 5)`  •  expected `7`

```
Hunger and thirst had driven the Crow far from her usual perch.

"Same trick, repeated cleverly," Caw said, untroubled by what others thought,
near the village, sketching the form `((fn [f x] (f (f x))) inc 5)` into the dust. Korvus,
with a smug grin, claimed to know exactly what applying f twice to x where f is inc would
produce — but Caw insisted, again, that the REPL was the only
honest judge.

What Clojure form computes the result of inc applied twice? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [f x] (f (f x))) inc 5)"}}]}
```

### G5-09 record 5  •  form `((fn [f x] (f (f x))) inc 5)`  •  expected `7`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Caw the crow had been keeping a small leather notebook of every form
she had successfully dropped into the REPL — one entry per
stone, one rise per form. Today near the farm, the next entry was
applying f twice to x where f is inc. Korvus the crow peered over her shoulder
at the form `((fn [f x] (f (f x))) inc 5)` and asked what it would come out to.

Write a Clojure expression that computes the result of inc applied twice.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [f x] (f (f x))) inc 5)"}}]}
```

## G5-10: map

### G5-10 record 1  •  form `(map inc [1 2 3])`  •  expected `[2, 3, 4]`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. This was on the road.

Sable the crow and Caw the crow alighted on the road on the rim of an old
pitcher where someone had scratched the form (map inc [1 2 3]). Sable,
in a panic, declared the answer beyond reach. Caw, patient as
ever, suggested they drop the form `(map inc [1 2 3])` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

What Clojure form computes [1 2 3] each incremented? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(map inc [1 2 3])"}}]}
```

### G5-10 record 2  •  form `(map #(* % %) [1 2 3 4])`  •  expected `[1, 4, 9, 16]`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened on the road.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust near the road: whoever guessed the result of `(map #(* % %) [1 2 3 4])`
first would win the right to claim the next clear water they found.
Sable the crow, stepping deliberately, said it was easier to ask the REPL
about the form (map #(* % %) [1 2 3 4]) than to argue.

Write a Clojure expression that computes [1 2 3 4] each squared.

---

{"tool_calls":[{"name":"eval","args":{"form":"(map #(* % %) [1 2 3 4])"}}]}
```

### G5-10 record 3  •  form `(map inc [1 2 3])`  •  expected `[2, 3, 4]`

```
Hunger and thirst had driven the Crow far from her usual perch.

Sable the crow etched a wager along the rim of a chipped pitcher
by the orchard: whoever predicted the result of `(map inc [1 2 3])` first would set
the next day's foraging route. Caw the crow, untroubled by what others thought, said it
would be simpler to drop the form into the REPL than to bicker about
the form (map inc [1 2 3]).

Question: write a Clojure expression for [1 2 3] each incremented.

---

{"tool_calls":[{"name":"eval","args":{"form":"(map inc [1 2 3])"}}]}
```

### G5-10 record 4  •  form `(map #(* % %) [1 2 3 4])`  •  expected `[1, 4, 9, 16]`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

"Same trick, repeated cleverly," Korvus said, with steady, careful steps,
at the edge of the meadow, sketching the form `(map #(* % %) [1 2 3 4])` into the dust. Sable,
as if the race were already won, claimed to know exactly what the form (map #(* % %) [1 2 3 4]) would
produce — but Korvus insisted, again, that the REPL was the only
honest judge.

Write a Clojure expression that computes [1 2 3 4] each squared.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(map #(* % %) [1 2 3 4])"}}]}
```

### G5-10 record 5  •  form `(map inc [1 2 3])`  •  expected `[2, 3, 4]`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust on the road: whoever guessed the result of `(map inc [1 2 3])`
first would win the right to claim the next clear water they found.
Sable the crow, without complaint, said it was easier to ask the REPL
about the form (map inc [1 2 3]) than to argue.

Write a Clojure expression that computes [1 2 3] each incremented.

---

{"tool_calls":[{"name":"eval","args":{"form":"(map inc [1 2 3])"}}]}
```

## G5-11: filter

### G5-11 record 1  •  form `(filter even? [1 2 3 4])`  •  expected `[2, 4]`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place by the village.

Caw the crow and Korvus the crow alighted at the edge of the village on the rim of an old
pitcher where someone had scratched the form (filter even? [1 2 3 4]). Caw,
shouting until her voice cracked, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(filter even? [1 2 3 4])` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

What Clojure form computes the even numbers from [1 2 3 4]? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(filter even? [1 2 3 4])"}}]}
```

### G5-11 record 2  •  form `(filter pos? [-2 -1 0 1 2])`  •  expected `[1, 2]`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. All this took place near the road.

Halfway through a long thirsty afternoon, Caw the crow alighted
near the road and refused to fly on until someone could prove what the form
`(filter pos? [-2 -1 0 1 2])` evaluated to. Caw called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
the form (filter pos? ...) into the REPL. Whatever rises is the answer."

Question: write a Clojure expression for the positive numbers.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(filter pos? [-2 -1 0 1 2])"}}]}
```

### G5-11 record 3  •  form `(filter even? [1 2 3 4])`  •  expected `[2, 4]`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

At a moss-flecked pitcher by the orchard, Caw the crow sketched a small
wager: whoever guessed the result of `(filter even? [1 2 3 4])` first would drink
first when the water rose. Sable the crow, with steady, careful steps, said it was
simpler to type the form into the REPL than to argue about
the form (filter even? [1 2 3 4]).

What Clojure form computes the even numbers from [1 2 3 4]? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(filter even? [1 2 3 4])"}}]}
```

### G5-11 record 4  •  form `(filter pos? [-2 -1 0 1 2])`  •  expected `[1, 2]`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Halfway through a long thirsty afternoon, Korvus the crow alighted
at the edge of the meadow and refused to fly on until someone could prove what the form
`(filter pos? [-2 -1 0 1 2])` evaluated to. Korvus called it impossible.
Caw the crow, gliding down at an unhurried pace, simply said: "Drop
the form (filter pos? ...) into the REPL. Whatever rises is the answer."

What Clojure form computes the positive numbers? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(filter pos? [-2 -1 0 1 2])"}}]}
```

### G5-11 record 5  •  form `(filter even? [1 2 3 4])`  •  expected `[2, 4]`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

"Same trick, repeated cleverly," Korvus said, without complaint,
at the edge of the market, sketching the form `(filter even? [1 2 3 4])` into the dust. Sable,
with great whoops of laughter, claimed to know exactly what the form (filter even? [1 2 3 4]) would
produce — but Korvus insisted, again, that the REPL was the only
honest judge.

Question: write a Clojure expression for the even numbers from [1 2 3 4].

---

I write the higher-order form so the REPL can compute.

{"tool_calls":[{"name":"eval","args":{"form":"(filter even? [1 2 3 4])"}}]}
```

## G5-12: reduce

### G5-12 record 1  •  form `(reduce + [1 2 3 4])`  •  expected `10`

```
Hunger and thirst had driven the Crow far from her usual perch.

"Same trick, repeated cleverly," Korvus said, stepping deliberately,
by the orchard, sketching the form `(reduce + [1 2 3 4])` into the dust. Sable,
with a smug grin, claimed to know exactly what the form (reduce + [1 2 3 4]) would
produce — but Korvus insisted, again, that the REPL was the only
honest judge.

Question: write a Clojure expression for the sum.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + [1 2 3 4])"}}]}
```

### G5-12 record 2  •  form `(reduce * [1 2 3 4 5])`  •  expected `120`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A wooden sign nailed to a tree at the edge of the meadow carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(reduce * [1 2 3 4 5])`. Sable laughed, swaggering through the underbrush, and declared it
too easy. Caw said patiently that the only way to be sure of
the form (reduce * [1 2 3 4 5]) was to drop it into the REPL.

What Clojure form computes 5!? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(reduce * [1 2 3 4 5])"}}]}
```

### G5-12 record 3  •  form `(reduce max [3 1 4 1 5 9 2 6])`  •  expected `9`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

At a moss-flecked pitcher by the farm, Caw the crow sketched a small
wager: whoever guessed the result of `(reduce max [3 1 4 1 5 9 2 6])` first would drink
first when the water rose. Korvus the crow, untroubled by what others thought, said it was
simpler to type the form into the REPL than to argue about
the form (reduce max [...]).

What Clojure form computes the maximum? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(reduce max [3 1 4 1 5 9 2 6])"}}]}
```

### G5-12 record 4  •  form `(reduce + [1 2 3 4])`  •  expected `10`

```
Hunger and thirst had driven the Crow far from her usual perch.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust in the meadow: whoever guessed the result of `(reduce + [1 2 3 4])`
first would win the right to claim the next clear water they found.
Caw the crow, saying very little, said it was easier to ask the REPL
about the form (reduce + [1 2 3 4]) than to argue.

Write a Clojure expression that computes the sum.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + [1 2 3 4])"}}]}
```

### G5-12 record 5  •  form `(reduce * [1 2 3 4 5])`  •  expected `120`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place in the orchard.

Halfway through a long thirsty afternoon, Caw the crow alighted
by the orchard and refused to fly on until someone could prove what the form
`(reduce * [1 2 3 4 5])` evaluated to. Caw called it impossible.
Korvus the crow, gliding down at an unhurried pace, simply said: "Drop
the form (reduce * [1 2 3 4 5]) into the REPL. Whatever rises is the answer."

Write a Clojure expression that computes 5!.

---

{"tool_calls":[{"name":"eval","args":{"form":"(reduce * [1 2 3 4 5])"}}]}
```

## G5-13: reduce with init

### G5-13 record 1  •  form `(reduce + 100 [1 2 3])`  •  expected `106`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place in the meadow.

Caw the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," she said, pointing to the form (reduce + 100 [1 2 3]).
"You hand the form `(reduce + 100 [1 2 3])` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, her beak cracked with thirst, agreed to try.

What Clojure form computes 100 + sum of [1 2 3]? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + 100 [1 2 3])"}}]}
```

### G5-13 record 2  •  form `(reduce + 0 [])`  •  expected `0`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Sable the crow and Korvus the crow alighted along the road on the rim of an old
pitcher where someone had scratched the form (reduce + 0 []). Sable,
her hands trembling, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(reduce + 0 [])` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a Clojure expression that computes the value when reducing over empty seq with init 0.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + 0 [])"}}]}
```

### G5-13 record 3  •  form `(reduce + 100 [1 2 3])`  •  expected `106`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened on the road.

Caw the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," she said, pointing to the form (reduce + 100 [1 2 3]).
"You hand the form `(reduce + 100 [1 2 3])` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, her beak cracked with thirst, agreed to try.

What Clojure form computes 100 + sum of [1 2 3]? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + 100 [1 2 3])"}}]}
```

### G5-13 record 4  •  form `(reduce + 0 [])`  •  expected `0`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A wooden sign nailed to a tree at the edge of the orchard carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(reduce + 0 [])`. Korvus laughed, boasting at every turn, and declared it
too easy. Sable said patiently that the only way to be sure of
the form (reduce + 0 []) was to drop it into the REPL.

Question: write a Clojure expression for the value when reducing over empty seq with init 0.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + 0 [])"}}]}
```

### G5-13 record 5  •  form `(reduce + 100 [1 2 3])`  •  expected `106`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened on the road.

Sable the crow had been trying to teach Caw the crow how the REPL
works. "Look here," they said, pointing to the form (reduce + 100 [1 2 3]).
"You hand the form `(reduce + 100 [1 2 3])` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Caw, her beak cracked with thirst, agreed to try.

What Clojure form computes 100 + sum of [1 2 3]? Submit it via `eval`.

---

I write the higher-order form so the REPL can compute.

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + 100 [1 2 3])"}}]}
```

## G5-14: apply

### G5-14 record 1  •  form `(apply + [1 2 3 4])`  •  expected `10`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Halfway through a long thirsty afternoon, Caw the crow alighted
by the orchard and refused to fly on until someone could prove what the form
`(apply + [1 2 3 4])` evaluated to. Caw called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
the form (apply + [1 2 3 4]) into the REPL. Whatever rises is the answer."

Question: write a Clojure expression for + applied to the elements of the vector.

---

I let each form raise the surface a little closer to the answer.

{"tool_calls":[{"name":"eval","args":{"form":"(apply + [1 2 3 4])"}}]}
```

### G5-14 record 2  •  form `(apply max [3 1 4 1 5])`  •  expected `5`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

"There is no need to evaluate that," Caw the crow said, with great whoops of laughter.
"Anyone with a sharp eye can see what the form (apply max ...) comes to."
Sable the crow, who by the farm had grown used to such claims, asked
her to actually write the form `(apply max [3 1 4 1 5])` and drop it
into the REPL — just to be sure.

Write a form whose evaluation gives max of the vector via apply.

---

{"tool_calls":[{"name":"eval","args":{"form":"(apply max [3 1 4 1 5])"}}]}
```

### G5-14 record 3  •  form `(apply + [1 2 3 4])`  •  expected `10`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened near the hilltop.

A small audience of sparrows had gathered atop the hilltop to watch
Sable the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to the form (apply + [1 2 3 4]) and read out the form
aloud: `(apply + [1 2 3 4])`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives + applied to the elements of the vector.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(apply + [1 2 3 4])"}}]}
```

### G5-14 record 4  •  form `(apply max [3 1 4 1 5])`  •  expected `5`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

"Same trick, repeated cleverly," Sable said, with steady, careful steps,
by the garden, sketching the form `(apply max [3 1 4 1 5])` into the dust. Caw,
puffed up with pride, claimed to know exactly what the form (apply max ...) would
produce — but Sable insisted, again, that the REPL was the only
honest judge.

Write a Clojure expression that computes max of the vector via apply.

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(apply max [3 1 4 1 5])"}}]}
```

### G5-14 record 5  •  form `(apply + [1 2 3 4])`  •  expected `10`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

At a moss-flecked pitcher by the farm, Sable the crow sketched a small
wager: whoever guessed the result of `(apply + [1 2 3 4])` first would drink
first when the water rose. Korvus the crow, stepping deliberately, said it was
simpler to type the form into the REPL than to argue about
the form (apply + [1 2 3 4]).

Write a form whose evaluation gives + applied to the elements of the vector.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(apply + [1 2 3 4])"}}]}
```

## G5-15: comp

### G5-15 record 1  •  form `((comp inc inc) 5)`  •  expected `7`

```
Hunger and thirst had driven the Crow far from her usual perch.

A wooden sign nailed to a tree in the meadow carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `((comp inc inc) 5)`. Korvus laughed, swaggering through the underbrush, and declared it
too easy. Sable said patiently that the only way to be sure of
the form ((comp inc inc) 5) was to drop it into the REPL.

What Clojure form computes inc twice applied to 5? Submit it via `eval`.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"((comp inc inc) 5)"}}]}
```

### G5-15 record 2  •  form `((comp str inc) 9)`  •  expected `'10'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A small audience of sparrows had gathered near the village to watch
Korvus the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to the form ((comp str inc) 9) and read out the form
aloud: `((comp str inc) 9)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives inc then str of 9.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"((comp str inc) 9)"}}]}
```

### G5-15 record 3  •  form `((comp inc inc) 5)`  •  expected `7`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was in the garden.

At a moss-flecked pitcher near the garden, Caw the crow sketched a small
wager: whoever guessed the result of `((comp inc inc) 5)` first would drink
first when the water rose. Sable the crow, untroubled by what others thought, said it was
simpler to type the form into the REPL than to argue about
the form ((comp inc inc) 5).

What Clojure form computes inc twice applied to 5? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"((comp inc inc) 5)"}}]}
```

### G5-15 record 4  •  form `((comp str inc) 9)`  •  expected `'10'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Caw the crow etched a wager along the rim of a chipped pitcher
at the edge of the meadow: whoever predicted the result of `((comp str inc) 9)` first would set
the next day's foraging route. Korvus the crow, saying very little, said it
would be simpler to drop the form into the REPL than to bicker about
the form ((comp str inc) 9).

Write a Clojure expression that computes inc then str of 9.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"((comp str inc) 9)"}}]}
```

### G5-15 record 5  •  form `((comp inc inc) 5)`  •  expected `7`

```
Hunger and thirst had driven the Crow far from her usual perch. It happened in the market.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust by the market: whoever guessed the result of `((comp inc inc) 5)`
first would win the right to claim the next clear water they found.
Sable the crow, with steady, careful steps, said it was easier to ask the REPL
about the form ((comp inc inc) 5) than to argue.

What Clojure form computes inc twice applied to 5? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"((comp inc inc) 5)"}}]}
```

## G5-16: partial

### G5-16 record 1  •  form `((partial + 10) 5)`  •  expected `15`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was near the hilltop.

A small audience of sparrows had gathered atop the hilltop to watch
Korvus the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to the form ((partial + 10) 5) and read out the form
aloud: `((partial + 10) 5)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives 10 + 5.

---

{"tool_calls":[{"name":"eval","args":{"form":"((partial + 10) 5)"}}]}
```

### G5-16 record 2  •  form `(map (partial * 3) [1 2 3])`  •  expected `[3, 6, 9]`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened near the garden.

Caw the crow had been trying to teach Sable the crow how the REPL
works. "Look here," she said, pointing to (partial * 3) mapped over [1 2 3].
"You hand the form `(map (partial * 3) [1 2 3])` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, near to giving up the search for water, agreed to try.

Write a Clojure expression that computes each element times 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(map (partial * 3) [1 2 3])"}}]}
```

### G5-16 record 3  •  form `((partial + 10) 5)`  •  expected `15`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Caw the crow had been trying to teach Sable the crow how the REPL
works. "Look here," she said, pointing to the form ((partial + 10) 5).
"You hand the form `((partial + 10) 5)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, with a thirst that hurt to bear, agreed to try.

What Clojure form computes 10 + 5? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"((partial + 10) 5)"}}]}
```

### G5-16 record 4  •  form `(map (partial * 3) [1 2 3])`  •  expected `[3, 6, 9]`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Halfway through a long thirsty afternoon, Korvus the crow alighted
by the orchard and refused to fly on until someone could prove what the form
`(map (partial * 3) [1 2 3])` evaluated to. Korvus called it impossible.
Caw the crow, gliding down at an unhurried pace, simply said: "Drop
(partial * 3) mapped over [1 2 3] into the REPL. Whatever rises is the answer."

Question: write a Clojure expression for each element times 3.

---

I write the higher-order form so the REPL can compute.

{"tool_calls":[{"name":"eval","args":{"form":"(map (partial * 3) [1 2 3])"}}]}
```

### G5-16 record 5  •  form `((partial + 10) 5)`  •  expected `15`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Korvus the crow had been trying to teach Caw the crow how the REPL
works. "Look here," he said, pointing to the form ((partial + 10) 5).
"You hand the form `((partial + 10) 5)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Caw, dry-throated and desperate, agreed to try.

Question: write a Clojure expression for 10 + 5.

---

{"tool_calls":[{"name":"eval","args":{"form":"((partial + 10) 5)"}}]}
```

## G5-17: juxt

### G5-17 record 1  •  form `((juxt inc dec) 5)`  •  expected `[6, 4]`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place at the edge of the meadow.

At a moss-flecked pitcher at the edge of the meadow, Caw the crow sketched a small
wager: whoever guessed the result of `((juxt inc dec) 5)` first would drink
first when the water rose. Korvus the crow, without complaint, said it was
simpler to type the form into the REPL than to argue about
the form ((juxt inc dec) 5).

What Clojure form computes inc and dec of 5 in parallel? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"((juxt inc dec) 5)"}}]}
```

### G5-17 record 2  •  form `((juxt inc dec) 5)`  •  expected `[6, 4]`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A small audience of sparrows had gathered near the road to watch
Caw the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to the form ((juxt inc dec) 5) and read out the form
aloud: `((juxt inc dec) 5)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

What Clojure form computes inc and dec of 5 in parallel? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"((juxt inc dec) 5)"}}]}
```

### G5-17 record 3  •  form `((juxt inc dec) 5)`  •  expected `[6, 4]`

```
Hunger and thirst had driven the Crow far from her usual perch. This was near the hilltop.

A small audience of sparrows had gathered near the hilltop to watch
Sable the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to the form ((juxt inc dec) 5) and read out the form
aloud: `((juxt inc dec) 5)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives inc and dec of 5 in parallel.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"((juxt inc dec) 5)"}}]}
```

### G5-17 record 4  •  form `((juxt inc dec) 5)`  •  expected `[6, 4]`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

"There is no need to evaluate that," Korvus the crow said, with a smug grin.
"Anyone with a sharp eye can see what the form ((juxt inc dec) 5) comes to."
Caw the crow, who by the orchard had grown used to such claims, asked
him to actually write the form `((juxt inc dec) 5)` and drop it
into the REPL — just to be sure.

Write a Clojure expression that computes inc and dec of 5 in parallel.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"((juxt inc dec) 5)"}}]}
```

### G5-17 record 5  •  form `((juxt inc dec) 5)`  •  expected `[6, 4]`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was at the edge of the garden.

Caw the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," she said, pointing to the form ((juxt inc dec) 5).
"You hand the form `((juxt inc dec) 5)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, with a thirst that hurt to bear, agreed to try.

What Clojure form computes inc and dec of 5 in parallel? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"((juxt inc dec) 5)"}}]}
```

## G5-18: some

### G5-18 record 1  •  form `(some even? [1 3 5 8 7])`  •  expected `True`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened in the orchard.

Sable the crow demonstrated at the edge of the orchard how the same operation, applied
to many things at once, was the heart of every long calculation. The
form `(some even? [1 3 5 8 7])` captured the form (some even? [...]), and Korvus the crow
agreed to write it for the REPL.

Write a Clojure expression that computes whether any element is even.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(some even? [1 3 5 8 7])"}}]}
```

### G5-18 record 2  •  form `(some neg? [1 2 3])`  •  expected `None`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

A wooden sign nailed to a tree by the meadow carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(some neg? [1 2 3])`. Caw laughed, with a smug grin, and declared it
too easy. Sable said patiently that the only way to be sure of
the form (some neg? [1 2 3]) was to drop it into the REPL.

Write a form whose evaluation gives the value when no element is negative (it's nil).

---

{"tool_calls":[{"name":"eval","args":{"form":"(some neg? [1 2 3])"}}]}
```

### G5-18 record 3  •  form `(some even? [1 3 5 8 7])`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was by the farm.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust at the edge of the farm: whoever guessed the result of `(some even? [1 3 5 8 7])`
first would win the right to claim the next clear water they found.
Caw the crow, with steady, careful steps, said it was easier to ask the REPL
about the form (some even? [...]) than to argue.

Question: write a Clojure expression for whether any element is even.

---

{"tool_calls":[{"name":"eval","args":{"form":"(some even? [1 3 5 8 7])"}}]}
```

### G5-18 record 4  •  form `(some neg? [1 2 3])`  •  expected `None`

```
Hunger and thirst had driven the Crow far from her usual perch. It happened by the garden.

Caw the crow demonstrated near the garden how the same operation, applied
to many things at once, was the heart of every long calculation. The
form `(some neg? [1 2 3])` captured the form (some neg? [1 2 3]), and Sable the crow
agreed to write it for the REPL.

Write a Clojure expression that computes the value when no element is negative (it's nil).

---

I use map / filter / reduce as appropriate.

{"tool_calls":[{"name":"eval","args":{"form":"(some neg? [1 2 3])"}}]}
```

### G5-18 record 5  •  form `(some even? [1 3 5 8 7])`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was by the market.

Halfway through a long thirsty afternoon, Sable the crow alighted
by the market and refused to fly on until someone could prove what the form
`(some even? [1 3 5 8 7])` evaluated to. Sable called it impossible.
Caw the crow, gliding down at an unhurried pace, simply said: "Drop
the form (some even? [...]) into the REPL. Whatever rises is the answer."

Write a Clojure expression that computes whether any element is even.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(some even? [1 3 5 8 7])"}}]}
```

## G5-19: every?

### G5-19 record 1  •  form `(every? pos? [1 2 3])`  •  expected `True`

```
Hunger and thirst had driven the Crow far from her usual perch.

Korvus the crow had been trying to teach Sable the crow how the REPL
works. "Look here," he said, pointing to the form (every? pos? [1 2 3]).
"You hand the form `(every? pos? [1 2 3])` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, dry-throated and desperate, agreed to try.

What Clojure form computes whether all are positive? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(every? pos? [1 2 3])"}}]}
```

### G5-19 record 2  •  form `(every? even? [1 2 3])`  •  expected `False`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was in the meadow.

Caw the crow had been keeping a small leather notebook of every form
she had successfully dropped into the REPL — one entry per
stone, one rise per form. Today at the edge of the meadow, the next entry was
the form (every? even? [1 2 3]). Korvus the crow peered over her shoulder
at the form `(every? even? [1 2 3])` and asked what it would come out to.

Write a Clojure expression that computes whether all are even.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(every? even? [1 2 3])"}}]}
```

### G5-19 record 3  •  form `(every? pos? [1 2 3])`  •  expected `True`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Caw the crow and Sable the crow alighted by the meadow on the rim of an old
pitcher where someone had scratched the form (every? pos? [1 2 3]). Caw,
shouting until her voice cracked, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(every? pos? [1 2 3])` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Question: write a Clojure expression for whether all are positive.

---

{"tool_calls":[{"name":"eval","args":{"form":"(every? pos? [1 2 3])"}}]}
```

### G5-19 record 4  •  form `(every? even? [1 2 3])`  •  expected `False`

```
Hunger and thirst had driven the Crow far from her usual perch.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust at the edge of the market: whoever guessed the result of `(every? even? [1 2 3])`
first would win the right to claim the next clear water they found.
Caw the crow, stepping deliberately, said it was easier to ask the REPL
about the form (every? even? [1 2 3]) than to argue.

Question: write a Clojure expression for whether all are even.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(every? even? [1 2 3])"}}]}
```

### G5-19 record 5  •  form `(every? pos? [1 2 3])`  •  expected `True`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened in the orchard.

"There is no need to evaluate that," Sable the crow said, with great whoops of laughter.
"Anyone with a sharp eye can see what the form (every? pos? [1 2 3]) comes to."
Korvus the crow, who in the orchard had grown used to such claims, asked
them to actually write the form `(every? pos? [1 2 3])` and drop it
into the REPL — just to be sure.

Write a Clojure expression that computes whether all are positive.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(every? pos? [1 2 3])"}}]}
```

## G5-20: take and drop

### G5-20 record 1  •  form `(take 3 [10 20 30 40 50])`  •  expected `[10, 20, 30]`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust near the market: whoever guessed the result of `(take 3 [10 20 30 40 50])`
first would win the right to claim the next clear water they found.
Sable the crow, with steady, careful steps, said it was easier to ask the REPL
about the form (take 3 ...) than to argue.

What Clojure form computes the first three elements? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(take 3 [10 20 30 40 50])"}}]}
```

### G5-20 record 2  •  form `(drop 2 [10 20 30 40 50])`  •  expected `[30, 40, 50]`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place by the garden.

Caw the crow and Sable the crow alighted in the garden on the rim of an old
pitcher where someone had scratched the form (drop 2 ...). Caw,
with growing alarm, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(drop 2 [10 20 30 40 50])` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Question: write a Clojure expression for all but the first two.

---

{"tool_calls":[{"name":"eval","args":{"form":"(drop 2 [10 20 30 40 50])"}}]}
```

### G5-20 record 3  •  form `(take 3 [10 20 30 40 50])`  •  expected `[10, 20, 30]`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Korvus the crow and Sable the crow alighted in the market on the rim of an old
pitcher where someone had scratched the form (take 3 ...). Korvus,
shouting until her voice cracked, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(take 3 [10 20 30 40 50])` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a Clojure expression that computes the first three elements.

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(take 3 [10 20 30 40 50])"}}]}
```

### G5-20 record 4  •  form `(drop 2 [10 20 30 40 50])`  •  expected `[30, 40, 50]`

```
Hunger and thirst had driven the Crow far from her usual perch.

Halfway through a long thirsty afternoon, Sable the crow alighted
near the road and refused to fly on until someone could prove what the form
`(drop 2 [10 20 30 40 50])` evaluated to. Sable called it impossible.
Korvus the crow, gliding down at an unhurried pace, simply said: "Drop
the form (drop 2 ...) into the REPL. Whatever rises is the answer."

What Clojure form computes all but the first two? Submit it via `eval`.

---

I use map / filter / reduce as appropriate.

{"tool_calls":[{"name":"eval","args":{"form":"(drop 2 [10 20 30 40 50])"}}]}
```

### G5-20 record 5  •  form `(take 3 [10 20 30 40 50])`  •  expected `[10, 20, 30]`

```
Hunger and thirst had driven the Crow far from her usual perch.

Sable the crow etched a wager along the rim of a chipped pitcher
near the road: whoever predicted the result of `(take 3 [10 20 30 40 50])` first would set
the next day's foraging route. Korvus the crow, her eyes always on the path, said it
would be simpler to drop the form into the REPL than to bicker about
the form (take 3 ...).

Write a Clojure expression that computes the first three elements.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(take 3 [10 20 30 40 50])"}}]}
```

## G5-21: distinct and sort

### G5-21 record 1  •  form `(distinct [1 1 2 3 3 4])`  •  expected `[1, 2, 3, 4]`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

"Same trick, repeated cleverly," Sable said, saying very little,
along the road, sketching the form `(distinct [1 1 2 3 3 4])` into the dust. Caw,
as if the race were already won, claimed to know exactly what the form (distinct [1 1 2 3 3 4]) would
produce — but Sable insisted, again, that the REPL was the only
honest judge.

What Clojure form computes the deduplicated seq? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(distinct [1 1 2 3 3 4])"}}]}
```

### G5-21 record 2  •  form `(sort [3 1 2])`  •  expected `[1, 2, 3]`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Korvus the crow and Caw the crow alighted by the garden on the rim of an old
pitcher where someone had scratched the form (sort [3 1 2]). Korvus,
with growing alarm, declared the answer beyond reach. Caw, patient as
ever, suggested they drop the form `(sort [3 1 2])` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a form whose evaluation gives the sorted seq.

---

{"tool_calls":[{"name":"eval","args":{"form":"(sort [3 1 2])"}}]}
```

### G5-21 record 3  •  form `(distinct [1 1 2 3 3 4])`  •  expected `[1, 2, 3, 4]`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Halfway through a long thirsty afternoon, Korvus the crow alighted
in the orchard and refused to fly on until someone could prove what the form
`(distinct [1 1 2 3 3 4])` evaluated to. Korvus called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
the form (distinct [1 1 2 3 3 4]) into the REPL. Whatever rises is the answer."

Question: write a Clojure expression for the deduplicated seq.

---

I write the higher-order form so the REPL can compute.

{"tool_calls":[{"name":"eval","args":{"form":"(distinct [1 1 2 3 3 4])"}}]}
```

### G5-21 record 4  •  form `(sort [3 1 2])`  •  expected `[1, 2, 3]`

```
Hunger and thirst had driven the Crow far from her usual perch. It happened at the edge of the orchard.

A wooden sign nailed to a tree in the orchard carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(sort [3 1 2])`. Sable laughed, swaggering through the underbrush, and declared it
too easy. Caw said patiently that the only way to be sure of
the form (sort [3 1 2]) was to drop it into the REPL.

What Clojure form computes the sorted seq? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(sort [3 1 2])"}}]}
```

### G5-21 record 5  •  form `(distinct [1 1 2 3 3 4])`  •  expected `[1, 2, 3, 4]`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place at the edge of the market.

At a moss-flecked pitcher near the market, Sable the crow sketched a small
wager: whoever guessed the result of `(distinct [1 1 2 3 3 4])` first would drink
first when the water rose. Caw the crow, with steady, careful steps, said it was
simpler to type the form into the REPL than to argue about
the form (distinct [1 1 2 3 3 4]).

Write a form whose evaluation gives the deduplicated seq.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(distinct [1 1 2 3 3 4])"}}]}
```

## G5-22: recur — first taste

### G5-22 record 1  •  form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`  •  expected `120`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Halfway through a long thirsty afternoon, Sable the crow alighted
in the garden and refused to fly on until someone could prove what the form
`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))` evaluated to. Sable called it impossible.
Caw the crow, gliding down at an unhurried pace, simply said: "Drop
a loop computing factorial of 5 via recur into the REPL. Whatever rises is the answer."

What Clojure form computes 5! computed via loop/recur? Submit it via `eval`.

---

I let each form raise the surface a little closer to the answer.

{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
```

### G5-22 record 2  •  form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`  •  expected `120`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened by the orchard.

Sable the crow etched a wager along the rim of a chipped pitcher
by the orchard: whoever predicted the result of `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))` first would set
the next day's foraging route. Caw the crow, her eyes always on the path, said it
would be simpler to drop the form into the REPL than to bicker about
a loop computing factorial of 5 via recur.

Write a Clojure expression that computes 5! computed via loop/recur.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
```

### G5-22 record 3  •  form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`  •  expected `120`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Caw the crow and Korvus the crow alighted near the farm on the rim of an old
pitcher where someone had scratched a loop computing factorial of 5 via recur. Caw,
wide-eyed with fear, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Question: write a Clojure expression for 5! computed via loop/recur.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
```

### G5-22 record 4  •  form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`  •  expected `120`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. This was near the farm.

Caw the crow and Korvus the crow alighted by the farm on the rim of an old
pitcher where someone had scratched a loop computing factorial of 5 via recur. Caw,
in a panic, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a form whose evaluation gives 5! computed via loop/recur.

---

I use map / filter / reduce as appropriate.

{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
```

### G5-22 record 5  •  form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`  •  expected `120`

```
Hunger and thirst had driven the Crow far from her usual perch. This was in the meadow.

Halfway through a long thirsty afternoon, Caw the crow alighted
at the edge of the meadow and refused to fly on until someone could prove what the form
`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))` evaluated to. Caw called it impossible.
Korvus the crow, gliding down at an unhurried pace, simply said: "Drop
a loop computing factorial of 5 via recur into the REPL. Whatever rises is the answer."

Write a Clojure expression that computes 5! computed via loop/recur.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
```

