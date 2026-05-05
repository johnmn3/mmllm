# Boy-wolf Grade 7 — deep spot-check

5 generated records per subject (across all examples and a variety of seeds). Read every record carefully. Flag anything that reads odd to a careful reader, including issues the structural audit can't catch (prose flow, contextual fit, cliché repetition, subplot/example mismatch, etc.)

---

## G7-01: throw

**Examples:** 1 | **Subplots:** 13 | **Plan-pool size:** 11

### Record 1 — example 1 of 1

**form**: `(try (throw (Exception. "bad")) (catch Exception e :thrown))` • **expected**: `':thrown'`

**concept_phrase**: `throwing an exception that is then caught`

**question_what**: `the keyword :thrown returned after the throw is caught`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A small slip of paper near the woods carried the form `(try (throw (Exception. "bad")) (catch Exception e :thrown))`.
Pat glanced at it and shrugged the warning off, certain there
was no trouble. Alice sat down, without complaint, and worked
through throwing an exception that is then caught step by step — ready, if anything went wrong,
to read the stack trace from top to bottom and try the form again.

Write a Clojure expression that computes the keyword :thrown returned after the throw is caught.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (Exception. \"bad\")) (catch Exception e :thrown))"}}]}
```

### Record 2 — example 1 of 1

**form**: `(try (throw (Exception. "bad")) (catch Exception e :thrown))` • **expected**: `':thrown'`

**concept_phrase**: `throwing an exception that is then caught`

**question_what**: `the keyword :thrown returned after the throw is caught`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Lou called down from a stone by the meadow where someone had
chalked throwing an exception that is then caught on a flat board. Lou, swaggering through the underbrush,
declared she already knew what would come back. Alice,
saying very little, asked her to actually submit the form
`(try (throw (Exception. "bad")) (catch Exception e :thrown))` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a form whose evaluation gives the keyword :thrown returned after the throw is caught.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (Exception. \"bad\")) (catch Exception e :thrown))"}}]}
```

### Record 3 — example 1 of 1

**form**: `(try (throw (Exception. "bad")) (catch Exception e :thrown))` • **expected**: `':thrown'`

**concept_phrase**: `throwing an exception that is then caught`

**question_what**: `the keyword :thrown returned after the throw is caught`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Frank kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today by the village the next entry was
throwing an exception that is then caught. Pat peered over his shoulder
at the form `(try (throw (Exception. "bad")) (catch Exception e :thrown))` and was asked, gently, to be the one to
submit it.

Write a Clojure expression that computes the keyword :thrown returned after the throw is caught.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (Exception. \"bad\")) (catch Exception e :thrown))"}}]}
```

### Record 4 — example 1 of 1

**form**: `(try (throw (Exception. "bad")) (catch Exception e :thrown))` • **expected**: `':thrown'`

**concept_phrase**: `throwing an exception that is then caught`

**question_what**: `the keyword :thrown returned after the throw is caught`

```
Every shepherd in the valley knew the danger of crying wolf for sport. It happened at the edge of the village.

A small slip of paper by the village carried the form `(try (throw (Exception. "bad")) (catch Exception e :thrown))`.
Jess glanced at it and shrugged the warning off, certain there
was no trouble. Frank sat down, stepping deliberately, and worked
through throwing an exception that is then caught step by step — ready, if anything went wrong,
to read the stack trace from top to bottom and try the form again.

Write a Clojure expression that computes the keyword :thrown returned after the throw is caught.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (Exception. \"bad\")) (catch Exception e :thrown))"}}]}
```

### Record 5 — example 1 of 1

**form**: `(try (throw (Exception. "bad")) (catch Exception e :thrown))` • **expected**: `':thrown'`

**concept_phrase**: `throwing an exception that is then caught`

**question_what**: `the keyword :thrown returned after the throw is caught`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Lou called down from a stone on the road where someone had
chalked throwing an exception that is then caught on a flat board. Lou, with great whoops of laughter,
declared she already knew what would come back. Alex,
stepping deliberately, asked her to actually submit the form
`(try (throw (Exception. "bad")) (catch Exception e :thrown))` to the REPL — the village had stopped trusting answers
that weren't checked.

What Clojure form computes the keyword :thrown returned after the throw is caught? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (Exception. \"bad\")) (catch Exception e :thrown))"}}]}
```

---

## G7-02: try / catch

**Examples:** 2 | **Subplots:** 13 | **Plan-pool size:** 11

### Record 1 — example 1 of 2

**form**: `(try (/ 1 0) (catch Exception e :caught))` • **expected**: `':caught'`

**concept_phrase**: `a division by zero wrapped in try/catch`

**question_what**: `the keyword :caught returned by the catch branch`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Will called down from a stone by the orchard where someone had
chalked a division by zero wrapped in try/catch on a flat board. Will, with a smug grin,
declared he already knew what would come back. Morgan,
stepping deliberately, asked him to actually submit the form
`(try (/ 1 0) (catch Exception e :caught))` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a form whose evaluation gives the keyword :caught returned by the catch branch.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 1 0) (catch Exception e :caught))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(try 42 (catch Exception e :caught))` • **expected**: `42`

**concept_phrase**: `a try with no error — the body's value is returned`

**question_what**: `the value 42 from the no-error branch`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place by the woods.

Beyond the REPL the world had files, streams, and surprises.
Grace opened a small notebook at the edge of the woods, copying down
a try with no error — the body's value is returned. Tom, her legs heavy from sprinting, watched as she
wrote the form `(try 42 (catch Exception e :caught))` so the runtime could carry the work the
rest of the way.

Write a Clojure expression that computes the value 42 from the no-error branch.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try 42 (catch Exception e :caught))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(try (/ 1 0) (catch Exception e :caught))` • **expected**: `':caught'`

**concept_phrase**: `a division by zero wrapped in try/catch`

**question_what**: `the keyword :caught returned by the catch branch`

```
The boy on the hill thought the trick clever the first time he played it. It happened by the woods.

Pat had cried alarm so often that the runtime now took
every careless throw at its word. in the woods, Alice typed
`(try (/ 1 0) (catch Exception e :caught))` carefully, ready to catch whatever the REPL might raise.
Pat, swaggering through the underbrush, said no error would ever come — but Alice
insisted on letting the runtime decide, then reading a division by zero wrapped in try/catch
from whatever it returned.

Write a form whose evaluation gives the keyword :caught returned by the catch branch.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 1 0) (catch Exception e :caught))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(try 42 (catch Exception e :caught))` • **expected**: `42`

**concept_phrase**: `a try with no error — the body's value is returned`

**question_what**: `the value 42 from the no-error branch`

```
The boy on the hill thought the trick clever the first time he played it. This was along the road.

A small slate sat on a flat stone on the road; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(try 42 (catch Exception e :caught))`, and the page
heading read a try with no error — the body's value is returned. George nodded at Jess to
write the form properly so the slate would carry an honest entry.

Write a Clojure expression that computes the value 42 from the no-error branch.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try 42 (catch Exception e :caught))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(try (/ 1 0) (catch Exception e :caught))` • **expected**: `':caught'`

**concept_phrase**: `a division by zero wrapped in try/catch`

**question_what**: `the keyword :caught returned by the catch branch`

```
The boy on the hill thought the trick clever the first time he played it. This was by the forest.

A small crowd of villagers had gathered at the edge of the forest to watch
Lou attempt to predict, off the cuff, what the REPL would
return. George pointed to a division by zero wrapped in try/catch and read out the
form aloud: `(try (/ 1 0) (catch Exception e :caught))`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

What Clojure form computes the keyword :caught returned by the catch branch? Submit it via `eval`.

---

I wrap the form in try/catch and let the REPL handle the error.

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 1 0) (catch Exception e :caught))"}}]}
```

---

## G7-03: try / finally

**Examples:** 2 | **Subplots:** 13 | **Plan-pool size:** 11

### Record 1 — example 1 of 2

**form**: `(try 7 (finally :cleanup))` • **expected**: `7`

**concept_phrase**: `a try whose finally clause runs but doesn't change the value`

