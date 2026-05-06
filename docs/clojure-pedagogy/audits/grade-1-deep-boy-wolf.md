# Boy-wolf Grade 1 — deep spot-check

5 generated records per subject (across all examples and a variety of seeds). Read every record carefully. Flag anything that reads odd to a careful reader, including issues the structural audit can't catch (prose flow, contextual fit, cliché repetition, subplot/example mismatch, etc.)

---

## G1-01: Eval as substitution

**Examples:** 8 | **Subplots:** 10 | **Plan-pool size:** 7

### Record 1 — example 1 of 8

**form**: `42` • **expected**: `42`

**concept_phrase**: `the value 42`

**question_what**: `the value of 42`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

"There is no need to evaluate that," Pat said, puffed up with pride.
"Anyone can see what the value 42 comes to." Alice, who
near the woods had heard such claims many times, asked them to
actually write the form `42` and submit it to the REPL —
just to be sure.

Write a Clojure expression that computes the value of 42.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
```

### Record 2 — example 2 of 8

**form**: `0` • **expected**: `0`

**concept_phrase**: `the value 0`

**question_what**: `the value of 0`

```
The boy on the hill thought the trick clever the first time he played it.

Lou called down from a stone in the village where someone had
chalked the value 0 on a flat board. Lou, puffed up with pride,
declared she already knew what would come back. Sam,
untroubled by what others thought, asked her to actually submit the form
`0` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the value of 0.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"0"}}]}
```

### Record 3 — example 3 of 8

**form**: `(+ 1 2)` • **expected**: `3`

**concept_phrase**: `the form (+ 1 2)`

**question_what**: `the result of (+ 1 2)`

```
Every shepherd in the valley knew the danger of crying wolf for sport. This was near the road.

Tom called down from a stone on the road where someone had
chalked the form (+ 1 2) on a flat board. Tom, swaggering through the underbrush,
declared he already knew what would come back. George,
with steady, careful steps, asked him to actually submit the form
`(+ 1 2)` to the REPL — the village had stopped trusting answers
that weren't checked.

Question: write a Clojure expression for the result of (+ 1 2).

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### Record 4 — example 4 of 8

**form**: `(* 4 5)` • **expected**: `20`

**concept_phrase**: `the form (* 4 5)`

**question_what**: `the result of (* 4 5)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

"There is no need to evaluate that," Will said, puffed up with pride.
"Anyone can see what the form (* 4 5) comes to." Alice, who
near the orchard had heard such claims many times, asked him to
actually write the form `(* 4 5)` and submit it to the REPL —
just to be sure.

What Clojure form computes the result of (* 4 5)? Submit it via `eval`.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(* 4 5)"}}]}
```

### Record 5 — example 5 of 8

**form**: `(- 10 (+ 2 3))` • **expected**: `5`

**concept_phrase**: `the nested form (- 10 (+ 2 3))`

**question_what**: `the result of (- 10 (+ 2 3))`

```
Every shepherd in the valley knew the danger of crying wolf for sport. This was near the orchard.

"There is no need to evaluate that," Tom said, with great whoops of laughter.
"Anyone can see what the nested form (- 10 (+ 2 3)) comes to." Grace, who
in the orchard had heard such claims many times, asked him to
actually write the form `(- 10 (+ 2 3))` and submit it to the REPL —
just to be sure.

What Clojure form computes the result of (- 10 (+ 2 3))? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(- 10 (+ 2 3))"}}]}
```

---

## G1-02: Integer numbers

**Examples:** 6 | **Subplots:** 10 | **Plan-pool size:** 7

### Record 1 — example 1 of 6

**form**: `7` • **expected**: `7`

**concept_phrase**: `the integer 7`

**question_what**: `the value of the integer 7`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Will called down from a stone by the orchard where someone had
chalked the integer 7 on a flat board. Will, with a smug grin,
declared he already knew what would come back. Morgan,
stepping deliberately, asked him to actually submit the form
`7` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a form whose evaluation gives the value of the integer 7.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"7"}}]}
```

### Record 2 — example 2 of 6

**form**: `-3` • **expected**: `-3`

**concept_phrase**: `the integer -3`

**question_what**: `the value of the integer -3`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place by the woods.

A wooden notice nailed to a post at the edge of the woods carried a small puzzle. The
riddle simply asked the reader to evaluate `-3`. Tom
laughed, boasting at every turn, and declared it too easy to bother with.
Grace said, patiently, that the only way to be certain of
the integer -3 was to put it in the REPL.

Write a Clojure expression that computes the value of the integer -3.

---

{"tool_calls":[{"name":"eval","args":{"form":"-3"}}]}
```

### Record 3 — example 3 of 6

**form**: `0` • **expected**: `0`

**concept_phrase**: `the integer 0`

**question_what**: `the value of zero`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

"There is no need to evaluate that," Pat said, with great whoops of laughter.
"Anyone can see what the integer 0 comes to." Oliver, who
at the edge of the orchard had heard such claims many times, asked them to
actually write the form `0` and submit it to the REPL —
just to be sure.

Write a Clojure expression that computes the value of zero.

---

{"tool_calls":[{"name":"eval","args":{"form":"0"}}]}
```

### Record 4 — example 4 of 6

**form**: `100` • **expected**: `100`

**concept_phrase**: `the integer 100`

**question_what**: `the value of one hundred`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Grace had been trying to teach Tom how the REPL
works. "Look here," she said, pointing to the integer 100.
"You hand the form `100` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Tom, drowsy from the warm sun, agreed to try.

Write a Clojure expression that computes the value of one hundred.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"100"}}]}
```

### Record 5 — example 5 of 6

**form**: `-25` • **expected**: `-25`

**concept_phrase**: `the integer -25`

**question_what**: `the value of negative twenty-five`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place on the road.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `-25`, and the line
above it read the integer -25. Carol handed the page to
Will, who, her legs heavy from sprinting, agreed to write it out properly.

What Clojure form computes the value of negative twenty-five? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"-25"}}]}
```

---

## G1-03: Ratios

**Examples:** 5 | **Subplots:** 10 | **Plan-pool size:** 7

### Record 1 — example 1 of 5

**form**: `1/2` • **expected**: `'1/2'`

**concept_phrase**: `the ratio 1/2`

**question_what**: `the value of the ratio 1/2`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place at the edge of the village.

Alice kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the village the next entry was
the ratio 1/2. Will peered over her shoulder
at the form `1/2` and was asked, gently, to be the one to
submit it.

Write a Clojure expression that computes the value of the ratio 1/2.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"1/2"}}]}
```

