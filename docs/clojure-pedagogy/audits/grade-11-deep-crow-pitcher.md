# crow-pitcher grade 11 — deep spot-check

5 records per subject for hand-audit.

---

## G11-01: JVM vs CLR vs JS vs Python (host overview)

### G11-01 record 1  •  form `(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)`  •  expected `':studied'`

```
Hunger and thirst had driven the Crow far from her usual perch.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust in the orchard: whoever guessed the result of `(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)`
first would win the right to claim the next clear water they found.
Caw the crow, saying very little, said it was easier to ask the REPL
about the idea that Clojure has multiple host runtimes than to argue.

Question: write a Clojure expression for the marker value when the host overview has been studied.

---

I express the host call as a Clojure form for the REPL.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Clojure runs on multiple hosts: JVM, CLR, JS, Python\" :studied)"}}]}
```

### G11-01 record 2  •  form `(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScript; Python: basilisp" :hosts)`  •  expected `':hosts'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

At a moss-flecked pitcher along the road, Caw the crow sketched a small
wager: whoever guessed the result of `(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScript; Python: basilisp" :hosts)` first would drink
first when the water rose. Sable the crow, saying very little, said it was
simpler to type the form into the REPL than to argue about
the family of Clojure host runtimes.

What Clojure form computes the marker keyword for the host family? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"JVM: Clojure; CLR: ClojureCLR; JS: ClojureScript; Python: basilisp\" :hosts)"}}]}
```

### G11-01 record 3  •  form `(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)`  •  expected `':studied'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Korvus the crow insisted the foreign-runtime forms were "just like
home." Caw the crow tapped a stone in the village where someone had
inscribed the idea that Clojure has multiple host runtimes. "Then write `(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)` into the
REPL," Caw said, "and we'll see if your familiarity holds."

Write a Clojure expression that computes the marker value when the host overview has been studied.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Clojure runs on multiple hosts: JVM, CLR, JS, Python\" :studied)"}}]}
```

### G11-01 record 4  •  form `(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScript; Python: basilisp" :hosts)`  •  expected `':hosts'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

"This is not your orchard," Caw the crow said, untroubled by what others thought,
at the edge of the orchard. "Here, the methods belong to objects, and the dot has a
particular meaning." Korvus the crow, boasting at every turn, said he
could read the foreign form anyway. Caw sketched `(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScript; Python: basilisp" :hosts)`
on the ground; let the runtime, she insisted, declare
what the family of Clojure host runtimes returned.

Write a Clojure expression that computes the marker keyword for the host family.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"JVM: Clojure; CLR: ClojureCLR; JS: ClojureScript; Python: basilisp\" :hosts)"}}]}
```

### G11-01 record 5  •  form `(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)`  •  expected `':studied'`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place by the meadow.

A small audience of sparrows had gathered at the edge of the meadow to watch
Korvus the crow attempt to outwit Sable the crow at the rim of an old
pitcher. Sable pointed to the idea that Clojure has multiple host runtimes and read out the form
aloud: `(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

What Clojure form computes the marker value when the host overview has been studied? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Clojure runs on multiple hosts: JVM, CLR, JS, Python\" :studied)"}}]}
```

## G11-02: Method call syntax

### G11-02 record 1  •  form `(.toUpperCase "abc")`  •  expected `'ABC'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A wooden border-post by the meadow marked the edge of the host runtime's
territory. The form written on it — `(.toUpperCase "abc")` — captured
the method call (.toUpperCase "abc"). Sable, her legs heavy from sprinting from flying, agreed for once
that crossing into foreign syntax called for actual evaluation, not
guessing.

Write a form whose evaluation gives the uppercased string returned by the method.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
```

### G11-02 record 2  •  form `(.startsWith "crow-pitcher" "crow")`  •  expected `True`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A wooden sign nailed to a tree in the village carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(.startsWith "crow-pitcher" "crow")`. Caw laughed, boasting at every turn, and declared it
too easy. Sable said patiently that the only way to be sure of
a method call (.startsWith ...) returning a boolean was to drop it into the REPL.

Write a Clojure expression that computes whether the string starts with the prefix.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(.startsWith \"crow-pitcher\" \"crow\")"}}]}
```

### G11-02 record 3  •  form `(. "abc" toUpperCase)`  •  expected `'ABC'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened atop the hilltop.

"This is not your orchard," Korvus the crow said, saying very little,
near the hilltop. "Here, the methods belong to objects, and the dot has a
particular meaning." Caw the crow, swaggering through the underbrush, said she
could read the foreign form anyway. Korvus sketched `(. "abc" toUpperCase)`
on the ground; let the runtime, he insisted, declare
what the alternate dot form (. obj method) returned.

Write a Clojure expression that computes the uppercased result via the longer dot syntax.

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(. \"abc\" toUpperCase)"}}]}
```

### G11-02 record 4  •  form `(.toUpperCase "abc")`  •  expected `'ABC'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. All this took place near the farm.

