# Boy-wolf Grade 11 — deep spot-check

5 generated records per subject (across all examples and a variety of seeds). Read every record carefully. Flag anything that reads odd to a careful reader, including issues the structural audit can't catch (prose flow, contextual fit, cliché repetition, subplot/example mismatch, etc.)

---

## G11-01: JVM vs CLR vs JS vs Python (host overview)

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the idea that Clojure has multiple host runtimes`

**question_what**: `the marker value when the host overview has been studied`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Pat insisted the foreign-runtime forms were "just like
home." Alice tapped a stone near the woods where someone had
inscribed the idea that Clojure has multiple host runtimes. "Then write `(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)` into the REPL,"
Alice said, "and we'll see if your familiarity holds."

Write a Clojure expression that computes the marker value when the host overview has been studied.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Clojure runs on multiple hosts: JVM, CLR, JS, Python\" :studied)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScript; Python: basilisp" :hosts)` • **expected**: `':hosts'`

**concept_phrase**: `the family of Clojure host runtimes`

**question_what**: `the marker keyword for the host family`

```
The boy on the hill thought the trick clever the first time he played it.

The elder of the village kept a small slate in the village, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the family of Clojure host runtimes. Sam read
out the form `(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScript; Python: basilisp" :hosts)` so Lou could write it
properly into the REPL and earn an honest mark on the slate.

Write a Clojure expression that computes the marker keyword for the host family.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"JVM: Clojure; CLR: ClojureCLR; JS: ClojureScript; Python: basilisp\" :hosts)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the idea that Clojure has multiple host runtimes`

**question_what**: `the marker value when the host overview has been studied`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Frank had been trying to teach Pat how the REPL
works. "Look here," he said, pointing to the idea that Clojure has multiple host runtimes.
"You hand the form `(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Pat, drowsy from the warm sun, agreed to try.

Write a Clojure expression that computes the marker value when the host overview has been studied.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Clojure runs on multiple hosts: JVM, CLR, JS, Python\" :studied)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScript; Python: basilisp" :hosts)` • **expected**: `':hosts'`

**concept_phrase**: `the family of Clojure host runtimes`

**question_what**: `the marker keyword for the host family`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden border-post by the orchard marked the edge of the host runtime's
territory. The form written on it — `(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScript; Python: basilisp" :hosts)` — captured
the family of Clojure host runtimes. Pat, weary from the morning's effort from a morning of false
calls, agreed for once that crossing into foreign syntax called for
actual evaluation, not guessing.

What Clojure form computes the marker keyword for the host family? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"JVM: Clojure; CLR: ClojureCLR; JS: ClojureScript; Python: basilisp\" :hosts)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the idea that Clojure has multiple host runtimes`

**question_what**: `the marker value when the host overview has been studied`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Lou called down from a stone on the road where someone had
chalked the idea that Clojure has multiple host runtimes on a flat board. Lou, with great whoops of laughter,
declared she already knew what would come back. Alex,
stepping deliberately, asked her to actually submit the form
`(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)` to the REPL — the village had stopped trusting answers
that weren't checked.

What Clojure form computes the marker value when the host overview has been studied? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Clojure runs on multiple hosts: JVM, CLR, JS, Python\" :studied)"}}]}
```

---

## G11-02: Method call syntax

**Examples:** 3 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 3

**form**: `(.toUpperCase "abc")` • **expected**: `'ABC'`

**concept_phrase**: `the method call (.toUpperCase "abc")`

**question_what**: `the uppercased string returned by the method`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Will called down from a stone by the orchard where someone had
chalked the method call (.toUpperCase "abc") on a flat board. Will, with a smug grin,
declared he already knew what would come back. Morgan,
stepping deliberately, asked him to actually submit the form
`(.toUpperCase "abc")` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a form whose evaluation gives the uppercased string returned by the method.

---

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
```

### Record 2 — example 2 of 3

**form**: `(.startsWith "shepherd-elder" "shepherd")` • **expected**: `True`

**concept_phrase**: `a method call (.startsWith ...) returning a boolean`

**question_what**: `whether the string starts with the prefix`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place by the woods.

A merchant's stall at the edge of the woods sold translated phrasebooks for the host
language; today's lesson was a method call (.startsWith ...) returning a boolean. Grace copied
the form `(.startsWith "shepherd-elder" "shepherd")` from the page, and Tom agreed
that, on this side of the river, one should always check the REPL
before trusting a translation.

Write a Clojure expression that computes whether the string starts with the prefix.

---

{"tool_calls":[{"name":"eval","args":{"form":"(.startsWith \"shepherd-elder\" \"shepherd\")"}}]}
```

### Record 3 — example 3 of 3

**form**: `(. "abc" toUpperCase)` • **expected**: `'ABC'`

**concept_phrase**: `the alternate dot form (. obj method)`

**question_what**: `the uppercased result via the longer dot syntax`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden border-post at the edge of the orchard marked the edge of the host runtime's
territory. The form written on it — `(. "abc" toUpperCase)` — captured
the alternate dot form (. obj method). Pat, yawning at the soft moss from a morning of false
calls, agreed for once that crossing into foreign syntax called for
actual evaluation, not guessing.

Write a Clojure expression that computes the uppercased result via the longer dot syntax.

---

{"tool_calls":[{"name":"eval","args":{"form":"(. \"abc\" toUpperCase)"}}]}
```

### Record 4 — example 1 of 3