### Record 2 — example 2 of 5

**form**: `3/4` • **expected**: `'3/4'`

**concept_phrase**: `the ratio 3/4`

**question_what**: `the value of three-quarters`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened near the meadow.

Oliver kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the meadow the next entry was
the ratio 3/4. Lou peered over his shoulder
at the form `3/4` and was asked, gently, to be the one to
submit it.

Write a form whose evaluation gives the value of three-quarters.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"3/4"}}]}
```

### Record 3 — example 3 of 5

**form**: `(+ 1/2 1/4)` • **expected**: `'3/4'`

**concept_phrase**: `the form (+ 1/2 1/4)`

**question_what**: `the value of (+ 1/2 1/4)`

```
Every shepherd in the valley knew the danger of crying wolf for sport. It happened at the edge of the orchard.

A small crowd of villagers had gathered by the orchard to watch
Pat attempt to predict, off the cuff, what the REPL would
return. George pointed to the form (+ 1/2 1/4) and read out the
form aloud: `(+ 1/2 1/4)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a form whose evaluation gives the value of (+ 1/2 1/4).

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1/2 1/4)"}}]}
```

### Record 4 — example 4 of 5

**form**: `(* 2 1/2)` • **expected**: `1`

**concept_phrase**: `the form (* 2 1/2)`

**question_what**: `the value of (* 2 1/2)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

"There is no need to evaluate that," Lou said, with great whoops of laughter.
"Anyone can see what the form (* 2 1/2) comes to." Robin, who
in the village had heard such claims many times, asked her to
actually write the form `(* 2 1/2)` and submit it to the REPL —
just to be sure.

Write a form whose evaluation gives the value of (* 2 1/2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 2 1/2)"}}]}
```

### Record 5 — example 5 of 5

**form**: `(- 1 1/3)` • **expected**: `'2/3'`

**concept_phrase**: `the form (- 1 1/3)`

**question_what**: `the value of (- 1 1/3)`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden notice nailed to a post at the edge of the village carried a small puzzle. The
riddle simply asked the reader to evaluate `(- 1 1/3)`. Tom
laughed, with a smug grin, and declared it too easy to bother with.
Alex said, patiently, that the only way to be certain of
the form (- 1 1/3) was to put it in the REPL.

Question: write a Clojure expression for the value of (- 1 1/3).

---

{"tool_calls":[{"name":"eval","args":{"form":"(- 1 1/3)"}}]}
```

---

## G1-04: Strings

**Examples:** 5 | **Subplots:** 10 | **Plan-pool size:** 7

### Record 1 — example 1 of 5

**form**: `"hello"` • **expected**: `'hello'`

**concept_phrase**: `the string "hello"`

**question_what**: `the value of "hello"`

```
The boy on the hill thought the trick clever the first time he played it.

A wooden notice nailed to a post near the farm carried a small puzzle. The
riddle simply asked the reader to evaluate `"hello"`. Pat
laughed, with great whoops of laughter, and declared it too easy to bother with.
Bob said, patiently, that the only way to be certain of
the string "hello" was to put it in the REPL.

Write a Clojure expression that computes the value of "hello".

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"\"hello\""}}]}
```

### Record 2 — example 2 of 5

**form**: `"flock"` • **expected**: `'flock'`

**concept_phrase**: `the string "flock"`

**question_what**: `the value of "flock"`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened at the edge of the village.

A wooden notice nailed to a post near the village carried a small puzzle. The
riddle simply asked the reader to evaluate `"flock"`. Jess
laughed, swaggering through the underbrush, and declared it too easy to bother with.
George said, patiently, that the only way to be certain of
the string "flock" was to put it in the REPL.

Write a Clojure expression that computes the value of "flock".

---

{"tool_calls":[{"name":"eval","args":{"form":"\"flock\""}}]}
```

### Record 3 — example 3 of 5

**form**: `"watch the meadow"` • **expected**: `'watch the meadow'`

**concept_phrase**: `the string "watch the meadow"`

**question_what**: `the value of "watch the meadow"`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. This was by the village.

A small crowd of villagers had gathered at the edge of the village to watch
Jess attempt to predict, off the cuff, what the REPL would
return. Grace pointed to the string "watch the meadow" and read out the
form aloud: `"watch the meadow"`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

What Clojure form computes the value of "watch the meadow"? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"\"watch the meadow\""}}]}
```

### Record 4 — example 4 of 5

**form**: `""` • **expected**: `''`

**concept_phrase**: `the empty string`

**question_what**: `the value of the empty string`

```
The boy on the hill thought the trick clever the first time he played it. All this took place by the farm.

A wooden notice nailed to a post in the farm carried a small puzzle. The
riddle simply asked the reader to evaluate `""`. Pat
laughed, swaggering through the underbrush, and declared it too easy to bother with.
Frank said, patiently, that the only way to be certain of
the empty string was to put it in the REPL.

Question: write a Clojure expression for the value of the empty string.

---

{"tool_calls":[{"name":"eval","args":{"form":"\"\""}}]}
```

### Record 5 — example 5 of 5

**form**: `"42"` • **expected**: `'42'`

**concept_phrase**: `the string "42"`

**question_what**: `the value of the string "42"`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened in the forest.

Robin had been trying to teach Will how the REPL
works. "Look here," they said, pointing to the string "42".
"You hand the form `"42"` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Will, weary from the morning's effort, agreed to try.

Write a form whose evaluation gives the value of the string "42".

---

{"tool_calls":[{"name":"eval","args":{"form":"\"42\""}}]}
```

---

## G1-05: Booleans

**Examples:** 6 | **Subplots:** 10 | **Plan-pool size:** 7

### Record 1 — example 1 of 6

**form**: `true` • **expected**: `True`

**concept_phrase**: `the literal true`

**question_what**: `the value of true`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A small crowd of villagers had gathered near the hilltop to watch
Jess attempt to predict, off the cuff, what the REPL would
return. Alice pointed to the literal true and read out the
form aloud: `true`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Question: write a Clojure expression for the value of true.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"true"}}]}
```

### Record 2 — example 2 of 6

**form**: `false` • **expected**: `False`

**concept_phrase**: `the literal false`

**question_what**: `the value of false`

```
The boy on the hill thought the trick clever the first time he played it.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `false`, and the line
above it read the literal false. Alex handed the page to
Tom, who, drowsy from the warm sun, agreed to write it out properly.