Korvus the crow etched a wager along the rim of a chipped pitcher
in the farm: whoever predicted the result of `(.toUpperCase "abc")` first would set
the next day's foraging route. Caw the crow, saying very little, said it
would be simpler to drop the form into the REPL than to bicker about
the method call (.toUpperCase "abc").

Write a Clojure expression that computes the uppercased string returned by the method.

---

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
```

### G11-02 record 5  •  form `(.startsWith "crow-pitcher" "crow")`  •  expected `True`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Caw the crow insisted the foreign-runtime forms were "just like
home." Korvus the crow tapped a stone along the road where someone had
inscribed a method call (.startsWith ...) returning a boolean. "Then write `(.startsWith "crow-pitcher" "crow")` into the
REPL," Korvus said, "and we'll see if your familiarity holds."

What Clojure form computes whether the string starts with the prefix? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(.startsWith \"crow-pitcher\" \"crow\")"}}]}
```

## G11-03: Static method call

### G11-03 record 1  •  form `(Math/abs -7)`  •  expected `7`

```
Hunger and thirst had driven the Crow far from her usual perch.

A wooden border-post at the edge of the market marked the edge of the host runtime's
territory. The form written on it — `(Math/abs -7)` — captured
the static call (Math/abs -7). Caw, lulled by the gentle wind from flying, agreed for once
that crossing into foreign syntax called for actual evaluation, not
guessing.

Write a Clojure expression that computes the absolute value of -7 via the static method.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(Math/abs -7)"}}]}
```

### G11-03 record 2  •  form `(Math/max 3 9)`  •  expected `9`

```
Hunger and thirst had driven the Crow far from her usual perch. It happened near the hilltop.

"This is not your orchard," Sable the crow said, stepping deliberately,
near the hilltop. "Here, the methods belong to objects, and the dot has a
particular meaning." Caw the crow, swaggering through the underbrush, said she
could read the foreign form anyway. Sable sketched `(Math/max 3 9)`
on the ground; let the runtime, they insisted, declare
what the static call (Math/max 3 9) returned.

What Clojure form computes the larger of 3 and 9 via the static method? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(Math/max 3 9)"}}]}
```

### G11-03 record 3  •  form `(Math/abs -7)`  •  expected `7`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

At a moss-flecked pitcher in the farm, Caw the crow sketched a small
wager: whoever guessed the result of `(Math/abs -7)` first would drink
first when the water rose. Sable the crow, her eyes always on the path, said it was
simpler to type the form into the REPL than to argue about
the static call (Math/abs -7).

What Clojure form computes the absolute value of -7 via the static method? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(Math/abs -7)"}}]}
```

### G11-03 record 4  •  form `(Math/max 3 9)`  •  expected `9`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Caw the crow insisted the foreign-runtime forms were "just like
home." Sable the crow tapped a stone at the edge of the farm where someone had
inscribed the static call (Math/max 3 9). "Then write `(Math/max 3 9)` into the
REPL," Sable said, "and we'll see if your familiarity holds."

What Clojure form computes the larger of 3 and 9 via the static method? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(Math/max 3 9)"}}]}
```

### G11-03 record 5  •  form `(Math/abs -7)`  •  expected `7`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Korvus the crow etched a wager along the rim of a chipped pitcher
along the road: whoever predicted the result of `(Math/abs -7)` first would set
the next day's foraging route. Sable the crow, without complaint, said it
would be simpler to drop the form into the REPL than to bicker about
the static call (Math/abs -7).

Question: write a Clojure expression for the absolute value of -7 via the static method.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(Math/abs -7)"}}]}
```

## G11-04: Field access

### G11-04 record 1  •  form `(count "stork")`  •  expected `5`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

At a moss-flecked pitcher near the road, Caw the crow sketched a small
wager: whoever guessed the result of `(count "stork")` first would drink
first when the water rose. Sable the crow, without complaint, said it was
simpler to type the form into the REPL than to argue about
the count of "stork".

What Clojure form computes the length of "stork"? Submit it via `eval`.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"stork\")"}}]}
```

### G11-04 record 2  •  form `(count "crow")`  •  expected `4`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

At a wayside shrine near the road dedicated to interop, the day's offering
was the count of "crow". Korvus the crow alighted on the stone and
placed the form `(count "crow")` there. Caw, watching, agreed to
be the one to submit it to the runtime.

Question: write a Clojure expression for the length of "crow".

---

{"tool_calls":[{"name":"eval","args":{"form":"(count \"crow\")"}}]}
```

### G11-04 record 3  •  form `(count "stork")`  •  expected `5`

```
Hunger and thirst had driven the Crow far from her usual perch.

Halfway through a long thirsty afternoon, Korvus the crow alighted
by the village and refused to fly on until someone could prove what the form
`(count "stork")` evaluated to. Korvus called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
the count of "stork" into the REPL. Whatever rises is the answer."

Write a form whose evaluation gives the length of "stork".

---

