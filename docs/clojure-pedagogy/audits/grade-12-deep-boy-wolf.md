# Boy-wolf Grade 12 — deep spot-check

5 generated records per subject (across all examples and a variety of seeds). Read every record carefully. Flag anything that reads odd to a careful reader, including issues the structural audit can't catch (prose flow, contextual fit, cliché repetition, subplot/example mismatch, etc.)

---

## G12-01: Transducers introduction

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(into [] (map inc) [1 2 3])` • **expected**: `[2, 3, 4]`

**concept_phrase**: `the transducer (map inc) used via into`

**question_what**: `[1 2 3] each incremented through a transducer`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

At the village square near the woods, a row of small markers commemorated
the libraries the careful shepherds had learned over the season. The
newest one honoured the transducer (map inc) used via into. Alice touched it and
said the form to remember was `(into [] (map inc) [1 2 3])`; Pat
agreed to submit it.

Write a Clojure expression that computes [1 2 3] each incremented through a transducer.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
```

### Record 2 — example 2 of 2

**form**: `(into [] (filter even?) [1 2 3 4 5])` • **expected**: `[2, 4]`

**concept_phrase**: `the transducer (filter even?) used via into`

**question_what**: `the even elements via a filter transducer`

```
The boy on the hill thought the trick clever the first time he played it.

The elder of the village kept a small slate in the village, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the transducer (filter even?) used via into. Sam read
out the form `(into [] (filter even?) [1 2 3 4 5])` so Lou could write it
properly into the REPL and earn an honest mark on the slate.

Write a Clojure expression that computes the even elements via a filter transducer.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (filter even?) [1 2 3 4 5])"}}]}
```

### Record 3 — example 1 of 2

**form**: `(into [] (map inc) [1 2 3])` • **expected**: `[2, 3, 4]`

**concept_phrase**: `the transducer (map inc) used via into`

**question_what**: `[1 2 3] each incremented through a transducer`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Frank had been trying to teach Pat how the REPL
works. "Look here," he said, pointing to the transducer (map inc) used via into.
"You hand the form `(into [] (map inc) [1 2 3])` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Pat, drowsy from the warm sun, agreed to try.

Write a Clojure expression that computes [1 2 3] each incremented through a transducer.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
```

### Record 4 — example 2 of 2

**form**: `(into [] (filter even?) [1 2 3 4 5])` • **expected**: `[2, 4]`

**concept_phrase**: `the transducer (filter even?) used via into`

**question_what**: `the even elements via a filter transducer`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

"This isn't a clever guess," Oliver said by the orchard, with steady, careful steps.
"It's a tool." Pat looked at the transducer (filter even?) used via into and
admitted they would not have known what to write.
Oliver sketched `(into [] (filter even?) [1 2 3 4 5])` on a slate so the runtime could speak
for itself.

What Clojure form computes the even elements via a filter transducer? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (filter even?) [1 2 3 4 5])"}}]}
```

### Record 5 — example 1 of 2

**form**: `(into [] (map inc) [1 2 3])` • **expected**: `[2, 3, 4]`

**concept_phrase**: `the transducer (map inc) used via into`

**question_what**: `[1 2 3] each incremented through a transducer`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Lou called down from a stone on the road where someone had
chalked the transducer (map inc) used via into on a flat board. Lou, with great whoops of laughter,
declared she already knew what would come back. Alex,
stepping deliberately, asked her to actually submit the form
`(into [] (map inc) [1 2 3])` to the REPL — the village had stopped trusting answers
that weren't checked.

What Clojure form computes [1 2 3] each incremented through a transducer? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
```

---

## G12-02: Transducer composition

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(into [] (comp (map inc) (filter even?)) [1 2 3 4])` • **expected**: `[2, 4]`

**concept_phrase**: `the composed transducer (comp (map inc) (filter even?))`

**question_what**: `the result of inc-then-keep-evens via a composed transducer`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Will called down from a stone by the orchard where someone had
chalked the composed transducer (comp (map inc) (filter even?)) on a flat board. Will, with a smug grin,
declared he already knew what would come back. Morgan,
stepping deliberately, asked him to actually submit the form
`(into [] (comp (map inc) (filter even?)) [1 2 3 4])` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a form whose evaluation gives the result of inc-then-keep-evens via a composed transducer.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (comp (map inc) (filter even?)) [1 2 3 4])"}}]}
```

### Record 2 — example 2 of 2

**form**: `(transduce (comp (map inc) (filter even?)) + 0 [1 2 3 4 5])` • **expected**: `12`

**concept_phrase**: `transduce with a composed transducer summing the kept items`

**question_what**: `the sum after inc-then-keep-evens via transduce`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place by the woods.

A harvest gathering at the end of the season at the edge of the woods brought together
every villager. The day's discussion was transduce with a composed transducer summing the kept items. Grace
wrote the form `(transduce (comp (map inc) (filter even?)) + 0 [1 2 3 4 5])` on a square of parchment and passed it
across the table; Tom, her legs heavy from sprinting but pleased to be trusted
again, agreed to read it into the REPL.

Write a Clojure expression that computes the sum after inc-then-keep-evens via transduce.

---

{"tool_calls":[{"name":"eval","args":{"form":"(transduce (comp (map inc) (filter even?)) + 0 [1 2 3 4 5])"}}]}
```

### Record 3 — example 1 of 2

**form**: `(into [] (comp (map inc) (filter even?)) [1 2 3 4])` • **expected**: `[2, 4]`

**concept_phrase**: `the composed transducer (comp (map inc) (filter even?))`

**question_what**: `the result of inc-then-keep-evens via a composed transducer`

```
The boy on the hill thought the trick clever the first time he played it. It happened by the woods.

"This isn't a clever guess," Alice said in the woods, saying very little.
"It's a tool." Pat looked at the composed transducer (comp (map inc) (filter even?)) and
admitted they would not have known what to write.
Alice sketched `(into [] (comp (map inc) (filter even?)) [1 2 3 4])` on a slate so the runtime could speak
for itself.

Write a form whose evaluation gives the result of inc-then-keep-evens via a composed transducer.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (comp (map inc) (filter even?)) [1 2 3 4])"}}]}
```

### Record 4 — example 2 of 2

**form**: `(transduce (comp (map inc) (filter even?)) + 0 [1 2 3 4 5])` • **expected**: `12`

**concept_phrase**: `transduce with a composed transducer summing the kept items`

**question_what**: `the sum after inc-then-keep-evens via transduce`

```
The boy on the hill thought the trick clever the first time he played it. This was along the road.

George kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today on the road the next entry was
transduce with a composed transducer summing the kept items. Jess peered over his shoulder
at the form `(transduce (comp (map inc) (filter even?)) + 0 [1 2 3 4 5])` and was asked, gently, to be the one to
submit it.

Write a Clojure expression that computes the sum after inc-then-keep-evens via transduce.

---

{"tool_calls":[{"name":"eval","args":{"form":"(transduce (comp (map inc) (filter even?)) + 0 [1 2 3 4 5])"}}]}
```

### Record 5 — example 1 of 2

**form**: `(into [] (comp (map inc) (filter even?)) [1 2 3 4])` • **expected**: `[2, 4]`

**concept_phrase**: `the composed transducer (comp (map inc) (filter even?))`

**question_what**: `the result of inc-then-keep-evens via a composed transducer`

