# Boy-wolf Grade 9 — deep spot-check

5 generated records per subject (across all examples and a variety of seeds). Read every record carefully. Flag anything that reads odd to a careful reader, including issues the structural audit can't catch (prose flow, contextual fit, cliché repetition, subplot/example mismatch, etc.)

---

## G9-01: Immutability as default — review

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(let [m {:a 1}] (assoc m :b 2) m)` • **expected**: `{':a': 1}`

**concept_phrase**: `binding m, calling (assoc m :b 2), then returning m unchanged`

**question_what**: `the original map after a non-mutating assoc`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Alice kept a small ledger of state near the woods — a value that
might change as the day went on, recording how many forms had been
honestly evaluated. She explained that the form
`(let [m {:a 1}] (assoc m :b 2) m)` captured binding m, calling (assoc m :b 2), then returning m unchanged: a careful, ordered update.
Pat, puffed up with pride, asked the REPL to confirm the final
value.

Write a Clojure expression that computes the original map after a non-mutating assoc.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :b 2) m)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(let [v [1 2 3]] (conj v 4) v)` • **expected**: `[1, 2, 3]`

**concept_phrase**: `binding v, calling (conj v 4), then returning v unchanged`

**question_what**: `the original vector after conj`

```
The boy on the hill thought the trick clever the first time he played it.

Lou called down from a stone in the village where someone had
chalked binding v, calling (conj v 4), then returning v unchanged on a flat board. Lou, puffed up with pride,
declared she already knew what would come back. Sam,
untroubled by what others thought, asked her to actually submit the form
`(let [v [1 2 3]] (conj v 4) v)` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the original vector after conj.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [v [1 2 3]] (conj v 4) v)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(let [m {:a 1}] (assoc m :b 2) m)` • **expected**: `{':a': 1}`

**concept_phrase**: `binding m, calling (assoc m :b 2), then returning m unchanged`

**question_what**: `the original map after a non-mutating assoc`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Frank kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today by the village the next entry was
binding m, calling (assoc m :b 2), then returning m unchanged. Pat peered over his shoulder
at the form `(let [m {:a 1}] (assoc m :b 2) m)` and was asked, gently, to be the one to
submit it.

Write a Clojure expression that computes the original map after a non-mutating assoc.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :b 2) m)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(let [v [1 2 3]] (conj v 4) v)` • **expected**: `[1, 2, 3]`

**concept_phrase**: `binding v, calling (conj v 4), then returning v unchanged`

**question_what**: `the original vector after conj`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden notice nailed to a post by the orchard carried a small puzzle. The
riddle simply asked the reader to evaluate `(let [v [1 2 3]] (conj v 4) v)`. Pat
laughed, puffed up with pride, and declared it too easy to bother with.
Oliver said, patiently, that the only way to be certain of
binding v, calling (conj v 4), then returning v unchanged was to put it in the REPL.

What Clojure form computes the original vector after conj? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [v [1 2 3]] (conj v 4) v)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(let [m {:a 1}] (assoc m :b 2) m)` • **expected**: `{':a': 1}`

**concept_phrase**: `binding m, calling (assoc m :b 2), then returning m unchanged`

**question_what**: `the original map after a non-mutating assoc`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Lou called down from a stone on the road where someone had
chalked binding m, calling (assoc m :b 2), then returning m unchanged on a flat board. Lou, with great whoops of laughter,
declared she already knew what would come back. Alex,
stepping deliberately, asked her to actually submit the form
`(let [m {:a 1}] (assoc m :b 2) m)` to the REPL — the village had stopped trusting answers
that weren't checked.

What Clojure form computes the original map after a non-mutating assoc? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :b 2) m)"}}]}
```

---

## G9-02: Why state at all

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do (def counter (atom 0)) (swap! counter inc) @counter)` • **expected**: `1`

**concept_phrase**: `an atom counter, incremented once, then read`

**question_what**: `the value of counter after one swap! inc`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Will called down from a stone by the orchard where someone had
chalked an atom counter, incremented once, then read on a flat board. Will, with a smug grin,
declared he already knew what would come back. Morgan,
stepping deliberately, asked him to actually submit the form
`(do (def counter (atom 0)) (swap! counter inc) @counter)` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a form whose evaluation gives the value of counter after one swap! inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def counter (atom 0)) (swap! counter inc) @counter)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (def progress (atom :idle)) (reset! progress :running) @progress)` • **expected**: `':running'`

**concept_phrase**: `a progress atom reset to :running`

**question_what**: `the value of progress after reset!`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place by the woods.

"Why bother with all this?" Tom demanded at the edge of the woods.
"He could just write the new value!" Grace,
saying very little, sketched out a progress atom reset to :running instead and showed the
form `(do (def progress (atom :idle)) (reset! progress :running) @progress)`: the proper way for the runtime to manage change.
They agreed to submit it to the REPL.

Write a Clojure expression that computes the value of progress after reset!.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def progress (atom :idle)) (reset! progress :running) @progress)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (def counter (atom 0)) (swap! counter inc) @counter)` • **expected**: `1`

**concept_phrase**: `an atom counter, incremented once, then read`

**question_what**: `the value of counter after one swap! inc`

```
The boy on the hill thought the trick clever the first time he played it. It happened by the woods.

A wooden notice nailed to a post in the woods carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (def counter (atom 0)) (swap! counter inc) @counter)`. Pat
laughed, swaggering through the underbrush, and declared it too easy to bother with.
Alice said, patiently, that the only way to be certain of
an atom counter, incremented once, then read was to put it in the REPL.

Write a form whose evaluation gives the value of counter after one swap! inc.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def counter (atom 0)) (swap! counter inc) @counter)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (def progress (atom :idle)) (reset! progress :running) @progress)` • **expected**: `':running'`

**concept_phrase**: `a progress atom reset to :running`

**question_what**: `the value of progress after reset!`

```
The boy on the hill thought the trick clever the first time he played it. This was along the road.

A small slate sat on a flat stone on the road; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(do (def progress (atom :idle)) (reset! progress :running) @progress)`, and the page
heading read a progress atom reset to :running. George nodded at Jess to
write the form properly so the slate would carry an honest entry.

Write a Clojure expression that computes the value of progress after reset!.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def progress (atom :idle)) (reset! progress :running) @progress)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (def counter (atom 0)) (swap! counter inc) @counter)` • **expected**: `1`

**concept_phrase**: `an atom counter, incremented once, then read`

**question_what**: `the value of counter after one swap! inc`

```
The boy on the hill thought the trick clever the first time he played it. This was by the forest.

A small crowd of villagers had gathered at the edge of the forest to watch
Lou attempt to predict, off the cuff, what the REPL would
return. George pointed to an atom counter, incremented once, then read and read out the
form aloud: `(do (def counter (atom 0)) (swap! counter inc) @counter)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

