# Boy-wolf Grade 5 — deep spot-check

5 generated records per subject (across all examples and a variety of seeds). Read every record carefully. Flag anything that reads odd to a careful reader, including issues the structural audit can't catch (prose flow, contextual fit, cliché repetition, subplot/example mismatch, etc.)

---

## G5-01: if

**Examples:** 3 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 3

**form**: `(if true :a :b)` • **expected**: `':a'`

**concept_phrase**: `the form (if true :a :b)`

**question_what**: `which of :a or :b is returned`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Alice demonstrated near the woods how the same operation, applied to
many things at once, was the heart of every long calculation. The form
`(if true :a :b)` captured the form (if true :a :b), and Pat agreed
to write it for the REPL — no claims required, just the runtime's
answer.

Write a Clojure expression that computes which of :a or :b is returned.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(if true :a :b)"}}]}
```

### Record 2 — example 2 of 3

**form**: `(if false :a :b)` • **expected**: `':b'`

**concept_phrase**: `the form (if false :a :b)`

**question_what**: `which of :a or :b is returned`

```
The boy on the hill thought the trick clever the first time he played it.

Lou called down from a stone in the village where someone had
chalked the form (if false :a :b) on a flat board. Lou, puffed up with pride,
declared she already knew what would come back. Sam,
untroubled by what others thought, asked her to actually submit the form
`(if false :a :b)` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes which of :a or :b is returned.

---

{"tool_calls":[{"name":"eval","args":{"form":"(if false :a :b)"}}]}
```

### Record 3 — example 3 of 3

**form**: `(if (> 5 3) :a :b)` • **expected**: `':a'`

**concept_phrase**: `the form (if (> 5 3) :a :b)`

**question_what**: `the if's branch`

```
Every shepherd in the valley knew the danger of crying wolf for sport. This was near the road.

The elder of the village kept a small slate on the road, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the form (if (> 5 3) :a :b). George read
out the form `(if (> 5 3) :a :b)` so Tom could write it
properly into the REPL and earn an honest mark on the slate.

Question: write a Clojure expression for the if's branch.

---

{"tool_calls":[{"name":"eval","args":{"form":"(if (> 5 3) :a :b)"}}]}
```

### Record 4 — example 1 of 3

**form**: `(if true :a :b)` • **expected**: `':a'`

**concept_phrase**: `the form (if true :a :b)`

**question_what**: `which of :a or :b is returned`

```
Every shepherd in the valley knew the danger of crying wolf for sport. It happened at the edge of the village.

Frank demonstrated by the village how the same operation, applied to
many things at once, was the heart of every long calculation. The form
`(if true :a :b)` captured the form (if true :a :b), and Jess agreed
to write it for the REPL — no claims required, just the runtime's
answer.

Write a Clojure expression that computes which of :a or :b is returned.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(if true :a :b)"}}]}
```

### Record 5 — example 2 of 3

**form**: `(if false :a :b)` • **expected**: `':b'`

**concept_phrase**: `the form (if false :a :b)`

**question_what**: `which of :a or :b is returned`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A wooden notice nailed to a post near the hilltop carried a small puzzle. The
riddle simply asked the reader to evaluate `(if false :a :b)`. Tom
laughed, puffed up with pride, and declared it too easy to bother with.
Oliver said, patiently, that the only way to be certain of
the form (if false :a :b) was to put it in the REPL.

Question: write a Clojure expression for which of :a or :b is returned.

---

{"tool_calls":[{"name":"eval","args":{"form":"(if false :a :b)"}}]}
```

---

## G5-02: if as expression

**Examples:** 1 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 1

**form**: `(+ 1 (if true 10 20))` • **expected**: `11`

**concept_phrase**: `the form (+ 1 (if true 10 20))`

**question_what**: `the result of adding 1 to the if expression`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Will called down from a stone by the orchard where someone had
chalked the form (+ 1 (if true 10 20)) on a flat board. Will, with a smug grin,
declared he already knew what would come back. Morgan,
stepping deliberately, asked him to actually submit the form
`(+ 1 (if true 10 20))` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a form whose evaluation gives the result of adding 1 to the if expression.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (if true 10 20))"}}]}
```

### Record 2 — example 1 of 1

**form**: `(+ 1 (if true 10 20))` • **expected**: `11`

**concept_phrase**: `the form (+ 1 (if true 10 20))`

**question_what**: `the result of adding 1 to the if expression`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place by the woods.

Tom called down from a stone by the woods where someone had
chalked the form (+ 1 (if true 10 20)) on a flat board. Tom, boasting at every turn,
declared he already knew what would come back. Alice,
with steady, careful steps, asked him to actually submit the form
`(+ 1 (if true 10 20))` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a form whose evaluation gives the result of adding 1 to the if expression.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (if true 10 20))"}}]}
```

### Record 3 — example 1 of 1

**form**: `(+ 1 (if true 10 20))` • **expected**: `11`

**concept_phrase**: `the form (+ 1 (if true 10 20))`

**question_what**: `the result of adding 1 to the if expression`

```
The boy on the hill thought the trick clever the first time he played it. It happened by the woods.

A wooden notice nailed to a post in the woods carried a small puzzle. The
riddle simply asked the reader to evaluate `(+ 1 (if true 10 20))`. Pat
laughed, swaggering through the underbrush, and declared it too easy to bother with.
Alice said, patiently, that the only way to be certain of
the form (+ 1 (if true 10 20)) was to put it in the REPL.

Write a form whose evaluation gives the result of adding 1 to the if expression.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (if true 10 20))"}}]}
```

### Record 4 — example 1 of 1

**form**: `(+ 1 (if true 10 20))` • **expected**: `11`

**concept_phrase**: `the form (+ 1 (if true 10 20))`

**question_what**: `the result of adding 1 to the if expression`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place by the orchard.

"Same trick, repeated cleverly," Carol said near the orchard, sketching the
form `(+ 1 (if true 10 20))` into the dust. Pat, puffed up with pride, claimed to
know exactly what the form (+ 1 (if true 10 20)) would produce — but Carol
insisted, again, that the REPL was the only honest judge in the
village now.

Write a Clojure expression that computes the result of adding 1 to the if expression.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (if true 10 20))"}}]}
```

### Record 5 — example 1 of 1

**form**: `(+ 1 (if true 10 20))` • **expected**: `11`

**concept_phrase**: `the form (+ 1 (if true 10 20))`

**question_what**: `the result of adding 1 to the if expression`

```
The boy on the hill thought the trick clever the first time he played it. This was by the forest.

A small crowd of villagers had gathered at the edge of the forest to watch
Lou attempt to predict, off the cuff, what the REPL would
return. George pointed to the form (+ 1 (if true 10 20)) and read out the
form aloud: `(+ 1 (if true 10 20))`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

What Clojure form computes the result of adding 1 to the if expression? Submit it via `eval`.

---

I use map / filter / reduce as appropriate.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (if true 10 20))"}}]}
```

---

## G5-03: when

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 2

**form**: `(when true :yes)` • **expected**: `':yes'`

**concept_phrase**: `the form (when true :yes)`

**question_what**: `the value of (when true :yes)`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place at the edge of the village.

Alice had been trying to teach Will how the REPL
works. "Look here," she said, pointing to the form (when true :yes).
"You hand the form `(when true :yes)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Will, drowsy from the warm sun, agreed to try.

Write a Clojure expression that computes the value of (when true :yes).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(when true :yes)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(when false :yes)` • **expected**: `None`

**concept_phrase**: `the form (when false :yes)`

**question_what**: `the value of (when false :yes)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened near the meadow.

Oliver had been trying to teach Lou how the REPL
works. "Look here," he said, pointing to the form (when false :yes).
"You hand the form `(when false :yes)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Lou, yawning at the soft moss, agreed to try.

Write a form whose evaluation gives the value of (when false :yes).

---

I use map / filter / reduce as appropriate.