```
The boy on the hill thought the trick clever the first time he played it. This was by the forest.

Halfway through the morning watch, Lou called out
at the edge of the forest, demanding a verdict on the form `(into [] (comp (map inc) (filter even?)) [1 2 3 4])` and refusing
to descend until somebody confirmed it. Lou insisted
she already knew the answer. George, walking up
at an unhurried pace, simply said: "Submit the composed transducer (comp (map inc) (filter even?)) to the
REPL. Whatever comes back is the answer."

What Clojure form computes the result of inc-then-keep-evens via a composed transducer? Submit it via `eval`.

---

I write the form using the appropriate library or tool.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (comp (map inc) (filter even?)) [1 2 3 4])"}}]}
```

---

## G12-03: into with a transducer (xform)

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(into #{} (map inc) [1 2 3])` • **expected**: `{2, 3, 4}`

**concept_phrase**: `into a set with the (map inc) transducer`

**question_what**: `the set produced by mapping inc into an empty set`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place at the edge of the village.

A small crowd of villagers had gathered near the village to watch
Will attempt to predict, off the cuff, what the REPL would
return. Alice pointed to into a set with the (map inc) transducer and read out the
form aloud: `(into #{} (map inc) [1 2 3])`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a Clojure expression that computes the set produced by mapping inc into an empty set.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(into #{} (map inc) [1 2 3])"}}]}
```

### Record 2 — example 2 of 2

**form**: `(into [] (take 3) (range 100))` • **expected**: `[0, 1, 2]`

**concept_phrase**: `into [] with the (take 3) transducer over (range 100)`

**question_what**: `the first three items collected through a transducer`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened near the meadow.

Halfway through the morning watch, Lou called out
near the meadow, demanding a verdict on the form `(into [] (take 3) (range 100))` and refusing
to descend until somebody confirmed it. Lou insisted
she already knew the answer. Oliver, walking up
at an unhurried pace, simply said: "Submit into [] with the (take 3) transducer over (range 100) to the
REPL. Whatever comes back is the answer."

Write a form whose evaluation gives the first three items collected through a transducer.

---

I write the form using the appropriate library or tool.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (take 3) (range 100))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(into #{} (map inc) [1 2 3])` • **expected**: `{2, 3, 4}`

**concept_phrase**: `into a set with the (map inc) transducer`

**question_what**: `the set produced by mapping inc into an empty set`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A wooden notice nailed to a post by the farm carried a small puzzle. The
riddle simply asked the reader to evaluate `(into #{} (map inc) [1 2 3])`. Pat
laughed, with great whoops of laughter, and declared it too easy to bother with.
Frank said, patiently, that the only way to be certain of
into a set with the (map inc) transducer was to put it in the REPL.

Write a Clojure expression that computes the set produced by mapping inc into an empty set.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(into #{} (map inc) [1 2 3])"}}]}
```

### Record 4 — example 2 of 2

**form**: `(into [] (take 3) (range 100))` • **expected**: `[0, 1, 2]`

**concept_phrase**: `into [] with the (take 3) transducer over (range 100)`

**question_what**: `the first three items collected through a transducer`

```
The boy on the hill thought the trick clever the first time he played it.

The elder of the village kept a small slate near the village, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was into [] with the (take 3) transducer over (range 100). Bob read
out the form `(into [] (take 3) (range 100))` so Will could write it
properly into the REPL and earn an honest mark on the slate.

What Clojure form computes the first three items collected through a transducer? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (take 3) (range 100))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(into #{} (map inc) [1 2 3])` • **expected**: `{2, 3, 4}`

**concept_phrase**: `into a set with the (map inc) transducer`

**question_what**: `the set produced by mapping inc into an empty set`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A harvest gathering at the end of the season by the village brought together
every villager. The day's discussion was into a set with the (map inc) transducer. Robin
wrote the form `(into #{} (map inc) [1 2 3])` on a square of parchment and passed it
across the table; Will, lulled by the gentle wind but pleased to be trusted
again, agreed to read it into the REPL.

Write a Clojure expression that computes the set produced by mapping inc into an empty set.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into #{} (map inc) [1 2 3])"}}]}
```

---

## G12-04: core.async introduction

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the core.async primitives chan/go/<!/>!`

**question_what**: `the marker for the core.async lesson`

```
The boy on the hill thought the trick clever the first time he played it.

Pat, lulled by the gentle wind from a season of false alarms long
since outgrown, was finally willing to study patterns. Bob
pointed near the farm at the core.async primitives chan/go/<!/>!. The form `(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)` was the
canonical example; the REPL would confirm what it produced.

Write a Clojure expression that computes the marker for the core.async lesson.

---

I express the pipeline / spec / test as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(chan), (go ...), (<! ...), (>! ...) form the core.async core\" :studied)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do "go-blocks let you write async code as if it were synchronous" :async)` • **expected**: `':async'`

**concept_phrase**: `what go blocks give you`

**question_what**: `the marker keyword for go-blocks`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened at the edge of the village.

A harvest gathering at the end of the season near the village brought together
every villager. The day's discussion was what go blocks give you. George
wrote the form `(do "go-blocks let you write async code as if it were synchronous" :async)` on a square of parchment and passed it
across the table; Jess, yawning at the soft moss but pleased to be trusted
again, agreed to read it into the REPL.

Write a Clojure expression that computes the marker keyword for go-blocks.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"go-blocks let you write async code as if it were synchronous\" :async)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the core.async primitives chan/go/<!/>!`

**question_what**: `the marker for the core.async lesson`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Sam had filled an entire notebook over the long season with
tools and patterns: transducers, channels, specs, tests. near the road, the
next entry was the core.async primitives chan/go/<!/>!, and the form was `(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)`.
Tom, his heart sinking but more reflective than usual,
agreed to write the form into the REPL.

Write a Clojure expression that computes the marker for the core.async lesson.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(chan), (go ...), (<! ...), (>! ...) form the core.async core\" :studied)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do "go-blocks let you write async code as if it were synchronous" :async)` • **expected**: `':async'`

**concept_phrase**: `what go blocks give you`

**question_what**: `the marker keyword for go-blocks`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden notice nailed to a post at the edge of the orchard carried a small puzzle. The
riddle simply asked the reader to evaluate `(do "go-blocks let you write async code as if it were synchronous" :async)`. Tom
laughed, puffed up with pride, and declared it too easy to bother with.
Bob said, patiently, that the only way to be certain of
what go blocks give you was to put it in the REPL.

Write a form whose evaluation gives the marker keyword for go-blocks.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"go-blocks let you write async code as if it were synchronous\" :async)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the core.async primitives chan/go/<!/>!`

**question_what**: `the marker for the core.async lesson`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place at the edge of the orchard.

A small crowd of villagers had gathered near the orchard to watch
Lou attempt to predict, off the cuff, what the REPL would
return. Oliver pointed to the core.async primitives chan/go/<!/>! and read out the
form aloud: `(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

What Clojure form computes the marker for the core.async lesson? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(chan), (go ...), (<! ...), (>! ...) form the core.async core\" :studied)"}}]}
```

---

## G12-05: Channels and pipelines

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do "pipe, mult, mix, pipeline-async route values across channels" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the pipeline operators in core.async`

**question_what**: `the marker for the channel-pipeline lesson`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

"There is no need to evaluate that," Jess said, swaggering through the underbrush.
"Anyone can see what the pipeline operators in core.async comes to." Alice, who
near the hilltop had heard such claims many times, asked her to
actually write the form `(do "pipe, mult, mix, pipeline-async route values across channels" :studied)` and submit it to the REPL —
just to be sure.

Question: write a Clojure expression for the marker for the channel-pipeline lesson.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"pipe, mult, mix, pipeline-async route values across channels\" :studied)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do "pipelines transform streams of values channel-to-channel" :pipelines)` • **expected**: `':pipelines'`

**concept_phrase**: `the role of pipelines in async code`

**question_what**: `the marker keyword for pipelines`

```
The boy on the hill thought the trick clever the first time he played it.

"This isn't a clever guess," Alex said in the forest, saying very little.
"It's a tool." Tom looked at the role of pipelines in async code and
admitted he would not have known what to write.
Alex sketched `(do "pipelines transform streams of values channel-to-channel" :pipelines)` on a slate so the runtime could speak
for itself.

What Clojure form computes the marker keyword for pipelines? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"pipelines transform streams of values channel-to-channel\" :pipelines)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do "pipe, mult, mix, pipeline-async route values across channels" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the pipeline operators in core.async`

**question_what**: `the marker for the channel-pipeline lesson`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place at the edge of the orchard.

Halfway through the morning watch, Jess called out
in the orchard, demanding a verdict on the form `(do "pipe, mult, mix, pipeline-async route values across channels" :studied)` and refusing
to descend until somebody confirmed it. Jess insisted
she already knew the answer. Grace, walking up
at an unhurried pace, simply said: "Submit the pipeline operators in core.async to the
REPL. Whatever comes back is the answer."

Write a form whose evaluation gives the marker for the channel-pipeline lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"pipe, mult, mix, pipeline-async route values across channels\" :studied)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do "pipelines transform streams of values channel-to-channel" :pipelines)` • **expected**: `':pipelines'`

**concept_phrase**: `the role of pipelines in async code`

**question_what**: `the marker keyword for pipelines`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

"This isn't a clever guess," Carol said in the farm, her eyes always on the path.
"It's a tool." Lou looked at the role of pipelines in async code and
admitted she would not have known what to write.
Carol sketched `(do "pipelines transform streams of values channel-to-channel" :pipelines)` on a slate so the runtime could speak
for itself.

Question: write a Clojure expression for the marker keyword for pipelines.

---

I express the pipeline / spec / test as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"pipelines transform streams of values channel-to-channel\" :pipelines)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do "pipe, mult, mix, pipeline-async route values across channels" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the pipeline operators in core.async`

**question_what**: `the marker for the channel-pipeline lesson`

```
The boy on the hill thought the trick clever the first time he played it.

"This isn't a clever guess," Carol said at the edge of the farm, stepping deliberately.
"It's a tool." Jess looked at the pipeline operators in core.async and
admitted she would not have known what to write.
Carol sketched `(do "pipe, mult, mix, pipeline-async route values across channels" :studied)` on a slate so the runtime could speak
for itself.

What Clojure form computes the marker for the channel-pipeline lesson? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"pipe, mult, mix, pipeline-async route values across channels\" :studied)"}}]}
```

---

## G12-06: clojure.spec

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))` • **expected**: `True`

**concept_phrase**: `(s/valid? int? 42) — a basic spec check`

**question_what**: `whether 42 conforms to the int? spec`

```
The boy on the hill thought the trick clever the first time he played it.

Will, weary from the morning's effort from a season of false alarms long
since outgrown, was finally willing to study patterns. Frank
pointed atop the hilltop at (s/valid? int? 42) — a basic spec check. The form `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))` was the
canonical example; the REPL would confirm what it produced.

Write a Clojure expression that computes whether 42 conforms to the int? spec.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (require '[clojure.spec.alpha :as s]) (s/valid? string? 42))` • **expected**: `False`

**concept_phrase**: `(s/valid? string? 42) — a failing spec check`

**question_what**: `whether 42 conforms to the string? spec`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

"There is no need to evaluate that," Pat said, with a smug grin.
"Anyone can see what (s/valid? string? 42) — a failing spec check comes to." Robin, who
near the woods had heard such claims many times, asked them to
actually write the form `(do (require '[clojure.spec.alpha :as s]) (s/valid? string? 42))` and submit it to the REPL —
just to be sure.

What Clojure form computes whether 42 conforms to the string? spec? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (require '[clojure.spec.alpha :as s]) (s/valid? string? 42))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))` • **expected**: `True`

**concept_phrase**: `(s/valid? int? 42) — a basic spec check`

**question_what**: `whether 42 conforms to the int? spec`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

"This isn't a clever guess," Morgan said atop the hilltop, saying very little.
"It's a tool." Jess looked at (s/valid? int? 42) — a basic spec check and
admitted she would not have known what to write.
Morgan sketched `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))` on a slate so the runtime could speak
for itself.

Question: write a Clojure expression for whether 42 conforms to the int? spec.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (require '[clojure.spec.alpha :as s]) (s/valid? string? 42))` • **expected**: `False`

**concept_phrase**: `(s/valid? string? 42) — a failing spec check`

**question_what**: `whether 42 conforms to the string? spec`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A wooden notice nailed to a post by the orchard carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (require '[clojure.spec.alpha :as s]) (s/valid? string? 42))`. Pat
laughed, puffed up with pride, and declared it too easy to bother with.
Robin said, patiently, that the only way to be certain of
(s/valid? string? 42) — a failing spec check was to put it in the REPL.

Write a Clojure expression that computes whether 42 conforms to the string? spec.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (require '[clojure.spec.alpha :as s]) (s/valid? string? 42))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))` • **expected**: `True`

**concept_phrase**: `(s/valid? int? 42) — a basic spec check`

**question_what**: `whether 42 conforms to the int? spec`

```
Every shepherd in the valley knew the danger of crying wolf for sport. It happened along the road.

George kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the road the next entry was
(s/valid? int? 42) — a basic spec check. Will peered over his shoulder
at the form `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))` and was asked, gently, to be the one to
submit it.

What Clojure form computes whether 42 conforms to the int? spec? Submit it via `eval`.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))"}}]}
```

---

## G12-07: Spec generators

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do "s/exercise produces sample inputs for a spec" :studied)` • **expected**: `':studied'`

**concept_phrase**: `what s/exercise does`

**question_what**: `the marker for the spec-generators lesson`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(do "s/exercise produces sample inputs for a spec" :studied)`, and the line
above it read what s/exercise does. Robin handed the page to
Tom, who, lulled by the gentle wind, agreed to write it out properly.

What Clojure form computes the marker for the spec-generators lesson? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"s/exercise produces sample inputs for a spec\" :studied)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do "spec generators turn specs into property-based test inputs" :gens)` • **expected**: `':gens'`

**concept_phrase**: `the role of spec generators`

**question_what**: `the marker keyword for spec generators`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place near the meadow.

"This isn't a clever guess," Oliver said by the meadow, without complaint.
"It's a tool." Jess looked at the role of spec generators and
admitted she would not have known what to write.
Oliver sketched `(do "spec generators turn specs into property-based test inputs" :gens)` on a slate so the runtime could speak
for itself.

Write a Clojure expression that computes the marker keyword for spec generators.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"spec generators turn specs into property-based test inputs\" :gens)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do "s/exercise produces sample inputs for a spec" :studied)` • **expected**: `':studied'`

**concept_phrase**: `what s/exercise does`

**question_what**: `the marker for the spec-generators lesson`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place on the hilltop.

The long season had ended at the edge of the hilltop and the two were sitting beneath an
old tree, comparing notes. Oliver drew what s/exercise does into
the dust. "We've come a long way," he said. "The form
`(do "s/exercise produces sample inputs for a spec" :studied)` is the kind of thing we'd reach for now." Will
nodded — for once her legs heavy from sprinting enough to listen.

What Clojure form computes the marker for the spec-generators lesson? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"s/exercise produces sample inputs for a spec\" :studied)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do "spec generators turn specs into property-based test inputs" :gens)` • **expected**: `':gens'`

**concept_phrase**: `the role of spec generators`

**question_what**: `the marker keyword for spec generators`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

"There is no need to evaluate that," Tom said, with a smug grin.
"Anyone can see what the role of spec generators comes to." Alex, who
in the orchard had heard such claims many times, asked him to
actually write the form `(do "spec generators turn specs into property-based test inputs" :gens)` and submit it to the REPL —
just to be sure.

Write a Clojure expression that computes the marker keyword for spec generators.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"spec generators turn specs into property-based test inputs\" :gens)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do "s/exercise produces sample inputs for a spec" :studied)` • **expected**: `':studied'`

**concept_phrase**: `what s/exercise does`

**question_what**: `the marker for the spec-generators lesson`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

George kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the farm the next entry was
what s/exercise does. Jess peered over his shoulder
at the form `(do "s/exercise produces sample inputs for a spec" :studied)` and was asked, gently, to be the one to
submit it.

What Clojure form computes the marker for the spec-generators lesson? Submit it via `eval`.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"s/exercise produces sample inputs for a spec\" :studied)"}}]}
```

---

## G12-08: clojure.test

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(= (+ 1 2) 3)` • **expected**: `True`