What Clojure form computes the value of counter after one swap! inc? Submit it via `eval`.

---

I bind the state, perform the update, then dereference.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def counter (atom 0)) (swap! counter inc) @counter)"}}]}
```

---

## G9-03: Atom introduction

**Examples:** 3 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 3

**form**: `(do (def a (atom 0)) (swap! a inc) @a)` • **expected**: `1`

**concept_phrase**: `an atom starting at 0, incremented once via swap!`

**question_what**: `the value of the atom after one swap! inc`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place at the edge of the village.

Alice had been trying to teach Will how the REPL
works. "Look here," she said, pointing to an atom starting at 0, incremented once via swap!.
"You hand the form `(do (def a (atom 0)) (swap! a inc) @a)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Will, drowsy from the warm sun, agreed to try.

Write a Clojure expression that computes the value of the atom after one swap! inc.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
```

### Record 2 — example 2 of 3

**form**: `(do (def a (atom 10)) (swap! a + 5) @a)` • **expected**: `15`

**concept_phrase**: `an atom starting at 10, with (swap! a + 5)`

**question_what**: `the value of the atom after swap! + 5`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened near the meadow.

Oliver had been trying to teach Lou how the REPL
works. "Look here," he said, pointing to an atom starting at 10, with (swap! a + 5).
"You hand the form `(do (def a (atom 10)) (swap! a + 5) @a)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Lou, yawning at the soft moss, agreed to try.

Write a form whose evaluation gives the value of the atom after swap! + 5.

---

I bind the state, perform the update, then dereference.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 10)) (swap! a + 5) @a)"}}]}
```

### Record 3 — example 3 of 3

**form**: `(do (def a (atom :start)) (reset! a :done) @a)` • **expected**: `':done'`

**concept_phrase**: `an atom reset! from :start to :done`

**question_what**: `the value of the atom after reset!`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A wooden notice nailed to a post at the edge of the meadow carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (def a (atom :start)) (reset! a :done) @a)`. Will
laughed, swaggering through the underbrush, and declared it too easy to bother with.
Oliver said, patiently, that the only way to be certain of
an atom reset! from :start to :done was to put it in the REPL.

Question: write a Clojure expression for the value of the atom after reset!.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom :start)) (reset! a :done) @a)"}}]}
```

### Record 4 — example 1 of 3

**form**: `(do (def a (atom 0)) (swap! a inc) @a)` • **expected**: `1`

**concept_phrase**: `an atom starting at 0, incremented once via swap!`

**question_what**: `the value of the atom after one swap! inc`

```
The boy on the hill thought the trick clever the first time he played it.

Frank had been trying to teach Will how the REPL
works. "Look here," he said, pointing to an atom starting at 0, incremented once via swap!.
"You hand the form `(do (def a (atom 0)) (swap! a inc) @a)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Will, lulled by the gentle wind, agreed to try.

What Clojure form computes the value of the atom after one swap! inc? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
```

### Record 5 — example 2 of 3

**form**: `(do (def a (atom 10)) (swap! a + 5) @a)` • **expected**: `15`

**concept_phrase**: `an atom starting at 10, with (swap! a + 5)`

**question_what**: `the value of the atom after swap! + 5`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

The elder of the village kept a small slate at the edge of the orchard, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was an atom starting at 10, with (swap! a + 5). George read
out the form `(do (def a (atom 10)) (swap! a + 5) @a)` so Will could write it
properly into the REPL and earn an honest mark on the slate.

Write a form whose evaluation gives the value of the atom after swap! + 5.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 10)) (swap! a + 5) @a)"}}]}
```

---

## G9-04: Atom CAS semantics

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` • **expected**: `1`

**concept_phrase**: `compare-and-set! on an atom: expected 0, set to 1`

**question_what**: `the value of the atom after a successful CAS`

```
The boy on the hill thought the trick clever the first time he played it.

"Why bother with all this?" Pat demanded near the farm.
"They could just write the new value!" Bob,
saying very little, sketched out compare-and-set! on an atom: expected 0, set to 1 instead and showed the
form `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)`: the proper way for the runtime to manage change.
They agreed to submit it to the REPL.

Write a Clojure expression that computes the value of the atom after a successful CAS.

---

I wrap the def, the update, and the deref together in a do block.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (compare-and-set! a 0 1) @a)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (def a (atom 5)) (compare-and-set! a 0 99) @a)` • **expected**: `5`

**concept_phrase**: `compare-and-set! when the expected value doesn't match (no change)`

**question_what**: `the value of the atom after a CAS that does not fire`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened at the edge of the village.

"Why bother with all this?" Jess demanded near the village.
"She could just write the new value!" George,
stepping deliberately, sketched out compare-and-set! when the expected value doesn't match (no change) instead and showed the
form `(do (def a (atom 5)) (compare-and-set! a 0 99) @a)`: the proper way for the runtime to manage change.
They agreed to submit it to the REPL.

Write a Clojure expression that computes the value of the atom after a CAS that does not fire.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 5)) (compare-and-set! a 0 99) @a)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` • **expected**: `1`

**concept_phrase**: `compare-and-set! on an atom: expected 0, set to 1`

**question_what**: `the value of the atom after a successful CAS`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

"There is no need to evaluate that," Tom said, swaggering through the underbrush.
"Anyone can see what compare-and-set! on an atom: expected 0, set to 1 comes to." Sam, who
near the road had heard such claims many times, asked him to
actually write the form `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` and submit it to the REPL —
just to be sure.

Write a Clojure expression that computes the value of the atom after a successful CAS.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (compare-and-set! a 0 1) @a)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (def a (atom 5)) (compare-and-set! a 0 99) @a)` • **expected**: `5`

**concept_phrase**: `compare-and-set! when the expected value doesn't match (no change)`

**question_what**: `the value of the atom after a CAS that does not fire`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(do (def a (atom 5)) (compare-and-set! a 0 99) @a)`, and the line
above it read compare-and-set! when the expected value doesn't match (no change). Bob handed the page to
Tom, who, her legs heavy from sprinting, agreed to write it out properly.

Write a form whose evaluation gives the value of the atom after a CAS that does not fire.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 5)) (compare-and-set! a 0 99) @a)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` • **expected**: `1`

**concept_phrase**: `compare-and-set! on an atom: expected 0, set to 1`

**question_what**: `the value of the atom after a successful CAS`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place at the edge of the orchard.

Oliver kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the orchard the next entry was
compare-and-set! on an atom: expected 0, set to 1. Lou peered over his shoulder
at the form `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` and was asked, gently, to be the one to
submit it.