{"tool_calls":[{"name":"eval","args":{"form":"(count \"stork\")"}}]}
```

### G11-04 record 4  •  form `(count "crow")`  •  expected `4`

```
Hunger and thirst had driven the Crow far from her usual perch.

Caw the crow etched a wager along the rim of a chipped pitcher
near the village: whoever predicted the result of `(count "crow")` first would set
the next day's foraging route. Sable the crow, her eyes always on the path, said it
would be simpler to drop the form into the REPL than to bicker about
the count of "crow".

Question: write a Clojure expression for the length of "crow".

---

{"tool_calls":[{"name":"eval","args":{"form":"(count \"crow\")"}}]}
```

### G11-04 record 5  •  form `(count "stork")`  •  expected `5`

```
Hunger and thirst had driven the Crow far from her usual perch.

Korvus the crow etched a wager along the rim of a chipped pitcher
in the market: whoever predicted the result of `(count "stork")` first would set
the next day's foraging route. Sable the crow, with steady, careful steps, said it
would be simpler to drop the form into the REPL than to bicker about
the count of "stork".

Write a form whose evaluation gives the length of "stork".

---

{"tool_calls":[{"name":"eval","args":{"form":"(count \"stork\")"}}]}
```

## G11-05: Import form

### G11-05 record 1  •  form `(do "(:import (java.util Date)) imports a host class" :imported)`  •  expected `':imported'`

```
Hunger and thirst had driven the Crow far from her usual perch.

Caw the crow and Sable the crow alighted near the village on the rim of an old
pitcher where someone had scratched the (:import ...) ns clause for host classes. Caw,
wide-eyed with fear, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(do "(:import (java.util Date)) imports a host class" :imported)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a Clojure expression that computes the marker for the import-form lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(:import (java.util Date)) imports a host class\" :imported)"}}]}
```

### G11-05 record 2  •  form `(do "import is a top-of-file ns clause" :studied)`  •  expected `':studied'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A wooden sign nailed to a tree by the meadow carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do "import is a top-of-file ns clause" :studied)`. Korvus laughed, swaggering through the underbrush, and declared it
too easy. Caw said patiently that the only way to be sure of
the role of import in a Clojure file was to drop it into the REPL.

Write a Clojure expression that computes the marker for studying import.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"import is a top-of-file ns clause\" :studied)"}}]}
```

### G11-05 record 3  •  form `(do "(:import (java.util Date)) imports a host class" :imported)`  •  expected `':imported'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Caw the crow insisted the foreign-runtime forms were "just like
home." Korvus the crow tapped a stone at the edge of the meadow where someone had
inscribed the (:import ...) ns clause for host classes. "Then write `(do "(:import (java.util Date)) imports a host class" :imported)` into the
REPL," Korvus said, "and we'll see if your familiarity holds."

Write a form whose evaluation gives the marker for the import-form lesson.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(:import (java.util Date)) imports a host class\" :imported)"}}]}
```

### G11-05 record 4  •  form `(do "import is a top-of-file ns clause" :studied)`  •  expected `':studied'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened near the meadow.

Caw the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," she said, pointing to the role of import in a Clojure file.
"You hand the form `(do "import is a top-of-file ns clause" :studied)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, near to giving up the search for water, agreed to try.

Question: write a Clojure expression for the marker for studying import.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"import is a top-of-file ns clause\" :studied)"}}]}
```

### G11-05 record 5  •  form `(do "(:import (java.util Date)) imports a host class" :imported)`  •  expected `':imported'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was atop the hilltop.

A wooden sign nailed to a tree atop the hilltop carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do "(:import (java.util Date)) imports a host class" :imported)`. Sable laughed, with great whoops of laughter, and declared it
too easy. Korvus said patiently that the only way to be sure of
the (:import ...) ns clause for host classes was to drop it into the REPL.

What Clojure form computes the marker for the import-form lesson? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(:import (java.util Date)) imports a host class\" :imported)"}}]}
```

## G11-06: new and dot-construct

### G11-06 record 1  •  form `(String. "hello")`  •  expected `'hello'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Korvus the crow etched a wager along the rim of a chipped pitcher
by the orchard: whoever predicted the result of `(String. "hello")` first would set
the next day's foraging route. Caw the crow, saying very little, said it
would be simpler to drop the form into the REPL than to bicker about
the constructor call (String. "hello").

Write a form whose evaluation gives the string built by the dot-construct.

---

{"tool_calls":[{"name":"eval","args":{"form":"(String. \"hello\")"}}]}
```

### G11-06 record 2  •  form `(new String "world")`  •  expected `'world'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A merchant's stall in the farm sold translated phrasebooks for the host
language; today's lesson was the (new String "world") form. Sable the crow
copied the form `(new String "world")` from the page, and Korvus the crow
agreed (for once) that one should always check the REPL before
trusting a translation.

What Clojure form computes the string built by (new ...)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(new String \"world\")"}}]}
```

### G11-06 record 3  •  form `(String. "hello")`  •  expected `'hello'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place in the village.