**concept_phrase**: `(= (+ 1 2) 3) — what an `is` would test`

**question_what**: `the truth value an `is` assertion would record`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened near the orchard.

Tom, lulled by the gentle wind from a season of false alarms long
since outgrown, was finally willing to study patterns. Oliver
pointed in the orchard at (= (+ 1 2) 3) — what an `is` would test. The form `(= (+ 1 2) 3)` was the
canonical example; the REPL would confirm what it produced.

Write a form whose evaluation gives the truth value an `is` assertion would record.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(= (+ 1 2) 3)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do "(deftest …), (is …), (testing …) are the core test forms" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the clojure.test core forms`

**question_what**: `the marker for the clojure.test lesson`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened by the orchard.

The long season had ended by the orchard and the two were sitting beneath an
old tree, comparing notes. Alex drew the clojure.test core forms into
the dust. "We've come a long way," they said. "The form
`(do "(deftest …), (is …), (testing …) are the core test forms" :studied)` is the kind of thing we'd reach for now." Pat
nodded — for once lulled by the gentle wind enough to listen.

Write a Clojure expression that computes the marker for the clojure.test lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(deftest …), (is …), (testing …) are the core test forms\" :studied)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(= (+ 1 2) 3)` • **expected**: `True`

**concept_phrase**: `(= (+ 1 2) 3) — what an `is` would test`