What Clojure form computes the value of the atom after a successful CAS? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (compare-and-set! a 0 1) @a)"}}]}
```

---

## G9-05: Watch on atom

**Examples:** 1 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 1

**form**: `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)` • **expected**: `[1]`

**concept_phrase**: `an atom with a watch that appends each new value to a log`

**question_what**: `the contents of the log after one swap`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Halfway through the morning watch, Jess called out
near the hilltop, demanding a verdict on the form `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)` and refusing
to descend until somebody confirmed it. Jess insisted
she already knew the answer. Alice, walking up
at an unhurried pace, simply said: "Submit an atom with a watch that appends each new value to a log to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the contents of the log after one swap.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)"}}]}
```

### Record 2 — example 1 of 1

**form**: `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)` • **expected**: `[1]`

**concept_phrase**: `an atom with a watch that appends each new value to a log`

**question_what**: `the contents of the log after one swap`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

"There is no need to evaluate that," Will said, with a smug grin.
"Anyone can see what an atom with a watch that appends each new value to a log comes to." Alex, who
atop the hilltop had heard such claims many times, asked him to
actually write the form `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)` and submit it to the REPL —
just to be sure.

What Clojure form computes the contents of the log after one swap? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)"}}]}
```

### Record 3 — example 1 of 1

**form**: `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)` • **expected**: `[1]`

**concept_phrase**: `an atom with a watch that appends each new value to a log`

**question_what**: `the contents of the log after one swap`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place at the edge of the orchard.

Grace had been trying to teach Jess how the REPL
works. "Look here," she said, pointing to an atom with a watch that appends each new value to a log.
"You hand the form `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, weary from the morning's effort, agreed to try.

Write a form whose evaluation gives the contents of the log after one swap.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)"}}]}
```

### Record 4 — example 1 of 1

**form**: `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)` • **expected**: `[1]`

**concept_phrase**: `an atom with a watch that appends each new value to a log`

**question_what**: `the contents of the log after one swap`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

The elder of the village kept a small slate atop the hilltop, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was an atom with a watch that appends each new value to a log. Sam read
out the form `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)` so Lou could write it
properly into the REPL and earn an honest mark on the slate.

Question: write a Clojure expression for the contents of the log after one swap.

---

I let the runtime mediate the change before reading the final value.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)"}}]}
```

### Record 5 — example 1 of 1

**form**: `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)` • **expected**: `[1]`

**concept_phrase**: `an atom with a watch that appends each new value to a log`

**question_what**: `the contents of the log after one swap`

```
The boy on the hill thought the trick clever the first time he played it.

A wooden notice nailed to a post at the edge of the farm carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)`. Jess
laughed, boasting at every turn, and declared it too easy to bother with.
Carol said, patiently, that the only way to be certain of
an atom with a watch that appends each new value to a log was to put it in the REPL.

What Clojure form computes the contents of the log after one swap? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)"}}]}
```

---

## G9-06: Validator on atom

**Examples:** 1 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 1

**form**: `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)` • **expected**: `1`

**concept_phrase**: `an atom with a number? validator, incremented once`

**question_what**: `the value of the atom after a valid update`

```
The boy on the hill thought the trick clever the first time he played it.

Frank kept a small ledger of state atop the hilltop — a value that
might change as the day went on, recording how many forms had been
honestly evaluated. He explained that the form
`(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)` captured an atom with a number? validator, incremented once: a careful, ordered update.
Will, swaggering through the underbrush, asked the REPL to confirm the final
value.

Write a Clojure expression that computes the value of the atom after a valid update.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)"}}]}
```

### Record 2 — example 1 of 1

**form**: `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)` • **expected**: `1`

**concept_phrase**: `an atom with a number? validator, incremented once`

**question_what**: `the value of the atom after a valid update`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened in the woods.

Lou called down from a stone near the woods where someone had
chalked an atom with a number? validator, incremented once on a flat board. Lou, swaggering through the underbrush,
declared she already knew what would come back. Sam,
stepping deliberately, asked her to actually submit the form
`(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)` to the REPL — the village had stopped trusting answers
that weren't checked.

Question: write a Clojure expression for the value of the atom after a valid update.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)"}}]}
```

### Record 3 — example 1 of 1

**form**: `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)` • **expected**: `1`

**concept_phrase**: `an atom with a number? validator, incremented once`

**question_what**: `the value of the atom after a valid update`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A wooden notice nailed to a post atop the hilltop carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)`. Jess
laughed, as if the race were already won, and declared it too easy to bother with.
Morgan said, patiently, that the only way to be certain of
an atom with a number? validator, incremented once was to put it in the REPL.

Question: write a Clojure expression for the value of the atom after a valid update.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)"}}]}
```

### Record 4 — example 1 of 1

**form**: `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)` • **expected**: `1`

**concept_phrase**: `an atom with a number? validator, incremented once`

**question_what**: `the value of the atom after a valid update`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Sam kept a small ledger of state at the edge of the hilltop — a value that
might change as the day went on, recording how many forms had been
honestly evaluated. They explained that the form
`(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)` captured an atom with a number? validator, incremented once: a careful, ordered update.
Lou, swaggering through the underbrush, asked the REPL to confirm the final
value.

Write a form whose evaluation gives the value of the atom after a valid update.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)"}}]}
```

### Record 5 — example 1 of 1

**form**: `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)` • **expected**: `1`

**concept_phrase**: `an atom with a number? validator, incremented once`

**question_what**: `the value of the atom after a valid update`

```
Every shepherd in the valley knew the danger of crying wolf for sport. It happened along the road.

A small slate sat on a flat stone near the road; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)`, and the page
heading read an atom with a number? validator, incremented once. George nodded at Will to
write the form properly so the slate would carry an honest entry.

What Clojure form computes the value of the atom after a valid update? Submit it via `eval`.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)"}}]}
```

---

## G9-07: Ref introduction

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do (def r (ref 0)) (dosync (alter r inc)) @r)` • **expected**: `1`

**concept_phrase**: `a ref incremented inside a dosync transaction`

**question_what**: `the value of the ref after dosync alter inc`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A small crowd of villagers had gathered by the woods to watch
Tom attempt to predict, off the cuff, what the REPL would
return. Robin pointed to a ref incremented inside a dosync transaction and read out the
form aloud: `(do (def r (ref 0)) (dosync (alter r inc)) @r)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

What Clojure form computes the value of the ref after dosync alter inc? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 0)) (dosync (alter r inc)) @r)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` • **expected**: `7`

**concept_phrase**: `a ref ref-set to 7 inside dosync`

**question_what**: `the value of the ref after ref-set 7`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place near the meadow.

A wooden notice nailed to a post by the meadow carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (def r (ref 100)) (dosync (ref-set r 7)) @r)`. Jess
laughed, puffed up with pride, and declared it too easy to bother with.
Oliver said, patiently, that the only way to be certain of
a ref ref-set to 7 inside dosync was to put it in the REPL.