**form**: `(.toUpperCase "abc")` • **expected**: `'ABC'`

**concept_phrase**: `the method call (.toUpperCase "abc")`

**question_what**: `the uppercased string returned by the method`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place by the orchard.

A merchant's stall near the orchard sold translated phrasebooks for the host
language; today's lesson was the method call (.toUpperCase "abc"). Carol copied
the form `(.toUpperCase "abc")` from the page, and Pat agreed
that, on this side of the river, one should always check the REPL
before trusting a translation.

Write a Clojure expression that computes the uppercased string returned by the method.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
```

### Record 5 — example 2 of 3

**form**: `(.startsWith "shepherd-elder" "shepherd")` • **expected**: `True`

**concept_phrase**: `a method call (.startsWith ...) returning a boolean`

**question_what**: `whether the string starts with the prefix`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place by the farm.

A merchant's stall in the farm sold translated phrasebooks for the host
language; today's lesson was a method call (.startsWith ...) returning a boolean. Grace copied
the form `(.startsWith "shepherd-elder" "shepherd")` from the page, and Tom agreed
that, on this side of the river, one should always check the REPL
before trusting a translation.

Write a Clojure expression that computes whether the string starts with the prefix.

---

{"tool_calls":[{"name":"eval","args":{"form":"(.startsWith \"shepherd-elder\" \"shepherd\")"}}]}
```

---

## G11-03: Static method call

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(Math/abs -7)` • **expected**: `7`

**concept_phrase**: `the static call (Math/abs -7)`

**question_what**: `the absolute value of -7 via the static method`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place at the edge of the village.

A small crowd of villagers had gathered near the village to watch
Will attempt to predict, off the cuff, what the REPL would
return. Alice pointed to the static call (Math/abs -7) and read out the
form aloud: `(Math/abs -7)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a Clojure expression that computes the absolute value of -7 via the static method.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(Math/abs -7)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(Math/max 3 9)` • **expected**: `9`

**concept_phrase**: `the static call (Math/max 3 9)`

**question_what**: `the larger of 3 and 9 via the static method`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened near the meadow.

Halfway through the morning watch, Lou called out
near the meadow, demanding a verdict on the form `(Math/max 3 9)` and refusing
to descend until somebody confirmed it. Lou insisted
she already knew the answer. Oliver, walking up
at an unhurried pace, simply said: "Submit the static call (Math/max 3 9) to the
REPL. Whatever comes back is the answer."

Write a form whose evaluation gives the larger of 3 and 9 via the static method.

---

I write the interop form using the host's convention.

{"tool_calls":[{"name":"eval","args":{"form":"(Math/max 3 9)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(Math/abs -7)` • **expected**: `7`

**concept_phrase**: `the static call (Math/abs -7)`

**question_what**: `the absolute value of -7 via the static method`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A wooden notice nailed to a post by the farm carried a small puzzle. The
riddle simply asked the reader to evaluate `(Math/abs -7)`. Pat
laughed, with great whoops of laughter, and declared it too easy to bother with.
Frank said, patiently, that the only way to be certain of
the static call (Math/abs -7) was to put it in the REPL.

Write a Clojure expression that computes the absolute value of -7 via the static method.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(Math/abs -7)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(Math/max 3 9)` • **expected**: `9`

**concept_phrase**: `the static call (Math/max 3 9)`

**question_what**: `the larger of 3 and 9 via the static method`

```
The boy on the hill thought the trick clever the first time he played it.

The elder of the village kept a small slate near the village, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the static call (Math/max 3 9). Bob read
out the form `(Math/max 3 9)` so Will could write it
properly into the REPL and earn an honest mark on the slate.

What Clojure form computes the larger of 3 and 9 via the static method? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(Math/max 3 9)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(Math/abs -7)` • **expected**: `7`

**concept_phrase**: `the static call (Math/abs -7)`

**question_what**: `the absolute value of -7 via the static method`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A merchant's stall by the village sold translated phrasebooks for the host
language; today's lesson was the static call (Math/abs -7). Robin copied
the form `(Math/abs -7)` from the page, and Will agreed
that, on this side of the river, one should always check the REPL
before trusting a translation.

Write a Clojure expression that computes the absolute value of -7 via the static method.

---

{"tool_calls":[{"name":"eval","args":{"form":"(Math/abs -7)"}}]}
```

---

## G11-04: Field access

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(count "shepherd")` • **expected**: `8`

**concept_phrase**: `the count of "shepherd" — host-portable length`

**question_what**: `the length of "shepherd"`

```
The boy on the hill thought the trick clever the first time he played it.

At a wayside shrine near the farm dedicated to interop, the day's offering
was the count of "shepherd" — host-portable length. Bob knelt and placed the form
`(count "shepherd")` on the stone. Pat, watching, agreed to be the
one to submit it to the runtime.

Write a Clojure expression that computes the length of "shepherd".

---

I use the dot or slash form for the host method, then submit.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"shepherd\")"}}]}
```

### Record 2 — example 2 of 2

**form**: `(count "flock")` • **expected**: `5`

**concept_phrase**: `the count of "flock"`

**question_what**: `the length of "flock"`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened at the edge of the village.

A merchant's stall near the village sold translated phrasebooks for the host
language; today's lesson was the count of "flock". George copied
the form `(count "flock")` from the page, and Jess agreed
that, on this side of the river, one should always check the REPL
before trusting a translation.

Write a Clojure expression that computes the length of "flock".

---

{"tool_calls":[{"name":"eval","args":{"form":"(count \"flock\")"}}]}
```