**question_what**: `the truth value an `is` assertion would record`

```
The boy on the hill thought the trick clever the first time he played it. It happened at the edge of the farm.

At the village square near the farm, a row of small markers commemorated
the libraries the careful shepherds had learned over the season. The
newest one honoured (= (+ 1 2) 3) — what an `is` would test. Grace touched it and
said the form to remember was `(= (+ 1 2) 3)`; Will
agreed to submit it.

Write a Clojure expression that computes the truth value an `is` assertion would record.

---

{"tool_calls":[{"name":"eval","args":{"form":"(= (+ 1 2) 3)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do "(deftest …), (is …), (testing …) are the core test forms" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the clojure.test core forms`

**question_what**: `the marker for the clojure.test lesson`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place in the meadow.

A wooden notice nailed to a post near the meadow carried a small puzzle. The
riddle simply asked the reader to evaluate `(do "(deftest …), (is …), (testing …) are the core test forms" :studied)`. Tom
laughed, with a smug grin, and declared it too easy to bother with.
Sam said, patiently, that the only way to be certain of
the clojure.test core forms was to put it in the REPL.

Write a Clojure expression that computes the marker for the clojure.test lesson.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(deftest …), (is …), (testing …) are the core test forms\" :studied)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(= (+ 1 2) 3)` • **expected**: `True`

**concept_phrase**: `(= (+ 1 2) 3) — what an `is` would test`

**question_what**: `the truth value an `is` assertion would record`

```
The boy on the hill thought the trick clever the first time he played it.

Oliver had filled an entire notebook over the long season with
tools and patterns: transducers, channels, specs, tests. by the orchard, the
next entry was (= (+ 1 2) 3) — what an `is` would test, and the form was `(= (+ 1 2) 3)`.
Pat, wishing she had been more careful but more reflective than usual,
agreed to write the form into the REPL.

Write a Clojure expression that computes the truth value an `is` assertion would record.

---

{"tool_calls":[{"name":"eval","args":{"form":"(= (+ 1 2) 3)"}}]}
```

---

## G12-09: Test fixtures

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)` • **expected**: `':studied'`

**concept_phrase**: `use-fixtures and the fixture pattern`

**question_what**: `the marker for the fixtures lesson`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place in the woods.

"There is no need to evaluate that," Will said, as if the race were already won.
"Anyone can see what use-fixtures and the fixture pattern comes to." George, who
at the edge of the woods had heard such claims many times, asked him to
actually write the form `(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)` and submit it to the REPL —
just to be sure.

Question: write a Clojure expression for the marker for the fixtures lesson.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(use-fixtures :each f) wraps every deftest in setup/teardown\" :studied)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do "fixtures provide setup/teardown around deftests" :fixtures)` • **expected**: `':fixtures'`

**concept_phrase**: `the purpose of fixtures`

**question_what**: `the marker keyword for the fixture lesson`

```
The boy on the hill thought the trick clever the first time he played it.

The long season had ended by the forest and the two were sitting beneath an
old tree, comparing notes. Alice drew the purpose of fixtures into
the dust. "We've come a long way," she said. "The form
`(do "fixtures provide setup/teardown around deftests" :fixtures)` is the kind of thing we'd reach for now." Pat
nodded — for once lulled by the gentle wind enough to listen.

Write a form whose evaluation gives the marker keyword for the fixture lesson.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"fixtures provide setup/teardown around deftests\" :fixtures)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)` • **expected**: `':studied'`

**concept_phrase**: `use-fixtures and the fixture pattern`

**question_what**: `the marker for the fixtures lesson`

```
The boy on the hill thought the trick clever the first time he played it.

Jess, yawning at the soft moss from a season of false alarms long
since outgrown, was finally willing to study patterns. Morgan
pointed in the orchard at use-fixtures and the fixture pattern. The form `(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)` was the
canonical example; the REPL would confirm what it produced.

Write a Clojure expression that computes the marker for the fixtures lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(use-fixtures :each f) wraps every deftest in setup/teardown\" :studied)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do "fixtures provide setup/teardown around deftests" :fixtures)` • **expected**: `':fixtures'`

**concept_phrase**: `the purpose of fixtures`

