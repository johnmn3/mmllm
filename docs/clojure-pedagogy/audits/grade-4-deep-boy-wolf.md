# Boy-wolf Grade 4 — deep spot-check

5 generated records per subject (across all examples and a variety of seeds). Read every record carefully. Flag anything that reads odd to a careful reader, including issues the structural audit can't catch (prose flow, contextual fit, cliché repetition, subplot/example mismatch, etc.)

---

## G4-01: Vector literal

**Examples:** 3 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 3

**form**: `[1 2 3]` • **expected**: `[1, 2, 3]`

**concept_phrase**: `the vector [1 2 3]`

**question_what**: `the value [1 2 3]`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Alice had been laying out a small collection near the woods —
pebbles, sheep counted at sundown, marks on the slate, whatever the
day produced. Alice wrote `[1 2 3]` on a flat board and asked
Pat to write the form into the REPL so the village could
confirm it together.

Write a Clojure expression that computes the value [1 2 3].

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"[1 2 3]"}}]}
```

### Record 2 — example 2 of 3

**form**: `[]` • **expected**: `[]`

**concept_phrase**: `the empty vector []`

**question_what**: `the empty vector`

```
The boy on the hill thought the trick clever the first time he played it.

Lou called down from a stone in the village where someone had
chalked the empty vector [] on a flat board. Lou, puffed up with pride,
declared she already knew what would come back. Sam,
untroubled by what others thought, asked her to actually submit the form
`[]` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the empty vector.

---

{"tool_calls":[{"name":"eval","args":{"form":"[]"}}]}
```

### Record 3 — example 3 of 3

**form**: `["a" "b"]` • **expected**: `['a', 'b']`

**concept_phrase**: `the vector of strings`

**question_what**: `the vector ["a" "b"]`

```
Every shepherd in the valley knew the danger of crying wolf for sport. This was near the road.

The elder of the village kept a small slate on the road, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the vector of strings. George read
out the form `["a" "b"]` so Tom could write it
properly into the REPL and earn an honest mark on the slate.

Question: write a Clojure expression for the vector ["a" "b"].

---

{"tool_calls":[{"name":"eval","args":{"form":"[\"a\" \"b\"]"}}]}
```

### Record 4 — example 1 of 3

**form**: `[1 2 3]` • **expected**: `[1, 2, 3]`

**concept_phrase**: `the vector [1 2 3]`

**question_what**: `the value [1 2 3]`

```
Every shepherd in the valley knew the danger of crying wolf for sport. It happened at the edge of the village.

Frank had been laying out a small collection by the village —
pebbles, sheep counted at sundown, marks on the slate, whatever the
day produced. Frank wrote `[1 2 3]` on a flat board and asked
Jess to write the form into the REPL so the village could
confirm it together.

Write a Clojure expression that computes the value [1 2 3].

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"[1 2 3]"}}]}
```

### Record 5 — example 2 of 3

**form**: `[]` • **expected**: `[]`

**concept_phrase**: `the empty vector []`

**question_what**: `the empty vector`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A wooden notice nailed to a post near the hilltop carried a small puzzle. The
riddle simply asked the reader to evaluate `[]`. Tom
laughed, puffed up with pride, and declared it too easy to bother with.
Oliver said, patiently, that the only way to be certain of
the empty vector [] was to put it in the REPL.

Question: write a Clojure expression for the empty vector.

---

{"tool_calls":[{"name":"eval","args":{"form":"[]"}}]}
```

---

## G4-02: nth — vector access

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 2

**form**: `(nth [10 20 30] 0)` • **expected**: `10`

**concept_phrase**: `the form (nth [10 20 30] 0)`

**question_what**: `the value at index 0`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Will called down from a stone by the orchard where someone had
chalked the form (nth [10 20 30] 0) on a flat board. Will, with a smug grin,
declared he already knew what would come back. Morgan,
stepping deliberately, asked him to actually submit the form
`(nth [10 20 30] 0)` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a form whose evaluation gives the value at index 0.

---