What Clojure form computes the value of false? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"false"}}]}
```

### Record 3 — example 3 of 6

**form**: `(= 1 1)` • **expected**: `True`

**concept_phrase**: `the equality (= 1 1)`

**question_what**: `the value of (= 1 1)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

The elder of the village kept a small slate by the forest, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the equality (= 1 1). Carol read
out the form `(= 1 1)` so Will could write it
properly into the REPL and earn an honest mark on the slate.

Question: write a Clojure expression for the value of (= 1 1).

---

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 1)"}}]}
```

### Record 4 — example 4 of 6

**form**: `(= 1 2)` • **expected**: `False`

**concept_phrase**: `the equality (= 1 2)`

**question_what**: `the value of (= 1 2)`

```
The boy on the hill thought the trick clever the first time he played it.

A wooden notice nailed to a post in the orchard carried a small puzzle. The
riddle simply asked the reader to evaluate `(= 1 2)`. Jess
laughed, with a smug grin, and declared it too easy to bother with.
Morgan said, patiently, that the only way to be certain of
the equality (= 1 2) was to put it in the REPL.

Write a form whose evaluation gives the value of (= 1 2).

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 2)"}}]}
```

### Record 5 — example 5 of 6

**form**: `(< 3 5)` • **expected**: `True`

**concept_phrase**: `the comparison (< 3 5)`

**question_what**: `the value of (< 3 5)`

```
The boy on the hill thought the trick clever the first time he played it. It happened in the orchard.

Halfway through the morning watch, Tom called out
near the orchard, demanding a verdict on the form `(< 3 5)` and refusing
to descend until somebody confirmed it. Tom insisted
he already knew the answer. Oliver, walking up
at an unhurried pace, simply said: "Submit the comparison (< 3 5) to the
REPL. Whatever comes back is the answer."

What Clojure form computes the value of (< 3 5)? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(< 3 5)"}}]}
```

---

## G1-06: nil

**Examples:** 5 | **Subplots:** 10 | **Plan-pool size:** 7

### Record 1 — example 1 of 5

**form**: `nil` • **expected**: `None`

**concept_phrase**: `the literal nil`

**question_what**: `the value of nil`

```
The boy on the hill thought the trick clever the first time he played it.

A wooden notice nailed to a post atop the hilltop carried a small puzzle. The
riddle simply asked the reader to evaluate `nil`. Will
laughed, swaggering through the underbrush, and declared it too easy to bother with.
Frank said, patiently, that the only way to be certain of
the literal nil was to put it in the REPL.

Write a Clojure expression that computes the value of nil.

---

{"tool_calls":[{"name":"eval","args":{"form":"nil"}}]}
```

### Record 2 — example 2 of 5

**form**: `(nil? nil)` • **expected**: `True`

**concept_phrase**: `the predicate (nil? nil)`

**question_what**: `whether nil is nil`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A small crowd of villagers had gathered near the woods to watch
Pat attempt to predict, off the cuff, what the REPL would
return. Robin pointed to the predicate (nil? nil) and read out the
form aloud: `(nil? nil)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

What Clojure form computes whether nil is nil? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(nil? nil)"}}]}
```

### Record 3 — example 3 of 5

**form**: `(nil? 0)` • **expected**: `False`

**concept_phrase**: `the predicate (nil? 0)`

**question_what**: `whether 0 is nil`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A small slate sat on a flat stone by the meadow; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(nil? 0)`, and the page
heading read the predicate (nil? 0). Robin nodded at Tom to
write the form properly so the slate would carry an honest entry.

Question: write a Clojure expression for whether 0 is nil.

---

{"tool_calls":[{"name":"eval","args":{"form":"(nil? 0)"}}]}
```

### Record 4 — example 4 of 5

**form**: `(nil? false)` • **expected**: `False`

**concept_phrase**: `the predicate (nil? false)`

**question_what**: `whether false is nil`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(nil? false)`, and the line
above it read the predicate (nil? false). Sam handed the page to
Will, who, lulled by the gentle wind, agreed to write it out properly.

What Clojure form computes whether false is nil? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(nil? false)"}}]}
```

### Record 5 — example 5 of 5

**form**: `(= nil nil)` • **expected**: `True`

**concept_phrase**: `the equality (= nil nil)`

**question_what**: `the value of (= nil nil)`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Halfway through the morning watch, Tom called out
at the edge of the hilltop, demanding a verdict on the form `(= nil nil)` and refusing
to descend until somebody confirmed it. Tom insisted
he already knew the answer. Frank, walking up
at an unhurried pace, simply said: "Submit the equality (= nil nil) to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the value of (= nil nil).

---

{"tool_calls":[{"name":"eval","args":{"form":"(= nil nil)"}}]}
```

---

## G1-07: Keywords

**Examples:** 5 | **Subplots:** 10 | **Plan-pool size:** 7

### Record 1 — example 1 of 5

**form**: `:wolf` • **expected**: `':wolf'`

**concept_phrase**: `the keyword :wolf`

**question_what**: `the value of :wolf`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Robin had been trying to teach Tom how the REPL
works. "Look here," they said, pointing to the keyword :wolf.
"You hand the form `:wolf` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Tom, lulled by the gentle wind, agreed to try.

What Clojure form computes the value of :wolf? Submit it via `eval`.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":":wolf"}}]}
```

### Record 2 — example 2 of 5

**form**: `:flock` • **expected**: `':flock'`

**concept_phrase**: `the keyword :flock`

**question_what**: `the value of :flock`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place near the meadow.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `:flock`, and the line
above it read the keyword :flock. Oliver handed the page to
Jess, who, drowsy from the warm sun, agreed to write it out properly.

Write a Clojure expression that computes the value of :flock.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":":flock"}}]}
```

### Record 3 — example 3 of 5

**form**: `:alarm` • **expected**: `':alarm'`

**concept_phrase**: `the keyword :alarm`

**question_what**: `the value of :alarm`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Lou called down from a stone near the village where someone had
chalked the keyword :alarm on a flat board. Lou, boasting at every turn,
declared she already knew what would come back. Frank,
without complaint, asked her to actually submit the form
`:alarm` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the value of :alarm.

---

{"tool_calls":[{"name":"eval","args":{"form":":alarm"}}]}
```

### Record 4 — example 4 of 5

**form**: `(keyword? :wolf)` • **expected**: `True`

**concept_phrase**: `the predicate (keyword? :wolf)`

**question_what**: `whether :wolf is a keyword`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened atop the hilltop.

Halfway through the morning watch, Will called out
on the hilltop, demanding a verdict on the form `(keyword? :wolf)` and refusing
to descend until somebody confirmed it. Will insisted
he already knew the answer. Alice, walking up
at an unhurried pace, simply said: "Submit the predicate (keyword? :wolf) to the
REPL. Whatever comes back is the answer."

Write a form whose evaluation gives whether :wolf is a keyword.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(keyword? :wolf)"}}]}
```