**question_what**: `the value 7 from the body (finally is for side effects)`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place at the edge of the village.

Alice had been trying to teach Will how the REPL
works. "Look here," she said, pointing to a try whose finally clause runs but doesn't change the value.
"You hand the form `(try 7 (finally :cleanup))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Will, drowsy from the warm sun, agreed to try.

Write a Clojure expression that computes the value 7 from the body (finally is for side effects).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(try 7 (finally :cleanup))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(try (try (/ 1 0) (finally :ran)) (catch Exception e :caught))` • **expected**: `':caught'`

**concept_phrase**: `a finally that runs before the outer catch fires`

**question_what**: `the keyword :caught (the outer catch handles the divide-by-zero)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened near the meadow.

A small crowd of villagers had gathered near the meadow to watch
Lou attempt to predict, off the cuff, what the REPL would
return. Oliver pointed to a finally that runs before the outer catch fires and read out the
form aloud: `(try (try (/ 1 0) (finally :ran)) (catch Exception e :caught))`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a form whose evaluation gives the keyword :caught (the outer catch handles the divide-by-zero).

---

I wrap the form in try/catch and let the REPL handle the error.

{"tool_calls":[{"name":"eval","args":{"form":"(try (try (/ 1 0) (finally :ran)) (catch Exception e :caught))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(try 7 (finally :cleanup))` • **expected**: `7`

**concept_phrase**: `a try whose finally clause runs but doesn't change the value`

**question_what**: `the value 7 from the body (finally is for side effects)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(try 7 (finally :cleanup))`, and the line
above it read a try whose finally clause runs but doesn't change the value. Frank handed the page to
Pat, who, yawning at the soft moss, agreed to write it out properly.

Write a Clojure expression that computes the value 7 from the body (finally is for side effects).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(try 7 (finally :cleanup))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(try (try (/ 1 0) (finally :ran)) (catch Exception e :caught))` • **expected**: `':caught'`

**concept_phrase**: `a finally that runs before the outer catch fires`

**question_what**: `the keyword :caught (the outer catch handles the divide-by-zero)`

```
The boy on the hill thought the trick clever the first time he played it.

The elder of the village kept a small slate near the village, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was a finally that runs before the outer catch fires. Bob read
out the form `(try (try (/ 1 0) (finally :ran)) (catch Exception e :caught))` so Will could write it
properly into the REPL and earn an honest mark on the slate.

What Clojure form computes the keyword :caught (the outer catch handles the divide-by-zero)? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(try (try (/ 1 0) (finally :ran)) (catch Exception e :caught))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(try 7 (finally :cleanup))` • **expected**: `7`

**concept_phrase**: `a try whose finally clause runs but doesn't change the value`

**question_what**: `the value 7 from the body (finally is for side effects)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Beyond the REPL the world had files, streams, and surprises.
Robin opened a small notebook by the village, copying down
a try whose finally clause runs but doesn't change the value. Will, lulled by the gentle wind, watched as they
wrote the form `(try 7 (finally :cleanup))` so the runtime could carry the work the
rest of the way.

Write a Clojure expression that computes the value 7 from the body (finally is for side effects).

---

{"tool_calls":[{"name":"eval","args":{"form":"(try 7 (finally :cleanup))"}}]}
```

---

## G7-04: ex-info

**Examples:** 2 | **Subplots:** 13 | **Plan-pool size:** 11

### Record 1 — example 1 of 2

**form**: `(try (throw (ex-info "bad" {:a 1})) (catch Exception e (ex-data e)))` • **expected**: `{':a': 1}`

**concept_phrase**: `throwing an ex-info with attached data, then reading it back`

**question_what**: `the data map {:a 1} pulled from the caught ex-info`

```
The boy on the hill thought the trick clever the first time he played it.

A small slip of paper near the farm carried the form `(try (throw (ex-info "bad" {:a 1})) (catch Exception e (ex-data e)))`.
Pat glanced at it and shrugged the warning off, certain there
was no trouble. Bob sat down, saying very little, and worked
through throwing an ex-info with attached data, then reading it back step by step — ready, if anything went wrong,
to read the stack trace from top to bottom and try the form again.

Write a Clojure expression that computes the data map {:a 1} pulled from the caught ex-info.

---

I use ex-info to attach data to the error.

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (ex-info \"bad\" {:a 1})) (catch Exception e (ex-data e)))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(try (throw (ex-info "x" {:k :v})) (catch Exception e (:k (ex-data e))))` • **expected**: `':v'`

**concept_phrase**: `extracting a single key from the caught ex-info's data`

**question_what**: `the value :v at key :k in the ex-data`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened at the edge of the village.

Beyond the REPL the world had files, streams, and surprises.
George opened a small notebook near the village, copying down
extracting a single key from the caught ex-info's data. Jess, yawning at the soft moss, watched as he
wrote the form `(try (throw (ex-info "x" {:k :v})) (catch Exception e (:k (ex-data e))))` so the runtime could carry the work the
rest of the way.

Write a Clojure expression that computes the value :v at key :k in the ex-data.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (ex-info \"x\" {:k :v})) (catch Exception e (:k (ex-data e))))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(try (throw (ex-info "bad" {:a 1})) (catch Exception e (ex-data e)))` • **expected**: `{':a': 1}`

**concept_phrase**: `throwing an ex-info with attached data, then reading it back`

**question_what**: `the data map {:a 1} pulled from the caught ex-info`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden notice nailed to a post near the road carried a small puzzle. The
riddle simply asked the reader to evaluate `(try (throw (ex-info "bad" {:a 1})) (catch Exception e (ex-data e)))`. Tom
laughed, swaggering through the underbrush, and declared it too easy to bother with.
Sam said, patiently, that the only way to be certain of
throwing an ex-info with attached data, then reading it back was to put it in the REPL.

Write a Clojure expression that computes the data map {:a 1} pulled from the caught ex-info.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (ex-info \"bad\" {:a 1})) (catch Exception e (ex-data e)))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(try (throw (ex-info "x" {:k :v})) (catch Exception e (:k (ex-data e))))` • **expected**: `':v'`

**concept_phrase**: `extracting a single key from the caught ex-info's data`

**question_what**: `the value :v at key :k in the ex-data`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(try (throw (ex-info "x" {:k :v})) (catch Exception e (:k (ex-data e))))`, and the line
above it read extracting a single key from the caught ex-info's data. Bob handed the page to
Tom, who, her legs heavy from sprinting, agreed to write it out properly.

Write a form whose evaluation gives the value :v at key :k in the ex-data.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (ex-info \"x\" {:k :v})) (catch Exception e (:k (ex-data e))))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(try (throw (ex-info "bad" {:a 1})) (catch Exception e (ex-data e)))` • **expected**: `{':a': 1}`

**concept_phrase**: `throwing an ex-info with attached data, then reading it back`

**question_what**: `the data map {:a 1} pulled from the caught ex-info`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place at the edge of the orchard.

Oliver had been trying to teach Lou how the REPL
works. "Look here," he said, pointing to throwing an ex-info with attached data, then reading it back.
"You hand the form `(try (throw (ex-info "bad" {:a 1})) (catch Exception e (ex-data e)))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Lou, lulled by the gentle wind, agreed to try.

What Clojure form computes the data map {:a 1} pulled from the caught ex-info? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (ex-info \"bad\" {:a 1})) (catch Exception e (ex-data e)))"}}]}
```

---

## G7-05: nil punning

**Examples:** 4 | **Subplots:** 13 | **Plan-pool size:** 11

### Record 1 — example 1 of 4

**form**: `(some? nil)` • **expected**: `False`

**concept_phrase**: `the predicate (some? nil)`

**question_what**: `whether nil counts as some?`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Halfway through the morning watch, Jess called out
near the hilltop, demanding a verdict on the form `(some? nil)` and refusing
to descend until somebody confirmed it. Jess insisted
she already knew the answer. Alice, walking up
at an unhurried pace, simply said: "Submit the predicate (some? nil) to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for whether nil counts as some?.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(some? nil)"}}]}
```

### Record 2 — example 2 of 4

**form**: `(some? 0)` • **expected**: `True`

**concept_phrase**: `the predicate (some? 0) — 0 is not nil`

**question_what**: `whether 0 counts as some?`

```
The boy on the hill thought the trick clever the first time he played it.

Tom had cried alarm so often that the runtime now took
every careless throw at its word. in the forest, Alex typed
`(some? 0)` carefully, ready to catch whatever the REPL might raise.
Tom, with great whoops of laughter, said no error would ever come — but Alex
insisted on letting the runtime decide, then reading the predicate (some? 0) — 0 is not nil
from whatever it returned.

What Clojure form computes whether 0 counts as some?? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(some? 0)"}}]}
```

### Record 3 — example 3 of 4

**form**: `(first nil)` • **expected**: `None`

**concept_phrase**: `calling first on nil`

**question_what**: `the value of (first nil), which is nil`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Alex had been trying to teach Tom how the REPL
works. "Look here," they said, pointing to calling first on nil.
"You hand the form `(first nil)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Tom, her legs heavy from sprinting, agreed to try.

Write a form whose evaluation gives the value of (first nil), which is nil.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(first nil)"}}]}
```

### Record 4 — example 4 of 4

**form**: `(count nil)` • **expected**: `0`

**concept_phrase**: `counting a nil collection`

**question_what**: `the count of nil, which is 0`

```
The boy on the hill thought the trick clever the first time he played it. It happened at the edge of the village.

Beyond the REPL the world had files, streams, and surprises.
Bob opened a small notebook at the edge of the village, copying down
counting a nil collection. Tom, her legs heavy from sprinting, watched as he
wrote the form `(count nil)` so the runtime could carry the work the
rest of the way.

Write a Clojure expression that computes the count of nil, which is 0.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(count nil)"}}]}
```

### Record 5 — example 1 of 4

**form**: `(some? nil)` • **expected**: `False`

**concept_phrase**: `the predicate (some? nil)`

**question_what**: `whether nil counts as some?`

```
The boy on the hill thought the trick clever the first time he played it.

Jess had cried alarm so often that the runtime now took
every careless throw at its word. at the edge of the farm, Carol typed
`(some? nil)` carefully, ready to catch whatever the REPL might raise.
Jess, boasting at every turn, said no error would ever come — but Carol
insisted on letting the runtime decide, then reading the predicate (some? nil)
from whatever it returned.

What Clojure form computes whether nil counts as some?? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(some? nil)"}}]}
```

---

## G7-06: pre and post conditions

**Examples:** 2 | **Subplots:** 13 | **Plan-pool size:** 11

### Record 1 — example 1 of 2

**form**: `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` • **expected**: `10`

**concept_phrase**: `a fn with a :pre condition that is satisfied`

**question_what**: `the value returned when the precondition holds and 5 is doubled`

```
The boy on the hill thought the trick clever the first time he played it.

A small slip of paper atop the hilltop carried the form `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)`.
Will glanced at it and shrugged the warning off, certain there
was no trouble. Frank sat down, her eyes always on the path, and worked
through a fn with a :pre condition that is satisfied step by step — ready, if anything went wrong,
to read the stack trace from top to bottom and try the form again.

Write a Clojure expression that computes the value returned when the precondition holds and 5 is doubled.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] {:pre [(pos? x)]} (* x 2)) 5)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exception e :pre-failed))` • **expected**: `':pre-failed'`

**concept_phrase**: `a :pre condition that fails, caught by surrounding try`

**question_what**: `the keyword :pre-failed when the pre-check rejects -1`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Halfway through the morning watch, Pat called out
near the woods, demanding a verdict on the form `(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exception e :pre-failed))` and refusing
to descend until somebody confirmed it. Pat insisted
they already knew the answer. Robin, walking up
at an unhurried pace, simply said: "Submit a :pre condition that fails, caught by surrounding try to the
REPL. Whatever comes back is the answer."

What Clojure form computes the keyword :pre-failed when the pre-check rejects -1? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exception e :pre-failed))"}}]}
```