**question_what**: `the marker keyword for the fixture lesson`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

"There is no need to evaluate that," Pat said, with great whoops of laughter.
"Anyone can see what the purpose of fixtures comes to." Carol, who
at the edge of the woods had heard such claims many times, asked them to
actually write the form `(do "fixtures provide setup/teardown around deftests" :fixtures)` and submit it to the REPL —
just to be sure.

Write a form whose evaluation gives the marker keyword for the fixture lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"fixtures provide setup/teardown around deftests\" :fixtures)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)` • **expected**: `':studied'`

**concept_phrase**: `use-fixtures and the fixture pattern`

**question_what**: `the marker for the fixtures lesson`

```
The boy on the hill thought the trick clever the first time he played it.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)`, and the line
above it read use-fixtures and the fixture pattern. George handed the page to
Tom, who, yawning at the soft moss, agreed to write it out properly.

Question: write a Clojure expression for the marker for the fixtures lesson.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(use-fixtures :each f) wraps every deftest in setup/teardown\" :studied)"}}]}
```

---

## G12-10: Property-based testing

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(= (reverse (reverse [1 2 3])) [1 2 3])` • **expected**: `True`

**concept_phrase**: `the property that double-reverse is identity`

**question_what**: `the truth value of the double-reverse property on [1 2 3]`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Lou called down from a stone atop the hilltop where someone had
chalked the property that double-reverse is identity on a flat board. Lou, boasting at every turn,
declared she already knew what would come back. Grace,
with steady, careful steps, asked her to actually submit the form
`(= (reverse (reverse [1 2 3])) [1 2 3])` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the truth value of the double-reverse property on [1 2 3].

---

{"tool_calls":[{"name":"eval","args":{"form":"(= (reverse (reverse [1 2 3])) [1 2 3])"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do "test.check generates inputs and checks properties hold" :studied)` • **expected**: `':studied'`

**concept_phrase**: `what test.check does`

**question_what**: `the marker for property-based testing`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. This was near the orchard.

Carol had filled an entire notebook over the long season with
tools and patterns: transducers, channels, specs, tests. near the orchard, the
next entry was what test.check does, and the form was `(do "test.check generates inputs and checks properties hold" :studied)`.
Pat, regretting every careless step but more reflective than usual,
agreed to write the form into the REPL.

Question: write a Clojure expression for the marker for property-based testing.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"test.check generates inputs and checks properties hold\" :studied)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(= (reverse (reverse [1 2 3])) [1 2 3])` • **expected**: `True`

**concept_phrase**: `the property that double-reverse is identity`

**question_what**: `the truth value of the double-reverse property on [1 2 3]`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Halfway through the morning watch, Tom called out
on the hilltop, demanding a verdict on the form `(= (reverse (reverse [1 2 3])) [1 2 3])` and refusing
to descend until somebody confirmed it. Tom insisted
he already knew the answer. Alice, walking up
at an unhurried pace, simply said: "Submit the property that double-reverse is identity to the
REPL. Whatever comes back is the answer."

What Clojure form computes the truth value of the double-reverse property on [1 2 3]? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(= (reverse (reverse [1 2 3])) [1 2 3])"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do "test.check generates inputs and checks properties hold" :studied)` • **expected**: `':studied'`

**concept_phrase**: `what test.check does`

**question_what**: `the marker for property-based testing`

```
The boy on the hill thought the trick clever the first time he played it. This was along the road.

A harvest gathering at the end of the season along the road brought together
every villager. The day's discussion was what test.check does. Alice
wrote the form `(do "test.check generates inputs and checks properties hold" :studied)` on a square of parchment and passed it
across the table; Tom, her legs heavy from sprinting but pleased to be trusted
again, agreed to read it into the REPL.

Question: write a Clojure expression for the marker for property-based testing.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"test.check generates inputs and checks properties hold\" :studied)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(= (reverse (reverse [1 2 3])) [1 2 3])` • **expected**: `True`

**concept_phrase**: `the property that double-reverse is identity`

**question_what**: `the truth value of the double-reverse property on [1 2 3]`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A harvest gathering at the end of the season by the farm brought together
every villager. The day's discussion was the property that double-reverse is identity. Robin
wrote the form `(= (reverse (reverse [1 2 3])) [1 2 3])` on a square of parchment and passed it
across the table; Tom, lulled by the gentle wind but pleased to be trusted
again, agreed to read it into the REPL.

Write a form whose evaluation gives the truth value of the double-reverse property on [1 2 3].

---

{"tool_calls":[{"name":"eval","args":{"form":"(= (reverse (reverse [1 2 3])) [1 2 3])"}}]}
```

---

## G12-11: Leiningen project.clj

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the project.clj manifest for Leiningen`

**question_what**: `the marker for the project.clj lesson`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened in the meadow.

A wooden notice nailed to a post in the meadow carried a small puzzle. The
riddle simply asked the reader to evaluate `(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)`. Will
laughed, boasting at every turn, and declared it too easy to bother with.
Bob said, patiently, that the only way to be certain of
the project.clj manifest for Leiningen was to put it in the REPL.

Question: write a Clojure expression for the marker for the project.clj lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"project.clj declares :dependencies, :main, :profiles for Leiningen\" :studied)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do "Leiningen reads project.clj at the project root" :lein)` • **expected**: `':lein'`

**concept_phrase**: `where Leiningen finds project.clj`

**question_what**: `the marker keyword for the Leiningen lesson`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place near the road.

Sam kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the road the next entry was
where Leiningen finds project.clj. Jess peered over their shoulder
at the form `(do "Leiningen reads project.clj at the project root" :lein)` and was asked, gently, to be the one to
submit it.

Write a Clojure expression that computes the marker keyword for the Leiningen lesson.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Leiningen reads project.clj at the project root\" :lein)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the project.clj manifest for Leiningen`

**question_what**: `the marker for the project.clj lesson`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

"This isn't a clever guess," Alex said in the village, stepping deliberately.
"It's a tool." Will looked at the project.clj manifest for Leiningen and
admitted he would not have known what to write.
Alex sketched `(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)` on a slate so the runtime could speak
for itself.

Write a Clojure expression that computes the marker for the project.clj lesson.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"project.clj declares :dependencies, :main, :profiles for Leiningen\" :studied)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do "Leiningen reads project.clj at the project root" :lein)` • **expected**: `':lein'`

**concept_phrase**: `where Leiningen finds project.clj`

**question_what**: `the marker keyword for the Leiningen lesson`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. This was on the road.

George had filled an entire notebook over the long season with
tools and patterns: transducers, channels, specs, tests. on the road, the
next entry was where Leiningen finds project.clj, and the form was `(do "Leiningen reads project.clj at the project root" :lein)`.
Lou, wishing she had been more careful but more reflective than usual,
agreed to write the form into the REPL.

What Clojure form computes the marker keyword for the Leiningen lesson? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Leiningen reads project.clj at the project root\" :lein)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the project.clj manifest for Leiningen`

**question_what**: `the marker for the project.clj lesson`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place by the orchard.

Halfway through the morning watch, Lou called out
near the orchard, demanding a verdict on the form `(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)` and refusing
to descend until somebody confirmed it. Lou insisted
she already knew the answer. Carol, walking up
at an unhurried pace, simply said: "Submit the project.clj manifest for Leiningen to the
REPL. Whatever comes back is the answer."

Write a form whose evaluation gives the marker for the project.clj lesson.

---

I write the form using the appropriate library or tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"project.clj declares :dependencies, :main, :profiles for Leiningen\" :studied)"}}]}
```

---

## G12-12: deps.edn projects

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the deps.edn manifest for the Clojure CLI`

