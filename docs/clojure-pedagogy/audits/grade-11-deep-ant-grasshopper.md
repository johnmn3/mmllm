# Deep spot-check: grade 11 ant-grasshopper (5 records per subject)

Manual-review dump for hand-audit. Each subject gets 5 rendered records sampled across different seeds so subplot/character/location variety is visible.

---

## G11-01: JVM vs CLR vs JS vs Python (host overview)

### G11-01 record 1

**form**: `(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently.

Toc the ant and Skip the grasshopper had wandered atop the hilltop into territory
where the REPL spoke to another runtime entirely. Toc read the sign
and pointed at the idea that Clojure has multiple host runtimes; the form to submit, written in the
foreign convention, was `(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)`.

What Clojure form computes the marker value when the host overview has been studied? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Clojure runs on multiple hosts: JVM, CLR, JS, Python\" :studied)"}}]}
```

### G11-01 record 2

**form**: `(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently. It happened in the farm.

Halfway through the morning's work, Hum the grasshopper blocked
Bit the ant's path in the farm and refused to step aside until someone
could prove what the form `(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)` evaluated to. Hum
called it impossible. Bit the ant, walking up at their usual
pace, simply said: "Submit the idea that Clojure has multiple host runtimes to the REPL. Whatever comes
back is the answer."

Write a form whose evaluation gives the marker value when the host overview has been studied.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Clojure runs on multiple hosts: JVM, CLR, JS, Python\" :studied)"}}]}
```

### G11-01 record 3

**form**: `(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)`  •  **expected**: `':studied'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

With a twig, Skip the grasshopper marked out a wager on the hilltop: whoever
guessed the result of `(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)` first would win the right to
choose the next song. Bit the ant, untroubled by what others thought, said it was easier
to ask the REPL about the idea that Clojure has multiple host runtimes than to argue.

Write a form whose evaluation gives the marker value when the host overview has been studied.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Clojure runs on multiple hosts: JVM, CLR, JS, Python\" :studied)"}}]}
```

### G11-01 record 4

**form**: `(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)`  •  **expected**: `':studied'`

```
All summer long, the Ant worked while the Grasshopper sang.

At a wayside shrine by the orchard dedicated to interop, the day's offering
was the idea that Clojure has multiple host runtimes. Bit the ant knelt and placed the form
`(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)` on the stone. Skip, watching, agreed to be the
one to submit it to the runtime.

Write a form whose evaluation gives the marker value when the host overview has been studied.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Clojure runs on multiple hosts: JVM, CLR, JS, Python\" :studied)"}}]}
```

### G11-01 record 5

**form**: `(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently.

Halfway through the morning's work, Skip the grasshopper blocked
Toc the ant's path at the edge of the forest and refused to step aside until someone
could prove what the form `(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)` evaluated to. Skip
called it impossible. Toc the ant, walking up at her usual
pace, simply said: "Submit the idea that Clojure has multiple host runtimes to the REPL. Whatever comes
back is the answer."

Question: write a Clojure expression for the marker value when the host overview has been studied.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Clojure runs on multiple hosts: JVM, CLR, JS, Python\" :studied)"}}]}
```

## G11-02: Method call syntax

### G11-02 record 1

**form**: `(.toUpperCase "abc")`  •  **expected**: `'ABC'`

```
Two creatures of the meadow approached the coming winter very differently.

"There is no need to evaluate that," Chirp the grasshopper said,
with great whoops of laughter. "Anyone can see what the method call (.toUpperCase "abc") comes to."
Bit the ant, who atop the hilltop had grown used to such claims, asked
him to actually write the form `(.toUpperCase "abc")` and
submit it to the REPL — just to be sure.

Question: write a Clojure expression for the uppercased string returned by the method.

---

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
```

### G11-02 record 2

**form**: `(.toUpperCase "abc")`  •  **expected**: `'ABC'`

```
Two creatures of the meadow approached the coming winter very differently.

Bit the ant had been trying to teach Chirp the grasshopper how the REPL
works. "Look here," they said, pointing to the method call (.toUpperCase "abc").
"You hand the form `(.toUpperCase "abc")` to the runtime, and the runtime hands
you back what it evaluates to." Chirp, yawning at the soft moss, agreed to
try.

What Clojure form computes the uppercased string returned by the method? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
```

### G11-02 record 3

**form**: `(.toUpperCase "abc")`  •  **expected**: `'ABC'`

```
All summer long, the Ant worked while the Grasshopper sang. This was near the orchard.

At a wayside shrine by the orchard dedicated to interop, the day's offering
was the method call (.toUpperCase "abc"). Toc the ant knelt and placed the form
`(.toUpperCase "abc")` on the stone. Hum, watching, agreed to be the
one to submit it to the runtime.

Write a Clojure expression that computes the uppercased string returned by the method.

---

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
```

### G11-02 record 4