### Record 3 — example 1 of 2

**form**: `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` • **expected**: `10`

**concept_phrase**: `a fn with a :pre condition that is satisfied`

**question_what**: `the value returned when the precondition holds and 5 is doubled`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A wooden notice nailed to a post atop the hilltop carried a small puzzle. The
riddle simply asked the reader to evaluate `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)`. Jess
laughed, as if the race were already won, and declared it too easy to bother with.
Morgan said, patiently, that the only way to be certain of
a fn with a :pre condition that is satisfied was to put it in the REPL.

Question: write a Clojure expression for the value returned when the precondition holds and 5 is doubled.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] {:pre [(pos? x)]} (* x 2)) 5)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exception e :pre-failed))` • **expected**: `':pre-failed'`

**concept_phrase**: `a :pre condition that fails, caught by surrounding try`

**question_what**: `the keyword :pre-failed when the pre-check rejects -1`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exception e :pre-failed))`, and the line
above it read a :pre condition that fails, caught by surrounding try. Robin handed the page to
Pat, who, lulled by the gentle wind, agreed to write it out properly.

Write a Clojure expression that computes the keyword :pre-failed when the pre-check rejects -1.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exception e :pre-failed))"}}]}
```

### Record 5 — example 1 of 2

**form**: `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` • **expected**: `10`

**concept_phrase**: `a fn with a :pre condition that is satisfied`

**question_what**: `the value returned when the precondition holds and 5 is doubled`

```
Every shepherd in the valley knew the danger of crying wolf for sport. It happened along the road.

A small slate sat on a flat stone near the road; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)`, and the page
heading read a fn with a :pre condition that is satisfied. George nodded at Will to
write the form properly so the slate would carry an honest entry.

What Clojure form computes the value returned when the precondition holds and 5 is doubled? Submit it via `eval`.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] {:pre [(pos? x)]} (* x 2)) 5)"}}]}
```

---

## G7-07: assert

**Examples:** 2 | **Subplots:** 13 | **Plan-pool size:** 11

### Record 1 — example 1 of 2

**form**: `(do (assert (= 1 1)) :ok)` • **expected**: `':ok'`

**concept_phrase**: `an assert that passes, followed by a return value`

**question_what**: `the keyword :ok returned after the assert succeeds`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A small crowd of villagers had gathered by the woods to watch
Tom attempt to predict, off the cuff, what the REPL would
return. Robin pointed to an assert that passes, followed by a return value and read out the
form aloud: `(do (assert (= 1 1)) :ok)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

What Clojure form computes the keyword :ok returned after the assert succeeds? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (assert (= 1 1)) :ok)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(try (assert (= 1 2)) (catch Throwable e :asserted))` • **expected**: `':asserted'`

**concept_phrase**: `an assert that fails, caught by surrounding try`

**question_what**: `the keyword :asserted when the assertion rejects (= 1 2)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place near the meadow.

A wooden notice nailed to a post by the meadow carried a small puzzle. The
riddle simply asked the reader to evaluate `(try (assert (= 1 2)) (catch Throwable e :asserted))`. Jess
laughed, puffed up with pride, and declared it too easy to bother with.
Oliver said, patiently, that the only way to be certain of
an assert that fails, caught by surrounding try was to put it in the REPL.

Write a Clojure expression that computes the keyword :asserted when the assertion rejects (= 1 2).

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(try (assert (= 1 2)) (catch Throwable e :asserted))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (assert (= 1 1)) :ok)` • **expected**: `':ok'`

**concept_phrase**: `an assert that passes, followed by a return value`

**question_what**: `the keyword :ok returned after the assert succeeds`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place on the hilltop.

