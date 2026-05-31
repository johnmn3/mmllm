# Boy-wolf Grade 2 — deep spot-check

5 generated records per subject (across all examples and a variety of seeds). Read every record carefully. Flag anything that reads odd to a careful reader, including issues the structural audit can't catch (prose flow, contextual fit, cliché repetition, subplot/example mismatch, etc.)

---

## G2-01: Multi-arg arithmetic

**Examples:** 6 | **Subplots:** 12 | **Plan-pool size:** 7

### Record 1 — example 1 of 6

**form**: `(+ 1 2 3 4)` • **expected**: `10`

**concept_phrase**: `the sum (+ 1 2 3 4)`

**question_what**: `the result of (+ 1 2 3 4)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Alice had been laying out a chain of small computations on a
slate near the woods — one operation, then another, all to settle a question
Pat had raised. The current form on the slate was
`(+ 1 2 3 4)`, and Alice explained that the sum (+ 1 2 3 4) would be
settled the moment the form was evaluated.

Write a Clojure expression that computes the result of (+ 1 2 3 4).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2 3 4)"}}]}
```

### Record 2 — example 2 of 6

**form**: `(* 2 3 4)` • **expected**: `24`

**concept_phrase**: `the product (* 2 3 4)`

**question_what**: `the result of (* 2 3 4)`

```
The boy on the hill thought the trick clever the first time he played it.

Lou called down from a stone in the village where someone had
chalked the product (* 2 3 4) on a flat board. Lou, puffed up with pride,
declared she already knew what would come back. Sam,
untroubled by what others thought, asked her to actually submit the form
`(* 2 3 4)` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the result of (* 2 3 4).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(* 2 3 4)"}}]}
```

### Record 3 — example 3 of 6

**form**: `(- 100 1 2 3)` • **expected**: `94`

**concept_phrase**: `the chain (- 100 1 2 3)`

**question_what**: `the result of (- 100 1 2 3)`

```
Every shepherd in the valley knew the danger of crying wolf for sport. This was near the road.

The elder of the village kept a small slate on the road, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the chain (- 100 1 2 3). George read
out the form `(- 100 1 2 3)` so Tom could write it
properly into the REPL and earn an honest mark on the slate.

Question: write a Clojure expression for the result of (- 100 1 2 3).

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(- 100 1 2 3)"}}]}
```

### Record 4 — example 4 of 6

**form**: `(+ 1 2 3 4 5 6 7 8 9 10)` • **expected**: `55`

**concept_phrase**: `the sum 1+2+...+10`

**question_what**: `the sum of integers 1 through 10`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Alice had been laying out a chain of small computations on a
slate near the orchard — one operation, then another, all to settle a question
Will had raised. The current form on the slate was
`(+ 1 2 3 4 5 6 7 8 9 10)`, and Alice explained that the sum 1+2+...+10 would be
settled the moment the form was evaluated.

What Clojure form computes the sum of integers 1 through 10? Submit it via `eval`.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2 3 4 5 6 7 8 9 10)"}}]}
```

### Record 5 — example 5 of 6

**form**: `(* 1 2 3 4 5)` • **expected**: `120`

**concept_phrase**: `the product 1*2*3*4*5`

**question_what**: `the product of 1 through 5 (5!)`

```
Every shepherd in the valley knew the danger of crying wolf for sport. This was near the orchard.

Grace had been laying out a chain of small computations on a
slate in the orchard — one operation, then another, all to settle a question
Tom had raised. The current form on the slate was
`(* 1 2 3 4 5)`, and Grace explained that the product 1*2*3*4*5 would be
settled the moment the form was evaluated.

What Clojure form computes the product of 1 through 5 (5!)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 1 2 3 4 5)"}}]}
```

---

## G2-02: Comparison chains

**Examples:** 5 | **Subplots:** 12 | **Plan-pool size:** 7

### Record 1 — example 1 of 5

**form**: `(< 1 2 3)` • **expected**: `True`

**concept_phrase**: `the chain (< 1 2 3)`

**question_what**: `whether 1 < 2 < 3`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Will called down from a stone by the orchard where someone had
chalked the chain (< 1 2 3) on a flat board. Will, with a smug grin,
declared he already knew what would come back. Morgan,
stepping deliberately, asked him to actually submit the form
`(< 1 2 3)` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a form whose evaluation gives whether 1 < 2 < 3.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(< 1 2 3)"}}]}
```

### Record 2 — example 2 of 5

**form**: `(< 3 2 1)` • **expected**: `False`

**concept_phrase**: `the chain (< 3 2 1)`

**question_what**: `whether 3 < 2 < 1`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place by the woods.

"Whatever `(< 3 2 1)` comes to," Tom declared,
boasting at every turn, at the edge of the woods, "anyone could see it without typing a thing."
Grace, saying very little, picked up a stick and drew
the chain (< 3 2 1) in the dust. "Then write the form," she
said. "The REPL will have the last word.

Write a Clojure expression that computes whether 3 < 2 < 1.

---

{"tool_calls":[{"name":"eval","args":{"form":"(< 3 2 1)"}}]}
```

### Record 3 — example 3 of 5

**form**: `(<= 1 1 2)` • **expected**: `True`

**concept_phrase**: `the chain (<= 1 1 2)`

**question_what**: `whether 1 ≤ 1 ≤ 2`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden notice nailed to a post at the edge of the orchard carried a small puzzle. The
riddle simply asked the reader to evaluate `(<= 1 1 2)`. Pat
laughed, with great whoops of laughter, and declared it too easy to bother with.
Oliver said, patiently, that the only way to be certain of
the chain (<= 1 1 2) was to put it in the REPL.

Write a Clojure expression that computes whether 1 ≤ 1 ≤ 2.

---

{"tool_calls":[{"name":"eval","args":{"form":"(<= 1 1 2)"}}]}
```

### Record 4 — example 4 of 5

**form**: `(> 5 4 3 2 1)` • **expected**: `True`

**concept_phrase**: `the chain (> 5 4 3 2 1)`

**question_what**: `whether the numbers 5,4,3,2,1 are strictly decreasing`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Grace had been trying to teach Tom how the REPL
works. "Look here," she said, pointing to the chain (> 5 4 3 2 1).
"You hand the form `(> 5 4 3 2 1)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Tom, drowsy from the warm sun, agreed to try.

Write a Clojure expression that computes whether the numbers 5,4,3,2,1 are strictly decreasing.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(> 5 4 3 2 1)"}}]}
```

### Record 5 — example 5 of 5

**form**: `(>= 3 3 2)` • **expected**: `True`

**concept_phrase**: `the chain (>= 3 3 2)`

**question_what**: `whether 3 ≥ 3 ≥ 2`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place on the road.

"There is no need to evaluate that," Will said, with great whoops of laughter.
"Anyone can see what the chain (>= 3 3 2) comes to." Carol, who
near the road had heard such claims many times, asked him to
actually write the form `(>= 3 3 2)` and submit it to the REPL —
just to be sure.

What Clojure form computes whether 3 ≥ 3 ≥ 2? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(>= 3 3 2)"}}]}
```

---

## G2-03: not= and = with multiple args

**Examples:** 5 | **Subplots:** 12 | **Plan-pool size:** 7

### Record 1 — example 1 of 5

**form**: `(not= 1 2)` • **expected**: `True`

**concept_phrase**: `the form (not= 1 2)`

**question_what**: `whether 1 differs from 2`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place at the edge of the village.

Alice had been trying to teach Will how the REPL
works. "Look here," she said, pointing to the form (not= 1 2).
"You hand the form `(not= 1 2)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Will, drowsy from the warm sun, agreed to try.

Write a Clojure expression that computes whether 1 differs from 2.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(not= 1 2)"}}]}
```

### Record 2 — example 2 of 5

**form**: `(not= 1 1)` • **expected**: `False`

**concept_phrase**: `the form (not= 1 1)`

**question_what**: `whether 1 differs from 1`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened near the meadow.

Oliver had been trying to teach Lou how the REPL
works. "Look here," he said, pointing to the form (not= 1 1).
"You hand the form `(not= 1 1)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Lou, yawning at the soft moss, agreed to try.

Write a form whose evaluation gives whether 1 differs from 1.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(not= 1 1)"}}]}
```

### Record 3 — example 3 of 5

**form**: `(= 1 1 1)` • **expected**: `True`

**concept_phrase**: `the form (= 1 1 1)`

**question_what**: `whether all of 1,1,1 are equal`

```
Every shepherd in the valley knew the danger of crying wolf for sport. It happened at the edge of the orchard.