Caw the crow and Sable the crow alighted in the village on the rim of an old
pitcher where someone had scratched the constructor call (String. "hello"). Caw,
wide-eyed with fear, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(String. "hello")` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a Clojure expression that computes the string built by the dot-construct.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(String. \"hello\")"}}]}
```

### G11-06 record 4  •  form `(new String "world")`  •  expected `'world'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Caw the crow had been keeping a small leather notebook of every form
she had successfully dropped into the REPL — one entry per
stone, one rise per form. Today in the garden, the next entry was
the (new String "world") form. Korvus the crow peered over her shoulder
at the form `(new String "world")` and asked what it would come out to.

Write a Clojure expression that computes the string built by (new ...).

---

{"tool_calls":[{"name":"eval","args":{"form":"(new String \"world\")"}}]}
```

### G11-06 record 5  •  form `(String. "hello")`  •  expected `'hello'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

At a wayside shrine in the village dedicated to interop, the day's offering
was the constructor call (String. "hello"). Korvus the crow alighted on the stone and
placed the form `(String. "hello")` there. Caw, watching, agreed to
be the one to submit it to the runtime.

What Clojure form computes the string built by the dot-construct? Submit it via `eval`.

---

I use the dot or slash form for the host method, then submit.

{"tool_calls":[{"name":"eval","args":{"form":"(String. \"hello\")"}}]}
```

## G11-07: Arrays

### G11-07 record 1  •  form `(let [a (int-array [10 20 30])] (aget a 1))`  •  expected `20`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place near the orchard.

A wooden border-post by the orchard marked the edge of the host runtime's
territory. The form written on it — `(let [a (int-array [10 20 30])] (aget a 1))` — captured
indexing into an int-array via aget. Korvus, weary from the morning's effort from flying, agreed for once
that crossing into foreign syntax called for actual evaluation, not
guessing.

Write a form whose evaluation gives the value at index 1 of the array.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a (int-array [10 20 30])] (aget a 1))"}}]}
```

### G11-07 record 2  •  form `(let [a (int-array [1 2 3])] (alength a))`  •  expected `3`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Korvus the crow and Sable the crow had flown in the orchard into territory
where the REPL spoke to another runtime entirely. Korvus read the
sign and pointed at the length of an int-array via alength; the form to submit, written in
the foreign convention, was `(let [a (int-array [1 2 3])] (alength a))`.

Write a form whose evaluation gives the length of the array.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a (int-array [1 2 3])] (alength a))"}}]}
```

### G11-07 record 3  •  form `(let [a (int-array [10 20 30])] (aget a 1))`  •  expected `20`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust at the edge of the orchard: whoever guessed the result of `(let [a (int-array [10 20 30])] (aget a 1))`
first would win the right to claim the next clear water they found.
Caw the crow, stepping deliberately, said it was easier to ask the REPL
about indexing into an int-array via aget than to argue.

Question: write a Clojure expression for the value at index 1 of the array.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a (int-array [10 20 30])] (aget a 1))"}}]}
```

### G11-07 record 4  •  form `(let [a (int-array [1 2 3])] (alength a))`  •  expected `3`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A wooden border-post near the garden marked the edge of the host runtime's
territory. The form written on it — `(let [a (int-array [1 2 3])] (alength a))` — captured
the length of an int-array via alength. Korvus, drowsy from the warm sun from flying, agreed for once
that crossing into foreign syntax called for actual evaluation, not
guessing.

What Clojure form computes the length of the array? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a (int-array [1 2 3])] (alength a))"}}]}
```

### G11-07 record 5  •  form `(let [a (int-array [10 20 30])] (aget a 1))`  •  expected `20`

```
Hunger and thirst had driven the Crow far from her usual perch.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust near the farm: whoever guessed the result of `(let [a (int-array [10 20 30])] (aget a 1))`
first would win the right to claim the next clear water they found.
Sable the crow, her eyes always on the path, said it was easier to ask the REPL
about indexing into an int-array via aget than to argue.

Write a form whose evaluation gives the value at index 1 of the array.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a (int-array [10 20 30])] (aget a 1))"}}]}
```

## G11-08: Type hints

### G11-08 record 1  •  form `(let [^String s "abc"] (.toUpperCase s))`  •  expected `'ABC'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was at the edge of the garden.

Caw the crow and Korvus the crow alighted near the garden on the rim of an old
pitcher where someone had scratched a let-binding with a ^String type hint. Caw,
shouting until her voice cracked, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(let [^String s "abc"] (.toUpperCase s))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a form whose evaluation gives the uppercased string after a type-hinted binding.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(let [^String s \"abc\"] (.toUpperCase s))"}}]}
```

### G11-08 record 2  •  form `(do "type hints are metadata that guide compilation" :studied)`  •  expected `':studied'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

"There is no need to evaluate that," Korvus the crow said, swaggering through the underbrush.
"Anyone with a sharp eye can see what the role of ^Type metadata as a hint comes to."
Sable the crow, who near the village had grown used to such claims, asked
him to actually write the form `(do "type hints are metadata that guide compilation" :studied)` and drop it
into the REPL — just to be sure.