Write a Clojure expression that computes the value of the ref after ref-set 7.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 100)) (dosync (ref-set r 7)) @r)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (def r (ref 0)) (dosync (alter r inc)) @r)` • **expected**: `1`

**concept_phrase**: `a ref incremented inside a dosync transaction`

**question_what**: `the value of the ref after dosync alter inc`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place on the hilltop.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(do (def r (ref 0)) (dosync (alter r inc)) @r)`, and the line
above it read a ref incremented inside a dosync transaction. Oliver handed the page to
Will, who, her legs heavy from sprinting, agreed to write it out properly.

What Clojure form computes the value of the ref after dosync alter inc? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 0)) (dosync (alter r inc)) @r)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` • **expected**: `7`

**concept_phrase**: `a ref ref-set to 7 inside dosync`

**question_what**: `the value of the ref after ref-set 7`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Halfway through the morning watch, Tom called out
in the orchard, demanding a verdict on the form `(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` and refusing
to descend until somebody confirmed it. Tom insisted
he already knew the answer. Alex, walking up
at an unhurried pace, simply said: "Submit a ref ref-set to 7 inside dosync to the
REPL. Whatever comes back is the answer."

Write a Clojure expression that computes the value of the ref after ref-set 7.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 100)) (dosync (ref-set r 7)) @r)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (def r (ref 0)) (dosync (alter r inc)) @r)` • **expected**: `1`

**concept_phrase**: `a ref incremented inside a dosync transaction`

**question_what**: `the value of the ref after dosync alter inc`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A small slate sat on a flat stone near the farm; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(do (def r (ref 0)) (dosync (alter r inc)) @r)`, and the page
heading read a ref incremented inside a dosync transaction. George nodded at Jess to
write the form properly so the slate would carry an honest entry.

What Clojure form computes the value of the ref after dosync alter inc? Submit it via `eval`.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 0)) (dosync (alter r inc)) @r)"}}]}
```

---

## G9-08: dosync and alter

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])` • **expected**: `[2, 3]`

**concept_phrase**: `two refs each incremented inside a single dosync`

**question_what**: `the pair [a b] after the coordinated transaction`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened near the orchard.

Oliver kept a small ledger of state in the orchard — a value that
might change as the day went on, recording how many forms had been
honestly evaluated. He explained that the form
`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])` captured two refs each incremented inside a single dosync: a careful, ordered update.
Tom, with a smug grin, asked the REPL to confirm the final
value.

Write a form whose evaluation gives the pair [a b] after the coordinated transaction.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (def r (ref 10)) (dosync (alter r + 5)) @r)` • **expected**: `15`

**concept_phrase**: `a ref altered by + 5 inside dosync`

**question_what**: `the value of the ref after alter + 5`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened by the orchard.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(do (def r (ref 10)) (dosync (alter r + 5)) @r)`, and the line
above it read a ref altered by + 5 inside dosync. Alex handed the page to
Pat, who, lulled by the gentle wind, agreed to write it out properly.

Write a Clojure expression that computes the value of the ref after alter + 5.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 10)) (dosync (alter r + 5)) @r)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])` • **expected**: `[2, 3]`

**concept_phrase**: `two refs each incremented inside a single dosync`

**question_what**: `the pair [a b] after the coordinated transaction`

```
The boy on the hill thought the trick clever the first time he played it. It happened at the edge of the farm.

A wooden notice nailed to a post near the farm carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])`. Will
laughed, as if the race were already won, and declared it too easy to bother with.
Grace said, patiently, that the only way to be certain of
two refs each incremented inside a single dosync was to put it in the REPL.

Write a Clojure expression that computes the pair [a b] after the coordinated transaction.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (def r (ref 10)) (dosync (alter r + 5)) @r)` • **expected**: `15`

**concept_phrase**: `a ref altered by + 5 inside dosync`

**question_what**: `the value of the ref after alter + 5`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place in the meadow.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(do (def r (ref 10)) (dosync (alter r + 5)) @r)`, and the line
above it read a ref altered by + 5 inside dosync. Sam handed the page to
Tom, who, her legs heavy from sprinting, agreed to write it out properly.

Write a Clojure expression that computes the value of the ref after alter + 5.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 10)) (dosync (alter r + 5)) @r)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])` • **expected**: `[2, 3]`

**concept_phrase**: `two refs each incremented inside a single dosync`

**question_what**: `the pair [a b] after the coordinated transaction`

```
The boy on the hill thought the trick clever the first time he played it.

"There is no need to evaluate that," Pat said, with great whoops of laughter.
"Anyone can see what two refs each incremented inside a single dosync comes to." Oliver, who
by the orchard had heard such claims many times, asked them to
actually write the form `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])` and submit it to the REPL —
just to be sure.

Write a Clojure expression that computes the pair [a b] after the coordinated transaction.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])"}}]}
```

---

## G9-09: Ref vs atom

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do (def a (atom 0)) (swap! a inc) @a)` • **expected**: `1`

**concept_phrase**: `an atom updated via swap!`

**question_what**: `the value of the atom after one swap! inc`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place in the woods.

Halfway through the morning watch, Will called out
at the edge of the woods, demanding a verdict on the form `(do (def a (atom 0)) (swap! a inc) @a)` and refusing
to descend until somebody confirmed it. Will insisted
he already knew the answer. George, walking up
at an unhurried pace, simply said: "Submit an atom updated via swap! to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the value of the atom after one swap! inc.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (def r (ref 0)) (dosync (alter r inc)) @r)` • **expected**: `1`

**concept_phrase**: `a ref updated via alter inside dosync`

**question_what**: `the value of the ref after one dosync alter inc`

```
The boy on the hill thought the trick clever the first time he played it.

"There is no need to evaluate that," Pat said, swaggering through the underbrush.
"Anyone can see what a ref updated via alter inside dosync comes to." Alice, who
by the forest had heard such claims many times, asked them to
actually write the form `(do (def r (ref 0)) (dosync (alter r inc)) @r)` and submit it to the REPL —
just to be sure.

Write a form whose evaluation gives the value of the ref after one dosync alter inc.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 0)) (dosync (alter r inc)) @r)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (def a (atom 0)) (swap! a inc) @a)` • **expected**: `1`

**concept_phrase**: `an atom updated via swap!`

**question_what**: `the value of the atom after one swap! inc`

```
The boy on the hill thought the trick clever the first time he played it.

"Why bother with all this?" Jess demanded in the orchard.
"She could just write the new value!" Morgan,
her eyes always on the path, sketched out an atom updated via swap! instead and showed the
form `(do (def a (atom 0)) (swap! a inc) @a)`: the proper way for the runtime to manage change.
They agreed to submit it to the REPL.

Write a Clojure expression that computes the value of the atom after one swap! inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (def r (ref 0)) (dosync (alter r inc)) @r)` • **expected**: `1`

**concept_phrase**: `a ref updated via alter inside dosync`