Halfway through the morning watch, Pat called out
by the orchard, demanding a verdict on the form `(= 1 1 1)` and refusing
to descend until somebody confirmed it. Pat insisted
they already knew the answer. George, walking up
at an unhurried pace, simply said: "Submit the form (= 1 1 1) to the
REPL. Whatever comes back is the answer."

Write a form whose evaluation gives whether all of 1,1,1 are equal.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 1 1)"}}]}
```

### Record 4 — example 4 of 5

**form**: `(= 1 1 2)` • **expected**: `False`

**concept_phrase**: `the form (= 1 1 2)`

**question_what**: `whether 1,1,2 are all equal`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Robin had been laying out a chain of small computations on a
slate in the village — one operation, then another, all to settle a question
Lou had raised. The current form on the slate was
`(= 1 1 2)`, and Robin explained that the form (= 1 1 2) would be
settled the moment the form was evaluated.

Write a form whose evaluation gives whether 1,1,2 are all equal.

---

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 1 2)"}}]}
```

### Record 5 — example 5 of 5

**form**: `(not= 1 1 2)` • **expected**: `True`

**concept_phrase**: `the form (not= 1 1 2)`

**question_what**: `whether at least one of 1,1,2 differs`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

"Whatever `(not= 1 1 2)` comes to," Tom declared,
with a smug grin, at the edge of the village, "anyone could see it without typing a thing."
Alex, saying very little, picked up a stick and drew
the form (not= 1 1 2) in the dust. "Then write the form," they
said. "The REPL will have the last word.

Question: write a Clojure expression for whether at least one of 1,1,2 differs.

---

{"tool_calls":[{"name":"eval","args":{"form":"(not= 1 1 2)"}}]}
```

---

## G2-04: min and max

**Examples:** 5 | **Subplots:** 12 | **Plan-pool size:** 7

### Record 1 — example 1 of 5

**form**: `(min 1 2 3)` • **expected**: `1`

**concept_phrase**: `the form (min 1 2 3)`

**question_what**: `the minimum of 1, 2, 3`

```
The boy on the hill thought the trick clever the first time he played it.

"Whatever `(min 1 2 3)` comes to," Pat declared,
with great whoops of laughter, near the farm, "anyone could see it without typing a thing."
Bob, saying very little, picked up a stick and drew
the form (min 1 2 3) in the dust. "Then write the form," he
said. "The REPL will have the last word.

Write a Clojure expression that computes the minimum of 1, 2, 3.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(min 1 2 3)"}}]}
```

### Record 2 — example 2 of 5

**form**: `(max 1 2 3)` • **expected**: `3`

**concept_phrase**: `the form (max 1 2 3)`

**question_what**: `the maximum of 1, 2, 3`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened at the edge of the village.

"Whatever `(max 1 2 3)` comes to," Jess declared,
swaggering through the underbrush, near the village, "anyone could see it without typing a thing."
George, stepping deliberately, picked up a stick and drew
the form (max 1 2 3) in the dust. "Then write the form," he
said. "The REPL will have the last word.

Write a Clojure expression that computes the maximum of 1, 2, 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(max 1 2 3)"}}]}
```

### Record 3 — example 3 of 5

**form**: `(min 7 3 9 1 5)` • **expected**: `1`

**concept_phrase**: `the form (min 7 3 9 1 5)`

**question_what**: `the minimum of 7, 3, 9, 1, 5`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. This was by the village.

Halfway through the morning watch, Jess called out
at the edge of the village, demanding a verdict on the form `(min 7 3 9 1 5)` and refusing
to descend until somebody confirmed it. Jess insisted
she already knew the answer. Grace, walking up
at an unhurried pace, simply said: "Submit the form (min 7 3 9 1 5) to the
REPL. Whatever comes back is the answer."

What Clojure form computes the minimum of 7, 3, 9, 1, 5? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(min 7 3 9 1 5)"}}]}
```

### Record 4 — example 4 of 5

**form**: `(max 7 3 9 1 5)` • **expected**: `9`

**concept_phrase**: `the form (max 7 3 9 1 5)`

**question_what**: `the maximum of 7, 3, 9, 1, 5`

```
The boy on the hill thought the trick clever the first time he played it. All this took place by the farm.

"Whatever `(max 7 3 9 1 5)` comes to," Pat declared,
swaggering through the underbrush, in the farm, "anyone could see it without typing a thing."
Frank, her eyes always on the path, picked up a stick and drew
the form (max 7 3 9 1 5) in the dust. "Then write the form," he
said. "The REPL will have the last word.

Question: write a Clojure expression for the maximum of 7, 3, 9, 1, 5.

---

{"tool_calls":[{"name":"eval","args":{"form":"(max 7 3 9 1 5)"}}]}
```

### Record 5 — example 5 of 5

**form**: `(min -3 -1 -5)` • **expected**: `-5`

**concept_phrase**: `the form (min -3 -1 -5)`

**question_what**: `the minimum of -3, -1, -5`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened in the forest.

A small crowd of villagers had gathered in the forest to watch
Will attempt to predict, off the cuff, what the REPL would
return. Robin pointed to the form (min -3 -1 -5) and read out the
form aloud: `(min -3 -1 -5)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a form whose evaluation gives the minimum of -3, -1, -5.

---

{"tool_calls":[{"name":"eval","args":{"form":"(min -3 -1 -5)"}}]}
```

---

## G2-05: quot, rem, mod

**Examples:** 6 | **Subplots:** 12 | **Plan-pool size:** 7

### Record 1 — example 1 of 6

**form**: `(quot 17 5)` • **expected**: `3`

**concept_phrase**: `the integer quotient of 17 and 5`

**question_what**: `the result of (quot 17 5)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Halfway through the morning watch, Jess called out
near the hilltop, demanding a verdict on the form `(quot 17 5)` and refusing
to descend until somebody confirmed it. Jess insisted
she already knew the answer. Alice, walking up
at an unhurried pace, simply said: "Submit the integer quotient of 17 and 5 to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the result of (quot 17 5).

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(quot 17 5)"}}]}
```

### Record 2 — example 2 of 6

**form**: `(rem 17 5)` • **expected**: `2`

**concept_phrase**: `the remainder of 17 divided by 5`

**question_what**: `the result of (rem 17 5)`

```
The boy on the hill thought the trick clever the first time he played it.

A wooden notice nailed to a post in the forest carried a small puzzle. The
riddle simply asked the reader to evaluate `(rem 17 5)`. Tom
laughed, with great whoops of laughter, and declared it too easy to bother with.
Alex said, patiently, that the only way to be certain of
the remainder of 17 divided by 5 was to put it in the REPL.

What Clojure form computes the result of (rem 17 5)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(rem 17 5)"}}]}
```

### Record 3 — example 3 of 6

**form**: `(mod 17 5)` • **expected**: `2`

**concept_phrase**: `17 mod 5`

**question_what**: `the result of (mod 17 5)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A small slate sat on a flat stone by the forest; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(mod 17 5)`, and the page
heading read 17 mod 5. Carol nodded at Will to
write the form properly so the slate would carry an honest entry.

Question: write a Clojure expression for the result of (mod 17 5).

---

{"tool_calls":[{"name":"eval","args":{"form":"(mod 17 5)"}}]}
```

### Record 4 — example 4 of 6

**form**: `(quot 100 7)` • **expected**: `14`

**concept_phrase**: `the integer quotient of 100 and 7`

**question_what**: `the result of (quot 100 7)`

```
The boy on the hill thought the trick clever the first time he played it.

"Whatever `(quot 100 7)` comes to," Jess declared,
with a smug grin, in the orchard, "anyone could see it without typing a thing."
Morgan, stepping deliberately, picked up a stick and drew
the integer quotient of 100 and 7 in the dust. "Then write the form," they
said. "The REPL will have the last word.

Write a form whose evaluation gives the result of (quot 100 7).

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(quot 100 7)"}}]}
```

### Record 5 — example 5 of 6

**form**: `(rem 100 7)` • **expected**: `2`

**concept_phrase**: `the remainder of 100 divided by 7`

**question_what**: `the result of (rem 100 7)`

```
The boy on the hill thought the trick clever the first time he played it. It happened in the orchard.

"There is no need to evaluate that," Tom said, puffed up with pride.
"Anyone can see what the remainder of 100 divided by 7 comes to." Oliver, who
near the orchard had heard such claims many times, asked him to
actually write the form `(rem 100 7)` and submit it to the REPL —
just to be sure.

What Clojure form computes the result of (rem 100 7)? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(rem 100 7)"}}]}
```

---

## G2-06: inc and dec

**Examples:** 5 | **Subplots:** 12 | **Plan-pool size:** 7

### Record 1 — example 1 of 5

**form**: `(inc 5)` • **expected**: `6`