**question_what**: `the marker for the deps.edn lesson`

```
The boy on the hill thought the trick clever the first time he played it. This was near the orchard.

A small crowd of villagers had gathered near the orchard to watch
Jess attempt to predict, off the cuff, what the REPL would
return. Grace pointed to the deps.edn manifest for the Clojure CLI and read out the
form aloud: `(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a Clojure expression that computes the marker for the deps.edn lesson.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"deps.edn declares :deps and :aliases for the Clojure CLI\" :studied)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do "deps.edn is read by the official `clj`/`clojure` tools" :deps)` • **expected**: `':deps'`

**concept_phrase**: `who reads deps.edn`

**question_what**: `the marker keyword for the deps.edn lesson`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A small crowd of villagers had gathered in the meadow to watch
Tom attempt to predict, off the cuff, what the REPL would
return. Robin pointed to who reads deps.edn and read out the
form aloud: `(do "deps.edn is read by the official `clj`/`clojure` tools" :deps)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Question: write a Clojure expression for the marker keyword for the deps.edn lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"deps.edn is read by the official `clj`/`clojure` tools\" :deps)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the deps.edn manifest for the Clojure CLI`

**question_what**: `the marker for the deps.edn lesson`

```
The boy on the hill thought the trick clever the first time he played it. It happened along the road.

The elder of the village kept a small slate near the road, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the deps.edn manifest for the Clojure CLI. George read
out the form `(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)` so Tom could write it
properly into the REPL and earn an honest mark on the slate.

What Clojure form computes the marker for the deps.edn lesson? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"deps.edn declares :deps and :aliases for the Clojure CLI\" :studied)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do "deps.edn is read by the official `clj`/`clojure` tools" :deps)` • **expected**: `':deps'`

**concept_phrase**: `who reads deps.edn`

**question_what**: `the marker keyword for the deps.edn lesson`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A small slate sat on a flat stone on the road; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(do "deps.edn is read by the official `clj`/`clojure` tools" :deps)`, and the page
heading read who reads deps.edn. Frank nodded at Will to
write the form properly so the slate would carry an honest entry.

Question: write a Clojure expression for the marker keyword for the deps.edn lesson.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"deps.edn is read by the official `clj`/`clojure` tools\" :deps)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the deps.edn manifest for the Clojure CLI`

**question_what**: `the marker for the deps.edn lesson`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A harvest gathering at the end of the season in the farm brought together
every villager. The day's discussion was the deps.edn manifest for the Clojure CLI. Oliver
wrote the form `(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)` on a square of parchment and passed it
across the table; Tom, yawning at the soft moss but pleased to be trusted
again, agreed to read it into the REPL.

What Clojure form computes the marker for the deps.edn lesson? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"deps.edn declares :deps and :aliases for the Clojure CLI\" :studied)"}}]}
```

---

## G12-13: Aliases and tools

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do "`clj -M:test` runs the :test alias from deps.edn" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the alias-execution pattern with the Clojure CLI`

**question_what**: `the marker for the aliases lesson`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

At the village square at the edge of the woods, a row of small markers commemorated
the libraries the careful shepherds had learned over the season. The
newest one honoured the alias-execution pattern with the Clojure CLI. Sam touched it and
said the form to remember was `(do "`clj -M:test` runs the :test alias from deps.edn" :studied)`; Pat
agreed to submit it.

Write a Clojure expression that computes the marker for the aliases lesson.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"`clj -M:test` runs the :test alias from deps.edn\" :studied)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do "aliases compose extra paths, deps, and main opts" :aliases)` • **expected**: `':aliases'`

**concept_phrase**: `what aliases let you compose`

**question_what**: `the marker keyword for the aliases lesson`

```
The boy on the hill thought the trick clever the first time he played it.

George had been trying to teach Jess how the REPL
works. "Look here," he said, pointing to what aliases let you compose.
"You hand the form `(do "aliases compose extra paths, deps, and main opts" :aliases)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, drowsy from the warm sun, agreed to try.

Write a Clojure expression that computes the marker keyword for the aliases lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"aliases compose extra paths, deps, and main opts\" :aliases)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do "`clj -M:test` runs the :test alias from deps.edn" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the alias-execution pattern with the Clojure CLI`

**question_what**: `the marker for the aliases lesson`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened at the edge of the farm.

A small crowd of villagers had gathered in the farm to watch
Tom attempt to predict, off the cuff, what the REPL would
return. Bob pointed to the alias-execution pattern with the Clojure CLI and read out the
form aloud: `(do "`clj -M:test` runs the :test alias from deps.edn" :studied)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

What Clojure form computes the marker for the aliases lesson? Submit it via `eval`.

---

I let the REPL exercise the library form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"`clj -M:test` runs the :test alias from deps.edn\" :studied)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do "aliases compose extra paths, deps, and main opts" :aliases)` • **expected**: `':aliases'`

**concept_phrase**: `what aliases let you compose`

**question_what**: `the marker keyword for the aliases lesson`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. This was at the edge of the forest.

The elder of the village kept a small slate near the forest, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was what aliases let you compose. Morgan read
out the form `(do "aliases compose extra paths, deps, and main opts" :aliases)` so Lou could write it
properly into the REPL and earn an honest mark on the slate.

Write a Clojure expression that computes the marker keyword for the aliases lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"aliases compose extra paths, deps, and main opts\" :aliases)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do "`clj -M:test` runs the :test alias from deps.edn" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the alias-execution pattern with the Clojure CLI`

**question_what**: `the marker for the aliases lesson`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Lou called down from a stone near the woods where someone had
chalked the alias-execution pattern with the Clojure CLI on a flat board. Lou, boasting at every turn,
declared she already knew what would come back. Alex,
stepping deliberately, asked her to actually submit the form
`(do "`clj -M:test` runs the :test alias from deps.edn" :studied)` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the marker for the aliases lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"`clj -M:test` runs the :test alias from deps.edn\" :studied)"}}]}
```

---

## G12-14: Pedestal / Ring (web stack brief)

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do "Ring models HTTP as request-map -> response-map" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the Ring HTTP-as-data abstraction`

**question_what**: `the marker for the Ring lesson`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A small crowd of villagers had gathered at the edge of the orchard to watch
Jess attempt to predict, off the cuff, what the REPL would
return. Carol pointed to the Ring HTTP-as-data abstraction and read out the
form aloud: `(do "Ring models HTTP as request-map -> response-map" :studied)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Question: write a Clojure expression for the marker for the Ring lesson.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Ring models HTTP as request-map -> response-map\" :studied)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do "Pedestal layers interceptors over Ring for richer pipelines" :web)` • **expected**: `':web'`

**concept_phrase**: `the Pedestal interceptor model`

**question_what**: `the marker keyword for the Pedestal lesson`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. This was along the road.

At the village square along the road, a row of small markers commemorated
the libraries the careful shepherds had learned over the season. The
newest one honoured the Pedestal interceptor model. Grace touched it and
said the form to remember was `(do "Pedestal layers interceptors over Ring for richer pipelines" :web)`; Pat
agreed to submit it.

