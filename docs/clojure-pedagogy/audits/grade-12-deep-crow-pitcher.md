# crow-pitcher grade 12 — deep spot-check

5 records per subject for hand-audit.

---

## G12-01: Transducers introduction

### G12-01 record 1  •  form `(into [] (map inc) [1 2 3])`  •  expected `[2, 3, 4]`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Caw the crow and Korvus the crow alighted near the hilltop on the rim of an old
pitcher where someone had scratched the transducer (map inc) used via into. Caw,
with growing alarm, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(into [] (map inc) [1 2 3])` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a Clojure expression that computes [1 2 3] each incremented through a transducer.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
```

### G12-01 record 2  •  form `(into [] (filter even?) [1 2 3 4 5])`  •  expected `[2, 4]`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

"There is no need to evaluate that," Korvus the crow said, boasting at every turn.
"Anyone with a sharp eye can see what the transducer (filter even?) used via into comes to."
Caw the crow, who in the orchard had grown used to such claims, asked
him to actually write the form `(into [] (filter even?) [1 2 3 4 5])` and drop it
into the REPL — just to be sure.

Write a form whose evaluation gives the even elements via a filter transducer.

---

I let the REPL exercise the library form.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (filter even?) [1 2 3 4 5])"}}]}
```

### G12-01 record 3  •  form `(into [] (map inc) [1 2 3])`  •  expected `[2, 3, 4]`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place by the meadow.

A small audience of sparrows had gathered at the edge of the meadow to watch
Korvus the crow attempt to outwit Sable the crow at the rim of an old
pitcher. Sable pointed to the transducer (map inc) used via into and read out the form
aloud: `(into [] (map inc) [1 2 3])`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

What Clojure form computes [1 2 3] each incremented through a transducer? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
```

### G12-01 record 4  •  form `(into [] (filter even?) [1 2 3 4 5])`  •  expected `[2, 4]`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A small gathering at the end of the season at the edge of the garden brought together
every bird who'd ever foraged together. The day's discussion was
the transducer (filter even?) used via into. Caw wrote the form `(into [] (filter even?) [1 2 3 4 5])` on a square
of bark and passed it across; Sable, lulled by the gentle wind but pleased,
agreed to read it into the REPL.

Question: write a Clojure expression for the even elements via a filter transducer.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (filter even?) [1 2 3 4 5])"}}]}
```

### G12-01 record 5  •  form `(into [] (map inc) [1 2 3])`  •  expected `[2, 3, 4]`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust along the road: whoever guessed the result of `(into [] (map inc) [1 2 3])`
first would win the right to claim the next clear water they found.
Caw the crow, stepping deliberately, said it was easier to ask the REPL
about the transducer (map inc) used via into than to argue.

Write a Clojure expression that computes [1 2 3] each incremented through a transducer.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
```

## G12-02: Transducer composition

### G12-02 record 1  •  form `(into [] (comp (map inc) (filter even?)) [1 2 3 4])`  •  expected `[2, 4]`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. All this took place in the village.

The day's foraging had ended at the edge of the village and the two crows were perched
on a branch, comparing notes. Caw the crow sketched
the composed transducer (comp (map inc) (filter even?)) into the dust below. "We've come a long way,"
she said. "The form `(into [] (comp (map inc) (filter even?)) [1 2 3 4])` is the kind of thing
we'd reach for now." Sable nodded — for once lulled by the gentle wind enough
to listen.

Question: write a Clojure expression for the result of inc-then-keep-evens via a composed transducer.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (comp (map inc) (filter even?)) [1 2 3 4])"}}]}
```

### G12-02 record 2  •  form `(transduce (comp (map inc) (filter even?)) + 0 [1 2 3 4 5])`  •  expected `12`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Sable the crow and Caw the crow alighted at the edge of the orchard on the rim of an old
pitcher where someone had scratched transduce with a composed transducer summing the kept items. Sable,
with growing alarm, declared the answer beyond reach. Caw, patient as
ever, suggested they drop the form `(transduce (comp (map inc) (filter even?)) + 0 [1 2 3 4 5])` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a form whose evaluation gives the sum after inc-then-keep-evens via transduce.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(transduce (comp (map inc) (filter even?)) + 0 [1 2 3 4 5])"}}]}
```

### G12-02 record 3  •  form `(into [] (comp (map inc) (filter even?)) [1 2 3 4])`  •  expected `[2, 4]`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place along the road.

Sable the crow had been keeping a small leather notebook of every form
they had successfully dropped into the REPL — one entry per
stone, one rise per form. Today on the road, the next entry was
the composed transducer (comp (map inc) (filter even?)). Korvus the crow peered over their shoulder
at the form `(into [] (comp (map inc) (filter even?)) [1 2 3 4])` and asked what it would come out to.

Write a Clojure expression that computes the result of inc-then-keep-evens via a composed transducer.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (comp (map inc) (filter even?)) [1 2 3 4])"}}]}
```

### G12-02 record 4  •  form `(transduce (comp (map inc) (filter even?)) + 0 [1 2 3 4 5])`  •  expected `12`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Sable the crow, her legs heavy from sprinting from a season of flights, was finally
willing to study patterns. Caw the crow pointed in the market at
transduce with a composed transducer summing the kept items. The form `(transduce (comp (map inc) (filter even?)) + 0 [1 2 3 4 5])` was the canonical example;
the REPL would confirm what it produced.

Write a form whose evaluation gives the sum after inc-then-keep-evens via transduce.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(transduce (comp (map inc) (filter even?)) + 0 [1 2 3 4 5])"}}]}
```

### G12-02 record 5  •  form `(into [] (comp (map inc) (filter even?)) [1 2 3 4])`  •  expected `[2, 4]`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened at the edge of the hilltop.

Sable the crow and Korvus the crow alighted on the hilltop on the rim of an old
pitcher where someone had scratched the composed transducer (comp (map inc) (filter even?)). Sable,
her hands trembling, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(into [] (comp (map inc) (filter even?)) [1 2 3 4])` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

What Clojure form computes the result of inc-then-keep-evens via a composed transducer? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (comp (map inc) (filter even?)) [1 2 3 4])"}}]}
```

## G12-03: into with a transducer (xform)

### G12-03 record 1  •  form `(into #{} (map inc) [1 2 3])`  •  expected `{2, 3, 4}`