**concept_phrase**: `the form (inc 5)`

**question_what**: `5 plus 1`

```
The boy on the hill thought the trick clever the first time he played it.

Frank had been laying out a chain of small computations on a
slate atop the hilltop — one operation, then another, all to settle a question
Will had raised. The current form on the slate was
`(inc 5)`, and Frank explained that the form (inc 5) would be
settled the moment the form was evaluated.

Write a Clojure expression that computes 5 plus 1.

---

{"tool_calls":[{"name":"eval","args":{"form":"(inc 5)"}}]}
```

### Record 2 — example 2 of 5

**form**: `(dec 5)` • **expected**: `4`

**concept_phrase**: `the form (dec 5)`

**question_what**: `5 minus 1`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Halfway through the morning watch, Pat called out
near the woods, demanding a verdict on the form `(dec 5)` and refusing
to descend until somebody confirmed it. Pat insisted
they already knew the answer. Robin, walking up
at an unhurried pace, simply said: "Submit the form (dec 5) to the
REPL. Whatever comes back is the answer."

What Clojure form computes 5 minus 1? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(dec 5)"}}]}
```

### Record 3 — example 3 of 5

**form**: `(inc 0)` • **expected**: `1`

**concept_phrase**: `the form (inc 0)`

**question_what**: `the successor of 0`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Robin kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today by the meadow the next entry was
the form (inc 0). Tom peered over their shoulder
at the form `(inc 0)` and was asked, gently, to be the one to
submit it.

Question: write a Clojure expression for the successor of 0.

---

{"tool_calls":[{"name":"eval","args":{"form":"(inc 0)"}}]}
```

### Record 4 — example 4 of 5

**form**: `(dec 0)` • **expected**: `-1`

**concept_phrase**: `the form (dec 0)`

**question_what**: `the predecessor of 0`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

"There is no need to evaluate that," Will said, as if the race were already won.
"Anyone can see what the form (dec 0) comes to." Sam, who
at the edge of the farm had heard such claims many times, asked him to
actually write the form `(dec 0)` and submit it to the REPL —
just to be sure.

What Clojure form computes the predecessor of 0? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(dec 0)"}}]}
```

### Record 5 — example 5 of 5

**form**: `(inc -1)` • **expected**: `0`

**concept_phrase**: `the form (inc -1)`

**question_what**: `the successor of -1`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

"There is no need to evaluate that," Tom said, with great whoops of laughter.
"Anyone can see what the form (inc -1) comes to." Frank, who
at the edge of the hilltop had heard such claims many times, asked him to
actually write the form `(inc -1)` and submit it to the REPL —
just to be sure.

Question: write a Clojure expression for the successor of -1.

---

{"tool_calls":[{"name":"eval","args":{"form":"(inc -1)"}}]}
```

---

## G2-07: Absolute value

**Examples:** 4 | **Subplots:** 12 | **Plan-pool size:** 7

### Record 1 — example 1 of 4

**form**: `(abs 5)` • **expected**: `5`

**concept_phrase**: `the form (abs 5)`

**question_what**: `the absolute value of 5`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A small crowd of villagers had gathered by the woods to watch
Tom attempt to predict, off the cuff, what the REPL would
return. Robin pointed to the form (abs 5) and read out the
form aloud: `(abs 5)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

What Clojure form computes the absolute value of 5? Submit it via `eval`.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(abs 5)"}}]}
```

### Record 2 — example 2 of 4

**form**: `(abs -5)` • **expected**: `5`

**concept_phrase**: `the form (abs -5)`

**question_what**: `the absolute value of -5`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place near the meadow.

A wooden notice nailed to a post by the meadow carried a small puzzle. The
riddle simply asked the reader to evaluate `(abs -5)`. Jess
laughed, puffed up with pride, and declared it too easy to bother with.
Oliver said, patiently, that the only way to be certain of
the form (abs -5) was to put it in the REPL.

Write a Clojure expression that computes the absolute value of -5.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(abs -5)"}}]}
```

### Record 3 — example 3 of 4

**form**: `(abs 0)` • **expected**: `0`

**concept_phrase**: `the form (abs 0)`

**question_what**: `the absolute value of 0`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Lou called down from a stone near the village where someone had
chalked the form (abs 0) on a flat board. Lou, boasting at every turn,
declared she already knew what would come back. Frank,
without complaint, asked her to actually submit the form
`(abs 0)` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the absolute value of 0.

---

{"tool_calls":[{"name":"eval","args":{"form":"(abs 0)"}}]}
```

### Record 4 — example 4 of 4

**form**: `(abs (- 3 8))` • **expected**: `5`

**concept_phrase**: `the form (abs (- 3 8))`

**question_what**: `the absolute value of 3 minus 8`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened atop the hilltop.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(abs (- 3 8))`, and the line
above it read the form (abs (- 3 8)). Alice handed the page to
Will, who, weary from the morning's effort, agreed to write it out properly.

Write a form whose evaluation gives the absolute value of 3 minus 8.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(abs (- 3 8))"}}]}
```

### Record 5 — example 1 of 4

**form**: `(abs 5)` • **expected**: `5`

**concept_phrase**: `the form (abs 5)`

**question_what**: `the absolute value of 5`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A small slate sat on a flat stone near the farm; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(abs 5)`, and the page
heading read the form (abs 5). George nodded at Jess to
write the form properly so the slate would carry an honest entry.

What Clojure form computes the absolute value of 5? Submit it via `eval`.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(abs 5)"}}]}
```

---

## G2-08: Arithmetic on ratios

**Examples:** 3 | **Subplots:** 12 | **Plan-pool size:** 7

### Record 1 — example 1 of 3

**form**: `(+ 1/2 1/4)` • **expected**: `'3/4'`

**concept_phrase**: `the sum 1/2 + 1/4`

**question_what**: `the value of (+ 1/2 1/4)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened near the orchard.

Oliver had been laying out a chain of small computations on a
slate in the orchard — one operation, then another, all to settle a question
Tom had raised. The current form on the slate was
`(+ 1/2 1/4)`, and Oliver explained that the sum 1/2 + 1/4 would be
settled the moment the form was evaluated.

Write a form whose evaluation gives the value of (+ 1/2 1/4).

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1/2 1/4)"}}]}
```

### Record 2 — example 2 of 3

**form**: `(* 2/3 3/4)` • **expected**: `'1/2'`

**concept_phrase**: `the product 2/3 × 3/4`

**question_what**: `the value of (* 2/3 3/4)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened by the orchard.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(* 2/3 3/4)`, and the line
above it read the product 2/3 × 3/4. Alex handed the page to
Pat, who, lulled by the gentle wind, agreed to write it out properly.

Write a Clojure expression that computes the value of (* 2/3 3/4).

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 2/3 3/4)"}}]}
```

### Record 3 — example 3 of 3

**form**: `(- 1 1/3)` • **expected**: `'2/3'`

**concept_phrase**: `the form (- 1 1/3)`

**question_what**: `the value of (- 1 1/3)`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Halfway through the morning watch, Jess called out
near the meadow, demanding a verdict on the form `(- 1 1/3)` and refusing
to descend until somebody confirmed it. Jess insisted
she already knew the answer. Bob, walking up
at an unhurried pace, simply said: "Submit the form (- 1 1/3) to the
REPL. Whatever comes back is the answer."

What Clojure form computes the value of (- 1 1/3)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(- 1 1/3)"}}]}
```

### Record 4 — example 1 of 3

**form**: `(+ 1/2 1/4)` • **expected**: `'3/4'`

**concept_phrase**: `the sum 1/2 + 1/4`

**question_what**: `the value of (+ 1/2 1/4)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Sam had been trying to teach Lou how the REPL
works. "Look here," they said, pointing to the sum 1/2 + 1/4.
"You hand the form `(+ 1/2 1/4)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Lou, drowsy from the warm sun, agreed to try.

Write a Clojure expression that computes the value of (+ 1/2 1/4).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1/2 1/4)"}}]}
```

### Record 5 — example 2 of 3

**form**: `(* 2/3 3/4)` • **expected**: `'1/2'`

**concept_phrase**: `the product 2/3 × 3/4`

**question_what**: `the value of (* 2/3 3/4)`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

The elder of the village kept a small slate near the village, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the product 2/3 × 3/4. Frank read
out the form `(* 2/3 3/4)` so Lou could write it
properly into the REPL and earn an honest mark on the slate.

Write a Clojure expression that computes the value of (* 2/3 3/4).

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 2/3 3/4)"}}]}
```

---

## G2-09: Floats vs ints (the / operator)

**Examples:** 3 | **Subplots:** 12 | **Plan-pool size:** 7

### Record 1 — example 1 of 3