### Record 5 — example 5 of 5

**form**: `(= :wolf :wolf)` • **expected**: `True`

**concept_phrase**: `the equality of two :wolf keywords`

**question_what**: `whether :wolf equals :wolf`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A small crowd of villagers had gathered at the edge of the woods to watch
Pat attempt to predict, off the cuff, what the REPL would
return. Carol pointed to the equality of two :wolf keywords and read out the
form aloud: `(= :wolf :wolf)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a Clojure expression that computes whether :wolf equals :wolf.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(= :wolf :wolf)"}}]}
```

---

## G1-08: Characters

**Examples:** 4 | **Subplots:** 10 | **Plan-pool size:** 7

### Record 1 — example 1 of 4

**form**: `\w` • **expected**: `'w'`

**concept_phrase**: `the character \w`

**question_what**: `the value of \w`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened near the orchard.

"There is no need to evaluate that," Tom said, with a smug grin.
"Anyone can see what the character \w comes to." Oliver, who
in the orchard had heard such claims many times, asked him to
actually write the form `\w` and submit it to the REPL —
just to be sure.

Write a form whose evaluation gives the value of \w.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"\\w"}}]}
```

### Record 2 — example 2 of 4

**form**: `\space` • **expected**: `' '`

**concept_phrase**: `the character \space`

**question_what**: `the value of \space`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened by the orchard.

Halfway through the morning watch, Pat called out
by the orchard, demanding a verdict on the form `\space` and refusing
to descend until somebody confirmed it. Pat insisted
they already knew the answer. Alex, walking up
at an unhurried pace, simply said: "Submit the character \space to the
REPL. Whatever comes back is the answer."

Write a Clojure expression that computes the value of \space.

---

{"tool_calls":[{"name":"eval","args":{"form":"\\space"}}]}
```

### Record 3 — example 3 of 4

**form**: `\T` • **expected**: `'T'`

**concept_phrase**: `the character \T`

**question_what**: `the value of \T`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A small crowd of villagers had gathered near the meadow to watch
Jess attempt to predict, off the cuff, what the REPL would
return. Bob pointed to the character \T and read out the
form aloud: `\T`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

What Clojure form computes the value of \T? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"\\T"}}]}
```

### Record 4 — example 4 of 4

**form**: `(char? \w)` • **expected**: `True`

**concept_phrase**: `the predicate (char? \w)`

**question_what**: `whether \w is a character`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A small slate sat on a flat stone in the meadow; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(char? \w)`, and the page
heading read the predicate (char? \w). Robin nodded at Lou to
write the form properly so the slate would carry an honest entry.

What Clojure form computes whether \w is a character? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(char? \\w)"}}]}
```

### Record 5 — example 1 of 4

**form**: `\w` • **expected**: `'w'`

**concept_phrase**: `the character \w`

**question_what**: `the value of \w`

```
The boy on the hill thought the trick clever the first time he played it.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `\w`, and the line
above it read the character \w. Oliver handed the page to
Pat, who, her legs heavy from sprinting, agreed to write it out properly.

Write a Clojure expression that computes the value of \w.

---

{"tool_calls":[{"name":"eval","args":{"form":"\\w"}}]}
```

---

## G1-09: Symbols vs values

**Examples:** 4 | **Subplots:** 10 | **Plan-pool size:** 7

### Record 1 — example 1 of 4

**form**: `(symbol? 'wolf)` • **expected**: `True`

**concept_phrase**: `the predicate (symbol? 'wolf)`

**question_what**: `whether 'wolf is a symbol`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place in the woods.

A small crowd of villagers had gathered at the edge of the woods to watch
Will attempt to predict, off the cuff, what the REPL would
return. George pointed to the predicate (symbol? 'wolf) and read out the
form aloud: `(symbol? 'wolf)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Question: write a Clojure expression for whether 'wolf is a symbol.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'wolf)"}}]}
```

### Record 2 — example 2 of 4

**form**: `(symbol? 42)` • **expected**: `False`

**concept_phrase**: `the predicate (symbol? 42)`

**question_what**: `whether 42 is a symbol`

```
The boy on the hill thought the trick clever the first time he played it.

Halfway through the morning watch, Pat called out
by the forest, demanding a verdict on the form `(symbol? 42)` and refusing
to descend until somebody confirmed it. Pat insisted
they already knew the answer. Alice, walking up
at an unhurried pace, simply said: "Submit the predicate (symbol? 42) to the
REPL. Whatever comes back is the answer."

Write a form whose evaluation gives whether 42 is a symbol.

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 42)"}}]}
```

### Record 3 — example 3 of 4

**form**: `'wolf` • **expected**: `'wolf'`

**concept_phrase**: `the quoted symbol 'wolf`

**question_what**: `the value of 'wolf`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. This was by the farm.

Sam had been trying to teach Will how the REPL
works. "Look here," they said, pointing to the quoted symbol 'wolf.
"You hand the form `'wolf` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Will, weary from the morning's effort, agreed to try.

Question: write a Clojure expression for the value of 'wolf.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"'wolf"}}]}
```

### Record 4 — example 4 of 4

**form**: `(= 'wolf 'wolf)` • **expected**: `True`

**concept_phrase**: `the equality of two 'wolf symbols`

**question_what**: `whether 'wolf equals 'wolf`

```
The boy on the hill thought the trick clever the first time he played it.

A small crowd of villagers had gathered in the village to watch
Tom attempt to predict, off the cuff, what the REPL would
return. George pointed to the equality of two 'wolf symbols and read out the
form aloud: `(= 'wolf 'wolf)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a Clojure expression that computes whether 'wolf equals 'wolf.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(= 'wolf 'wolf)"}}]}
```

### Record 5 — example 1 of 4

**form**: `(symbol? 'wolf)` • **expected**: `True`

**concept_phrase**: `the predicate (symbol? 'wolf)`

**question_what**: `whether 'wolf is a symbol`

```
The boy on the hill thought the trick clever the first time he played it.

George had been trying to teach Tom how the REPL
works. "Look here," he said, pointing to the predicate (symbol? 'wolf).
"You hand the form `(symbol? 'wolf)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Tom, yawning at the soft moss, agreed to try.

Question: write a Clojure expression for whether 'wolf is a symbol.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'wolf)"}}]}
```

---

## G1-10: Comments

**Examples:** 2 | **Subplots:** 10 | **Plan-pool size:** 7

### Record 1 — example 1 of 2

**form**: `(+ 1 2) ; sum of one and two` • **expected**: `3`

**concept_phrase**: `the form (+ 1 2) followed by a comment`

**question_what**: `the result of (+ 1 2) ignoring the comment`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Lou called down from a stone atop the hilltop where someone had
chalked the form (+ 1 2) followed by a comment on a flat board. Lou, boasting at every turn,
declared she already knew what would come back. Grace,
with steady, careful steps, asked her to actually submit the form
`(+ 1 2) ; sum of one and two` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the result of (+ 1 2) ignoring the comment.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2) ; sum of one and two"}}]}
```

### Record 2 — example 2 of 2

**form**: `42 ;; the answer` • **expected**: `42`

**concept_phrase**: `the literal 42 with a trailing comment`

**question_what**: `the value of 42`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. This was near the orchard.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `42 ;; the answer`, and the line
above it read the literal 42 with a trailing comment. Morgan handed the page to
Pat, who, lulled by the gentle wind, agreed to write it out properly.

Question: write a Clojure expression for the value of 42.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"42 ;; the answer"}}]}
```

### Record 3 — example 1 of 2

**form**: `(+ 1 2) ; sum of one and two` • **expected**: `3`

**concept_phrase**: `the form (+ 1 2) followed by a comment`

**question_what**: `the result of (+ 1 2) ignoring the comment`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Alice kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today on the hilltop the next entry was
the form (+ 1 2) followed by a comment. Tom peered over her shoulder
at the form `(+ 1 2) ; sum of one and two` and was asked, gently, to be the one to
submit it.

What Clojure form computes the result of (+ 1 2) ignoring the comment? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2) ; sum of one and two"}}]}
```