What Clojure form computes the marker keyword for the type-hint lesson? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"type hints are metadata that guide compilation\" :studied)"}}]}
```

### G11-08 record 3  •  form `(let [^String s "abc"] (.toUpperCase s))`  •  expected `'ABC'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. All this took place in the meadow.

Sable the crow and Caw the crow had flown near the meadow into territory
where the REPL spoke to another runtime entirely. Sable read the
sign and pointed at a let-binding with a ^String type hint; the form to submit, written in
the foreign convention, was `(let [^String s "abc"] (.toUpperCase s))`.

What Clojure form computes the uppercased string after a type-hinted binding? Submit it via `eval`.

---

I use the dot or slash form for the host method, then submit.

{"tool_calls":[{"name":"eval","args":{"form":"(let [^String s \"abc\"] (.toUpperCase s))"}}]}
```

### G11-08 record 4  •  form `(do "type hints are metadata that guide compilation" :studied)`  •  expected `':studied'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened at the edge of the farm.

Korvus the crow had been keeping a small leather notebook of every form
he had successfully dropped into the REPL — one entry per
stone, one rise per form. Today near the farm, the next entry was
the role of ^Type metadata as a hint. Caw the crow peered over his shoulder
at the form `(do "type hints are metadata that guide compilation" :studied)` and asked what it would come out to.

What Clojure form computes the marker keyword for the type-hint lesson? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"type hints are metadata that guide compilation\" :studied)"}}]}
```

### G11-08 record 5  •  form `(let [^String s "abc"] (.toUpperCase s))`  •  expected `'ABC'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened near the road.

A wooden sign nailed to a tree near the road carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(let [^String s "abc"] (.toUpperCase s))`. Sable laughed, with a smug grin, and declared it
too easy. Caw said patiently that the only way to be sure of
a let-binding with a ^String type hint was to drop it into the REPL.

Write a Clojure expression that computes the uppercased string after a type-hinted binding.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(let [^String s \"abc\"] (.toUpperCase s))"}}]}
```

## G11-09: Checked vs unchecked math

### G11-09 record 1  •  form `(+ 1 2)`  •  expected `3`

```
Hunger and thirst had driven the Crow far from her usual perch.

A merchant's stall at the edge of the market sold translated phrasebooks for the host
language; today's lesson was the form (+ 1 2) under default checked math. Caw the crow
copied the form `(+ 1 2)` from the page, and Korvus the crow
agreed (for once) that one should always check the REPL before
trusting a translation.

What Clojure form computes the result of (+ 1 2) under the default math regime? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G11-09 record 2  •  form `(do "*unchecked-math* turns off overflow checking on prims" :studied)`  •  expected `':studied'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

"This is not your orchard," Caw the crow said, her eyes always on the path,
by the market. "Here, the methods belong to objects, and the dot has a
particular meaning." Korvus the crow, puffed up with pride, said he
could read the foreign form anyway. Caw sketched `(do "*unchecked-math* turns off overflow checking on prims" :studied)`
on the ground; let the runtime, she insisted, declare
what the *unchecked-math* dynamic var returned.

What Clojure form computes the marker for the checked/unchecked lesson? Submit it via `eval`.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"*unchecked-math* turns off overflow checking on prims\" :studied)"}}]}
```

### G11-09 record 3  •  form `(+ 1 2)`  •  expected `3`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Halfway through a long thirsty afternoon, Korvus the crow alighted
at the edge of the village and refused to fly on until someone could prove what the form
`(+ 1 2)` evaluated to. Korvus called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
the form (+ 1 2) under default checked math into the REPL. Whatever rises is the answer."

Question: write a Clojure expression for the result of (+ 1 2) under the default math regime.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G11-09 record 4  •  form `(do "*unchecked-math* turns off overflow checking on prims" :studied)`  •  expected `':studied'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened at the edge of the meadow.

"This is not your orchard," Sable the crow said, without complaint,
at the edge of the meadow. "Here, the methods belong to objects, and the dot has a
particular meaning." Caw the crow, puffed up with pride, said she
could read the foreign form anyway. Sable sketched `(do "*unchecked-math* turns off overflow checking on prims" :studied)`
on the ground; let the runtime, they insisted, declare
what the *unchecked-math* dynamic var returned.

Write a form whose evaluation gives the marker for the checked/unchecked lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"*unchecked-math* turns off overflow checking on prims\" :studied)"}}]}
```

### G11-09 record 5  •  form `(+ 1 2)`  •  expected `3`

```
Hunger and thirst had driven the Crow far from her usual perch.

A merchant's stall on the road sold translated phrasebooks for the host
language; today's lesson was the form (+ 1 2) under default checked math. Caw the crow
copied the form `(+ 1 2)` from the page, and Sable the crow
agreed (for once) that one should always check the REPL before
trusting a translation.

Question: write a Clojure expression for the result of (+ 1 2) under the default math regime.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