```
Hunger and thirst had driven the Crow far from her usual perch.

Sable the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," they said, pointing to into a set with the (map inc) transducer.
"You hand the form `(into #{} (map inc) [1 2 3])` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, with a thirst that hurt to bear, agreed to try.

What Clojure form computes the set produced by mapping inc into an empty set? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into #{} (map inc) [1 2 3])"}}]}
```

### G12-03 record 2  •  form `(into [] (take 3) (range 100))`  •  expected `[0, 1, 2]`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Caw the crow and Korvus the crow alighted near the garden on the rim of an old
pitcher where someone had scratched into [] with the (take 3) transducer over (range 100). Caw,
shouting until her voice cracked, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(into [] (take 3) (range 100))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a form whose evaluation gives the first three items collected through a transducer.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (take 3) (range 100))"}}]}
```

### G12-03 record 3  •  form `(into #{} (map inc) [1 2 3])`  •  expected `{2, 3, 4}`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Korvus the crow etched a wager along the rim of a chipped pitcher
along the road: whoever predicted the result of `(into #{} (map inc) [1 2 3])` first would set
the next day's foraging route. Sable the crow, without complaint, said it
would be simpler to drop the form into the REPL than to bicker about
into a set with the (map inc) transducer.

Question: write a Clojure expression for the set produced by mapping inc into an empty set.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(into #{} (map inc) [1 2 3])"}}]}
```

### G12-03 record 4  •  form `(into [] (take 3) (range 100))`  •  expected `[0, 1, 2]`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Caw the crow had been keeping a small leather notebook of every form
she had successfully dropped into the REPL — one entry per
stone, one rise per form. Today by the orchard, the next entry was
into [] with the (take 3) transducer over (range 100). Sable the crow peered over her shoulder
at the form `(into [] (take 3) (range 100))` and asked what it would come out to.

Write a form whose evaluation gives the first three items collected through a transducer.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (take 3) (range 100))"}}]}
```

### G12-03 record 5  •  form `(into #{} (map inc) [1 2 3])`  •  expected `{2, 3, 4}`

```
Hunger and thirst had driven the Crow far from her usual perch.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust in the market: whoever guessed the result of `(into #{} (map inc) [1 2 3])`
first would win the right to claim the next clear water they found.
Sable the crow, saying very little, said it was easier to ask the REPL
about into a set with the (map inc) transducer than to argue.

Question: write a Clojure expression for the set produced by mapping inc into an empty set.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into #{} (map inc) [1 2 3])"}}]}
```

## G12-04: core.async introduction

### G12-04 record 1  •  form `(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)`  •  expected `':studied'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened at the edge of the village.

At the edge of the orchard by the village, a row of small markers
commemorated the libraries the crows had learned along the way. The
newest one honoured the core.async primitives chan/go/<!/>!. Korvus the crow touched it
with a wing and said the form to remember was `(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)`;
Caw the crow agreed to submit it.

Write a Clojure expression that computes the marker for the core.async lesson.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(chan), (go ...), (<! ...), (>! ...) form the core.async core\" :studied)"}}]}
```

### G12-04 record 2  •  form `(do "go-blocks let you write async code as if it were synchronous" :async)`  •  expected `':async'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

"This isn't a quick trick," Korvus said, with steady, careful steps, at the edge of the hilltop.
"It's a tool." Caw the crow looked at what go blocks give you and
admitted she would not have known what to write. Korvus
sketched `(do "go-blocks let you write async code as if it were synchronous" :async)` on a slate so the runtime could speak for
itself.

What Clojure form computes the marker keyword for go-blocks? Submit it via `eval`.

---

I write the form using the appropriate library or tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"go-blocks let you write async code as if it were synchronous\" :async)"}}]}
```

### G12-04 record 3  •  form `(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)`  •  expected `':studied'`

```
Hunger and thirst had driven the Crow far from her usual perch.

Korvus the crow etched a wager along the rim of a chipped pitcher
in the market: whoever predicted the result of `(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)` first would set
the next day's foraging route. Sable the crow, with steady, careful steps, said it
would be simpler to drop the form into the REPL than to bicker about
the core.async primitives chan/go/<!/>!.

Write a form whose evaluation gives the marker for the core.async lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(chan), (go ...), (<! ...), (>! ...) form the core.async core\" :studied)"}}]}
```

### G12-04 record 4  •  form `(do "go-blocks let you write async code as if it were synchronous" :async)`  •  expected `':async'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A small gathering at the end of the season at the edge of the orchard brought together
every bird who'd ever foraged together. The day's discussion was
what go blocks give you. Sable wrote the form `(do "go-blocks let you write async code as if it were synchronous" :async)` on a square
of bark and passed it across; Korvus, her legs heavy from sprinting but pleased,
agreed to read it into the REPL.

Write a Clojure expression that computes the marker keyword for go-blocks.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"go-blocks let you write async code as if it were synchronous\" :async)"}}]}
```

### G12-04 record 5  •  form `(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)`  •  expected `':studied'`

```
Hunger and thirst had driven the Crow far from her usual perch.

Sable the crow etched a wager along the rim of a chipped pitcher
by the market: whoever predicted the result of `(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)` first would set
the next day's foraging route. Korvus the crow, saying very little, said it
would be simpler to drop the form into the REPL than to bicker about
the core.async primitives chan/go/<!/>!.

What Clojure form computes the marker for the core.async lesson? Submit it via `eval`.

---

I let the REPL exercise the library form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(chan), (go ...), (<! ...), (>! ...) form the core.async core\" :studied)"}}]}
```

## G12-05: Channels and pipelines

### G12-05 record 1  •  form `(do "pipe, mult, mix, pipeline-async route values across channels" :studied)`  •  expected `':studied'`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place at the edge of the hilltop.

A small gathering at the end of the season atop the hilltop brought together
every bird who'd ever foraged together. The day's discussion was
the pipeline operators in core.async. Sable wrote the form `(do "pipe, mult, mix, pipeline-async route values across channels" :studied)` on a square
of bark and passed it across; Caw, yawning at the soft moss but pleased,
agreed to read it into the REPL.

Write a Clojure expression that computes the marker for the channel-pipeline lesson.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"pipe, mult, mix, pipeline-async route values across channels\" :studied)"}}]}
```

### G12-05 record 2  •  form `(do "pipelines transform streams of values channel-to-channel" :pipelines)`  •  expected `':pipelines'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened at the edge of the market.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust in the market: whoever guessed the result of `(do "pipelines transform streams of values channel-to-channel" :pipelines)`
first would win the right to claim the next clear water they found.
Korvus the crow, stepping deliberately, said it was easier to ask the REPL
about the role of pipelines in async code than to argue.

Write a Clojure expression that computes the marker keyword for pipelines.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"pipelines transform streams of values channel-to-channel\" :pipelines)"}}]}
```

### G12-05 record 3  •  form `(do "pipe, mult, mix, pipeline-async route values across channels" :studied)`  •  expected `':studied'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was atop the hilltop.

