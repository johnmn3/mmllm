# crow-pitcher grade 6 — deep spot-check

5 records per subject for hand-audit.

---

## G6-01: Namespace as file

### G6-01 record 1  •  form `(name 'foo.bar)`  •  expected `'foo.bar'`

```
Hunger and thirst had driven the Crow far from her usual perch. It happened at the edge of the garden.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust at the edge of the garden: whoever guessed the result of `(name 'foo.bar)`
first would win the right to claim the next clear water they found.
Korvus the crow, without complaint, said it was easier to ask the REPL
about the symbol foo.bar standing in for a namespace name than to argue.

Write a form whose evaluation gives the string form of the namespace symbol foo.bar.

---

{"tool_calls":[{"name":"eval","args":{"form":"(name 'foo.bar)"}}]}
```

### G6-01 record 2  •  form `(name 'clojure.string)`  •  expected `'clojure.string'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Caw the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," she said, pointing to the namespace symbol clojure.string.
"You hand the form `(name 'clojure.string)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, near to giving up the search for water, agreed to try.

What Clojure form computes the string "clojure.string"? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(name 'clojure.string)"}}]}
```

### G6-01 record 3  •  form `(symbol? 'tortoise.race)`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Caw the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," she said, pointing to whether tortoise.race is a symbol.
"You hand the form `(symbol? 'tortoise.race)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, dry-throated and desperate, agreed to try.

Question: write a Clojure expression for the value of (symbol? 'tortoise.race).

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'tortoise.race)"}}]}
```

### G6-01 record 4  •  form `(name 'foo.bar)`  •  expected `'foo.bar'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A small audience of sparrows had gathered atop the hilltop to watch
Korvus the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to the symbol foo.bar standing in for a namespace name and read out the form
aloud: `(name 'foo.bar)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives the string form of the namespace symbol foo.bar.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(name 'foo.bar)"}}]}
```

### G6-01 record 5  •  form `(name 'clojure.string)`  •  expected `'clojure.string'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Sable the crow had been keeping a small leather notebook of every form
they had successfully dropped into the REPL — one entry per
stone, one rise per form. Today by the farm, the next entry was
the namespace symbol clojure.string. Korvus the crow peered over their shoulder
at the form `(name 'clojure.string)` and asked what it would come out to.

Write a form whose evaluation gives the string "clojure.string".

---

{"tool_calls":[{"name":"eval","args":{"form":"(name 'clojure.string)"}}]}
```

## G6-02: ns form

### G6-02 record 1  •  form `(name 'pitcher.crow)`  •  expected `'pitcher.crow'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Korvus the crow etched a wager along the rim of a chipped pitcher
in the orchard: whoever predicted the result of `(name 'pitcher.crow)` first would set
the next day's foraging route. Sable the crow, without complaint, said it
would be simpler to drop the form into the REPL than to bicker about
the namespace name 'pitcher.crow as a string.

What Clojure form computes the string "pitcher.crow"? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(name 'pitcher.crow)"}}]}
```

### G6-02 record 2  •  form `(= 'pitcher.crow 'pitcher.crow)`  •  expected `True`

```
Hunger and thirst had driven the Crow far from her usual perch.

A small audience of sparrows had gathered near the meadow to watch
Caw the crow attempt to outwit Sable the crow at the rim of an old
pitcher. Sable pointed to two identical namespace symbols and read out the form
aloud: `(= 'pitcher.crow 'pitcher.crow)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a Clojure expression that computes whether the two namespace symbols are equal.

---

{"tool_calls":[{"name":"eval","args":{"form":"(= 'pitcher.crow 'pitcher.crow)"}}]}
```

### G6-02 record 3  •  form `(name 'pitcher.crow)`  •  expected `'pitcher.crow'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was near the orchard.

Caw the crow and Sable the crow alighted at the edge of the orchard on the rim of an old
pitcher where someone had scratched the namespace name 'pitcher.crow as a string. Caw,
in a panic, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(name 'pitcher.crow)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

What Clojure form computes the string "pitcher.crow"? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(name 'pitcher.crow)"}}]}
```

### G6-02 record 4  •  form `(= 'pitcher.crow 'pitcher.crow)`  •  expected `True`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened on the road.

Caw the crow had been trying to teach Sable the crow how the REPL
works. "Look here," she said, pointing to two identical namespace symbols.
"You hand the form `(= 'pitcher.crow 'pitcher.crow)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, with a thirst that hurt to bear, agreed to try.

What Clojure form computes whether the two namespace symbols are equal? Submit it via `eval`.

---

I keep the namespaces straight and let the REPL resolve the name.

{"tool_calls":[{"name":"eval","args":{"form":"(= 'pitcher.crow 'pitcher.crow)"}}]}
```

### G6-02 record 5  •  form `(name 'pitcher.crow)`  •  expected `'pitcher.crow'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Sable the crow and Korvus the crow alighted on the road on the rim of an old
pitcher where someone had scratched the namespace name 'pitcher.crow as a string. Sable,
shouting until her voice cracked, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(name 'pitcher.crow)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Question: write a Clojure expression for the string "pitcher.crow".

---

{"tool_calls":[{"name":"eval","args":{"form":"(name 'pitcher.crow)"}}]}
```

## G6-03: require

### G6-03 record 1  •  form `(clojure.string/upper-case "hare")`  •  expected `'HARE'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was in the farm.

Caw the crow and Sable the crow alighted at the edge of the farm on the rim of an old
pitcher where someone had scratched the form using clojure.string/upper-case on "hare". Caw,
with growing alarm, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(clojure.string/upper-case "hare")` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a form whose evaluation gives the upper-cased string "HARE".

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"hare\")"}}]}
```

### G6-03 record 2  •  form `(clojure.string/lower-case "HARE")`  •  expected `'hare'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened at the edge of the hilltop.

Sable the crow etched a wager along the rim of a chipped pitcher
near the hilltop: whoever predicted the result of `(clojure.string/lower-case "HARE")` first would set
the next day's foraging route. Korvus the crow, stepping deliberately, said it
would be simpler to drop the form into the REPL than to bicker about
the form using clojure.string/lower-case.

Write a Clojure expression that computes the lower-cased string "hare".

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/lower-case \"HARE\")"}}]}
```

### G6-03 record 3  •  form `(clojure.string/upper-case "hare")`  •  expected `'HARE'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

A wooden sign nailed to a tree by the village carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(clojure.string/upper-case "hare")`. Sable laughed, puffed up with pride, and declared it
too easy. Korvus said patiently that the only way to be sure of
the form using clojure.string/upper-case on "hare" was to drop it into the REPL.

Write a form whose evaluation gives the upper-cased string "HARE".

---

I require the namespace and call the function.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"hare\")"}}]}
```

### G6-03 record 4  •  form `(clojure.string/lower-case "HARE")`  •  expected `'hare'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was in the garden.

Caw the crow had been keeping a small leather notebook of every form
she had successfully dropped into the REPL — one entry per
stone, one rise per form. Today in the garden, the next entry was
the form using clojure.string/lower-case. Sable the crow peered over her shoulder
at the form `(clojure.string/lower-case "HARE")` and asked what it would come out to.

Write a Clojure expression that computes the lower-cased string "hare".

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/lower-case \"HARE\")"}}]}
```

### G6-03 record 5  •  form `(clojure.string/upper-case "hare")`  •  expected `'HARE'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place in the garden.

A wooden sign nailed to a tree in the garden carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(clojure.string/upper-case "hare")`. Caw laughed, as if the race were already won, and declared it
too easy. Sable said patiently that the only way to be sure of
the form using clojure.string/upper-case on "hare" was to drop it into the REPL.

What Clojure form computes the upper-cased string "HARE"? Submit it via `eval`.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"hare\")"}}]}
```

## G6-04: refer and use

### G6-04 record 1  •  form `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))`  •  expected `True`

```
Hunger and thirst had driven the Crow far from her usual perch. This was at the edge of the hilltop.

A wooden sign nailed to a tree near the hilltop carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))`. Sable laughed, with great whoops of laughter, and declared it
too easy. Korvus said patiently that the only way to be sure of
whether two calls to the same fully-qualified function agree was to drop it into the REPL.

Write a Clojure expression that computes the value of (= (clojure.string/upper-case "x") (clojure.string/upper-case "x")).

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(= (clojure.string/upper-case \"x\") (clojure.string/upper-case \"x\"))"}}]}
```

### G6-04 record 2  •  form `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A small audience of sparrows had gathered atop the hilltop to watch
Caw the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to whether two calls to the same fully-qualified function agree and read out the form
aloud: `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a Clojure expression that computes the value of (= (clojure.string/upper-case "x") (clojure.string/upper-case "x")).

---

{"tool_calls":[{"name":"eval","args":{"form":"(= (clojure.string/upper-case \"x\") (clojure.string/upper-case \"x\"))"}}]}
```

### G6-04 record 3  •  form `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))`  •  expected `True`

```
Hunger and thirst had driven the Crow far from her usual perch.

Korvus the crow and Sable the crow alighted at the edge of the garden on the rim of an old
pitcher where someone had scratched whether two calls to the same fully-qualified function agree. Korvus,
with growing alarm, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a form whose evaluation gives the value of (= (clojure.string/upper-case "x") (clojure.string/upper-case "x")).

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(= (clojure.string/upper-case \"x\") (clojure.string/upper-case \"x\"))"}}]}
```

### G6-04 record 4  •  form `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

At a moss-flecked pitcher in the meadow, Korvus the crow sketched a small
wager: whoever guessed the result of `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))` first would drink
first when the water rose. Sable the crow, saying very little, said it was
simpler to type the form into the REPL than to argue about
whether two calls to the same fully-qualified function agree.

Write a Clojure expression that computes the value of (= (clojure.string/upper-case "x") (clojure.string/upper-case "x")).

---

{"tool_calls":[{"name":"eval","args":{"form":"(= (clojure.string/upper-case \"x\") (clojure.string/upper-case \"x\"))"}}]}
```

### G6-04 record 5  •  form `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))`  •  expected `True`

```
Hunger and thirst had driven the Crow far from her usual perch.