## G11-10: ClojureScript overview

### G11-10 record 1  •  form `(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)`  •  expected `':studied'`

```
Hunger and thirst had driven the Crow far from her usual perch.

Korvus the crow had been keeping a small leather notebook of every form
he had successfully dropped into the REPL — one entry per
stone, one rise per form. Today at the edge of the farm, the next entry was
the ClojureScript host overview. Sable the crow peered over his shoulder
at the form `(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)` and asked what it would come out to.

Write a form whose evaluation gives the marker for studying the cljs host.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"ClojureScript compiles to JavaScript via the Closure compiler\" :studied)"}}]}
```

### G11-10 record 2  •  form `(do "cljs runs in browsers and Node, with JS interop syntax" :cljs)`  •  expected `':cljs'`

```
Hunger and thirst had driven the Crow far from her usual perch.

A small audience of sparrows had gathered near the orchard to watch
Sable the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to where ClojureScript runs and how interop looks and read out the form
aloud: `(do "cljs runs in browsers and Node, with JS interop syntax" :cljs)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Question: write a Clojure expression for the marker for the cljs-runtime lesson.

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"cljs runs in browsers and Node, with JS interop syntax\" :cljs)"}}]}
```

### G11-10 record 3  •  form `(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)`  •  expected `':studied'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Korvus the crow had been keeping a small leather notebook of every form
he had successfully dropped into the REPL — one entry per
stone, one rise per form. Today by the garden, the next entry was
the ClojureScript host overview. Caw the crow peered over his shoulder
at the form `(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)` and asked what it would come out to.

What Clojure form computes the marker for studying the cljs host? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"ClojureScript compiles to JavaScript via the Closure compiler\" :studied)"}}]}
```

### G11-10 record 4  •  form `(do "cljs runs in browsers and Node, with JS interop syntax" :cljs)`  •  expected `':cljs'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. This was by the village.

"This is not your orchard," Sable the crow said, without complaint,
near the village. "Here, the methods belong to objects, and the dot has a
particular meaning." Caw the crow, as if the race were already won, said she
could read the foreign form anyway. Sable sketched `(do "cljs runs in browsers and Node, with JS interop syntax" :cljs)`
on the ground; let the runtime, they insisted, declare
what where ClojureScript runs and how interop looks returned.

Write a form whose evaluation gives the marker for the cljs-runtime lesson.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"cljs runs in browsers and Node, with JS interop syntax\" :cljs)"}}]}
```

### G11-10 record 5  •  form `(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)`  •  expected `':studied'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Sable the crow and Korvus the crow had flown near the road into territory
where the REPL spoke to another runtime entirely. Sable read the
sign and pointed at the ClojureScript host overview; the form to submit, written in
the foreign convention, was `(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)`.

Write a Clojure expression that computes the marker for studying the cljs host.

---

I use the dot or slash form for the host method, then submit.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"ClojureScript compiles to JavaScript via the Closure compiler\" :studied)"}}]}
```

## G11-11: cljs / JavaScript interop

### G11-11 record 1  •  form `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)`  •  expected `':studied'`

```
Hunger and thirst had driven the Crow far from her usual perch.

Korvus the crow and Caw the crow alighted by the farm on the rim of an old
pitcher where someone had scratched the cljs-to-js interop syntax. Korvus,
with growing alarm, declared the answer beyond reach. Caw, patient as
ever, suggested they drop the form `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Question: write a Clojure expression for the marker for the cljs-js interop lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(js/console.log x) calls a JS global; (.-foo o) reads a JS field\" :studied)"}}]}
```

### G11-11 record 2  •  form `(do "js/<name> namespaces JS globals; .- prefix marks field access" :cljs-interop)`  •  expected `':cljs-interop'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

A wooden sign nailed to a tree at the edge of the village carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do "js/<name> namespaces JS globals; .- prefix marks field access" :cljs-interop)`. Korvus laughed, as if the race were already won, and declared it
too easy. Caw said patiently that the only way to be sure of
two key cljs-js interop conventions was to drop it into the REPL.

Write a Clojure expression that computes the marker keyword for the conventions.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"js/<name> namespaces JS globals; .- prefix marks field access\" :cljs-interop)"}}]}
```

### G11-11 record 3  •  form `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)`  •  expected `':studied'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Korvus the crow and Sable the crow had flown in the garden into territory
where the REPL spoke to another runtime entirely. Korvus read the
sign and pointed at the cljs-to-js interop syntax; the form to submit, written in
the foreign convention, was `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)`.

Write a Clojure expression that computes the marker for the cljs-js interop lesson.

---

I write the interop form using the host's convention.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(js/console.log x) calls a JS global; (.-foo o) reads a JS field\" :studied)"}}]}
```

### G11-11 record 4  •  form `(do "js/<name> namespaces JS globals; .- prefix marks field access" :cljs-interop)`  •  expected `':cljs-interop'`

```
Hunger and thirst had driven the Crow far from her usual perch.