{"tool_calls":[{"name":"eval","args":{"form":"(when false :yes)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(when true :yes)` • **expected**: `':yes'`

**concept_phrase**: `the form (when true :yes)`

**question_what**: `the value of (when true :yes)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(when true :yes)`, and the line
above it read the form (when true :yes). Frank handed the page to
Pat, who, yawning at the soft moss, agreed to write it out properly.

Write a Clojure expression that computes the value of (when true :yes).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(when true :yes)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(when false :yes)` • **expected**: `None`

**concept_phrase**: `the form (when false :yes)`

**question_what**: `the value of (when false :yes)`

```
The boy on the hill thought the trick clever the first time he played it.

The elder of the village kept a small slate near the village, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the form (when false :yes). Bob read
out the form `(when false :yes)` so Will could write it
properly into the REPL and earn an honest mark on the slate.

What Clojure form computes the value of (when false :yes)? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(when false :yes)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(when true :yes)` • **expected**: `':yes'`

**concept_phrase**: `the form (when true :yes)`

**question_what**: `the value of (when true :yes)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

"Same trick, repeated cleverly," Robin said by the village, sketching the
form `(when true :yes)` into the dust. Will, boasting at every turn, claimed to
know exactly what the form (when true :yes) would produce — but Robin
insisted, again, that the REPL was the only honest judge in the
village now.

Write a Clojure expression that computes the value of (when true :yes).

---

{"tool_calls":[{"name":"eval","args":{"form":"(when true :yes)"}}]}
```

---

## G5-04: cond

**Examples:** 1 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 1

**form**: `(cond (= 1 2) :a (= 1 1) :b :else :c)` • **expected**: `':b'`

**concept_phrase**: `the cond form`

**question_what**: `which clause of the cond fires`

```
The boy on the hill thought the trick clever the first time he played it.

"Same trick, repeated cleverly," Bob said near the farm, sketching the
form `(cond (= 1 2) :a (= 1 1) :b :else :c)` into the dust. Pat, with great whoops of laughter, claimed to
know exactly what the cond form would produce — but Bob
insisted, again, that the REPL was the only honest judge in the
village now.

Write a Clojure expression that computes which clause of the cond fires.

---

I write the higher-order form so the REPL can compute.

{"tool_calls":[{"name":"eval","args":{"form":"(cond (= 1 2) :a (= 1 1) :b :else :c)"}}]}
```

### Record 2 — example 1 of 1

**form**: `(cond (= 1 2) :a (= 1 1) :b :else :c)` • **expected**: `':b'`

**concept_phrase**: `the cond form`

**question_what**: `which clause of the cond fires`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Frank kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today by the woods the next entry was
the cond form. Tom peered over his shoulder
at the form `(cond (= 1 2) :a (= 1 1) :b :else :c)` and was asked, gently, to be the one to
submit it.

What Clojure form computes which clause of the cond fires? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(cond (= 1 2) :a (= 1 1) :b :else :c)"}}]}
```

### Record 3 — example 1 of 1

**form**: `(cond (= 1 2) :a (= 1 1) :b :else :c)` • **expected**: `':b'`

**concept_phrase**: `the cond form`

**question_what**: `which clause of the cond fires`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

"There is no need to evaluate that," Tom said, swaggering through the underbrush.
"Anyone can see what the cond form comes to." Sam, who
near the road had heard such claims many times, asked him to
actually write the form `(cond (= 1 2) :a (= 1 1) :b :else :c)` and submit it to the REPL —
just to be sure.

Write a Clojure expression that computes which clause of the cond fires.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(cond (= 1 2) :a (= 1 1) :b :else :c)"}}]}
```

### Record 4 — example 1 of 1

**form**: `(cond (= 1 2) :a (= 1 1) :b :else :c)` • **expected**: `':b'`

**concept_phrase**: `the cond form`

**question_what**: `which clause of the cond fires`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A small crowd of villagers had gathered at the edge of the forest to watch
Jess attempt to predict, off the cuff, what the REPL would
return. Oliver pointed to the cond form and read out the
form aloud: `(cond (= 1 2) :a (= 1 1) :b :else :c)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a form whose evaluation gives which clause of the cond fires.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(cond (= 1 2) :a (= 1 1) :b :else :c)"}}]}
```

### Record 5 — example 1 of 1

**form**: `(cond (= 1 2) :a (= 1 1) :b :else :c)` • **expected**: `':b'`

**concept_phrase**: `the cond form`

**question_what**: `which clause of the cond fires`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place at the edge of the orchard.

Oliver kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the orchard the next entry was
the cond form. Lou peered over his shoulder
at the form `(cond (= 1 2) :a (= 1 1) :b :else :c)` and was asked, gently, to be the one to
submit it.

What Clojure form computes which clause of the cond fires? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(cond (= 1 2) :a (= 1 1) :b :else :c)"}}]}
```

---

## G5-05: cond — :else

**Examples:** 1 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 1

**form**: `(cond false :a false :b :else :c)` • **expected**: `':c'`

**concept_phrase**: `the cond falling through to :else`

**question_what**: `the :else value`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Halfway through the morning watch, Jess called out
near the hilltop, demanding a verdict on the form `(cond false :a false :b :else :c)` and refusing
to descend until somebody confirmed it. Jess insisted
she already knew the answer. Alice, walking up
at an unhurried pace, simply said: "Submit the cond falling through to :else to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the :else value.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(cond false :a false :b :else :c)"}}]}
```

### Record 2 — example 1 of 1

**form**: `(cond false :a false :b :else :c)` • **expected**: `':c'`

**concept_phrase**: `the cond falling through to :else`

**question_what**: `the :else value`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

"There is no need to evaluate that," Will said, with a smug grin.
"Anyone can see what the cond falling through to :else comes to." Alex, who
atop the hilltop had heard such claims many times, asked him to
actually write the form `(cond false :a false :b :else :c)` and submit it to the REPL —
just to be sure.

What Clojure form computes the :else value? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(cond false :a false :b :else :c)"}}]}
```

### Record 3 — example 1 of 1

**form**: `(cond false :a false :b :else :c)` • **expected**: `':c'`

**concept_phrase**: `the cond falling through to :else`

**question_what**: `the :else value`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place at the edge of the orchard.

Grace had been trying to teach Jess how the REPL
works. "Look here," she said, pointing to the cond falling through to :else.
"You hand the form `(cond false :a false :b :else :c)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, weary from the morning's effort, agreed to try.

Write a form whose evaluation gives the :else value.

---

{"tool_calls":[{"name":"eval","args":{"form":"(cond false :a false :b :else :c)"}}]}
```

### Record 4 — example 1 of 1

**form**: `(cond false :a false :b :else :c)` • **expected**: `':c'`

**concept_phrase**: `the cond falling through to :else`

**question_what**: `the :else value`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

The elder of the village kept a small slate atop the hilltop, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the cond falling through to :else. Sam read
out the form `(cond false :a false :b :else :c)` so Lou could write it
properly into the REPL and earn an honest mark on the slate.

Question: write a Clojure expression for the :else value.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(cond false :a false :b :else :c)"}}]}
```

### Record 5 — example 1 of 1

**form**: `(cond false :a false :b :else :c)` • **expected**: `':c'`

**concept_phrase**: `the cond falling through to :else`

**question_what**: `the :else value`

```
The boy on the hill thought the trick clever the first time he played it.

A wooden notice nailed to a post at the edge of the farm carried a small puzzle. The
riddle simply asked the reader to evaluate `(cond false :a false :b :else :c)`. Jess
laughed, boasting at every turn, and declared it too easy to bother with.
Carol said, patiently, that the only way to be certain of
the cond falling through to :else was to put it in the REPL.

What Clojure form computes the :else value? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(cond false :a false :b :else :c)"}}]}
```

---

## G5-06: case

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 2

**form**: `(case 2 1 :one 2 :two 3 :three :default)` • **expected**: `':two'`

**concept_phrase**: `the case form`

**question_what**: `the matched branch`

```
The boy on the hill thought the trick clever the first time he played it.

Frank demonstrated atop the hilltop how the same operation, applied to
many things at once, was the heart of every long calculation. The form
`(case 2 1 :one 2 :two 3 :three :default)` captured the case form, and Will agreed
to write it for the REPL — no claims required, just the runtime's
answer.

Write a Clojure expression that computes the matched branch.

---

{"tool_calls":[{"name":"eval","args":{"form":"(case 2 1 :one 2 :two 3 :three :default)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(case 99 1 :one 2 :two :default)` • **expected**: `':default'`

**concept_phrase**: `case falling through to default`

**question_what**: `the default branch`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Halfway through the morning watch, Pat called out
near the woods, demanding a verdict on the form `(case 99 1 :one 2 :two :default)` and refusing
to descend until somebody confirmed it. Pat insisted
they already knew the answer. Robin, walking up
at an unhurried pace, simply said: "Submit case falling through to default to the
REPL. Whatever comes back is the answer."

What Clojure form computes the default branch? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(case 99 1 :one 2 :two :default)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(case 2 1 :one 2 :two 3 :three :default)` • **expected**: `':two'`

**concept_phrase**: `the case form`

**question_what**: `the matched branch`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A wooden notice nailed to a post atop the hilltop carried a small puzzle. The
riddle simply asked the reader to evaluate `(case 2 1 :one 2 :two 3 :three :default)`. Jess
laughed, as if the race were already won, and declared it too easy to bother with.
Morgan said, patiently, that the only way to be certain of
the case form was to put it in the REPL.

Question: write a Clojure expression for the matched branch.

---

{"tool_calls":[{"name":"eval","args":{"form":"(case 2 1 :one 2 :two 3 :three :default)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(case 99 1 :one 2 :two :default)` • **expected**: `':default'`