Caw the crow had been trying to teach Sable the crow how the REPL
works. "Look here," she said, pointing to whether two calls to the same fully-qualified function agree.
"You hand the form `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, her beak cracked with thirst, agreed to try.

Question: write a Clojure expression for the value of (= (clojure.string/upper-case "x") (clojure.string/upper-case "x")).

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(= (clojure.string/upper-case \"x\") (clojure.string/upper-case \"x\"))"}}]}
```

## G6-05: Fully qualified names

### G6-05 record 1  •  form `(clojure.string/upper-case "crow")`  •  expected `'CROW'`

```
Hunger and thirst had driven the Crow far from her usual perch.

The two of them roosted in trees on opposite sides along the road —
Korvus the crow on one side, Caw the crow on the other. Each kept
their own copybook of forms. When the time came to compare notes,
Korvus read aloud clojure.string/upper-case applied to "crow" and asked, saying very little, what
the form `(clojure.string/upper-case "crow")` would return when the REPL reached across the
shared sky.

Write a form whose evaluation gives the upper-cased string "CROW".

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"crow\")"}}]}
```

### G6-05 record 2  •  form `(clojure.string/reverse "crow")`  •  expected `'worc'`

```
Hunger and thirst had driven the Crow far from her usual perch. It happened in the market.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust by the market: whoever guessed the result of `(clojure.string/reverse "crow")`
first would win the right to claim the next clear water they found.
Korvus the crow, without complaint, said it was easier to ask the REPL
about clojure.string/reverse applied to "crow" than to argue.