Sable the crow and Caw the crow had flown at the edge of the garden into territory
where the REPL spoke to another runtime entirely. Sable read the
sign and pointed at two key cljs-js interop conventions; the form to submit, written in
the foreign convention, was `(do "js/<name> namespaces JS globals; .- prefix marks field access" :cljs-interop)`.

Question: write a Clojure expression for the marker keyword for the conventions.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"js/<name> namespaces JS globals; .- prefix marks field access\" :cljs-interop)"}}]}
```

### G11-11 record 5  •  form `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)`  •  expected `':studied'`

```
Hunger and thirst had driven the Crow far from her usual perch.

Korvus the crow and Caw the crow alighted atop the hilltop on the rim of an old
pitcher where someone had scratched the cljs-to-js interop syntax. Korvus,
shouting until her voice cracked, declared the answer beyond reach. Caw, patient as
ever, suggested they drop the form `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a form whose evaluation gives the marker for the cljs-js interop lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(js/console.log x) calls a JS global; (.-foo o) reads a JS field\" :studied)"}}]}
```

## G11-12: Basilisp overview (Python host)

### G11-12 record 1  •  form `(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)`  •  expected `':studied'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place by the market.

A wooden border-post near the market marked the edge of the host runtime's
territory. The form written on it — `(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)` — captured
the basilisp host overview. Korvus, drowsy from the warm sun from flying, agreed for once
that crossing into foreign syntax called for actual evaluation, not
guessing.

What Clojure form computes the marker for studying basilisp? Submit it via `eval`.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"basilisp is a Clojure-like Lisp implemented on Python\" :studied)"}}]}
```

### G11-12 record 2  •  form `(do "basilisp interops with Python via the same dot-syntax conventions" :basilisp)`  •  expected `':basilisp'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was in the garden.

Korvus the crow had been keeping a small leather notebook of every form
he had successfully dropped into the REPL — one entry per
stone, one rise per form. Today at the edge of the garden, the next entry was
how basilisp does Python interop. Caw the crow peered over his shoulder
at the form `(do "basilisp interops with Python via the same dot-syntax conventions" :basilisp)` and asked what it would come out to.

Write a Clojure expression that computes the marker keyword for basilisp interop.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"basilisp interops with Python via the same dot-syntax conventions\" :basilisp)"}}]}
```

### G11-12 record 3  •  form `(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)`  •  expected `':studied'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

At a moss-flecked pitcher in the village, Sable the crow sketched a small
wager: whoever guessed the result of `(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)` first would drink
first when the water rose. Korvus the crow, without complaint, said it was
simpler to type the form into the REPL than to argue about
the basilisp host overview.

What Clojure form computes the marker for studying basilisp? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"basilisp is a Clojure-like Lisp implemented on Python\" :studied)"}}]}
```

### G11-12 record 4  •  form `(do "basilisp interops with Python via the same dot-syntax conventions" :basilisp)`  •  expected `':basilisp'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was in the meadow.

Korvus the crow etched a wager along the rim of a chipped pitcher
in the meadow: whoever predicted the result of `(do "basilisp interops with Python via the same dot-syntax conventions" :basilisp)` first would set
the next day's foraging route. Caw the crow, untroubled by what others thought, said it
would be simpler to drop the form into the REPL than to bicker about
how basilisp does Python interop.

What Clojure form computes the marker keyword for basilisp interop? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"basilisp interops with Python via the same dot-syntax conventions\" :basilisp)"}}]}
```

### G11-12 record 5  •  form `(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)`  •  expected `':studied'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened near the hilltop.

"There is no need to evaluate that," Sable the crow said, with great whoops of laughter.
"Anyone with a sharp eye can see what the basilisp host overview comes to."
Korvus the crow, who atop the hilltop had grown used to such claims, asked
them to actually write the form `(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)` and drop it
into the REPL — just to be sure.

Write a Clojure expression that computes the marker for studying basilisp.

---

I let each form raise the surface a little closer to the answer.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"basilisp is a Clojure-like Lisp implemented on Python\" :studied)"}}]}
```

## G11-13: Cross-platform .cljc and reader-conditionals

### G11-13 record 1  •  form `(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)`  •  expected `':studied'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened by the meadow.

At a moss-flecked pitcher in the meadow, Korvus the crow sketched a small
wager: whoever guessed the result of `(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)` first would drink
first when the water rose. Sable the crow, saying very little, said it was
simpler to type the form into the REPL than to argue about
the reader-conditional #?(...) form.

Question: write a Clojure expression for the marker for the reader-conditional lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"#?(:clj … :cljs …) selects a form per host at read time\" :studied)"}}]}
```

### G11-13 record 2  •  form `(do ".cljc files share code across multiple hosts" :cljc)`  •  expected `':cljc'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was on the road.

A wooden sign nailed to a tree near the road carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do ".cljc files share code across multiple hosts" :cljc)`. Sable laughed, swaggering through the underbrush, and declared it
too easy. Korvus said patiently that the only way to be sure of
the role of .cljc files was to drop it into the REPL.

Question: write a Clojure expression for the marker keyword for the .cljc lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \".cljc files share code across multiple hosts\" :cljc)"}}]}
```