**form**: `(/ 10 2)` • **expected**: `5`

**concept_phrase**: `the integer division 10 ÷ 2`

**question_what**: `the value of (/ 10 2)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place in the woods.

Halfway through the morning watch, Will called out
at the edge of the woods, demanding a verdict on the form `(/ 10 2)` and refusing
to descend until somebody confirmed it. Will insisted
he already knew the answer. George, walking up
at an unhurried pace, simply said: "Submit the integer division 10 ÷ 2 to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the value of (/ 10 2).

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(/ 10 2)"}}]}
```

### Record 2 — example 2 of 3

**form**: `(/ 10 3)` • **expected**: `'10/3'`

**concept_phrase**: `the form (/ 10 3)`

**question_what**: `the exact rational result of (/ 10 3)`

```
The boy on the hill thought the trick clever the first time he played it.

"There is no need to evaluate that," Pat said, swaggering through the underbrush.
"Anyone can see what the form (/ 10 3) comes to." Alice, who
by the forest had heard such claims many times, asked them to
actually write the form `(/ 10 3)` and submit it to the REPL —
just to be sure.

Write a form whose evaluation gives the exact rational result of (/ 10 3).

---

{"tool_calls":[{"name":"eval","args":{"form":"(/ 10 3)"}}]}
```

### Record 3 — example 3 of 3

**form**: `(/ 1.0 2)` • **expected**: `0.5`

**concept_phrase**: `the float division 1.0 ÷ 2`

**question_what**: `the value of (/ 1.0 2)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. This was by the farm.

Sam had been trying to teach Will how the REPL
works. "Look here," they said, pointing to the float division 1.0 ÷ 2.
"You hand the form `(/ 1.0 2)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Will, weary from the morning's effort, agreed to try.

Question: write a Clojure expression for the value of (/ 1.0 2).

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(/ 1.0 2)"}}]}
```

### Record 4 — example 1 of 3

**form**: `(/ 10 2)` • **expected**: `5`

**concept_phrase**: `the integer division 10 ÷ 2`

**question_what**: `the value of (/ 10 2)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place on the road.

Halfway through the morning watch, Tom called out
along the road, demanding a verdict on the form `(/ 10 2)` and refusing
to descend until somebody confirmed it. Tom insisted
he already knew the answer. Sam, walking up
at an unhurried pace, simply said: "Submit the integer division 10 ÷ 2 to the
REPL. Whatever comes back is the answer."

Write a Clojure expression that computes the value of (/ 10 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(/ 10 2)"}}]}
```

### Record 5 — example 2 of 3

**form**: `(/ 10 3)` • **expected**: `'10/3'`

**concept_phrase**: `the form (/ 10 3)`

**question_what**: `the exact rational result of (/ 10 3)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

"There is no need to evaluate that," Jess said, as if the race were already won.
"Anyone can see what the form (/ 10 3) comes to." Alice, who
at the edge of the hilltop had heard such claims many times, asked her to
actually write the form `(/ 10 3)` and submit it to the REPL —
just to be sure.

Write a form whose evaluation gives the exact rational result of (/ 10 3).

---

{"tool_calls":[{"name":"eval","args":{"form":"(/ 10 3)"}}]}
```

---

## G2-10: Powers via repeated multiplication

**Examples:** 4 | **Subplots:** 12 | **Plan-pool size:** 7

### Record 1 — example 1 of 4

**form**: `(* 2 2 2)` • **expected**: `8`

**concept_phrase**: `two cubed`

**question_what**: `2 to the third power`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Lou called down from a stone atop the hilltop where someone had
chalked two cubed on a flat board. Lou, boasting at every turn,
declared she already knew what would come back. Grace,
with steady, careful steps, asked her to actually submit the form
`(* 2 2 2)` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes 2 to the third power.

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 2 2 2)"}}]}
```

### Record 2 — example 2 of 4

**form**: `(* 5 5)` • **expected**: `25`

**concept_phrase**: `five squared`

**question_what**: `5 squared`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. This was near the orchard.

"There is no need to evaluate that," Pat said, with a smug grin.
"Anyone can see what five squared comes to." Morgan, who
near the orchard had heard such claims many times, asked them to
actually write the form `(* 5 5)` and submit it to the REPL —
just to be sure.

Question: write a Clojure expression for 5 squared.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(* 5 5)"}}]}
```

### Record 3 — example 3 of 4

**form**: `(* 3 3 3 3)` • **expected**: `81`

**concept_phrase**: `three to the fourth`

**question_what**: `3 to the fourth power`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Alice had been laying out a chain of small computations on a
slate by the forest — one operation, then another, all to settle a question
Will had raised. The current form on the slate was
`(* 3 3 3 3)`, and Alice explained that three to the fourth would be
settled the moment the form was evaluated.

What Clojure form computes 3 to the fourth power? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(* 3 3 3 3)"}}]}
```

### Record 4 — example 4 of 4

**form**: `(* 10 10)` • **expected**: `100`

**concept_phrase**: `ten squared`

**question_what**: `10 squared`

```
The boy on the hill thought the trick clever the first time he played it.

Grace kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the village the next entry was
ten squared. Pat peered over her shoulder
at the form `(* 10 10)` and was asked, gently, to be the one to
submit it.

Question: write a Clojure expression for 10 squared.

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 10 10)"}}]}
```

### Record 5 — example 1 of 4

**form**: `(* 2 2 2)` • **expected**: `8`

**concept_phrase**: `two cubed`

**question_what**: `2 to the third power`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

"Whatever `(* 2 2 2)` comes to," Tom declared,
with a smug grin, by the farm, "anyone could see it without typing a thing."
Robin, untroubled by what others thought, picked up a stick and drew
two cubed in the dust. "Then write the form," they
said. "The REPL will have the last word.

Write a form whose evaluation gives 2 to the third power.

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 2 2 2)"}}]}
```

---

## G2-11: String concatenation with str

**Examples:** 4 | **Subplots:** 12 | **Plan-pool size:** 7

### Record 1 — example 1 of 4

**form**: `(str "wa" "tch")` • **expected**: `'watch'`

**concept_phrase**: `the form (str "wa" "tch")`

**question_what**: `the joined string "watch"`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened in the meadow.

Halfway through the morning watch, Will called out
in the meadow, demanding a verdict on the form `(str "wa" "tch")` and refusing
to descend until somebody confirmed it. Will insisted
he already knew the answer. Bob, walking up
at an unhurried pace, simply said: "Submit the form (str "wa" "tch") to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the joined string "watch".

---

{"tool_calls":[{"name":"eval","args":{"form":"(str \"wa\" \"tch\")"}}]}
```

### Record 2 — example 2 of 4

**form**: `(str "flock")` • **expected**: `'flock'`

**concept_phrase**: `the form (str "flock")`

**question_what**: `the value of (str "flock")`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place near the road.

A small slate sat on a flat stone near the road; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(str "flock")`, and the page
heading read the form (str "flock"). Sam nodded at Jess to
write the form properly so the slate would carry an honest entry.

Write a Clojure expression that computes the value of (str "flock").

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(str \"flock\")"}}]}
```

### Record 3 — example 3 of 4

**form**: `(str "x" "y" "z")` • **expected**: `'xyz'`

**concept_phrase**: `the form (str "x" "y" "z")`

**question_what**: `the joined string "xyz"`

```
The boy on the hill thought the trick clever the first time he played it.

George had been laying out a chain of small computations on a
slate at the edge of the village — one operation, then another, all to settle a question
Pat had raised. The current form on the slate was
`(str "x" "y" "z")`, and George explained that the form (str "x" "y" "z") would be
settled the moment the form was evaluated.

Question: write a Clojure expression for the joined string "xyz".

---

{"tool_calls":[{"name":"eval","args":{"form":"(str \"x\" \"y\" \"z\")"}}]}
```

### Record 4 — example 4 of 4

**form**: `(str 1 "+" 2 "=" 3)` • **expected**: `'1+2=3'`

**concept_phrase**: `the form (str 1 "+" 2 "=" 3)`

**question_what**: `the joined string "1+2=3"`

```
The boy on the hill thought the trick clever the first time he played it. This was at the edge of the woods.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(str 1 "+" 2 "=" 3)`, and the line
above it read the form (str 1 "+" 2 "=" 3). Alice handed the page to
Lou, who, drowsy from the warm sun, agreed to write it out properly.