### Record 4 — example 2 of 2

**form**: `42 ;; the answer` • **expected**: `42`

**concept_phrase**: `the literal 42 with a trailing comment`

**question_what**: `the value of 42`

```
The boy on the hill thought the trick clever the first time he played it. This was along the road.

A wooden notice nailed to a post along the road carried a small puzzle. The
riddle simply asked the reader to evaluate `42 ;; the answer`. Tom
laughed, puffed up with pride, and declared it too easy to bother with.
Alice said, patiently, that the only way to be certain of
the literal 42 with a trailing comment was to put it in the REPL.

Question: write a Clojure expression for the value of 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"42 ;; the answer"}}]}
```

### Record 5 — example 1 of 2

**form**: `(+ 1 2) ; sum of one and two` • **expected**: `3`

**concept_phrase**: `the form (+ 1 2) followed by a comment`

**question_what**: `the result of (+ 1 2) ignoring the comment`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden notice nailed to a post by the farm carried a small puzzle. The
riddle simply asked the reader to evaluate `(+ 1 2) ; sum of one and two`. Tom
laughed, with a smug grin, and declared it too easy to bother with.
Robin said, patiently, that the only way to be certain of
the form (+ 1 2) followed by a comment was to put it in the REPL.

Write a form whose evaluation gives the result of (+ 1 2) ignoring the comment.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2) ; sum of one and two"}}]}
```

---

## G1-11: Whitespace doesn't matter

**Examples:** 2 | **Subplots:** 10 | **Plan-pool size:** 7

### Record 1 — example 1 of 2

**form**: `(+    1    2)` • **expected**: `3`

**concept_phrase**: `the form (+ 1 2) with extra spaces`

**question_what**: `the result of the form`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened in the meadow.

A small crowd of villagers had gathered in the meadow to watch
Will attempt to predict, off the cuff, what the REPL would
return. Bob pointed to the form (+ 1 2) with extra spaces and read out the
form aloud: `(+    1    2)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Question: write a Clojure expression for the result of the form.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+    1    2)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(+
  1
  2)` • **expected**: `3`

**concept_phrase**: `the form (+ 1 2) split across lines`

**question_what**: `the result of the form`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place near the road.

A small slate sat on a flat stone near the road; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(+
  1
  2)`, and the page
heading read the form (+ 1 2) split across lines. Sam nodded at Jess to
write the form properly so the slate would carry an honest entry.

Write a Clojure expression that computes the result of the form.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(+\n  1\n  2)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(+    1    2)` • **expected**: `3`

**concept_phrase**: `the form (+ 1 2) with extra spaces`

**question_what**: `the result of the form`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

"There is no need to evaluate that," Will said, with great whoops of laughter.
"Anyone can see what the form (+ 1 2) with extra spaces comes to." Alex, who
in the village had heard such claims many times, asked him to
actually write the form `(+    1    2)` and submit it to the REPL —
just to be sure.

Write a Clojure expression that computes the result of the form.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(+    1    2)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(+
  1
  2)` • **expected**: `3`

**concept_phrase**: `the form (+ 1 2) split across lines`

**question_what**: `the result of the form`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Sam had been trying to teach Will how the REPL
works. "Look here," they said, pointing to the form (+ 1 2) split across lines.
"You hand the form `(+
  1
  2)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Will, her legs heavy from sprinting, agreed to try.

Question: write a Clojure expression for the result of the form.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(+\n  1\n  2)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(+    1    2)` • **expected**: `3`

**concept_phrase**: `the form (+ 1 2) with extra spaces`

**question_what**: `the result of the form`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place by the orchard.

Carol had been trying to teach Lou how the REPL
works. "Look here," she said, pointing to the form (+ 1 2) with extra spaces.
"You hand the form `(+    1    2)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Lou, yawning at the soft moss, agreed to try.

Write a form whose evaluation gives the result of the form.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(+    1    2)"}}]}
```

---

## G1-12: Parens group; they don't multiply

**Examples:** 2 | **Subplots:** 10 | **Plan-pool size:** 7

### Record 1 — example 1 of 2

**form**: `(+ 2 3)` • **expected**: `5`

**concept_phrase**: `the form (+ 2 3)`

**question_what**: `the result of (+ 2 3)`

```
The boy on the hill thought the trick clever the first time he played it. This was near the orchard.

Grace kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the orchard the next entry was
the form (+ 2 3). Jess peered over her shoulder
at the form `(+ 2 3)` and was asked, gently, to be the one to
submit it.