**form**: `(.toUpperCase "abc")`  •  **expected**: `'ABC'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Toc the ant had been trying to teach Chirp the grasshopper how the REPL
works. "Look here," she said, pointing to the method call (.toUpperCase "abc").
"You hand the form `(.toUpperCase "abc")` to the runtime, and the runtime hands
you back what it evaluates to." Chirp, drowsy from the warm sun, agreed to
try.

Write a Clojure expression that computes the uppercased string returned by the method.

---

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
```

### G11-02 record 5

**form**: `(.toUpperCase "abc")`  •  **expected**: `'ABC'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

A merchant's stall by the orchard sold translated phrasebooks for the host
language; today's lesson was the method call (.toUpperCase "abc"). Tic the ant copied the
form `(.toUpperCase "abc")` from the page, and Skip the grasshopper agreed
(for once) that one should always check the REPL before trusting a
translation.

Write a Clojure expression that computes the uppercased string returned by the method.

---

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
```

## G11-03: Static method call

### G11-03 record 1

**form**: `(Math/abs -7)`  •  **expected**: `7`

```
All summer long, the Ant worked while the Grasshopper sang. All this took place at the edge of the garden.

A small audience of meadow creatures had gathered near the garden to watch
Skip the grasshopper attempt to outwit Tic the ant at reading the
REPL. Tic pointed to the static call (Math/abs -7) and read out the form aloud:
`(Math/abs -7)`. The crowd waited to see who would correctly write the
form to submit.

Question: write a Clojure expression for the absolute value of -7 via the static method.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(Math/abs -7)"}}]}
```

### G11-03 record 2

**form**: `(Math/abs -7)`  •  **expected**: `7`

```
Two creatures of the meadow approached the coming winter very differently.

Skip the grasshopper chalked a wager on a flat slate in the meadow: whoever
predicted the result of `(Math/abs -7)` first would set the next day's
ration. Tic the ant, without complaint, said it would be simpler to type
the form into the REPL than to bicker about the static call (Math/abs -7).

What Clojure form computes the absolute value of -7 via the static method? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(Math/abs -7)"}}]}
```

### G11-03 record 3

**form**: `(Math/abs -7)`  •  **expected**: `7`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

"There is no need to evaluate that," Chirp the grasshopper said,
swaggering through the underbrush. "Anyone can see what the static call (Math/abs -7) comes to."
Bit the ant, who by the garden had grown used to such claims, asked
him to actually write the form `(Math/abs -7)` and
submit it to the REPL — just to be sure.

What Clojure form computes the absolute value of -7 via the static method? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(Math/abs -7)"}}]}
```

### G11-03 record 4

**form**: `(Math/abs -7)`  •  **expected**: `7`

```
Two creatures of the meadow approached the coming winter very differently. It happened by the orchard.

A wooden border-post in the orchard marked the edge of the host runtime's
territory. The form written on it — `(Math/abs -7)` — captured
the static call (Math/abs -7). Skip, weary from the morning's effort, agreed for once that
crossing into foreign syntax called for actual evaluation, not
guessing.

Write a Clojure expression that computes the absolute value of -7 via the static method.

---

{"tool_calls":[{"name":"eval","args":{"form":"(Math/abs -7)"}}]}
```

### G11-03 record 5

**form**: `(Math/abs -7)`  •  **expected**: `7`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Halfway through the morning's work, Chirp the grasshopper blocked
Tic the ant's path by the farm and refused to step aside until someone
could prove what the form `(Math/abs -7)` evaluated to. Chirp
called it impossible. Tic the ant, walking up at his usual
pace, simply said: "Submit the static call (Math/abs -7) to the REPL. Whatever comes
back is the answer."

What Clojure form computes the absolute value of -7 via the static method? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(Math/abs -7)"}}]}
```

## G11-04: Field access

### G11-04 record 1

**form**: `(count "ant")`  •  **expected**: `3`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

A small audience of meadow creatures had gathered on the hilltop to watch
Chirp the grasshopper attempt to outwit Toc the ant at reading the
REPL. Toc pointed to the count of "ant" — host-portable length and read out the form aloud:
`(count "ant")`. The crowd waited to see who would correctly write the
form to submit.

Write a Clojure expression that computes the length of "ant".

---

{"tool_calls":[{"name":"eval","args":{"form":"(count \"ant\")"}}]}
```

### G11-04 record 2

**form**: `(count "ant")`  •  **expected**: `3`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. This was on the hilltop.

Halfway through the morning's work, Chirp the grasshopper blocked
Tic the ant's path near the hilltop and refused to step aside until someone
could prove what the form `(count "ant")` evaluated to. Chirp
called it impossible. Tic the ant, walking up at his usual
pace, simply said: "Submit the count of "ant" — host-portable length to the REPL. Whatever comes
back is the answer."

Write a Clojure expression that computes the length of "ant".

---

{"tool_calls":[{"name":"eval","args":{"form":"(count \"ant\")"}}]}
```

### G11-04 record 3

**form**: `(count "ant")`  •  **expected**: `3`