A wooden sign nailed to a tree atop the hilltop carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do "pipe, mult, mix, pipeline-async route values across channels" :studied)`. Sable laughed, with great whoops of laughter, and declared it
too easy. Korvus said patiently that the only way to be sure of
the pipeline operators in core.async was to drop it into the REPL.

What Clojure form computes the marker for the channel-pipeline lesson? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"pipe, mult, mix, pipeline-async route values across channels\" :studied)"}}]}
```

### G12-05 record 4  •  form `(do "pipelines transform streams of values channel-to-channel" :pipelines)`  •  expected `':pipelines'`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place along the road.

Sable the crow had filled an entire notebook over the long thirsty
season with tools and patterns: transducers, channels, specs, tests.
near the road, the next entry was the role of pipelines in async code, and the form was
`(do "pipelines transform streams of values channel-to-channel" :pipelines)`. Caw the crow, as if the race were already won but more reflective than
usual, agreed to write the form into the REPL.

What Clojure form computes the marker keyword for pipelines? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"pipelines transform streams of values channel-to-channel\" :pipelines)"}}]}
```

### G12-05 record 5  •  form `(do "pipe, mult, mix, pipeline-async route values across channels" :studied)`  •  expected `':studied'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Korvus the crow and Sable the crow alighted by the farm on the rim of an old
pitcher where someone had scratched the pipeline operators in core.async. Korvus,
wide-eyed with fear, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(do "pipe, mult, mix, pipeline-async route values across channels" :studied)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a form whose evaluation gives the marker for the channel-pipeline lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"pipe, mult, mix, pipeline-async route values across channels\" :studied)"}}]}
```

## G12-06: clojure.spec

### G12-06 record 1  •  form `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))`  •  expected `True`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A small audience of sparrows had gathered by the farm to watch
Korvus the crow attempt to outwit Sable the crow at the rim of an old
pitcher. Sable pointed to (s/valid? int? 42) — a basic spec check and read out the form
aloud: `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

What Clojure form computes whether 42 conforms to the int? spec? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))"}}]}
```

### G12-06 record 2  •  form `(do (require '[clojure.spec.alpha :as s]) (s/valid? string? 42))`  •  expected `False`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

At a moss-flecked pitcher near the village, Korvus the crow sketched a small
wager: whoever guessed the result of `(do (require '[clojure.spec.alpha :as s]) (s/valid? string? 42))` first would drink
first when the water rose. Sable the crow, stepping deliberately, said it was
simpler to type the form into the REPL than to argue about
(s/valid? string? 42) — a failing spec check.

What Clojure form computes whether 42 conforms to the string? spec? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (require '[clojure.spec.alpha :as s]) (s/valid? string? 42))"}}]}
```

### G12-06 record 3  •  form `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))`  •  expected `True`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Caw the crow, yawning at the soft moss from a season of flights, was finally
willing to study patterns. Korvus the crow pointed in the village at
(s/valid? int? 42) — a basic spec check. The form `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))` was the canonical example;
the REPL would confirm what it produced.

What Clojure form computes whether 42 conforms to the int? spec? Submit it via `eval`.

---

I express the pipeline / spec / test as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))"}}]}
```

### G12-06 record 4  •  form `(do (require '[clojure.spec.alpha :as s]) (s/valid? string? 42))`  •  expected `False`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place near the hilltop.

A wooden sign nailed to a tree on the hilltop carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do (require '[clojure.spec.alpha :as s]) (s/valid? string? 42))`. Sable laughed, with a smug grin, and declared it
too easy. Caw said patiently that the only way to be sure of
(s/valid? string? 42) — a failing spec check was to drop it into the REPL.

Question: write a Clojure expression for whether 42 conforms to the string? spec.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (require '[clojure.spec.alpha :as s]) (s/valid? string? 42))"}}]}
```

### G12-06 record 5  •  form `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened near the road.

Korvus the crow had filled an entire notebook over the long thirsty
season with tools and patterns: transducers, channels, specs, tests.
near the road, the next entry was (s/valid? int? 42) — a basic spec check, and the form was
`(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))`. Caw the crow, puffed up with pride but more reflective than
usual, agreed to write the form into the REPL.

What Clojure form computes whether 42 conforms to the int? spec? Submit it via `eval`.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))"}}]}
```

## G12-07: Spec generators

### G12-07 record 1  •  form `(do "s/exercise produces sample inputs for a spec" :studied)`  •  expected `':studied'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Caw the crow had filled an entire notebook over the long thirsty
season with tools and patterns: transducers, channels, specs, tests.
at the edge of the hilltop, the next entry was what s/exercise does, and the form was
`(do "s/exercise produces sample inputs for a spec" :studied)`. Sable the crow, with great whoops of laughter but more reflective than
usual, agreed to write the form into the REPL.

Write a form whose evaluation gives the marker for the spec-generators lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"s/exercise produces sample inputs for a spec\" :studied)"}}]}
```

### G12-07 record 2  •  form `(do "spec generators turn specs into property-based test inputs" :gens)`  •  expected `':gens'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A wooden sign nailed to a tree near the hilltop carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do "spec generators turn specs into property-based test inputs" :gens)`. Korvus laughed, puffed up with pride, and declared it
too easy. Sable said patiently that the only way to be sure of
the role of spec generators was to drop it into the REPL.

Write a form whose evaluation gives the marker keyword for spec generators.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"spec generators turn specs into property-based test inputs\" :gens)"}}]}
```

### G12-07 record 3  •  form `(do "s/exercise produces sample inputs for a spec" :studied)`  •  expected `':studied'`

```
Hunger and thirst had driven the Crow far from her usual perch.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust near the farm: whoever guessed the result of `(do "s/exercise produces sample inputs for a spec" :studied)`
first would win the right to claim the next clear water they found.
Sable the crow, her eyes always on the path, said it was easier to ask the REPL
about what s/exercise does than to argue.

Write a form whose evaluation gives the marker for the spec-generators lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"s/exercise produces sample inputs for a spec\" :studied)"}}]}
```

### G12-07 record 4  •  form `(do "spec generators turn specs into property-based test inputs" :gens)`  •  expected `':gens'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Caw the crow had been keeping a small leather notebook of every form
she had successfully dropped into the REPL — one entry per
stone, one rise per form. Today near the orchard, the next entry was
the role of spec generators. Sable the crow peered over her shoulder
at the form `(do "spec generators turn specs into property-based test inputs" :gens)` and asked what it would come out to.

Write a Clojure expression that computes the marker keyword for spec generators.

---

I express the pipeline / spec / test as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"spec generators turn specs into property-based test inputs\" :gens)"}}]}
```

### G12-07 record 5  •  form `(do "s/exercise produces sample inputs for a spec" :studied)`  •  expected `':studied'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was in the market.