**concept_phrase**: `case falling through to default`

**question_what**: `the default branch`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(case 99 1 :one 2 :two :default)`, and the line
above it read case falling through to default. Robin handed the page to
Pat, who, lulled by the gentle wind, agreed to write it out properly.

Write a Clojure expression that computes the default branch.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(case 99 1 :one 2 :two :default)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(case 2 1 :one 2 :two 3 :three :default)` • **expected**: `':two'`

**concept_phrase**: `the case form`

**question_what**: `the matched branch`

```
Every shepherd in the valley knew the danger of crying wolf for sport. It happened along the road.

A small slate sat on a flat stone near the road; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(case 2 1 :one 2 :two 3 :three :default)`, and the page
heading read the case form. George nodded at Will to
write the form properly so the slate would carry an honest entry.

What Clojure form computes the matched branch? Submit it via `eval`.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(case 2 1 :one 2 :two 3 :three :default)"}}]}
```

---

## G5-07: and / or as control flow

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 2

**form**: `(and 1 2 3)` • **expected**: `3`

**concept_phrase**: `the form (and 1 2 3) returns last truthy`

**question_what**: `the last truthy value`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A small crowd of villagers had gathered by the woods to watch
Tom attempt to predict, off the cuff, what the REPL would
return. Robin pointed to the form (and 1 2 3) returns last truthy and read out the
form aloud: `(and 1 2 3)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

What Clojure form computes the last truthy value? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(and 1 2 3)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(or nil false :found)` • **expected**: `':found'`

**concept_phrase**: `the form (or nil false :found)`

**question_what**: `the first truthy value`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place near the meadow.

A wooden notice nailed to a post by the meadow carried a small puzzle. The
riddle simply asked the reader to evaluate `(or nil false :found)`. Jess
laughed, puffed up with pride, and declared it too easy to bother with.
Oliver said, patiently, that the only way to be certain of
the form (or nil false :found) was to put it in the REPL.

Write a Clojure expression that computes the first truthy value.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(or nil false :found)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(and 1 2 3)` • **expected**: `3`

**concept_phrase**: `the form (and 1 2 3) returns last truthy`

**question_what**: `the last truthy value`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place on the hilltop.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(and 1 2 3)`, and the line
above it read the form (and 1 2 3) returns last truthy. Oliver handed the page to
Will, who, her legs heavy from sprinting, agreed to write it out properly.

What Clojure form computes the last truthy value? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(and 1 2 3)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(or nil false :found)` • **expected**: `':found'`

**concept_phrase**: `the form (or nil false :found)`

**question_what**: `the first truthy value`

```
The boy on the hill thought the trick clever the first time he played it.

The elder of the village kept a small slate in the forest, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the form (or nil false :found). Oliver read
out the form `(or nil false :found)` so Jess could write it
properly into the REPL and earn an honest mark on the slate.

Write a Clojure expression that computes the first truthy value.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(or nil false :found)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(and 1 2 3)` • **expected**: `3`

**concept_phrase**: `the form (and 1 2 3) returns last truthy`

**question_what**: `the last truthy value`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A small slate sat on a flat stone near the farm; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(and 1 2 3)`, and the page
heading read the form (and 1 2 3) returns last truthy. George nodded at Jess to
write the form properly so the slate would carry an honest entry.

What Clojure form computes the last truthy value? Submit it via `eval`.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(and 1 2 3)"}}]}
```

---

## G5-08: not

**Examples:** 1 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 1

**form**: `(not (> 1 2))` • **expected**: `True`

**concept_phrase**: `the form (not (> 1 2))`

**question_what**: `the negated comparison`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened near the orchard.

Oliver demonstrated in the orchard how the same operation, applied to
many things at once, was the heart of every long calculation. The form
`(not (> 1 2))` captured the form (not (> 1 2)), and Tom agreed
to write it for the REPL — no claims required, just the runtime's
answer.

Write a form whose evaluation gives the negated comparison.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(not (> 1 2))"}}]}
```

### Record 2 — example 1 of 1

**form**: `(not (> 1 2))` • **expected**: `True`

**concept_phrase**: `the form (not (> 1 2))`

**question_what**: `the negated comparison`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Halfway through the morning watch, Tom called out
at the edge of the village, demanding a verdict on the form `(not (> 1 2))` and refusing
to descend until somebody confirmed it. Tom insisted
he already knew the answer. Oliver, walking up
at an unhurried pace, simply said: "Submit the form (not (> 1 2)) to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the negated comparison.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(not (> 1 2))"}}]}
```

### Record 3 — example 1 of 1

**form**: `(not (> 1 2))` • **expected**: `True`

**concept_phrase**: `the form (not (> 1 2))`

**question_what**: `the negated comparison`

```
The boy on the hill thought the trick clever the first time he played it. It happened at the edge of the farm.

A wooden notice nailed to a post near the farm carried a small puzzle. The
riddle simply asked the reader to evaluate `(not (> 1 2))`. Will
laughed, as if the race were already won, and declared it too easy to bother with.
Grace said, patiently, that the only way to be certain of
the form (not (> 1 2)) was to put it in the REPL.

Write a Clojure expression that computes the negated comparison.

---

{"tool_calls":[{"name":"eval","args":{"form":"(not (> 1 2))"}}]}
```

### Record 4 — example 1 of 1

**form**: `(not (> 1 2))` • **expected**: `True`

**concept_phrase**: `the form (not (> 1 2))`

**question_what**: `the negated comparison`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Sam had been trying to teach Lou how the REPL
works. "Look here," they said, pointing to the form (not (> 1 2)).
"You hand the form `(not (> 1 2))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Lou, drowsy from the warm sun, agreed to try.

Write a Clojure expression that computes the negated comparison.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(not (> 1 2))"}}]}
```

### Record 5 — example 1 of 1

**form**: `(not (> 1 2))` • **expected**: `True`

**concept_phrase**: `the form (not (> 1 2))`

**question_what**: `the negated comparison`

```
The boy on the hill thought the trick clever the first time he played it.

"There is no need to evaluate that," Pat said, with great whoops of laughter.
"Anyone can see what the form (not (> 1 2)) comes to." Oliver, who
by the orchard had heard such claims many times, asked them to
actually write the form `(not (> 1 2))` and submit it to the REPL —
just to be sure.

Write a Clojure expression that computes the negated comparison.

---

{"tool_calls":[{"name":"eval","args":{"form":"(not (> 1 2))"}}]}
```

---

## G5-09: fn as value

**Examples:** 1 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 1

**form**: `((fn [f x] (f (f x))) inc 5)` • **expected**: `7`

**concept_phrase**: `applying f twice to x where f is inc`

**question_what**: `the result of inc applied twice`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place in the woods.

Halfway through the morning watch, Will called out
at the edge of the woods, demanding a verdict on the form `((fn [f x] (f (f x))) inc 5)` and refusing
to descend until somebody confirmed it. Will insisted
he already knew the answer. George, walking up
at an unhurried pace, simply said: "Submit applying f twice to x where f is inc to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the result of inc applied twice.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [f x] (f (f x))) inc 5)"}}]}
```

### Record 2 — example 1 of 1

**form**: `((fn [f x] (f (f x))) inc 5)` • **expected**: `7`

**concept_phrase**: `applying f twice to x where f is inc`

**question_what**: `the result of inc applied twice`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened by the orchard.

A small crowd of villagers had gathered near the orchard to watch
Jess attempt to predict, off the cuff, what the REPL would
return. Sam pointed to applying f twice to x where f is inc and read out the
form aloud: `((fn [f x] (f (f x))) inc 5)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

What Clojure form computes the result of inc applied twice? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [f x] (f (f x))) inc 5)"}}]}
```

### Record 3 — example 1 of 1

**form**: `((fn [f x] (f (f x))) inc 5)` • **expected**: `7`

**concept_phrase**: `applying f twice to x where f is inc`

**question_what**: `the result of inc applied twice`

```
The boy on the hill thought the trick clever the first time he played it.

"Same trick, repeated cleverly," Morgan said in the orchard, sketching the
form `((fn [f x] (f (f x))) inc 5)` into the dust. Jess, with great whoops of laughter, claimed to
know exactly what applying f twice to x where f is inc would produce — but Morgan
insisted, again, that the REPL was the only honest judge in the
village now.

Write a Clojure expression that computes the result of inc applied twice.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [f x] (f (f x))) inc 5)"}}]}
```

### Record 4 — example 1 of 1