What Clojure form computes the joined string "1+2=3"? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(str 1 \"+\" 2 \"=\" 3)"}}]}
```

### Record 5 — example 1 of 4

**form**: `(str "wa" "tch")` • **expected**: `'watch'`

**concept_phrase**: `the form (str "wa" "tch")`

**question_what**: `the joined string "watch"`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place by the orchard.

A small crowd of villagers had gathered near the orchard to watch
Lou attempt to predict, off the cuff, what the REPL would
return. Carol pointed to the form (str "wa" "tch") and read out the
form aloud: `(str "wa" "tch")`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a form whose evaluation gives the joined string "watch".

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(str \"wa\" \"tch\")"}}]}
```

---

## G2-12: print and println — return values

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 7

### Record 1 — example 1 of 2

**form**: `(println "hello")` • **expected**: `None`

**concept_phrase**: `the form (println "hello")`

**question_what**: `the return value of (println "hello")`

```
The boy on the hill thought the trick clever the first time he played it. This was near the orchard.

Grace kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the orchard the next entry was
the form (println "hello"). Jess peered over her shoulder
at the form `(println "hello")` and was asked, gently, to be the one to
submit it.

Write a Clojure expression that computes the return value of (println "hello").

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(println \"hello\")"}}]}
```

### Record 2 — example 2 of 2

**form**: `(print "x")` • **expected**: `None`

**concept_phrase**: `the form (print "x")`

**question_what**: `the return value of (print "x")`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

The elder of the village kept a small slate by the forest, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the form (print "x"). Oliver read
out the form `(print "x")` so Will could write it
properly into the REPL and earn an honest mark on the slate.

What Clojure form computes the return value of (print "x")? Submit it via `eval`.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(print \"x\")"}}]}
```

### Record 3 — example 1 of 2

**form**: `(println "hello")` • **expected**: `None`

**concept_phrase**: `the form (println "hello")`

**question_what**: `the return value of (println "hello")`

```
The boy on the hill thought the trick clever the first time he played it. It happened along the road.

The elder of the village kept a small slate near the road, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the form (println "hello"). George read
out the form `(println "hello")` so Tom could write it
properly into the REPL and earn an honest mark on the slate.

What Clojure form computes the return value of (println "hello")? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(println \"hello\")"}}]}
```

### Record 4 — example 2 of 2

**form**: `(print "x")` • **expected**: `None`

**concept_phrase**: `the form (print "x")`

**question_what**: `the return value of (print "x")`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A small slate sat on a flat stone on the road; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(print "x")`, and the page
heading read the form (print "x"). Frank nodded at Will to
write the form properly so the slate would carry an honest entry.

Question: write a Clojure expression for the return value of (print "x").

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(print \"x\")"}}]}
```

### Record 5 — example 1 of 2

**form**: `(println "hello")` • **expected**: `None`

**concept_phrase**: `the form (println "hello")`

**question_what**: `the return value of (println "hello")`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

"Whatever `(println "hello")` comes to," Tom declared,
with great whoops of laughter, in the farm, "anyone could see it without typing a thing."
Oliver, stepping deliberately, picked up a stick and drew
the form (println "hello") in the dust. "Then write the form," he
said. "The REPL will have the last word.

What Clojure form computes the return value of (println "hello")? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(println \"hello\")"}}]}
```

---

## G2-13: and / or — short circuit, return values

**Examples:** 6 | **Subplots:** 12 | **Plan-pool size:** 7

### Record 1 — example 1 of 6

**form**: `(and true true)` • **expected**: `True`

**concept_phrase**: `the form (and true true)`

**question_what**: `the value of (and true true)`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden notice nailed to a post at the edge of the woods carried a small puzzle. The
riddle simply asked the reader to evaluate `(and true true)`. Pat
laughed, with great whoops of laughter, and declared it too easy to bother with.
Sam said, patiently, that the only way to be certain of
the form (and true true) was to put it in the REPL.

Write a Clojure expression that computes the value of (and true true).

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(and true true)"}}]}
```

### Record 2 — example 2 of 6

**form**: `(and true false)` • **expected**: `False`

**concept_phrase**: `the form (and true false)`

**question_what**: `the value of (and true false)`

```
The boy on the hill thought the trick clever the first time he played it.

George kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today in the forest the next entry was
the form (and true false). Jess peered over his shoulder
at the form `(and true false)` and was asked, gently, to be the one to
submit it.

Write a Clojure expression that computes the value of (and true false).

---

{"tool_calls":[{"name":"eval","args":{"form":"(and true false)"}}]}
```

### Record 3 — example 3 of 6

**form**: `(or false true)` • **expected**: `True`

**concept_phrase**: `the form (or false true)`

**question_what**: `the value of (or false true)`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

"Whatever `(or false true)` comes to," Jess declared,
as if the race were already won, along the road, "anyone could see it without typing a thing."
Sam, stepping deliberately, picked up a stick and drew
the form (or false true) in the dust. "Then write the form," they
said. "The REPL will have the last word.

Write a Clojure expression that computes the value of (or false true).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(or false true)"}}]}
```

### Record 4 — example 4 of 6

**form**: `(or false false)` • **expected**: `False`

**concept_phrase**: `the form (or false false)`

**question_what**: `the value of (or false false)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Lou called down from a stone by the village where someone had
chalked the form (or false false) on a flat board. Lou, as if the race were already won,
declared she already knew what would come back. Morgan,
stepping deliberately, asked her to actually submit the form
`(or false false)` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a form whose evaluation gives the value of (or false false).

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(or false false)"}}]}
```

### Record 5 — example 5 of 6

**form**: `(and 1 2 3)` • **expected**: `3`

**concept_phrase**: `the form (and 1 2 3)`

**question_what**: `the value of (and 1 2 3)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A wooden notice nailed to a post at the edge of the forest carried a small puzzle. The
riddle simply asked the reader to evaluate `(and 1 2 3)`. Lou
laughed, boasting at every turn, and declared it too easy to bother with.
Grace said, patiently, that the only way to be certain of
the form (and 1 2 3) was to put it in the REPL.

Write a form whose evaluation gives the value of (and 1 2 3).

---

{"tool_calls":[{"name":"eval","args":{"form":"(and 1 2 3)"}}]}
```

---

## G2-14: not — turning truthy to false

**Examples:** 5 | **Subplots:** 12 | **Plan-pool size:** 7

### Record 1 — example 1 of 5

**form**: `(not true)` • **expected**: `False`

**concept_phrase**: `the form (not true)`

**question_what**: `the value of (not true)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Carol had been trying to teach Jess how the REPL
works. "Look here," she said, pointing to the form (not true).
"You hand the form `(not true)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, lulled by the gentle wind, agreed to try.

Question: write a Clojure expression for the value of (not true).

---

{"tool_calls":[{"name":"eval","args":{"form":"(not true)"}}]}
```

### Record 2 — example 2 of 5

**form**: `(not false)` • **expected**: `True`

**concept_phrase**: `the form (not false)`

**question_what**: `the value of (not false)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. This was along the road.

A wooden notice nailed to a post along the road carried a small puzzle. The
riddle simply asked the reader to evaluate `(not false)`. Pat
laughed, with a smug grin, and declared it too easy to bother with.
Grace said, patiently, that the only way to be certain of
the form (not false) was to put it in the REPL.

Question: write a Clojure expression for the value of (not false).

---

{"tool_calls":[{"name":"eval","args":{"form":"(not false)"}}]}
```

### Record 3 — example 3 of 5

**form**: `(not nil)` • **expected**: `True`

**concept_phrase**: `the form (not nil)`

**question_what**: `the value of (not nil)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

"Whatever `(not nil)` comes to," Pat declared,
as if the race were already won, by the orchard, "anyone could see it without typing a thing."
Alice, stepping deliberately, picked up a stick and drew
the form (not nil) in the dust. "Then write the form," she
said. "The REPL will have the last word.

Question: write a Clojure expression for the value of (not nil).

---

{"tool_calls":[{"name":"eval","args":{"form":"(not nil)"}}]}
```

### Record 4 — example 4 of 5

**form**: `(not 0)` • **expected**: `False`

**concept_phrase**: `the form (not 0)`

**question_what**: `the value of (not 0)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Tom called down from a stone at the edge of the farm where someone had
chalked the form (not 0) on a flat board. Tom, with great whoops of laughter,
declared he already knew what would come back. Robin,
saying very little, asked him to actually submit the form
`(not 0)` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a form whose evaluation gives the value of (not 0).

---

{"tool_calls":[{"name":"eval","args":{"form":"(not 0)"}}]}
```

### Record 5 — example 5 of 5

**form**: `(not "")` • **expected**: `False`

**concept_phrase**: `the form (not "")`

**question_what**: `the value of (not "")`

```
Every shepherd in the valley knew the danger of crying wolf for sport. It happened near the road.

"There is no need to evaluate that," Lou said, puffed up with pride.
"Anyone can see what the form (not "") comes to." Bob, who
along the road had heard such claims many times, asked her to
actually write the form `(not "")` and submit it to the REPL —
just to be sure.