```
Two creatures of the meadow approached the coming winter very differently.

Tic the ant had been trying to teach Skip the grasshopper how the REPL
works. "Look here," he said, pointing to the count of "ant" — host-portable length.
"You hand the form `(count "ant")` to the runtime, and the runtime hands
you back what it evaluates to." Skip, weary from the morning's effort, agreed to
try.

What Clojure form computes the length of "ant"? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"ant\")"}}]}
```

### G11-04 record 4

**form**: `(count "ant")`  •  **expected**: `3`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Toc the ant had been keeping a small leather notebook of every form
she had successfully evaluated. Today in the orchard, the next entry
was the count of "ant" — host-portable length. Chirp the grasshopper peered over
her shoulder at the form `(count "ant")` and asked what it
would come out to.

Write a Clojure expression that computes the length of "ant".

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"ant\")"}}]}
```

### G11-04 record 5

**form**: `(count "ant")`  •  **expected**: `3`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. All this took place in the orchard.

A wooden border-post by the orchard marked the edge of the host runtime's
territory. The form written on it — `(count "ant")` — captured
the count of "ant" — host-portable length. Skip, drowsy from the warm sun, agreed for once that
crossing into foreign syntax called for actual evaluation, not
guessing.

Write a Clojure expression that computes the length of "ant".

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"ant\")"}}]}
```

## G11-05: Import form

### G11-05 record 1

**form**: `(do "(:import (java.util Date)) imports a host class" :imported)`  •  **expected**: `':imported'`

```
Two creatures of the meadow approached the coming winter very differently.

"There is no need to evaluate that," Skip the grasshopper said,
swaggering through the underbrush. "Anyone can see what the (:import ...) ns clause for host classes comes to."
Toc the ant, who at the edge of the woods had grown used to such claims, asked
her to actually write the form `(do "(:import (java.util Date)) imports a host class" :imported)` and
submit it to the REPL — just to be sure.

Write a form whose evaluation gives the marker for the import-form lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(:import (java.util Date)) imports a host class\" :imported)"}}]}
```

### G11-05 record 2

**form**: `(do "(:import (java.util Date)) imports a host class" :imported)`  •  **expected**: `':imported'`

```
Two creatures of the meadow approached the coming winter very differently. All this took place atop the hilltop.

"This is not your meadow," Tic the ant said atop the hilltop, saying very little.
"Here, the methods belong to objects, and the dot has a particular
meaning." Hum the grasshopper, with great whoops of laughter, said they
could read the foreign form anyway. Tic sketched `(do "(:import (java.util Date)) imports a host class" :imported)` on
the ground; let the runtime, he insisted, declare what
the (:import ...) ns clause for host classes returned.

Question: write a Clojure expression for the marker for the import-form lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(:import (java.util Date)) imports a host class\" :imported)"}}]}
```

### G11-05 record 3

**form**: `(do "(:import (java.util Date)) imports a host class" :imported)`  •  **expected**: `':imported'`

```
Two creatures of the meadow approached the coming winter very differently. This was near the woods.

Tic the ant and Skip the grasshopper stopped in the woods where someone had
written the (:import ...) ns clause for host classes on a flat stone. Skip, swaggering through the underbrush,
declared that she could see the answer at a glance.
Tic, her eyes always on the path, suggested they actually evaluate the form
`(do "(:import (java.util Date)) imports a host class" :imported)` in the REPL and read off whatever it returned.

What Clojure form computes the marker for the import-form lesson? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(:import (java.util Date)) imports a host class\" :imported)"}}]}
```

### G11-05 record 4

**form**: `(do "(:import (java.util Date)) imports a host class" :imported)`  •  **expected**: `':imported'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

A wooden border-post at the edge of the farm marked the edge of the host runtime's
territory. The form written on it — `(do "(:import (java.util Date)) imports a host class" :imported)` — captured
the (:import ...) ns clause for host classes. Hum, drowsy from the warm sun, agreed for once that
crossing into foreign syntax called for actual evaluation, not
guessing.

Write a Clojure expression that computes the marker for the import-form lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(:import (java.util Date)) imports a host class\" :imported)"}}]}
```

### G11-05 record 5

**form**: `(do "(:import (java.util Date)) imports a host class" :imported)`  •  **expected**: `':imported'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

At the edge of a stockpile atop the hilltop, Hum the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(do "(:import (java.util Date)) imports a host class" :imported)`
first would win the right to set the next day's count.
Toc the ant, her eyes always on the path, said it was simpler to type the form into
the REPL than to argue about the (:import ...) ns clause for host classes.

What Clojure form computes the marker for the import-form lesson? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(:import (java.util Date)) imports a host class\" :imported)"}}]}
```

## G11-06: new and dot-construct

### G11-06 record 1

**form**: `(String. "hello")`  •  **expected**: `'hello'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

At a wayside shrine near the woods dedicated to interop, the day's offering
was the constructor call (String. "hello"). Tic the ant knelt and placed the form
`(String. "hello")` on the stone. Chirp, watching, agreed to be the
one to submit it to the runtime.