### Record 3 — example 1 of 2

**form**: `(count "shepherd")` • **expected**: `8`

**concept_phrase**: `the count of "shepherd" — host-portable length`

**question_what**: `the length of "shepherd"`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

"This is not our meadow," Sam said near the road, with steady, careful steps.
"Here, the methods belong to objects, and the dot has a particular
meaning." Tom, swaggering through the underbrush, said he
could read the foreign form anyway. Sam sketched `(count "shepherd")`
on the ground; let the runtime, they insisted, declare what
the count of "shepherd" — host-portable length returned.

Write a Clojure expression that computes the length of "shepherd".

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"shepherd\")"}}]}
```

### Record 4 — example 2 of 2

**form**: `(count "flock")` • **expected**: `5`

**concept_phrase**: `the count of "flock"`

**question_what**: `the length of "flock"`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden notice nailed to a post at the edge of the orchard carried a small puzzle. The
riddle simply asked the reader to evaluate `(count "flock")`. Tom
laughed, puffed up with pride, and declared it too easy to bother with.
Bob said, patiently, that the only way to be certain of
the count of "flock" was to put it in the REPL.

Write a form whose evaluation gives the length of "flock".

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"flock\")"}}]}
```

### Record 5 — example 1 of 2

**form**: `(count "shepherd")` • **expected**: `8`

**concept_phrase**: `the count of "shepherd" — host-portable length`

**question_what**: `the length of "shepherd"`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place at the edge of the orchard.

A small crowd of villagers had gathered near the orchard to watch
Lou attempt to predict, off the cuff, what the REPL would
return. Oliver pointed to the count of "shepherd" — host-portable length and read out the
form aloud: `(count "shepherd")`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

What Clojure form computes the length of "shepherd"? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"shepherd\")"}}]}
```

---

## G11-05: Import form

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do "(:import (java.util Date)) imports a host class" :imported)` • **expected**: `':imported'`

**concept_phrase**: `the (:import ...) ns clause for host classes`

**question_what**: `the marker for the import-form lesson`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

"There is no need to evaluate that," Jess said, swaggering through the underbrush.
"Anyone can see what the (:import ...) ns clause for host classes comes to." Alice, who
near the hilltop had heard such claims many times, asked her to
actually write the form `(do "(:import (java.util Date)) imports a host class" :imported)` and submit it to the REPL —
just to be sure.

Question: write a Clojure expression for the marker for the import-form lesson.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(:import (java.util Date)) imports a host class\" :imported)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do "import is a top-of-file ns clause" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the role of import in a Clojure file`

**question_what**: `the marker for studying import`

```
The boy on the hill thought the trick clever the first time he played it.

A wooden border-post in the forest marked the edge of the host runtime's
territory. The form written on it — `(do "import is a top-of-file ns clause" :studied)` — captured
the role of import in a Clojure file. Tom, drowsy from the warm sun from a morning of false
calls, agreed for once that crossing into foreign syntax called for
actual evaluation, not guessing.

What Clojure form computes the marker for studying import? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"import is a top-of-file ns clause\" :studied)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do "(:import (java.util Date)) imports a host class" :imported)` • **expected**: `':imported'`

**concept_phrase**: `the (:import ...) ns clause for host classes`

**question_what**: `the marker for the import-form lesson`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place at the edge of the orchard.

Halfway through the morning watch, Jess called out
in the orchard, demanding a verdict on the form `(do "(:import (java.util Date)) imports a host class" :imported)` and refusing
to descend until somebody confirmed it. Jess insisted
she already knew the answer. Grace, walking up
at an unhurried pace, simply said: "Submit the (:import ...) ns clause for host classes to the
REPL. Whatever comes back is the answer."

Write a form whose evaluation gives the marker for the import-form lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(:import (java.util Date)) imports a host class\" :imported)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do "import is a top-of-file ns clause" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the role of import in a Clojure file`

**question_what**: `the marker for studying import`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden border-post in the farm marked the edge of the host runtime's
territory. The form written on it — `(do "import is a top-of-file ns clause" :studied)` — captured
the role of import in a Clojure file. Lou, weary from the morning's effort from a morning of false
calls, agreed for once that crossing into foreign syntax called for
actual evaluation, not guessing.

Question: write a Clojure expression for the marker for studying import.

---

I use the dot or slash form for the host method, then submit.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"import is a top-of-file ns clause\" :studied)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do "(:import (java.util Date)) imports a host class" :imported)` • **expected**: `':imported'`

**concept_phrase**: `the (:import ...) ns clause for host classes`

**question_what**: `the marker for the import-form lesson`

```
The boy on the hill thought the trick clever the first time he played it.

A wooden border-post at the edge of the farm marked the edge of the host runtime's
territory. The form written on it — `(do "(:import (java.util Date)) imports a host class" :imported)` — captured
the (:import ...) ns clause for host classes. Jess, yawning at the soft moss from a morning of false
calls, agreed for once that crossing into foreign syntax called for
actual evaluation, not guessing.

What Clojure form computes the marker for the import-form lesson? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(:import (java.util Date)) imports a host class\" :imported)"}}]}
```

---

## G11-06: new and dot-construct

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(String. "hello")` • **expected**: `'hello'`

**concept_phrase**: `the constructor call (String. "hello")`

**question_what**: `the string built by the dot-construct`

```
The boy on the hill thought the trick clever the first time he played it.