**question_what**: `the value of the ref after one dosync alter inc`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Halfway through the morning watch, Pat called out
at the edge of the woods, demanding a verdict on the form `(do (def r (ref 0)) (dosync (alter r inc)) @r)` and refusing
to descend until somebody confirmed it. Pat insisted
they already knew the answer. Carol, walking up
at an unhurried pace, simply said: "Submit a ref updated via alter inside dosync to the
REPL. Whatever comes back is the answer."

Write a form whose evaluation gives the value of the ref after one dosync alter inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 0)) (dosync (alter r inc)) @r)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (def a (atom 0)) (swap! a inc) @a)` • **expected**: `1`

**concept_phrase**: `an atom updated via swap!`

**question_what**: `the value of the atom after one swap! inc`

```
The boy on the hill thought the trick clever the first time he played it.

A small crowd of villagers had gathered by the woods to watch
Tom attempt to predict, off the cuff, what the REPL would
return. George pointed to an atom updated via swap! and read out the
form aloud: `(do (def a (atom 0)) (swap! a inc) @a)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Question: write a Clojure expression for the value of the atom after one swap! inc.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
```

---

## G9-10: Agent introduction

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)` • **expected**: `1`

**concept_phrase**: `an agent sent inc and awaited`

**question_what**: `the value of the agent after send inc and await`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Lou called down from a stone atop the hilltop where someone had
chalked an agent sent inc and awaited on a flat board. Lou, boasting at every turn,
declared she already knew what would come back. Grace,
with steady, careful steps, asked her to actually submit the form
`(do (def ag (agent 0)) (send ag inc) (await ag) @ag)` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the value of the agent after send inc and await.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (def ag (agent 5)) (send ag + 10) (await ag) @ag)` • **expected**: `15`

**concept_phrase**: `an agent sent (+ 10) and awaited`

**question_what**: `the value of the agent after send + 10 and await`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. This was near the orchard.

"There is no need to evaluate that," Pat said, with a smug grin.
"Anyone can see what an agent sent (+ 10) and awaited comes to." Carol, who
near the orchard had heard such claims many times, asked them to
actually write the form `(do (def ag (agent 5)) (send ag + 10) (await ag) @ag)` and submit it to the REPL —
just to be sure.

Question: write a Clojure expression for the value of the agent after send + 10 and await.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 5)) (send ag + 10) (await ag) @ag)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)` • **expected**: `1`

**concept_phrase**: `an agent sent inc and awaited`

**question_what**: `the value of the agent after send inc and await`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Alice had been trying to teach Tom how the REPL
works. "Look here," she said, pointing to an agent sent inc and awaited.
"You hand the form `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Tom, drowsy from the warm sun, agreed to try.

What Clojure form computes the value of the agent after send inc and await? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (def ag (agent 5)) (send ag + 10) (await ag) @ag)` • **expected**: `15`

**concept_phrase**: `an agent sent (+ 10) and awaited`

**question_what**: `the value of the agent after send + 10 and await`

```
The boy on the hill thought the trick clever the first time he played it. This was along the road.

"Why bother with all this?" Tom demanded along the road.
"He could just write the new value!" Alice,
without complaint, sketched out an agent sent (+ 10) and awaited instead and showed the
form `(do (def ag (agent 5)) (send ag + 10) (await ag) @ag)`: the proper way for the runtime to manage change.
They agreed to submit it to the REPL.

Question: write a Clojure expression for the value of the agent after send + 10 and await.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 5)) (send ag + 10) (await ag) @ag)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)` • **expected**: `1`

**concept_phrase**: `an agent sent inc and awaited`

**question_what**: `the value of the agent after send inc and await`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

"Why bother with all this?" Tom demanded by the farm.
"He could just write the new value!" Robin,
untroubled by what others thought, sketched out an agent sent inc and awaited instead and showed the
form `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`: the proper way for the runtime to manage change.
They agreed to submit it to the REPL.

Write a form whose evaluation gives the value of the agent after send inc and await.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

---

## G9-11: send and send-off

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)` • **expected**: `1`

**concept_phrase**: `send used on an agent, then awaited`

**question_what**: `the agent's value after send inc`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened in the meadow.

Halfway through the morning watch, Will called out
in the meadow, demanding a verdict on the form `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)` and refusing
to descend until somebody confirmed it. Will insisted
he already knew the answer. Bob, walking up
at an unhurried pace, simply said: "Submit send used on an agent, then awaited to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the agent's value after send inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (def ag (agent 0)) (send-off ag inc) (await ag) @ag)` • **expected**: `1`

**concept_phrase**: `send-off used on an agent, then awaited`

**question_what**: `the agent's value after send-off inc`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place near the road.

A small slate sat on a flat stone near the road; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(do (def ag (agent 0)) (send-off ag inc) (await ag) @ag)`, and the page
heading read send-off used on an agent, then awaited. Sam nodded at Jess to
write the form properly so the slate would carry an honest entry.

Write a Clojure expression that computes the agent's value after send-off inc.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send-off ag inc) (await ag) @ag)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)` • **expected**: `1`

**concept_phrase**: `send used on an agent, then awaited`

**question_what**: `the agent's value after send inc`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A wooden notice nailed to a post in the village carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`. Will
laughed, with great whoops of laughter, and declared it too easy to bother with.
Alex said, patiently, that the only way to be certain of
send used on an agent, then awaited was to put it in the REPL.

Write a Clojure expression that computes the agent's value after send inc.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (def ag (agent 0)) (send-off ag inc) (await ag) @ag)` • **expected**: `1`

**concept_phrase**: `send-off used on an agent, then awaited`

**question_what**: `the agent's value after send-off inc`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. This was on the road.

"There is no need to evaluate that," Lou said, with great whoops of laughter.
"Anyone can see what send-off used on an agent, then awaited comes to." George, who
on the road had heard such claims many times, asked her to
actually write the form `(do (def ag (agent 0)) (send-off ag inc) (await ag) @ag)` and submit it to the REPL —
just to be sure.

What Clojure form computes the agent's value after send-off inc? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send-off ag inc) (await ag) @ag)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)` • **expected**: `1`

**concept_phrase**: `send used on an agent, then awaited`

**question_what**: `the agent's value after send inc`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place by the orchard.

A small crowd of villagers had gathered near the orchard to watch
Lou attempt to predict, off the cuff, what the REPL would
return. Carol pointed to send used on an agent, then awaited and read out the
form aloud: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a form whose evaluation gives the agent's value after send inc.

---

I bind the state, perform the update, then dereference.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

---

## G9-12: await — synchronizing on agents

**Examples:** 1 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 1

**form**: `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)` • **expected**: `2`

**concept_phrase**: `two send inc calls then await before deref`

**question_what**: `the agent's value after two sends and await`

```
The boy on the hill thought the trick clever the first time he played it. This was near the orchard.

Grace kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the orchard the next entry was
two send inc calls then await before deref. Jess peered over her shoulder
at the form `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)` and was asked, gently, to be the one to
submit it.

Write a Clojure expression that computes the agent's value after two sends and await.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)"}}]}
```