"There is no need to evaluate that," Will said, boasting at every turn.
"Anyone can see what an assert that passes, followed by a return value comes to." Oliver, who
at the edge of the hilltop had heard such claims many times, asked him to
actually write the form `(do (assert (= 1 1)) :ok)` and submit it to the REPL —
just to be sure.

What Clojure form computes the keyword :ok returned after the assert succeeds? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (assert (= 1 1)) :ok)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(try (assert (= 1 2)) (catch Throwable e :asserted))` • **expected**: `':asserted'`

**concept_phrase**: `an assert that fails, caught by surrounding try`

**question_what**: `the keyword :asserted when the assertion rejects (= 1 2)`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Halfway through the morning watch, Tom called out
in the orchard, demanding a verdict on the form `(try (assert (= 1 2)) (catch Throwable e :asserted))` and refusing
to descend until somebody confirmed it. Tom insisted
he already knew the answer. Alex, walking up
at an unhurried pace, simply said: "Submit an assert that fails, caught by surrounding try to the
REPL. Whatever comes back is the answer."

Write a Clojure expression that computes the keyword :asserted when the assertion rejects (= 1 2).

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(try (assert (= 1 2)) (catch Throwable e :asserted))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (assert (= 1 1)) :ok)` • **expected**: `':ok'`

**concept_phrase**: `an assert that passes, followed by a return value`

**question_what**: `the keyword :ok returned after the assert succeeds`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A small slate sat on a flat stone near the farm; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(do (assert (= 1 1)) :ok)`, and the page
heading read an assert that passes, followed by a return value. George nodded at Jess to
write the form properly so the slate would carry an honest entry.

What Clojure form computes the keyword :ok returned after the assert succeeds? Submit it via `eval`.

---

I print or tap the value for inspection, then return.

{"tool_calls":[{"name":"eval","args":{"form":"(do (assert (= 1 1)) :ok)"}}]}
```

---

## G7-08: prn and pprint

**Examples:** 2 | **Subplots:** 13 | **Plan-pool size:** 11

### Record 1 — example 1 of 2

**form**: `(with-out-str (prn 42))` • **expected**: `'42\n'`

**concept_phrase**: `capturing the output of (prn 42)`

**question_what**: `the string "42\n" produced by prn`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened near the orchard.

A small slip of paper in the orchard carried the form `(with-out-str (prn 42))`.
Tom glanced at it and shrugged the warning off, certain there
was no trouble. Oliver sat down, stepping deliberately, and worked
through capturing the output of (prn 42) step by step — ready, if anything went wrong,
to read the stack trace from top to bottom and try the form again.

Write a form whose evaluation gives the string "42\n" produced by prn.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (prn 42))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(with-out-str (prn :wolf))` • **expected**: `':wolf\n'`

**concept_phrase**: `capturing prn applied to the keyword :wolf`

**question_what**: `the string ":wolf\n" produced by prn`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened by the orchard.

"There is no need to evaluate that," Pat said, puffed up with pride.
"Anyone can see what capturing prn applied to the keyword :wolf comes to." Alex, who
by the orchard had heard such claims many times, asked them to
actually write the form `(with-out-str (prn :wolf))` and submit it to the REPL —
just to be sure.

Write a Clojure expression that computes the string ":wolf\n" produced by prn.

---

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (prn :wolf))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(with-out-str (prn 42))` • **expected**: `'42\n'`

**concept_phrase**: `capturing the output of (prn 42)`

**question_what**: `the string "42\n" produced by prn`

```
The boy on the hill thought the trick clever the first time he played it. It happened at the edge of the farm.

Will had cried alarm so often that the runtime now took
every careless throw at its word. near the farm, Grace typed
`(with-out-str (prn 42))` carefully, ready to catch whatever the REPL might raise.
Will, as if the race were already won, said no error would ever come — but Grace
insisted on letting the runtime decide, then reading capturing the output of (prn 42)
from whatever it returned.

Write a Clojure expression that computes the string "42\n" produced by prn.

---

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (prn 42))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(with-out-str (prn :wolf))` • **expected**: `':wolf\n'`

**concept_phrase**: `capturing prn applied to the keyword :wolf`

**question_what**: `the string ":wolf\n" produced by prn`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place in the meadow.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(with-out-str (prn :wolf))`, and the line
above it read capturing prn applied to the keyword :wolf. Sam handed the page to
Tom, who, her legs heavy from sprinting, agreed to write it out properly.

Write a Clojure expression that computes the string ":wolf\n" produced by prn.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (prn :wolf))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(with-out-str (prn 42))` • **expected**: `'42\n'`

**concept_phrase**: `capturing the output of (prn 42)`

**question_what**: `the string "42\n" produced by prn`

```
The boy on the hill thought the trick clever the first time he played it.

A wooden notice nailed to a post by the orchard carried a small puzzle. The
riddle simply asked the reader to evaluate `(with-out-str (prn 42))`. Pat
laughed, with great whoops of laughter, and declared it too easy to bother with.
Oliver said, patiently, that the only way to be certain of
capturing the output of (prn 42) was to put it in the REPL.

Write a Clojure expression that computes the string "42\n" produced by prn.

---

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (prn 42))"}}]}
```

---

## G7-09: tap>

**Examples:** 2 | **Subplots:** 13 | **Plan-pool size:** 11

### Record 1 — example 1 of 2

**form**: `(tap> :hello)` • **expected**: `True`

**concept_phrase**: `tapping a value into the tap pool`

**question_what**: `the boolean true returned by tap>`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place in the woods.

Halfway through the morning watch, Will called out
at the edge of the woods, demanding a verdict on the form `(tap> :hello)` and refusing
to descend until somebody confirmed it. Will insisted
he already knew the answer. George, walking up
at an unhurried pace, simply said: "Submit tapping a value into the tap pool to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the boolean true returned by tap>.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(tap> :hello)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(tap> 42)` • **expected**: `True`

**concept_phrase**: `tapping the number 42 into the tap pool`

**question_what**: `the boolean true (tap> always returns true on send)`

```
The boy on the hill thought the trick clever the first time he played it.

"There is no need to evaluate that," Pat said, swaggering through the underbrush.
"Anyone can see what tapping the number 42 into the tap pool comes to." Alice, who
by the forest had heard such claims many times, asked them to
actually write the form `(tap> 42)` and submit it to the REPL —
just to be sure.

Write a form whose evaluation gives the boolean true (tap> always returns true on send).

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(tap> 42)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(tap> :hello)` • **expected**: `True`

**concept_phrase**: `tapping a value into the tap pool`

**question_what**: `the boolean true returned by tap>`

```
The boy on the hill thought the trick clever the first time he played it.

A small slip of paper in the orchard carried the form `(tap> :hello)`.
Jess glanced at it and shrugged the warning off, certain there
was no trouble. Morgan sat down, her eyes always on the path, and worked
through tapping a value into the tap pool step by step — ready, if anything went wrong,
to read the stack trace from top to bottom and try the form again.

Write a Clojure expression that computes the boolean true returned by tap>.

---

{"tool_calls":[{"name":"eval","args":{"form":"(tap> :hello)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(tap> 42)` • **expected**: `True`

**concept_phrase**: `tapping the number 42 into the tap pool`

**question_what**: `the boolean true (tap> always returns true on send)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(tap> 42)`, and the line
above it read tapping the number 42 into the tap pool. Carol handed the page to
Pat, who, drowsy from the warm sun, agreed to write it out properly.

Write a form whose evaluation gives the boolean true (tap> always returns true on send).

---