At a wayside shrine atop the hilltop dedicated to interop, the day's offering
was the constructor call (String. "hello"). Frank knelt and placed the form
`(String. "hello")` on the stone. Will, watching, agreed to be the
one to submit it to the runtime.

Write a Clojure expression that computes the string built by the dot-construct.

---

{"tool_calls":[{"name":"eval","args":{"form":"(String. \"hello\")"}}]}
```

### Record 2 — example 2 of 2

**form**: `(new String "world")` • **expected**: `'world'`

**concept_phrase**: `the (new String "world") form`

**question_what**: `the string built by (new ...)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

"There is no need to evaluate that," Pat said, with a smug grin.
"Anyone can see what the (new String "world") form comes to." Robin, who
near the woods had heard such claims many times, asked them to
actually write the form `(new String "world")` and submit it to the REPL —
just to be sure.

What Clojure form computes the string built by (new ...)? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(new String \"world\")"}}]}
```

### Record 3 — example 1 of 2

**form**: `(String. "hello")` • **expected**: `'hello'`

**concept_phrase**: `the constructor call (String. "hello")`

**question_what**: `the string built by the dot-construct`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A wooden border-post atop the hilltop marked the edge of the host runtime's
territory. The form written on it — `(String. "hello")` — captured
the constructor call (String. "hello"). Jess, yawning at the soft moss from a morning of false
calls, agreed for once that crossing into foreign syntax called for
actual evaluation, not guessing.

Question: write a Clojure expression for the string built by the dot-construct.

---

{"tool_calls":[{"name":"eval","args":{"form":"(String. \"hello\")"}}]}
```

### Record 4 — example 2 of 2

**form**: `(new String "world")` • **expected**: `'world'`

**concept_phrase**: `the (new String "world") form`

**question_what**: `the string built by (new ...)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A wooden notice nailed to a post by the orchard carried a small puzzle. The
riddle simply asked the reader to evaluate `(new String "world")`. Pat
laughed, puffed up with pride, and declared it too easy to bother with.
Robin said, patiently, that the only way to be certain of
the (new String "world") form was to put it in the REPL.

Write a Clojure expression that computes the string built by (new ...).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(new String \"world\")"}}]}
```

### Record 5 — example 1 of 2

**form**: `(String. "hello")` • **expected**: `'hello'`

**concept_phrase**: `the constructor call (String. "hello")`

**question_what**: `the string built by the dot-construct`

```
Every shepherd in the valley knew the danger of crying wolf for sport. It happened along the road.

George kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the road the next entry was
the constructor call (String. "hello"). Will peered over his shoulder
at the form `(String. "hello")` and was asked, gently, to be the one to
submit it.

What Clojure form computes the string built by the dot-construct? Submit it via `eval`.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(String. \"hello\")"}}]}
```

---

## G11-07: Arrays

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(let [a (int-array [10 20 30])] (aget a 1))` • **expected**: `20`

**concept_phrase**: `indexing into an int-array via aget`

**question_what**: `the value at index 1 of the array`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(let [a (int-array [10 20 30])] (aget a 1))`, and the line
above it read indexing into an int-array via aget. Robin handed the page to
Tom, who, lulled by the gentle wind, agreed to write it out properly.

What Clojure form computes the value at index 1 of the array? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a (int-array [10 20 30])] (aget a 1))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(let [a (int-array [1 2 3])] (alength a))` • **expected**: `3`

**concept_phrase**: `the length of an int-array via alength`

**question_what**: `the length of the array`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place near the meadow.

A wooden border-post by the meadow marked the edge of the host runtime's
territory. The form written on it — `(let [a (int-array [1 2 3])] (alength a))` — captured
the length of an int-array via alength. Jess, drowsy from the warm sun from a morning of false
calls, agreed for once that crossing into foreign syntax called for
actual evaluation, not guessing.

Write a Clojure expression that computes the length of the array.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a (int-array [1 2 3])] (alength a))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(let [a (int-array [10 20 30])] (aget a 1))` • **expected**: `20`

**concept_phrase**: `indexing into an int-array via aget`

**question_what**: `the value at index 1 of the array`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place on the hilltop.

Oliver and Will had wandered at the edge of the hilltop into territory
where the REPL spoke to another runtime entirely. Oliver read the
sign and pointed at indexing into an int-array via aget; the form to submit, written in
the foreign convention, was `(let [a (int-array [10 20 30])] (aget a 1))`.

What Clojure form computes the value at index 1 of the array? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a (int-array [10 20 30])] (aget a 1))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(let [a (int-array [1 2 3])] (alength a))` • **expected**: `3`

**concept_phrase**: `the length of an int-array via alength`

**question_what**: `the length of the array`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

"There is no need to evaluate that," Tom said, with a smug grin.
"Anyone can see what the length of an int-array via alength comes to." Alex, who
in the orchard had heard such claims many times, asked him to
actually write the form `(let [a (int-array [1 2 3])] (alength a))` and submit it to the REPL —
just to be sure.

Write a Clojure expression that computes the length of the array.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a (int-array [1 2 3])] (alength a))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(let [a (int-array [10 20 30])] (aget a 1))` • **expected**: `20`

**concept_phrase**: `indexing into an int-array via aget`

**question_what**: `the value at index 1 of the array`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

George kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the farm the next entry was
indexing into an int-array via aget. Jess peered over his shoulder
at the form `(let [a (int-array [10 20 30])] (aget a 1))` and was asked, gently, to be the one to
submit it.

What Clojure form computes the value at index 1 of the array? Submit it via `eval`.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a (int-array [10 20 30])] (aget a 1))"}}]}
```

---

## G11-08: Type hints

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(let [^String s "abc"] (.toUpperCase s))` • **expected**: `'ABC'`

**concept_phrase**: `a let-binding with a ^String type hint`

**question_what**: `the uppercased string after a type-hinted binding`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened near the orchard.

At a wayside shrine in the orchard dedicated to interop, the day's offering
was a let-binding with a ^String type hint. Oliver knelt and placed the form
`(let [^String s "abc"] (.toUpperCase s))` on the stone. Tom, watching, agreed to be the
one to submit it to the runtime.

Write a form whose evaluation gives the uppercased string after a type-hinted binding.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(let [^String s \"abc\"] (.toUpperCase s))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do "type hints are metadata that guide compilation" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the role of ^Type metadata as a hint`

**question_what**: `the marker keyword for the type-hint lesson`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened by the orchard.

Alex and Pat had wandered by the orchard into territory
where the REPL spoke to another runtime entirely. Alex read the
sign and pointed at the role of ^Type metadata as a hint; the form to submit, written in
the foreign convention, was `(do "type hints are metadata that guide compilation" :studied)`.

Write a Clojure expression that computes the marker keyword for the type-hint lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"type hints are metadata that guide compilation\" :studied)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(let [^String s "abc"] (.toUpperCase s))` • **expected**: `'ABC'`

**concept_phrase**: `a let-binding with a ^String type hint`

**question_what**: `the uppercased string after a type-hinted binding`

```
The boy on the hill thought the trick clever the first time he played it. It happened at the edge of the farm.

Will insisted the foreign-runtime forms were "just like
home." Grace tapped a stone near the farm where someone had
inscribed a let-binding with a ^String type hint. "Then write `(let [^String s "abc"] (.toUpperCase s))` into the REPL,"
Grace said, "and we'll see if your familiarity holds."

Write a Clojure expression that computes the uppercased string after a type-hinted binding.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [^String s \"abc\"] (.toUpperCase s))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do "type hints are metadata that guide compilation" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the role of ^Type metadata as a hint`

**question_what**: `the marker keyword for the type-hint lesson`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place in the meadow.

A wooden notice nailed to a post near the meadow carried a small puzzle. The
riddle simply asked the reader to evaluate `(do "type hints are metadata that guide compilation" :studied)`. Tom
laughed, with a smug grin, and declared it too easy to bother with.
Sam said, patiently, that the only way to be certain of
the role of ^Type metadata as a hint was to put it in the REPL.

Write a Clojure expression that computes the marker keyword for the type-hint lesson.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"type hints are metadata that guide compilation\" :studied)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(let [^String s "abc"] (.toUpperCase s))` • **expected**: `'ABC'`

**concept_phrase**: `a let-binding with a ^String type hint`

**question_what**: `the uppercased string after a type-hinted binding`

```
The boy on the hill thought the trick clever the first time he played it.

"This is not our meadow," Oliver said by the orchard, untroubled by what others thought.
"Here, the methods belong to objects, and the dot has a particular
meaning." Pat, with great whoops of laughter, said they
could read the foreign form anyway. Oliver sketched `(let [^String s "abc"] (.toUpperCase s))`
on the ground; let the runtime, he insisted, declare what
a let-binding with a ^String type hint returned.

Write a Clojure expression that computes the uppercased string after a type-hinted binding.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [^String s \"abc\"] (.toUpperCase s))"}}]}
```

---

## G11-09: Checked vs unchecked math

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(+ 1 2)` • **expected**: `3`

**concept_phrase**: `the form (+ 1 2) under default checked math`

**question_what**: `the result of (+ 1 2) under the default math regime`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place in the woods.

"There is no need to evaluate that," Will said, as if the race were already won.
"Anyone can see what the form (+ 1 2) under default checked math comes to." George, who
at the edge of the woods had heard such claims many times, asked him to
actually write the form `(+ 1 2)` and submit it to the REPL —
just to be sure.

Question: write a Clojure expression for the result of (+ 1 2) under the default math regime.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do "*unchecked-math* turns off overflow checking on prims" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the *unchecked-math* dynamic var`

**question_what**: `the marker for the checked/unchecked lesson`

```
The boy on the hill thought the trick clever the first time he played it.

Alice and Pat had wandered by the forest into territory
where the REPL spoke to another runtime entirely. Alice read the
sign and pointed at the *unchecked-math* dynamic var; the form to submit, written in
the foreign convention, was `(do "*unchecked-math* turns off overflow checking on prims" :studied)`.

Write a form whose evaluation gives the marker for the checked/unchecked lesson.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"*unchecked-math* turns off overflow checking on prims\" :studied)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(+ 1 2)` • **expected**: `3`

**concept_phrase**: `the form (+ 1 2) under default checked math`

**question_what**: `the result of (+ 1 2) under the default math regime`

```
The boy on the hill thought the trick clever the first time he played it.

At a wayside shrine in the orchard dedicated to interop, the day's offering
was the form (+ 1 2) under default checked math. Morgan knelt and placed the form
`(+ 1 2)` on the stone. Jess, watching, agreed to be the
one to submit it to the runtime.

Write a Clojure expression that computes the result of (+ 1 2) under the default math regime.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do "*unchecked-math* turns off overflow checking on prims" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the *unchecked-math* dynamic var`

**question_what**: `the marker for the checked/unchecked lesson`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

"There is no need to evaluate that," Pat said, with great whoops of laughter.
"Anyone can see what the *unchecked-math* dynamic var comes to." Carol, who
at the edge of the woods had heard such claims many times, asked them to
actually write the form `(do "*unchecked-math* turns off overflow checking on prims" :studied)` and submit it to the REPL —
just to be sure.

Write a form whose evaluation gives the marker for the checked/unchecked lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"*unchecked-math* turns off overflow checking on prims\" :studied)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(+ 1 2)` • **expected**: `3`

**concept_phrase**: `the form (+ 1 2) under default checked math`

**question_what**: `the result of (+ 1 2) under the default math regime`

```
The boy on the hill thought the trick clever the first time he played it.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(+ 1 2)`, and the line
above it read the form (+ 1 2) under default checked math. George handed the page to
Tom, who, yawning at the soft moss, agreed to write it out properly.

Question: write a Clojure expression for the result of (+ 1 2) under the default math regime.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

---

## G11-10: ClojureScript overview

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the ClojureScript host overview`

**question_what**: `the marker for studying the cljs host`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Lou called down from a stone atop the hilltop where someone had
chalked the ClojureScript host overview on a flat board. Lou, boasting at every turn,
declared she already knew what would come back. Grace,
with steady, careful steps, asked her to actually submit the form
`(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the marker for studying the cljs host.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"ClojureScript compiles to JavaScript via the Closure compiler\" :studied)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do "cljs runs in browsers and Node, with JS interop syntax" :cljs)` • **expected**: `':cljs'`

**concept_phrase**: `where ClojureScript runs and how interop looks`

**question_what**: `the marker for the cljs-runtime lesson`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. This was near the orchard.

"This is not our meadow," Carol said near the orchard, saying very little.
"Here, the methods belong to objects, and the dot has a particular
meaning." Pat, with a smug grin, said they
could read the foreign form anyway. Carol sketched `(do "cljs runs in browsers and Node, with JS interop syntax" :cljs)`
on the ground; let the runtime, she insisted, declare what
where ClojureScript runs and how interop looks returned.

Question: write a Clojure expression for the marker for the cljs-runtime lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"cljs runs in browsers and Node, with JS interop syntax\" :cljs)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the ClojureScript host overview`

**question_what**: `the marker for studying the cljs host`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Halfway through the morning watch, Tom called out
on the hilltop, demanding a verdict on the form `(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)` and refusing
to descend until somebody confirmed it. Tom insisted
he already knew the answer. Alice, walking up
at an unhurried pace, simply said: "Submit the ClojureScript host overview to the
REPL. Whatever comes back is the answer."

What Clojure form computes the marker for studying the cljs host? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"ClojureScript compiles to JavaScript via the Closure compiler\" :studied)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do "cljs runs in browsers and Node, with JS interop syntax" :cljs)` • **expected**: `':cljs'`

**concept_phrase**: `where ClojureScript runs and how interop looks`

**question_what**: `the marker for the cljs-runtime lesson`

```
The boy on the hill thought the trick clever the first time he played it. This was along the road.

A merchant's stall along the road sold translated phrasebooks for the host
language; today's lesson was where ClojureScript runs and how interop looks. Alice copied
the form `(do "cljs runs in browsers and Node, with JS interop syntax" :cljs)` from the page, and Tom agreed
that, on this side of the river, one should always check the REPL
before trusting a translation.

Question: write a Clojure expression for the marker for the cljs-runtime lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"cljs runs in browsers and Node, with JS interop syntax\" :cljs)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the ClojureScript host overview`

**question_what**: `the marker for studying the cljs host`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A merchant's stall by the farm sold translated phrasebooks for the host
language; today's lesson was the ClojureScript host overview. Robin copied
the form `(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)` from the page, and Tom agreed
that, on this side of the river, one should always check the REPL
before trusting a translation.

Write a form whose evaluation gives the marker for studying the cljs host.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"ClojureScript compiles to JavaScript via the Closure compiler\" :studied)"}}]}
```

---

## G11-11: cljs / JavaScript interop

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the cljs-to-js interop syntax`