Write a Clojure expression that computes the value of (not "").

---

{"tool_calls":[{"name":"eval","args":{"form":"(not \"\")"}}]}
```

---

## G2-15: Falsey values: only false and nil

**Examples:** 4 | **Subplots:** 12 | **Plan-pool size:** 7

### Record 1 — example 1 of 4

**form**: `(if 0 :truthy :falsey)` • **expected**: `':truthy'`

**concept_phrase**: `the form (if 0 :truthy :falsey)`

**question_what**: `which keyword (if 0 :truthy :falsey) returns`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Grace had been laying out a chain of small computations on a
slate near the meadow — one operation, then another, all to settle a question
Lou had raised. The current form on the slate was
`(if 0 :truthy :falsey)`, and Grace explained that the form (if 0 :truthy :falsey) would be
settled the moment the form was evaluated.

What Clojure form computes which keyword (if 0 :truthy :falsey) returns? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(if 0 :truthy :falsey)"}}]}
```

### Record 2 — example 2 of 4

**form**: `(if "" :truthy :falsey)` • **expected**: `':truthy'`

**concept_phrase**: `the form (if "" :truthy :falsey)`

**question_what**: `which keyword (if "" :truthy :falsey) returns`

```
Every shepherd in the valley knew the danger of crying wolf for sport. This was near the hilltop.

Tom called down from a stone atop the hilltop where someone had
chalked the form (if "" :truthy :falsey) on a flat board. Tom, as if the race were already won,
declared he already knew what would come back. Alex,
untroubled by what others thought, asked him to actually submit the form
`(if "" :truthy :falsey)` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes which keyword (if "" :truthy :falsey) returns.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(if \"\" :truthy :falsey)"}}]}
```

### Record 3 — example 3 of 4

**form**: `(if nil :truthy :falsey)` • **expected**: `':falsey'`

**concept_phrase**: `the form (if nil :truthy :falsey)`

**question_what**: `which keyword (if nil :truthy :falsey) returns`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Will called down from a stone near the road where someone had
chalked the form (if nil :truthy :falsey) on a flat board. Will, with great whoops of laughter,
declared he already knew what would come back. Alex,
with steady, careful steps, asked him to actually submit the form
`(if nil :truthy :falsey)` to the REPL — the village had stopped trusting answers
that weren't checked.

What Clojure form computes which keyword (if nil :truthy :falsey) returns? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(if nil :truthy :falsey)"}}]}
```

### Record 4 — example 4 of 4

**form**: `(if false :truthy :falsey)` • **expected**: `':falsey'`

**concept_phrase**: `the form (if false :truthy :falsey)`

**question_what**: `which keyword (if false :truthy :falsey) returns`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened by the forest.

A wooden notice nailed to a post at the edge of the forest carried a small puzzle. The
riddle simply asked the reader to evaluate `(if false :truthy :falsey)`. Lou
laughed, swaggering through the underbrush, and declared it too easy to bother with.
Alex said, patiently, that the only way to be certain of
the form (if false :truthy :falsey) was to put it in the REPL.

Write a Clojure expression that computes which keyword (if false :truthy :falsey) returns.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(if false :truthy :falsey)"}}]}
```

### Record 5 — example 1 of 4

**form**: `(if 0 :truthy :falsey)` • **expected**: `':truthy'`

**concept_phrase**: `the form (if 0 :truthy :falsey)`

**question_what**: `which keyword (if 0 :truthy :falsey) returns`

```
The boy on the hill thought the trick clever the first time he played it. All this took place in the village.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(if 0 :truthy :falsey)`, and the line
above it read the form (if 0 :truthy :falsey). Carol handed the page to
Jess, who, her legs heavy from sprinting, agreed to write it out properly.

Write a Clojure expression that computes which keyword (if 0 :truthy :falsey) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(if 0 :truthy :falsey)"}}]}
```

---

## G2-16: Truthy 0 and empty string

**Examples:** 4 | **Subplots:** 12 | **Plan-pool size:** 7

### Record 1 — example 1 of 4

**form**: `(boolean 0)` • **expected**: `True`

**concept_phrase**: `the form (boolean 0)`

**question_what**: `the truthiness of 0`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Halfway through the morning watch, Pat called out
by the orchard, demanding a verdict on the form `(boolean 0)` and refusing
to descend until somebody confirmed it. Pat insisted
they already knew the answer. Sam, walking up
at an unhurried pace, simply said: "Submit the form (boolean 0) to the
REPL. Whatever comes back is the answer."

Write a form whose evaluation gives the truthiness of 0.

---

{"tool_calls":[{"name":"eval","args":{"form":"(boolean 0)"}}]}
```

### Record 2 — example 2 of 4

**form**: `(boolean "")` • **expected**: `True`

**concept_phrase**: `the form (boolean "")`

**question_what**: `the truthiness of the empty string`

```
The boy on the hill thought the trick clever the first time he played it. All this took place near the village.

"There is no need to evaluate that," Tom said, swaggering through the underbrush.
"Anyone can see what the form (boolean "") comes to." Alice, who
at the edge of the village had heard such claims many times, asked him to
actually write the form `(boolean "")` and submit it to the REPL —
just to be sure.

What Clojure form computes the truthiness of the empty string? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(boolean \"\")"}}]}
```

### Record 3 — example 3 of 4

**form**: `(boolean nil)` • **expected**: `False`

**concept_phrase**: `the form (boolean nil)`

**question_what**: `the truthiness of nil`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened along the road.

A wooden notice nailed to a post on the road carried a small puzzle. The
riddle simply asked the reader to evaluate `(boolean nil)`. Will
laughed, with a smug grin, and declared it too easy to bother with.
George said, patiently, that the only way to be certain of
the form (boolean nil) was to put it in the REPL.

What Clojure form computes the truthiness of nil? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(boolean nil)"}}]}
```

### Record 4 — example 4 of 4

**form**: `(boolean false)` • **expected**: `False`

**concept_phrase**: `the form (boolean false)`

**question_what**: `the truthiness of false`

```
Every shepherd in the valley knew the danger of crying wolf for sport. It happened near the meadow.

Halfway through the morning watch, Will called out
by the meadow, demanding a verdict on the form `(boolean false)` and refusing
to descend until somebody confirmed it. Will insisted
he already knew the answer. Alex, walking up
at an unhurried pace, simply said: "Submit the form (boolean false) to the
REPL. Whatever comes back is the answer."

What Clojure form computes the truthiness of false? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(boolean false)"}}]}
```

### Record 5 — example 1 of 4

**form**: `(boolean 0)` • **expected**: `True`

**concept_phrase**: `the form (boolean 0)`

**question_what**: `the truthiness of 0`

```
The boy on the hill thought the trick clever the first time he played it. This was by the orchard.

Frank kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today at the edge of the orchard the next entry was
the form (boolean 0). Pat peered over his shoulder
at the form `(boolean 0)` and was asked, gently, to be the one to
submit it.

Write a form whose evaluation gives the truthiness of 0.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(boolean 0)"}}]}
```

---

## G2-17: Keyword as function for map lookup

**Examples:** 3 | **Subplots:** 12 | **Plan-pool size:** 7

### Record 1 — example 1 of 3

**form**: `(:wolf {:wolf 1 :flock 2})` • **expected**: `1`

**concept_phrase**: `the form (:wolf {:wolf 1 :flock 2})`

**question_what**: `the value (:wolf {:wolf 1 :flock 2}) returns`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place by the forest.

"There is no need to evaluate that," Will said, with a smug grin.
"Anyone can see what the form (:wolf {:wolf 1 :flock 2}) comes to." Grace, who
in the forest had heard such claims many times, asked him to
actually write the form `(:wolf {:wolf 1 :flock 2})` and submit it to the REPL —
just to be sure.

Question: write a Clojure expression for the value (:wolf {:wolf 1 :flock 2}) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:wolf {:wolf 1 :flock 2})"}}]}
```

### Record 2 — example 2 of 3

**form**: `(:flock {:wolf 1 :flock 2})` • **expected**: `2`

**concept_phrase**: `the form (:flock {:wolf 1 :flock 2})`

**question_what**: `the value (:flock {:wolf 1 :flock 2}) returns`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Frank had been laying out a chain of small computations on a
slate in the orchard — one operation, then another, all to settle a question
Jess had raised. The current form on the slate was
`(:flock {:wolf 1 :flock 2})`, and Frank explained that the form (:flock {:wolf 1 :flock 2}) would be
settled the moment the form was evaluated.