{"tool_calls":[{"name":"eval","args":{"form":"(tap> 42)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(tap> :hello)` • **expected**: `True`

**concept_phrase**: `tapping a value into the tap pool`

**question_what**: `the boolean true returned by tap>`

```
The boy on the hill thought the trick clever the first time he played it.

Halfway through the morning watch, Tom called out
by the woods, demanding a verdict on the form `(tap> :hello)` and refusing
to descend until somebody confirmed it. Tom insisted
he already knew the answer. George, walking up
at an unhurried pace, simply said: "Submit tapping a value into the tap pool to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the boolean true returned by tap>.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(tap> :hello)"}}]}
```

---

## G7-10: doc and source

**Examples:** 1 | **Subplots:** 13 | **Plan-pool size:** 11

### Record 1 — example 1 of 1

**form**: `(:doc (meta '^{:doc "adds two"} plus))` • **expected**: `'adds two'`

**concept_phrase**: `the :doc metadata on a symbol — what doc would print`

**question_what**: `the string "adds two" from the metadata`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Lou called down from a stone atop the hilltop where someone had
chalked the :doc metadata on a symbol — what doc would print on a flat board. Lou, boasting at every turn,
declared she already knew what would come back. Grace,
with steady, careful steps, asked her to actually submit the form
`(:doc (meta '^{:doc "adds two"} plus))` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the string "adds two" from the metadata.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"adds two\"} plus))"}}]}
```

### Record 2 — example 1 of 1

**form**: `(:doc (meta '^{:doc "adds two"} plus))` • **expected**: `'adds two'`

**concept_phrase**: `the :doc metadata on a symbol — what doc would print`

**question_what**: `the string "adds two" from the metadata`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A small crowd of villagers had gathered at the edge of the woods to watch
Lou attempt to predict, off the cuff, what the REPL would
return. Morgan pointed to the :doc metadata on a symbol — what doc would print and read out the
form aloud: `(:doc (meta '^{:doc "adds two"} plus))`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a Clojure expression that computes the string "adds two" from the metadata.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"adds two\"} plus))"}}]}
```

### Record 3 — example 1 of 1

**form**: `(:doc (meta '^{:doc "adds two"} plus))` • **expected**: `'adds two'`

**concept_phrase**: `the :doc metadata on a symbol — what doc would print`

**question_what**: `the string "adds two" from the metadata`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Alice had been trying to teach Tom how the REPL
works. "Look here," she said, pointing to the :doc metadata on a symbol — what doc would print.
"You hand the form `(:doc (meta '^{:doc "adds two"} plus))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Tom, drowsy from the warm sun, agreed to try.

What Clojure form computes the string "adds two" from the metadata? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"adds two\"} plus))"}}]}
```

### Record 4 — example 1 of 1

**form**: `(:doc (meta '^{:doc "adds two"} plus))` • **expected**: `'adds two'`

**concept_phrase**: `the :doc metadata on a symbol — what doc would print`

**question_what**: `the string "adds two" from the metadata`

```
The boy on the hill thought the trick clever the first time he played it.

Lou had cried alarm so often that the runtime now took
every careless throw at its word. at the edge of the meadow, Frank typed
`(:doc (meta '^{:doc "adds two"} plus))` carefully, ready to catch whatever the REPL might raise.
Lou, as if the race were already won, said no error would ever come — but Frank
insisted on letting the runtime decide, then reading the :doc metadata on a symbol — what doc would print
from whatever it returned.

Write a Clojure expression that computes the string "adds two" from the metadata.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"adds two\"} plus))"}}]}
```

### Record 5 — example 1 of 1

**form**: `(:doc (meta '^{:doc "adds two"} plus))` • **expected**: `'adds two'`

**concept_phrase**: `the :doc metadata on a symbol — what doc would print`

**question_what**: `the string "adds two" from the metadata`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Beyond the REPL the world had files, streams, and surprises.
Robin opened a small notebook by the farm, copying down
the :doc metadata on a symbol — what doc would print. Tom, lulled by the gentle wind, watched as they
wrote the form `(:doc (meta '^{:doc "adds two"} plus))` so the runtime could carry the work the
rest of the way.

Write a form whose evaluation gives the string "adds two" from the metadata.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"adds two\"} plus))"}}]}
```

---

## G7-11: Reading stack traces

**Examples:** 2 | **Subplots:** 13 | **Plan-pool size:** 11

### Record 1 — example 1 of 2

**form**: `(try (throw (Exception. "oops")) (catch Exception e (.getMessage e)))` • **expected**: `'oops'`

**concept_phrase**: `extracting the message from a caught exception`

**question_what**: `the string "oops" from the caught Exception`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened in the meadow.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(try (throw (Exception. "oops")) (catch Exception e (.getMessage e)))`, and the line
above it read extracting the message from a caught exception. Bob handed the page to
Will, who, her legs heavy from sprinting, agreed to write it out properly.

Question: write a Clojure expression for the string "oops" from the caught Exception.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (Exception. \"oops\")) (catch Exception e (.getMessage e)))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(try (throw (ex-info "trouble" {})) (catch Exception e (.getMessage e)))` • **expected**: `'trouble'`

**concept_phrase**: `the message of a caught ex-info`

**question_what**: `the string "trouble"`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place near the road.

A small slate sat on a flat stone near the road; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(try (throw (ex-info "trouble" {})) (catch Exception e (.getMessage e)))`, and the page
heading read the message of a caught ex-info. Sam nodded at Jess to
write the form properly so the slate would carry an honest entry.

Write a Clojure expression that computes the string "trouble".

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (ex-info \"trouble\" {})) (catch Exception e (.getMessage e)))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(try (throw (Exception. "oops")) (catch Exception e (.getMessage e)))` • **expected**: `'oops'`

**concept_phrase**: `extracting the message from a caught exception`

**question_what**: `the string "oops" from the caught Exception`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Will had cried alarm so often that the runtime now took
every careless throw at its word. in the village, Alex typed
`(try (throw (Exception. "oops")) (catch Exception e (.getMessage e)))` carefully, ready to catch whatever the REPL might raise.
Will, with great whoops of laughter, said no error would ever come — but Alex
insisted on letting the runtime decide, then reading extracting the message from a caught exception
from whatever it returned.

Write a Clojure expression that computes the string "oops" from the caught Exception.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (Exception. \"oops\")) (catch Exception e (.getMessage e)))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(try (throw (ex-info "trouble" {})) (catch Exception e (.getMessage e)))` • **expected**: `'trouble'`

**concept_phrase**: `the message of a caught ex-info`

**question_what**: `the string "trouble"`

```
The boy on the hill thought the trick clever the first time he played it.

Beyond the REPL the world had files, streams, and surprises.
Frank opened a small notebook near the woods, copying down
the message of a caught ex-info. Lou, her legs heavy from sprinting, watched as he
wrote the form `(try (throw (ex-info "trouble" {})) (catch Exception e (.getMessage e)))` so the runtime could carry the work the
rest of the way.

Write a form whose evaluation gives the string "trouble".

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (ex-info \"trouble\" {})) (catch Exception e (.getMessage e)))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(try (throw (Exception. "oops")) (catch Exception e (.getMessage e)))` • **expected**: `'oops'`

**concept_phrase**: `extracting the message from a caught exception`

**question_what**: `the string "oops" from the caught Exception`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place by the orchard.

A small crowd of villagers had gathered near the orchard to watch
Lou attempt to predict, off the cuff, what the REPL would
return. Carol pointed to extracting the message from a caught exception and read out the
form aloud: `(try (throw (Exception. "oops")) (catch Exception e (.getMessage e)))`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a form whose evaluation gives the string "oops" from the caught Exception.

---

I wrap the form in try/catch and let the REPL handle the error.

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (Exception. \"oops\")) (catch Exception e (.getMessage e)))"}}]}
```

---

## G7-12: slurp and spit

**Examples:** 2 | **Subplots:** 13 | **Plan-pool size:** 11

### Record 1 — example 1 of 2

**form**: `(count "wolf\nshepherd\n")` • **expected**: `14`

**concept_phrase**: `the length of a multi-line string (as if read by slurp)`

**question_what**: `the count of characters in "wolf\nshepherd\n"`

```
The boy on the hill thought the trick clever the first time he played it. This was near the orchard.