**form**: `((fn [f x] (f (f x))) inc 5)` • **expected**: `7`

**concept_phrase**: `applying f twice to x where f is inc`

**question_what**: `the result of inc applied twice`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place on the road.

Halfway through the morning watch, Tom called out
along the road, demanding a verdict on the form `((fn [f x] (f (f x))) inc 5)` and refusing
to descend until somebody confirmed it. Tom insisted
he already knew the answer. Sam, walking up
at an unhurried pace, simply said: "Submit applying f twice to x where f is inc to the
REPL. Whatever comes back is the answer."

Write a Clojure expression that computes the result of inc applied twice.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [f x] (f (f x))) inc 5)"}}]}
```

### Record 5 — example 1 of 1

**form**: `((fn [f x] (f (f x))) inc 5)` • **expected**: `7`

**concept_phrase**: `applying f twice to x where f is inc`

**question_what**: `the result of inc applied twice`

```
The boy on the hill thought the trick clever the first time he played it.

A small crowd of villagers had gathered by the woods to watch
Tom attempt to predict, off the cuff, what the REPL would
return. George pointed to applying f twice to x where f is inc and read out the
form aloud: `((fn [f x] (f (f x))) inc 5)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Question: write a Clojure expression for the result of inc applied twice.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [f x] (f (f x))) inc 5)"}}]}
```

---

## G5-10: map

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 2

**form**: `(map inc [1 2 3])` • **expected**: `[2, 3, 4]`

**concept_phrase**: `the form (map inc [1 2 3])`

**question_what**: `[1 2 3] each incremented`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Lou called down from a stone atop the hilltop where someone had
chalked the form (map inc [1 2 3]) on a flat board. Lou, boasting at every turn,
declared she already knew what would come back. Grace,
with steady, careful steps, asked her to actually submit the form
`(map inc [1 2 3])` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes [1 2 3] each incremented.

---

{"tool_calls":[{"name":"eval","args":{"form":"(map inc [1 2 3])"}}]}
```

### Record 2 — example 2 of 2

**form**: `(map #(* % %) [1 2 3 4])` • **expected**: `[1, 4, 9, 16]`

**concept_phrase**: `the form (map #(* % %) [1 2 3 4])`

**question_what**: `[1 2 3 4] each squared`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. This was near the orchard.

"There is no need to evaluate that," Pat said, with a smug grin.
"Anyone can see what the form (map #(* % %) [1 2 3 4]) comes to." Carol, who
near the orchard had heard such claims many times, asked them to
actually write the form `(map #(* % %) [1 2 3 4])` and submit it to the REPL —
just to be sure.

Question: write a Clojure expression for [1 2 3 4] each squared.

---

{"tool_calls":[{"name":"eval","args":{"form":"(map #(* % %) [1 2 3 4])"}}]}
```

### Record 3 — example 1 of 2

**form**: `(map inc [1 2 3])` • **expected**: `[2, 3, 4]`

**concept_phrase**: `the form (map inc [1 2 3])`

**question_what**: `[1 2 3] each incremented`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Alice had been trying to teach Tom how the REPL
works. "Look here," she said, pointing to the form (map inc [1 2 3]).
"You hand the form `(map inc [1 2 3])` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Tom, drowsy from the warm sun, agreed to try.

What Clojure form computes [1 2 3] each incremented? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(map inc [1 2 3])"}}]}
```

### Record 4 — example 2 of 2

**form**: `(map #(* % %) [1 2 3 4])` • **expected**: `[1, 4, 9, 16]`

**concept_phrase**: `the form (map #(* % %) [1 2 3 4])`

**question_what**: `[1 2 3 4] each squared`

```
The boy on the hill thought the trick clever the first time he played it. This was along the road.

"Same trick, repeated cleverly," Alice said along the road, sketching the
form `(map #(* % %) [1 2 3 4])` into the dust. Tom, puffed up with pride, claimed to
know exactly what the form (map #(* % %) [1 2 3 4]) would produce — but Alice
insisted, again, that the REPL was the only honest judge in the
village now.

Question: write a Clojure expression for [1 2 3 4] each squared.

---

{"tool_calls":[{"name":"eval","args":{"form":"(map #(* % %) [1 2 3 4])"}}]}
```

### Record 5 — example 1 of 2

**form**: `(map inc [1 2 3])` • **expected**: `[2, 3, 4]`

**concept_phrase**: `the form (map inc [1 2 3])`

**question_what**: `[1 2 3] each incremented`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

"Same trick, repeated cleverly," Robin said by the farm, sketching the
form `(map inc [1 2 3])` into the dust. Tom, with a smug grin, claimed to
know exactly what the form (map inc [1 2 3]) would produce — but Robin
insisted, again, that the REPL was the only honest judge in the
village now.

Write a form whose evaluation gives [1 2 3] each incremented.

---

{"tool_calls":[{"name":"eval","args":{"form":"(map inc [1 2 3])"}}]}
```

---

## G5-11: filter

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 2

**form**: `(filter even? [1 2 3 4])` • **expected**: `[2, 4]`

**concept_phrase**: `the form (filter even? [1 2 3 4])`

**question_what**: `the even numbers from [1 2 3 4]`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened in the meadow.

Halfway through the morning watch, Will called out
in the meadow, demanding a verdict on the form `(filter even? [1 2 3 4])` and refusing
to descend until somebody confirmed it. Will insisted
he already knew the answer. Bob, walking up
at an unhurried pace, simply said: "Submit the form (filter even? [1 2 3 4]) to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the even numbers from [1 2 3 4].

---

{"tool_calls":[{"name":"eval","args":{"form":"(filter even? [1 2 3 4])"}}]}
```

### Record 2 — example 2 of 2

**form**: `(filter pos? [-2 -1 0 1 2])` • **expected**: `[1, 2]`

**concept_phrase**: `the form (filter pos? ...)`

**question_what**: `the positive numbers`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place near the road.

A small slate sat on a flat stone near the road; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(filter pos? [-2 -1 0 1 2])`, and the page
heading read the form (filter pos? ...). Sam nodded at Jess to
write the form properly so the slate would carry an honest entry.

Write a Clojure expression that computes the positive numbers.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(filter pos? [-2 -1 0 1 2])"}}]}
```

### Record 3 — example 1 of 2

**form**: `(filter even? [1 2 3 4])` • **expected**: `[2, 4]`

**concept_phrase**: `the form (filter even? [1 2 3 4])`

**question_what**: `the even numbers from [1 2 3 4]`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A wooden notice nailed to a post in the village carried a small puzzle. The
riddle simply asked the reader to evaluate `(filter even? [1 2 3 4])`. Will
laughed, with great whoops of laughter, and declared it too easy to bother with.
Alex said, patiently, that the only way to be certain of
the form (filter even? [1 2 3 4]) was to put it in the REPL.

Write a Clojure expression that computes the even numbers from [1 2 3 4].

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(filter even? [1 2 3 4])"}}]}
```

### Record 4 — example 2 of 2

**form**: `(filter pos? [-2 -1 0 1 2])` • **expected**: `[1, 2]`

**concept_phrase**: `the form (filter pos? ...)`

**question_what**: `the positive numbers`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. This was on the road.

"There is no need to evaluate that," Lou said, with great whoops of laughter.
"Anyone can see what the form (filter pos? ...) comes to." George, who
on the road had heard such claims many times, asked her to
actually write the form `(filter pos? [-2 -1 0 1 2])` and submit it to the REPL —
just to be sure.

What Clojure form computes the positive numbers? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(filter pos? [-2 -1 0 1 2])"}}]}
```

### Record 5 — example 1 of 2

**form**: `(filter even? [1 2 3 4])` • **expected**: `[2, 4]`

**concept_phrase**: `the form (filter even? [1 2 3 4])`

**question_what**: `the even numbers from [1 2 3 4]`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place by the orchard.

A small crowd of villagers had gathered near the orchard to watch
Lou attempt to predict, off the cuff, what the REPL would
return. Carol pointed to the form (filter even? [1 2 3 4]) and read out the
form aloud: `(filter even? [1 2 3 4])`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a form whose evaluation gives the even numbers from [1 2 3 4].

---

I use map / filter / reduce as appropriate.

{"tool_calls":[{"name":"eval","args":{"form":"(filter even? [1 2 3 4])"}}]}
```

---

## G5-12: reduce

**Examples:** 3 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 3

**form**: `(reduce + [1 2 3 4])` • **expected**: `10`

**concept_phrase**: `the form (reduce + [1 2 3 4])`

**question_what**: `the sum`

```
The boy on the hill thought the trick clever the first time he played it. This was near the orchard.

Grace kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the orchard the next entry was
the form (reduce + [1 2 3 4]). Jess peered over her shoulder
at the form `(reduce + [1 2 3 4])` and was asked, gently, to be the one to
submit it.

Write a Clojure expression that computes the sum.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + [1 2 3 4])"}}]}
```

### Record 2 — example 2 of 3

**form**: `(reduce * [1 2 3 4 5])` • **expected**: `120`

**concept_phrase**: `the form (reduce * [1 2 3 4 5])`

**question_what**: `5!`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Robin kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today in the meadow the next entry was
the form (reduce * [1 2 3 4 5]). Tom peered over their shoulder
at the form `(reduce * [1 2 3 4 5])` and was asked, gently, to be the one to
submit it.

Question: write a Clojure expression for 5!.

---

{"tool_calls":[{"name":"eval","args":{"form":"(reduce * [1 2 3 4 5])"}}]}
```

### Record 3 — example 3 of 3

**form**: `(reduce max [3 1 4 1 5 9 2 6])` • **expected**: `9`

**concept_phrase**: `the form (reduce max [...])`

**question_what**: `the maximum`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Halfway through the morning watch, Lou called out
by the village, demanding a verdict on the form `(reduce max [3 1 4 1 5 9 2 6])` and refusing
to descend until somebody confirmed it. Lou insisted
she already knew the answer. Oliver, walking up
at an unhurried pace, simply said: "Submit the form (reduce max [...]) to the
REPL. Whatever comes back is the answer."

Write a form whose evaluation gives the maximum.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(reduce max [3 1 4 1 5 9 2 6])"}}]}
```

### Record 4 — example 1 of 3

**form**: `(reduce + [1 2 3 4])` • **expected**: `10`

**concept_phrase**: `the form (reduce + [1 2 3 4])`

**question_what**: `the sum`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened at the edge of the orchard.

Lou called down from a stone at the edge of the orchard where someone had
chalked the form (reduce + [1 2 3 4]) on a flat board. Lou, puffed up with pride,
declared she already knew what would come back. Morgan,
saying very little, asked her to actually submit the form
`(reduce + [1 2 3 4])` to the REPL — the village had stopped trusting answers
that weren't checked.

Question: write a Clojure expression for the sum.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + [1 2 3 4])"}}]}
```

### Record 5 — example 2 of 3

**form**: `(reduce * [1 2 3 4 5])` • **expected**: `120`

**concept_phrase**: `the form (reduce * [1 2 3 4 5])`

**question_what**: `5!`

```
The boy on the hill thought the trick clever the first time he played it. This was by the village.

"There is no need to evaluate that," Tom said, swaggering through the underbrush.
"Anyone can see what the form (reduce * [1 2 3 4 5]) comes to." George, who
near the village had heard such claims many times, asked him to
actually write the form `(reduce * [1 2 3 4 5])` and submit it to the REPL —
just to be sure.

What Clojure form computes 5!? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(reduce * [1 2 3 4 5])"}}]}
```

---

## G5-13: reduce with init

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 2

**form**: `(reduce + 100 [1 2 3])` • **expected**: `106`

**concept_phrase**: `the form (reduce + 100 [1 2 3])`

**question_what**: `100 + sum of [1 2 3]`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden notice nailed to a post at the edge of the woods carried a small puzzle. The
riddle simply asked the reader to evaluate `(reduce + 100 [1 2 3])`. Pat
laughed, with great whoops of laughter, and declared it too easy to bother with.
Sam said, patiently, that the only way to be certain of
the form (reduce + 100 [1 2 3]) was to put it in the REPL.

Write a Clojure expression that computes 100 + sum of [1 2 3].

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + 100 [1 2 3])"}}]}
```

### Record 2 — example 2 of 2

**form**: `(reduce + 0 [])` • **expected**: `0`

**concept_phrase**: `the form (reduce + 0 [])`

**question_what**: `the value when reducing over empty seq with init 0`

```
The boy on the hill thought the trick clever the first time he played it.

George kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today in the forest the next entry was
the form (reduce + 0 []). Jess peered over his shoulder
at the form `(reduce + 0 [])` and was asked, gently, to be the one to
submit it.

Write a Clojure expression that computes the value when reducing over empty seq with init 0.

---

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + 0 [])"}}]}
```

### Record 3 — example 1 of 2

**form**: `(reduce + 100 [1 2 3])` • **expected**: `106`

**concept_phrase**: `the form (reduce + 100 [1 2 3])`

**question_what**: `100 + sum of [1 2 3]`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened at the edge of the farm.

Bob had been trying to teach Tom how the REPL
works. "Look here," he said, pointing to the form (reduce + 100 [1 2 3]).
"You hand the form `(reduce + 100 [1 2 3])` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Tom, drowsy from the warm sun, agreed to try.

What Clojure form computes 100 + sum of [1 2 3]? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + 100 [1 2 3])"}}]}
```

### Record 4 — example 2 of 2

**form**: `(reduce + 0 [])` • **expected**: `0`

**concept_phrase**: `the form (reduce + 0 [])`

**question_what**: `the value when reducing over empty seq with init 0`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. This was at the edge of the forest.

Lou called down from a stone near the forest where someone had
chalked the form (reduce + 0 []) on a flat board. Lou, with a smug grin,
declared she already knew what would come back. Morgan,
stepping deliberately, asked her to actually submit the form
`(reduce + 0 [])` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the value when reducing over empty seq with init 0.

---

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + 0 [])"}}]}
```

### Record 5 — example 1 of 2

**form**: `(reduce + 100 [1 2 3])` • **expected**: `106`

**concept_phrase**: `the form (reduce + 100 [1 2 3])`

**question_what**: `100 + sum of [1 2 3]`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Lou called down from a stone near the woods where someone had
chalked the form (reduce + 100 [1 2 3]) on a flat board. Lou, boasting at every turn,
declared she already knew what would come back. Alex,
stepping deliberately, asked her to actually submit the form
`(reduce + 100 [1 2 3])` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes 100 + sum of [1 2 3].

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + 100 [1 2 3])"}}]}
```

---

## G5-14: apply

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 2

**form**: `(apply + [1 2 3 4])` • **expected**: `10`

**concept_phrase**: `the form (apply + [1 2 3 4])`

**question_what**: `+ applied to the elements of the vector`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Carol had been trying to teach Jess how the REPL
works. "Look here," she said, pointing to the form (apply + [1 2 3 4]).
"You hand the form `(apply + [1 2 3 4])` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, lulled by the gentle wind, agreed to try.

Question: write a Clojure expression for + applied to the elements of the vector.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(apply + [1 2 3 4])"}}]}
```