Question: write a Clojure expression for the marker keyword for the Pedestal lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Pedestal layers interceptors over Ring for richer pipelines\" :web)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do "Ring models HTTP as request-map -> response-map" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the Ring HTTP-as-data abstraction`

**question_what**: `the marker for the Ring lesson`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Halfway through the morning watch, Will called out
in the woods, demanding a verdict on the form `(do "Ring models HTTP as request-map -> response-map" :studied)` and refusing
to descend until somebody confirmed it. Will insisted
he already knew the answer. Morgan, walking up
at an unhurried pace, simply said: "Submit the Ring HTTP-as-data abstraction to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the marker for the Ring lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Ring models HTTP as request-map -> response-map\" :studied)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do "Pedestal layers interceptors over Ring for richer pipelines" :web)` • **expected**: `':web'`

**concept_phrase**: `the Pedestal interceptor model`

**question_what**: `the marker keyword for the Pedestal lesson`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Alice had filled an entire notebook over the long season with
tools and patterns: transducers, channels, specs, tests. at the edge of the farm, the
next entry was the Pedestal interceptor model, and the form was `(do "Pedestal layers interceptors over Ring for richer pipelines" :web)`.
Tom, regretting every careless step but more reflective than usual,
agreed to write the form into the REPL.

Write a Clojure expression that computes the marker keyword for the Pedestal lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Pedestal layers interceptors over Ring for richer pipelines\" :web)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do "Ring models HTTP as request-map -> response-map" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the Ring HTTP-as-data abstraction`

**question_what**: `the marker for the Ring lesson`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

"There is no need to evaluate that," Jess said, as if the race were already won.
"Anyone can see what the Ring HTTP-as-data abstraction comes to." Grace, who
near the woods had heard such claims many times, asked her to
actually write the form `(do "Ring models HTTP as request-map -> response-map" :studied)` and submit it to the REPL —
just to be sure.

What Clojure form computes the marker for the Ring lesson? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Ring models HTTP as request-map -> response-map\" :studied)"}}]}
```

---

## G12-15: Datomic / XTDB (datalog db brief)

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the Datomic / XTDB family`

**question_what**: `the marker for the datalog-DB lesson`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

At the village square near the meadow, a row of small markers commemorated
the libraries the careful shepherds had learned over the season. The
newest one honoured the Datomic / XTDB family. Grace touched it and
said the form to remember was `(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)`; Lou
agreed to submit it.

What Clojure form computes the marker for the datalog-DB lesson? Submit it via `eval`.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Datomic and XTDB are immutable, time-aware datalog DBs\" :studied)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do "queries are written in datalog over EDN-shaped data" :datalog)` • **expected**: `':datalog'`

**concept_phrase**: `how queries look in these databases`

**question_what**: `the marker keyword for datalog queries`

```
Every shepherd in the valley knew the danger of crying wolf for sport. This was near the hilltop.

Tom called down from a stone atop the hilltop where someone had
chalked how queries look in these databases on a flat board. Tom, as if the race were already won,
declared he already knew what would come back. Alex,
untroubled by what others thought, asked him to actually submit the form
`(do "queries are written in datalog over EDN-shaped data" :datalog)` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the marker keyword for datalog queries.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"queries are written in datalog over EDN-shaped data\" :datalog)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the Datomic / XTDB family`

**question_what**: `the marker for the datalog-DB lesson`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

At the village square near the orchard, a row of small markers commemorated
the libraries the careful shepherds had learned over the season. The
newest one honoured the Datomic / XTDB family. George touched it and
said the form to remember was `(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)`; Lou
agreed to submit it.

Write a Clojure expression that computes the marker for the datalog-DB lesson.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Datomic and XTDB are immutable, time-aware datalog DBs\" :studied)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do "queries are written in datalog over EDN-shaped data" :datalog)` • **expected**: `':datalog'`

**concept_phrase**: `how queries look in these databases`

**question_what**: `the marker keyword for datalog queries`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

At the village square near the meadow, a row of small markers commemorated
the libraries the careful shepherds had learned over the season. The
newest one honoured how queries look in these databases. Frank touched it and
said the form to remember was `(do "queries are written in datalog over EDN-shaped data" :datalog)`; Will
agreed to submit it.

Question: write a Clojure expression for the marker keyword for datalog queries.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"queries are written in datalog over EDN-shaped data\" :datalog)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the Datomic / XTDB family`

**question_what**: `the marker for the datalog-DB lesson`

```
The boy on the hill thought the trick clever the first time he played it. All this took place in the village.

The long season had ended at the edge of the village and the two were sitting beneath an
old tree, comparing notes. Carol drew the Datomic / XTDB family into
the dust. "We've come a long way," she said. "The form
`(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)` is the kind of thing we'd reach for now." Jess
nodded — for once her legs heavy from sprinting enough to listen.

Write a Clojure expression that computes the marker for the datalog-DB lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Datomic and XTDB are immutable, time-aware datalog DBs\" :studied)"}}]}
```

---

## G12-16: Reagent (cljs UI brief)

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the Reagent wrapper around React`

**question_what**: `the marker for the Reagent lesson`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden notice nailed to a post by the orchard carried a small puzzle. The
riddle simply asked the reader to evaluate `(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)`. Pat
laughed, as if the race were already won, and declared it too easy to bother with.
Sam said, patiently, that the only way to be certain of
the Reagent wrapper around React was to put it in the REPL.

Write a form whose evaluation gives the marker for the Reagent lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Reagent wraps React with Hiccup-shaped Clojure data\" :studied)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do "components are functions returning Hiccup vectors" :reagent)` • **expected**: `':reagent'`

**concept_phrase**: `how Reagent components are written`

**question_what**: `the marker keyword for Reagent components`

```
The boy on the hill thought the trick clever the first time he played it. All this took place near the village.

The long season had ended at the edge of the village and the two were sitting beneath an
old tree, comparing notes. Alice drew how Reagent components are written into
the dust. "We've come a long way," she said. "The form
`(do "components are functions returning Hiccup vectors" :reagent)` is the kind of thing we'd reach for now." Tom
nodded — for once lulled by the gentle wind enough to listen.

What Clojure form computes the marker keyword for Reagent components? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"components are functions returning Hiccup vectors\" :reagent)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the Reagent wrapper around React`

**question_what**: `the marker for the Reagent lesson`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

"This isn't a clever guess," Bob said in the farm, with steady, careful steps.
"It's a tool." Pat looked at the Reagent wrapper around React and
admitted they would not have known what to write.
Bob sketched `(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)` on a slate so the runtime could speak
for itself.

Question: write a Clojure expression for the marker for the Reagent lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Reagent wraps React with Hiccup-shaped Clojure data\" :studied)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do "components are functions returning Hiccup vectors" :reagent)` • **expected**: `':reagent'`

**concept_phrase**: `how Reagent components are written`

**question_what**: `the marker keyword for Reagent components`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Frank had been trying to teach Will how the REPL
works. "Look here," he said, pointing to how Reagent components are written.
"You hand the form `(do "components are functions returning Hiccup vectors" :reagent)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Will, drowsy from the warm sun, agreed to try.

Question: write a Clojure expression for the marker keyword for Reagent components.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"components are functions returning Hiccup vectors\" :reagent)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the Reagent wrapper around React`

**question_what**: `the marker for the Reagent lesson`