**question_what**: `the marker for the cljs-js interop lesson`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened in the meadow.

A wooden notice nailed to a post in the meadow carried a small puzzle. The
riddle simply asked the reader to evaluate `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)`. Will
laughed, boasting at every turn, and declared it too easy to bother with.
Bob said, patiently, that the only way to be certain of
the cljs-to-js interop syntax was to put it in the REPL.

Question: write a Clojure expression for the marker for the cljs-js interop lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(js/console.log x) calls a JS global; (.-foo o) reads a JS field\" :studied)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do "js/<name> namespaces JS globals; .- prefix marks field access" :cljs-interop)` • **expected**: `':cljs-interop'`

**concept_phrase**: `two key cljs-js interop conventions`

**question_what**: `the marker keyword for the conventions`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place near the road.

Sam kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the road the next entry was
two key cljs-js interop conventions. Jess peered over their shoulder
at the form `(do "js/<name> namespaces JS globals; .- prefix marks field access" :cljs-interop)` and was asked, gently, to be the one to
submit it.

Write a Clojure expression that computes the marker keyword for the conventions.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"js/<name> namespaces JS globals; .- prefix marks field access\" :cljs-interop)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the cljs-to-js interop syntax`

**question_what**: `the marker for the cljs-js interop lesson`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A wooden border-post in the village marked the edge of the host runtime's
territory. The form written on it — `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)` — captured
the cljs-to-js interop syntax. Will, yawning at the soft moss from a morning of false
calls, agreed for once that crossing into foreign syntax called for
actual evaluation, not guessing.