A small gathering at the end of the season at the edge of the market brought together
every bird who'd ever foraged together. The day's discussion was
what s/exercise does. Sable wrote the form `(do "s/exercise produces sample inputs for a spec" :studied)` on a square
of bark and passed it across; Caw, yawning at the soft moss but pleased,
agreed to read it into the REPL.

What Clojure form computes the marker for the spec-generators lesson? Submit it via `eval`.

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"s/exercise produces sample inputs for a spec\" :studied)"}}]}
```

## G12-08: clojure.test

### G12-08 record 1  •  form `(= (+ 1 2) 3)`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Caw the crow had been keeping a small leather notebook of every form
she had successfully dropped into the REPL — one entry per
stone, one rise per form. Today by the meadow, the next entry was
(= (+ 1 2) 3) — what an `is` would test. Sable the crow peered over her shoulder
at the form `(= (+ 1 2) 3)` and asked what it would come out to.

Write a Clojure expression that computes the truth value an `is` assertion would record.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(= (+ 1 2) 3)"}}]}
```

### G12-08 record 2  •  form `(do "(deftest …), (is …), (testing …) are the core test forms" :studied)`  •  expected `':studied'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Sable the crow had been keeping a small leather notebook of every form
they had successfully dropped into the REPL — one entry per
stone, one rise per form. Today at the edge of the meadow, the next entry was
the clojure.test core forms. Caw the crow peered over their shoulder
at the form `(do "(deftest …), (is …), (testing …) are the core test forms" :studied)` and asked what it would come out to.

Question: write a Clojure expression for the marker for the clojure.test lesson.

---

I express the pipeline / spec / test as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(deftest …), (is …), (testing …) are the core test forms\" :studied)"}}]}
```

### G12-08 record 3  •  form `(= (+ 1 2) 3)`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened near the road.

A wooden sign nailed to a tree near the road carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(= (+ 1 2) 3)`. Sable laughed, with a smug grin, and declared it
too easy. Caw said patiently that the only way to be sure of
(= (+ 1 2) 3) — what an `is` would test was to drop it into the REPL.

Write a Clojure expression that computes the truth value an `is` assertion would record.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(= (+ 1 2) 3)"}}]}
```

### G12-08 record 4  •  form `(do "(deftest …), (is …), (testing …) are the core test forms" :studied)`  •  expected `':studied'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

The day's foraging had ended by the farm and the two crows were perched
on a branch, comparing notes. Korvus the crow sketched
the clojure.test core forms into the dust below. "We've come a long way,"
he said. "The form `(do "(deftest …), (is …), (testing …) are the core test forms" :studied)` is the kind of thing
we'd reach for now." Caw nodded — for once weary from the morning's effort enough
to listen.

What Clojure form computes the marker for the clojure.test lesson? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(deftest …), (is …), (testing …) are the core test forms\" :studied)"}}]}
```

### G12-08 record 5  •  form `(= (+ 1 2) 3)`  •  expected `True`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A small audience of sparrows had gathered near the road to watch
Caw the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to (= (+ 1 2) 3) — what an `is` would test and read out the form
aloud: `(= (+ 1 2) 3)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives the truth value an `is` assertion would record.

---

{"tool_calls":[{"name":"eval","args":{"form":"(= (+ 1 2) 3)"}}]}
```

## G12-09: Test fixtures

### G12-09 record 1  •  form `(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)`  •  expected `':studied'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

A small audience of sparrows had gathered near the meadow to watch
Sable the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to use-fixtures and the fixture pattern and read out the form
aloud: `(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

What Clojure form computes the marker for the fixtures lesson? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(use-fixtures :each f) wraps every deftest in setup/teardown\" :studied)"}}]}
```

### G12-09 record 2  •  form `(do "fixtures provide setup/teardown around deftests" :fixtures)`  •  expected `':fixtures'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened at the edge of the orchard.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust near the orchard: whoever guessed the result of `(do "fixtures provide setup/teardown around deftests" :fixtures)`
first would win the right to claim the next clear water they found.
Caw the crow, saying very little, said it was easier to ask the REPL
about the purpose of fixtures than to argue.

What Clojure form computes the marker keyword for the fixture lesson? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"fixtures provide setup/teardown around deftests\" :fixtures)"}}]}
```

### G12-09 record 3  •  form `(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)`  •  expected `':studied'`

```
Hunger and thirst had driven the Crow far from her usual perch.

A small gathering at the end of the season on the road brought together
every bird who'd ever foraged together. The day's discussion was
use-fixtures and the fixture pattern. Caw wrote the form `(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)` on a square
of bark and passed it across; Sable, weary from the morning's effort but pleased,
agreed to read it into the REPL.

Question: write a Clojure expression for the marker for the fixtures lesson.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(use-fixtures :each f) wraps every deftest in setup/teardown\" :studied)"}}]}
```

### G12-09 record 4  •  form `(do "fixtures provide setup/teardown around deftests" :fixtures)`  •  expected `':fixtures'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A small gathering at the end of the season on the hilltop brought together
every bird who'd ever foraged together. The day's discussion was
the purpose of fixtures. Caw wrote the form `(do "fixtures provide setup/teardown around deftests" :fixtures)` on a square
of bark and passed it across; Korvus, drowsy from the warm sun but pleased,
agreed to read it into the REPL.

Write a form whose evaluation gives the marker keyword for the fixture lesson.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"fixtures provide setup/teardown around deftests\" :fixtures)"}}]}
```

### G12-09 record 5  •  form `(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)`  •  expected `':studied'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was at the edge of the farm.

Caw the crow had filled an entire notebook over the long thirsty
season with tools and patterns: transducers, channels, specs, tests.
by the farm, the next entry was use-fixtures and the fixture pattern, and the form was
`(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)`. Sable the crow, puffed up with pride but more reflective than
usual, agreed to write the form into the REPL.

Write a Clojure expression that computes the marker for the fixtures lesson.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(use-fixtures :each f) wraps every deftest in setup/teardown\" :studied)"}}]}
```

## G12-10: Property-based testing

### G12-10 record 1  •  form `(= (reverse (reverse [1 2 3])) [1 2 3])`  •  expected `True`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened at the edge of the orchard.

Caw the crow had been trying to teach Sable the crow how the REPL
works. "Look here," she said, pointing to the property that double-reverse is identity.
"You hand the form `(= (reverse (reverse [1 2 3])) [1 2 3])` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, near to giving up the search for water, agreed to try.

Write a Clojure expression that computes the truth value of the double-reverse property on [1 2 3].

---

{"tool_calls":[{"name":"eval","args":{"form":"(= (reverse (reverse [1 2 3])) [1 2 3])"}}]}
```

### G12-10 record 2  •  form `(do "test.check generates inputs and checks properties hold" :studied)`  •  expected `':studied'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened in the farm.