Write a form whose evaluation gives the string built by the dot-construct.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(String. \"hello\")"}}]}
```

### G11-06 record 2

**form**: `(String. "hello")`  •  **expected**: `'hello'`

```
All summer long, the Ant worked while the Grasshopper sang. This was near the orchard.

A wooden sign nailed to a stalk by the orchard carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(String. "hello")`. Hum
laughed, boasting at every turn, and declared it too easy. Tic said patiently
that the only way to be sure of the constructor call (String. "hello") was to put it in the
REPL.

Write a Clojure expression that computes the string built by the dot-construct.

---

I use the dot or slash form for the host method, then submit.

{"tool_calls":[{"name":"eval","args":{"form":"(String. \"hello\")"}}]}
```

### G11-06 record 3

**form**: `(String. "hello")`  •  **expected**: `'hello'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

A merchant's stall in the orchard sold translated phrasebooks for the host
language; today's lesson was the constructor call (String. "hello"). Toc the ant copied the
form `(String. "hello")` from the page, and Hum the grasshopper agreed
(for once) that one should always check the REPL before trusting a
translation.

Write a Clojure expression that computes the string built by the dot-construct.

---

{"tool_calls":[{"name":"eval","args":{"form":"(String. \"hello\")"}}]}
```

### G11-06 record 4

**form**: `(String. "hello")`  •  **expected**: `'hello'`

```
Two creatures of the meadow approached the coming winter very differently. All this took place at the edge of the forest.

Halfway through the morning's work, Skip the grasshopper blocked
Toc the ant's path in the forest and refused to step aside until someone
could prove what the form `(String. "hello")` evaluated to. Skip
called it impossible. Toc the ant, walking up at her usual
pace, simply said: "Submit the constructor call (String. "hello") to the REPL. Whatever comes
back is the answer."

Question: write a Clojure expression for the string built by the dot-construct.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(String. \"hello\")"}}]}
```

### G11-06 record 5

**form**: `(String. "hello")`  •  **expected**: `'hello'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. This was in the meadow.

A small audience of meadow creatures had gathered by the meadow to watch
Skip the grasshopper attempt to outwit Bit the ant at reading the
REPL. Bit pointed to the constructor call (String. "hello") and read out the form aloud:
`(String. "hello")`. The crowd waited to see who would correctly write the
form to submit.

Question: write a Clojure expression for the string built by the dot-construct.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(String. \"hello\")"}}]}
```

## G11-07: Arrays

### G11-07 record 1

**form**: `(let [a (int-array [10 20 30])] (aget a 1))`  •  **expected**: `20`

```
Two creatures of the meadow approached the coming winter very differently.

Tic the ant had been keeping a small leather notebook of every form
he had successfully evaluated. Today by the forest, the next entry
was indexing into an int-array via aget. Hum the grasshopper peered over
his shoulder at the form `(let [a (int-array [10 20 30])] (aget a 1))` and asked what it
would come out to.

Question: write a Clojure expression for the value at index 1 of the array.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a (int-array [10 20 30])] (aget a 1))"}}]}
```

### G11-07 record 2

**form**: `(let [a (int-array [10 20 30])] (aget a 1))`  •  **expected**: `20`

```
All summer long, the Ant worked while the Grasshopper sang. All this took place at the edge of the farm.

Hum the grasshopper insisted the foreign-runtime forms were "just like
home." Toc the ant tapped a stone in the farm where someone had inscribed
indexing into an int-array via aget. "Then write `(let [a (int-array [10 20 30])] (aget a 1))` into the REPL," Toc
said, "and we'll see if your familiarity holds."

Write a Clojure expression that computes the value at index 1 of the array.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a (int-array [10 20 30])] (aget a 1))"}}]}
```

### G11-07 record 3

**form**: `(let [a (int-array [10 20 30])] (aget a 1))`  •  **expected**: `20`

```
All summer long, the Ant worked while the Grasshopper sang.

Bit the ant had been trying to teach Skip the grasshopper how the REPL
works. "Look here," they said, pointing to indexing into an int-array via aget.
"You hand the form `(let [a (int-array [10 20 30])] (aget a 1))` to the runtime, and the runtime hands
you back what it evaluates to." Skip, lulled by the gentle wind, agreed to
try.

Question: write a Clojure expression for the value at index 1 of the array.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a (int-array [10 20 30])] (aget a 1))"}}]}
```

### G11-07 record 4

**form**: `(let [a (int-array [10 20 30])] (aget a 1))`  •  **expected**: `20`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

At a wayside shrine near the orchard dedicated to interop, the day's offering
was indexing into an int-array via aget. Toc the ant knelt and placed the form
`(let [a (int-array [10 20 30])] (aget a 1))` on the stone. Hum, watching, agreed to be the
one to submit it to the runtime.

Write a form whose evaluation gives the value at index 1 of the array.

---