### Record 2 — example 2 of 2

**form**: `(apply max [3 1 4 1 5])` • **expected**: `5`

**concept_phrase**: `the form (apply max ...)`

**question_what**: `max of the vector via apply`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. This was along the road.

A wooden notice nailed to a post along the road carried a small puzzle. The
riddle simply asked the reader to evaluate `(apply max [3 1 4 1 5])`. Pat
laughed, with a smug grin, and declared it too easy to bother with.
Grace said, patiently, that the only way to be certain of
the form (apply max ...) was to put it in the REPL.

Question: write a Clojure expression for max of the vector via apply.

---

{"tool_calls":[{"name":"eval","args":{"form":"(apply max [3 1 4 1 5])"}}]}
```

### Record 3 — example 1 of 2

**form**: `(apply + [1 2 3 4])` • **expected**: `10`

**concept_phrase**: `the form (apply + [1 2 3 4])`

**question_what**: `+ applied to the elements of the vector`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Morgan had been trying to teach Will how the REPL
works. "Look here," they said, pointing to the form (apply + [1 2 3 4]).
"You hand the form `(apply + [1 2 3 4])` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Will, yawning at the soft moss, agreed to try.

Question: write a Clojure expression for + applied to the elements of the vector.

---

{"tool_calls":[{"name":"eval","args":{"form":"(apply + [1 2 3 4])"}}]}
```

### Record 4 — example 2 of 2

**form**: `(apply max [3 1 4 1 5])` • **expected**: `5`

**concept_phrase**: `the form (apply max ...)`

**question_what**: `max of the vector via apply`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

"There is no need to evaluate that," Tom said, with a smug grin.
"Anyone can see what the form (apply max ...) comes to." Alice, who
at the edge of the farm had heard such claims many times, asked him to
actually write the form `(apply max [3 1 4 1 5])` and submit it to the REPL —
just to be sure.

Write a Clojure expression that computes max of the vector via apply.

---