Sable the crow had filled an entire notebook over the long thirsty
season with tools and patterns: transducers, channels, specs, tests.
at the edge of the farm, the next entry was what test.check does, and the form was
`(do "test.check generates inputs and checks properties hold" :studied)`. Korvus the crow, with great whoops of laughter but more reflective than
usual, agreed to write the form into the REPL.

Write a Clojure expression that computes the marker for property-based testing.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"test.check generates inputs and checks properties hold\" :studied)"}}]}
```

### G12-10 record 3  •  form `(= (reverse (reverse [1 2 3])) [1 2 3])`  •  expected `True`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

The day's foraging had ended near the road and the two crows were perched
on a branch, comparing notes. Sable the crow sketched
the property that double-reverse is identity into the dust below. "We've come a long way,"
they said. "The form `(= (reverse (reverse [1 2 3])) [1 2 3])` is the kind of thing
we'd reach for now." Korvus nodded — for once yawning at the soft moss enough
to listen.

Write a Clojure expression that computes the truth value of the double-reverse property on [1 2 3].

---

I express the pipeline / spec / test as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(= (reverse (reverse [1 2 3])) [1 2 3])"}}]}
```

### G12-10 record 4  •  form `(do "test.check generates inputs and checks properties hold" :studied)`  •  expected `':studied'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened near the garden.

At a moss-flecked pitcher in the garden, Caw the crow sketched a small
wager: whoever guessed the result of `(do "test.check generates inputs and checks properties hold" :studied)` first would drink
first when the water rose. Sable the crow, saying very little, said it was
simpler to type the form into the REPL than to argue about
what test.check does.

Write a Clojure expression that computes the marker for property-based testing.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"test.check generates inputs and checks properties hold\" :studied)"}}]}
```

### G12-10 record 5  •  form `(= (reverse (reverse [1 2 3])) [1 2 3])`  •  expected `True`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened near the market.

"There is no need to evaluate that," Sable the crow said, with a smug grin.
"Anyone with a sharp eye can see what the property that double-reverse is identity comes to."
Korvus the crow, who at the edge of the market had grown used to such claims, asked
them to actually write the form `(= (reverse (reverse [1 2 3])) [1 2 3])` and drop it
into the REPL — just to be sure.

Question: write a Clojure expression for the truth value of the double-reverse property on [1 2 3].

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(= (reverse (reverse [1 2 3])) [1 2 3])"}}]}
```

## G12-11: Leiningen project.clj

### G12-11 record 1  •  form `(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)`  •  expected `':studied'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

A wooden sign nailed to a tree at the edge of the village carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)`. Sable laughed, puffed up with pride, and declared it
too easy. Caw said patiently that the only way to be sure of
the project.clj manifest for Leiningen was to drop it into the REPL.

Write a Clojure expression that computes the marker for the project.clj lesson.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"project.clj declares :dependencies, :main, :profiles for Leiningen\" :studied)"}}]}
```

### G12-11 record 2  •  form `(do "Leiningen reads project.clj at the project root" :lein)`  •  expected `':lein'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place on the hilltop.

A wooden sign nailed to a tree atop the hilltop carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do "Leiningen reads project.clj at the project root" :lein)`. Korvus laughed, with a smug grin, and declared it
too easy. Sable said patiently that the only way to be sure of
where Leiningen finds project.clj was to drop it into the REPL.

Write a Clojure expression that computes the marker keyword for the Leiningen lesson.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Leiningen reads project.clj at the project root\" :lein)"}}]}
```

### G12-11 record 3  •  form `(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)`  •  expected `':studied'`

```
Hunger and thirst had driven the Crow far from her usual perch.

Korvus the crow and Caw the crow alighted atop the hilltop on the rim of an old
pitcher where someone had scratched the project.clj manifest for Leiningen. Korvus,
shouting until her voice cracked, declared the answer beyond reach. Caw, patient as
ever, suggested they drop the form `(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a form whose evaluation gives the marker for the project.clj lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"project.clj declares :dependencies, :main, :profiles for Leiningen\" :studied)"}}]}
```

### G12-11 record 4  •  form `(do "Leiningen reads project.clj at the project root" :lein)`  •  expected `':lein'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Halfway through a long thirsty afternoon, Korvus the crow alighted
near the hilltop and refused to fly on until someone could prove what the form
`(do "Leiningen reads project.clj at the project root" :lein)` evaluated to. Korvus called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
where Leiningen finds project.clj into the REPL. Whatever rises is the answer."

What Clojure form computes the marker keyword for the Leiningen lesson? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Leiningen reads project.clj at the project root\" :lein)"}}]}
```

### G12-11 record 5  •  form `(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)`  •  expected `':studied'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Halfway through a long thirsty afternoon, Sable the crow alighted
by the village and refused to fly on until someone could prove what the form
`(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)` evaluated to. Sable called it impossible.
Korvus the crow, gliding down at an unhurried pace, simply said: "Drop
the project.clj manifest for Leiningen into the REPL. Whatever rises is the answer."

Question: write a Clojure expression for the marker for the project.clj lesson.

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"project.clj declares :dependencies, :main, :profiles for Leiningen\" :studied)"}}]}
```

## G12-12: deps.edn projects

### G12-12 record 1  •  form `(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)`  •  expected `':studied'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place by the market.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust by the market: whoever guessed the result of `(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)`
first would win the right to claim the next clear water they found.
Korvus the crow, without complaint, said it was easier to ask the REPL
about the deps.edn manifest for the Clojure CLI than to argue.

What Clojure form computes the marker for the deps.edn lesson? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"deps.edn declares :deps and :aliases for the Clojure CLI\" :studied)"}}]}
```

### G12-12 record 2  •  form `(do "deps.edn is read by the official `clj`/`clojure` tools" :deps)`  •  expected `':deps'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened on the road.

Korvus the crow etched a wager along the rim of a chipped pitcher
along the road: whoever predicted the result of `(do "deps.edn is read by the official `clj`/`clojure` tools" :deps)` first would set
the next day's foraging route. Caw the crow, untroubled by what others thought, said it
would be simpler to drop the form into the REPL than to bicker about
who reads deps.edn.

What Clojure form computes the marker keyword for the deps.edn lesson? Submit it via `eval`.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"deps.edn is read by the official `clj`/`clojure` tools\" :deps)"}}]}
```

### G12-12 record 3  •  form `(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)`  •  expected `':studied'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened near the hilltop.

"There is no need to evaluate that," Sable the crow said, with great whoops of laughter.
"Anyone with a sharp eye can see what the deps.edn manifest for the Clojure CLI comes to."
Korvus the crow, who atop the hilltop had grown used to such claims, asked
them to actually write the form `(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)` and drop it
into the REPL — just to be sure.