Question: write a Clojure expression for the value (:flock {:wolf 1 :flock 2}) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:flock {:wolf 1 :flock 2})"}}]}
```

### Record 3 — example 3 of 3

**form**: `(:missing {:wolf 1})` • **expected**: `None`

**concept_phrase**: `the form (:missing {:wolf 1})`

**question_what**: `the value when a missing keyword is looked up`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Oliver had been laying out a chain of small computations on a
slate in the forest — one operation, then another, all to settle a question
Jess had raised. The current form on the slate was
`(:missing {:wolf 1})`, and Oliver explained that the form (:missing {:wolf 1}) would be
settled the moment the form was evaluated.

Write a form whose evaluation gives the value when a missing keyword is looked up.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:missing {:wolf 1})"}}]}
```

### Record 4 — example 1 of 3

**form**: `(:wolf {:wolf 1 :flock 2})` • **expected**: `1`

**concept_phrase**: `the form (:wolf {:wolf 1 :flock 2})`

**question_what**: `the value (:wolf {:wolf 1 :flock 2}) returns`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened at the edge of the forest.

Carol had been trying to teach Jess how the REPL
works. "Look here," she said, pointing to the form (:wolf {:wolf 1 :flock 2}).
"You hand the form `(:wolf {:wolf 1 :flock 2})` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, lulled by the gentle wind, agreed to try.

Write a form whose evaluation gives the value (:wolf {:wolf 1 :flock 2}) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:wolf {:wolf 1 :flock 2})"}}]}
```

### Record 5 — example 2 of 3

**form**: `(:flock {:wolf 1 :flock 2})` • **expected**: `2`

**concept_phrase**: `the form (:flock {:wolf 1 :flock 2})`

**question_what**: `the value (:flock {:wolf 1 :flock 2}) returns`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place near the forest.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(:flock {:wolf 1 :flock 2})`, and the line
above it read the form (:flock {:wolf 1 :flock 2}). Morgan handed the page to
Will, who, weary from the morning's effort, agreed to write it out properly.

Write a form whose evaluation gives the value (:flock {:wolf 1 :flock 2}) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:flock {:wolf 1 :flock 2})"}}]}
```

---

## G2-18: Quoting symbols

**Examples:** 3 | **Subplots:** 12 | **Plan-pool size:** 7

### Record 1 — example 1 of 3

**form**: `(quote wolf)` • **expected**: `'wolf'`

**concept_phrase**: `the quoted symbol (quote wolf)`

**question_what**: `the value of (quote wolf)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A small crowd of villagers had gathered near the meadow to watch
Pat attempt to predict, off the cuff, what the REPL would
return. Alice pointed to the quoted symbol (quote wolf) and read out the
form aloud: `(quote wolf)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a Clojure expression that computes the value of (quote wolf).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(quote wolf)"}}]}
```

### Record 2 — example 2 of 3

**form**: `'flock` • **expected**: `'flock'`

**concept_phrase**: `the quoted symbol 'flock`

**question_what**: `the value of 'flock`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Robin had been trying to teach Jess how the REPL
works. "Look here," they said, pointing to the quoted symbol 'flock.
"You hand the form `'flock` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, weary from the morning's effort, agreed to try.

Write a Clojure expression that computes the value of 'flock.

---

{"tool_calls":[{"name":"eval","args":{"form":"'flock"}}]}
```

### Record 3 — example 3 of 3

**form**: `'(1 2 3)` • **expected**: `[1, 2, 3]`

**concept_phrase**: `the quoted list '(1 2 3)`

**question_what**: `the value of '(1 2 3)`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place near the orchard.

Halfway through the morning watch, Will called out
at the edge of the orchard, demanding a verdict on the form `'(1 2 3)` and refusing
to descend until somebody confirmed it. Will insisted
he already knew the answer. Robin, walking up
at an unhurried pace, simply said: "Submit the quoted list '(1 2 3) to the
REPL. Whatever comes back is the answer."

What Clojure form computes the value of '(1 2 3)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### Record 4 — example 1 of 3

**form**: `(quote wolf)` • **expected**: `'wolf'`

**concept_phrase**: `the quoted symbol (quote wolf)`

**question_what**: `the value of (quote wolf)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened at the edge of the village.

Alice had been trying to teach Lou how the REPL
works. "Look here," she said, pointing to the quoted symbol (quote wolf).
"You hand the form `(quote wolf)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Lou, weary from the morning's effort, agreed to try.

Write a Clojure expression that computes the value of (quote wolf).

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(quote wolf)"}}]}
```

### Record 5 — example 2 of 3

**form**: `'flock` • **expected**: `'flock'`

**concept_phrase**: `the quoted symbol 'flock`

**question_what**: `the value of 'flock`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Tom called down from a stone in the orchard where someone had
chalked the quoted symbol 'flock on a flat board. Tom, as if the race were already won,
declared he already knew what would come back. Morgan,
her eyes always on the path, asked him to actually submit the form
`'flock` to the REPL — the village had stopped trusting answers
that weren't checked.

Question: write a Clojure expression for the value of 'flock.

---

{"tool_calls":[{"name":"eval","args":{"form":"'flock"}}]}
```

---

## G2-19: Auto-promotion to bigint

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 7

### Record 1 — example 1 of 2

**form**: `(* 1000000 1000000)` • **expected**: `1000000000000`

**concept_phrase**: `the form (* 1000000 1000000)`

**question_what**: `the result of one million times one million`

```
The boy on the hill thought the trick clever the first time he played it.

Carol had been laying out a chain of small computations on a
slate in the meadow — one operation, then another, all to settle a question
Jess had raised. The current form on the slate was
`(* 1000000 1000000)`, and Carol explained that the form (* 1000000 1000000) would be
settled the moment the form was evaluated.

Write a form whose evaluation gives the result of one million times one million.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(* 1000000 1000000)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(+ 99999999999 1)` • **expected**: `100000000000`

**concept_phrase**: `the form (+ 99999999999 1)`

**question_what**: `the result of 99999999999 plus 1`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Jess called down from a stone at the edge of the woods where someone had
chalked the form (+ 99999999999 1) on a flat board. Jess, puffed up with pride,
declared she already knew what would come back. Oliver,
with steady, careful steps, asked her to actually submit the form
`(+ 99999999999 1)` to the REPL — the village had stopped trusting answers
that weren't checked.

What Clojure form computes the result of 99999999999 plus 1? Submit it via `eval`.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 99999999999 1)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(* 1000000 1000000)` • **expected**: `1000000000000`

**concept_phrase**: `the form (* 1000000 1000000)`

**question_what**: `the result of one million times one million`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

"Whatever `(* 1000000 1000000)` comes to," Tom declared,
with a smug grin, atop the hilltop, "anyone could see it without typing a thing."
Alice, untroubled by what others thought, picked up a stick and drew
the form (* 1000000 1000000) in the dust. "Then write the form," she
said. "The REPL will have the last word.

Question: write a Clojure expression for the result of one million times one million.

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 1000000 1000000)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(+ 99999999999 1)` • **expected**: `100000000000`

**concept_phrase**: `the form (+ 99999999999 1)`

**question_what**: `the result of 99999999999 plus 1`

```
Every shepherd in the valley knew the danger of crying wolf for sport. This was atop the hilltop.

Alex had been trying to teach Jess how the REPL
works. "Look here," they said, pointing to the form (+ 99999999999 1).
"You hand the form `(+ 99999999999 1)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, weary from the morning's effort, agreed to try.

Question: write a Clojure expression for the result of 99999999999 plus 1.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 99999999999 1)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(* 1000000 1000000)` • **expected**: `1000000000000`

**concept_phrase**: `the form (* 1000000 1000000)`

**question_what**: `the result of one million times one million`

```
Every shepherd in the valley knew the danger of crying wolf for sport. It happened near the road.

"There is no need to evaluate that," Jess said, swaggering through the underbrush.
"Anyone can see what the form (* 1000000 1000000) comes to." Grace, who
on the road had heard such claims many times, asked her to
actually write the form `(* 1000000 1000000)` and submit it to the REPL —
just to be sure.

Write a form whose evaluation gives the result of one million times one million.

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 1000000 1000000)"}}]}
```

---

## G2-20: Counting

**Examples:** 3 | **Subplots:** 12 | **Plan-pool size:** 7

### Record 1 — example 1 of 3

**form**: `(count [1 2 3])` • **expected**: `3`

**concept_phrase**: `the count of [1 2 3]`

**question_what**: `the count of the vector [1 2 3]`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened in the village.

Frank kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today in the village the next entry was
the count of [1 2 3]. Will peered over his shoulder
at the form `(count [1 2 3])` and was asked, gently, to be the one to
submit it.

What Clojure form computes the count of the vector [1 2 3]? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count [1 2 3])"}}]}
```