### Record 2 — example 1 of 1

**form**: `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)` • **expected**: `2`

**concept_phrase**: `two send inc calls then await before deref`

**question_what**: `the agent's value after two sends and await`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

"There is no need to evaluate that," Pat said, swaggering through the underbrush.
"Anyone can see what two send inc calls then await before deref comes to." Alex, who
along the road had heard such claims many times, asked them to
actually write the form `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)` and submit it to the REPL —
just to be sure.

Question: write a Clojure expression for the agent's value after two sends and await.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)"}}]}
```

### Record 3 — example 1 of 1

**form**: `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)` • **expected**: `2`

**concept_phrase**: `two send inc calls then await before deref`

**question_what**: `the agent's value after two sends and await`

```
The boy on the hill thought the trick clever the first time he played it. It happened along the road.

The elder of the village kept a small slate near the road, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was two send inc calls then await before deref. George read
out the form `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)` so Tom could write it
properly into the REPL and earn an honest mark on the slate.

What Clojure form computes the agent's value after two sends and await? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)"}}]}
```

### Record 4 — example 1 of 1

**form**: `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)` • **expected**: `2`

**concept_phrase**: `two send inc calls then await before deref`

**question_what**: `the agent's value after two sends and await`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened at the edge of the orchard.

Lou called down from a stone at the edge of the orchard where someone had
chalked two send inc calls then await before deref on a flat board. Lou, puffed up with pride,
declared she already knew what would come back. Morgan,
saying very little, asked her to actually submit the form
`(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)` to the REPL — the village had stopped trusting answers
that weren't checked.

Question: write a Clojure expression for the agent's value after two sends and await.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)"}}]}
```

### Record 5 — example 1 of 1

**form**: `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)` • **expected**: `2`

**concept_phrase**: `two send inc calls then await before deref`

**question_what**: `the agent's value after two sends and await`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

"Why bother with all this?" Tom demanded in the farm.
"He could just write the new value!" Oliver,
stepping deliberately, sketched out two send inc calls then await before deref instead and showed the
form `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)`: the proper way for the runtime to manage change.
They agreed to submit it to the REPL.

What Clojure form computes the agent's value after two sends and await? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)"}}]}
```

---

## G9-13: future introduction

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `@(future (+ 1 2))` • **expected**: `3`

**concept_phrase**: `a future computing (+ 1 2), dereferenced`

**question_what**: `the value of the future for (+ 1 2)`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden notice nailed to a post at the edge of the woods carried a small puzzle. The
riddle simply asked the reader to evaluate `@(future (+ 1 2))`. Pat
laughed, with great whoops of laughter, and declared it too easy to bother with.
Sam said, patiently, that the only way to be certain of
a future computing (+ 1 2), dereferenced was to put it in the REPL.

Write a Clojure expression that computes the value of the future for (+ 1 2).

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"@(future (+ 1 2))"}}]}
```

### Record 2 — example 2 of 2

**form**: `@(future (* 6 7))` • **expected**: `42`

**concept_phrase**: `a future computing (* 6 7), dereferenced`

**question_what**: `the value of the future for (* 6 7)`

```
The boy on the hill thought the trick clever the first time he played it.

George kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today in the forest the next entry was
a future computing (* 6 7), dereferenced. Jess peered over his shoulder
at the form `@(future (* 6 7))` and was asked, gently, to be the one to
submit it.

Write a Clojure expression that computes the value of the future for (* 6 7).

---

{"tool_calls":[{"name":"eval","args":{"form":"@(future (* 6 7))"}}]}
```

### Record 3 — example 1 of 2

**form**: `@(future (+ 1 2))` • **expected**: `3`

**concept_phrase**: `a future computing (+ 1 2), dereferenced`

**question_what**: `the value of the future for (+ 1 2)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened at the edge of the farm.

Bob had been trying to teach Tom how the REPL
works. "Look here," he said, pointing to a future computing (+ 1 2), dereferenced.
"You hand the form `@(future (+ 1 2))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Tom, drowsy from the warm sun, agreed to try.

What Clojure form computes the value of the future for (+ 1 2)? Submit it via `eval`.

---

I let the runtime mediate the change before reading the final value.

{"tool_calls":[{"name":"eval","args":{"form":"@(future (+ 1 2))"}}]}
```

### Record 4 — example 2 of 2

**form**: `@(future (* 6 7))` • **expected**: `42`

**concept_phrase**: `a future computing (* 6 7), dereferenced`

**question_what**: `the value of the future for (* 6 7)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. This was at the edge of the forest.

Lou called down from a stone near the forest where someone had
chalked a future computing (* 6 7), dereferenced on a flat board. Lou, with a smug grin,
declared she already knew what would come back. Morgan,
stepping deliberately, asked her to actually submit the form
`@(future (* 6 7))` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the value of the future for (* 6 7).

---

{"tool_calls":[{"name":"eval","args":{"form":"@(future (* 6 7))"}}]}
```

### Record 5 — example 1 of 2

**form**: `@(future (+ 1 2))` • **expected**: `3`

**concept_phrase**: `a future computing (+ 1 2), dereferenced`

**question_what**: `the value of the future for (+ 1 2)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Lou called down from a stone near the woods where someone had
chalked a future computing (+ 1 2), dereferenced on a flat board. Lou, boasting at every turn,
declared she already knew what would come back. Alex,
stepping deliberately, asked her to actually submit the form
`@(future (+ 1 2))` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the value of the future for (+ 1 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"@(future (+ 1 2))"}}]}
```

---

## G9-14: deref @ shorthand

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do (def a (atom 7)) @a)` • **expected**: `7`

**concept_phrase**: `deref via @ on an atom holding 7`

**question_what**: `the value of the atom via @`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Carol had been trying to teach Jess how the REPL
works. "Look here," she said, pointing to deref via @ on an atom holding 7.
"You hand the form `(do (def a (atom 7)) @a)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, lulled by the gentle wind, agreed to try.

Question: write a Clojure expression for the value of the atom via @.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 7)) @a)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (def a (atom 7)) (deref a))` • **expected**: `7`

**concept_phrase**: `deref via the function form on an atom`

**question_what**: `the value of the atom via the deref function`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. This was along the road.

A wooden notice nailed to a post along the road carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (def a (atom 7)) (deref a))`. Pat
laughed, with a smug grin, and declared it too easy to bother with.
Grace said, patiently, that the only way to be certain of
deref via the function form on an atom was to put it in the REPL.

Question: write a Clojure expression for the value of the atom via the deref function.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 7)) (deref a))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (def a (atom 7)) @a)` • **expected**: `7`

**concept_phrase**: `deref via @ on an atom holding 7`

**question_what**: `the value of the atom via @`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Morgan had been trying to teach Will how the REPL
works. "Look here," they said, pointing to deref via @ on an atom holding 7.
"You hand the form `(do (def a (atom 7)) @a)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Will, yawning at the soft moss, agreed to try.