### G11-13 record 3  •  form `(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)`  •  expected `':studied'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was near the village.

"There is no need to evaluate that," Caw the crow said, with a smug grin.
"Anyone with a sharp eye can see what the reader-conditional #?(...) form comes to."
Sable the crow, who at the edge of the village had grown used to such claims, asked
her to actually write the form `(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)` and drop it
into the REPL — just to be sure.

Write a form whose evaluation gives the marker for the reader-conditional lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"#?(:clj … :cljs …) selects a form per host at read time\" :studied)"}}]}
```

### G11-13 record 4  •  form `(do ".cljc files share code across multiple hosts" :cljc)`  •  expected `':cljc'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

At a moss-flecked pitcher in the farm, Korvus the crow sketched a small
wager: whoever guessed the result of `(do ".cljc files share code across multiple hosts" :cljc)` first would drink
first when the water rose. Sable the crow, untroubled by what others thought, said it was
simpler to type the form into the REPL than to argue about
the role of .cljc files.

Write a Clojure expression that computes the marker keyword for the .cljc lesson.

---

I express the host call as a Clojure form for the REPL.

{"tool_calls":[{"name":"eval","args":{"form":"(do \".cljc files share code across multiple hosts\" :cljc)"}}]}
```

### G11-13 record 5  •  form `(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)`  •  expected `':studied'`

```
Hunger and thirst had driven the Crow far from her usual perch.

A wooden sign nailed to a tree in the market carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)`. Caw laughed, swaggering through the underbrush, and declared it
too easy. Korvus said patiently that the only way to be sure of
the reader-conditional #?(...) form was to drop it into the REPL.

What Clojure form computes the marker for the reader-conditional lesson? Submit it via `eval`.

---

I write the interop form using the host's convention.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"#?(:clj … :cljs …) selects a form per host at read time\" :studied)"}}]}
```

## G11-14: Debugging host leaks

### G11-14 record 1  •  form `(do "host stack traces leak through interop; learn to read them" :studied)`  •  expected `':studied'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

"There is no need to evaluate that," Sable the crow said, with a smug grin.
"Anyone with a sharp eye can see what the topic of debugging host-runtime leaks comes to."
Caw the crow, who near the orchard had grown used to such claims, asked
them to actually write the form `(do "host stack traces leak through interop; learn to read them" :studied)` and drop it
into the REPL — just to be sure.

Write a form whose evaluation gives the marker for the host-leaks lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"host stack traces leak through interop; learn to read them\" :studied)"}}]}
```

### G11-14 record 2  •  form `(try (Math/sqrt 4) (catch Exception _ :err))`  •  expected `2.0`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

"There is no need to evaluate that," Caw the crow said, as if the race were already won.
"Anyone with a sharp eye can see what wrapping a host call in try/catch in case it leaks comes to."
Sable the crow, who near the market had grown used to such claims, asked
her to actually write the form `(try (Math/sqrt 4) (catch Exception _ :err))` and drop it
into the REPL — just to be sure.

What Clojure form computes the result when the host call succeeds? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (Math/sqrt 4) (catch Exception _ :err))"}}]}
```

### G11-14 record 3  •  form `(do "host stack traces leak through interop; learn to read them" :studied)`  •  expected `':studied'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was near the village.

A wooden sign nailed to a tree near the village carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do "host stack traces leak through interop; learn to read them" :studied)`. Caw laughed, swaggering through the underbrush, and declared it
too easy. Sable said patiently that the only way to be sure of
the topic of debugging host-runtime leaks was to drop it into the REPL.

Write a form whose evaluation gives the marker for the host-leaks lesson.

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"host stack traces leak through interop; learn to read them\" :studied)"}}]}
```

### G11-14 record 4  •  form `(try (Math/sqrt 4) (catch Exception _ :err))`  •  expected `2.0`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A wooden sign nailed to a tree by the orchard carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(try (Math/sqrt 4) (catch Exception _ :err))`. Caw laughed, puffed up with pride, and declared it
too easy. Sable said patiently that the only way to be sure of
wrapping a host call in try/catch in case it leaks was to drop it into the REPL.

Question: write a Clojure expression for the result when the host call succeeds.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (Math/sqrt 4) (catch Exception _ :err))"}}]}
```

### G11-14 record 5  •  form `(do "host stack traces leak through interop; learn to read them" :studied)`  •  expected `':studied'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was near the garden.

Sable the crow and Caw the crow alighted at the edge of the garden on the rim of an old
pitcher where someone had scratched the topic of debugging host-runtime leaks. Sable,
wide-eyed with fear, declared the answer beyond reach. Caw, patient as
ever, suggested they drop the form `(do "host stack traces leak through interop; learn to read them" :studied)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a form whose evaluation gives the marker for the host-leaks lesson.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"host stack traces leak through interop; learn to read them\" :studied)"}}]}
```