Grace had been trying to teach Jess how the REPL
works. "Look here," she said, pointing to the length of a multi-line string (as if read by slurp).
"You hand the form `(count "wolf\nshepherd\n")` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, weary from the morning's effort, agreed to try.

Write a Clojure expression that computes the count of characters in "wolf\nshepherd\n".

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"wolf\\nshepherd\\n\")"}}]}
```

### Record 2 — example 2 of 2

**form**: `(clojure.string/split "a\nb\nc" #"\n")` • **expected**: `['a', 'b', 'c']`

**concept_phrase**: `splitting a slurped-style string on newlines`

**question_what**: `the vector ["a" "b" "c"] of three lines`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Frank had been trying to teach Will how the REPL
works. "Look here," he said, pointing to splitting a slurped-style string on newlines.
"You hand the form `(clojure.string/split "a\nb\nc" #"\n")` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Will, lulled by the gentle wind, agreed to try.

Question: write a Clojure expression for the vector ["a" "b" "c"] of three lines.

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/split \"a\\nb\\nc\" #\"\\n\")"}}]}
```

### Record 3 — example 1 of 2

**form**: `(count "wolf\nshepherd\n")` • **expected**: `14`

**concept_phrase**: `the length of a multi-line string (as if read by slurp)`

**question_what**: `the count of characters in "wolf\nshepherd\n"`

```
The boy on the hill thought the trick clever the first time he played it. It happened along the road.

The elder of the village kept a small slate near the road, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the length of a multi-line string (as if read by slurp). George read
out the form `(count "wolf\nshepherd\n")` so Tom could write it
properly into the REPL and earn an honest mark on the slate.

What Clojure form computes the count of characters in "wolf\nshepherd\n"? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"wolf\\nshepherd\\n\")"}}]}
```

### Record 4 — example 2 of 2

**form**: `(clojure.string/split "a\nb\nc" #"\n")` • **expected**: `['a', 'b', 'c']`

**concept_phrase**: `splitting a slurped-style string on newlines`

**question_what**: `the vector ["a" "b" "c"] of three lines`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A small slate sat on a flat stone on the road; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(clojure.string/split "a\nb\nc" #"\n")`, and the page
heading read splitting a slurped-style string on newlines. Frank nodded at Will to
write the form properly so the slate would carry an honest entry.

Question: write a Clojure expression for the vector ["a" "b" "c"] of three lines.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/split \"a\\nb\\nc\" #\"\\n\")"}}]}
```

### Record 5 — example 1 of 2

**form**: `(count "wolf\nshepherd\n")` • **expected**: `14`

**concept_phrase**: `the length of a multi-line string (as if read by slurp)`

**question_what**: `the count of characters in "wolf\nshepherd\n"`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Beyond the REPL the world had files, streams, and surprises.
Oliver opened a small notebook in the farm, copying down
the length of a multi-line string (as if read by slurp). Tom, yawning at the soft moss, watched as he
wrote the form `(count "wolf\nshepherd\n")` so the runtime could carry the work the
rest of the way.

What Clojure form computes the count of characters in "wolf\nshepherd\n"? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count \"wolf\\nshepherd\\n\")"}}]}
```

---

## G7-13: line-seq

**Examples:** 2 | **Subplots:** 13 | **Plan-pool size:** 11

### Record 1 — example 1 of 2

**form**: `(count (clojure.string/split-lines "a\nb\nc"))` • **expected**: `3`

**concept_phrase**: `the number of lines in a small text`

**question_what**: `the count of lines in "a\nb\nc"`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Pat had cried alarm so often that the runtime now took
every careless throw at its word. at the edge of the woods, Sam typed
`(count (clojure.string/split-lines "a\nb\nc"))` carefully, ready to catch whatever the REPL might raise.
Pat, with great whoops of laughter, said no error would ever come — but Sam
insisted on letting the runtime decide, then reading the number of lines in a small text
from whatever it returned.