### Record 2 — example 2 of 3

**form**: `(count "hello")` • **expected**: `5`

**concept_phrase**: `the count of "hello"`

**question_what**: `the length of the string "hello"`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

"There is no need to evaluate that," Lou said, with great whoops of laughter.
"Anyone can see what the count of "hello" comes to." George, who
in the meadow had heard such claims many times, asked her to
actually write the form `(count "hello")` and submit it to the REPL —
just to be sure.

Question: write a Clojure expression for the length of the string "hello".

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"hello\")"}}]}
```

### Record 3 — example 3 of 3

**form**: `(count [])` • **expected**: `0`

**concept_phrase**: `the count of an empty vector`

**question_what**: `the count of an empty vector`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Oliver had been laying out a chain of small computations on a
slate near the road — one operation, then another, all to settle a question
Jess had raised. The current form on the slate was
`(count [])`, and Oliver explained that the count of an empty vector would be
settled the moment the form was evaluated.

What Clojure form computes the count of an empty vector? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(count [])"}}]}
```

### Record 4 — example 1 of 3

**form**: `(count [1 2 3])` • **expected**: `3`

**concept_phrase**: `the count of [1 2 3]`

**question_what**: `the count of the vector [1 2 3]`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Alice had been laying out a chain of small computations on a
slate at the edge of the forest — one operation, then another, all to settle a question
Pat had raised. The current form on the slate was
`(count [1 2 3])`, and Alice explained that the count of [1 2 3] would be
settled the moment the form was evaluated.

What Clojure form computes the count of the vector [1 2 3]? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(count [1 2 3])"}}]}
```

### Record 5 — example 2 of 3

**form**: `(count "hello")` • **expected**: `5`

**concept_phrase**: `the count of "hello"`

**question_what**: `the length of the string "hello"`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Sam had been trying to teach Will how the REPL
works. "Look here," they said, pointing to the count of "hello".
"You hand the form `(count "hello")` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Will, drowsy from the warm sun, agreed to try.

Write a Clojure expression that computes the length of the string "hello".

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"hello\")"}}]}
```

---

## G2-21: String length and substring

**Examples:** 3 | **Subplots:** 12 | **Plan-pool size:** 7

### Record 1 — example 1 of 3

**form**: `(count "shepherd")` • **expected**: `8`

**concept_phrase**: `the length of "shepherd"`

**question_what**: `the length of the string "shepherd"`

```
The boy on the hill thought the trick clever the first time he played it.

Halfway through the morning watch, Will called out
near the orchard, demanding a verdict on the form `(count "shepherd")` and refusing
to descend until somebody confirmed it. Will insisted
he already knew the answer. Morgan, walking up
at an unhurried pace, simply said: "Submit the length of "shepherd" to the
REPL. Whatever comes back is the answer."

Write a Clojure expression that computes the length of the string "shepherd".

---

{"tool_calls":[{"name":"eval","args":{"form":"(count \"shepherd\")"}}]}
```

### Record 2 — example 2 of 3

**form**: `(count "wolf")` • **expected**: `4`

**concept_phrase**: `the length of "wolf"`

**question_what**: `the length of the string "wolf"`

```
The boy on the hill thought the trick clever the first time he played it.

Grace kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today at the edge of the orchard the next entry was
the length of "wolf". Lou peered over her shoulder
at the form `(count "wolf")` and was asked, gently, to be the one to
submit it.

What Clojure form computes the length of the string "wolf"? Submit it via `eval`.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"wolf\")"}}]}
```

### Record 3 — example 3 of 3

**form**: `(subs "shepherd" 0 3)` • **expected**: `'she'`

**concept_phrase**: `the form (subs "shepherd" 0 3)`

**question_what**: `the first three characters of "shepherd"`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Pat called down from a stone near the farm where someone had
chalked the form (subs "shepherd" 0 3) on a flat board. Pat, with a smug grin,
declared they already knew what would come back. George,
saying very little, asked them to actually submit the form
`(subs "shepherd" 0 3)` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a form whose evaluation gives the first three characters of "shepherd".

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(subs \"shepherd\" 0 3)"}}]}
```

### Record 4 — example 1 of 3

**form**: `(count "shepherd")` • **expected**: `8`

**concept_phrase**: `the length of "shepherd"`

**question_what**: `the length of the string "shepherd"`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden notice nailed to a post in the farm carried a small puzzle. The
riddle simply asked the reader to evaluate `(count "shepherd")`. Lou
laughed, with a smug grin, and declared it too easy to bother with.
George said, patiently, that the only way to be certain of
the length of "shepherd" was to put it in the REPL.

What Clojure form computes the length of the string "shepherd"? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"shepherd\")"}}]}
```

### Record 5 — example 2 of 3

**form**: `(count "wolf")` • **expected**: `4`

**concept_phrase**: `the length of "wolf"`

**question_what**: `the length of the string "wolf"`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Frank kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today by the village the next entry was
the length of "wolf". Pat peered over his shoulder
at the form `(count "wolf")` and was asked, gently, to be the one to
submit it.

Write a form whose evaluation gives the length of the string "wolf".

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"wolf\")"}}]}
```

---

## G2-22: Compose pure arithmetic (multi-step calculation)

**Examples:** 3 | **Subplots:** 12 | **Plan-pool size:** 7

### Record 1 — example 1 of 3

**form**: `(- (* 5 4) 7)` • **expected**: `13`

**concept_phrase**: `the form (- (* 5 4) 7)`

**question_what**: `5 sheep per pen across 4 pens, minus 7 strays`

```
Every shepherd in the valley knew the danger of crying wolf for sport. It happened along the road.

Halfway through the morning watch, Jess called out
along the road, demanding a verdict on the form `(- (* 5 4) 7)` and refusing
to descend until somebody confirmed it. Jess insisted
she already knew the answer. Frank, walking up
at an unhurried pace, simply said: "Submit the form (- (* 5 4) 7) to the
REPL. Whatever comes back is the answer."

Write a Clojure expression that computes 5 sheep per pen across 4 pens, minus 7 strays.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(- (* 5 4) 7)"}}]}
```

### Record 2 — example 2 of 3

**form**: `(+ (* 3 8) (* 2 4))` • **expected**: `32`

**concept_phrase**: `the sum of two products`

**question_what**: `3*8 + 2*4`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

The elder of the village kept a small slate at the edge of the meadow, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the sum of two products. Alice read
out the form `(+ (* 3 8) (* 2 4))` so Tom could write it
properly into the REPL and earn an honest mark on the slate.

Write a form whose evaluation gives 3*8 + 2*4.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(+ (* 3 8) (* 2 4))"}}]}
```

### Record 3 — example 3 of 3

**form**: `(quot (+ 100 50) 5)` • **expected**: `30`

**concept_phrase**: `the form (quot (+ 100 50) 5)`

**question_what**: `150 divided by 5`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

"There is no need to evaluate that," Jess said, puffed up with pride.
"Anyone can see what the form (quot (+ 100 50) 5) comes to." Morgan, who
at the edge of the farm had heard such claims many times, asked her to
actually write the form `(quot (+ 100 50) 5)` and submit it to the REPL —
just to be sure.

Question: write a Clojure expression for 150 divided by 5.

---

{"tool_calls":[{"name":"eval","args":{"form":"(quot (+ 100 50) 5)"}}]}
```

### Record 4 — example 1 of 3

**form**: `(- (* 5 4) 7)` • **expected**: `13`

**concept_phrase**: `the form (- (* 5 4) 7)`

**question_what**: `5 sheep per pen across 4 pens, minus 7 strays`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Alex had been trying to teach Will how the REPL
works. "Look here," they said, pointing to the form (- (* 5 4) 7).
"You hand the form `(- (* 5 4) 7)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Will, her legs heavy from sprinting, agreed to try.

What Clojure form computes 5 sheep per pen across 4 pens, minus 7 strays? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(- (* 5 4) 7)"}}]}
```

### Record 5 — example 2 of 3

**form**: `(+ (* 3 8) (* 2 4))` • **expected**: `32`

**concept_phrase**: `the sum of two products`

**question_what**: `3*8 + 2*4`

```
The boy on the hill thought the trick clever the first time he played it.

"Whatever `(+ (* 3 8) (* 2 4))` comes to," Jess declared,
boasting at every turn, at the edge of the woods, "anyone could see it without typing a thing."
Alex, her eyes always on the path, picked up a stick and drew
the sum of two products in the dust. "Then write the form," they
said. "The REPL will have the last word.

Question: write a Clojure expression for 3*8 + 2*4.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ (* 3 8) (* 2 4))"}}]}
```

---