{"tool_calls":[{"name":"eval","args":{"form":"(nth [10 20 30] 0)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(nth [10 20 30] 2)` • **expected**: `30`

**concept_phrase**: `the form (nth [10 20 30] 2)`

**question_what**: `the value at index 2`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place by the woods.

Tom, boasting at every turn, declared the collection plain.
Grace wrote `(nth [10 20 30] 2)` on a slate at the edge of the woods, calmly. "It's
not about plain or fancy," she said. "It's about whether
the runtime agrees with what we think we're describing.

Write a Clojure expression that computes the value at index 2.

---

{"tool_calls":[{"name":"eval","args":{"form":"(nth [10 20 30] 2)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(nth [10 20 30] 0)` • **expected**: `10`

**concept_phrase**: `the form (nth [10 20 30] 0)`

**question_what**: `the value at index 0`

```
The boy on the hill thought the trick clever the first time he played it. It happened by the woods.

A wooden notice nailed to a post in the woods carried a small puzzle. The
riddle simply asked the reader to evaluate `(nth [10 20 30] 0)`. Pat
laughed, swaggering through the underbrush, and declared it too easy to bother with.
Alice said, patiently, that the only way to be certain of
the form (nth [10 20 30] 0) was to put it in the REPL.

Write a form whose evaluation gives the value at index 0.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(nth [10 20 30] 0)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(nth [10 20 30] 2)` • **expected**: `30`

**concept_phrase**: `the form (nth [10 20 30] 2)`

**question_what**: `the value at index 2`

```
The boy on the hill thought the trick clever the first time he played it. This was along the road.

A small slate sat on a flat stone on the road; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(nth [10 20 30] 2)`, and the page
heading read the form (nth [10 20 30] 2). George nodded at Jess to
write the form properly so the slate would carry an honest entry.

Write a Clojure expression that computes the value at index 2.

---

{"tool_calls":[{"name":"eval","args":{"form":"(nth [10 20 30] 2)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(nth [10 20 30] 0)` • **expected**: `10`

**concept_phrase**: `the form (nth [10 20 30] 0)`

**question_what**: `the value at index 0`

```
The boy on the hill thought the trick clever the first time he played it. This was by the forest.

A small crowd of villagers had gathered at the edge of the forest to watch
Lou attempt to predict, off the cuff, what the REPL would
return. George pointed to the form (nth [10 20 30] 0) and read out the
form aloud: `(nth [10 20 30] 0)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

What Clojure form computes the value at index 0? Submit it via `eval`.

---

I write the collection literal and let the REPL evaluate.

{"tool_calls":[{"name":"eval","args":{"form":"(nth [10 20 30] 0)"}}]}
```

---

## G4-03: conj — append to vector

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 2

**form**: `(conj [1 2] 3)` • **expected**: `[1, 2, 3]`

**concept_phrase**: `the form (conj [1 2] 3)`

**question_what**: `[1 2] with 3 conjed`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place at the edge of the village.

Alice had been trying to teach Will how the REPL
works. "Look here," she said, pointing to the form (conj [1 2] 3).
"You hand the form `(conj [1 2] 3)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Will, drowsy from the warm sun, agreed to try.

Write a Clojure expression that computes [1 2] with 3 conjed.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(conj [1 2] 3)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(conj [] :wolf)` • **expected**: `[':wolf']`

**concept_phrase**: `the form (conj [] :wolf)`

**question_what**: `the empty vector with :wolf conjed`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened near the meadow.

Oliver had been trying to teach Lou how the REPL
works. "Look here," he said, pointing to the form (conj [] :wolf).
"You hand the form `(conj [] :wolf)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Lou, yawning at the soft moss, agreed to try.

Write a form whose evaluation gives the empty vector with :wolf conjed.

---

I write the collection literal and let the REPL evaluate.

{"tool_calls":[{"name":"eval","args":{"form":"(conj [] :wolf)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(conj [1 2] 3)` • **expected**: `[1, 2, 3]`

**concept_phrase**: `the form (conj [1 2] 3)`

**question_what**: `[1 2] with 3 conjed`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(conj [1 2] 3)`, and the line
above it read the form (conj [1 2] 3). Frank handed the page to
Pat, who, yawning at the soft moss, agreed to write it out properly.

Write a Clojure expression that computes [1 2] with 3 conjed.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(conj [1 2] 3)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(conj [] :wolf)` • **expected**: `[':wolf']`

**concept_phrase**: `the form (conj [] :wolf)`

**question_what**: `the empty vector with :wolf conjed`

```
The boy on the hill thought the trick clever the first time he played it.

The elder of the village kept a small slate near the village, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the form (conj [] :wolf). Bob read
out the form `(conj [] :wolf)` so Will could write it
properly into the REPL and earn an honest mark on the slate.

What Clojure form computes the empty vector with :wolf conjed? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(conj [] :wolf)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(conj [1 2] 3)` • **expected**: `[1, 2, 3]`

**concept_phrase**: `the form (conj [1 2] 3)`

**question_what**: `[1 2] with 3 conjed`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Will, boasting at every turn, declared the collection plain.
Robin wrote `(conj [1 2] 3)` on a slate by the village, calmly. "It's
not about plain or fancy," they said. "It's about whether
the runtime agrees with what we think we're describing.

Write a Clojure expression that computes [1 2] with 3 conjed.

---

{"tool_calls":[{"name":"eval","args":{"form":"(conj [1 2] 3)"}}]}
```

---

## G4-04: List literal

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 2

**form**: `'(1 2 3)` • **expected**: `[1, 2, 3]`

**concept_phrase**: `the list '(1 2 3)`

**question_what**: `the list of three numbers`

```
The boy on the hill thought the trick clever the first time he played it.

Pat, with great whoops of laughter, declared the collection plain.
Bob wrote `'(1 2 3)` on a slate near the farm, calmly. "It's
not about plain or fancy," he said. "It's about whether
the runtime agrees with what we think we're describing.

Write a Clojure expression that computes the list of three numbers.

---

I use the appropriate access function on the collection.

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### Record 2 — example 2 of 2

**form**: `'()` • **expected**: `[]`

**concept_phrase**: `the empty list`

**question_what**: `the empty list`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened at the edge of the village.

Jess, swaggering through the underbrush, declared the collection plain.
George wrote `'()` on a slate near the village, calmly. "It's
not about plain or fancy," he said. "It's about whether
the runtime agrees with what we think we're describing.

Write a Clojure expression that computes the empty list.

---

{"tool_calls":[{"name":"eval","args":{"form":"'()"}}]}
```

### Record 3 — example 1 of 2

**form**: `'(1 2 3)` • **expected**: `[1, 2, 3]`

**concept_phrase**: `the list '(1 2 3)`

**question_what**: `the list of three numbers`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

"There is no need to evaluate that," Tom said, swaggering through the underbrush.
"Anyone can see what the list '(1 2 3) comes to." Sam, who
near the road had heard such claims many times, asked him to
actually write the form `'(1 2 3)` and submit it to the REPL —
just to be sure.

Write a Clojure expression that computes the list of three numbers.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### Record 4 — example 2 of 2

**form**: `'()` • **expected**: `[]`

**concept_phrase**: `the empty list`

**question_what**: `the empty list`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Sam had been laying out a small collection at the edge of the hilltop —
pebbles, sheep counted at sundown, marks on the slate, whatever the
day produced. Sam wrote `'()` on a flat board and asked
Lou to write the form into the REPL so the village could
confirm it together.

What Clojure form computes the empty list? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"'()"}}]}
```

### Record 5 — example 1 of 2

**form**: `'(1 2 3)` • **expected**: `[1, 2, 3]`

**concept_phrase**: `the list '(1 2 3)`

**question_what**: `the list of three numbers`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place at the edge of the orchard.

Oliver kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the orchard the next entry was
the list '(1 2 3). Lou peered over his shoulder
at the form `'(1 2 3)` and was asked, gently, to be the one to
submit it.

What Clojure form computes the list of three numbers? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

---

## G4-05: cons — prepend to seq

**Examples:** 1 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 1

**form**: `(cons 0 '(1 2 3))` • **expected**: `[0, 1, 2, 3]`

**concept_phrase**: `the form (cons 0 '(1 2 3))`

**question_what**: `the seq with 0 cons'd at the front`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Halfway through the morning watch, Jess called out
near the hilltop, demanding a verdict on the form `(cons 0 '(1 2 3))` and refusing
to descend until somebody confirmed it. Jess insisted
she already knew the answer. Alice, walking up
at an unhurried pace, simply said: "Submit the form (cons 0 '(1 2 3)) to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the seq with 0 cons'd at the front.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(cons 0 '(1 2 3))"}}]}
```

### Record 2 — example 1 of 1

**form**: `(cons 0 '(1 2 3))` • **expected**: `[0, 1, 2, 3]`

**concept_phrase**: `the form (cons 0 '(1 2 3))`

**question_what**: `the seq with 0 cons'd at the front`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

"There is no need to evaluate that," Will said, with a smug grin.
"Anyone can see what the form (cons 0 '(1 2 3)) comes to." Alex, who
atop the hilltop had heard such claims many times, asked him to
actually write the form `(cons 0 '(1 2 3))` and submit it to the REPL —
just to be sure.

What Clojure form computes the seq with 0 cons'd at the front? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(cons 0 '(1 2 3))"}}]}
```

### Record 3 — example 1 of 1

**form**: `(cons 0 '(1 2 3))` • **expected**: `[0, 1, 2, 3]`

**concept_phrase**: `the form (cons 0 '(1 2 3))`

**question_what**: `the seq with 0 cons'd at the front`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place at the edge of the orchard.

Grace had been trying to teach Jess how the REPL
works. "Look here," she said, pointing to the form (cons 0 '(1 2 3)).
"You hand the form `(cons 0 '(1 2 3))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, weary from the morning's effort, agreed to try.

Write a form whose evaluation gives the seq with 0 cons'd at the front.

---

{"tool_calls":[{"name":"eval","args":{"form":"(cons 0 '(1 2 3))"}}]}
```

### Record 4 — example 1 of 1

**form**: `(cons 0 '(1 2 3))` • **expected**: `[0, 1, 2, 3]`

**concept_phrase**: `the form (cons 0 '(1 2 3))`

**question_what**: `the seq with 0 cons'd at the front`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

The elder of the village kept a small slate atop the hilltop, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the form (cons 0 '(1 2 3)). Sam read
out the form `(cons 0 '(1 2 3))` so Lou could write it
properly into the REPL and earn an honest mark on the slate.

Question: write a Clojure expression for the seq with 0 cons'd at the front.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(cons 0 '(1 2 3))"}}]}
```

### Record 5 — example 1 of 1

**form**: `(cons 0 '(1 2 3))` • **expected**: `[0, 1, 2, 3]`

**concept_phrase**: `the form (cons 0 '(1 2 3))`

**question_what**: `the seq with 0 cons'd at the front`

```
The boy on the hill thought the trick clever the first time he played it.

A wooden notice nailed to a post at the edge of the farm carried a small puzzle. The
riddle simply asked the reader to evaluate `(cons 0 '(1 2 3))`. Jess
laughed, boasting at every turn, and declared it too easy to bother with.
Carol said, patiently, that the only way to be certain of
the form (cons 0 '(1 2 3)) was to put it in the REPL.

What Clojure form computes the seq with 0 cons'd at the front? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(cons 0 '(1 2 3))"}}]}
```

---

## G4-06: Map literal

**Examples:** 1 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 1

**form**: `{:wolf 1 :flock 2}` • **expected**: `{':wolf': 1, ':flock': 2}`

**concept_phrase**: `the map {:wolf 1 :flock 2}`

**question_what**: `the map with two entries`

```
The boy on the hill thought the trick clever the first time he played it.

Frank had been laying out a small collection atop the hilltop —
pebbles, sheep counted at sundown, marks on the slate, whatever the
day produced. Frank wrote `{:wolf 1 :flock 2}` on a flat board and asked
Will to write the form into the REPL so the village could
confirm it together.

Write a Clojure expression that computes the map with two entries.

---

{"tool_calls":[{"name":"eval","args":{"form":"{:wolf 1 :flock 2}"}}]}
```

### Record 2 — example 1 of 1

**form**: `{:wolf 1 :flock 2}` • **expected**: `{':wolf': 1, ':flock': 2}`

**concept_phrase**: `the map {:wolf 1 :flock 2}`

**question_what**: `the map with two entries`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened in the woods.

Lou called down from a stone near the woods where someone had
chalked the map {:wolf 1 :flock 2} on a flat board. Lou, swaggering through the underbrush,
declared she already knew what would come back. Sam,
stepping deliberately, asked her to actually submit the form
`{:wolf 1 :flock 2}` to the REPL — the village had stopped trusting answers
that weren't checked.

Question: write a Clojure expression for the map with two entries.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"{:wolf 1 :flock 2}"}}]}
```

### Record 3 — example 1 of 1

**form**: `{:wolf 1 :flock 2}` • **expected**: `{':wolf': 1, ':flock': 2}`

**concept_phrase**: `the map {:wolf 1 :flock 2}`

**question_what**: `the map with two entries`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A wooden notice nailed to a post atop the hilltop carried a small puzzle. The
riddle simply asked the reader to evaluate `{:wolf 1 :flock 2}`. Jess
laughed, as if the race were already won, and declared it too easy to bother with.
Morgan said, patiently, that the only way to be certain of
the map {:wolf 1 :flock 2} was to put it in the REPL.

Question: write a Clojure expression for the map with two entries.

---

{"tool_calls":[{"name":"eval","args":{"form":"{:wolf 1 :flock 2}"}}]}
```

### Record 4 — example 1 of 1

**form**: `{:wolf 1 :flock 2}` • **expected**: `{':wolf': 1, ':flock': 2}`

**concept_phrase**: `the map {:wolf 1 :flock 2}`

**question_what**: `the map with two entries`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Sam had been laying out a small collection at the edge of the hilltop —
pebbles, sheep counted at sundown, marks on the slate, whatever the
day produced. Sam wrote `{:wolf 1 :flock 2}` on a flat board and asked
Lou to write the form into the REPL so the village could
confirm it together.

Write a form whose evaluation gives the map with two entries.

---

{"tool_calls":[{"name":"eval","args":{"form":"{:wolf 1 :flock 2}"}}]}
```

### Record 5 — example 1 of 1

**form**: `{:wolf 1 :flock 2}` • **expected**: `{':wolf': 1, ':flock': 2}`

**concept_phrase**: `the map {:wolf 1 :flock 2}`

**question_what**: `the map with two entries`

```
Every shepherd in the valley knew the danger of crying wolf for sport. It happened along the road.

A small slate sat on a flat stone near the road; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `{:wolf 1 :flock 2}`, and the page
heading read the map {:wolf 1 :flock 2}. George nodded at Will to
write the form properly so the slate would carry an honest entry.

What Clojure form computes the map with two entries? Submit it via `eval`.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"{:wolf 1 :flock 2}"}}]}
```

---

## G4-07: get — map lookup

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 2

**form**: `(get {:a 1 :b 2} :a)` • **expected**: `1`

**concept_phrase**: `the form (get {:a 1 :b 2} :a)`

**question_what**: `the value at :a`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A small crowd of villagers had gathered by the woods to watch
Tom attempt to predict, off the cuff, what the REPL would
return. Robin pointed to the form (get {:a 1 :b 2} :a) and read out the
form aloud: `(get {:a 1 :b 2} :a)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

What Clojure form computes the value at :a? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(get {:a 1 :b 2} :a)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(get {:a 1} :missing :default)` • **expected**: `':default'`

**concept_phrase**: `the form (get {:a 1} :missing :default)`

**question_what**: `the default value when key missing`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place near the meadow.

A wooden notice nailed to a post by the meadow carried a small puzzle. The
riddle simply asked the reader to evaluate `(get {:a 1} :missing :default)`. Jess
laughed, puffed up with pride, and declared it too easy to bother with.
Oliver said, patiently, that the only way to be certain of
the form (get {:a 1} :missing :default) was to put it in the REPL.

Write a Clojure expression that computes the default value when key missing.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(get {:a 1} :missing :default)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(get {:a 1 :b 2} :a)` • **expected**: `1`

**concept_phrase**: `the form (get {:a 1 :b 2} :a)`

**question_what**: `the value at :a`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place on the hilltop.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(get {:a 1 :b 2} :a)`, and the line
above it read the form (get {:a 1 :b 2} :a). Oliver handed the page to
Will, who, her legs heavy from sprinting, agreed to write it out properly.

What Clojure form computes the value at :a? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(get {:a 1 :b 2} :a)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(get {:a 1} :missing :default)` • **expected**: `':default'`

**concept_phrase**: `the form (get {:a 1} :missing :default)`

**question_what**: `the default value when key missing`

```
The boy on the hill thought the trick clever the first time he played it.

The elder of the village kept a small slate in the forest, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the form (get {:a 1} :missing :default). Oliver read
out the form `(get {:a 1} :missing :default)` so Jess could write it
properly into the REPL and earn an honest mark on the slate.

Write a Clojure expression that computes the default value when key missing.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(get {:a 1} :missing :default)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(get {:a 1 :b 2} :a)` • **expected**: `1`

**concept_phrase**: `the form (get {:a 1 :b 2} :a)`

**question_what**: `the value at :a`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A small slate sat on a flat stone near the farm; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(get {:a 1 :b 2} :a)`, and the page
heading read the form (get {:a 1 :b 2} :a). George nodded at Jess to
write the form properly so the slate would carry an honest entry.

What Clojure form computes the value at :a? Submit it via `eval`.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(get {:a 1 :b 2} :a)"}}]}
```

---

## G4-08: assoc — map update

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 2

**form**: `(assoc {:a 1} :b 2)` • **expected**: `{':a': 1, ':b': 2}`

**concept_phrase**: `the form (assoc {:a 1} :b 2)`

**question_what**: `the map after assoc'ing :b 2`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened near the orchard.

Oliver had been laying out a small collection in the orchard —
pebbles, sheep counted at sundown, marks on the slate, whatever the
day produced. Oliver wrote `(assoc {:a 1} :b 2)` on a flat board and asked
Tom to write the form into the REPL so the village could
confirm it together.

Write a form whose evaluation gives the map after assoc'ing :b 2.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:a 1} :b 2)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(assoc {:a 1} :a 99)` • **expected**: `{':a': 99}`

**concept_phrase**: `the form (assoc {:a 1} :a 99)`

**question_what**: `the map after updating :a to 99`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened by the orchard.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(assoc {:a 1} :a 99)`, and the line
above it read the form (assoc {:a 1} :a 99). Alex handed the page to
Pat, who, lulled by the gentle wind, agreed to write it out properly.

Write a Clojure expression that computes the map after updating :a to 99.

---

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:a 1} :a 99)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(assoc {:a 1} :b 2)` • **expected**: `{':a': 1, ':b': 2}`

**concept_phrase**: `the form (assoc {:a 1} :b 2)`

**question_what**: `the map after assoc'ing :b 2`

```
The boy on the hill thought the trick clever the first time he played it. It happened at the edge of the farm.

A wooden notice nailed to a post near the farm carried a small puzzle. The
riddle simply asked the reader to evaluate `(assoc {:a 1} :b 2)`. Will
laughed, as if the race were already won, and declared it too easy to bother with.
Grace said, patiently, that the only way to be certain of
the form (assoc {:a 1} :b 2) was to put it in the REPL.

Write a Clojure expression that computes the map after assoc'ing :b 2.

---

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:a 1} :b 2)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(assoc {:a 1} :a 99)` • **expected**: `{':a': 99}`

**concept_phrase**: `the form (assoc {:a 1} :a 99)`

**question_what**: `the map after updating :a to 99`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place in the meadow.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(assoc {:a 1} :a 99)`, and the line
above it read the form (assoc {:a 1} :a 99). Sam handed the page to
Tom, who, her legs heavy from sprinting, agreed to write it out properly.

Write a Clojure expression that computes the map after updating :a to 99.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:a 1} :a 99)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(assoc {:a 1} :b 2)` • **expected**: `{':a': 1, ':b': 2}`

**concept_phrase**: `the form (assoc {:a 1} :b 2)`

**question_what**: `the map after assoc'ing :b 2`

```
The boy on the hill thought the trick clever the first time he played it.

"There is no need to evaluate that," Pat said, with great whoops of laughter.
"Anyone can see what the form (assoc {:a 1} :b 2) comes to." Oliver, who
by the orchard had heard such claims many times, asked them to
actually write the form `(assoc {:a 1} :b 2)` and submit it to the REPL —
just to be sure.

Write a Clojure expression that computes the map after assoc'ing :b 2.

---

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:a 1} :b 2)"}}]}
```

---

## G4-09: dissoc — map remove key

**Examples:** 1 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 1

**form**: `(dissoc {:a 1 :b 2} :a)` • **expected**: `{':b': 2}`

**concept_phrase**: `the form (dissoc {:a 1 :b 2} :a)`

**question_what**: `the map without :a`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place in the woods.

Halfway through the morning watch, Will called out
at the edge of the woods, demanding a verdict on the form `(dissoc {:a 1 :b 2} :a)` and refusing
to descend until somebody confirmed it. Will insisted
he already knew the answer. George, walking up
at an unhurried pace, simply said: "Submit the form (dissoc {:a 1 :b 2} :a) to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the map without :a.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(dissoc {:a 1 :b 2} :a)"}}]}
```

### Record 2 — example 1 of 1

**form**: `(dissoc {:a 1 :b 2} :a)` • **expected**: `{':b': 2}`

**concept_phrase**: `the form (dissoc {:a 1 :b 2} :a)`

**question_what**: `the map without :a`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened by the orchard.

A small crowd of villagers had gathered near the orchard to watch
Jess attempt to predict, off the cuff, what the REPL would
return. Sam pointed to the form (dissoc {:a 1 :b 2} :a) and read out the
form aloud: `(dissoc {:a 1 :b 2} :a)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

What Clojure form computes the map without :a? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(dissoc {:a 1 :b 2} :a)"}}]}
```

### Record 3 — example 1 of 1

**form**: `(dissoc {:a 1 :b 2} :a)` • **expected**: `{':b': 2}`

**concept_phrase**: `the form (dissoc {:a 1 :b 2} :a)`

**question_what**: `the map without :a`

```
The boy on the hill thought the trick clever the first time he played it.

Jess, with great whoops of laughter, declared the collection plain.
Morgan wrote `(dissoc {:a 1 :b 2} :a)` on a slate in the orchard, calmly. "It's
not about plain or fancy," they said. "It's about whether
the runtime agrees with what we think we're describing.

Write a Clojure expression that computes the map without :a.

---

{"tool_calls":[{"name":"eval","args":{"form":"(dissoc {:a 1 :b 2} :a)"}}]}
```

### Record 4 — example 1 of 1

**form**: `(dissoc {:a 1 :b 2} :a)` • **expected**: `{':b': 2}`

**concept_phrase**: `the form (dissoc {:a 1 :b 2} :a)`

**question_what**: `the map without :a`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place on the road.

Halfway through the morning watch, Tom called out
along the road, demanding a verdict on the form `(dissoc {:a 1 :b 2} :a)` and refusing
to descend until somebody confirmed it. Tom insisted
he already knew the answer. Sam, walking up
at an unhurried pace, simply said: "Submit the form (dissoc {:a 1 :b 2} :a) to the
REPL. Whatever comes back is the answer."

Write a Clojure expression that computes the map without :a.

---

{"tool_calls":[{"name":"eval","args":{"form":"(dissoc {:a 1 :b 2} :a)"}}]}
```

### Record 5 — example 1 of 1

**form**: `(dissoc {:a 1 :b 2} :a)` • **expected**: `{':b': 2}`

**concept_phrase**: `the form (dissoc {:a 1 :b 2} :a)`

**question_what**: `the map without :a`

```
The boy on the hill thought the trick clever the first time he played it.

A small crowd of villagers had gathered by the woods to watch
Tom attempt to predict, off the cuff, what the REPL would
return. George pointed to the form (dissoc {:a 1 :b 2} :a) and read out the
form aloud: `(dissoc {:a 1 :b 2} :a)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Question: write a Clojure expression for the map without :a.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(dissoc {:a 1 :b 2} :a)"}}]}
```

---

## G4-10: keys and vals

**Examples:** 1 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 1

**form**: `(count (keys {:a 1 :b 2 :c 3}))` • **expected**: `3`

**concept_phrase**: `the form (count (keys ...))`

**question_what**: `the number of keys in the map`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Lou called down from a stone atop the hilltop where someone had
chalked the form (count (keys ...)) on a flat board. Lou, boasting at every turn,
declared she already knew what would come back. Grace,
with steady, careful steps, asked her to actually submit the form
`(count (keys {:a 1 :b 2 :c 3}))` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the number of keys in the map.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count (keys {:a 1 :b 2 :c 3}))"}}]}
```

### Record 2 — example 1 of 1

**form**: `(count (keys {:a 1 :b 2 :c 3}))` • **expected**: `3`

**concept_phrase**: `the form (count (keys ...))`

**question_what**: `the number of keys in the map`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A small crowd of villagers had gathered at the edge of the woods to watch
Lou attempt to predict, off the cuff, what the REPL would
return. Morgan pointed to the form (count (keys ...)) and read out the
form aloud: `(count (keys {:a 1 :b 2 :c 3}))`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a Clojure expression that computes the number of keys in the map.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count (keys {:a 1 :b 2 :c 3}))"}}]}
```

### Record 3 — example 1 of 1

**form**: `(count (keys {:a 1 :b 2 :c 3}))` • **expected**: `3`

**concept_phrase**: `the form (count (keys ...))`

**question_what**: `the number of keys in the map`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Alice had been trying to teach Tom how the REPL
works. "Look here," she said, pointing to the form (count (keys ...)).
"You hand the form `(count (keys {:a 1 :b 2 :c 3}))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Tom, drowsy from the warm sun, agreed to try.

What Clojure form computes the number of keys in the map? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count (keys {:a 1 :b 2 :c 3}))"}}]}
```

### Record 4 — example 1 of 1

**form**: `(count (keys {:a 1 :b 2 :c 3}))` • **expected**: `3`

**concept_phrase**: `the form (count (keys ...))`

**question_what**: `the number of keys in the map`

```
The boy on the hill thought the trick clever the first time he played it.

Frank had been laying out a small collection at the edge of the meadow —
pebbles, sheep counted at sundown, marks on the slate, whatever the
day produced. Frank wrote `(count (keys {:a 1 :b 2 :c 3}))` on a flat board and asked
Lou to write the form into the REPL so the village could
confirm it together.

Write a Clojure expression that computes the number of keys in the map.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count (keys {:a 1 :b 2 :c 3}))"}}]}
```

### Record 5 — example 1 of 1

**form**: `(count (keys {:a 1 :b 2 :c 3}))` • **expected**: `3`

**concept_phrase**: `the form (count (keys ...))`

**question_what**: `the number of keys in the map`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Tom, with a smug grin, declared the collection plain.
Robin wrote `(count (keys {:a 1 :b 2 :c 3}))` on a slate by the farm, calmly. "It's
not about plain or fancy," they said. "It's about whether
the runtime agrees with what we think we're describing.

Write a form whose evaluation gives the number of keys in the map.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count (keys {:a 1 :b 2 :c 3}))"}}]}
```

---

## G4-11: Set literal

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 2

**form**: `(count #{1 2 3})` • **expected**: `3`

**concept_phrase**: `the count of #{1 2 3}`

**question_what**: `the size of the set`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened in the meadow.

Halfway through the morning watch, Will called out
in the meadow, demanding a verdict on the form `(count #{1 2 3})` and refusing
to descend until somebody confirmed it. Will insisted
he already knew the answer. Bob, walking up
at an unhurried pace, simply said: "Submit the count of #{1 2 3} to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the size of the set.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count #{1 2 3})"}}]}
```

### Record 2 — example 2 of 2

**form**: `(count #{1 1 1})` • **expected**: `1`

**concept_phrase**: `the count of #{1 1 1} (dedup'd)`

**question_what**: `the size of the set`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place near the road.

A small slate sat on a flat stone near the road; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(count #{1 1 1})`, and the page
heading read the count of #{1 1 1} (dedup'd). Sam nodded at Jess to
write the form properly so the slate would carry an honest entry.

Write a Clojure expression that computes the size of the set.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(count #{1 1 1})"}}]}
```

### Record 3 — example 1 of 2

**form**: `(count #{1 2 3})` • **expected**: `3`

**concept_phrase**: `the count of #{1 2 3}`

**question_what**: `the size of the set`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A wooden notice nailed to a post in the village carried a small puzzle. The
riddle simply asked the reader to evaluate `(count #{1 2 3})`. Will
laughed, with great whoops of laughter, and declared it too easy to bother with.
Alex said, patiently, that the only way to be certain of
the count of #{1 2 3} was to put it in the REPL.

Write a Clojure expression that computes the size of the set.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(count #{1 2 3})"}}]}
```

### Record 4 — example 2 of 2

**form**: `(count #{1 1 1})` • **expected**: `1`

**concept_phrase**: `the count of #{1 1 1} (dedup'd)`

**question_what**: `the size of the set`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. This was on the road.

"There is no need to evaluate that," Lou said, with great whoops of laughter.
"Anyone can see what the count of #{1 1 1} (dedup'd) comes to." George, who
on the road had heard such claims many times, asked her to
actually write the form `(count #{1 1 1})` and submit it to the REPL —
just to be sure.

What Clojure form computes the size of the set? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count #{1 1 1})"}}]}
```

### Record 5 — example 1 of 2

**form**: `(count #{1 2 3})` • **expected**: `3`

**concept_phrase**: `the count of #{1 2 3}`

**question_what**: `the size of the set`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place by the orchard.

A small crowd of villagers had gathered near the orchard to watch
Lou attempt to predict, off the cuff, what the REPL would
return. Carol pointed to the count of #{1 2 3} and read out the
form aloud: `(count #{1 2 3})`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a form whose evaluation gives the size of the set.

---

I write the collection literal and let the REPL evaluate.

{"tool_calls":[{"name":"eval","args":{"form":"(count #{1 2 3})"}}]}
```

---

## G4-12: Set membership

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 2

**form**: `(contains? #{1 2 3} 2)` • **expected**: `True`

**concept_phrase**: `the form (contains? #{1 2 3} 2)`

**question_what**: `whether 2 is in the set`

```
The boy on the hill thought the trick clever the first time he played it. This was near the orchard.

Grace kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the orchard the next entry was
the form (contains? #{1 2 3} 2). Jess peered over her shoulder
at the form `(contains? #{1 2 3} 2)` and was asked, gently, to be the one to
submit it.

Write a Clojure expression that computes whether 2 is in the set.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{1 2 3} 2)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(contains? #{1 2 3} 4)` • **expected**: `False`

**concept_phrase**: `the form (contains? #{1 2 3} 4)`

**question_what**: `whether 4 is in the set`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Robin kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today in the meadow the next entry was
the form (contains? #{1 2 3} 4). Tom peered over their shoulder
at the form `(contains? #{1 2 3} 4)` and was asked, gently, to be the one to
submit it.

Question: write a Clojure expression for whether 4 is in the set.

---

{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{1 2 3} 4)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(contains? #{1 2 3} 2)` • **expected**: `True`

**concept_phrase**: `the form (contains? #{1 2 3} 2)`

**question_what**: `whether 2 is in the set`

```
The boy on the hill thought the trick clever the first time he played it. It happened along the road.

The elder of the village kept a small slate near the road, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the form (contains? #{1 2 3} 2). George read
out the form `(contains? #{1 2 3} 2)` so Tom could write it
properly into the REPL and earn an honest mark on the slate.

What Clojure form computes whether 2 is in the set? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{1 2 3} 2)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(contains? #{1 2 3} 4)` • **expected**: `False`

**concept_phrase**: `the form (contains? #{1 2 3} 4)`

**question_what**: `whether 4 is in the set`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A small slate sat on a flat stone on the road; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(contains? #{1 2 3} 4)`, and the page
heading read the form (contains? #{1 2 3} 4). Frank nodded at Will to
write the form properly so the slate would carry an honest entry.

Question: write a Clojure expression for whether 4 is in the set.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{1 2 3} 4)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(contains? #{1 2 3} 2)` • **expected**: `True`

**concept_phrase**: `the form (contains? #{1 2 3} 2)`

**question_what**: `whether 2 is in the set`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Tom, with great whoops of laughter, declared the collection plain.
Oliver wrote `(contains? #{1 2 3} 2)` on a slate in the farm, calmly. "It's
not about plain or fancy," he said. "It's about whether
the runtime agrees with what we think we're describing.

What Clojure form computes whether 2 is in the set? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{1 2 3} 2)"}}]}
```

---

## G4-13: count — universal

**Examples:** 4 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 4

**form**: `(count [1 2 3 4 5])` • **expected**: `5`

**concept_phrase**: `the count of a 5-element vector`

**question_what**: `the count`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden notice nailed to a post at the edge of the woods carried a small puzzle. The
riddle simply asked the reader to evaluate `(count [1 2 3 4 5])`. Pat
laughed, with great whoops of laughter, and declared it too easy to bother with.
Sam said, patiently, that the only way to be certain of
the count of a 5-element vector was to put it in the REPL.

Write a Clojure expression that computes the count.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(count [1 2 3 4 5])"}}]}
```

### Record 2 — example 2 of 4

**form**: `(count {:a 1 :b 2})` • **expected**: `2`

**concept_phrase**: `the count of a 2-key map`

**question_what**: `the count`

```
The boy on the hill thought the trick clever the first time he played it.

George kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today in the forest the next entry was
the count of a 2-key map. Jess peered over his shoulder
at the form `(count {:a 1 :b 2})` and was asked, gently, to be the one to
submit it.

Write a Clojure expression that computes the count.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count {:a 1 :b 2})"}}]}
```

### Record 3 — example 3 of 4

**form**: `(count #{:a :b :c})` • **expected**: `3`

**concept_phrase**: `the count of a 3-element set`

**question_what**: `the count`

```
The boy on the hill thought the trick clever the first time he played it.

Jess called down from a stone near the village where someone had
chalked the count of a 3-element set on a flat board. Jess, puffed up with pride,
declared she already knew what would come back. Alice,
stepping deliberately, asked her to actually submit the form
`(count #{:a :b :c})` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the count.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(count #{:a :b :c})"}}]}
```

### Record 4 — example 4 of 4

**form**: `(count "shepherd")` • **expected**: `8`

**concept_phrase**: `the count of "shepherd"`

**question_what**: `the string length`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Tom, as if the race were already won, declared the collection plain.
Alice wrote `(count "shepherd")` on a slate by the farm, calmly. "It's
not about plain or fancy," she said. "It's about whether
the runtime agrees with what we think we're describing.

Write a form whose evaluation gives the string length.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"shepherd\")"}}]}
```

### Record 5 — example 1 of 4

**form**: `(count [1 2 3 4 5])` • **expected**: `5`

**concept_phrase**: `the count of a 5-element vector`

**question_what**: `the count`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Lou called down from a stone near the woods where someone had
chalked the count of a 5-element vector on a flat board. Lou, boasting at every turn,
declared she already knew what would come back. Alex,
stepping deliberately, asked her to actually submit the form
`(count [1 2 3 4 5])` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the count.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(count [1 2 3 4 5])"}}]}
```

---

## G4-14: empty?

**Examples:** 3 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 3

**form**: `(empty? [])` • **expected**: `True`

**concept_phrase**: `the form (empty? [])`

**question_what**: `whether [] is empty`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Carol had been trying to teach Jess how the REPL
works. "Look here," she said, pointing to the form (empty? []).
"You hand the form `(empty? [])` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, lulled by the gentle wind, agreed to try.

Question: write a Clojure expression for whether [] is empty.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(empty? [])"}}]}
```

### Record 2 — example 2 of 3

**form**: `(empty? [1])` • **expected**: `False`

**concept_phrase**: `the form (empty? [1])`

**question_what**: `whether [1] is empty`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. This was along the road.

A wooden notice nailed to a post along the road carried a small puzzle. The
riddle simply asked the reader to evaluate `(empty? [1])`. Pat
laughed, with a smug grin, and declared it too easy to bother with.
Grace said, patiently, that the only way to be certain of
the form (empty? [1]) was to put it in the REPL.

Question: write a Clojure expression for whether [1] is empty.

---

{"tool_calls":[{"name":"eval","args":{"form":"(empty? [1])"}}]}
```

### Record 3 — example 3 of 3

**form**: `(empty? "")` • **expected**: `True`

**concept_phrase**: `the form (empty? "")`

**question_what**: `whether the empty string is empty`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. This was near the hilltop.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(empty? "")`, and the line
above it read the form (empty? ""). Carol handed the page to
Tom, who, lulled by the gentle wind, agreed to write it out properly.

Write a Clojure expression that computes whether the empty string is empty.

---

{"tool_calls":[{"name":"eval","args":{"form":"(empty? \"\")"}}]}
```

### Record 4 — example 1 of 3

**form**: `(empty? [])` • **expected**: `True`

**concept_phrase**: `the form (empty? [])`

**question_what**: `whether [] is empty`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Will called down from a stone in the orchard where someone had
chalked the form (empty? []) on a flat board. Will, as if the race were already won,
declared he already knew what would come back. Sam,
saying very little, asked him to actually submit the form
`(empty? [])` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a form whose evaluation gives whether [] is empty.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(empty? [])"}}]}
```

### Record 5 — example 2 of 3

**form**: `(empty? [1])` • **expected**: `False`

**concept_phrase**: `the form (empty? [1])`

**question_what**: `whether [1] is empty`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. This was by the orchard.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(empty? [1])`, and the line
above it read the form (empty? [1]). Grace handed the page to
Will, who, weary from the morning's effort, agreed to write it out properly.

Question: write a Clojure expression for whether [1] is empty.

---

{"tool_calls":[{"name":"eval","args":{"form":"(empty? [1])"}}]}
```

---

## G4-15: first, rest, last

**Examples:** 3 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 3

**form**: `(first [10 20 30])` • **expected**: `10`

**concept_phrase**: `the first of the vector`

**question_what**: `the first element`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Grace had been laying out a small collection near the meadow —
pebbles, sheep counted at sundown, marks on the slate, whatever the
day produced. Grace wrote `(first [10 20 30])` on a flat board and asked
Lou to write the form into the REPL so the village could
confirm it together.

What Clojure form computes the first element? Submit it via `eval`.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(first [10 20 30])"}}]}
```

### Record 2 — example 2 of 3

**form**: `(last  [10 20 30])` • **expected**: `30`

**concept_phrase**: `the last of the vector`

**question_what**: `the last element`

```
Every shepherd in the valley knew the danger of crying wolf for sport. This was near the hilltop.

Tom called down from a stone atop the hilltop where someone had
chalked the last of the vector on a flat board. Tom, as if the race were already won,
declared he already knew what would come back. Alex,
untroubled by what others thought, asked him to actually submit the form
`(last  [10 20 30])` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the last element.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(last  [10 20 30])"}}]}
```

### Record 3 — example 3 of 3

**form**: `(count (rest [10 20 30]))` • **expected**: `2`

**concept_phrase**: `the rest of [10 20 30] (count)`

**question_what**: `the count after removing first`

```
The boy on the hill thought the trick clever the first time he played it.

A small slate sat on a flat stone at the edge of the farm; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(count (rest [10 20 30]))`, and the page
heading read the rest of [10 20 30] (count). Frank nodded at Lou to
write the form properly so the slate would carry an honest entry.

Question: write a Clojure expression for the count after removing first.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count (rest [10 20 30]))"}}]}
```

### Record 4 — example 1 of 3

**form**: `(first [10 20 30])` • **expected**: `10`

**concept_phrase**: `the first of the vector`

**question_what**: `the first element`

```
The boy on the hill thought the trick clever the first time he played it. This was near the village.

Tom, swaggering through the underbrush, declared the collection plain.
Sam wrote `(first [10 20 30])` on a slate in the village, calmly. "It's
not about plain or fancy," they said. "It's about whether
the runtime agrees with what we think we're describing.

Write a form whose evaluation gives the first element.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(first [10 20 30])"}}]}
```

### Record 5 — example 2 of 3

**form**: `(last  [10 20 30])` • **expected**: `30`

**concept_phrase**: `the last of the vector`

**question_what**: `the last element`

```
The boy on the hill thought the trick clever the first time he played it.

George had been laying out a small collection near the orchard —
pebbles, sheep counted at sundown, marks on the slate, whatever the
day produced. George wrote `(last  [10 20 30])` on a flat board and asked
Will to write the form into the REPL so the village could
confirm it together.

Write a form whose evaluation gives the last element.

---

{"tool_calls":[{"name":"eval","args":{"form":"(last  [10 20 30])"}}]}
```

---

## G4-16: into and conj on collections

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 2

**form**: `(into [] '(1 2 3))` • **expected**: `[1, 2, 3]`

**concept_phrase**: `the form (into [] '(1 2 3))`

**question_what**: `the vector built from a list`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Halfway through the morning watch, Pat called out
by the orchard, demanding a verdict on the form `(into [] '(1 2 3))` and refusing
to descend until somebody confirmed it. Pat insisted
they already knew the answer. Sam, walking up
at an unhurried pace, simply said: "Submit the form (into [] '(1 2 3)) to the
REPL. Whatever comes back is the answer."

Write a form whose evaluation gives the vector built from a list.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] '(1 2 3))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(into #{} [1 2 2 3])` • **expected**: `[1, 2, 3]`

**concept_phrase**: `the form (into #{} [1 2 2 3])`

**question_what**: `the set built from a vector (dups removed)`

```
The boy on the hill thought the trick clever the first time he played it. All this took place near the village.

"There is no need to evaluate that," Tom said, swaggering through the underbrush.
"Anyone can see what the form (into #{} [1 2 2 3]) comes to." Alice, who
at the edge of the village had heard such claims many times, asked him to
actually write the form `(into #{} [1 2 2 3])` and submit it to the REPL —
just to be sure.

What Clojure form computes the set built from a vector (dups removed)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into #{} [1 2 2 3])"}}]}
```

### Record 3 — example 1 of 2

**form**: `(into [] '(1 2 3))` • **expected**: `[1, 2, 3]`

**concept_phrase**: `the form (into [] '(1 2 3))`

**question_what**: `the vector built from a list`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A wooden notice nailed to a post in the farm carried a small puzzle. The
riddle simply asked the reader to evaluate `(into [] '(1 2 3))`. Pat
laughed, puffed up with pride, and declared it too easy to bother with.
Bob said, patiently, that the only way to be certain of
the form (into [] '(1 2 3)) was to put it in the REPL.

Question: write a Clojure expression for the vector built from a list.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] '(1 2 3))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(into #{} [1 2 2 3])` • **expected**: `[1, 2, 3]`

**concept_phrase**: `the form (into #{} [1 2 2 3])`

**question_what**: `the set built from a vector (dups removed)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(into #{} [1 2 2 3])`, and the line
above it read the form (into #{} [1 2 2 3]). George handed the page to
Will, who, weary from the morning's effort, agreed to write it out properly.

Question: write a Clojure expression for the set built from a vector (dups removed).

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(into #{} [1 2 2 3])"}}]}
```

### Record 5 — example 1 of 2

**form**: `(into [] '(1 2 3))` • **expected**: `[1, 2, 3]`

**concept_phrase**: `the form (into [] '(1 2 3))`

**question_what**: `the vector built from a list`

```
The boy on the hill thought the trick clever the first time he played it. This was by the orchard.

Frank kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today at the edge of the orchard the next entry was
the form (into [] '(1 2 3)). Pat peered over his shoulder
at the form `(into [] '(1 2 3))` and was asked, gently, to be the one to
submit it.

Write a form whose evaluation gives the vector built from a list.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] '(1 2 3))"}}]}
```

---

## G4-17: Immutability — assoc returns new

**Examples:** 1 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 1

**form**: `(let [m {:a 1}] (assoc m :a 99) m)` • **expected**: `{':a': 1}`

**concept_phrase**: `the form showing assoc returns a new map`

**question_what**: `the original map after assoc`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place by the forest.

"There is no need to evaluate that," Will said, with a smug grin.
"Anyone can see what the form showing assoc returns a new map comes to." Grace, who
in the forest had heard such claims many times, asked him to
actually write the form `(let [m {:a 1}] (assoc m :a 99) m)` and submit it to the REPL —
just to be sure.

Question: write a Clojure expression for the original map after assoc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :a 99) m)"}}]}
```

### Record 2 — example 1 of 1

**form**: `(let [m {:a 1}] (assoc m :a 99) m)` • **expected**: `{':a': 1}`

**concept_phrase**: `the form showing assoc returns a new map`

**question_what**: `the original map after assoc`

```
Every shepherd in the valley knew the danger of crying wolf for sport. It happened near the village.

A small slate sat on a flat stone at the edge of the village; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(let [m {:a 1}] (assoc m :a 99) m)`, and the page
heading read the form showing assoc returns a new map. Frank nodded at Pat to
write the form properly so the slate would carry an honest entry.

Write a form whose evaluation gives the original map after assoc.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :a 99) m)"}}]}
```

### Record 3 — example 1 of 1

**form**: `(let [m {:a 1}] (assoc m :a 99) m)` • **expected**: `{':a': 1}`

**concept_phrase**: `the form showing assoc returns a new map`

**question_what**: `the original map after assoc`

```
The boy on the hill thought the trick clever the first time he played it.

The elder of the village kept a small slate at the edge of the meadow, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the form showing assoc returns a new map. Carol read
out the form `(let [m {:a 1}] (assoc m :a 99) m)` so Tom could write it
properly into the REPL and earn an honest mark on the slate.

Question: write a Clojure expression for the original map after assoc.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :a 99) m)"}}]}
```

### Record 4 — example 1 of 1

**form**: `(let [m {:a 1}] (assoc m :a 99) m)` • **expected**: `{':a': 1}`

**concept_phrase**: `the form showing assoc returns a new map`

**question_what**: `the original map after assoc`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened at the edge of the forest.

Carol had been trying to teach Jess how the REPL
works. "Look here," she said, pointing to the form showing assoc returns a new map.
"You hand the form `(let [m {:a 1}] (assoc m :a 99) m)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, lulled by the gentle wind, agreed to try.

Write a form whose evaluation gives the original map after assoc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :a 99) m)"}}]}
```

### Record 5 — example 1 of 1

**form**: `(let [m {:a 1}] (assoc m :a 99) m)` • **expected**: `{':a': 1}`

**concept_phrase**: `the form showing assoc returns a new map`

**question_what**: `the original map after assoc`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden notice nailed to a post by the woods carried a small puzzle. The
riddle simply asked the reader to evaluate `(let [m {:a 1}] (assoc m :a 99) m)`. Pat
laughed, swaggering through the underbrush, and declared it too easy to bother with.
Morgan said, patiently, that the only way to be certain of
the form showing assoc returns a new map was to put it in the REPL.

Write a Clojure expression that computes the original map after assoc.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :a 99) m)"}}]}
```

---

## G4-18: Equality of vectors and lists

**Examples:** 1 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 1

**form**: `(= [1 2 3] '(1 2 3))` • **expected**: `True`

**concept_phrase**: `the form (= [1 2 3] '(1 2 3))`

**question_what**: `whether vector and list with same elements are equal`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A small crowd of villagers had gathered near the meadow to watch
Pat attempt to predict, off the cuff, what the REPL would
return. Alice pointed to the form (= [1 2 3] '(1 2 3)) and read out the
form aloud: `(= [1 2 3] '(1 2 3))`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a Clojure expression that computes whether vector and list with same elements are equal.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(= [1 2 3] '(1 2 3))"}}]}
```

### Record 2 — example 1 of 1

**form**: `(= [1 2 3] '(1 2 3))` • **expected**: `True`

**concept_phrase**: `the form (= [1 2 3] '(1 2 3))`

**question_what**: `whether vector and list with same elements are equal`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened by the village.

Morgan had been laying out a small collection by the village —
pebbles, sheep counted at sundown, marks on the slate, whatever the
day produced. Morgan wrote `(= [1 2 3] '(1 2 3))` on a flat board and asked
Jess to write the form into the REPL so the village could
confirm it together.

Write a Clojure expression that computes whether vector and list with same elements are equal.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(= [1 2 3] '(1 2 3))"}}]}
```

### Record 3 — example 1 of 1

**form**: `(= [1 2 3] '(1 2 3))` • **expected**: `True`

**concept_phrase**: `the form (= [1 2 3] '(1 2 3))`

**question_what**: `whether vector and list with same elements are equal`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Sam had been laying out a small collection near the road —
pebbles, sheep counted at sundown, marks on the slate, whatever the
day produced. Sam wrote `(= [1 2 3] '(1 2 3))` on a flat board and asked
Lou to write the form into the REPL so the village could
confirm it together.

Write a form whose evaluation gives whether vector and list with same elements are equal.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(= [1 2 3] '(1 2 3))"}}]}
```

### Record 4 — example 1 of 1

**form**: `(= [1 2 3] '(1 2 3))` • **expected**: `True`

**concept_phrase**: `the form (= [1 2 3] '(1 2 3))`

**question_what**: `whether vector and list with same elements are equal`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened at the edge of the village.

Alice had been trying to teach Lou how the REPL
works. "Look here," she said, pointing to the form (= [1 2 3] '(1 2 3)).
"You hand the form `(= [1 2 3] '(1 2 3))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Lou, weary from the morning's effort, agreed to try.

Write a Clojure expression that computes whether vector and list with same elements are equal.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(= [1 2 3] '(1 2 3))"}}]}
```

### Record 5 — example 1 of 1

**form**: `(= [1 2 3] '(1 2 3))` • **expected**: `True`

**concept_phrase**: `the form (= [1 2 3] '(1 2 3))`

**question_what**: `whether vector and list with same elements are equal`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A wooden notice nailed to a post by the village carried a small puzzle. The
riddle simply asked the reader to evaluate `(= [1 2 3] '(1 2 3))`. Lou
laughed, with great whoops of laughter, and declared it too easy to bother with.
Sam said, patiently, that the only way to be certain of
the form (= [1 2 3] '(1 2 3)) was to put it in the REPL.

Write a Clojure expression that computes whether vector and list with same elements are equal.

---

I use the appropriate access function on the collection.

{"tool_calls":[{"name":"eval","args":{"form":"(= [1 2 3] '(1 2 3))"}}]}
```

---

## G4-19: range and seq

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 2

**form**: `(count (range 5))` • **expected**: `5`

**concept_phrase**: `the count of (range 5)`

**question_what**: `the count of range 0..4`

```
The boy on the hill thought the trick clever the first time he played it.

Carol had been laying out a small collection in the meadow —
pebbles, sheep counted at sundown, marks on the slate, whatever the
day produced. Carol wrote `(count (range 5))` on a flat board and asked
Jess to write the form into the REPL so the village could
confirm it together.

Write a form whose evaluation gives the count of range 0..4.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(count (range 5))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(first (range 1 100))` • **expected**: `1`

**concept_phrase**: `the first of (range 1 100)`

**question_what**: `the first of range 1..99`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Jess called down from a stone at the edge of the woods where someone had
chalked the first of (range 1 100) on a flat board. Jess, puffed up with pride,
declared she already knew what would come back. Oliver,
with steady, careful steps, asked her to actually submit the form
`(first (range 1 100))` to the REPL — the village had stopped trusting answers
that weren't checked.

What Clojure form computes the first of range 1..99? Submit it via `eval`.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(first (range 1 100))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(count (range 5))` • **expected**: `5`

**concept_phrase**: `the count of (range 5)`

**question_what**: `the count of range 0..4`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Tom, with a smug grin, declared the collection plain.
Alice wrote `(count (range 5))` on a slate atop the hilltop, calmly. "It's
not about plain or fancy," she said. "It's about whether
the runtime agrees with what we think we're describing.

Question: write a Clojure expression for the count of range 0..4.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count (range 5))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(first (range 1 100))` • **expected**: `1`

**concept_phrase**: `the first of (range 1 100)`

**question_what**: `the first of range 1..99`

```
Every shepherd in the valley knew the danger of crying wolf for sport. This was atop the hilltop.

Alex had been trying to teach Jess how the REPL
works. "Look here," they said, pointing to the first of (range 1 100).
"You hand the form `(first (range 1 100))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, weary from the morning's effort, agreed to try.

Question: write a Clojure expression for the first of range 1..99.

---

{"tool_calls":[{"name":"eval","args":{"form":"(first (range 1 100))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(count (range 5))` • **expected**: `5`

**concept_phrase**: `the count of (range 5)`

**question_what**: `the count of range 0..4`

```
Every shepherd in the valley knew the danger of crying wolf for sport. It happened near the road.

"There is no need to evaluate that," Jess said, swaggering through the underbrush.
"Anyone can see what the count of (range 5) comes to." Grace, who
on the road had heard such claims many times, asked her to
actually write the form `(count (range 5))` and submit it to the REPL —
just to be sure.

Write a form whose evaluation gives the count of range 0..4.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count (range 5))"}}]}
```

---

## G4-20: Collection vs sequence

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 2

**form**: `(count (seq [1 2 3]))` • **expected**: `3`

**concept_phrase**: `the form (count (seq [1 2 3]))`

**question_what**: `the count of seq over a vector`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened in the village.

Frank kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today in the village the next entry was
the form (count (seq [1 2 3])). Will peered over his shoulder
at the form `(count (seq [1 2 3]))` and was asked, gently, to be the one to
submit it.

What Clojure form computes the count of seq over a vector? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count (seq [1 2 3]))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(seq [])` • **expected**: `None`

**concept_phrase**: `the form (seq [])`

**question_what**: `what (seq []) returns`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

"There is no need to evaluate that," Lou said, with great whoops of laughter.
"Anyone can see what the form (seq []) comes to." George, who
in the meadow had heard such claims many times, asked her to
actually write the form `(seq [])` and submit it to the REPL —
just to be sure.

Question: write a Clojure expression for what (seq []) returns.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(seq [])"}}]}
```

### Record 3 — example 1 of 2

**form**: `(count (seq [1 2 3]))` • **expected**: `3`

**concept_phrase**: `the form (count (seq [1 2 3]))`

**question_what**: `the count of seq over a vector`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

The elder of the village kept a small slate by the farm, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the form (count (seq [1 2 3])). Bob read
out the form `(count (seq [1 2 3]))` so Will could write it
properly into the REPL and earn an honest mark on the slate.

Write a form whose evaluation gives the count of seq over a vector.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(count (seq [1 2 3]))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(seq [])` • **expected**: `None`

**concept_phrase**: `the form (seq [])`

**question_what**: `what (seq []) returns`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Alice kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today at the edge of the forest the next entry was
the form (seq []). Pat peered over her shoulder
at the form `(seq [])` and was asked, gently, to be the one to
submit it.

Write a Clojure expression that computes what (seq []) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(seq [])"}}]}
```

### Record 5 — example 1 of 2

**form**: `(count (seq [1 2 3]))` • **expected**: `3`

**concept_phrase**: `the form (count (seq [1 2 3]))`

**question_what**: `the count of seq over a vector`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

"There is no need to evaluate that," Lou said, swaggering through the underbrush.
"Anyone can see what the form (count (seq [1 2 3])) comes to." Carol, who
by the farm had heard such claims many times, asked her to
actually write the form `(count (seq [1 2 3]))` and submit it to the REPL —
just to be sure.

What Clojure form computes the count of seq over a vector? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count (seq [1 2 3]))"}}]}
```

---