Write a Clojure expression that computes the count of lines in "a\nb\nc".

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(count (clojure.string/split-lines \"a\\nb\\nc\"))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(first (clojure.string/split-lines "first\nsecond"))` • **expected**: `'first'`

**concept_phrase**: `the first line of a small text`

**question_what**: `the string "first"`

```
The boy on the hill thought the trick clever the first time he played it.

George kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today in the forest the next entry was
the first line of a small text. Jess peered over his shoulder
at the form `(first (clojure.string/split-lines "first\nsecond"))` and was asked, gently, to be the one to
submit it.

Write a Clojure expression that computes the string "first".

---

{"tool_calls":[{"name":"eval","args":{"form":"(first (clojure.string/split-lines \"first\\nsecond\"))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(count (clojure.string/split-lines "a\nb\nc"))` • **expected**: `3`

**concept_phrase**: `the number of lines in a small text`

**question_what**: `the count of lines in "a\nb\nc"`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened at the edge of the farm.

Bob had been trying to teach Tom how the REPL
works. "Look here," he said, pointing to the number of lines in a small text.
"You hand the form `(count (clojure.string/split-lines "a\nb\nc"))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Tom, drowsy from the warm sun, agreed to try.

What Clojure form computes the count of lines in "a\nb\nc"? Submit it via `eval`.

---

I let the REPL read the file or stream for me.

{"tool_calls":[{"name":"eval","args":{"form":"(count (clojure.string/split-lines \"a\\nb\\nc\"))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(first (clojure.string/split-lines "first\nsecond"))` • **expected**: `'first'`

**concept_phrase**: `the first line of a small text`

**question_what**: `the string "first"`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. This was at the edge of the forest.

Lou called down from a stone near the forest where someone had
chalked the first line of a small text on a flat board. Lou, with a smug grin,
declared she already knew what would come back. Morgan,
stepping deliberately, asked her to actually submit the form
`(first (clojure.string/split-lines "first\nsecond"))` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the string "first".

---

{"tool_calls":[{"name":"eval","args":{"form":"(first (clojure.string/split-lines \"first\\nsecond\"))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(count (clojure.string/split-lines "a\nb\nc"))` • **expected**: `3`

**concept_phrase**: `the number of lines in a small text`

**question_what**: `the count of lines in "a\nb\nc"`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Lou called down from a stone near the woods where someone had
chalked the number of lines in a small text on a flat board. Lou, boasting at every turn,
declared she already knew what would come back. Alex,
stepping deliberately, asked her to actually submit the form
`(count (clojure.string/split-lines "a\nb\nc"))` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the count of lines in "a\nb\nc".

---

{"tool_calls":[{"name":"eval","args":{"form":"(count (clojure.string/split-lines \"a\\nb\\nc\"))"}}]}
```

---

## G7-14: with-open

**Examples:** 1 | **Subplots:** 13 | **Plan-pool size:** 11

### Record 1 — example 1 of 1

**form**: `(with-out-str (println "wolf"))` • **expected**: `'wolf\n'`

**concept_phrase**: `a resource-scoped capture of println output`

**question_what**: `the string "wolf\n" from the scoped block`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Carol had been trying to teach Jess how the REPL
works. "Look here," she said, pointing to a resource-scoped capture of println output.
"You hand the form `(with-out-str (println "wolf"))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, lulled by the gentle wind, agreed to try.

Question: write a Clojure expression for the string "wolf\n" from the scoped block.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (println \"wolf\"))"}}]}
```

### Record 2 — example 1 of 1

**form**: `(with-out-str (println "wolf"))` • **expected**: `'wolf\n'`

**concept_phrase**: `a resource-scoped capture of println output`

**question_what**: `the string "wolf\n" from the scoped block`

```
The boy on the hill thought the trick clever the first time he played it. All this took place atop the hilltop.

Grace had been trying to teach Pat how the REPL
works. "Look here," she said, pointing to a resource-scoped capture of println output.
"You hand the form `(with-out-str (println "wolf"))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Pat, yawning at the soft moss, agreed to try.

Write a form whose evaluation gives the string "wolf\n" from the scoped block.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (println \"wolf\"))"}}]}
```

### Record 3 — example 1 of 1

**form**: `(with-out-str (println "wolf"))` • **expected**: `'wolf\n'`

**concept_phrase**: `a resource-scoped capture of println output`

**question_what**: `the string "wolf\n" from the scoped block`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Morgan had been trying to teach Will how the REPL
works. "Look here," they said, pointing to a resource-scoped capture of println output.
"You hand the form `(with-out-str (println "wolf"))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Will, yawning at the soft moss, agreed to try.

Question: write a Clojure expression for the string "wolf\n" from the scoped block.

---

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (println \"wolf\"))"}}]}
```

### Record 4 — example 1 of 1

**form**: `(with-out-str (println "wolf"))` • **expected**: `'wolf\n'`

**concept_phrase**: `a resource-scoped capture of println output`

**question_what**: `the string "wolf\n" from the scoped block`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

The elder of the village kept a small slate in the orchard, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was a resource-scoped capture of println output. Sam read
out the form `(with-out-str (println "wolf"))` so Will could write it
properly into the REPL and earn an honest mark on the slate.

Write a form whose evaluation gives the string "wolf\n" from the scoped block.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (println \"wolf\"))"}}]}
```

### Record 5 — example 1 of 1

**form**: `(with-out-str (println "wolf"))` • **expected**: `'wolf\n'`

**concept_phrase**: `a resource-scoped capture of println output`

**question_what**: `the string "wolf\n" from the scoped block`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(with-out-str (println "wolf"))`, and the line
above it read a resource-scoped capture of println output. Grace handed the page to
Jess, who, lulled by the gentle wind, agreed to write it out properly.

What Clojure form computes the string "wolf\n" from the scoped block? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (println \"wolf\"))"}}]}
```

---

## G7-15: *in* and *out*

**Examples:** 2 | **Subplots:** 13 | **Plan-pool size:** 11

### Record 1 — example 1 of 2

**form**: `(with-out-str (print "x"))` • **expected**: `'x'`

**concept_phrase**: `redirecting *out* via with-out-str and printing`

**question_what**: `the string "x" captured from *out*`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A small slip of paper near the meadow carried the form `(with-out-str (print "x"))`.
Lou glanced at it and shrugged the warning off, certain there
was no trouble. Grace sat down, without complaint, and worked
through redirecting *out* via with-out-str and printing step by step — ready, if anything went wrong,
to read the stack trace from top to bottom and try the form again.

What Clojure form computes the string "x" captured from *out*? Submit it via `eval`.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (print \"x\"))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(with-out-str (println))` • **expected**: `'\n'`

**concept_phrase**: `a bare println redirected through *out*`

**question_what**: `the string "\n"`

```
Every shepherd in the valley knew the danger of crying wolf for sport. This was near the hilltop.

Tom called down from a stone atop the hilltop where someone had
chalked a bare println redirected through *out* on a flat board. Tom, as if the race were already won,
declared he already knew what would come back. Alex,
untroubled by what others thought, asked him to actually submit the form
`(with-out-str (println))` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the string "\n".

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (println))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(with-out-str (print "x"))` • **expected**: `'x'`

**concept_phrase**: `redirecting *out* via with-out-str and printing`

**question_what**: `the string "x" captured from *out*`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Lou had cried alarm so often that the runtime now took
every careless throw at its word. near the orchard, George typed
`(with-out-str (print "x"))` carefully, ready to catch whatever the REPL might raise.
Lou, boasting at every turn, said no error would ever come — but George
insisted on letting the runtime decide, then reading redirecting *out* via with-out-str and printing
from whatever it returned.

Write a Clojure expression that computes the string "x" captured from *out*.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (print \"x\"))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(with-out-str (println))` • **expected**: `'\n'`

**concept_phrase**: `a bare println redirected through *out*`

**question_what**: `the string "\n"`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Will had cried alarm so often that the runtime now took
every careless throw at its word. near the meadow, Frank typed
`(with-out-str (println))` carefully, ready to catch whatever the REPL might raise.
Will, swaggering through the underbrush, said no error would ever come — but Frank
insisted on letting the runtime decide, then reading a bare println redirected through *out*
from whatever it returned.

Question: write a Clojure expression for the string "\n".

---

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (println))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(with-out-str (print "x"))` • **expected**: `'x'`

**concept_phrase**: `redirecting *out* via with-out-str and printing`

**question_what**: `the string "x" captured from *out*`

```
The boy on the hill thought the trick clever the first time he played it. All this took place in the village.

"There is no need to evaluate that," Jess said, boasting at every turn.
"Anyone can see what redirecting *out* via with-out-str and printing comes to." Carol, who
at the edge of the village had heard such claims many times, asked her to
actually write the form `(with-out-str (print "x"))` and submit it to the REPL —
just to be sure.

Write a Clojure expression that computes the string "x" captured from *out*.

---

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (print \"x\"))"}}]}
```

---

## G7-16: edn read

**Examples:** 3 | **Subplots:** 13 | **Plan-pool size:** 11

### Record 1 — example 1 of 3

**form**: `(clojure.edn/read-string "42")` • **expected**: `42`

**concept_phrase**: `reading an edn integer from a string`

**question_what**: `the integer 42 read from "42"`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(clojure.edn/read-string "42")`, and the line
above it read reading an edn integer from a string. Sam handed the page to
Pat, who, her legs heavy from sprinting, agreed to write it out properly.

Write a form whose evaluation gives the integer 42 read from "42".

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"42\")"}}]}
```

### Record 2 — example 2 of 3

**form**: `(clojure.edn/read-string "{:a 1}")` • **expected**: `{':a': 1}`

**concept_phrase**: `reading an edn map from a string`

**question_what**: `the map {:a 1} read from "{:a 1}"`

```
The boy on the hill thought the trick clever the first time he played it. All this took place near the village.

"There is no need to evaluate that," Tom said, swaggering through the underbrush.
"Anyone can see what reading an edn map from a string comes to." Alice, who
at the edge of the village had heard such claims many times, asked him to
actually write the form `(clojure.edn/read-string "{:a 1}")` and submit it to the REPL —
just to be sure.

What Clojure form computes the map {:a 1} read from "{:a 1}"? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"{:a 1}\")"}}]}
```

### Record 3 — example 3 of 3

**form**: `(clojure.edn/read-string "[:wolf :flock]")` • **expected**: `[':wolf', ':flock']`

**concept_phrase**: `reading an edn vector of keywords`

**question_what**: `the vector [:wolf :flock]`

```
The boy on the hill thought the trick clever the first time he played it.

Halfway through the morning watch, Will called out
near the orchard, demanding a verdict on the form `(clojure.edn/read-string "[:wolf :flock]")` and refusing
to descend until somebody confirmed it. Will insisted
he already knew the answer. Carol, walking up
at an unhurried pace, simply said: "Submit reading an edn vector of keywords to the
REPL. Whatever comes back is the answer."

Write a form whose evaluation gives the vector [:wolf :flock].

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"[:wolf :flock]\")"}}]}
```

### Record 4 — example 1 of 3

**form**: `(clojure.edn/read-string "42")` • **expected**: `42`

**concept_phrase**: `reading an edn integer from a string`

**question_what**: `the integer 42 read from "42"`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Halfway through the morning watch, Tom called out
near the forest, demanding a verdict on the form `(clojure.edn/read-string "42")` and refusing
to descend until somebody confirmed it. Tom insisted
he already knew the answer. Sam, walking up
at an unhurried pace, simply said: "Submit reading an edn integer from a string to the
REPL. Whatever comes back is the answer."

Write a form whose evaluation gives the integer 42 read from "42".

---

I let the REPL read the file or stream for me.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"42\")"}}]}
```

### Record 5 — example 2 of 3

**form**: `(clojure.edn/read-string "{:a 1}")` • **expected**: `{':a': 1}`

**concept_phrase**: `reading an edn map from a string`