{"tool_calls":[{"name":"eval","args":{"form":"(apply max [3 1 4 1 5])"}}]}
```

### Record 5 — example 1 of 2

**form**: `(apply + [1 2 3 4])` • **expected**: `10`

**concept_phrase**: `the form (apply + [1 2 3 4])`

**question_what**: `+ applied to the elements of the vector`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Halfway through the morning watch, Jess called out
near the woods, demanding a verdict on the form `(apply + [1 2 3 4])` and refusing
to descend until somebody confirmed it. Jess insisted
she already knew the answer. Grace, walking up
at an unhurried pace, simply said: "Submit the form (apply + [1 2 3 4]) to the
REPL. Whatever comes back is the answer."

What Clojure form computes + applied to the elements of the vector? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(apply + [1 2 3 4])"}}]}
```

---

## G5-15: comp

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 2

**form**: `((comp inc inc) 5)` • **expected**: `7`

**concept_phrase**: `the form ((comp inc inc) 5)`

**question_what**: `inc twice applied to 5`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Grace demonstrated near the meadow how the same operation, applied to
many things at once, was the heart of every long calculation. The form
`((comp inc inc) 5)` captured the form ((comp inc inc) 5), and Lou agreed
to write it for the REPL — no claims required, just the runtime's
answer.

What Clojure form computes inc twice applied to 5? Submit it via `eval`.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"((comp inc inc) 5)"}}]}
```

### Record 2 — example 2 of 2

**form**: `((comp str inc) 9)` • **expected**: `'10'`

**concept_phrase**: `the form ((comp str inc) 9)`

**question_what**: `inc then str of 9`

```
Every shepherd in the valley knew the danger of crying wolf for sport. This was near the hilltop.

Tom called down from a stone atop the hilltop where someone had
chalked the form ((comp str inc) 9) on a flat board. Tom, as if the race were already won,
declared he already knew what would come back. Alex,
untroubled by what others thought, asked him to actually submit the form
`((comp str inc) 9)` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes inc then str of 9.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"((comp str inc) 9)"}}]}
```

### Record 3 — example 1 of 2

**form**: `((comp inc inc) 5)` • **expected**: `7`

**concept_phrase**: `the form ((comp inc inc) 5)`

**question_what**: `inc twice applied to 5`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A wooden notice nailed to a post near the orchard carried a small puzzle. The
riddle simply asked the reader to evaluate `((comp inc inc) 5)`. Lou
laughed, boasting at every turn, and declared it too easy to bother with.
George said, patiently, that the only way to be certain of
the form ((comp inc inc) 5) was to put it in the REPL.

Write a Clojure expression that computes inc twice applied to 5.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"((comp inc inc) 5)"}}]}
```

### Record 4 — example 2 of 2

**form**: `((comp str inc) 9)` • **expected**: `'10'`

**concept_phrase**: `the form ((comp str inc) 9)`

**question_what**: `inc then str of 9`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A wooden notice nailed to a post near the meadow carried a small puzzle. The
riddle simply asked the reader to evaluate `((comp str inc) 9)`. Will
laughed, swaggering through the underbrush, and declared it too easy to bother with.
Frank said, patiently, that the only way to be certain of
the form ((comp str inc) 9) was to put it in the REPL.

Question: write a Clojure expression for inc then str of 9.

---

{"tool_calls":[{"name":"eval","args":{"form":"((comp str inc) 9)"}}]}
```

### Record 5 — example 1 of 2

**form**: `((comp inc inc) 5)` • **expected**: `7`

**concept_phrase**: `the form ((comp inc inc) 5)`

**question_what**: `inc twice applied to 5`

```
The boy on the hill thought the trick clever the first time he played it. All this took place in the village.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `((comp inc inc) 5)`, and the line
above it read the form ((comp inc inc) 5). Carol handed the page to
Jess, who, her legs heavy from sprinting, agreed to write it out properly.

Write a Clojure expression that computes inc twice applied to 5.

---

{"tool_calls":[{"name":"eval","args":{"form":"((comp inc inc) 5)"}}]}
```

---

## G5-16: partial

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 2

**form**: `((partial + 10) 5)` • **expected**: `15`

**concept_phrase**: `the form ((partial + 10) 5)`

**question_what**: `10 + 5`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Halfway through the morning watch, Pat called out
by the orchard, demanding a verdict on the form `((partial + 10) 5)` and refusing
to descend until somebody confirmed it. Pat insisted
they already knew the answer. Sam, walking up
at an unhurried pace, simply said: "Submit the form ((partial + 10) 5) to the
REPL. Whatever comes back is the answer."

Write a form whose evaluation gives 10 + 5.

---

{"tool_calls":[{"name":"eval","args":{"form":"((partial + 10) 5)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(map (partial * 3) [1 2 3])` • **expected**: `[3, 6, 9]`

**concept_phrase**: `(partial * 3) mapped over [1 2 3]`

**question_what**: `each element times 3`

```
The boy on the hill thought the trick clever the first time he played it. All this took place near the village.

"There is no need to evaluate that," Tom said, swaggering through the underbrush.
"Anyone can see what (partial * 3) mapped over [1 2 3] comes to." Alice, who
at the edge of the village had heard such claims many times, asked him to
actually write the form `(map (partial * 3) [1 2 3])` and submit it to the REPL —
just to be sure.

What Clojure form computes each element times 3? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(map (partial * 3) [1 2 3])"}}]}
```

### Record 3 — example 1 of 2

**form**: `((partial + 10) 5)` • **expected**: `15`

**concept_phrase**: `the form ((partial + 10) 5)`

**question_what**: `10 + 5`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A wooden notice nailed to a post in the farm carried a small puzzle. The
riddle simply asked the reader to evaluate `((partial + 10) 5)`. Pat
laughed, puffed up with pride, and declared it too easy to bother with.
Bob said, patiently, that the only way to be certain of
the form ((partial + 10) 5) was to put it in the REPL.

Question: write a Clojure expression for 10 + 5.

---

{"tool_calls":[{"name":"eval","args":{"form":"((partial + 10) 5)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(map (partial * 3) [1 2 3])` • **expected**: `[3, 6, 9]`

**concept_phrase**: `(partial * 3) mapped over [1 2 3]`

**question_what**: `each element times 3`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(map (partial * 3) [1 2 3])`, and the line
above it read (partial * 3) mapped over [1 2 3]. George handed the page to
Will, who, weary from the morning's effort, agreed to write it out properly.

Question: write a Clojure expression for each element times 3.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(map (partial * 3) [1 2 3])"}}]}
```

### Record 5 — example 1 of 2

**form**: `((partial + 10) 5)` • **expected**: `15`

**concept_phrase**: `the form ((partial + 10) 5)`

**question_what**: `10 + 5`

```
The boy on the hill thought the trick clever the first time he played it. This was by the orchard.

Frank kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today at the edge of the orchard the next entry was
the form ((partial + 10) 5). Pat peered over his shoulder
at the form `((partial + 10) 5)` and was asked, gently, to be the one to
submit it.

Write a form whose evaluation gives 10 + 5.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"((partial + 10) 5)"}}]}
```

---

## G5-17: juxt

**Examples:** 1 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 1

**form**: `((juxt inc dec) 5)` • **expected**: `[6, 4]`

**concept_phrase**: `the form ((juxt inc dec) 5)`

**question_what**: `inc and dec of 5 in parallel`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place by the forest.

"There is no need to evaluate that," Will said, with a smug grin.
"Anyone can see what the form ((juxt inc dec) 5) comes to." Grace, who
in the forest had heard such claims many times, asked him to
actually write the form `((juxt inc dec) 5)` and submit it to the REPL —
just to be sure.

Question: write a Clojure expression for inc and dec of 5 in parallel.

---

{"tool_calls":[{"name":"eval","args":{"form":"((juxt inc dec) 5)"}}]}
```

### Record 2 — example 1 of 1

**form**: `((juxt inc dec) 5)` • **expected**: `[6, 4]`

**concept_phrase**: `the form ((juxt inc dec) 5)`

**question_what**: `inc and dec of 5 in parallel`

```
Every shepherd in the valley knew the danger of crying wolf for sport. It happened near the village.

A small slate sat on a flat stone at the edge of the village; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `((juxt inc dec) 5)`, and the page
heading read the form ((juxt inc dec) 5). Frank nodded at Pat to
write the form properly so the slate would carry an honest entry.

Write a form whose evaluation gives inc and dec of 5 in parallel.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"((juxt inc dec) 5)"}}]}
```

### Record 3 — example 1 of 1

**form**: `((juxt inc dec) 5)` • **expected**: `[6, 4]`

**concept_phrase**: `the form ((juxt inc dec) 5)`

**question_what**: `inc and dec of 5 in parallel`

```
The boy on the hill thought the trick clever the first time he played it.

The elder of the village kept a small slate at the edge of the meadow, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the form ((juxt inc dec) 5). Carol read
out the form `((juxt inc dec) 5)` so Tom could write it
properly into the REPL and earn an honest mark on the slate.