I write the interop form using the host's convention.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a (int-array [10 20 30])] (aget a 1))"}}]}
```

### G11-07 record 5

**form**: `(let [a (int-array [10 20 30])] (aget a 1))`  •  **expected**: `20`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. This was atop the hilltop.

A merchant's stall near the hilltop sold translated phrasebooks for the host
language; today's lesson was indexing into an int-array via aget. Toc the ant copied the
form `(let [a (int-array [10 20 30])] (aget a 1))` from the page, and Chirp the grasshopper agreed
(for once) that one should always check the REPL before trusting a
translation.

Question: write a Clojure expression for the value at index 1 of the array.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a (int-array [10 20 30])] (aget a 1))"}}]}
```

## G11-08: Type hints

### G11-08 record 1

**form**: `(let [^String s "abc"] (.toUpperCase s))`  •  **expected**: `'ABC'`

```
Two creatures of the meadow approached the coming winter very differently. It happened on the hilltop.

At the edge of a stockpile atop the hilltop, Chirp the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(let [^String s "abc"] (.toUpperCase s))`
first would win the right to set the next day's count.
Tic the ant, without complaint, said it was simpler to type the form into
the REPL than to argue about a let-binding with a ^String type hint.

What Clojure form computes the uppercased string after a type-hinted binding? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [^String s \"abc\"] (.toUpperCase s))"}}]}
```

### G11-08 record 2

**form**: `(let [^String s "abc"] (.toUpperCase s))`  •  **expected**: `'ABC'`

```
Two creatures of the meadow approached the coming winter very differently. All this took place by the garden.

With a twig, Skip the grasshopper marked out a wager by the garden: whoever
guessed the result of `(let [^String s "abc"] (.toUpperCase s))` first would win the right to
choose the next song. Tic the ant, her eyes always on the path, said it was easier
to ask the REPL about a let-binding with a ^String type hint than to argue.

Question: write a Clojure expression for the uppercased string after a type-hinted binding.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(let [^String s \"abc\"] (.toUpperCase s))"}}]}
```

### G11-08 record 3

**form**: `(let [^String s "abc"] (.toUpperCase s))`  •  **expected**: `'ABC'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. This was at the edge of the forest.

A small audience of meadow creatures had gathered in the forest to watch
Hum the grasshopper attempt to outwit Bit the ant at reading the
REPL. Bit pointed to a let-binding with a ^String type hint and read out the form aloud:
`(let [^String s "abc"] (.toUpperCase s))`. The crowd waited to see who would correctly write the
form to submit.

Write a form whose evaluation gives the uppercased string after a type-hinted binding.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(let [^String s \"abc\"] (.toUpperCase s))"}}]}
```

### G11-08 record 4

**form**: `(let [^String s "abc"] (.toUpperCase s))`  •  **expected**: `'ABC'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Chirp the grasshopper chalked a wager on a flat slate near the farm: whoever
predicted the result of `(let [^String s "abc"] (.toUpperCase s))` first would set the next day's
ration. Tic the ant, with steady, careful steps, said it would be simpler to type
the form into the REPL than to bicker about a let-binding with a ^String type hint.

Question: write a Clojure expression for the uppercased string after a type-hinted binding.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [^String s \"abc\"] (.toUpperCase s))"}}]}
```

### G11-08 record 5

**form**: `(let [^String s "abc"] (.toUpperCase s))`  •  **expected**: `'ABC'`

```
All summer long, the Ant worked while the Grasshopper sang.

At a wayside shrine at the edge of the garden dedicated to interop, the day's offering
was a let-binding with a ^String type hint. Toc the ant knelt and placed the form
`(let [^String s "abc"] (.toUpperCase s))` on the stone. Chirp, watching, agreed to be the
one to submit it to the runtime.

Write a form whose evaluation gives the uppercased string after a type-hinted binding.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(let [^String s \"abc\"] (.toUpperCase s))"}}]}
```

## G11-09: Checked vs unchecked math

### G11-09 record 1

**form**: `(+ 1 2)`  •  **expected**: `3`

```
Two creatures of the meadow approached the coming winter very differently. All this took place in the forest.

"There is no need to evaluate that," Chirp the grasshopper said,
as if the race were already won. "Anyone can see what the form (+ 1 2) under default checked math comes to."
Tic the ant, who at the edge of the forest had grown used to such claims, asked
him to actually write the form `(+ 1 2)` and
submit it to the REPL — just to be sure.

Write a Clojure expression that computes the result of (+ 1 2) under the default math regime.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G11-09 record 2

**form**: `(+ 1 2)`  •  **expected**: `3`

```
Two creatures of the meadow approached the coming winter very differently.

Toc the ant and Hum the grasshopper stopped at the edge of the meadow where someone had
written the form (+ 1 2) under default checked math on a flat stone. Hum, as if the race were already won,
declared that they could see the answer at a glance.
Toc, without complaint, suggested they actually evaluate the form
`(+ 1 2)` in the REPL and read off whatever it returned.

Question: write a Clojure expression for the result of (+ 1 2) under the default math regime.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G11-09 record 3

**form**: `(+ 1 2)`  •  **expected**: `3`

```
All summer long, the Ant worked while the Grasshopper sang. This was by the farm.