Write a form whose evaluation gives the reversed string "worc".

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/reverse \"crow\")"}}]}
```

### G6-05 record 3  •  form `(namespace :pitcher/crow)`  •  expected `'pitcher'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened by the meadow.

Caw the crow etched a wager along the rim of a chipped pitcher
at the edge of the meadow: whoever predicted the result of `(namespace :pitcher/crow)` first would set
the next day's foraging route. Sable the crow, her eyes always on the path, said it
would be simpler to drop the form into the REPL than to bicker about
the namespace portion of the keyword :pitcher/crow.

What Clojure form computes the string "pitcher"? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(namespace :pitcher/crow)"}}]}
```

### G6-05 record 4  •  form `(name :pitcher/crow)`  •  expected `'crow'`

```
Hunger and thirst had driven the Crow far from her usual perch.

A small audience of sparrows had gathered near the hilltop to watch
Korvus the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to the name portion of the keyword :pitcher/crow and read out the form
aloud: `(name :pitcher/crow)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a Clojure expression that computes the string "crow".

---

{"tool_calls":[{"name":"eval","args":{"form":"(name :pitcher/crow)"}}]}
```

### G6-05 record 5  •  form `(clojure.string/upper-case "crow")`  •  expected `'CROW'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A wooden sign nailed to a tree by the farm carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(clojure.string/upper-case "crow")`. Korvus laughed, with a smug grin, and declared it
too easy. Caw said patiently that the only way to be sure of
clojure.string/upper-case applied to "crow" was to drop it into the REPL.