Write a Clojure expression that computes the result of (+ 2 3).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 2 3)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(* (+ 1 2) 3)` • **expected**: `9`

**concept_phrase**: `the form (* (+ 1 2) 3)`

**question_what**: `the result of (* (+ 1 2) 3)`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

The elder of the village kept a small slate by the forest, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the form (* (+ 1 2) 3). Oliver read
out the form `(* (+ 1 2) 3)` so Will could write it
properly into the REPL and earn an honest mark on the slate.

What Clojure form computes the result of (* (+ 1 2) 3)? Submit it via `eval`.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(* (+ 1 2) 3)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(+ 2 3)` • **expected**: `5`

**concept_phrase**: `the form (+ 2 3)`

**question_what**: `the result of (+ 2 3)`

```
The boy on the hill thought the trick clever the first time he played it. It happened along the road.

Tom called down from a stone near the road where someone had
chalked the form (+ 2 3) on a flat board. Tom, boasting at every turn,
declared he already knew what would come back. George,
without complaint, asked him to actually submit the form
`(+ 2 3)` to the REPL — the village had stopped trusting answers
that weren't checked.

What Clojure form computes the result of (+ 2 3)? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 2 3)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(* (+ 1 2) 3)` • **expected**: `9`

**concept_phrase**: `the form (* (+ 1 2) 3)`

**question_what**: `the result of (* (+ 1 2) 3)`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

The elder of the village kept a small slate on the road, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the form (* (+ 1 2) 3). Frank read
out the form `(* (+ 1 2) 3)` so Will could write it
properly into the REPL and earn an honest mark on the slate.

Question: write a Clojure expression for the result of (* (+ 1 2) 3).

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(* (+ 1 2) 3)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(+ 2 3)` • **expected**: `5`

**concept_phrase**: `the form (+ 2 3)`

**question_what**: `the result of (+ 2 3)`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden notice nailed to a post in the farm carried a small puzzle. The
riddle simply asked the reader to evaluate `(+ 2 3)`. Tom
laughed, with great whoops of laughter, and declared it too easy to bother with.
Oliver said, patiently, that the only way to be certain of
the form (+ 2 3) was to put it in the REPL.

What Clojure form computes the result of (+ 2 3)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 2 3)"}}]}
```

---

## G1-13: First arithmetic call

**Examples:** 6 | **Subplots:** 10 | **Plan-pool size:** 7

### Record 1 — example 1 of 6

**form**: `(+ 1 2)` • **expected**: `3`

**concept_phrase**: `the form (+ 1 2)`

**question_what**: `the result of (+ 1 2)`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

"There is no need to evaluate that," Pat said, with great whoops of laughter.
"Anyone can see what the form (+ 1 2) comes to." Sam, who
at the edge of the woods had heard such claims many times, asked them to
actually write the form `(+ 1 2)` and submit it to the REPL —
just to be sure.

Write a Clojure expression that computes the result of (+ 1 2).

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### Record 2 — example 2 of 6

**form**: `(- 5 3)` • **expected**: `2`

**concept_phrase**: `the form (- 5 3)`

**question_what**: `the result of (- 5 3)`

```
The boy on the hill thought the trick clever the first time he played it.

A small slate sat on a flat stone in the forest; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(- 5 3)`, and the page
heading read the form (- 5 3). George nodded at Jess to
write the form properly so the slate would carry an honest entry.

Write a Clojure expression that computes the result of (- 5 3).

---

{"tool_calls":[{"name":"eval","args":{"form":"(- 5 3)"}}]}
```

### Record 3 — example 3 of 6

**form**: `(* 4 5)` • **expected**: `20`

**concept_phrase**: `the form (* 4 5)`

**question_what**: `the result of (* 4 5)`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden notice nailed to a post along the road carried a small puzzle. The
riddle simply asked the reader to evaluate `(* 4 5)`. Jess
laughed, as if the race were already won, and declared it too easy to bother with.
Sam said, patiently, that the only way to be certain of
the form (* 4 5) was to put it in the REPL.

Write a Clojure expression that computes the result of (* 4 5).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(* 4 5)"}}]}
```

### Record 4 — example 4 of 6

**form**: `(/ 10 2)` • **expected**: `5`

**concept_phrase**: `the form (/ 10 2)`

**question_what**: `the result of (/ 10 2)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Lou called down from a stone by the village where someone had
chalked the form (/ 10 2) on a flat board. Lou, as if the race were already won,
declared she already knew what would come back. Morgan,
stepping deliberately, asked her to actually submit the form
`(/ 10 2)` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a form whose evaluation gives the result of (/ 10 2).

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(/ 10 2)"}}]}
```

### Record 5 — example 5 of 6

**form**: `(+ 7 8)` • **expected**: `15`

**concept_phrase**: `the form (+ 7 8)`

**question_what**: `the result of (+ 7 8)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(+ 7 8)`, and the line
above it read the form (+ 7 8). Grace handed the page to
Lou, who, yawning at the soft moss, agreed to write it out properly.

Write a form whose evaluation gives the result of (+ 7 8).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 7 8)"}}]}
```

---

## G1-14: Nested call evaluation

**Examples:** 4 | **Subplots:** 10 | **Plan-pool size:** 7

### Record 1 — example 1 of 4

**form**: `(+ 1 (* 2 3))` • **expected**: `7`

**concept_phrase**: `the nested form (+ 1 (* 2 3))`

**question_what**: `the result of (+ 1 (* 2 3))`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Carol kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today at the edge of the orchard the next entry was
the nested form (+ 1 (* 2 3)). Jess peered over her shoulder
at the form `(+ 1 (* 2 3))` and was asked, gently, to be the one to
submit it.

Question: write a Clojure expression for the result of (+ 1 (* 2 3)).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (* 2 3))"}}]}
```

### Record 2 — example 2 of 4

**form**: `(* (+ 1 2) (+ 3 4))` • **expected**: `21`

**concept_phrase**: `the nested form (* (+ 1 2) (+ 3 4))`

**question_what**: `the result of (* (+ 1 2) (+ 3 4))`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. This was along the road.

"There is no need to evaluate that," Pat said, with a smug grin.
"Anyone can see what the nested form (* (+ 1 2) (+ 3 4)) comes to." Grace, who
along the road had heard such claims many times, asked them to
actually write the form `(* (+ 1 2) (+ 3 4))` and submit it to the REPL —
just to be sure.

Question: write a Clojure expression for the result of (* (+ 1 2) (+ 3 4)).

---