A wooden sign nailed to a stalk in the farm carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(+ 1 2)`. Skip
laughed, swaggering through the underbrush, and declared it too easy. Toc said patiently
that the only way to be sure of the form (+ 1 2) under default checked math was to put it in the
REPL.

Write a form whose evaluation gives the result of (+ 1 2) under the default math regime.

---

I use the dot or slash form for the host method, then submit.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G11-09 record 4

**form**: `(+ 1 2)`  •  **expected**: `3`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. It happened at the edge of the garden.

Skip the grasshopper insisted the foreign-runtime forms were "just like
home." Tic the ant tapped a stone near the garden where someone had inscribed
the form (+ 1 2) under default checked math. "Then write `(+ 1 2)` into the REPL," Tic
said, "and we'll see if your familiarity holds."

Write a form whose evaluation gives the result of (+ 1 2) under the default math regime.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G11-09 record 5

**form**: `(+ 1 2)`  •  **expected**: `3`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. It happened at the edge of the meadow.

Toc the ant had been trying to teach Hum the grasshopper how the REPL
works. "Look here," she said, pointing to the form (+ 1 2) under default checked math.
"You hand the form `(+ 1 2)` to the runtime, and the runtime hands
you back what it evaluates to." Hum, lulled by the gentle wind, agreed to
try.

What Clojure form computes the result of (+ 1 2) under the default math regime? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

## G11-10: ClojureScript overview

### G11-10 record 1

**form**: `(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)`  •  **expected**: `':studied'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Bit the ant and Skip the grasshopper stopped near the woods where someone had
written the ClojureScript host overview on a flat stone. Skip, boasting at every turn,
declared that she could see the answer at a glance.
Bit, with steady, careful steps, suggested they actually evaluate the form
`(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)` in the REPL and read off whatever it returned.

What Clojure form computes the marker for studying the cljs host? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"ClojureScript compiles to JavaScript via the Closure compiler\" :studied)"}}]}
```

### G11-10 record 2

**form**: `(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)`  •  **expected**: `':studied'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

With a twig, Chirp the grasshopper marked out a wager at the edge of the garden: whoever
guessed the result of `(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)` first would win the right to
choose the next song. Tic the ant, her eyes always on the path, said it was easier
to ask the REPL about the ClojureScript host overview than to argue.

Write a form whose evaluation gives the marker for studying the cljs host.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"ClojureScript compiles to JavaScript via the Closure compiler\" :studied)"}}]}
```

### G11-10 record 3

**form**: `(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)`  •  **expected**: `':studied'`

```
All summer long, the Ant worked while the Grasshopper sang.

"This is not your meadow," Toc the ant said by the garden, stepping deliberately.
"Here, the methods belong to objects, and the dot has a particular
meaning." Chirp the grasshopper, with a smug grin, said he
could read the foreign form anyway. Toc sketched `(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)` on
the ground; let the runtime, she insisted, declare what
the ClojureScript host overview returned.

Write a form whose evaluation gives the marker for studying the cljs host.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"ClojureScript compiles to JavaScript via the Closure compiler\" :studied)"}}]}
```

### G11-10 record 4

**form**: `(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently. This was at the edge of the farm.

Bit the ant had been keeping a small leather notebook of every form
they had successfully evaluated. Today in the farm, the next entry
was the ClojureScript host overview. Skip the grasshopper peered over
their shoulder at the form `(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)` and asked what it
would come out to.

Write a Clojure expression that computes the marker for studying the cljs host.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"ClojureScript compiles to JavaScript via the Closure compiler\" :studied)"}}]}
```

### G11-10 record 5

**form**: `(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)`  •  **expected**: `':studied'`

```
All summer long, the Ant worked while the Grasshopper sang. It happened at the edge of the farm.

Chirp the grasshopper insisted the foreign-runtime forms were "just like
home." Bit the ant tapped a stone in the farm where someone had inscribed
the ClojureScript host overview. "Then write `(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)` into the REPL," Bit
said, "and we'll see if your familiarity holds."

Write a Clojure expression that computes the marker for studying the cljs host.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"ClojureScript compiles to JavaScript via the Closure compiler\" :studied)"}}]}
```

## G11-11: cljs / JavaScript interop

### G11-11 record 1

**form**: `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently. It happened in the meadow.

A wooden sign nailed to a stalk in the meadow carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)`. Chirp
laughed, boasting at every turn, and declared it too easy. Tic said patiently
that the only way to be sure of the cljs-to-js interop syntax was to put it in the
REPL.

Question: write a Clojure expression for the marker for the cljs-js interop lesson.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(js/console.log x) calls a JS global; (.-foo o) reads a JS field\" :studied)"}}]}
```

### G11-11 record 2

**form**: `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently. This was near the forest.

At the edge of a stockpile at the edge of the forest, Skip the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)`
first would win the right to set the next day's count.
Toc the ant, with steady, careful steps, said it was simpler to type the form into
the REPL than to argue about the cljs-to-js interop syntax.

Write a form whose evaluation gives the marker for the cljs-js interop lesson.

---