Write a Clojure expression that computes the marker for the deps.edn lesson.

---

I let each form raise the surface a little closer to the answer.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"deps.edn declares :deps and :aliases for the Clojure CLI\" :studied)"}}]}
```

### G12-12 record 4  •  form `(do "deps.edn is read by the official `clj`/`clojure` tools" :deps)`  •  expected `':deps'`

```
Hunger and thirst had driven the Crow far from her usual perch. This was by the garden.

"There is no need to evaluate that," Korvus the crow said, as if the race were already won.
"Anyone with a sharp eye can see what who reads deps.edn comes to."
Caw the crow, who by the garden had grown used to such claims, asked
him to actually write the form `(do "deps.edn is read by the official `clj`/`clojure` tools" :deps)` and drop it
into the REPL — just to be sure.

What Clojure form computes the marker keyword for the deps.edn lesson? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"deps.edn is read by the official `clj`/`clojure` tools\" :deps)"}}]}
```

### G12-12 record 5  •  form `(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)`  •  expected `':studied'`

```
Hunger and thirst had driven the Crow far from her usual perch.

A small audience of sparrows had gathered at the edge of the market to watch
Korvus the crow attempt to outwit Sable the crow at the rim of an old
pitcher. Sable pointed to the deps.edn manifest for the Clojure CLI and read out the form
aloud: `(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives the marker for the deps.edn lesson.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"deps.edn declares :deps and :aliases for the Clojure CLI\" :studied)"}}]}
```

## G12-13: Aliases and tools

### G12-13 record 1  •  form `(do "`clj -M:test` runs the :test alias from deps.edn" :studied)`  •  expected `':studied'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

At the edge of the orchard at the edge of the meadow, a row of small markers
commemorated the libraries the crows had learned along the way. The
newest one honoured the alias-execution pattern with the Clojure CLI. Korvus the crow touched it
with a wing and said the form to remember was `(do "`clj -M:test` runs the :test alias from deps.edn" :studied)`;
Sable the crow agreed to submit it.

Write a Clojure expression that computes the marker for the aliases lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"`clj -M:test` runs the :test alias from deps.edn\" :studied)"}}]}
```

### G12-13 record 2  •  form `(do "aliases compose extra paths, deps, and main opts" :aliases)`  •  expected `':aliases'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place by the market.

Korvus the crow, yawning at the soft moss from a season of flights, was finally
willing to study patterns. Caw the crow pointed near the market at
what aliases let you compose. The form `(do "aliases compose extra paths, deps, and main opts" :aliases)` was the canonical example;
the REPL would confirm what it produced.

Question: write a Clojure expression for the marker keyword for the aliases lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"aliases compose extra paths, deps, and main opts\" :aliases)"}}]}
```

### G12-13 record 3  •  form `(do "`clj -M:test` runs the :test alias from deps.edn" :studied)`  •  expected `':studied'`

```
Hunger and thirst had driven the Crow far from her usual perch.

A wooden sign nailed to a tree in the market carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do "`clj -M:test` runs the :test alias from deps.edn" :studied)`. Caw laughed, swaggering through the underbrush, and declared it
too easy. Korvus said patiently that the only way to be sure of
the alias-execution pattern with the Clojure CLI was to drop it into the REPL.

What Clojure form computes the marker for the aliases lesson? Submit it via `eval`.

---

I write the form using the appropriate library or tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"`clj -M:test` runs the :test alias from deps.edn\" :studied)"}}]}
```

### G12-13 record 4  •  form `(do "aliases compose extra paths, deps, and main opts" :aliases)`  •  expected `':aliases'`

```
Hunger and thirst had driven the Crow far from her usual perch.

A wooden sign nailed to a tree near the meadow carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do "aliases compose extra paths, deps, and main opts" :aliases)`. Caw laughed, as if the race were already won, and declared it
too easy. Korvus said patiently that the only way to be sure of
what aliases let you compose was to drop it into the REPL.

Write a Clojure expression that computes the marker keyword for the aliases lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"aliases compose extra paths, deps, and main opts\" :aliases)"}}]}
```

### G12-13 record 5  •  form `(do "`clj -M:test` runs the :test alias from deps.edn" :studied)`  •  expected `':studied'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

At the edge of the orchard by the meadow, a row of small markers
commemorated the libraries the crows had learned along the way. The
newest one honoured the alias-execution pattern with the Clojure CLI. Korvus the crow touched it
with a wing and said the form to remember was `(do "`clj -M:test` runs the :test alias from deps.edn" :studied)`;
Sable the crow agreed to submit it.

Write a form whose evaluation gives the marker for the aliases lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"`clj -M:test` runs the :test alias from deps.edn\" :studied)"}}]}
```

## G12-14: Pedestal / Ring (web stack brief)

### G12-14 record 1  •  form `(do "Ring models HTTP as request-map -> response-map" :studied)`  •  expected `':studied'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place by the orchard.

Halfway through a long thirsty afternoon, Sable the crow alighted
by the orchard and refused to fly on until someone could prove what the form
`(do "Ring models HTTP as request-map -> response-map" :studied)` evaluated to. Sable called it impossible.
Korvus the crow, gliding down at an unhurried pace, simply said: "Drop
the Ring HTTP-as-data abstraction into the REPL. Whatever rises is the answer."

Write a Clojure expression that computes the marker for the Ring lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Ring models HTTP as request-map -> response-map\" :studied)"}}]}
```

### G12-14 record 2  •  form `(do "Pedestal layers interceptors over Ring for richer pipelines" :web)`  •  expected `':web'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A small gathering at the end of the season near the orchard brought together
every bird who'd ever foraged together. The day's discussion was
the Pedestal interceptor model. Korvus wrote the form `(do "Pedestal layers interceptors over Ring for richer pipelines" :web)` on a square
of bark and passed it across; Sable, her legs heavy from sprinting but pleased,
agreed to read it into the REPL.

Write a form whose evaluation gives the marker keyword for the Pedestal lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Pedestal layers interceptors over Ring for richer pipelines\" :web)"}}]}
```

### G12-14 record 3  •  form `(do "Ring models HTTP as request-map -> response-map" :studied)`  •  expected `':studied'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was near the garden.

Sable the crow and Caw the crow alighted at the edge of the garden on the rim of an old
pitcher where someone had scratched the Ring HTTP-as-data abstraction. Sable,
wide-eyed with fear, declared the answer beyond reach. Caw, patient as
ever, suggested they drop the form `(do "Ring models HTTP as request-map -> response-map" :studied)` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a form whose evaluation gives the marker for the Ring lesson.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Ring models HTTP as request-map -> response-map\" :studied)"}}]}
```

### G12-14 record 4  •  form `(do "Pedestal layers interceptors over Ring for richer pipelines" :web)`  •  expected `':web'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