Question: write a Clojure expression for inc and dec of 5 in parallel.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"((juxt inc dec) 5)"}}]}
```

### Record 4 — example 1 of 1

**form**: `((juxt inc dec) 5)` • **expected**: `[6, 4]`

**concept_phrase**: `the form ((juxt inc dec) 5)`

**question_what**: `inc and dec of 5 in parallel`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened at the edge of the forest.

Carol had been trying to teach Jess how the REPL
works. "Look here," she said, pointing to the form ((juxt inc dec) 5).
"You hand the form `((juxt inc dec) 5)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, lulled by the gentle wind, agreed to try.

Write a form whose evaluation gives inc and dec of 5 in parallel.

---

{"tool_calls":[{"name":"eval","args":{"form":"((juxt inc dec) 5)"}}]}
```

### Record 5 — example 1 of 1

**form**: `((juxt inc dec) 5)` • **expected**: `[6, 4]`

**concept_phrase**: `the form ((juxt inc dec) 5)`

**question_what**: `inc and dec of 5 in parallel`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden notice nailed to a post by the woods carried a small puzzle. The
riddle simply asked the reader to evaluate `((juxt inc dec) 5)`. Pat
laughed, swaggering through the underbrush, and declared it too easy to bother with.
Morgan said, patiently, that the only way to be certain of
the form ((juxt inc dec) 5) was to put it in the REPL.

Write a Clojure expression that computes inc and dec of 5 in parallel.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"((juxt inc dec) 5)"}}]}
```

---

## G5-18: some

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 2

**form**: `(some even? [1 3 5 8 7])` • **expected**: `True`

**concept_phrase**: `the form (some even? [...])`

**question_what**: `whether any element is even`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A small crowd of villagers had gathered near the meadow to watch
Pat attempt to predict, off the cuff, what the REPL would
return. Alice pointed to the form (some even? [...]) and read out the
form aloud: `(some even? [1 3 5 8 7])`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a Clojure expression that computes whether any element is even.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(some even? [1 3 5 8 7])"}}]}
```

### Record 2 — example 2 of 2

**form**: `(some neg? [1 2 3])` • **expected**: `None`

**concept_phrase**: `the form (some neg? [1 2 3])`

**question_what**: `the value when no element is negative`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Robin had been trying to teach Jess how the REPL
works. "Look here," they said, pointing to the form (some neg? [1 2 3]).
"You hand the form `(some neg? [1 2 3])` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, weary from the morning's effort, agreed to try.

Write a Clojure expression that computes the value when no element is negative.

---

{"tool_calls":[{"name":"eval","args":{"form":"(some neg? [1 2 3])"}}]}
```

### Record 3 — example 1 of 2

**form**: `(some even? [1 3 5 8 7])` • **expected**: `True`

**concept_phrase**: `the form (some even? [...])`

**question_what**: `whether any element is even`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Sam demonstrated near the road how the same operation, applied to
many things at once, was the heart of every long calculation. The form
`(some even? [1 3 5 8 7])` captured the form (some even? [...]), and Lou agreed
to write it for the REPL — no claims required, just the runtime's
answer.

Write a form whose evaluation gives whether any element is even.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(some even? [1 3 5 8 7])"}}]}
```

### Record 4 — example 2 of 2

**form**: `(some neg? [1 2 3])` • **expected**: `None`

**concept_phrase**: `the form (some neg? [1 2 3])`

**question_what**: `the value when no element is negative`

```
The boy on the hill thought the trick clever the first time he played it. All this took place near the meadow.

A small crowd of villagers had gathered near the meadow to watch
Will attempt to predict, off the cuff, what the REPL would
return. Oliver pointed to the form (some neg? [1 2 3]) and read out the
form aloud: `(some neg? [1 2 3])`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a form whose evaluation gives the value when no element is negative.

---

{"tool_calls":[{"name":"eval","args":{"form":"(some neg? [1 2 3])"}}]}
```

### Record 5 — example 1 of 2

**form**: `(some even? [1 3 5 8 7])` • **expected**: `True`

**concept_phrase**: `the form (some even? [...])`

**question_what**: `whether any element is even`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A wooden notice nailed to a post by the village carried a small puzzle. The
riddle simply asked the reader to evaluate `(some even? [1 3 5 8 7])`. Lou
laughed, with great whoops of laughter, and declared it too easy to bother with.
Sam said, patiently, that the only way to be certain of
the form (some even? [...]) was to put it in the REPL.

Write a Clojure expression that computes whether any element is even.

---

I write the higher-order form so the REPL can compute.

{"tool_calls":[{"name":"eval","args":{"form":"(some even? [1 3 5 8 7])"}}]}
```

---

## G5-19: every?

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 2

**form**: `(every? pos? [1 2 3])` • **expected**: `True`

**concept_phrase**: `the form (every? pos? [1 2 3])`

**question_what**: `whether all are positive`

```
The boy on the hill thought the trick clever the first time he played it.

Carol demonstrated in the meadow how the same operation, applied to
many things at once, was the heart of every long calculation. The form
`(every? pos? [1 2 3])` captured the form (every? pos? [1 2 3]), and Jess agreed
to write it for the REPL — no claims required, just the runtime's
answer.

Write a form whose evaluation gives whether all are positive.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(every? pos? [1 2 3])"}}]}
```

### Record 2 — example 2 of 2

**form**: `(every? even? [1 2 3])` • **expected**: `False`

**concept_phrase**: `the form (every? even? [1 2 3])`

**question_what**: `whether all are even`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Jess called down from a stone at the edge of the woods where someone had
chalked the form (every? even? [1 2 3]) on a flat board. Jess, puffed up with pride,
declared she already knew what would come back. Oliver,
with steady, careful steps, asked her to actually submit the form
`(every? even? [1 2 3])` to the REPL — the village had stopped trusting answers
that weren't checked.

What Clojure form computes whether all are even? Submit it via `eval`.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(every? even? [1 2 3])"}}]}
```

### Record 3 — example 1 of 2

**form**: `(every? pos? [1 2 3])` • **expected**: `True`

**concept_phrase**: `the form (every? pos? [1 2 3])`

**question_what**: `whether all are positive`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

"Same trick, repeated cleverly," Alice said atop the hilltop, sketching the
form `(every? pos? [1 2 3])` into the dust. Tom, with a smug grin, claimed to
know exactly what the form (every? pos? [1 2 3]) would produce — but Alice
insisted, again, that the REPL was the only honest judge in the
village now.

Question: write a Clojure expression for whether all are positive.

---

{"tool_calls":[{"name":"eval","args":{"form":"(every? pos? [1 2 3])"}}]}
```

### Record 4 — example 2 of 2

**form**: `(every? even? [1 2 3])` • **expected**: `False`

**concept_phrase**: `the form (every? even? [1 2 3])`

**question_what**: `whether all are even`

```
Every shepherd in the valley knew the danger of crying wolf for sport. This was atop the hilltop.

Alex had been trying to teach Jess how the REPL
works. "Look here," they said, pointing to the form (every? even? [1 2 3]).
"You hand the form `(every? even? [1 2 3])` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, weary from the morning's effort, agreed to try.

Question: write a Clojure expression for whether all are even.

---

{"tool_calls":[{"name":"eval","args":{"form":"(every? even? [1 2 3])"}}]}
```

### Record 5 — example 1 of 2

**form**: `(every? pos? [1 2 3])` • **expected**: `True`

**concept_phrase**: `the form (every? pos? [1 2 3])`

**question_what**: `whether all are positive`

```
Every shepherd in the valley knew the danger of crying wolf for sport. It happened near the road.

"There is no need to evaluate that," Jess said, swaggering through the underbrush.
"Anyone can see what the form (every? pos? [1 2 3]) comes to." Grace, who
on the road had heard such claims many times, asked her to
actually write the form `(every? pos? [1 2 3])` and submit it to the REPL —
just to be sure.

Write a form whose evaluation gives whether all are positive.

---

{"tool_calls":[{"name":"eval","args":{"form":"(every? pos? [1 2 3])"}}]}
```

---

## G5-20: take and drop

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 2

**form**: `(take 3 [10 20 30 40 50])` • **expected**: `[10, 20, 30]`

**concept_phrase**: `the form (take 3 ...)`

**question_what**: `the first three elements`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened in the village.

Frank kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today in the village the next entry was
the form (take 3 ...). Will peered over his shoulder
at the form `(take 3 [10 20 30 40 50])` and was asked, gently, to be the one to
submit it.