{"tool_calls":[{"name":"eval","args":{"form":"(* (+ 1 2) (+ 3 4))"}}]}
```

### Record 3 — example 3 of 4

**form**: `(- 100 (* 5 5))` • **expected**: `75`

**concept_phrase**: `the nested form (- 100 (* 5 5))`

**question_what**: `the result of (- 100 (* 5 5))`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A wooden notice nailed to a post by the orchard carried a small puzzle. The
riddle simply asked the reader to evaluate `(- 100 (* 5 5))`. Pat
laughed, as if the race were already won, and declared it too easy to bother with.
Alice said, patiently, that the only way to be certain of
the nested form (- 100 (* 5 5)) was to put it in the REPL.

Question: write a Clojure expression for the result of (- 100 (* 5 5)).

---

{"tool_calls":[{"name":"eval","args":{"form":"(- 100 (* 5 5))"}}]}
```

### Record 4 — example 4 of 4

**form**: `(+ (* 2 3) (* 4 5))` • **expected**: `26`

**concept_phrase**: `the sum of two products`

**question_what**: `the result of (+ (* 2 3) (* 4 5))`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Tom called down from a stone at the edge of the farm where someone had
chalked the sum of two products on a flat board. Tom, with great whoops of laughter,
declared he already knew what would come back. Robin,
saying very little, asked him to actually submit the form
`(+ (* 2 3) (* 4 5))` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a form whose evaluation gives the result of (+ (* 2 3) (* 4 5)).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ (* 2 3) (* 4 5))"}}]}
```

### Record 5 — example 1 of 4

**form**: `(+ 1 (* 2 3))` • **expected**: `7`

**concept_phrase**: `the nested form (+ 1 (* 2 3))`

**question_what**: `the result of (+ 1 (* 2 3))`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A small crowd of villagers had gathered near the woods to watch
Jess attempt to predict, off the cuff, what the REPL would
return. Grace pointed to the nested form (+ 1 (* 2 3)) and read out the
form aloud: `(+ 1 (* 2 3))`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

What Clojure form computes the result of (+ 1 (* 2 3))? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (* 2 3))"}}]}
```

---

## G1-15: Equality

**Examples:** 6 | **Subplots:** 10 | **Plan-pool size:** 7

### Record 1 — example 1 of 6

**form**: `(= 1 1)` • **expected**: `True`

**concept_phrase**: `the equality (= 1 1)`

**question_what**: `the value of (= 1 1)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

"There is no need to evaluate that," Lou said, with great whoops of laughter.
"Anyone can see what the equality (= 1 1) comes to." Grace, who
near the meadow had heard such claims many times, asked her to
actually write the form `(= 1 1)` and submit it to the REPL —
just to be sure.

What Clojure form computes the value of (= 1 1)? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 1)"}}]}
```

### Record 2 — example 2 of 6

**form**: `(= 1 2)` • **expected**: `False`

**concept_phrase**: `the equality (= 1 2)`

**question_what**: `the value of (= 1 2)`

```
Every shepherd in the valley knew the danger of crying wolf for sport. This was near the hilltop.

Tom called down from a stone atop the hilltop where someone had
chalked the equality (= 1 2) on a flat board. Tom, as if the race were already won,
declared he already knew what would come back. Alex,
untroubled by what others thought, asked him to actually submit the form
`(= 1 2)` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the value of (= 1 2).

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 2)"}}]}
```

### Record 3 — example 3 of 6

**form**: `(= "a" "a")` • **expected**: `True`

**concept_phrase**: `the equality (= "a" "a")`

**question_what**: `the value of (= "a" "a")`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Will called down from a stone near the road where someone had
chalked the equality (= "a" "a") on a flat board. Will, with great whoops of laughter,
declared he already knew what would come back. Alex,
with steady, careful steps, asked him to actually submit the form
`(= "a" "a")` to the REPL — the village had stopped trusting answers
that weren't checked.

What Clojure form computes the value of (= "a" "a")? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(= \"a\" \"a\")"}}]}
```

### Record 4 — example 4 of 6

**form**: `(= :wolf :wolf)` • **expected**: `True`

**concept_phrase**: `the equality (= :wolf :wolf)`

**question_what**: `the value of (= :wolf :wolf)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened by the forest.

"There is no need to evaluate that," Lou said, swaggering through the underbrush.
"Anyone can see what the equality (= :wolf :wolf) comes to." Alex, who
at the edge of the forest had heard such claims many times, asked her to
actually write the form `(= :wolf :wolf)` and submit it to the REPL —
just to be sure.

Write a Clojure expression that computes the value of (= :wolf :wolf).

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(= :wolf :wolf)"}}]}
```

### Record 5 — example 5 of 6

**form**: `(= :wolf :flock)` • **expected**: `False`

**concept_phrase**: `the equality (= :wolf :flock)`

**question_what**: `the value of (= :wolf :flock)`

```
Every shepherd in the valley knew the danger of crying wolf for sport. This was in the village.

Frank kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today by the village the next entry was
the equality (= :wolf :flock). Jess peered over his shoulder
at the form `(= :wolf :flock)` and was asked, gently, to be the one to
submit it.

Write a form whose evaluation gives the value of (= :wolf :flock).

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(= :wolf :flock)"}}]}
```

---

## G1-16: Numeric predicates

**Examples:** 6 | **Subplots:** 10 | **Plan-pool size:** 7

### Record 1 — example 1 of 6

**form**: `(zero? 0)` • **expected**: `True`

**concept_phrase**: `the predicate (zero? 0)`

**question_what**: `whether 0 is zero`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A small crowd of villagers had gathered by the orchard to watch
Pat attempt to predict, off the cuff, what the REPL would
return. Sam pointed to the predicate (zero? 0) and read out the
form aloud: `(zero? 0)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a form whose evaluation gives whether 0 is zero.

---

{"tool_calls":[{"name":"eval","args":{"form":"(zero? 0)"}}]}
```

### Record 2 — example 2 of 6

**form**: `(zero? 5)` • **expected**: `False`

**concept_phrase**: `the predicate (zero? 5)`

**question_what**: `whether 5 is zero`

```
The boy on the hill thought the trick clever the first time he played it. All this took place near the village.

Halfway through the morning watch, Tom called out
at the edge of the village, demanding a verdict on the form `(zero? 5)` and refusing
to descend until somebody confirmed it. Tom insisted
he already knew the answer. Alice, walking up
at an unhurried pace, simply said: "Submit the predicate (zero? 5) to the
REPL. Whatever comes back is the answer."