Question: write a Clojure expression for the value of the atom via @.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 7)) @a)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (def a (atom 7)) (deref a))` • **expected**: `7`

**concept_phrase**: `deref via the function form on an atom`

**question_what**: `the value of the atom via the deref function`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

"There is no need to evaluate that," Tom said, with a smug grin.
"Anyone can see what deref via the function form on an atom comes to." Alice, who
at the edge of the farm had heard such claims many times, asked him to
actually write the form `(do (def a (atom 7)) (deref a))` and submit it to the REPL —
just to be sure.

Write a Clojure expression that computes the value of the atom via the deref function.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 7)) (deref a))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (def a (atom 7)) @a)` • **expected**: `7`

**concept_phrase**: `deref via @ on an atom holding 7`

**question_what**: `the value of the atom via @`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Halfway through the morning watch, Jess called out
near the woods, demanding a verdict on the form `(do (def a (atom 7)) @a)` and refusing
to descend until somebody confirmed it. Jess insisted
she already knew the answer. Grace, walking up
at an unhurried pace, simply said: "Submit deref via @ on an atom holding 7 to the
REPL. Whatever comes back is the answer."

What Clojure form computes the value of the atom via @? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 7)) @a)"}}]}
```

---

## G9-15: promise — deliver and deref

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do (def p (promise)) (deliver p :done) @p)` • **expected**: `':done'`

**concept_phrase**: `a promise delivered with :done, then dereffed`

**question_what**: `the value of the promise after deliver`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Grace kept a small ledger of state near the meadow — a value that
might change as the day went on, recording how many forms had been
honestly evaluated. She explained that the form
`(do (def p (promise)) (deliver p :done) @p)` captured a promise delivered with :done, then dereffed: a careful, ordered update.
Lou, with great whoops of laughter, asked the REPL to confirm the final
value.

What Clojure form computes the value of the promise after deliver? Submit it via `eval`.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def p (promise)) (deliver p :done) @p)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (def p (promise)) (deliver p 42) @p)` • **expected**: `42`

**concept_phrase**: `a promise delivered with 42`

**question_what**: `the value of the promise after deliver 42`

```
Every shepherd in the valley knew the danger of crying wolf for sport. This was near the hilltop.

Tom called down from a stone atop the hilltop where someone had
chalked a promise delivered with 42 on a flat board. Tom, as if the race were already won,
declared he already knew what would come back. Alex,
untroubled by what others thought, asked him to actually submit the form
`(do (def p (promise)) (deliver p 42) @p)` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the value of the promise after deliver 42.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def p (promise)) (deliver p 42) @p)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (def p (promise)) (deliver p :done) @p)` • **expected**: `':done'`

**concept_phrase**: `a promise delivered with :done, then dereffed`

**question_what**: `the value of the promise after deliver`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A wooden notice nailed to a post near the orchard carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (def p (promise)) (deliver p :done) @p)`. Lou
laughed, boasting at every turn, and declared it too easy to bother with.
George said, patiently, that the only way to be certain of
a promise delivered with :done, then dereffed was to put it in the REPL.

Write a Clojure expression that computes the value of the promise after deliver.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def p (promise)) (deliver p :done) @p)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (def p (promise)) (deliver p 42) @p)` • **expected**: `42`

**concept_phrase**: `a promise delivered with 42`

**question_what**: `the value of the promise after deliver 42`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A wooden notice nailed to a post near the meadow carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (def p (promise)) (deliver p 42) @p)`. Will
laughed, swaggering through the underbrush, and declared it too easy to bother with.
Frank said, patiently, that the only way to be certain of
a promise delivered with 42 was to put it in the REPL.

Question: write a Clojure expression for the value of the promise after deliver 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def p (promise)) (deliver p 42) @p)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (def p (promise)) (deliver p :done) @p)` • **expected**: `':done'`

**concept_phrase**: `a promise delivered with :done, then dereffed`

**question_what**: `the value of the promise after deliver`

```
The boy on the hill thought the trick clever the first time he played it. All this took place in the village.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(do (def p (promise)) (deliver p :done) @p)`, and the line
above it read a promise delivered with :done, then dereffed. Carol handed the page to
Jess, who, her legs heavy from sprinting, agreed to write it out properly.

Write a Clojure expression that computes the value of the promise after deliver.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def p (promise)) (deliver p :done) @p)"}}]}
```

---

## G9-16: volatile — when STM is too heavy

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do (def v (volatile! 0)) (vswap! v inc) @v)` • **expected**: `1`

**concept_phrase**: `a volatile! incremented via vswap!`

**question_what**: `the value of the volatile after one vswap! inc`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Halfway through the morning watch, Pat called out
by the orchard, demanding a verdict on the form `(do (def v (volatile! 0)) (vswap! v inc) @v)` and refusing
to descend until somebody confirmed it. Pat insisted
they already knew the answer. Sam, walking up
at an unhurried pace, simply said: "Submit a volatile! incremented via vswap! to the
REPL. Whatever comes back is the answer."

Write a form whose evaluation gives the value of the volatile after one vswap! inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def v (volatile! 0)) (vswap! v inc) @v)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (def v (volatile! 5)) (vreset! v 99) @v)` • **expected**: `99`

**concept_phrase**: `a volatile! reset via vreset!`

**question_what**: `the value of the volatile after vreset! 99`

```
The boy on the hill thought the trick clever the first time he played it. All this took place near the village.

"There is no need to evaluate that," Tom said, swaggering through the underbrush.
"Anyone can see what a volatile! reset via vreset! comes to." Alice, who
at the edge of the village had heard such claims many times, asked him to
actually write the form `(do (def v (volatile! 5)) (vreset! v 99) @v)` and submit it to the REPL —
just to be sure.

What Clojure form computes the value of the volatile after vreset! 99? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def v (volatile! 5)) (vreset! v 99) @v)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (def v (volatile! 0)) (vswap! v inc) @v)` • **expected**: `1`

**concept_phrase**: `a volatile! incremented via vswap!`

**question_what**: `the value of the volatile after one vswap! inc`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A wooden notice nailed to a post in the farm carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (def v (volatile! 0)) (vswap! v inc) @v)`. Pat
laughed, puffed up with pride, and declared it too easy to bother with.
Bob said, patiently, that the only way to be certain of
a volatile! incremented via vswap! was to put it in the REPL.

Question: write a Clojure expression for the value of the volatile after one vswap! inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def v (volatile! 0)) (vswap! v inc) @v)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (def v (volatile! 5)) (vreset! v 99) @v)` • **expected**: `99`

**concept_phrase**: `a volatile! reset via vreset!`