**question_what**: `the map {:a 1} read from "{:a 1}"`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Grace kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today at the edge of the village the next entry was
reading an edn map from a string. Will peered over her shoulder
at the form `(clojure.edn/read-string "{:a 1}")` and was asked, gently, to be the one to
submit it.

Write a Clojure expression that computes the map {:a 1} read from "{:a 1}".

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"{:a 1}\")"}}]}
```

---

## G7-17: JSON roundtrip

**Examples:** 2 | **Subplots:** 13 | **Plan-pool size:** 11

### Record 1 — example 1 of 2

**form**: `(clojure.edn/read-string (pr-str {:a 1 :b 2}))` • **expected**: `{':a': 1, ':b': 2}`

**concept_phrase**: `writing then reading back a small map (edn-shaped roundtrip)`

**question_what**: `the map {:a 1 :b 2} after the roundtrip`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place by the forest.

A wooden notice nailed to a post in the forest carried a small puzzle. The
riddle simply asked the reader to evaluate `(clojure.edn/read-string (pr-str {:a 1 :b 2}))`. Will
laughed, with a smug grin, and declared it too easy to bother with.
Grace said, patiently, that the only way to be certain of
writing then reading back a small map (edn-shaped roundtrip) was to put it in the REPL.

Question: write a Clojure expression for the map {:a 1 :b 2} after the roundtrip.

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string (pr-str {:a 1 :b 2}))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(clojure.edn/read-string (pr-str [1 2 3]))` • **expected**: `[1, 2, 3]`

**concept_phrase**: `round-tripping a vector through pr-str then edn/read-string`

**question_what**: `the vector [1 2 3]`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place by the forest.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(clojure.edn/read-string (pr-str [1 2 3]))`, and the line
above it read round-tripping a vector through pr-str then edn/read-string. George handed the page to
Tom, who, her legs heavy from sprinting, agreed to write it out properly.

Write a form whose evaluation gives the vector [1 2 3].

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string (pr-str [1 2 3]))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(clojure.edn/read-string (pr-str {:a 1 :b 2}))` • **expected**: `{':a': 1, ':b': 2}`

**concept_phrase**: `writing then reading back a small map (edn-shaped roundtrip)`

**question_what**: `the map {:a 1 :b 2} after the roundtrip`

```
The boy on the hill thought the trick clever the first time he played it.

The elder of the village kept a small slate at the edge of the meadow, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was writing then reading back a small map (edn-shaped roundtrip). Carol read
out the form `(clojure.edn/read-string (pr-str {:a 1 :b 2}))` so Tom could write it
properly into the REPL and earn an honest mark on the slate.

Question: write a Clojure expression for the map {:a 1 :b 2} after the roundtrip.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string (pr-str {:a 1 :b 2}))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(clojure.edn/read-string (pr-str [1 2 3]))` • **expected**: `[1, 2, 3]`

**concept_phrase**: `round-tripping a vector through pr-str then edn/read-string`

**question_what**: `the vector [1 2 3]`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Beyond the REPL the world had files, streams, and surprises.
Alex opened a small notebook near the forest, copying down
round-tripping a vector through pr-str then edn/read-string. Will, weary from the morning's effort, watched as they
wrote the form `(clojure.edn/read-string (pr-str [1 2 3]))` so the runtime could carry the work the
rest of the way.

Write a form whose evaluation gives the vector [1 2 3].

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string (pr-str [1 2 3]))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(clojure.edn/read-string (pr-str {:a 1 :b 2}))` • **expected**: `{':a': 1, ':b': 2}`

**concept_phrase**: `writing then reading back a small map (edn-shaped roundtrip)`

**question_what**: `the map {:a 1 :b 2} after the roundtrip`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Pat had cried alarm so often that the runtime now took
every careless throw at its word. by the woods, Morgan typed
`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` carefully, ready to catch whatever the REPL might raise.
Pat, swaggering through the underbrush, said no error would ever come — but Morgan
insisted on letting the runtime decide, then reading writing then reading back a small map (edn-shaped roundtrip)
from whatever it returned.

Write a Clojure expression that computes the map {:a 1 :b 2} after the roundtrip.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string (pr-str {:a 1 :b 2}))"}}]}
```

---

## G7-18: Shell command

**Examples:** 2 | **Subplots:** 13 | **Plan-pool size:** 11

### Record 1 — example 1 of 2

**form**: `(:cmd {:cmd "ls" :args ["-l"]})` • **expected**: `'ls'`

**concept_phrase**: `the :cmd portion of a shell-call descriptor map`

**question_what**: `the string "ls"`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Halfway through the morning watch, Pat called out
near the meadow, demanding a verdict on the form `(:cmd {:cmd "ls" :args ["-l"]})` and refusing
to descend until somebody confirmed it. Pat insisted
they already knew the answer. Alice, walking up
at an unhurried pace, simply said: "Submit the :cmd portion of a shell-call descriptor map to the
REPL. Whatever comes back is the answer."

Write a Clojure expression that computes the string "ls".

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(:cmd {:cmd \"ls\" :args [\"-l\"]})"}}]}
```

### Record 2 — example 2 of 2

**form**: `(count (:args {:cmd "echo" :args ["hello" "world"]}))` • **expected**: `2`

**concept_phrase**: `the number of args in a shell-call descriptor`

**question_what**: `the count of args, which is 2`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A small crowd of villagers had gathered near the orchard to watch
Jess attempt to predict, off the cuff, what the REPL would
return. Robin pointed to the number of args in a shell-call descriptor and read out the
form aloud: `(count (:args {:cmd "echo" :args ["hello" "world"]}))`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a Clojure expression that computes the count of args, which is 2.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count (:args {:cmd \"echo\" :args [\"hello\" \"world\"]}))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(:cmd {:cmd "ls" :args ["-l"]})` • **expected**: `'ls'`

**concept_phrase**: `the :cmd portion of a shell-call descriptor map`

**question_what**: `the string "ls"`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Lou had cried alarm so often that the runtime now took
every careless throw at its word. near the road, Sam typed
`(:cmd {:cmd "ls" :args ["-l"]})` carefully, ready to catch whatever the REPL might raise.
Lou, puffed up with pride, said no error would ever come — but Sam
insisted on letting the runtime decide, then reading the :cmd portion of a shell-call descriptor map
from whatever it returned.

Write a form whose evaluation gives the string "ls".

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(:cmd {:cmd \"ls\" :args [\"-l\"]})"}}]}
```

### Record 4 — example 2 of 2

**form**: `(count (:args {:cmd "echo" :args ["hello" "world"]}))` • **expected**: `2`

**concept_phrase**: `the number of args in a shell-call descriptor`

**question_what**: `the count of args, which is 2`

```
The boy on the hill thought the trick clever the first time he played it. All this took place near the meadow.

A small crowd of villagers had gathered near the meadow to watch
Will attempt to predict, off the cuff, what the REPL would
return. Oliver pointed to the number of args in a shell-call descriptor and read out the
form aloud: `(count (:args {:cmd "echo" :args ["hello" "world"]}))`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a form whose evaluation gives the count of args, which is 2.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count (:args {:cmd \"echo\" :args [\"hello\" \"world\"]}))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(:cmd {:cmd "ls" :args ["-l"]})` • **expected**: `'ls'`

**concept_phrase**: `the :cmd portion of a shell-call descriptor map`

**question_what**: `the string "ls"`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Lou had cried alarm so often that the runtime now took
every careless throw at its word. by the village, Sam typed
`(:cmd {:cmd "ls" :args ["-l"]})` carefully, ready to catch whatever the REPL might raise.
Lou, with great whoops of laughter, said no error would ever come — but Sam
insisted on letting the runtime decide, then reading the :cmd portion of a shell-call descriptor map
from whatever it returned.

Write a Clojure expression that computes the string "ls".

---

{"tool_calls":[{"name":"eval","args":{"form":"(:cmd {:cmd \"ls\" :args [\"-l\"]})"}}]}
```

---