I write the interop form using the host's convention.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(js/console.log x) calls a JS global; (.-foo o) reads a JS field\" :studied)"}}]}
```

### G11-11 record 3

**form**: `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently. This was at the edge of the forest.

Skip the grasshopper insisted the foreign-runtime forms were "just like
home." Bit the ant tapped a stone in the forest where someone had inscribed
the cljs-to-js interop syntax. "Then write `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)` into the REPL," Bit
said, "and we'll see if your familiarity holds."

Question: write a Clojure expression for the marker for the cljs-js interop lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(js/console.log x) calls a JS global; (.-foo o) reads a JS field\" :studied)"}}]}
```

### G11-11 record 4

**form**: `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)`  •  **expected**: `':studied'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

A wooden sign nailed to a stalk in the woods carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)`. Hum
laughed, with a smug grin, and declared it too easy. Tic said patiently
that the only way to be sure of the cljs-to-js interop syntax was to put it in the
REPL.

What Clojure form computes the marker for the cljs-js interop lesson? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(js/console.log x) calls a JS global; (.-foo o) reads a JS field\" :studied)"}}]}
```

### G11-11 record 5

**form**: `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)`  •  **expected**: `':studied'`

```
All summer long, the Ant worked while the Grasshopper sang.

Skip the grasshopper insisted the foreign-runtime forms were "just like
home." Bit the ant tapped a stone by the garden where someone had inscribed
the cljs-to-js interop syntax. "Then write `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)` into the REPL," Bit
said, "and we'll see if your familiarity holds."

Write a form whose evaluation gives the marker for the cljs-js interop lesson.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(js/console.log x) calls a JS global; (.-foo o) reads a JS field\" :studied)"}}]}
```

## G11-12: Basilisp overview (Python host)

### G11-12 record 1

**form**: `(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently.

Skip the grasshopper chalked a wager on a flat slate atop the hilltop: whoever
predicted the result of `(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)` first would set the next day's
ration. Toc the ant, stepping deliberately, said it would be simpler to type
the form into the REPL than to bicker about the basilisp host overview.

Write a form whose evaluation gives the marker for studying basilisp.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"basilisp is a Clojure-like Lisp implemented on Python\" :studied)"}}]}
```

### G11-12 record 2

**form**: `(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently.

At a wayside shrine at the edge of the garden dedicated to interop, the day's offering
was the basilisp host overview. Bit the ant knelt and placed the form
`(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)` on the stone. Hum, watching, agreed to be the
one to submit it to the runtime.

Write a form whose evaluation gives the marker for studying basilisp.

---

I express the host call as a Clojure form for the REPL.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"basilisp is a Clojure-like Lisp implemented on Python\" :studied)"}}]}
```

### G11-12 record 3

**form**: `(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)`  •  **expected**: `':studied'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. It happened at the edge of the woods.

A wooden border-post in the woods marked the edge of the host runtime's
territory. The form written on it — `(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)` — captured
the basilisp host overview. Hum, lulled by the gentle wind, agreed for once that
crossing into foreign syntax called for actual evaluation, not
guessing.

Write a form whose evaluation gives the marker for studying basilisp.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"basilisp is a Clojure-like Lisp implemented on Python\" :studied)"}}]}
```

### G11-12 record 4

**form**: `(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently.

A wooden border-post in the garden marked the edge of the host runtime's
territory. The form written on it — `(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)` — captured
the basilisp host overview. Skip, yawning at the soft moss, agreed for once that
crossing into foreign syntax called for actual evaluation, not
guessing.

Write a Clojure expression that computes the marker for studying basilisp.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"basilisp is a Clojure-like Lisp implemented on Python\" :studied)"}}]}
```

### G11-12 record 5

**form**: `(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)`  •  **expected**: `':studied'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. It happened near the forest.

"There is no need to evaluate that," Chirp the grasshopper said,
puffed up with pride. "Anyone can see what the basilisp host overview comes to."
Toc the ant, who at the edge of the forest had grown used to such claims, asked
him to actually write the form `(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)` and
submit it to the REPL — just to be sure.

Write a Clojure expression that computes the marker for studying basilisp.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"basilisp is a Clojure-like Lisp implemented on Python\" :studied)"}}]}
```

## G11-13: Cross-platform .cljc and reader-conditionals

### G11-13 record 1

**form**: `(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently.

At the edge of a stockpile at the edge of the orchard, Hum the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)`
first would win the right to set the next day's count.
Toc the ant, with steady, careful steps, said it was simpler to type the form into
the REPL than to argue about the reader-conditional #?(...) form.

Write a form whose evaluation gives the marker for the reader-conditional lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"#?(:clj … :cljs …) selects a form per host at read time\" :studied)"}}]}
```

### G11-13 record 2

**form**: `(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently.

Chirp the grasshopper insisted the foreign-runtime forms were "just like
home." Tic the ant tapped a stone by the farm where someone had inscribed
the reader-conditional #?(...) form. "Then write `(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)` into the REPL," Tic
said, "and we'll see if your familiarity holds."

Write a Clojure expression that computes the marker for the reader-conditional lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"#?(:clj … :cljs …) selects a form per host at read time\" :studied)"}}]}
```

### G11-13 record 3

**form**: `(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)`  •  **expected**: `':studied'`

```
All summer long, the Ant worked while the Grasshopper sang. It happened atop the hilltop.