**question_what**: `the value of the volatile after vreset! 99`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Frank kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the farm the next entry was
a volatile! reset via vreset!. Will peered over his shoulder
at the form `(do (def v (volatile! 5)) (vreset! v 99) @v)` and was asked, gently, to be the one to
submit it.

Question: write a Clojure expression for the value of the volatile after vreset! 99.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def v (volatile! 5)) (vreset! v 99) @v)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (def v (volatile! 0)) (vswap! v inc) @v)` • **expected**: `1`

**concept_phrase**: `a volatile! incremented via vswap!`

**question_what**: `the value of the volatile after one vswap! inc`

```
The boy on the hill thought the trick clever the first time he played it. This was by the orchard.

Frank kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today at the edge of the orchard the next entry was
a volatile! incremented via vswap!. Pat peered over his shoulder
at the form `(do (def v (volatile! 0)) (vswap! v inc) @v)` and was asked, gently, to be the one to
submit it.

Write a form whose evaluation gives the value of the volatile after one vswap! inc.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def v (volatile! 0)) (vswap! v inc) @v)"}}]}
```

---

## G9-17: binding — thread-local

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` • **expected**: `99`

**concept_phrase**: `a dynamic var *p* rebound to 99 inside binding`

**question_what**: `the value of *p* inside the binding form`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place by the forest.

"There is no need to evaluate that," Will said, with a smug grin.
"Anyone can see what a dynamic var *p* rebound to 99 inside binding comes to." Grace, who
in the forest had heard such claims many times, asked him to
actually write the form `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` and submit it to the REPL —
just to be sure.

Question: write a Clojure expression for the value of *p* inside the binding form.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)` • **expected**: `1`

**concept_phrase**: `the value of *p* AFTER the binding form exits`

**question_what**: `the original value of *p* once binding has unwound`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place by the forest.

Halfway through the morning watch, Tom called out
by the forest, demanding a verdict on the form `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)` and refusing
to descend until somebody confirmed it. Tom insisted
he already knew the answer. George, walking up
at an unhurried pace, simply said: "Submit the value of *p* AFTER the binding form exits to the
REPL. Whatever comes back is the answer."

Write a form whose evaluation gives the original value of *p* once binding has unwound.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` • **expected**: `99`

**concept_phrase**: `a dynamic var *p* rebound to 99 inside binding`

**question_what**: `the value of *p* inside the binding form`

```
The boy on the hill thought the trick clever the first time he played it.

The elder of the village kept a small slate at the edge of the meadow, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was a dynamic var *p* rebound to 99 inside binding. Carol read
out the form `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` so Tom could write it
properly into the REPL and earn an honest mark on the slate.

Question: write a Clojure expression for the value of *p* inside the binding form.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)` • **expected**: `1`

**concept_phrase**: `the value of *p* AFTER the binding form exits`

**question_what**: `the original value of *p* once binding has unwound`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

"Why bother with all this?" Will demanded near the forest.
"He could just write the new value!" Alex,
untroubled by what others thought, sketched out the value of *p* AFTER the binding form exits instead and showed the
form `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)`: the proper way for the runtime to manage change.
They agreed to submit it to the REPL.

Write a form whose evaluation gives the original value of *p* once binding has unwound.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` • **expected**: `99`

**concept_phrase**: `a dynamic var *p* rebound to 99 inside binding`

**question_what**: `the value of *p* inside the binding form`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden notice nailed to a post by the woods carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))`. Pat
laughed, swaggering through the underbrush, and declared it too easy to bother with.
Morgan said, patiently, that the only way to be certain of
a dynamic var *p* rebound to 99 inside binding was to put it in the REPL.

Write a Clojure expression that computes the value of *p* inside the binding form.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))"}}]}
```

---

## G9-18: locking — last resort

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do (def lock (Object.)) (locking lock (+ 1 2)))` • **expected**: `3`

**concept_phrase**: `a locking form around (+ 1 2) using a fresh Object as monitor`

**question_what**: `the result of the body inside locking`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A small crowd of villagers had gathered near the meadow to watch
Pat attempt to predict, off the cuff, what the REPL would
return. Alice pointed to a locking form around (+ 1 2) using a fresh Object as monitor and read out the
form aloud: `(do (def lock (Object.)) (locking lock (+ 1 2)))`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a Clojure expression that computes the result of the body inside locking.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def lock (Object.)) (locking lock (+ 1 2)))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (def lock (Object.)) (locking lock 42))` • **expected**: `42`

**concept_phrase**: `a locking form whose body is just the literal 42`

**question_what**: `the value the locking form returns`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Robin had been trying to teach Jess how the REPL
works. "Look here," they said, pointing to a locking form whose body is just the literal 42.
"You hand the form `(do (def lock (Object.)) (locking lock 42))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, weary from the morning's effort, agreed to try.

Write a Clojure expression that computes the value the locking form returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def lock (Object.)) (locking lock 42))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (def lock (Object.)) (locking lock (+ 1 2)))` • **expected**: `3`

**concept_phrase**: `a locking form around (+ 1 2) using a fresh Object as monitor`

**question_what**: `the result of the body inside locking`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Sam kept a small ledger of state near the road — a value that
might change as the day went on, recording how many forms had been
honestly evaluated. They explained that the form
`(do (def lock (Object.)) (locking lock (+ 1 2)))` captured a locking form around (+ 1 2) using a fresh Object as monitor: a careful, ordered update.
Lou, puffed up with pride, asked the REPL to confirm the final
value.

Write a form whose evaluation gives the result of the body inside locking.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def lock (Object.)) (locking lock (+ 1 2)))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (def lock (Object.)) (locking lock 42))` • **expected**: `42`

**concept_phrase**: `a locking form whose body is just the literal 42`

**question_what**: `the value the locking form returns`

```
The boy on the hill thought the trick clever the first time he played it. All this took place near the meadow.

A small crowd of villagers had gathered near the meadow to watch
Will attempt to predict, off the cuff, what the REPL would
return. Oliver pointed to a locking form whose body is just the literal 42 and read out the
form aloud: `(do (def lock (Object.)) (locking lock 42))`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a form whose evaluation gives the value the locking form returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def lock (Object.)) (locking lock 42))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (def lock (Object.)) (locking lock (+ 1 2)))` • **expected**: `3`

**concept_phrase**: `a locking form around (+ 1 2) using a fresh Object as monitor`

**question_what**: `the result of the body inside locking`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A wooden notice nailed to a post by the village carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (def lock (Object.)) (locking lock (+ 1 2)))`. Lou
laughed, with great whoops of laughter, and declared it too easy to bother with.
Sam said, patiently, that the only way to be certain of
a locking form around (+ 1 2) using a fresh Object as monitor was to put it in the REPL.

Write a Clojure expression that computes the result of the body inside locking.

---

I wrap the def, the update, and the deref together in a do block.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def lock (Object.)) (locking lock (+ 1 2)))"}}]}
```

---