What Clojure form computes whether 5 is zero? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(zero? 5)"}}]}
```

### Record 3 — example 3 of 6

**form**: `(pos? 7)` • **expected**: `True`

**concept_phrase**: `the predicate (pos? 7)`

**question_what**: `whether 7 is positive`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened along the road.

"There is no need to evaluate that," Will said, with a smug grin.
"Anyone can see what the predicate (pos? 7) comes to." George, who
on the road had heard such claims many times, asked him to
actually write the form `(pos? 7)` and submit it to the REPL —
just to be sure.

What Clojure form computes whether 7 is positive? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(pos? 7)"}}]}
```

### Record 4 — example 4 of 6

**form**: `(pos? -2)` • **expected**: `False`

**concept_phrase**: `the predicate (pos? -2)`

**question_what**: `whether -2 is positive`

```
Every shepherd in the valley knew the danger of crying wolf for sport. It happened near the meadow.

A small crowd of villagers had gathered by the meadow to watch
Will attempt to predict, off the cuff, what the REPL would
return. Alex pointed to the predicate (pos? -2) and read out the
form aloud: `(pos? -2)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

What Clojure form computes whether -2 is positive? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(pos? -2)"}}]}
```

### Record 5 — example 5 of 6

**form**: `(neg? -3)` • **expected**: `True`

**concept_phrase**: `the predicate (neg? -3)`

**question_what**: `whether -3 is negative`

```
The boy on the hill thought the trick clever the first time he played it.

Tom called down from a stone by the village where someone had
chalked the predicate (neg? -3) on a flat board. Tom, as if the race were already won,
declared he already knew what would come back. Alex,
saying very little, asked him to actually submit the form
`(neg? -3)` to the REPL — the village had stopped trusting answers
that weren't checked.

What Clojure form computes whether -3 is negative? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(neg? -3)"}}]}
```

---

## G1-17: Printing vs returning

**Examples:** 2 | **Subplots:** 10 | **Plan-pool size:** 7

### Record 1 — example 1 of 2

**form**: `42` • **expected**: `42`

**concept_phrase**: `the value 42`

**question_what**: `the value of 42`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place by the forest.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `42`, and the line
above it read the value 42. Grace handed the page to
Will, who, drowsy from the warm sun, agreed to write it out properly.

Question: write a Clojure expression for the value of 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
```

### Record 2 — example 2 of 2

**form**: `(+ 1 2)` • **expected**: `3`

**concept_phrase**: `the form (+ 1 2)`

**question_what**: `the result of (+ 1 2)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

"There is no need to evaluate that," Jess said, puffed up with pride.
"Anyone can see what the form (+ 1 2) comes to." Frank, who
in the orchard had heard such claims many times, asked her to
actually write the form `(+ 1 2)` and submit it to the REPL —
just to be sure.

Question: write a Clojure expression for the result of (+ 1 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### Record 3 — example 1 of 2

**form**: `42` • **expected**: `42`

**concept_phrase**: `the value 42`

**question_what**: `the value of 42`

```
The boy on the hill thought the trick clever the first time he played it.

The elder of the village kept a small slate at the edge of the meadow, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the value 42. Carol read
out the form `42` so Tom could write it
properly into the REPL and earn an honest mark on the slate.

Question: write a Clojure expression for the value of 42.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
```

### Record 4 — example 2 of 2

**form**: `(+ 1 2)` • **expected**: `3`

**concept_phrase**: `the form (+ 1 2)`

**question_what**: `the result of (+ 1 2)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A wooden notice nailed to a post near the forest carried a small puzzle. The
riddle simply asked the reader to evaluate `(+ 1 2)`. Will
laughed, swaggering through the underbrush, and declared it too easy to bother with.
Alex said, patiently, that the only way to be certain of
the form (+ 1 2) was to put it in the REPL.

Write a form whose evaluation gives the result of (+ 1 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### Record 5 — example 1 of 2

**form**: `42` • **expected**: `42`

**concept_phrase**: `the value 42`

**question_what**: `the value of 42`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `42`, and the line
above it read the value 42. Morgan handed the page to
Pat, who, drowsy from the warm sun, agreed to write it out properly.

Write a Clojure expression that computes the value of 42.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
```

---

## G1-18: Errors are safe in the REPL

**Examples:** 2 | **Subplots:** 10 | **Plan-pool size:** 7

### Record 1 — example 1 of 2

**form**: `(+ 1 2)` • **expected**: `3`

**concept_phrase**: `the form (+ 1 2)`

**question_what**: `the result of (+ 1 2)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Alice had been trying to teach Pat how the REPL
works. "Look here," she said, pointing to the form (+ 1 2).
"You hand the form `(+ 1 2)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Pat, lulled by the gentle wind, agreed to try.

Write a Clojure expression that computes the result of (+ 1 2).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(* 7 6)` • **expected**: `42`

**concept_phrase**: `the form (* 7 6)`

**question_what**: `the result of (* 7 6)`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Robin had been trying to teach Jess how the REPL
works. "Look here," they said, pointing to the form (* 7 6).
"You hand the form `(* 7 6)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, weary from the morning's effort, agreed to try.

Write a Clojure expression that computes the result of (* 7 6).

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 7 6)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(+ 1 2)` • **expected**: `3`

**concept_phrase**: `the form (+ 1 2)`

**question_what**: `the result of (+ 1 2)`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

"There is no need to evaluate that," Lou said, puffed up with pride.
"Anyone can see what the form (+ 1 2) comes to." Sam, who
near the road had heard such claims many times, asked her to
actually write the form `(+ 1 2)` and submit it to the REPL —
just to be sure.

Write a form whose evaluation gives the result of (+ 1 2).

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(* 7 6)` • **expected**: `42`

**concept_phrase**: `the form (* 7 6)`

**question_what**: `the result of (* 7 6)`

```
The boy on the hill thought the trick clever the first time he played it. All this took place near the meadow.

Oliver had been trying to teach Will how the REPL
works. "Look here," he said, pointing to the form (* 7 6).
"You hand the form `(* 7 6)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Will, drowsy from the warm sun, agreed to try.

Write a form whose evaluation gives the result of (* 7 6).

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 7 6)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(+ 1 2)` • **expected**: `3`

**concept_phrase**: `the form (+ 1 2)`

**question_what**: `the result of (+ 1 2)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

"There is no need to evaluate that," Lou said, with great whoops of laughter.
"Anyone can see what the form (+ 1 2) comes to." Sam, who
by the village had heard such claims many times, asked her to
actually write the form `(+ 1 2)` and submit it to the REPL —
just to be sure.

Write a Clojure expression that computes the result of (+ 1 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

---