At the edge of the orchard near the farm, a row of small markers
commemorated the libraries the crows had learned along the way. The
newest one honoured the Pedestal interceptor model. Caw the crow touched it
with a wing and said the form to remember was `(do "Pedestal layers interceptors over Ring for richer pipelines" :web)`;
Korvus the crow agreed to submit it.

What Clojure form computes the marker keyword for the Pedestal lesson? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Pedestal layers interceptors over Ring for richer pipelines\" :web)"}}]}
```

### G12-14 record 5  •  form `(do "Ring models HTTP as request-map -> response-map" :studied)`  •  expected `':studied'`

```
Hunger and thirst had driven the Crow far from her usual perch.

Caw the crow etched a wager along the rim of a chipped pitcher
along the road: whoever predicted the result of `(do "Ring models HTTP as request-map -> response-map" :studied)` first would set
the next day's foraging route. Sable the crow, her eyes always on the path, said it
would be simpler to drop the form into the REPL than to bicker about
the Ring HTTP-as-data abstraction.

Write a form whose evaluation gives the marker for the Ring lesson.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Ring models HTTP as request-map -> response-map\" :studied)"}}]}
```

## G12-15: Datomic / XTDB (datalog db brief)

### G12-15 record 1  •  form `(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)`  •  expected `':studied'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A small audience of sparrows had gathered by the orchard to watch
Sable the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to the Datomic / XTDB family and read out the form
aloud: `(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives the marker for the datalog-DB lesson.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Datomic and XTDB are immutable, time-aware datalog DBs\" :studied)"}}]}
```

### G12-15 record 2  •  form `(do "queries are written in datalog over EDN-shaped data" :datalog)`  •  expected `':datalog'`

```
Hunger and thirst had driven the Crow far from her usual perch.

A small audience of sparrows had gathered atop the hilltop to watch
Caw the crow attempt to outwit Sable the crow at the rim of an old
pitcher. Sable pointed to how queries look in these databases and read out the form
aloud: `(do "queries are written in datalog over EDN-shaped data" :datalog)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives the marker keyword for datalog queries.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"queries are written in datalog over EDN-shaped data\" :datalog)"}}]}
```

### G12-15 record 3  •  form `(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)`  •  expected `':studied'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

At a moss-flecked pitcher by the meadow, Sable the crow sketched a small
wager: whoever guessed the result of `(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)` first would drink
first when the water rose. Korvus the crow, untroubled by what others thought, said it was
simpler to type the form into the REPL than to argue about
the Datomic / XTDB family.

Write a form whose evaluation gives the marker for the datalog-DB lesson.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Datomic and XTDB are immutable, time-aware datalog DBs\" :studied)"}}]}
```

### G12-15 record 4  •  form `(do "queries are written in datalog over EDN-shaped data" :datalog)`  •  expected `':datalog'`

```
Hunger and thirst had driven the Crow far from her usual perch.

"This isn't a quick trick," Korvus said, untroubled by what others thought, along the road.
"It's a tool." Sable the crow looked at how queries look in these databases and
admitted they would not have known what to write. Korvus
sketched `(do "queries are written in datalog over EDN-shaped data" :datalog)` on a slate so the runtime could speak for
itself.

Write a form whose evaluation gives the marker keyword for datalog queries.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"queries are written in datalog over EDN-shaped data\" :datalog)"}}]}
```

### G12-15 record 5  •  form `(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)`  •  expected `':studied'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. This was by the village.

"This isn't a quick trick," Sable said, with steady, careful steps, at the edge of the village.
"It's a tool." Korvus the crow looked at the Datomic / XTDB family and
admitted he would not have known what to write. Sable
sketched `(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)` on a slate so the runtime could speak for
itself.

Write a form whose evaluation gives the marker for the datalog-DB lesson.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Datomic and XTDB are immutable, time-aware datalog DBs\" :studied)"}}]}
```

## G12-16: Reagent (cljs UI brief)

### G12-16 record 1  •  form `(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)`  •  expected `':studied'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened at the edge of the hilltop.

Korvus the crow had filled an entire notebook over the long thirsty
season with tools and patterns: transducers, channels, specs, tests.
atop the hilltop, the next entry was the Reagent wrapper around React, and the form was
`(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)`. Sable the crow, with great whoops of laughter but more reflective than
usual, agreed to write the form into the REPL.

Write a form whose evaluation gives the marker for the Reagent lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Reagent wraps React with Hiccup-shaped Clojure data\" :studied)"}}]}
```

### G12-16 record 2  •  form `(do "components are functions returning Hiccup vectors" :reagent)`  •  expected `':reagent'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

"There is no need to evaluate that," Sable the crow said, with a smug grin.
"Anyone with a sharp eye can see what how Reagent components are written comes to."
Korvus the crow, who near the hilltop had grown used to such claims, asked
them to actually write the form `(do "components are functions returning Hiccup vectors" :reagent)` and drop it
into the REPL — just to be sure.

Write a Clojure expression that computes the marker keyword for Reagent components.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"components are functions returning Hiccup vectors\" :reagent)"}}]}
```

### G12-16 record 3  •  form `(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)`  •  expected `':studied'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened at the edge of the garden.

A wooden sign nailed to a tree by the garden carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)`. Caw laughed, boasting at every turn, and declared it
too easy. Sable said patiently that the only way to be sure of
the Reagent wrapper around React was to drop it into the REPL.

What Clojure form computes the marker for the Reagent lesson? Submit it via `eval`.

---

I let each form raise the surface a little closer to the answer.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Reagent wraps React with Hiccup-shaped Clojure data\" :studied)"}}]}
```

### G12-16 record 4  •  form `(do "components are functions returning Hiccup vectors" :reagent)`  •  expected `':reagent'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened near the village.

Sable the crow had been keeping a small leather notebook of every form
they had successfully dropped into the REPL — one entry per
stone, one rise per form. Today at the edge of the village, the next entry was
how Reagent components are written. Korvus the crow peered over their shoulder
at the form `(do "components are functions returning Hiccup vectors" :reagent)` and asked what it would come out to.

Question: write a Clojure expression for the marker keyword for Reagent components.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"components are functions returning Hiccup vectors\" :reagent)"}}]}
```

### G12-16 record 5  •  form `(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)`  •  expected `':studied'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A wooden sign nailed to a tree near the road carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)`. Korvus laughed, with great whoops of laughter, and declared it
too easy. Caw said patiently that the only way to be sure of
the Reagent wrapper around React was to drop it into the REPL.

Write a form whose evaluation gives the marker for the Reagent lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Reagent wraps React with Hiccup-shaped Clojure data\" :studied)"}}]}
```