What Clojure form computes the first three elements? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(take 3 [10 20 30 40 50])"}}]}
```

### Record 2 — example 2 of 2

**form**: `(drop 2 [10 20 30 40 50])` • **expected**: `[30, 40, 50]`

**concept_phrase**: `the form (drop 2 ...)`

**question_what**: `all but the first two`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

"There is no need to evaluate that," Lou said, with great whoops of laughter.
"Anyone can see what the form (drop 2 ...) comes to." George, who
in the meadow had heard such claims many times, asked her to
actually write the form `(drop 2 [10 20 30 40 50])` and submit it to the REPL —
just to be sure.

Question: write a Clojure expression for all but the first two.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(drop 2 [10 20 30 40 50])"}}]}
```

### Record 3 — example 1 of 2

**form**: `(take 3 [10 20 30 40 50])` • **expected**: `[10, 20, 30]`

**concept_phrase**: `the form (take 3 ...)`

**question_what**: `the first three elements`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

The elder of the village kept a small slate by the farm, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the form (take 3 ...). Bob read
out the form `(take 3 [10 20 30 40 50])` so Will could write it
properly into the REPL and earn an honest mark on the slate.

Write a form whose evaluation gives the first three elements.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(take 3 [10 20 30 40 50])"}}]}
```

### Record 4 — example 2 of 2

**form**: `(drop 2 [10 20 30 40 50])` • **expected**: `[30, 40, 50]`

**concept_phrase**: `the form (drop 2 ...)`

**question_what**: `all but the first two`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Alice kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today at the edge of the forest the next entry was
the form (drop 2 ...). Pat peered over her shoulder
at the form `(drop 2 [10 20 30 40 50])` and was asked, gently, to be the one to
submit it.

Write a Clojure expression that computes all but the first two.

---

{"tool_calls":[{"name":"eval","args":{"form":"(drop 2 [10 20 30 40 50])"}}]}
```

### Record 5 — example 1 of 2

**form**: `(take 3 [10 20 30 40 50])` • **expected**: `[10, 20, 30]`

**concept_phrase**: `the form (take 3 ...)`

**question_what**: `the first three elements`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

"There is no need to evaluate that," Lou said, swaggering through the underbrush.
"Anyone can see what the form (take 3 ...) comes to." Carol, who
by the farm had heard such claims many times, asked her to
actually write the form `(take 3 [10 20 30 40 50])` and submit it to the REPL —
just to be sure.

What Clojure form computes the first three elements? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(take 3 [10 20 30 40 50])"}}]}
```

---

## G5-21: distinct and sort

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 2

**form**: `(distinct [1 1 2 3 3 4])` • **expected**: `[1, 2, 3, 4]`

**concept_phrase**: `the form (distinct [1 1 2 3 3 4])`

**question_what**: `the deduplicated seq`

```
The boy on the hill thought the trick clever the first time he played it.

Halfway through the morning watch, Will called out
near the orchard, demanding a verdict on the form `(distinct [1 1 2 3 3 4])` and refusing
to descend until somebody confirmed it. Will insisted
he already knew the answer. Morgan, walking up
at an unhurried pace, simply said: "Submit the form (distinct [1 1 2 3 3 4]) to the
REPL. Whatever comes back is the answer."

Write a Clojure expression that computes the deduplicated seq.

---

{"tool_calls":[{"name":"eval","args":{"form":"(distinct [1 1 2 3 3 4])"}}]}
```

### Record 2 — example 2 of 2

**form**: `(sort [3 1 2])` • **expected**: `[1, 2, 3]`

**concept_phrase**: `the form (sort [3 1 2])`

**question_what**: `the sorted seq`

```
The boy on the hill thought the trick clever the first time he played it.

Grace kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today at the edge of the orchard the next entry was
the form (sort [3 1 2]). Lou peered over her shoulder
at the form `(sort [3 1 2])` and was asked, gently, to be the one to
submit it.

What Clojure form computes the sorted seq? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(sort [3 1 2])"}}]}
```

### Record 3 — example 1 of 2

**form**: `(distinct [1 1 2 3 3 4])` • **expected**: `[1, 2, 3, 4]`

**concept_phrase**: `the form (distinct [1 1 2 3 3 4])`

**question_what**: `the deduplicated seq`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Lou called down from a stone at the edge of the hilltop where someone had
chalked the form (distinct [1 1 2 3 3 4]) on a flat board. Lou, swaggering through the underbrush,
declared she already knew what would come back. Alice,
saying very little, asked her to actually submit the form
`(distinct [1 1 2 3 3 4])` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a form whose evaluation gives the deduplicated seq.

---

{"tool_calls":[{"name":"eval","args":{"form":"(distinct [1 1 2 3 3 4])"}}]}
```

### Record 4 — example 2 of 2

**form**: `(sort [3 1 2])` • **expected**: `[1, 2, 3]`

**concept_phrase**: `the form (sort [3 1 2])`

**question_what**: `the sorted seq`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

The elder of the village kept a small slate near the orchard, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the form (sort [3 1 2]). Oliver read
out the form `(sort [3 1 2])` so Lou could write it
properly into the REPL and earn an honest mark on the slate.

Write a Clojure expression that computes the sorted seq.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(sort [3 1 2])"}}]}
```

### Record 5 — example 1 of 2

**form**: `(distinct [1 1 2 3 3 4])` • **expected**: `[1, 2, 3, 4]`

**concept_phrase**: `the form (distinct [1 1 2 3 3 4])`

**question_what**: `the deduplicated seq`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place at the edge of the woods.

Alice demonstrated at the edge of the woods how the same operation, applied to
many things at once, was the heart of every long calculation. The form
`(distinct [1 1 2 3 3 4])` captured the form (distinct [1 1 2 3 3 4]), and Lou agreed
to write it for the REPL — no claims required, just the runtime's
answer.

Write a Clojure expression that computes the deduplicated seq.

---

{"tool_calls":[{"name":"eval","args":{"form":"(distinct [1 1 2 3 3 4])"}}]}
```

---

## G5-22: recur — first taste

**Examples:** 1 | **Subplots:** 12 | **Plan-pool size:** 9

### Record 1 — example 1 of 1

**form**: `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))` • **expected**: `120`

**concept_phrase**: `a loop computing factorial of 5 via recur`

**question_what**: `5! computed via loop/recur`

```
Every shepherd in the valley knew the danger of crying wolf for sport. It happened along the road.

Halfway through the morning watch, Jess called out
along the road, demanding a verdict on the form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))` and refusing
to descend until somebody confirmed it. Jess insisted
she already knew the answer. Frank, walking up
at an unhurried pace, simply said: "Submit a loop computing factorial of 5 via recur to the
REPL. Whatever comes back is the answer."

Write a Clojure expression that computes 5! computed via loop/recur.

---

{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
```

### Record 2 — example 1 of 1

**form**: `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))` • **expected**: `120`

**concept_phrase**: `a loop computing factorial of 5 via recur`

**question_what**: `5! computed via loop/recur`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

"Same trick, repeated cleverly," Oliver said at the edge of the orchard, sketching the
form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))` into the dust. Tom, boasting at every turn, claimed to
know exactly what a loop computing factorial of 5 via recur would produce — but Oliver
insisted, again, that the REPL was the only honest judge in the
village now.

Question: write a Clojure expression for 5! computed via loop/recur.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
```

### Record 3 — example 1 of 1

**form**: `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))` • **expected**: `120`

**concept_phrase**: `a loop computing factorial of 5 via recur`

**question_what**: `5! computed via loop/recur`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

The elder of the village kept a small slate at the edge of the forest, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was a loop computing factorial of 5 via recur. Sam read
out the form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))` so Jess could write it
properly into the REPL and earn an honest mark on the slate.

Write a form whose evaluation gives 5! computed via loop/recur.

---

{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
```

### Record 4 — example 1 of 1

**form**: `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))` • **expected**: `120`

**concept_phrase**: `a loop computing factorial of 5 via recur`

**question_what**: `5! computed via loop/recur`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Alex had been trying to teach Will how the REPL
works. "Look here," they said, pointing to a loop computing factorial of 5 via recur.
"You hand the form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Will, her legs heavy from sprinting, agreed to try.

What Clojure form computes 5! computed via loop/recur? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
```

### Record 5 — example 1 of 1

**form**: `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))` • **expected**: `120`

**concept_phrase**: `a loop computing factorial of 5 via recur`

**question_what**: `5! computed via loop/recur`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden notice nailed to a post near the forest carried a small puzzle. The
riddle simply asked the reader to evaluate `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`. Will
laughed, with a smug grin, and declared it too easy to bother with.
Oliver said, patiently, that the only way to be certain of
a loop computing factorial of 5 via recur was to put it in the REPL.

Question: write a Clojure expression for 5! computed via loop/recur.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
```

---