Write a Clojure expression that computes the marker for the cljs-js interop lesson.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(js/console.log x) calls a JS global; (.-foo o) reads a JS field\" :studied)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do "js/<name> namespaces JS globals; .- prefix marks field access" :cljs-interop)` • **expected**: `':cljs-interop'`

**concept_phrase**: `two key cljs-js interop conventions`

**question_what**: `the marker keyword for the conventions`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. This was on the road.

"This is not our meadow," George said on the road, saying very little.
"Here, the methods belong to objects, and the dot has a particular
meaning." Lou, with great whoops of laughter, said she
could read the foreign form anyway. George sketched `(do "js/<name> namespaces JS globals; .- prefix marks field access" :cljs-interop)`
on the ground; let the runtime, he insisted, declare what
two key cljs-js interop conventions returned.

What Clojure form computes the marker keyword for the conventions? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"js/<name> namespaces JS globals; .- prefix marks field access\" :cljs-interop)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the cljs-to-js interop syntax`

**question_what**: `the marker for the cljs-js interop lesson`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place by the orchard.

Halfway through the morning watch, Lou called out
near the orchard, demanding a verdict on the form `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)` and refusing
to descend until somebody confirmed it. Lou insisted
she already knew the answer. Carol, walking up
at an unhurried pace, simply said: "Submit the cljs-to-js interop syntax to the
REPL. Whatever comes back is the answer."

Write a form whose evaluation gives the marker for the cljs-js interop lesson.

---

I write the interop form using the host's convention.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(js/console.log x) calls a JS global; (.-foo o) reads a JS field\" :studied)"}}]}
```

---

## G11-12: Basilisp overview (Python host)

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the basilisp host overview`

**question_what**: `the marker for studying basilisp`

```
The boy on the hill thought the trick clever the first time he played it. This was near the orchard.

A small crowd of villagers had gathered near the orchard to watch
Jess attempt to predict, off the cuff, what the REPL would
return. Grace pointed to the basilisp host overview and read out the
form aloud: `(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a Clojure expression that computes the marker for studying basilisp.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"basilisp is a Clojure-like Lisp implemented on Python\" :studied)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do "basilisp interops with Python via the same dot-syntax conventions" :basilisp)` • **expected**: `':basilisp'`

**concept_phrase**: `how basilisp does Python interop`

**question_what**: `the marker keyword for basilisp interop`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A small crowd of villagers had gathered in the meadow to watch
Tom attempt to predict, off the cuff, what the REPL would
return. Robin pointed to how basilisp does Python interop and read out the
form aloud: `(do "basilisp interops with Python via the same dot-syntax conventions" :basilisp)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Question: write a Clojure expression for the marker keyword for basilisp interop.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"basilisp interops with Python via the same dot-syntax conventions\" :basilisp)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the basilisp host overview`

**question_what**: `the marker for studying basilisp`

```
The boy on the hill thought the trick clever the first time he played it. It happened along the road.

The elder of the village kept a small slate near the road, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the basilisp host overview. George read
out the form `(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)` so Tom could write it
properly into the REPL and earn an honest mark on the slate.

What Clojure form computes the marker for studying basilisp? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"basilisp is a Clojure-like Lisp implemented on Python\" :studied)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do "basilisp interops with Python via the same dot-syntax conventions" :basilisp)` • **expected**: `':basilisp'`

**concept_phrase**: `how basilisp does Python interop`

**question_what**: `the marker keyword for basilisp interop`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A small slate sat on a flat stone on the road; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(do "basilisp interops with Python via the same dot-syntax conventions" :basilisp)`, and the page
heading read how basilisp does Python interop. Frank nodded at Will to
write the form properly so the slate would carry an honest entry.

Question: write a Clojure expression for the marker keyword for basilisp interop.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"basilisp interops with Python via the same dot-syntax conventions\" :basilisp)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the basilisp host overview`

**question_what**: `the marker for studying basilisp`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A merchant's stall in the farm sold translated phrasebooks for the host
language; today's lesson was the basilisp host overview. Oliver copied
the form `(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)` from the page, and Tom agreed
that, on this side of the river, one should always check the REPL
before trusting a translation.

What Clojure form computes the marker for studying basilisp? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"basilisp is a Clojure-like Lisp implemented on Python\" :studied)"}}]}
```

---

## G11-13: Cross-platform .cljc and reader-conditionals

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the reader-conditional #?(...) form`

**question_what**: `the marker for the reader-conditional lesson`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Pat insisted the foreign-runtime forms were "just like
home." Sam tapped a stone at the edge of the woods where someone had
inscribed the reader-conditional #?(...) form. "Then write `(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)` into the REPL,"
Sam said, "and we'll see if your familiarity holds."

Write a Clojure expression that computes the marker for the reader-conditional lesson.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"#?(:clj … :cljs …) selects a form per host at read time\" :studied)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do ".cljc files share code across multiple hosts" :cljc)` • **expected**: `':cljc'`