Tic the ant and Chirp the grasshopper had wandered on the hilltop into territory
where the REPL spoke to another runtime entirely. Tic read the sign
and pointed at the reader-conditional #?(...) form; the form to submit, written in the
foreign convention, was `(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)`.

Write a Clojure expression that computes the marker for the reader-conditional lesson.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"#?(:clj … :cljs …) selects a form per host at read time\" :studied)"}}]}
```

### G11-13 record 4

**form**: `(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)`  •  **expected**: `':studied'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

With a twig, Chirp the grasshopper marked out a wager by the farm: whoever
guessed the result of `(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)` first would win the right to
choose the next song. Tic the ant, without complaint, said it was easier
to ask the REPL about the reader-conditional #?(...) form than to argue.

What Clojure form computes the marker for the reader-conditional lesson? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"#?(:clj … :cljs …) selects a form per host at read time\" :studied)"}}]}
```

### G11-13 record 5

**form**: `(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently. All this took place in the forest.

Bit the ant had been keeping a small leather notebook of every form
they had successfully evaluated. Today in the forest, the next entry
was the reader-conditional #?(...) form. Chirp the grasshopper peered over
their shoulder at the form `(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)` and asked what it
would come out to.

Question: write a Clojure expression for the marker for the reader-conditional lesson.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"#?(:clj … :cljs …) selects a form per host at read time\" :studied)"}}]}
```

## G11-14: Debugging host leaks

### G11-14 record 1

**form**: `(do "host stack traces leak through interop; learn to read them" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently.

A small audience of meadow creatures had gathered at the edge of the forest to watch
Skip the grasshopper attempt to outwit Toc the ant at reading the
REPL. Toc pointed to the topic of debugging host-runtime leaks and read out the form aloud:
`(do "host stack traces leak through interop; learn to read them" :studied)`. The crowd waited to see who would correctly write the
form to submit.

Write a Clojure expression that computes the marker for the host-leaks lesson.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"host stack traces leak through interop; learn to read them\" :studied)"}}]}
```

### G11-14 record 2

**form**: `(do "host stack traces leak through interop; learn to read them" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently.

At the edge of a stockpile by the woods, Hum the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(do "host stack traces leak through interop; learn to read them" :studied)`
first would win the right to set the next day's count.
Toc the ant, without complaint, said it was simpler to type the form into
the REPL than to argue about the topic of debugging host-runtime leaks.

Write a form whose evaluation gives the marker for the host-leaks lesson.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"host stack traces leak through interop; learn to read them\" :studied)"}}]}
```

### G11-14 record 3

**form**: `(do "host stack traces leak through interop; learn to read them" :studied)`  •  **expected**: `':studied'`

```
All summer long, the Ant worked while the Grasshopper sang.

With a twig, Hum the grasshopper marked out a wager at the edge of the hilltop: whoever
guessed the result of `(do "host stack traces leak through interop; learn to read them" :studied)` first would win the right to
choose the next song. Bit the ant, stepping deliberately, said it was easier
to ask the REPL about the topic of debugging host-runtime leaks than to argue.

What Clojure form computes the marker for the host-leaks lesson? Submit it via `eval`.

---

I express the host call as a Clojure form for the REPL.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"host stack traces leak through interop; learn to read them\" :studied)"}}]}
```

### G11-14 record 4

**form**: `(do "host stack traces leak through interop; learn to read them" :studied)`  •  **expected**: `':studied'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

With a twig, Chirp the grasshopper marked out a wager at the edge of the farm: whoever
guessed the result of `(do "host stack traces leak through interop; learn to read them" :studied)` first would win the right to
choose the next song. Tic the ant, saying very little, said it was easier
to ask the REPL about the topic of debugging host-runtime leaks than to argue.

Write a form whose evaluation gives the marker for the host-leaks lesson.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"host stack traces leak through interop; learn to read them\" :studied)"}}]}
```

### G11-14 record 5

**form**: `(do "host stack traces leak through interop; learn to read them" :studied)`  •  **expected**: `':studied'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

"This is not your meadow," Toc the ant said near the hilltop, without complaint.
"Here, the methods belong to objects, and the dot has a particular
meaning." Chirp the grasshopper, puffed up with pride, said he
could read the foreign form anyway. Toc sketched `(do "host stack traces leak through interop; learn to read them" :studied)` on
the ground; let the runtime, she insisted, declare what
the topic of debugging host-runtime leaks returned.

Write a Clojure expression that computes the marker for the host-leaks lesson.

---

I write the interop form using the host's convention.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"host stack traces leak through interop; learn to read them\" :studied)"}}]}
```


---

**Grade 11 totals: 14 subjects, 70 records.**