```
The boy on the hill thought the trick clever the first time he played it. This was by the orchard.

Frank had been trying to teach Pat how the REPL
works. "Look here," he said, pointing to the Reagent wrapper around React.
"You hand the form `(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Pat, drowsy from the warm sun, agreed to try.

Write a form whose evaluation gives the marker for the Reagent lesson.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Reagent wraps React with Hiccup-shaped Clojure data\" :studied)"}}]}
```

---

## G12-17: Library design patterns

**Examples:** 3 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 3

**form**: `(do "good libraries expose data, then functions, then macros sparingly" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the Clojure library-design hierarchy`

**question_what**: `the marker for the library-design lesson`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place by the forest.

Grace had filled an entire notebook over the long season with
tools and patterns: transducers, channels, specs, tests. in the forest, the
next entry was the Clojure library-design hierarchy, and the form was `(do "good libraries expose data, then functions, then macros sparingly" :studied)`.
Will, regretting every careless step but more reflective than usual,
agreed to write the form into the REPL.

Question: write a Clojure expression for the marker for the library-design lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"good libraries expose data, then functions, then macros sparingly\" :studied)"}}]}
```

### Record 2 — example 2 of 3

**form**: `(do "small public API surface, plain data inputs, return values" :design)` • **expected**: `':design'`

**concept_phrase**: `the conventional Clojure API shape`

**question_what**: `the marker keyword for the API-shape lesson`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place by the forest.

A wooden notice nailed to a post by the forest carried a small puzzle. The
riddle simply asked the reader to evaluate `(do "small public API surface, plain data inputs, return values" :design)`. Tom
laughed, swaggering through the underbrush, and declared it too easy to bother with.
George said, patiently, that the only way to be certain of
the conventional Clojure API shape was to put it in the REPL.

Write a form whose evaluation gives the marker keyword for the API-shape lesson.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"small public API surface, plain data inputs, return values\" :design)"}}]}
```

### Record 3 — example 3 of 3

**form**: `(= [1 2 3] (vec '(1 2 3)))` • **expected**: `True`

**concept_phrase**: `a tiny example of a data-first conversion at the API edge`

**question_what**: `whether the vector and the converted seq are equal`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Jess, lulled by the gentle wind from a season of false alarms long
since outgrown, was finally willing to study patterns. Oliver
pointed in the forest at a tiny example of a data-first conversion at the API edge. The form `(= [1 2 3] (vec '(1 2 3)))` was the
canonical example; the REPL would confirm what it produced.

Write a form whose evaluation gives whether the vector and the converted seq are equal.

---

{"tool_calls":[{"name":"eval","args":{"form":"(= [1 2 3] (vec '(1 2 3)))"}}]}
```

### Record 4 — example 1 of 3

**form**: `(do "good libraries expose data, then functions, then macros sparingly" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the Clojure library-design hierarchy`

**question_what**: `the marker for the library-design lesson`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened at the edge of the forest.

Halfway through the morning watch, Jess called out
in the forest, demanding a verdict on the form `(do "good libraries expose data, then functions, then macros sparingly" :studied)` and refusing
to descend until somebody confirmed it. Jess insisted
she already knew the answer. Carol, walking up
at an unhurried pace, simply said: "Submit the Clojure library-design hierarchy to the
REPL. Whatever comes back is the answer."

Write a form whose evaluation gives the marker for the library-design lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"good libraries expose data, then functions, then macros sparingly\" :studied)"}}]}
```

### Record 5 — example 2 of 3

**form**: `(do "small public API surface, plain data inputs, return values" :design)` • **expected**: `':design'`

**concept_phrase**: `the conventional Clojure API shape`

**question_what**: `the marker keyword for the API-shape lesson`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place near the forest.

A wooden notice nailed to a post by the forest carried a small puzzle. The
riddle simply asked the reader to evaluate `(do "small public API surface, plain data inputs, return values" :design)`. Will
laughed, with a smug grin, and declared it too easy to bother with.
Morgan said, patiently, that the only way to be certain of
the conventional Clojure API shape was to put it in the REPL.

Write a form whose evaluation gives the marker keyword for the API-shape lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"small public API surface, plain data inputs, return values\" :design)"}}]}
```

---

## G12-18: Clojure style guide

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do "kebab-case names, two-space indent, threading for deep nests" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the community-style basics`

**question_what**: `the marker for the style-guide lesson`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(do "kebab-case names, two-space indent, threading for deep nests" :studied)`, and the line
above it read the community-style basics. Alice handed the page to
Pat, who, lulled by the gentle wind, agreed to write it out properly.

Write a Clojure expression that computes the marker for the style-guide lesson.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"kebab-case names, two-space indent, threading for deep nests\" :studied)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do "prefer pure functions, name predicates with ?, danger! ops with !" :style)` • **expected**: `':style'`

**concept_phrase**: `two naming conventions from the style guide`

**question_what**: `the marker keyword for the naming-conventions lesson`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Halfway through the morning watch, Jess called out
near the orchard, demanding a verdict on the form `(do "prefer pure functions, name predicates with ?, danger! ops with !" :style)` and refusing
to descend until somebody confirmed it. Jess insisted
she already knew the answer. Robin, walking up
at an unhurried pace, simply said: "Submit two naming conventions from the style guide to the
REPL. Whatever comes back is the answer."

Write a Clojure expression that computes the marker keyword for the naming-conventions lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"prefer pure functions, name predicates with ?, danger! ops with !\" :style)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do "kebab-case names, two-space indent, threading for deep nests" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the community-style basics`

**question_what**: `the marker for the style-guide lesson`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

At the village square near the road, a row of small markers commemorated
the libraries the careful shepherds had learned over the season. The
newest one honoured the community-style basics. Sam touched it and
said the form to remember was `(do "kebab-case names, two-space indent, threading for deep nests" :studied)`; Lou
agreed to submit it.

Write a form whose evaluation gives the marker for the style-guide lesson.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"kebab-case names, two-space indent, threading for deep nests\" :studied)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do "prefer pure functions, name predicates with ?, danger! ops with !" :style)` • **expected**: `':style'`

**concept_phrase**: `two naming conventions from the style guide`

**question_what**: `the marker keyword for the naming-conventions lesson`

```
The boy on the hill thought the trick clever the first time he played it. All this took place near the meadow.

Halfway through the morning watch, Will called out
near the meadow, demanding a verdict on the form `(do "prefer pure functions, name predicates with ?, danger! ops with !" :style)` and refusing
to descend until somebody confirmed it. Will insisted
he already knew the answer. Oliver, walking up
at an unhurried pace, simply said: "Submit two naming conventions from the style guide to the
REPL. Whatever comes back is the answer."

Write a form whose evaluation gives the marker keyword for the naming-conventions lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"prefer pure functions, name predicates with ?, danger! ops with !\" :style)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do "kebab-case names, two-space indent, threading for deep nests" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the community-style basics`

**question_what**: `the marker for the style-guide lesson`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

At the village square by the village, a row of small markers commemorated
the libraries the careful shepherds had learned over the season. The
newest one honoured the community-style basics. Sam touched it and
said the form to remember was `(do "kebab-case names, two-space indent, threading for deep nests" :studied)`; Lou
agreed to submit it.

Write a Clojure expression that computes the marker for the style-guide lesson.

---

I express the pipeline / spec / test as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"kebab-case names, two-space indent, threading for deep nests\" :studied)"}}]}
```

---