**concept_phrase**: `the role of .cljc files`

**question_what**: `the marker keyword for the .cljc lesson`

```
The boy on the hill thought the trick clever the first time he played it.

George had been trying to teach Jess how the REPL
works. "Look here," he said, pointing to the role of .cljc files.
"You hand the form `(do ".cljc files share code across multiple hosts" :cljc)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, drowsy from the warm sun, agreed to try.

Write a Clojure expression that computes the marker keyword for the .cljc lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \".cljc files share code across multiple hosts\" :cljc)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the reader-conditional #?(...) form`

**question_what**: `the marker for the reader-conditional lesson`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened at the edge of the farm.

A small crowd of villagers had gathered in the farm to watch
Tom attempt to predict, off the cuff, what the REPL would
return. Bob pointed to the reader-conditional #?(...) form and read out the
form aloud: `(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

What Clojure form computes the marker for the reader-conditional lesson? Submit it via `eval`.

---

I express the host call as a Clojure form for the REPL.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"#?(:clj … :cljs …) selects a form per host at read time\" :studied)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do ".cljc files share code across multiple hosts" :cljc)` • **expected**: `':cljc'`

**concept_phrase**: `the role of .cljc files`

**question_what**: `the marker keyword for the .cljc lesson`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. This was at the edge of the forest.

The elder of the village kept a small slate near the forest, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the role of .cljc files. Morgan read
out the form `(do ".cljc files share code across multiple hosts" :cljc)` so Lou could write it
properly into the REPL and earn an honest mark on the slate.

Write a Clojure expression that computes the marker keyword for the .cljc lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \".cljc files share code across multiple hosts\" :cljc)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the reader-conditional #?(...) form`

**question_what**: `the marker for the reader-conditional lesson`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Lou called down from a stone near the woods where someone had
chalked the reader-conditional #?(...) form on a flat board. Lou, boasting at every turn,
declared she already knew what would come back. Alex,
stepping deliberately, asked her to actually submit the form
`(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the marker for the reader-conditional lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"#?(:clj … :cljs …) selects a form per host at read time\" :studied)"}}]}
```

---

## G11-14: Debugging host leaks

**Examples:** 2 | **Subplots:** 16 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do "host stack traces leak through interop; learn to read them" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the topic of debugging host-runtime leaks`

**question_what**: `the marker for the host-leaks lesson`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A small crowd of villagers had gathered at the edge of the orchard to watch
Jess attempt to predict, off the cuff, what the REPL would
return. Carol pointed to the topic of debugging host-runtime leaks and read out the
form aloud: `(do "host stack traces leak through interop; learn to read them" :studied)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Question: write a Clojure expression for the marker for the host-leaks lesson.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"host stack traces leak through interop; learn to read them\" :studied)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(try (Math/sqrt 4) (catch Exception _ :err))` • **expected**: `2.0`

**concept_phrase**: `wrapping a host call in try/catch in case it leaks`

**question_what**: `the result when the host call succeeds`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. This was along the road.

Pat insisted the foreign-runtime forms were "just like
home." Grace tapped a stone along the road where someone had
inscribed wrapping a host call in try/catch in case it leaks. "Then write `(try (Math/sqrt 4) (catch Exception _ :err))` into the REPL,"
Grace said, "and we'll see if your familiarity holds."

Question: write a Clojure expression for the result when the host call succeeds.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (Math/sqrt 4) (catch Exception _ :err))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do "host stack traces leak through interop; learn to read them" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the topic of debugging host-runtime leaks`

**question_what**: `the marker for the host-leaks lesson`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Halfway through the morning watch, Will called out
in the woods, demanding a verdict on the form `(do "host stack traces leak through interop; learn to read them" :studied)` and refusing
to descend until somebody confirmed it. Will insisted
he already knew the answer. Morgan, walking up
at an unhurried pace, simply said: "Submit the topic of debugging host-runtime leaks to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the marker for the host-leaks lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"host stack traces leak through interop; learn to read them\" :studied)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(try (Math/sqrt 4) (catch Exception _ :err))` • **expected**: `2.0`

**concept_phrase**: `wrapping a host call in try/catch in case it leaks`

**question_what**: `the result when the host call succeeds`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

"This is not our meadow," Alice said at the edge of the farm, untroubled by what others thought.
"Here, the methods belong to objects, and the dot has a particular
meaning." Tom, with a smug grin, said he
could read the foreign form anyway. Alice sketched `(try (Math/sqrt 4) (catch Exception _ :err))`
on the ground; let the runtime, she insisted, declare what
wrapping a host call in try/catch in case it leaks returned.

Write a Clojure expression that computes the result when the host call succeeds.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (Math/sqrt 4) (catch Exception _ :err))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do "host stack traces leak through interop; learn to read them" :studied)` • **expected**: `':studied'`

**concept_phrase**: `the topic of debugging host-runtime leaks`

**question_what**: `the marker for the host-leaks lesson`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

"There is no need to evaluate that," Jess said, as if the race were already won.
"Anyone can see what the topic of debugging host-runtime leaks comes to." Grace, who
near the woods had heard such claims many times, asked her to
actually write the form `(do "host stack traces leak through interop; learn to read them" :studied)` and submit it to the REPL —
just to be sure.

What Clojure form computes the marker for the host-leaks lesson? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"host stack traces leak through interop; learn to read them\" :studied)"}}]}
```

---