## G12-17: Library design patterns

### G12-17 record 1  •  form `(do "good libraries expose data, then functions, then macros sparingly" :studied)`  •  expected `':studied'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

At a moss-flecked pitcher on the hilltop, Sable the crow sketched a small
wager: whoever guessed the result of `(do "good libraries expose data, then functions, then macros sparingly" :studied)` first would drink
first when the water rose. Korvus the crow, saying very little, said it was
simpler to type the form into the REPL than to argue about
the Clojure library-design hierarchy.

Write a form whose evaluation gives the marker for the library-design lesson.

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"good libraries expose data, then functions, then macros sparingly\" :studied)"}}]}
```

### G12-17 record 2  •  form `(do "small public API surface, plain data inputs, return values" :design)`  •  expected `':design'`

```
Hunger and thirst had driven the Crow far from her usual perch.

Caw the crow had filled an entire notebook over the long thirsty
season with tools and patterns: transducers, channels, specs, tests.
at the edge of the farm, the next entry was the conventional Clojure API shape, and the form was
`(do "small public API surface, plain data inputs, return values" :design)`. Korvus the crow, with a smug grin but more reflective than
usual, agreed to write the form into the REPL.

Write a Clojure expression that computes the marker keyword for the API-shape lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"small public API surface, plain data inputs, return values\" :design)"}}]}
```

### G12-17 record 3  •  form `(= [1 2 3] (vec '(1 2 3)))`  •  expected `True`

```
Hunger and thirst had driven the Crow far from her usual perch. It happened at the edge of the garden.

A small gathering at the end of the season by the garden brought together
every bird who'd ever foraged together. The day's discussion was
a tiny example of a data-first conversion at the API edge. Sable wrote the form `(= [1 2 3] (vec '(1 2 3)))` on a square
of bark and passed it across; Korvus, lulled by the gentle wind but pleased,
agreed to read it into the REPL.

What Clojure form computes whether the vector and the converted seq are equal? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(= [1 2 3] (vec '(1 2 3)))"}}]}
```

### G12-17 record 4  •  form `(do "good libraries expose data, then functions, then macros sparingly" :studied)`  •  expected `':studied'`

```
Hunger and thirst had driven the Crow far from her usual perch.

The day's foraging had ended on the road and the two crows were perched
on a branch, comparing notes. Sable the crow sketched
the Clojure library-design hierarchy into the dust below. "We've come a long way,"
they said. "The form `(do "good libraries expose data, then functions, then macros sparingly" :studied)` is the kind of thing
we'd reach for now." Caw nodded — for once drowsy from the warm sun enough
to listen.

What Clojure form computes the marker for the library-design lesson? Submit it via `eval`.

---

I let the REPL exercise the library form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"good libraries expose data, then functions, then macros sparingly\" :studied)"}}]}
```

### G12-17 record 5  •  form `(do "small public API surface, plain data inputs, return values" :design)`  •  expected `':design'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was near the village.

At a moss-flecked pitcher near the village, Caw the crow sketched a small
wager: whoever guessed the result of `(do "small public API surface, plain data inputs, return values" :design)` first would drink
first when the water rose. Korvus the crow, stepping deliberately, said it was
simpler to type the form into the REPL than to argue about
the conventional Clojure API shape.

Write a Clojure expression that computes the marker keyword for the API-shape lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"small public API surface, plain data inputs, return values\" :design)"}}]}
```

## G12-18: Clojure style guide

### G12-18 record 1  •  form `(do "kebab-case names, two-space indent, threading for deep nests" :studied)`  •  expected `':studied'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Korvus the crow etched a wager along the rim of a chipped pitcher
near the market: whoever predicted the result of `(do "kebab-case names, two-space indent, threading for deep nests" :studied)` first would set
the next day's foraging route. Caw the crow, untroubled by what others thought, said it
would be simpler to drop the form into the REPL than to bicker about
the community-style basics.

What Clojure form computes the marker for the style-guide lesson? Submit it via `eval`.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"kebab-case names, two-space indent, threading for deep nests\" :studied)"}}]}
```

### G12-18 record 2  •  form `(do "prefer pure functions, name predicates with ?, danger! ops with !" :style)`  •  expected `':style'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was atop the hilltop.

At the edge of the orchard at the edge of the hilltop, a row of small markers
commemorated the libraries the crows had learned along the way. The
newest one honoured two naming conventions from the style guide. Sable the crow touched it
with a wing and said the form to remember was `(do "prefer pure functions, name predicates with ?, danger! ops with !" :style)`;
Korvus the crow agreed to submit it.

Write a form whose evaluation gives the marker keyword for the naming-conventions lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"prefer pure functions, name predicates with ?, danger! ops with !\" :style)"}}]}
```

### G12-18 record 3  •  form `(do "kebab-case names, two-space indent, threading for deep nests" :studied)`  •  expected `':studied'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened near the orchard.

A small gathering at the end of the season at the edge of the orchard brought together
every bird who'd ever foraged together. The day's discussion was
the community-style basics. Sable wrote the form `(do "kebab-case names, two-space indent, threading for deep nests" :studied)` on a square
of bark and passed it across; Korvus, drowsy from the warm sun but pleased,
agreed to read it into the REPL.

Question: write a Clojure expression for the marker for the style-guide lesson.

---

I let each form raise the surface a little closer to the answer.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"kebab-case names, two-space indent, threading for deep nests\" :studied)"}}]}
```

### G12-18 record 4  •  form `(do "prefer pure functions, name predicates with ?, danger! ops with !" :style)`  •  expected `':style'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened at the edge of the meadow.

At a moss-flecked pitcher at the edge of the meadow, Caw the crow sketched a small
wager: whoever guessed the result of `(do "prefer pure functions, name predicates with ?, danger! ops with !" :style)` first would drink
first when the water rose. Sable the crow, with steady, careful steps, said it was
simpler to type the form into the REPL than to argue about
two naming conventions from the style guide.

Write a form whose evaluation gives the marker keyword for the naming-conventions lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"prefer pure functions, name predicates with ?, danger! ops with !\" :style)"}}]}
```

### G12-18 record 5  •  form `(do "kebab-case names, two-space indent, threading for deep nests" :studied)`  •  expected `':studied'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

A wooden sign nailed to a tree in the market carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do "kebab-case names, two-space indent, threading for deep nests" :studied)`. Korvus laughed, puffed up with pride, and declared it
too easy. Sable said patiently that the only way to be sure of
the community-style basics was to drop it into the REPL.

What Clojure form computes the marker for the style-guide lesson? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"kebab-case names, two-space indent, threading for deep nests\" :studied)"}}]}
```