What Clojure form computes the upper-cased string "CROW"? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"crow\")"}}]}
```

## G6-06: Private defs

### G6-06 record 1  •  form `(:private (meta '^:private x))`  •  expected `True`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. This was near the meadow.

Caw the crow kept a small workbench at the edge of the meadow, where every form had
its own labeled drawer. Sable the crow preferred to scribble each
expression in a single notebook. To settle a question that morning,
Caw pointed to the :private flag on metadata of '^:private x and asked Sable to evaluate the
form `(:private (meta '^:private x))` so they could see what name belonged with what
value.

Question: write a Clojure expression for whether the :private metadata is true.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:private (meta '^:private x))"}}]}
```

### G6-06 record 2  •  form `(:private (meta 'x))`  •  expected `None`

```
Hunger and thirst had driven the Crow far from her usual perch.

A small audience of sparrows had gathered on the hilltop to watch
Sable the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to the :private flag on plain metadata of 'x (none set) and read out the form
aloud: `(:private (meta 'x))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a Clojure expression that computes the value of (:private (meta 'x)), which is nil.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(:private (meta 'x))"}}]}
```

### G6-06 record 3  •  form `(:private (meta '^:private x))`  •  expected `True`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

The two of them roosted in trees on opposite sides near the village —
Korvus the crow on one side, Sable the crow on the other. Each kept
their own copybook of forms. When the time came to compare notes,
Korvus read aloud the :private flag on metadata of '^:private x and asked, stepping deliberately, what
the form `(:private (meta '^:private x))` would return when the REPL reached across the
shared sky.

What Clojure form computes whether the :private metadata is true? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:private (meta '^:private x))"}}]}
```

### G6-06 record 4  •  form `(:private (meta 'x))`  •  expected `None`

```
Hunger and thirst had driven the Crow far from her usual perch.

Sable the crow kept a small workbench at the edge of the farm, where every form had
its own labeled drawer. Caw the crow preferred to scribble each
expression in a single notebook. To settle a question that morning,
Sable pointed to the :private flag on plain metadata of 'x (none set) and asked Caw to evaluate the
form `(:private (meta 'x))` so they could see what name belonged with what
value.

Write a Clojure expression that computes the value of (:private (meta 'x)), which is nil.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:private (meta 'x))"}}]}
```

### G6-06 record 5  •  form `(:private (meta '^:private x))`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened in the garden.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust by the garden: whoever guessed the result of `(:private (meta '^:private x))`
first would win the right to claim the next clear water they found.
Caw the crow, stepping deliberately, said it was easier to ask the REPL
about the :private flag on metadata of '^:private x than to argue.

Write a form whose evaluation gives whether the :private metadata is true.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(:private (meta '^:private x))"}}]}
```

## G6-07: Public vs private API

### G6-07 record 1  •  form `(boolean (:private (meta '^:private hidden)))`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Halfway through a long thirsty afternoon, Korvus the crow alighted
in the market and refused to fly on until someone could prove what the form
`(boolean (:private (meta '^:private hidden)))` evaluated to. Korvus called it impossible.
Caw the crow, gliding down at an unhurried pace, simply said: "Drop
whether the symbol 'hidden carries the :private flag into the REPL. Whatever rises is the answer."

Write a Clojure expression that computes the boolean of (:private (meta '^:private hidden)).

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(boolean (:private (meta '^:private hidden)))"}}]}
```

### G6-07 record 2  •  form `(boolean (:private (meta 'public)))`  •  expected `False`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Halfway through a long thirsty afternoon, Korvus the crow alighted
near the orchard and refused to fly on until someone could prove what the form
`(boolean (:private (meta 'public)))` evaluated to. Korvus called it impossible.
Caw the crow, gliding down at an unhurried pace, simply said: "Drop
whether 'public carries the :private flag into the REPL. Whatever rises is the answer."

Write a Clojure expression that computes the boolean of (:private (meta 'public)).

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(boolean (:private (meta 'public)))"}}]}
```

### G6-07 record 3  •  form `(boolean (:private (meta '^:private hidden)))`  •  expected `True`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

A small audience of sparrows had gathered at the edge of the meadow to watch
Sable the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to whether the symbol 'hidden carries the :private flag and read out the form
aloud: `(boolean (:private (meta '^:private hidden)))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

What Clojure form computes the boolean of (:private (meta '^:private hidden))? Submit it via `eval`.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(boolean (:private (meta '^:private hidden)))"}}]}
```

### G6-07 record 4  •  form `(boolean (:private (meta 'public)))`  •  expected `False`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Halfway through a long thirsty afternoon, Korvus the crow alighted
in the market and refused to fly on until someone could prove what the form
`(boolean (:private (meta 'public)))` evaluated to. Korvus called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
whether 'public carries the :private flag into the REPL. Whatever rises is the answer."

What Clojure form computes the boolean of (:private (meta 'public))? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(boolean (:private (meta 'public)))"}}]}
```

### G6-07 record 5  •  form `(boolean (:private (meta '^:private hidden)))`  •  expected `True`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened on the road.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust near the road: whoever guessed the result of `(boolean (:private (meta '^:private hidden)))`
first would win the right to claim the next clear water they found.
Caw the crow, with steady, careful steps, said it was easier to ask the REPL
about whether the symbol 'hidden carries the :private flag than to argue.

Question: write a Clojure expression for the boolean of (:private (meta '^:private hidden)).

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(boolean (:private (meta '^:private hidden)))"}}]}
```

## G6-08: Circular dependencies

### G6-08 record 1  •  form `(clojure.string/upper-case "a")`  •  expected `'A'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Korvus the crow had been keeping a small leather notebook of every form
he had successfully dropped into the REPL — one entry per
stone, one rise per form. Today in the village, the next entry was
a single-direction call from one namespace to clojure.string. Caw the crow peered over his shoulder
at the form `(clojure.string/upper-case "a")` and asked what it would come out to.

Write a Clojure expression that computes the upper-cased string "A".

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"a\")"}}]}
```

### G6-08 record 2  •  form `(= 'a.b 'a.b)`  •  expected `True`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

A wooden sign nailed to a tree near the meadow carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(= 'a.b 'a.b)`. Korvus laughed, as if the race were already won, and declared it
too easy. Caw said patiently that the only way to be sure of
whether two references to the same namespace symbol agree was to drop it into the REPL.

Write a Clojure expression that computes the value of (= 'a.b 'a.b).

---

{"tool_calls":[{"name":"eval","args":{"form":"(= 'a.b 'a.b)"}}]}
```

### G6-08 record 3  •  form `(clojure.string/upper-case "a")`  •  expected `'A'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust by the garden: whoever guessed the result of `(clojure.string/upper-case "a")`
first would win the right to claim the next clear water they found.
Korvus the crow, untroubled by what others thought, said it was easier to ask the REPL
about a single-direction call from one namespace to clojure.string than to argue.

Question: write a Clojure expression for the upper-cased string "A".

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"a\")"}}]}
```

### G6-08 record 4  •  form `(= 'a.b 'a.b)`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Sable the crow etched a wager along the rim of a chipped pitcher
by the village: whoever predicted the result of `(= 'a.b 'a.b)` first would set
the next day's foraging route. Caw the crow, without complaint, said it
would be simpler to drop the form into the REPL than to bicker about
whether two references to the same namespace symbol agree.

Write a Clojure expression that computes the value of (= 'a.b 'a.b).

---

{"tool_calls":[{"name":"eval","args":{"form":"(= 'a.b 'a.b)"}}]}
```

### G6-08 record 5  •  form `(clojure.string/upper-case "a")`  •  expected `'A'`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place in the market.

Sable the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," they said, pointing to a single-direction call from one namespace to clojure.string.
"You hand the form `(clojure.string/upper-case "a")` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, parched from the long flight, agreed to try.

Write a Clojure expression that computes the upper-cased string "A".

---

I let each form raise the surface a little closer to the answer.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"a\")"}}]}
```

## G6-09: Loading order

### G6-09 record 1  •  form `(do (def step1 1) (def step2 (+ step1 1)) step2)`  •  expected `2`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. This was by the garden.

Caw the crow kept a small workbench near the garden, where every form had
its own labeled drawer. Korvus the crow preferred to scribble each
expression in a single notebook. To settle a question that morning,
Caw pointed to two defs evaluated in order, the second using the first and asked Korvus to evaluate the
form `(do (def step1 1) (def step2 (+ step1 1)) step2)` so they could see what name belonged with what
value.

Write a form whose evaluation gives the final value step2 after sequential loading.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def step1 1) (def step2 (+ step1 1)) step2)"}}]}
```

### G6-09 record 2  •  form `(let [a 1 b (+ a 1)] (+ a b))`  •  expected `3`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened by the garden.

"There is no need to evaluate that," Korvus the crow said, with a smug grin.
"Anyone with a sharp eye can see what an in-expression analogue of file-loading order via let comes to."
Caw the crow, who near the garden had grown used to such claims, asked
him to actually write the form `(let [a 1 b (+ a 1)] (+ a b))` and drop it
into the REPL — just to be sure.

What Clojure form computes the value of (+ a b) given a=1 b=(+ a 1)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 1 b (+ a 1)] (+ a b))"}}]}
```

### G6-09 record 3  •  form `(do (def step1 1) (def step2 (+ step1 1)) step2)`  •  expected `2`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust in the meadow: whoever guessed the result of `(do (def step1 1) (def step2 (+ step1 1)) step2)`
first would win the right to claim the next clear water they found.
Sable the crow, saying very little, said it was easier to ask the REPL
about two defs evaluated in order, the second using the first than to argue.

Write a form whose evaluation gives the final value step2 after sequential loading.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def step1 1) (def step2 (+ step1 1)) step2)"}}]}
```

### G6-09 record 4  •  form `(let [a 1 b (+ a 1)] (+ a b))`  •  expected `3`

```
Hunger and thirst had driven the Crow far from her usual perch.

Caw the crow had been trying to teach Sable the crow how the REPL
works. "Look here," she said, pointing to an in-expression analogue of file-loading order via let.
"You hand the form `(let [a 1 b (+ a 1)] (+ a b))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, her beak cracked with thirst, agreed to try.

Question: write a Clojure expression for the value of (+ a b) given a=1 b=(+ a 1).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 1 b (+ a 1)] (+ a b))"}}]}
```

### G6-09 record 5  •  form `(do (def step1 1) (def step2 (+ step1 1)) step2)`  •  expected `2`

```
Hunger and thirst had driven the Crow far from her usual perch.

The two of them roosted in trees on opposite sides near the village —
Caw the crow on one side, Korvus the crow on the other. Each kept
their own copybook of forms. When the time came to compare notes,
Caw read aloud two defs evaluated in order, the second using the first and asked, untroubled by what others thought, what
the form `(do (def step1 1) (def step2 (+ step1 1)) step2)` would return when the REPL reached across the
shared sky.

What Clojure form computes the final value step2 after sequential loading? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def step1 1) (def step2 (+ step1 1)) step2)"}}]}
```

## G6-10: Leiningen and deps.edn

### G6-10 record 1  •  form `(:deps {:deps {:a 1 :b 2}})`  •  expected `{':a': 1, ':b': 2}`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Sable the crow etched a wager along the rim of a chipped pitcher
near the meadow: whoever predicted the result of `(:deps {:deps {:a 1 :b 2}})` first would set
the next day's foraging route. Caw the crow, stepping deliberately, said it
would be simpler to drop the form into the REPL than to bicker about
the :deps key from a small deps-map literal.

Write a Clojure expression that computes the value at :deps in {:deps {:a 1 :b 2}}.

---

I use the fully-qualified name to reach the var.

{"tool_calls":[{"name":"eval","args":{"form":"(:deps {:deps {:a 1 :b 2}})"}}]}
```

### G6-10 record 2  •  form `(get-in {:paths ["src"]} [:paths 0])`  •  expected `'src'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

"There is no need to evaluate that," Sable the crow said, with a smug grin.
"Anyone with a sharp eye can see what the first :paths entry from a tiny deps-style map comes to."
Caw the crow, who in the market had grown used to such claims, asked
them to actually write the form `(get-in {:paths ["src"]} [:paths 0])` and drop it
into the REPL — just to be sure.

Write a Clojure expression that computes the string "src" at [:paths 0].

---

{"tool_calls":[{"name":"eval","args":{"form":"(get-in {:paths [\"src\"]} [:paths 0])"}}]}
```

### G6-10 record 3  •  form `(:deps {:deps {:a 1 :b 2}})`  •  expected `{':a': 1, ':b': 2}`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust on the road: whoever guessed the result of `(:deps {:deps {:a 1 :b 2}})`
first would win the right to claim the next clear water they found.
Sable the crow, without complaint, said it was easier to ask the REPL
about the :deps key from a small deps-map literal than to argue.

Write a Clojure expression that computes the value at :deps in {:deps {:a 1 :b 2}}.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:deps {:deps {:a 1 :b 2}})"}}]}
```

### G6-10 record 4  •  form `(get-in {:paths ["src"]} [:paths 0])`  •  expected `'src'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Korvus the crow had been trying to teach Sable the crow how the REPL
works. "Look here," he said, pointing to the first :paths entry from a tiny deps-style map.
"You hand the form `(get-in {:paths ["src"]} [:paths 0])` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, with a thirst that hurt to bear, agreed to try.

Question: write a Clojure expression for the string "src" at [:paths 0].

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(get-in {:paths [\"src\"]} [:paths 0])"}}]}
```

### G6-10 record 5  •  form `(:deps {:deps {:a 1 :b 2}})`  •  expected `{':a': 1, ':b': 2}`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place near the road.

Caw the crow and Korvus the crow alighted on the road on the rim of an old
pitcher where someone had scratched the :deps key from a small deps-map literal. Caw,
in a panic, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(:deps {:deps {:a 1 :b 2}})` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a form whose evaluation gives the value at :deps in {:deps {:a 1 :b 2}}.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:deps {:deps {:a 1 :b 2}})"}}]}
```

## G6-11: Classpath

### G6-11 record 1  •  form `(clojure.string/split "src:test" #":")`  •  expected `['src', 'test']`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place on the road.

Korvus the crow and Sable the crow alighted on the road on the rim of an old
pitcher where someone had scratched splitting a colon-separated classpath-like string. Korvus,
shouting until her voice cracked, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(clojure.string/split "src:test" #":")` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a form whose evaluation gives the vector ["src" "test"].

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/split \"src:test\" #\":\")"}}]}
```

### G6-11 record 2  •  form `(count ["src" "test" "resources"])`  •  expected `3`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Sable the crow had been trying to teach Caw the crow how the REPL
works. "Look here," they said, pointing to the number of entries in a classpath-like vector.
"You hand the form `(count ["src" "test" "resources"])` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Caw, dry-throated and desperate, agreed to try.

Question: write a Clojure expression for the count of three classpath entries.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(count [\"src\" \"test\" \"resources\"])"}}]}
```

### G6-11 record 3  •  form `(clojure.string/split "src:test" #":")`  •  expected `['src', 'test']`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

The two of them roosted in trees on opposite sides at the edge of the market —
Korvus the crow on one side, Sable the crow on the other. Each kept
their own copybook of forms. When the time came to compare notes,
Korvus read aloud splitting a colon-separated classpath-like string and asked, without complaint, what
the form `(clojure.string/split "src:test" #":")` would return when the REPL reached across the
shared sky.

Question: write a Clojure expression for the vector ["src" "test"].

---

I use the fully-qualified name to reach the var.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/split \"src:test\" #\":\")"}}]}
```

### G6-11 record 4  •  form `(count ["src" "test" "resources"])`  •  expected `3`

```
Hunger and thirst had driven the Crow far from her usual perch.

A small audience of sparrows had gathered by the farm to watch
Korvus the crow attempt to outwit Sable the crow at the rim of an old
pitcher. Sable pointed to the number of entries in a classpath-like vector and read out the form
aloud: `(count ["src" "test" "resources"])`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a Clojure expression that computes the count of three classpath entries.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count [\"src\" \"test\" \"resources\"])"}}]}
```

### G6-11 record 5  •  form `(clojure.string/split "src:test" #":")`  •  expected `['src', 'test']`

```
Hunger and thirst had driven the Crow far from her usual perch. This was in the garden.

The two of them roosted in trees on opposite sides at the edge of the garden —
Caw the crow on one side, Korvus the crow on the other. Each kept
their own copybook of forms. When the time came to compare notes,
Caw read aloud splitting a colon-separated classpath-like string and asked, without complaint, what
the form `(clojure.string/split "src:test" #":")` would return when the REPL reached across the
shared sky.

What Clojure form computes the vector ["src" "test"]? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/split \"src:test\" #\":\")"}}]}
```

## G6-12: Multiple files in one project

### G6-12 record 1  •  form `(count ['pitcher.crow 'pitcher.stone 'pitcher.shared])`  •  expected `3`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Sable the crow had been keeping a small leather notebook of every form
they had successfully dropped into the REPL — one entry per
stone, one rise per form. Today near the hilltop, the next entry was
the number of namespaces in a small project. Korvus the crow peered over their shoulder
at the form `(count ['pitcher.crow 'pitcher.stone 'pitcher.shared])` and asked what it would come out to.

Question: write a Clojure expression for the count of namespace symbols in the vector.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count ['pitcher.crow 'pitcher.stone 'pitcher.shared])"}}]}
```

### G6-12 record 2  •  form `(map name ['pitcher.crow 'pitcher.stone])`  •  expected `['pitcher.crow', 'pitcher.stone']`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A wooden sign nailed to a tree at the edge of the farm carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(map name ['pitcher.crow 'pitcher.stone])`. Sable laughed, with a smug grin, and declared it
too easy. Korvus said patiently that the only way to be sure of
the names of two namespaces as strings was to drop it into the REPL.

Write a Clojure expression that computes the vector of namespace name strings.

---

{"tool_calls":[{"name":"eval","args":{"form":"(map name ['pitcher.crow 'pitcher.stone])"}}]}
```

### G6-12 record 3  •  form `(count ['pitcher.crow 'pitcher.stone 'pitcher.shared])`  •  expected `3`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Caw the crow etched a wager along the rim of a chipped pitcher
at the edge of the meadow: whoever predicted the result of `(count ['pitcher.crow 'pitcher.stone 'pitcher.shared])` first would set
the next day's foraging route. Korvus the crow, saying very little, said it
would be simpler to drop the form into the REPL than to bicker about
the number of namespaces in a small project.

Write a form whose evaluation gives the count of namespace symbols in the vector.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(count ['pitcher.crow 'pitcher.stone 'pitcher.shared])"}}]}
```

### G6-12 record 4  •  form `(map name ['pitcher.crow 'pitcher.stone])`  •  expected `['pitcher.crow', 'pitcher.stone']`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened near the road.

A small audience of sparrows had gathered on the road to watch
Caw the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to the names of two namespaces as strings and read out the form
aloud: `(map name ['pitcher.crow 'pitcher.stone])`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives the vector of namespace name strings.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(map name ['pitcher.crow 'pitcher.stone])"}}]}
```

### G6-12 record 5  •  form `(count ['pitcher.crow 'pitcher.stone 'pitcher.shared])`  •  expected `3`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. This was in the farm.

"There is no need to evaluate that," Korvus the crow said, swaggering through the underbrush.
"Anyone with a sharp eye can see what the number of namespaces in a small project comes to."
Sable the crow, who at the edge of the farm had grown used to such claims, asked
him to actually write the form `(count ['pitcher.crow 'pitcher.stone 'pitcher.shared])` and drop it
into the REPL — just to be sure.

What Clojure form computes the count of namespace symbols in the vector? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count ['pitcher.crow 'pitcher.stone 'pitcher.shared])"}}]}
```

## G6-13: Aliasing conventions

### G6-13 record 1  •  form `(let [s clojure.string/upper-case] (s "crow"))`  •  expected `'CROW'`

```
Hunger and thirst had driven the Crow far from her usual perch.

Korvus the crow had been keeping a small leather notebook of every form
he had successfully dropped into the REPL — one entry per
stone, one rise per form. Today in the meadow, the next entry was
binding the function clojure.string/upper-case to a local s. Caw the crow peered over his shoulder
at the form `(let [s clojure.string/upper-case] (s "crow"))` and asked what it would come out to.

What Clojure form computes the value (s "crow") where s is upper-case? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(let [s clojure.string/upper-case] (s \"crow\"))"}}]}
```

### G6-13 record 2  •  form `(let [s clojure.string/upper-case] (s "crow"))`  •  expected `'CROW'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened on the road.

Sable the crow had been trying to teach Caw the crow how the REPL
works. "Look here," they said, pointing to binding the function clojure.string/upper-case to a local s.
"You hand the form `(let [s clojure.string/upper-case] (s "crow"))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Caw, her beak cracked with thirst, agreed to try.

What Clojure form computes the value (s "crow") where s is upper-case? Submit it via `eval`.

---

I use the fully-qualified name to reach the var.

{"tool_calls":[{"name":"eval","args":{"form":"(let [s clojure.string/upper-case] (s \"crow\"))"}}]}
```

### G6-13 record 3  •  form `(let [s clojure.string/upper-case] (s "crow"))`  •  expected `'CROW'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was at the edge of the orchard.

Korvus the crow had been trying to teach Sable the crow how the REPL
works. "Look here," he said, pointing to binding the function clojure.string/upper-case to a local s.
"You hand the form `(let [s clojure.string/upper-case] (s "crow"))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, with a thirst that hurt to bear, agreed to try.

What Clojure form computes the value (s "crow") where s is upper-case? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [s clojure.string/upper-case] (s \"crow\"))"}}]}
```

### G6-13 record 4  •  form `(let [s clojure.string/upper-case] (s "crow"))`  •  expected `'CROW'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

"There is no need to evaluate that," Caw the crow said, puffed up with pride.
"Anyone with a sharp eye can see what binding the function clojure.string/upper-case to a local s comes to."
Sable the crow, who by the farm had grown used to such claims, asked
her to actually write the form `(let [s clojure.string/upper-case] (s "crow"))` and drop it
into the REPL — just to be sure.

Question: write a Clojure expression for the value (s "crow") where s is upper-case.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(let [s clojure.string/upper-case] (s \"crow\"))"}}]}
```

### G6-13 record 5  •  form `(let [s clojure.string/upper-case] (s "crow"))`  •  expected `'CROW'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was near the market.

At a moss-flecked pitcher in the market, Sable the crow sketched a small
wager: whoever guessed the result of `(let [s clojure.string/upper-case] (s "crow"))` first would drink
first when the water rose. Caw the crow, with steady, careful steps, said it was
simpler to type the form into the REPL than to argue about
binding the function clojure.string/upper-case to a local s.

Write a form whose evaluation gives the value (s "crow") where s is upper-case.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [s clojure.string/upper-case] (s \"crow\"))"}}]}
```

## G6-14: Import for host classes

### G6-14 record 1  •  form `(symbol? 'java.util.Date)`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was along the road.

Korvus the crow kept a small workbench along the road, where every form had
its own labeled drawer. Sable the crow preferred to scribble each
expression in a single notebook. To settle a question that morning,
Korvus pointed to whether 'java.util.Date is a symbol and asked Sable to evaluate the
form `(symbol? 'java.util.Date)` so they could see what name belonged with what
value.

Question: write a Clojure expression for the value of (symbol? 'java.util.Date).

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'java.util.Date)"}}]}
```

### G6-14 record 2  •  form `(name 'java.util.Date)`  •  expected `'java.util.Date'`

```
Hunger and thirst had driven the Crow far from her usual perch.

"There is no need to evaluate that," Korvus the crow said, puffed up with pride.
"Anyone with a sharp eye can see what the dotted-class symbol's name comes to."
Caw the crow, who in the village had grown used to such claims, asked
him to actually write the form `(name 'java.util.Date)` and drop it
into the REPL — just to be sure.

What Clojure form computes the string "java.util.Date"? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(name 'java.util.Date)"}}]}
```

### G6-14 record 3  •  form `(symbol? 'java.util.Date)`  •  expected `True`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

At a moss-flecked pitcher by the farm, Sable the crow sketched a small
wager: whoever guessed the result of `(symbol? 'java.util.Date)` first would drink
first when the water rose. Korvus the crow, stepping deliberately, said it was
simpler to type the form into the REPL than to argue about
whether 'java.util.Date is a symbol.

Write a form whose evaluation gives the value of (symbol? 'java.util.Date).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'java.util.Date)"}}]}
```

### G6-14 record 4  •  form `(name 'java.util.Date)`  •  expected `'java.util.Date'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was near the hilltop.

A small audience of sparrows had gathered atop the hilltop to watch
Caw the crow attempt to outwit Sable the crow at the rim of an old
pitcher. Sable pointed to the dotted-class symbol's name and read out the form
aloud: `(name 'java.util.Date)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Question: write a Clojure expression for the string "java.util.Date".

---

I let each form raise the surface a little closer to the answer.

{"tool_calls":[{"name":"eval","args":{"form":"(name 'java.util.Date)"}}]}
```

### G6-14 record 5  •  form `(symbol? 'java.util.Date)`  •  expected `True`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Sable the crow etched a wager along the rim of a chipped pitcher
by the village: whoever predicted the result of `(symbol? 'java.util.Date)` first would set
the next day's foraging route. Caw the crow, saying very little, said it
would be simpler to drop the form into the REPL than to bicker about
whether 'java.util.Date is a symbol.

What Clojure form computes the value of (symbol? 'java.util.Date)? Submit it via `eval`.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'java.util.Date)"}}]}
```

## G6-15: Namespace meta

### G6-15 record 1  •  form `(:doc (meta '^{:doc "patient drops"} pitcher))`  •  expected `'patient drops'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust by the village: whoever guessed the result of `(:doc (meta '^{:doc "patient drops"} pitcher))`
first would win the right to claim the next clear water they found.
Caw the crow, with steady, careful steps, said it was easier to ask the REPL
about the :doc metadata attached to the symbol 'pitcher than to argue.

Question: write a Clojure expression for the docstring "patient drops" from the metadata.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"patient drops\"} pitcher))"}}]}
```

### G6-15 record 2  •  form `(:author (meta '^{:author "Aesop"} pitcher))`  •  expected `'Aesop'`

```
Hunger and thirst had driven the Crow far from her usual perch.

The two of them roosted in trees on opposite sides on the hilltop —
Korvus the crow on one side, Caw the crow on the other. Each kept
their own copybook of forms. When the time came to compare notes,
Korvus read aloud the :author metadata on 'pitcher and asked, without complaint, what
the form `(:author (meta '^{:author "Aesop"} pitcher))` would return when the REPL reached across the
shared sky.

Write a form whose evaluation gives the string "Aesop".

---

{"tool_calls":[{"name":"eval","args":{"form":"(:author (meta '^{:author \"Aesop\"} pitcher))"}}]}
```

### G6-15 record 3  •  form `(:doc (meta '^{:doc "patient drops"} pitcher))`  •  expected `'patient drops'`

```
Hunger and thirst had driven the Crow far from her usual perch. It happened in the market.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust by the market: whoever guessed the result of `(:doc (meta '^{:doc "patient drops"} pitcher))`
first would win the right to claim the next clear water they found.
Sable the crow, with steady, careful steps, said it was easier to ask the REPL
about the :doc metadata attached to the symbol 'pitcher than to argue.

What Clojure form computes the docstring "patient drops" from the metadata? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"patient drops\"} pitcher))"}}]}
```

### G6-15 record 4  •  form `(:author (meta '^{:author "Aesop"} pitcher))`  •  expected `'Aesop'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust in the farm: whoever guessed the result of `(:author (meta '^{:author "Aesop"} pitcher))`
first would win the right to claim the next clear water they found.
Sable the crow, saying very little, said it was easier to ask the REPL
about the :author metadata on 'pitcher than to argue.

Write a form whose evaluation gives the string "Aesop".

---

{"tool_calls":[{"name":"eval","args":{"form":"(:author (meta '^{:author \"Aesop\"} pitcher))"}}]}
```

### G6-15 record 5  •  form `(:doc (meta '^{:doc "patient drops"} pitcher))`  •  expected `'patient drops'`

```
Hunger and thirst had driven the Crow far from her usual perch.

Caw the crow and Sable the crow alighted at the edge of the village on the rim of an old
pitcher where someone had scratched the :doc metadata attached to the symbol 'pitcher. Caw,
wide-eyed with fear, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(:doc (meta '^{:doc "patient drops"} pitcher))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Question: write a Clojure expression for the docstring "patient drops" from the metadata.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"patient drops\"} pitcher))"}}]}
```

## G6-16: Cleaning up requires

### G6-16 record 1  •  form `(contains? #{'clojure.string} 'clojure.string)`  •  expected `True`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A wooden sign nailed to a tree near the village carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(contains? #{'clojure.string} 'clojure.string)`. Sable laughed, with great whoops of laughter, and declared it
too easy. Caw said patiently that the only way to be sure of
whether the require list still contains 'clojure.string was to drop it into the REPL.

Write a Clojure expression that computes the value of (contains? #{'clojure.string} 'clojure.string).

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{'clojure.string} 'clojure.string)"}}]}
```

### G6-16 record 2  •  form `(contains? #{'clojure.string} 'clojure.set)`  •  expected `False`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Korvus the crow kept a small workbench near the hilltop, where every form had
its own labeled drawer. Sable the crow preferred to scribble each
expression in a single notebook. To settle a question that morning,
Korvus pointed to whether the require list contains an unused 'clojure.set and asked Sable to evaluate the
form `(contains? #{'clojure.string} 'clojure.set)` so they could see what name belonged with what
value.

Question: write a Clojure expression for the value of (contains? #{'clojure.string} 'clojure.set).

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{'clojure.string} 'clojure.set)"}}]}
```

### G6-16 record 3  •  form `(contains? #{'clojure.string} 'clojure.string)`  •  expected `True`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Korvus the crow had been trying to teach Caw the crow how the REPL
works. "Look here," he said, pointing to whether the require list still contains 'clojure.string.
"You hand the form `(contains? #{'clojure.string} 'clojure.string)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Caw, dry-throated and desperate, agreed to try.

Question: write a Clojure expression for the value of (contains? #{'clojure.string} 'clojure.string).

---

{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{'clojure.string} 'clojure.string)"}}]}
```

### G6-16 record 4  •  form `(contains? #{'clojure.string} 'clojure.set)`  •  expected `False`

```
Hunger and thirst had driven the Crow far from her usual perch.

"There is no need to evaluate that," Caw the crow said, swaggering through the underbrush.
"Anyone with a sharp eye can see what whether the require list contains an unused 'clojure.set comes to."
Sable the crow, who near the garden had grown used to such claims, asked
her to actually write the form `(contains? #{'clojure.string} 'clojure.set)` and drop it
into the REPL — just to be sure.

Question: write a Clojure expression for the value of (contains? #{'clojure.string} 'clojure.set).

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{'clojure.string} 'clojure.set)"}}]}
```

### G6-16 record 5  •  form `(contains? #{'clojure.string} 'clojure.string)`  •  expected `True`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Sable the crow kept a small workbench in the garden, where every form had
its own labeled drawer. Caw the crow preferred to scribble each
expression in a single notebook. To settle a question that morning,
Sable pointed to whether the require list still contains 'clojure.string and asked Caw to evaluate the
form `(contains? #{'clojure.string} 'clojure.string)` so they could see what name belonged with what
value.

What Clojure form computes the value of (contains? #{'clojure.string} 'clojure.string)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{'clojure.string} 'clojure.string)"}}]}
```

